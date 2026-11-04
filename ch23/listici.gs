// Trideset listića: predložak, robusna petlja i pomoćne funkcije.
// Treba: pitajModel.gs i shema.gs u istom projektu; listove "ucenici",
// "predlozak" (predložak u ćeliji A1) i "zapisnik"; prazan Google dokument.
// List "ucenici": šifra, staza, interes, status, poslano (stupci A-E).

const ISHOD = '[ISHOD IZ KURIKULA, DOSLOVNO]';
const STAZE = {
  A: 'Prvi zadatak je razrađen primjer, ostali su vođeni koracima.',
  B: 'Vođeni pa samostalni zadaci.',
  C: 'Otvoreni problemi iz stvarnog života; jedan traži objašnjenje.'
};
const DOKUMENT_ID = '[ID PRAZNOG DOKUMENTA]';
// red = [šifra, staza, interes, status, poslano]
function popuni_(predlozak, red) {
  return predlozak
    .split('{{staza}}').join(red[1])
    .split('{{opis_staze}}').join(STAZE[red[1]])
    .split('{{interes}}').join(red[2])
    .split('{{ishod}}').join(ISHOD);  // red[0] ne ide van
}

const GRANICA_USD = 0.20;          // vaša granica za cijeli tok
const SERIJA_MS = 4.5 * 60 * 1000; // stati prije 6 minuta

function obradiRazred() {
  const pocetak = Date.now();
  const knj = SpreadsheetApp.getActive();
  const tab = knj.getSheetByName('ucenici');
  const redovi = tab.getDataRange().getValues();
  const predlozak = knj.getSheetByName('predlozak')
    .getRange('A1').getValue();
  const sv = PropertiesService.getScriptProperties();
  let ukupno = Number(sv.getProperty('UKUPNO_USD') || 0);
  for (let r = 1; r < redovi.length; r++) {
    const [sifra, , , status] = redovi[r];
    if (status !== '' && status !== 'čeka') continue;
    if (Date.now() - pocetak > SERIJA_MS)
      return zakaziNastavak_();
    if (ukupno >= GRANICA_USD)
      return zapisi_(sifra, null, 'STOP: granica troška');
    const upit = popuni_(predlozak, redovi[r]);
    const poslano = tab.getRange(r + 1, 5);
    let odg = pozoviUporno_(upit, sifra, poslano);
    let p = provjeri_(odg);
    if (odg.kod === 200 && !p.listic) {   // jedan popravak
      ukupno += odg.usd;
      zapisi_(sifra, odg, 'shema: ' + p.razlog);
      odg = pozoviUporno_(upit + '\nPrethodni odgovor ' +
        'nije valjao: ' + p.razlog, sifra, poslano);
      p = provjeri_(odg);
    }
    ukupno += odg.usd;
    sv.setProperty('UKUPNO_USD', String(ukupno));
    if (p.listic) dodajListic_(sifra, p.listic);
    tab.getRange(r + 1, 4)
      .setValue(p.listic ? 'gotovo' : 'pogreška');
    zapisi_(sifra, odg, p.listic ? '' : p.razlog);
  }
  dodajStraniceZaUcitelja_();          // rješenja na kraj, samo nova
}

// Ponovni pokušaji: na 429 i 5xx čeka 4, 8 i 16 sekundi, najviše tri
// puta; ostale kodove vraća odmah.
function pozoviUporno_(upit, sifra, celijaPoslano) {
  let odg;
  for (let pokusaj = 0; pokusaj <= 3; pokusaj++) {
    if (pokusaj > 0)   // čekanje 4, 8, 16 sekundi
      Utilities.sleep(2000 * Math.pow(2, pokusaj));
    celijaPoslano.setValue(new Date());
    odg = pitajModel(upit, SHEMA_LISTICA);
    if (odg.kod !== 429 && odg.kod < 500) return odg;
    zapisi_(sifra, odg, odg.kod + ', novi pokušaj');
  }
  return odg;
}

// Provjera listića samo kad je poziv uspio; inače razlog iz koda.
function provjeri_(odg) {
  if (odg.kod !== 200)
    return { razlog: 'kod ' + odg.kod + (odg.greska ? ': ' + odg.greska : '') };
  return provjeriListic_(odg.tekst);
}

// Nastavak za minutu. Najprije briše stari okidač za istu funkciju, da se
// ne nakupe okidači koji istu skriptu pokreću jedan preko drugoga.
function zakaziNastavak_(funkcija) {
  const ime = funkcija || 'obradiRazred';
  ScriptApp.getProjectTriggers()
    .filter(function (t) { return t.getHandlerFunction() === ime; })
    .forEach(function (t) { ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger(ime).timeBased().after(60 * 1000).create();
  zapisi_('', null, 'serija je stala nakon 4,5 minute; nastavak za minutu');
}

// List "zapisnik": vrijeme, šifra, ulaz, izlaz, USD, napomena.
function zapisi_(sifra, odg, napomena) {
  const knj = SpreadsheetApp.getActive();
  const list = knj.getSheetByName('zapisnik') || knj.insertSheet('zapisnik');
  if (list.getLastRow() === 0)
    list.appendRow(['vrijeme', 'šifra', 'ulaz', 'izlaz', 'USD', 'napomena']);
  list.appendRow([new Date(), sifra,
    odg ? odg.ulaz : 0, odg ? odg.izlaz : 0,
    odg ? Math.round(odg.usd * 10000) / 10000 : 0, napomena || '']);
}

// Listić na novu stranicu dokumenta, sa šifrom na vrhu. Rješenja idu na
// zaseban list "rjesenja", a na kraj dokumenta ih dodaje
// dodajStraniceZaUcitelja_, kad prođu svi retci.
function dodajListic_(sifra, listic) {
  const tijelo = DocumentApp.openById(DOKUMENT_ID).getBody();
  if (tijelo.getText().trim() !== '') tijelo.appendPageBreak();
  tijelo.appendParagraph(sifra).editAsText().setFontSize(9);
  tijelo.appendParagraph(listic.naslov)
    .setHeading(DocumentApp.ParagraphHeading.HEADING1);
  tijelo.appendParagraph(listic.uvod).editAsText().setItalic(true);
  const knj = SpreadsheetApp.getActive();
  let rj = knj.getSheetByName('rjesenja');
  if (!rj) {
    rj = knj.insertSheet('rjesenja');
    rj.appendRow(['šifra', 'zadatak', 'razina', 'rješenje', 'u dokumentu']);
  }
  listic.zadaci.forEach(function (z, i) {
    tijelo.appendParagraph((i + 1) + '. (' + z.razina + ') ' + z.tekst);
    rj.appendRow([sifra, i + 1, z.razina, z.rjesenje, '']);
  });
}

// Stranice za učitelja s rješenjima: dodaje samo retke lista "rjesenja"
// koji još nisu u dokumentu, pa ponovno pokretanje ništa ne udvostručuje.
function dodajStraniceZaUcitelja_() {
  const list = SpreadsheetApp.getActive().getSheetByName('rjesenja');
  if (!list || list.getLastRow() < 2) return;
  const redovi = list.getDataRange().getValues();
  const nova = [];
  for (let r = 1; r < redovi.length; r++) if (!redovi[r][4]) nova.push(r);
  if (nova.length === 0) return;
  const tijelo = DocumentApp.openById(DOKUMENT_ID).getBody();
  tijelo.appendPageBreak();
  tijelo.appendParagraph('Rješenja (za učitelja)')
    .setHeading(DocumentApp.ParagraphHeading.HEADING1);
  let zadnja = '';
  nova.forEach(function (r) {
    const [sifra, broj, razina, rjesenje] = redovi[r];
    if (sifra !== zadnja) {
      tijelo.appendParagraph(String(sifra))
        .setHeading(DocumentApp.ParagraphHeading.HEADING2);
      zadnja = sifra;
    }
    tijelo.appendParagraph(broj + '. (' + razina + ') ' + rjesenje);
    list.getRange(r + 1, 5).setValue(new Date());
  });
}

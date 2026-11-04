// Nacrti povratne informacije prema rubrici (odjeljak „Sto dvadeset
// nacrta povratne informacije“). Ista robusna petlja kao obradiRazred,
// s drugom shemom. Treba: pitajModel.gs, listici.gs (zakaziNastavak_,
// zapisi_, SERIJA_MS) i listove "radovi",
// "predlozak_povratna" (upit u ćeliji A1), "zapisnik" i, za slanje, "adrese".
// List "radovi", stupci A-H: šifra, tekst rada, status, nacrt, konačno,
// odobreno, poslano, predano.
// Za stvarne radove samo odobreni put škole (školski ugovoreni alat ili
// lokalni model); za učenje izmišljena izvješća iz spremišta.

const RUBRIKA = [
  '- Opis postupka: učenik svojim riječima opisuje što je radio.',
  '- Redoslijed koraka: koraci su navedeni redom kojim su izvedeni.',
  '- Sigurnost na radu: navodi mjere zaštite prije i tijekom rada.',
  '- Poteškoće i rješenje: opisuje što je bilo teško i kako je to riješio.',
  'Razine za svaki kriterij: početna, razvojna, ostvarena.'
].join('\n');
const RAZINE = ['početna', 'razvojna', 'ostvarena'];
const GRANICA_USD_RADOVI = 0.20;     // granica za ovaj tok, odvojena od listića

const SHEMA_POVRATNE = {
  type: 'object',
  properties: {
    kriteriji: {
      type: 'array', minItems: 4, maxItems: 4,
      description: 'Jedan element za svaki redak rubrike, istim redom',
      items: {
        type: 'object',
        properties: {
          kriterij: { type: 'string', description: 'Naziv kriterija iz rubrike' },
          razina:   { type: 'string', enum: RAZINE },
          dokaz:    { type: 'string',
            description: 'Kratak doslovni citat iz rada ili "nema dokaza"' }
        },
        required: ['kriterij', 'razina', 'dokaz'],
        additionalProperties: false
      }
    },
    dobro:          { type: 'string', description: 'Što je dobro, jedna ili dvije rečenice' },
    poboljsati:     { type: 'string', description: 'Što poboljšati, jedna ili dvije rečenice' },
    sljedeci_korak: { type: 'string', description: 'Jedan konkretan sljedeći korak' }
  },
  required: ['kriteriji', 'dobro', 'poboljsati', 'sljedeci_korak'],
  additionalProperties: false
};

// red = [šifra, tekst rada, ...]; šifra (red[0]) ne ide van.
function popuniPovratnu_(predlozak, red) {
  return predlozak
    .split('{{rubrika}}').join(RUBRIKA)
    .split('{{tekst_rada}}').join(String(red[1]));
}

function brojKriterija_() {
  return RUBRIKA.split('\n').filter(function (r) {
    return r.indexOf('- ') === 0; }).length;
}

// Za usporedbu citata: mala slova, bez navodnika, jedan razmak.
function normaliziraj_(t) {
  return String(t).toLowerCase().replace(/[„“”"'’‘«»]/g, '')
    .replace(/\s+/g, ' ').trim();
}

// Ono što shema ne može: broj kriterija jednak rubrici i svaki citat
// doista u radu. Vraća { povratna } ili { razlog }.
function provjeriPovratnu_(odg, rad) {
  if (odg.kod !== 200)
    return { razlog: 'kod ' + odg.kod + (odg.greska ? ': ' + odg.greska : '') };
  let o;
  try { o = JSON.parse(odg.tekst); }
  catch (e) { return { razlog: 'odgovor nije JSON' }; }
  if (!Array.isArray(o.kriteriji) || o.kriteriji.length !== brojKriterija_())
    return { razlog: 'broj kriterija nije jednak broju redaka rubrike' };
  for (const k of o.kriteriji) {
    if (RAZINE.indexOf(k.razina) < 0)
      return { razlog: 'nepoznata razina: ' + k.razina };
    const dokaz = normaliziraj_(k.dokaz).replace(/^\.+|\.+$/g, '');
    if (dokaz !== 'nema dokaza' && normaliziraj_(rad).indexOf(dokaz) < 0)
      return { razlog: 'citat nije u radu: ' + String(k.dokaz).slice(0, 40) };
  }
  if (!o.dobro || !o.poboljsati || !o.sljedeci_korak)
    return { razlog: 'nedostaje korak povratne informacije' };
  return { povratna: o };
}

// Nacrt za stupac "nacrt": tri koraka, a ispod razine s dokazima.
function nacrtIzPovratne_(o) {
  return 'Što je dobro: ' + o.dobro + '\nŠto poboljšati: ' + o.poboljsati +
    '\nSljedeći korak: ' + o.sljedeci_korak + '\n---\n' +
    o.kriteriji.map(function (k) {
      return k.kriterij + ': ' + k.razina + ' („' + k.dokaz + '“)';
    }).join('\n');
}

// Isti ponovni pokušaji kao pozoviUporno_ u listici.gs (4, 8, 16 s na 429
// i 5xx), ali sa shemom povratne informacije i bez stupca "poslano":
// u listu "radovi" taj stupac znači slanje učeniku, a ne poziv modelu.
function pozoviUpornoPovratna_(upit, sifra) {
  let odg;
  for (let pokusaj = 0; pokusaj <= 3; pokusaj++) {
    if (pokusaj > 0)   // čekanje 4, 8, 16 sekundi
      Utilities.sleep(2000 * Math.pow(2, pokusaj));
    odg = pitajModel(upit, SHEMA_POVRATNE);
    if (odg.kod !== 429 && odg.kod < 500) return odg;
    zapisi_(sifra, odg, odg.kod + ', novi pokušaj');
  }
  return odg;
}

function obradiRadove() {
  const pocetak = Date.now();
  const knj = SpreadsheetApp.getActive();
  const tab = knj.getSheetByName('radovi');
  const redovi = tab.getDataRange().getValues();
  const predlozak = knj.getSheetByName('predlozak_povratna')
    .getRange('A1').getValue();
  const sv = PropertiesService.getScriptProperties();
  let ukupno = Number(sv.getProperty('UKUPNO_USD_RADOVI') || 0);
  for (let r = 1; r < redovi.length; r++) {
    const [sifra, rad, status] = redovi[r];
    if (status !== '' && status !== 'čeka') continue;
    if (!String(rad).trim()) continue;              // prazan redak
    if (Date.now() - pocetak > SERIJA_MS)
      return zakaziNastavak_('obradiRadove');
    if (ukupno >= GRANICA_USD_RADOVI)
      return zapisi_(sifra, null, 'STOP: granica troška');
    const upit = popuniPovratnu_(predlozak, redovi[r]);
    let odg = pozoviUpornoPovratna_(upit, sifra);
    let p = provjeriPovratnu_(odg, rad);
    if (odg.kod === 200 && !p.povratna) {            // jedan popravak
      ukupno += odg.usd;
      zapisi_(sifra, odg, 'provjera: ' + p.razlog);
      odg = pozoviUpornoPovratna_(upit + '\nPrethodni odgovor nije valjao: ' +
        p.razlog, sifra);
      p = provjeriPovratnu_(odg, rad);
    }
    ukupno += odg.usd;
    sv.setProperty('UKUPNO_USD_RADOVI', String(ukupno));
    if (p.povratna) tab.getRange(r + 1, 4).setValue(nacrtIzPovratne_(p.povratna));
    tab.getRange(r + 1, 3).setValue(p.povratna ? 'gotovo' : 'pogreška');
    zapisi_(sifra, odg, p.povratna ? '' : p.razlog);
  }
}

// Slanje: samo retci s DA u stupcu "odobreno", praznim "poslano" i
// napisanim konačnim tekstom. Šalje se KONAČNI tekst, nikad nacrt.
function posaljiOdobreneRadove() {
  const knj = SpreadsheetApp.getActive();
  const adrese = {};                                  // šifra -> adresa
  knj.getSheetByName('adrese').getDataRange().getValues()
    .forEach(function (a) { adrese[a[0]] = a[1]; });
  const tab = knj.getSheetByName('radovi');
  const redovi = tab.getDataRange().getValues();
  for (let r = 1; r < redovi.length; r++) {
    const [sifra, , , , konacno, odobreno, poslano] = redovi[r];
    const da = String(odobreno).trim().toUpperCase() === 'DA';
    if (!da || poslano || !String(konacno).trim()) continue;
    const adresa = adrese[sifra];
    if (!adresa) { Logger.log('Nema adrese: ' + sifra); continue; }
    if (MailApp.getRemainingDailyQuota() < 1) {
      Logger.log('Kvota je potrošena.'); return;
    }
    MailApp.sendEmail(adresa, 'Povratna informacija: izvješće s prakse',
      String(konacno));
    tab.getRange(r + 1, 7).setValue(new Date());
  }
}

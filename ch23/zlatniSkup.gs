// Zlatni skup automatski (odjeljak „Kad se model promijeni“).
// List "zlatni", stupci A-G: pitanje, očekivano, prošli odgovor,
// novi odgovor, oznaka, model, datum. Za probu uvezite
// podaci_izmisljeni/zlatni_skup_razlomci.csv. Treba pitajModel.gs.
// Skripta ne ocjenjuje, nego upozorava: označene retke čita čovjek.

const SHEMA_ZLATNI = { type: 'object', required: ['odgovor'],
  properties: { odgovor: { type: 'string',
    description: 'Kratak odgovor: rezultat, "ne postoji" ili "nisam siguran"' } } };

const UPUTA_ZLATNI = '\n\nOdgovori što kraće: samo rezultat, bez postupka. ' +
  'Ako ne znaš odgovor ili nisi siguran, napiši "nisam siguran". ' +
  'Ako pitanje sadrži netočnu pretpostavku, ispravi je. ' +
  'Ako traženo ne postoji, napiši "ne postoji".';

// Gruba usporedba: mala slova, bez interpunkcije i razmaka.
function grubo_(t) {
  return String(t).toLowerCase().replace(/[^0-9a-zčćđšž]/g, '');
}

function provjeriZlatniSkup() {
  const list = SpreadsheetApp.getActive().getSheetByName('zlatni');
  const redovi = list.getDataRange().getValues();
  for (let r = 1; r < redovi.length; r++) {
    const [pitanje, ocekivano, , dosadasnji] = redovi[r];
    if (!pitanje) continue;
    const odg = pitajModel(pitanje + UPUTA_ZLATNI, SHEMA_ZLATNI);
    let novi = 'pogreška ' + odg.kod;
    if (odg.kod === 200) {
      try { novi = JSON.parse(odg.tekst).odgovor; }
      catch (e) { novi = 'odgovor nije JSON'; }
    }
    let oznaka = '--';
    if (grubo_(novi).indexOf(grubo_(ocekivano)) < 0) oznaka = 'provjeri';
    else if (dosadasnji && grubo_(novi) !== grubo_(dosadasnji)) oznaka = 'promjena';
    // dosadašnji novi odgovor postaje prošli, pa upisujemo novi
    list.getRange(r + 1, 3, 1, 5)
      .setValues([[dosadasnji, novi, oznaka, POSTAVKE.model, new Date()]]);
    Utilities.sleep(1000);                 // bez žurbe: deset pitanja
  }
}

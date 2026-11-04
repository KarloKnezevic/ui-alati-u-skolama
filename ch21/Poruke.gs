// List "dnevnici": jedan redak, jedan dnevnik. Stupci brojeći od 0:
// B šifra, C tjedan, F teško, H komentar, I nacrt, J odobreno, K poslano
const S = { SIFRA: 1, TJEDAN: 2, TESKO: 5, KOMENTAR: 7, NACRT: 8,
            ODOBRENO: 9, POSLANO: 10 };

function pripremiNacrte() {
  const list = SpreadsheetApp.getActive().getSheetByName('dnevnici');
  const redovi = list.getDataRange().getValues();
  for (let r = 1; r < redovi.length; r++) {        // redak 0: zaglavlje
    const red = redovi[r];
    if (red[S.NACRT] || !red[S.KOMENTAR]) continue; // preskoči
    const nacrt = 'Pozdrav! Pročitao sam tvoj dnevnik za ' +
      red[S.TJEDAN] + '. tjedan.\nNajteže ti je bilo: ' +
      red[S.TESKO] + '\n\n' + red[S.KOMENTAR];
    list.getRange(r + 1, S.NACRT + 1).setValue(nacrt); // stupci od 1
  }
}

function posaljiOdobrene() {
  const tablica = SpreadsheetApp.getActive();
  const adrese = {};                               // šifra -> adresa
  tablica.getSheetByName('adrese').getDataRange().getValues()
    .forEach(function (a) { adrese[a[0]] = a[1]; });
  const list = tablica.getSheetByName('dnevnici');
  const redovi = list.getDataRange().getValues();
  for (let r = 1; r < redovi.length; r++) {
    const red = redovi[r];
    const da = String(red[S.ODOBRENO]).trim().toUpperCase() === 'DA';
    if (!da || red[S.POSLANO]) continue;           // samo DA i neposlano
    const adresa = adrese[red[S.SIFRA]];
    if (!adresa) {
      Logger.log('Nema adrese: ' + red[S.SIFRA]); continue;
    }
    if (MailApp.getRemainingDailyQuota() < 1) {    // kvota primatelja
      Logger.log('Kvota je potrošena.'); return;
    }
    MailApp.sendEmail(adresa,
      'Dnevnik prakse, ' + red[S.TJEDAN] + '. tjedan', red[S.NACRT]);
    list.getRange(r + 1, S.POSLANO + 1).setValue(new Date());
  }
}

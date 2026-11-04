// Nacrti poruka iz lista "dnevnici"; stupce traži po nazivu iz prvog
// retka, pa novi stupac u obrascu ne pomiče ništa. Ništa ne šalje.
function pripremiNacrte() {
  const list = SpreadsheetApp.getActive().getSheetByName('dnevnici');
  const podaci = list.getDataRange().getValues();
  const zaglavlje = podaci[0];               // prvi redak: nazivi
  const stSifra = zaglavlje.indexOf('šifra');
  // Uzrok pogreške [DATUM]: stupac je preimenovan iz "sigurnosna
  // napomena" u "Sigurnost", pa je indexOf vraćao -1.
  const stNapomena = zaglavlje.indexOf('Sigurnost');
  if (stNapomena === -1)
    throw new Error('Nema stupca „Sigurnost“ u listu dnevnici.');
  const stNacrt = zaglavlje.indexOf('nacrt');
  if (stSifra === -1 || stNacrt === -1)
    throw new Error('Nema stupca „šifra“ ili „nacrt“ u listu dnevnici.');
  for (let r = 1; r < podaci.length; r++) {  // od drugog retka
    const napomena = String(podaci[r][stNapomena]).trim();
    const nacrt = 'Pregledao sam dnevnik (' + podaci[r][stSifra] +
      '). Sigurnosna napomena: ' + napomena;
    list.getRange(r + 1, stNacrt + 1).setValue(nacrt);
  }
}

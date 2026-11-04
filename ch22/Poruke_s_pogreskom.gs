function pripremiNacrte() {
  const list = SpreadsheetApp.getActive().getSheetByName('dnevnici');
  const podaci = list.getDataRange().getValues();
  const zaglavlje = podaci[0];               // prvi redak: nazivi
  const stSifra = zaglavlje.indexOf('šifra');
  const stNapomena = zaglavlje.indexOf('sigurnosna napomena');
  const stNacrt = zaglavlje.indexOf('nacrt');
  for (let r = 1; r < podaci.length; r++) {  // od drugog retka
    const napomena = podaci[r][stNapomena].trim();
    const nacrt = 'Pregledao sam dnevnik (' + podaci[r][stSifra] +
      '). Sigurnosna napomena: ' + napomena;
    list.getRange(r + 1, stNacrt + 1).setValue(nacrt);
  }
}

// Dio Damirove skripte iz poglavlja 22, u obliku u kojem je javio
// TypeError: Cannot read properties of undefined (reading 'trim')
//   pripremiNacrte @ Poruke.gs:9
// Da biste pogrešku vidjeli sami: na listu "dnevnici" stupac
// "sigurnosna napomena" preimenujte u "Sigurnost" i pokrenite funkciju.
// Popravljena inačica je u datoteci Poruke.gs u istoj mapi.

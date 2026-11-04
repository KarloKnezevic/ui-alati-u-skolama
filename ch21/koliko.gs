// Damirova prva skripta: samo broji dnevnike na otvorenom listu.
function koliko() {
  const broj = SpreadsheetApp.getActiveSheet().getLastRow() - 1;
  Logger.log('U tablici je ' + broj + ' dnevnika.');   // bez zaglavlja
}

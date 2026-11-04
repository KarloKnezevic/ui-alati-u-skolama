// Pokrenite JEDNOM ručno. Postavlja tjedni okidač.
function postaviTjedniOkidac() {
  const FUNKCIJA = 'ponedjeljakUjutro';
  // najprije obriši stare: nikad dva ista okidača
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === FUNKCIJA)
    .forEach(t => ScriptApp.deleteTrigger(t));
  ScriptApp.newTrigger(FUNKCIJA)
    .timeBased()
    .onWeekDay(ScriptApp.WeekDay.MONDAY)
    .atHour(6)              // stvarno između 6 i 7
    .create();
}

// Pokreće ga okidač: prijenos, nacrti i poruka Damiru, bez slanja.
function ponedjeljakUjutro() {
  prenesiNoveDnevnike_();
  obradiRadove();             // robusna petlja (pogl. 23)
  const knj = SpreadsheetApp.getActive();
  const ceka = knj.getSheetByName('radovi')
    .getDataRange().getValues().slice(1)      // bez zaglavlja
    .filter(r => r[3] !== '' && r[5] !== 'DA').length;
  MailApp.sendEmail(Session.getEffectiveUser().getEmail(),
    'Dnevnici prakse: ' + ceka + ' nacrta čeka pregled',
    'Tablica: ' + knj.getUrl());
}

// Samo novi: list "dnevnici" (pogl. 21) -> "radovi" (pogl. 23)
function prenesiNoveDnevnike_() {
  const knj = SpreadsheetApp.getActive();
  const radovi = knj.getSheetByName('radovi');
  const vec = new Set(radovi.getDataRange().getValues()
    .map(r => String(r[7])));               // H: vrijeme predaje
  knj.getSheetByName('dnevnici')
    .getDataRange().getValues().slice(1)
    .filter(d => !vec.has(String(d[0])))    // A: vrijeme predaje
    .forEach(d => radovi.appendRow(         // šifra, D-G, ..., H
      [d[1], d.slice(3, 7).join('\n'), '', '', '', '', '', d[0]]));
}

// Kad tjedni tok više ne treba: obrišite okidač u izborniku Triggers ili
// pokrenite ovu funkciju. Brisanje kôda ne briše okidač.
function obrisiTjedniOkidac() {
  ScriptApp.getProjectTriggers()
    .filter(t => t.getHandlerFunction() === 'ponedjeljakUjutro')
    .forEach(t => ScriptApp.deleteTrigger(t));
}

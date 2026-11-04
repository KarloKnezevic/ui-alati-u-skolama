// POSTAVKE: sve što se mijenja, na jednom mjestu.
// Trenutačne vrijednosti provjerite u Dodatku A.
const POSTAVKE = {
  dobavljac: 'gemini',
  osnovniUrl: 'https://generativelanguage.googleapis.com/v1beta',
  model: 'gemini-3.1-flash-lite',    // ID modela, studeni 2026.
  svojstvoKljuca: 'GEMINI_API_KEY'   // ključ u svojstvima skripte
};

// Jedina funkcija koja razgovara s modelom (tijelo: pogl. 23).
function pitajModel(upit, shema) {
  // 1. pročitaj ključ  2. pošalji upit i shemu
  // 3. provjeri odgovor  4. vrati podatak ili baci jasnu pogrešku
}

// Zapisnik: jedan redak po radnji, u listu "zapisnik".
function zapisi(poruka) {
  SpreadsheetApp.getActive().getSheetByName('zapisnik')
    .appendRow([new Date(), poruka]);
}

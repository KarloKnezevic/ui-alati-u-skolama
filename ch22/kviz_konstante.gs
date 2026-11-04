// Kviz iz JSON-a u Google obrascu (preuređeno)
const NASLOV = 'Razlomci: kviz za učenje';
const BODOVI = 1;

function napraviKviz(kviz) {
  const obrazac = FormApp.create(NASLOV, false);
  obrazac.setIsQuiz(true);
  kviz.pitanja.forEach(function (p) {
    if (p.ponudeni.length < 2) return;
    const stavka = obrazac.addMultipleChoiceItem();
    stavka.setTitle(p.tekst);
    const izbori = p.ponudeni.map(function (o, i) {
      return stavka.createChoice(o, i === p.tocan);
    });
    stavka.setChoices(izbori);
    stavka.setPoints(BODOVI).setRequired(true);
  });
  Logger.log('Uređivanje: ' + obrazac.getEditUrl());
}

// Ova inačica zamjenjuje napraviKviz iz ch21/Code.gs (obrišite staru
// funkciju, inače projekt ima dvije s istim imenom). Funkcije pokreni i
// uGift ostaju kakve jesu. Brojevi redaka iznad odgovaraju slici
// „Anatomija skripte“ u poglavlju 22: mijenjate retke 2 i 3 i tekst
// između navodnika. Provjera ključa iz ch21 ovdje je namjerno izostavljena
// radi preglednosti; za stvarni kviz rabite inačicu iz ch21.

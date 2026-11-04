// Iz JSON-a (pogl. 16) složi kviz u Google obrascu, kao nacrt.
function napraviKviz(kviz) {
  kviz.pitanja.forEach(function (p, i) {           // 1. provjera ključa
    const n = p.tocan;                             // cijeli broj, od 0
    if (!(Number.isInteger(n) && n >= 0 && n < p.ponudeni.length)) {
      throw new Error('Pitanje ' + (i + 1) +
        ': "tocan" ne pokazuje ni na jedan odgovor.');
    }
  });
  const obrazac = FormApp.create(kviz.naslov, false); // 2. neobjavljen
  obrazac.setIsQuiz(true);
  kviz.pitanja.forEach(function (p) {              // 3. pitanje = stavka
    const stavka = obrazac.addMultipleChoiceItem();
    stavka.setTitle(p.tekst)
      .setChoices(p.ponudeni.map(function (odg, j) {
        return stavka.createChoice(odg, j === p.tocan); // točan: true
      }))
      .setPoints(p.bodovi || 1)
      .setRequired(true);
  });
  Logger.log('Uređivanje: ' + obrazac.getEditUrl());
  Logger.log('Za učenike, nakon objave: ' + obrazac.getPublishedUrl());
}

// Isti JSON kao datoteka GIFT za uvoz u Loomen (Moodle).
function uGift(kviz) {
  const zastiti = function (t) {                   // \ ispred ~ = # { } :
    return String(t).replace(/([~=#{}:])/g, '\\$1');
  };
  const blokovi = kviz.pitanja.map(function (p, i) {
    const odgovori = p.ponudeni.map(function (odg, j) {
      const znak = (j === p.tocan) ? '=' : '~';
      const obj = (p.objasnjenje && p.objasnjenje[j])
        ? ' # ' + zastiti(p.objasnjenje[j]) : '';
      return '  ' + znak + zastiti(odg) + obj;
    });
    return '::P' + (i + 1) + ':: ' + zastiti(p.tekst) + ' {\n' +
      odgovori.join('\n') + '\n}';
  });
  const tekst = '// ' + kviz.naslov + ' (' + kviz.razred + ' razred)\n' +
    blokovi.join('\n\n') + '\n';
  const datoteka = DriveApp.createFile(kviz.naslov + ' (GIFT).txt',
    tekst, MimeType.PLAIN_TEXT);
  Logger.log('GIFT u Driveu: ' + datoteka.getUrl());
}

function pokreni() {                               // ovu pokrećete
  napraviKviz(KVIZ);
  uGift(KVIZ);
}

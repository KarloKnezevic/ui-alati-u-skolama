// Shema listića i provjera nakon primitka (odjeljak „Strukturirani izlaz“).
// Ista shema kao u datoteci shema_listica.json.
const SHEMA_LISTICA = {
  type: 'object',
  properties: {
    naslov: { type: 'string', description: 'Naslov, do 8 riječi' },
    uvod:   { type: 'string', description: 'Dvije rečenice o interesu' },
    zadaci: {
      type: 'array', minItems: 5, maxItems: 5,
      items: {
        type: 'object',
        properties: {
          tekst:    { type: 'string' },
          rjesenje: { type: 'string', description: 'Rezultat i postupak' },
          razina:   { type: 'string', enum:
            ['prisjećanje', 'razumijevanje', 'primjena'] }
        },
        required: ['tekst', 'rjesenje', 'razina'],
        additionalProperties: false
      }
    }
  },
  required: ['naslov', 'uvod', 'zadaci'],
  additionalProperties: false
};

// Vraća { listic } ako valja, inače { razlog }.
function provjeriListic_(tekst) {
  let l;
  try { l = JSON.parse(tekst); }
  catch (e) { return { razlog: 'odgovor nije JSON' }; }
  if (!l.naslov || !l.uvod)
    return { razlog: 'nedostaje naslov ili uvod' };
  if (!Array.isArray(l.zadaci) || l.zadaci.length !== 5)
    return { razlog: 'treba točno 5 zadataka' };
  const razine = ['prisjećanje', 'razumijevanje', 'primjena'];
  for (const z of l.zadaci) {
    if (!z.tekst || !z.rjesenje)
      return { razlog: 'zadatak bez teksta ili rješenja' };
    if (razine.indexOf(z.razina) < 0)
      return { razlog: 'nepoznata razina: ' + z.razina };
  }
  return { listic: l };
}

// Jedan pravi listić za stazu B i interes „glazba“. Šalje jedan poziv
// modelu; ne treba ni list „predlozak“ ni podatke o učenicima.
function probniListic() {
  const upit = 'Sastavi radni listić od 5 zadataka o razlomcima za ' +
    '5. razred osnovne škole u Hrvatskoj. Staza B: vođeni pa samostalni ' +
    'zadaci. Svi primjeri neka budu iz svijeta glazbe. Za svaki zadatak ' +
    'napiši rješenje s kratkim postupkom i razinu. Hrvatski standardni ' +
    'jezik, rečenice do 20 riječi. Vrati samo JSON prema zadanoj shemi.';
  const odg = pitajModel(upit, SHEMA_LISTICA);
  if (odg.kod !== 200) {
    Logger.log(odg.kod + ' ' + odg.greska); return;
  }
  const p = provjeriListic_(odg.tekst);
  Logger.log(p.listic ? JSON.stringify(p.listic, null, 2)
                      : 'Odbijeno: ' + p.razlog);
  Logger.log('ulaz ' + odg.ulaz + ', izlaz ' + odg.izlaz +
    ', USD ' + odg.usd.toFixed(4));
}

function pokvareniListic() {   // ne zove model, ne stoji ništa
  const los = '{"naslov": "Probni", "uvod": "Dvije rečenice.", ' +
    '"zadaci": []}';
  Logger.log(provjeriListic_(los).razlog); // treba točno 5 zadataka
}

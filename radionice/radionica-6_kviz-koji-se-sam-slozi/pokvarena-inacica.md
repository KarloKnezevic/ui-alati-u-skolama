# Pokvarena inačica · upute za voditelja

*Radionica 6 · priprema za drugi dio rada u parovima · samo za voditelja, ne dijeliti prije radionice*

Pogreška je namjerno jedna i sitna, kakvu nastavnik stvarno napravi kad ručno dorađuje JSON: u jednom pitanju polje se zove drukčije nego što ga skripta traži. Takav kvar odgovara drugoj poruci iz galerije pogrešaka u poglavlju 22 („Cannot read properties of undefined“) i brzoj provjeri iz istog poglavlja (`reading 'length'` u retku 9 funkcije `napraviKviz`).

## Kako je napraviti

1. U projektu Apps Scripta iz recepta 21.3 zamijenite funkciju `napraviKviz` preuređenom inačicom iz mape `ch22/` (slika 22.1 u knjizi). Funkciju `pokreni` iz poglavlja 21 ostavite kakva jest.
2. Pokrenite `pokreni` jednom s ispravnim kvizom i provjerite da obrazac nastaje.
3. U datoteci `kviz` (ondje gdje je `const KVIZ =`) u **prvom** pitanju preimenujte polje `ponudeni` u `ponudjeni`. Ništa drugo ne mijenjajte.

Prvo pitanje nakon promjene izgleda ovako (ostala pitanja ostaju kakva jesu):

```json
{ "tekst": "Pizza je izrezana na 8 jednakih komada. Pojedena su 3. Koji je dio pojeden?",
  "ponudjeni": ["3/5", "3/8", "5/8", "8/3"], "tocan": 1, "bodovi": 1,
  "objasnjenje": [
    "Usporedio si pojedeno s preostalim, a ne s cijelom pizzom.",
    "Točno: 3 od 8 jednakih dijelova.", "To je dio koji je ostao.",
    "Brojnik i nazivnik su zamijenjeni."],
  "ishod": "MAT OŠ A.5.3" }
```

4. Pokrenite `pokreni` i prepišite poruku iz zapisnika izvršavanja točno onako kako je glasi na vašem računu. Ako se razlikuje od one u [poruka-o-pogresci.md](poruka-o-pogresci.md) (drukčiji naziv datoteke ili broj retka, jer ste skriptu složili drukčije), ispravite ispis prije radionice. Tekst poruke ovisi o okruženju i inačici; važni su vrsta, opis i redak.
5. Obrišite obrazac koji je možda nastao u prvom pokušaju i vratite naziv polja `ponudeni` kad radionica završi.

## Rješenje (za raspravu)

- **Što se dogodilo.** Redak 9 preuređene funkcije traži `p.ponudeni.length`. U prvom pitanju polja `ponudeni` više nema, pa je `p.ponudeni` *undefined*, a od nepostojeće vrijednosti ne može se tražiti duljina.
- **Dobra hipoteza** (jedna rečenica, prije pitanja asistentu): „U nekom pitanju polje `ponudeni` ne postoji ili se zove drukčije.“
- **Najmanja promjena koja uklanja uzrok:** u JSON-u vratiti naziv `ponudeni`. Slovo po slovo usporedite naziv u kȏdu s nazivom u JSON-u.
- **Zamka.** Asistent može ponuditi i promjenu koja uklanja poruku, a ne uzrok (npr. da skripta preskoči pitanje bez ponuđenih odgovora). Skripta bi tada „proradila“ i tiho složila kviz bez prvog pitanja. Isti obrazac pogreške pokazuje Damirov primjer u poglavlju 22; upit 22.1 izrijekom traži promjenu koja uklanja uzrok, a prijedlog čitamo prije nego što ga prihvatimo.

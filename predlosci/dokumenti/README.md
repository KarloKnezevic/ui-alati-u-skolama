# Predlošci dokumenata

Devet dokumenata iz dodatka D knjige, svaki u svojoj datoteci i s istim brojem kao u knjizi. Poglavlja ih spominju, ali nijedno ih ne donosi u cijelosti. Svaki počinje zaglavljem s mjestima za popunjavanje (`[NAZIV ŠKOLE]`, `[DATUM]`) i završava ondje gdje škola mora odlučiti sama. Zašto dokument izgleda baš tako, piše u poglavlju navedenom u tablici; tamo se vratite prije nego što neku stavku izbrišete.

Mjesta za popunjavanje pisana su velikim slovima u uglatim zagradama, `[OVAKO]`; kućice za označavanje su `☐`. Datoteke su u Markdownu, pa ih možete otvoriti u bilo kojem uređivaču teksta, zalijepiti u dokument ili dati asistentu kao predložak.

| Br. | Dokument | Tko ga rabi | Pogl. |
|---|---|---|---|
| D.1 | [Školska pravila o uporabi UI-ja](D.1_skolska-pravila.md) | tim za UI, zbornica, ravnatelj | 13 |
| D.2 | [Izjava o uporabi UI-ja](D.2_izjava-o-uporabi-ui-ja.md) | učenici, studenti, nastavnici | 15 |
| D.3 | [Kartica zadatka po AIAS-u](D.3_kartica-zadatka.md) | nastavnik, aktiv, katedra | 15 |
| D.4 | [Obavijest i česta pitanja za roditelje](D.4_obavijest-roditeljima.md) | škola, razrednici | 13, 18 |
| D.5 | [Postupak u slučaju krivotvorenog sadržaja](D.5_postupak-krivotvoreni-sadrzaj.md) | ravnatelj, stručna služba, razrednici | 18 |
| D.6 | [Zahtjev školskom administratoru](D.6_zahtjev-administratoru.md) | nastavnik | 5, 21 |
| D.7 | [Prijedlog pilota ravnatelju](D.7_prijedlog-pilota.md) | tim za UI, nastavnik | 13 |
| D.8 | [Anonimni nacrt prilagodbe zadataka](D.8_anonimni-nacrt-prilagodbe.md) | nastavnik, stručni suradnik | 11 |
| D.9 | [Specifikacija aplikacije na jednoj stranici](D.9_specifikacija-aplikacije.md) | nastavnik koji gradi alat | 24 |


## Word i PDF

Svaki predložak postoji u tri oblika: Markdown u ovoj mapi, `word/` za uređivanje u Wordu ili LibreOfficeu i `pdf/` za ispis. Mijenja se samo Markdown; Word i PDF izrađuju se iz njega naredbom `bash scripts/izradi_predloske.sh`.

## Predložak, a ne pravni savjet

Nijedan dokument iz ove mape nije pravni savjet. Prije uporabe svaki uskladite sa službenikom za zaštitu podataka, sa statutom i općim aktima škole i s tajnikom, koji zna u kojem se obliku dokument donosi. Navodi iz propisa i CARNET-ovih Smjernica preneseni su doslovno, s izvorom; ne prepričavajte ih slobodnije nego što ih prenosimo mi.

## Licencija

Predlošci su pod licencijom CC BY-NC 4.0 (v. [LICENCA.md](../../LICENCA.md)): prilagodite ih svojoj školi i podijelite s kolegama, uz navođenje knjige kao izvora. Hrvatska prilagodba ljestvice AIAS 2.1 (autori Mike Perkins, Jasper Roe, Leon Furze i Jason MacVaugh) nalazi se samo u knjizi, u poglavlju 15 i dodatku D; u spremištu je samo kartica zadatka koja se na nju oslanja.

## Povezano

- Kontrolni popisi iz dodatka C: [../kontrolni-popisi/](../kontrolni-popisi/README.md)
- Predlošci upita iz knjige: [../upiti/](../upiti/README.md)
- Stanje alata (živa inačica dodatka A): [../../STANJE_ALATA.md](../../STANJE_ALATA.md)

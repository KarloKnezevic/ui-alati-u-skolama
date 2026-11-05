# Dimni test: `provjeri_primjere.py`

Skripta iz dodatka E koja prije objave i jednom u polugodištu provjerava
cijelo spremište. Prođe sve mape `chNN/` i `podaci_izmisljeni/`: provjeri
`README.md` i `PROVJERENO.md`, sintaksu Pythona i JavaScripta (`.gs`, `.js`,
skripte u `.html`), ispravnost JSON-a i bilježnica, broj stupaca u CSV-ovima,
kodiranje UTF-8 i da nigdje nema ničega što izgleda kao ključ. Zatim
pokrene primjere koji rade bez mreže (analiza kviza, težina zadataka, alat
za listić, GIFT i kviz iz Apps Scripta u simulaciji, MCP poslužitelj) i,
ako je postavljena varijabla `GEMINI_API_KEY`, pošalje jedan probni poziv
modelu `gemini-3.1-flash-lite`. Na kraju ispiše sažetak „prošlo / palo /
preskočeno“.

Pokretanje iz korijena spremišta:

    python3 scripts/provjeri_primjere.py
    python3 scripts/provjeri_primjere.py --bez-poziva

Bez ključa, bez mreže, bez Node.js-a ili bez paketa skripta i dalje radi:
ono što ne može provjeriti označi kao preskočeno. Za potpun prolaz pokrenite
je iz virtualnog okruženja u kojem su instalirani paketi iz
`ch19/requirements.txt` i `ch26/requirements.txt`. Ništa u spremištu ne
mijenja; primjeri se pokreću u privremenoj mapi. Kad ništa ne padne,
upišite datum u `PROVJERENO.md` provjerenih mapa, a što se promijenilo, u
`ISPRAVCI.md`.

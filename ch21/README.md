# Poglavlje 21: Tablica koja radi sama: automatizacija bez straha

Skripte za Google Apps Script iz poglavlja 21. `Code.gs` sadrži
`napraviKviz`, `uGift` i `pokreni` (kviz iz JSON-a u Google obrascu i
datoteka GIFT za Loomen), `kviz.gs` cijeli Tomislavov kviz od deset pitanja
kao konstantu `KVIZ`, a `kviz.json` isti kviz kao običan JSON. U
`kviz_pokvareni.gs` osmo pitanje ima ključ izvan popisa odgovora
(`"tocan": 4`), za vježbu čitanja poruke o pogrešci. `koliko.gs` je Damirova prva skripta, a
`Poruke.gs` nacrti poruka s odobrenjem (`pripremiNacrte`,
`posaljiOdobrene`).

Kviz: na `script.google.com` napravite projekt, u `Code.gs` zalijepite
istoimenu datoteku, dodajte datoteku skripte `kviz` sa sadržajem `kviz.gs`
i pokrenite `pokreni` (recept „Kviz iz JSON-a u Google obrascu i GIFT za
Loomen“). Poruke: u tablicu uvezite
`../podaci_izmisljeni/dnevnici_prakse_izmisljeni.csv` kao list `dnevnici`
i `../podaci_izmisljeni/adrese_izmisljene.csv` kao list `adrese`, umjesto
primjera adrese upišite svoju, upišite komentar uz dva ili tri retka i
pokrenite najprije `pripremiNacrte`. Ništa se ne šalje dok u stupcu
`odobreno` ne upišete DA.

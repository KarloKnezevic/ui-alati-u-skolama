# Poglavlje 25: Damirov ponedjeljak

`tjedni_okidac.gs` sadrži tri funkcije iz odjeljka o zakazanom tijeku:
`postaviTjedniOkidac` (pokreće se jednom, ručno), `ponedjeljakUjutro` (nju
pokreće okidač) i `prenesiNoveDnevnike_`, te `obrisiTjedniOkidac` za kraj
projekta. Tok svakog ponedjeljka između 6 i 7 sati prenosi nove dnevnike s
lista `dnevnici` na list `radovi`, izrađuje nacrte i Damiru šalje jednu
poruku s brojem nacrta koji čekaju pregled. Učenicima ne šalje ništa:
slanje odobrenih poruka pokreće čovjek.

Datoteka ide u isti projekt Apps Scripta kao `pitajModel.gs`, `listici.gs`
i `povratna.gs` iz mape `ch23/` (funkcija `obradiRadove`). Za probu u
tablicu uvezite `../podaci_izmisljeni/dnevnici_prakse_izmisljeni.csv` kao
list `dnevnici` i napravite list `radovi` sa zaglavljem šifra, tekst rada,
status, nacrt, konačno, odobreno, poslano, predano. Prije okidača tok barem
jednom pokrenite ručno i pročitajte zapisnik. Zbroj troška u svojstvu
`UKUPNO_USD_RADOVI` raste iz tjedna u tjedan; kad tok stane na granici,
pogledajte zapisnik, pa svojstvo obrišite ili povisite granicu.

# Poglavlje 22: Kȏd bez straha: čitati, mijenjati i popravljati

Primjeri za čitanje i mijenjanje kôda. `kviz_konstante.gs` je preuređena
funkcija `napraviKviz` sa slike „Anatomija skripte“ (zamjenjuje istoimenu
funkciju iz `ch21/Code.gs`). `Poruke_s_pogreskom.gs` je Damirova skripta u
obliku koji javlja `TypeError`, a `Poruke.gs` popravljena inačica s glasnom
pogreškom. `kviz_pokvaren.json` sadrži dvije pogreške iz odjeljka o JSON-u
(provjera: `python3 -m json.tool kviz_pokvaren.json`). `tezina.py` računa
težinu zadataka iz `../ch19/rezultati_izmisljeni.csv`, a `kostur.gs` i
`kostur.py` su kostur idioma knjige (`POSTAVKE`, `pitajModel`, zapisnik).
U podmapi `listic/` je mali alat iz recepta s asistentom za programiranje:
`kviz_u_listic.py` iz `kviz.json` pravi `listic.md` i `kljuc.md`.

Pokretanje: u mapi `ch22` napravite okruženje (`python3 -m venv .venv`,
`source .venv/bin/activate`, `pip install -r requirements.txt`) pa
`python3 tezina.py`. Alat za listić treba samo Python: `cd listic` i
`python3 kviz_u_listic.py`. Skripte `.gs` lijepe se u projekt Apps Scripta
iz poglavlja 21; za Damirovu skriptu u tablicu uvezite
`../podaci_izmisljeni/dnevnici_prakse_izmisljeni.csv` kao list `dnevnici`.

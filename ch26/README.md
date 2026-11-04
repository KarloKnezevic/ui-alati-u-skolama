# Poglavlje 26: pretraživanje po značenju i MCP

Dva primjera iz poglavlja. Prvi je pretraživanje po značenju:
`pretrazivanje_po_znacenju.ipynb` za Colab i `pretrazivanje_po_znacenju.py`
za vlastito računalo otvaraju `listici_izmisljeni.txt` (dvadeset izmišljenih
opisa u retcima `naslov | opis`, u kojima se riječ „razlomak“ ne pojavljuje
nijednom); za svoju datoteku promijenite konstantu `DATOTEKA`.
`biljeske_izvori_izmisljene.txt` su Antinih pet bilježaka o izvorima,
izmišljenih za vježbu. Brojke u knjizi dobivene su jednim pokretanjem;
vaše se mogu malo razlikovati.

Drugi je mali MCP-poslužitelj koji samo čita mapu `knjiznica/`: resurs s
ishodima (`ishodi.md`), predložak upita (`upiti/listic.md`) i alat
`pronadi_materijal`. `posluzitelj_pokrivenost.py` je isti poslužitelj s
drugim alatom, `pokrivenost`. Mapa `knjiznica/listici/` ima četrdeset
izmišljenih listića s oznakama ishoda i jedan bez oznake („Linearna
jednadžba s vagom“), pa alat daje iste brojeve kao tablica pokrivenosti u
knjizi. Neki listići nose i ishod A.5.5. koji nije među osam ishoda prvog
polugodišta.

Pokretanje poslužitelja: `python3 -m venv .venv`, uključite okruženje,
`pip install -r requirements.txt`, zatim `python proba.py` (ili
`python proba.py posluzitelj_pokrivenost.py`). Ispis mora sadržavati popis
alata i jedanaest listića za A.5.3. U `posluzitelj.py` konstantu `MAPA`
promijenite u potpunu putanju svoje mape, a u `klijent_konfiguracija.json`
upišite potpune putanje do Pythona iz `.venv` i do poslužitelja.

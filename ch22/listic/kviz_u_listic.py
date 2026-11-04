"""Iz kviz.json napravi radni listić (listic.md) i zaseban ključ (kljuc.md).

Specifikacija je upit 22.2: samo standardna biblioteka, ništa ne šalje na
internet, čita samo kviz.json u istoj mapi i piše samo dvije nove datoteke.
Ako JSON nije ispravan ili polje nedostaje, staje s porukom na hrvatskom.
Pokretanje: python3 kviz_u_listic.py
"""
import json
import sys
from pathlib import Path

# POSTAVKE
MAPA = Path(__file__).parent          # sve datoteke su u mapi skripte
ULAZ = MAPA / "kviz.json"
LISTIC = MAPA / "listic.md"
KLJUC = MAPA / "kljuc.md"
SLOVA = "ABCDEFGH"                    # oznake ponuđenih odgovora


def stani(poruka):
    """Glasna pogreška: poruka na hrvatskom i izlaz bez ikakve datoteke."""
    sys.exit("POGREŠKA: " + poruka)


def ucitaj_kviz():
    """Pročitaj kviz.json i provjeri sva polja prije pisanja ičega."""
    if not ULAZ.exists():
        stani(f"nema datoteke {ULAZ.name} u mapi {MAPA}.")
    try:
        kviz = json.loads(ULAZ.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        stani(f"{ULAZ.name} nije ispravan JSON (redak {e.lineno}, "
              f"stupac {e.colno}): {e.msg}.")
    if not isinstance(kviz.get("naslov"), str):
        stani('nedostaje polje "naslov".')
    pitanja = kviz.get("pitanja")
    if not isinstance(pitanja, list) or not pitanja:
        stani('nedostaje polje "pitanja" ili je prazno.')
    for i, p in enumerate(pitanja, start=1):
        for polje in ("tekst", "ponudeni", "tocan"):
            if polje not in p:
                stani(f'pitanje {i}: nedostaje polje "{polje}".')
        if not isinstance(p["ponudeni"], list) or len(p["ponudeni"]) < 2:
            stani(f'pitanje {i}: "ponudeni" mora imati barem dva odgovora.')
        if len(p["ponudeni"]) > len(SLOVA):
            stani(f"pitanje {i}: previše ponuđenih odgovora.")
        n = p["tocan"]
        # bool je u Pythonu posebna vrsta cijelog broja, pa ga isključujemo
        if not isinstance(n, int) or isinstance(n, bool) \
                or not 0 <= n < len(p["ponudeni"]):
            stani(f'pitanje {i}: "tocan" ne pokazuje ni na jedan odgovor '
                  f'(broji se od 0).')
        bodovi = p.get("bodovi", 1)
        if not isinstance(bodovi, (int, float)) or isinstance(bodovi, bool):
            stani(f'pitanje {i}: "bodovi" mora biti broj.')
    return kviz


def napisi_listic(kviz):
    retci = [f"# {kviz['naslov']}", "",
             "Ime i prezime: ______________________   Razred: ______", "",
             "Zaokruži slovo ispred točnog odgovora.", ""]
    for i, p in enumerate(kviz["pitanja"], start=1):
        retci.append(f"**{i}.** {p['tekst']}")
        retci.append("")
        for slovo, odgovor in zip(SLOVA, p["ponudeni"]):
            retci.append(f"- {slovo}) {odgovor}")
        retci.append("")
    return "\n".join(retci)


def napisi_kljuc(kviz):
    retci = [f"# {kviz['naslov']}: ključ", "",
             "| Pitanje | Točno | Bodovi |", "|---------|-------|--------|"]
    ukupno = 0
    for i, p in enumerate(kviz["pitanja"], start=1):
        bodovi = p.get("bodovi", 1)
        ukupno += bodovi
        retci.append(f"| {i} | {SLOVA[p['tocan']]} | {bodovi} |")
    retci += ["", f"Ukupno bodova: {ukupno}", ""]
    return "\n".join(retci), ukupno


def main():
    kviz = ucitaj_kviz()                  # sve provjere prije pisanja
    listic = napisi_listic(kviz)
    kljuc, ukupno = napisi_kljuc(kviz)
    LISTIC.write_text(listic, encoding="utf-8")
    KLJUC.write_text(kljuc, encoding="utf-8")
    print(f"Zapisnik: broj pitanja {len(kviz['pitanja'])}, "
          f"ukupno bodova {ukupno}.")
    print(f"Napravljeno: {LISTIC.name} i {KLJUC.name}. Ključ provjerite ručno.")


if __name__ == "__main__":
    main()

"""Nacrti povratne informacije u Pythonu: isti tok kao obradiRadove u povratna.gs.

Čita ../podaci_izmisljeni/izvjesca_prakse_izmisljena.csv (izvješća napisana
za vježbu), predlozak_povratna.txt i shema_povratne.json. Stanje vodi u
izlaz/radovi.csv: skripta piše samo stupce "status" i "nacrt"; "konačno" i
"odobreno" piše nastavnik, a ova skripta ništa ne šalje.
Za stvarne radove samo odobreni put škole; najsigurnije je lokalni model
(u pitaj_model.py POSTAVKE za "ollama", poglavlje 27).
Pokretanje: python3 tok_povratna.py
"""
import csv
import json
import re
import shutil
import sys
from pathlib import Path

from pitaj_model import POSTAVKE, zadnji_racun
from tok_listici import GRANICA_USD, IZLAZ, pozovi_uporno, zapisi

MAPA = Path(__file__).parent
ULAZ = MAPA.parent / "podaci_izmisljeni" / "izvjesca_prakse_izmisljena.csv"
RUBRIKA_DAT = MAPA.parent / "podaci_izmisljeni" / "rubrika_prakticna_vjezba.md"
PREDLOZAK = MAPA / "predlozak_povratna.txt"
SHEMA = json.loads((MAPA / "shema_povratne.json").read_text(encoding="utf-8"))
STANJE = IZLAZ / "radovi.csv"
UKUPNO = IZLAZ / "ukupno_usd_radovi.txt"
RAZINE = ("početna", "razvojna", "ostvarena")


def normaliziraj(t):
    t = re.sub(r"[„“”\"'’‘«»]", "", str(t).lower())
    return re.sub(r"\s+", " ", t).strip()


def provjeri(o, rad, broj_kriterija):
    """Ono što shema ne može: broj kriterija i citati koji su doista u radu."""
    kriteriji = o.get("kriteriji") if isinstance(o, dict) else None
    if not isinstance(kriteriji, list) or len(kriteriji) != broj_kriterija:
        return "broj kriterija nije jednak broju redaka rubrike"
    for k in kriteriji:
        if k.get("razina") not in RAZINE:
            return f"nepoznata razina: {k.get('razina')}"
        dokaz = normaliziraj(k.get("dokaz", "")).strip(".")
        if dokaz != "nema dokaza" and dokaz not in normaliziraj(rad):
            return f"citat nije u radu: {str(k.get('dokaz'))[:40]}"
    if not (o.get("dobro") and o.get("poboljsati") and o.get("sljedeci_korak")):
        return "nedostaje korak povratne informacije"
    return None


def nacrt(o):
    kriteriji = "\n".join(f"{k['kriterij']}: {k['razina']} („{k['dokaz']}“)"
                          for k in o["kriteriji"])
    return (f"Što je dobro: {o['dobro']}\nŠto poboljšati: {o['poboljsati']}\n"
            f"Sljedeći korak: {o['sljedeci_korak']}\n---\n{kriteriji}")


def main():
    IZLAZ.mkdir(exist_ok=True)
    if not STANJE.exists():
        shutil.copyfile(ULAZ, STANJE)
    with open(STANJE, encoding="utf-8", newline="") as f:
        redovi = list(csv.DictReader(f, delimiter=";"))
    rubrika = RUBRIKA_DAT.read_text(encoding="utf-8")
    broj_kriterija = sum(1 for r in rubrika.splitlines() if r.startswith("- "))
    predlozak = PREDLOZAK.read_text(encoding="utf-8").replace("{{rubrika}}", rubrika)
    ukupno = float(UKUPNO.read_text()) if UKUPNO.exists() else 0.0
    print(f"Model: {POSTAVKE['dobavljac']} / {POSTAVKE['model']}")
    for red in redovi:
        sifra, rad = red["šifra"], red["tekst rada"]
        if red["status"] not in ("", "čeka") or not rad.strip():
            continue
        if ukupno >= GRANICA_USD:
            zapisi(sifra, "STOP: granica troška")
            sys.exit(f"Granica troška ({GRANICA_USD} USD) je dosegnuta.")
        upit = predlozak.replace("{{tekst_rada}}", rad)     # šifra ne ide van
        razlog, o = "", None
        for pokusaj in range(2):                            # jedan popravak
            o, razlog = pozovi_uporno(upit, sifra, None, SHEMA)
            if o is not None:
                razlog = provjeri(o, rad, broj_kriterija)
            ukupno += zadnji_racun()["usd"]
            if not razlog or pokusaj == 1 or \
                    (o is None and not razlog.startswith("200:")):
                break
            zapisi(sifra, f"provjera: {razlog}")
            upit += f"\nPrethodni odgovor nije valjao: {razlog}"
        if o is not None and not razlog:
            red["nacrt"], red["status"] = nacrt(o), "gotovo"
        else:
            red["status"] = "pogreška"
        UKUPNO.write_text(f"{ukupno:.6f}")
        with open(STANJE, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(redovi[0]), delimiter=";")
            w.writeheader()
            w.writerows(redovi)
        zapisi(sifra, "" if red["status"] == "gotovo" else razlog)
        print(f"{sifra}: {red['status']} {razlog or ''}".rstrip())
    print("Nacrti su u izlaz/radovi.csv. Konačni tekst piše nastavnik.")


if __name__ == "__main__":
    main()

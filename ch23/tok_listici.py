"""Trideset listića u Pythonu: isti robusni tok kao obradiRazred u listici.gs.

Za Microsoftov put, vlastito računalo ili Colab, i za lokalni model iz
poglavlja 27 (u pitaj_model.py promijenite samo POSTAVKE). Čita
ucenici_izmisljeni.csv, predlozak_listic.txt i shema_listica.json iz ove
mape. Stanje (status, poslano) vodi u izlaz/ucenici.csv, pa ponovno
pokretanje obrađuje samo retke sa statusom "" ili "čeka". Listići idu u
izlaz/listici.md, rješenja u izlaz/rjesenja.md, a svaki poziv u
zapisnik.txt. Šifra učenika nikad ne ide modelu.
Pokretanje: python3 tok_listici.py   (ključ u varijabli okruženja, Dodatak E)
"""
import csv
import json
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

from pitaj_model import POSTAVKE, PogreskaModela, pitaj_model, zadnji_racun

MAPA = Path(__file__).parent
ULAZ = MAPA / "ucenici_izmisljeni.csv"
PREDLOZAK = MAPA / "predlozak_listic.txt"
SHEMA = json.loads((MAPA / "shema_listica.json").read_text(encoding="utf-8"))
IZLAZ = MAPA / "izlaz"
STANJE = IZLAZ / "ucenici.csv"
UKUPNO = IZLAZ / "ukupno_usd.txt"      # zbroj troška preživljava prekide
ZAPISNIK = MAPA / "zapisnik.txt"

GRANICA_USD = 0.20                     # vaša granica za cijeli tok
ISHOD = "[ISHOD IZ KURIKULA, DOSLOVNO]"
STAZE = {
    "A": "Prvi zadatak je razrađen primjer, ostali su vođeni koracima.",
    "B": "Vođeni pa samostalni zadaci.",
    "C": "Otvoreni problemi iz stvarnog života; jedan traži objašnjenje.",
}
RAZINE = ("prisjećanje", "razumijevanje", "primjena")


def zapisi(sifra, napomena=""):
    r = zadnji_racun()
    with open(ZAPISNIK, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\t{sifra}\t{r['ulaz']}\t"
                f"{r['izlaz']}\t{r['usd']:.4f}\t{napomena}\n")


def popuni(predlozak, red):            # red["šifra"] ne ide van
    return (predlozak.replace("{{staza}}", red["staza"])
            .replace("{{opis_staze}}", STAZE[red["staza"]])
            .replace("{{interes}}", red["interes"])
            .replace("{{ishod}}", ISHOD))


def provjeri_listic(l):
    """Vrati None ako listić valja, inače razlog odbijanja."""
    if not isinstance(l, dict) or not l.get("naslov") or not l.get("uvod"):
        return "nedostaje naslov ili uvod"
    zadaci = l.get("zadaci")
    if not isinstance(zadaci, list) or len(zadaci) != 5:
        return "treba točno 5 zadataka"
    for z in zadaci:
        if not z.get("tekst") or not z.get("rjesenje"):
            return "zadatak bez teksta ili rješenja"
        if z.get("razina") not in RAZINE:
            return f"nepoznata razina: {z.get('razina')}"
    return None


def pozovi_uporno(upit, sifra, red, shema=None):
    """Na 429 i 5xx čeka 4, 8 i 16 s, najviše tri puta; ostalo vraća odmah.
    Vraća (podatak ili None, razlog). Bez retka (red=None) ne bilježi
    vrijeme slanja; bez sheme rabi shemu listića."""
    for pokusaj in range(4):
        if pokusaj > 0:
            time.sleep(2 * 2 ** pokusaj)
        if red is not None:
            red["poslano"] = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        try:
            return pitaj_model(upit, shema or SHEMA), ""
        except PogreskaModela as e:
            if e.kod == 429 or e.kod >= 500:
                zapisi(sifra, f"{e.kod}, novi pokušaj")
                continue
            return None, str(e)
    return None, "429 ili 5xx i nakon tri ponovna pokušaja"


def pokusaj(upit, sifra, red):
    """Poziv s ponovnim pokušajima i provjera listića.
    Vraća (listić ili None, razlog, smije li se jednom popraviti)."""
    listic, greska = pozovi_uporno(upit, sifra, red)
    if greska:                     # "200: odgovor nije JSON" smije popravak
        return None, greska, greska.startswith("200:")
    razlog = provjeri_listic(listic)
    return (None, razlog, True) if razlog else (listic, "", False)


def spremi_stanje(redovi):
    with open(STANJE, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(redovi[0]), delimiter=";")
        w.writeheader()
        w.writerows(redovi)


def dodaj_listic(sifra, l):
    with open(IZLAZ / "listici.md", "a", encoding="utf-8") as f:
        f.write(f"\n<!-- nova stranica -->\n{sifra}\n\n# {l['naslov']}\n\n"
                f"*{l['uvod']}*\n\n")
        for i, z in enumerate(l["zadaci"], start=1):
            f.write(f"{i}. ({z['razina']}) {z['tekst']}\n\n")
    with open(IZLAZ / "rjesenja.md", "a", encoding="utf-8") as f:
        f.write(f"\n## {sifra}\n\n")
        for i, z in enumerate(l["zadaci"], start=1):
            f.write(f"{i}. ({z['razina']}) {z['rjesenje']}\n")


def main():
    IZLAZ.mkdir(exist_ok=True)
    if not STANJE.exists():
        shutil.copyfile(ULAZ, STANJE)
    with open(STANJE, encoding="utf-8", newline="") as f:
        redovi = list(csv.DictReader(f, delimiter=";"))
    predlozak = PREDLOZAK.read_text(encoding="utf-8")
    ukupno = float(UKUPNO.read_text()) if UKUPNO.exists() else 0.0
    print(f"Model: {POSTAVKE['dobavljac']} / {POSTAVKE['model']}")
    for red in redovi:
        sifra = red["šifra"]
        if red["status"] not in ("", "čeka"):
            continue                                   # preskoči gotovo
        if ukupno >= GRANICA_USD:
            zapisi(sifra, "STOP: granica troška")
            sys.exit(f"Granica troška ({GRANICA_USD} USD) je dosegnuta.")
        upit = popuni(predlozak, red)
        listic, razlog, popravljivo = pokusaj(upit, sifra, red)
        ukupno += zadnji_racun()["usd"]
        if popravljivo:                                # jedan popravak
            zapisi(sifra, f"shema: {razlog}")
            listic, razlog, _ = pokusaj(
                upit + f"\nPrethodni odgovor nije valjao: {razlog}", sifra, red)
            ukupno += zadnji_racun()["usd"]
        if listic is not None:
            dodaj_listic(sifra, listic)
            red["status"] = "gotovo"
        else:
            red["status"] = "pogreška"
        UKUPNO.write_text(f"{ukupno:.6f}")
        spremi_stanje(redovi)                          # poslije svakog retka
        zapisi(sifra, "" if red["status"] == "gotovo" else razlog)
        print(f"{sifra}: {red['status']} {razlog}".rstrip())
    print(f"Ukupno: {ukupno:.4f} USD. Pročitajte sva rješenja prije ispisa.")


if __name__ == "__main__":
    main()

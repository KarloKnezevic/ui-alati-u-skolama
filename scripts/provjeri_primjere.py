#!/usr/bin/env python3
"""Dimni test spremišta primjera (Dodatak E, „Spremište primjera“).

Prođe sve mape chNN/ i podaci_izmisljeni/ i provjeri:
  - ima li svaka mapa README.md i PROVJERENO.md u obliku iz knjige;
  - sintaksu Pythona (.py i kôdne ćelije bilježnica .ipynb);
  - ispravnost JSON-a (datoteke s „pokvaren“ u imenu moraju biti neispravne);
  - CSV: isti broj stupaca u svakom retku;
  - sintaksu JavaScripta u .gs, .js i .html (ako je instaliran Node.js);
  - da nigdje nema nečega što izgleda kao ključ API-ja i da nema pokvarenih
    hrvatskih znakova;
  - da aplikacije iz ch24 ništa ne spremaju i ništa ne dohvaćaju s mreže;
pokreće primjere koji rade bez mreže i bez ključa (ako su potrebni paketi
instalirani) i, ako je postavljena varijabla okruženja GEMINI_API_KEY,
šalje jedan probni poziv jeftinim modelom iz knjige.

Radi bez ključa i bez mreže; tada probni poziv preskoči. Ništa u spremištu
ne mijenja: primjeri se pokreću u privremenoj mapi.
Pokretanje iz korijena spremišta:
    python3 scripts/provjeri_primjere.py
    python3 scripts/provjeri_primjere.py --bez-poziva   (bez probnog poziva)
Nakon prolaza ažurirajte datume u PROVJERENO.md.
"""
import csv
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

# POSTAVKE probnog poziva: jeftin model iz knjige (Dodatak A)
POSTAVKE = {
    "osnovni_url": "https://generativelanguage.googleapis.com/v1beta",
    "model": "gemini-3.1-flash-lite",
    "varijabla_kljuca": "GEMINI_API_KEY",
}

KORIJEN = Path(__file__).resolve().parent.parent
TEKSTNE = {".py", ".json", ".ipynb", ".csv", ".gs", ".js", ".html", ".md",
           ".txt", ".sh"}
TAJNE = [
    (re.compile(r"AIza[0-9A-Za-z_\-]{30,}"), "ključ Google API-ja"),
    (re.compile(r"sk-ant-[0-9A-Za-z_\-]{10,}"), "ključ Anthropica"),
    (re.compile(r"\bsk-(proj-)?[0-9A-Za-z]{20,}"), "ključ OpenAI-ja"),
    (re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}"), "GitHubov token"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "privatni ključ"),
]
POKVARENI_ZNAKOVI = re.compile("Ä[‡Ť‘Ť]|Å[¡¾]|Ĺ[ˇľ]|Ã[¨©]")
SPREMANJE = re.compile(r"localStorage|sessionStorage|document\.cookie|"
                       r"indexedDB|\bfetch\s*\(|XMLHttpRequest|<link[^>]+href=\"http")
DOPUSTENE_ADRESE = ("http://www.w3.org/2000/svg", "https://doi.org/")

rezultati = []          # (stanje, opis)


def zapis(stanje, opis):
    rezultati.append((stanje, opis))
    oznaka = {"ok": "PROŠLO", "palo": "PALO", "preskoceno": "PRESKOČENO"}[stanje]
    print(f"[{oznaka:10}] {opis}")


def rel(p):
    return str(Path(p).relative_to(KORIJEN))


def mape_primjera():
    mape = sorted(p for p in KORIJEN.iterdir()
                  if p.is_dir() and re.fullmatch(r"ch\d\d", p.name))
    podaci = KORIJEN / "podaci_izmisljeni"
    return mape, ([podaci] if podaci.is_dir() else [])


def sve_datoteke(mape):
    for mapa in mape:
        for p in sorted(mapa.rglob("*")):
            if p.is_file() and not any(d in p.parts for d in
                                       (".venv", "__pycache__", "izlaz")):
                yield p


# ---------------------------------------------------------------- provjere

def provjeri_strukturu(mape):
    for mapa in mape:
        nedostaje = [d for d in ("README.md", "PROVJERENO.md")
                     if not (mapa / d).is_file()]
        if nedostaje:
            zapis("palo", f"{mapa.name}: nedostaje {', '.join(nedostaje)}")
            continue
        prov = (mapa / "PROVJERENO.md").read_text(encoding="utf-8")
        if not prov.startswith(f"Provjereno: {mapa.name}") or \
                "Datum zadnje provjere:" not in prov or "Model u POSTAVKE:" not in prov:
            zapis("palo", f"{mapa.name}/PROVJERENO.md nije u obliku iz Dodatka E")
        else:
            zapis("ok", f"{mapa.name}: README.md i PROVJERENO.md")


def provjeri_tekst(datoteke):
    """UTF-8, pokvareni hrvatski znakovi i ključevi u svim tekstnim datotekama."""
    prije = sum(1 for s, _ in rezultati if s == "palo")
    broj = 0
    for p in datoteke:
        if p.suffix not in TEKSTNE:
            continue
        broj += 1
        try:
            t = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            zapis("palo", f"{rel(p)}: nije spremljena kao UTF-8")
            continue
        for uzorak, opis in TAJNE:
            if uzorak.search(t):
                zapis("palo", f"{rel(p)}: sadrži nešto što izgleda kao {opis}")
        if POKVARENI_ZNAKOVI.search(t):
            zapis("palo", f"{rel(p)}: pokvareni hrvatski znakovi (dvostruko kodiranje)")
    if sum(1 for s, _ in rezultati if s == "palo") == prije:
        zapis("ok", f"{broj} tekstnih datoteka: UTF-8, bez ključeva i pokvarenih znakova")


def provjeri_python(datoteke):
    for p in datoteke:
        if p.suffix == ".py":
            try:
                compile(p.read_text(encoding="utf-8"), str(p), "exec")
                zapis("ok", f"{rel(p)}: sintaksa Pythona")
            except SyntaxError as e:
                zapis("palo", f"{rel(p)}: SyntaxError u retku {e.lineno}: {e.msg}")


def provjeri_json(datoteke):
    for p in datoteke:
        if p.suffix not in (".json", ".ipynb"):
            continue
        namjerno = "pokvaren" in p.name
        try:
            podatak = json.loads(p.read_text(encoding="utf-8"))
        except ValueError as e:
            if namjerno:
                zapis("ok", f"{rel(p)}: namjerno neispravan JSON javlja pogrešku ({e})")
            else:
                zapis("palo", f"{rel(p)}: neispravan JSON: {e}")
            continue
        if namjerno:
            zapis("palo", f"{rel(p)}: trebao bi biti neispravan, a nije")
            continue
        if p.suffix == ".ipynb":
            kod = []
            for celija in podatak.get("cells", []):
                if celija.get("cell_type") == "code":
                    izvor = "".join(celija.get("source", []))
                    # retci s ! i % su naredbe bilježnice, ne Python
                    kod.append("\n".join(r for r in izvor.splitlines()
                                         if not r.lstrip().startswith(("!", "%"))))
            try:
                compile("\n\n".join(kod), str(p), "exec")
                zapis("ok", f"{rel(p)}: bilježnica (JSON i Python u ćelijama)")
            except SyntaxError as e:
                zapis("palo", f"{rel(p)}: SyntaxError u ćeliji: {e.msg}")
        else:
            zapis("ok", f"{rel(p)}: JSON")


def provjeri_csv(datoteke):
    for p in datoteke:
        if p.suffix != ".csv":
            continue
        tekst = p.read_text(encoding="utf-8")
        prvi = tekst.splitlines()[0] if tekst else ""
        razdjelnik = ";" if prvi.count(";") >= prvi.count(",") else ","
        retci = list(csv.reader(io.StringIO(tekst), delimiter=razdjelnik))
        if len(retci) < 2:
            zapis("palo", f"{rel(p)}: nema podataka ispod zaglavlja")
            continue
        n = len(retci[0])
        losi = [i + 1 for i, r in enumerate(retci) if r and len(r) != n]
        if losi:
            zapis("palo", f"{rel(p)}: retci {losi[:5]} nemaju {n} stupaca")
        else:
            zapis("ok", f"{rel(p)}: CSV, {len(retci) - 1} redaka, {n} stupaca")


def node_dostupan():
    return shutil.which("node") is not None


def provjeri_javascript(datoteke, privremena):
    if not node_dostupan():
        zapis("preskoceno", "JavaScript (.gs, .js, .html): Node.js nije instaliran")
        return
    for p in datoteke:
        if p.suffix in (".gs", ".js"):
            izvor = p.read_text(encoding="utf-8")
        elif p.suffix == ".html":
            izvor = "\n".join(re.findall(r"<script[^>]*>(.*?)</script>",
                                         p.read_text(encoding="utf-8"), re.S))
        else:
            continue
        kopija = Path(privremena) / "provjera.js"
        kopija.write_text(izvor, encoding="utf-8")
        r = subprocess.run(["node", "--check", str(kopija)],
                           capture_output=True, text=True)
        if r.returncode == 0:
            zapis("ok", f"{rel(p)}: sintaksa JavaScripta")
        else:
            poruka = (r.stderr.strip().splitlines() or ["?"])[-1]
            zapis("palo", f"{rel(p)}: {poruka}")


def provjeri_aplikacije(datoteke):
    """Aplikacije iz ch24: ništa ne spremaju i ništa ne dohvaćaju s mreže."""
    for p in datoteke:
        if p.suffix != ".html":
            continue
        t = p.read_text(encoding="utf-8")
        greske = []
        if '<meta charset="utf-8">' not in t or 'lang="hr"' not in t:
            greske.append('nedostaje <meta charset="utf-8"> ili lang="hr"')
        if SPREMANJE.search(t):
            greske.append("spremanje ili dohvaćanje: " + SPREMANJE.search(t).group(0))
        for adresa in re.findall(r"https?://[^\s\"'<>]+", t):
            if not adresa.startswith(DOPUSTENE_ADRESE):
                greske.append("neobjašnjena adresa: " + adresa)
        if greske:
            zapis("palo", f"{rel(p)}: " + "; ".join(greske))
        else:
            zapis("ok", f"{rel(p)}: jedna datoteka, ništa ne sprema ni ne dohvaća")


# ------------------------------------------------------- pokretanje primjera

def ima_paket(ime):
    r = subprocess.run([sys.executable, "-c", f"import {ime}"],
                       capture_output=True, text=True)
    return r.returncode == 0


def pokreni(opis, naredba, mapa, ocekivano, paketi=(), istek=120):
    nedostaje = [p for p in paketi if not ima_paket(p)]
    if nedostaje:
        zapis("preskoceno", f"{opis}: nije instaliran paket {', '.join(nedostaje)}")
        return
    okolina = dict(os.environ, MPLBACKEND="Agg", PYTHONDONTWRITEBYTECODE="1")
    try:
        r = subprocess.run(naredba, cwd=mapa, capture_output=True, text=True,
                           timeout=istek, env=okolina)
    except subprocess.TimeoutExpired:
        zapis("palo", f"{opis}: nije završilo u {istek} s")
        return
    izlaz = r.stdout + r.stderr
    nema = [o for o in ocekivano if o not in izlaz]
    if r.returncode != 0 or nema:
        zadnji = (izlaz.strip().splitlines() or ["(bez ispisa)"])[-1]
        zapis("palo", f"{opis}: {('nema u ispisu: ' + repr(nema[0])) if nema else zadnji}")
    else:
        zapis("ok", f"{opis}")


NODE_GOOGLE = r"""
// Lažne Googleove usluge: dovoljno da se skripte pokrenu bez Googlea.
const fs = require('fs'), vm = require('vm');
const zapisnik = [];
global.Logger = { log: m => zapisnik.push(String(m)) };
global.MimeType = { PLAIN_TEXT: 'text/plain' };
let gift = null;
global.DriveApp = { createFile: (ime, tekst) => { gift = tekst; return { getUrl: () => 'drive' }; } };
const obrasci = [];
global.FormApp = { create: (naslov, objavljen) => {
  const o = { naslov, objavljen, stavke: [], setIsQuiz() {}, getEditUrl: () => 'uredi',
    getPublishedUrl: () => 'objava',
    addMultipleChoiceItem() { const s = { izbori: [], setTitle() { return s; },
      createChoice: (t, tocan) => ({ t, tocan }), setChoices(i) { s.izbori = i; return s; },
      setPoints() { return s; }, setRequired() { return s; } }; o.stavke.push(s); return s; } };
  obrasci.push(o); return o; } };
global.ucitaj = f => vm.runInThisContext(fs.readFileSync(f, 'utf8'));
global.stanje = { zapisnik, obrasci, dohvati: () => gift };
"""


def pokreni_node(opis, skripta, privremena):
    if not node_dostupan():
        zapis("preskoceno", f"{opis}: Node.js nije instaliran")
        return
    datoteka = Path(privremena) / "simulacija.js"
    datoteka.write_text(NODE_GOOGLE + skripta, encoding="utf-8")
    r = subprocess.run(["node", str(datoteka)], capture_output=True, text=True,
                       cwd=KORIJEN, timeout=60)
    if r.returncode == 0 and "U REDU" in r.stdout:
        zapis("ok", opis)
    else:
        zadnji = ((r.stdout + r.stderr).strip().splitlines() or ["?"])[-1]
        zapis("palo", f"{opis}: {zadnji}")


def pokreni_primjere(privremena):
    py = sys.executable
    if (KORIJEN / "ch19").is_dir():
        pokreni("ch19/analiza_kviza.py: 24 učenika, P2 p = 0.46, P7 D = -0.250",
                [py, str(KORIJEN / "ch19/analiza_kviza.py")], privremena,
                ["Učenika: 24", "P2       0.46  +0.750", "P7 D = -0.250"],
                paketi=("pandas",))
    if (KORIJEN / "ch22").is_dir():
        pokreni("ch22/tezina.py: P5 prelagan, P10 pretežak",
                [py, "tezina.py"], KORIJEN / "ch22",
                ["P5 je možda prelagan: 0.92", "P10 je možda pretežak: 0.29"],
                paketi=("pandas",))
        listic = Path(privremena) / "listic"
        shutil.copytree(KORIJEN / "ch22/listic", listic)
        pokreni("ch22/listic/kviz_u_listic.py: listić i ključ iz kviz.json",
                [py, "kviz_u_listic.py"], listic,
                ["broj pitanja 3", "ukupno bodova 3"])
    if (KORIJEN / "ch21").is_dir() and (KORIJEN / "ch16").is_dir():
        pokreni_node("ch21/Code.gs: uGift daje GIFT iz ch16/kviz_gift.txt (ch16 i ch21 kviz)", r"""
ucitaj('ch21/Code.gs');
const ocekivano = fs.readFileSync('ch16/kviz_gift.txt', 'utf8');
uGift(JSON.parse(fs.readFileSync('ch16/kviz.json', 'utf8')));
if (stanje.dohvati() !== ocekivano) { console.log('GIFT iz ch16/kviz.json se razlikuje'); process.exit(1); }
uGift(JSON.parse(fs.readFileSync('ch21/kviz.json', 'utf8')));
if (!stanje.dohvati().startsWith(ocekivano)) { console.log('prva pitanja ch21/kviz.json ne daju GIFT iz ch16'); process.exit(1); }
console.log('U REDU');
""", privremena)
        pokreni_node("ch21: pokreni() s kviz.gs složi 10 pitanja, kviz_pokvareni.gs staje na 7.", r"""
ucitaj('ch21/Code.gs');
vm.runInThisContext(fs.readFileSync('ch21/kviz.gs', 'utf8').replace('const KVIZ', 'globalThis.KVIZ'));
pokreni();
const o = stanje.obrasci[0];
if (o.stavke.length !== 10 || o.objavljen !== false) { console.log('obrazac nije dobar'); process.exit(1); }
const kljuc = o.stavke.map(s => 'ABCD'[s.izbori.findIndex(i => i.tocan)]).join('');
if (kljuc !== 'BBACDABDCA') { console.log('ključ se ne slaže s ch19: ' + kljuc); process.exit(1); }
vm.runInThisContext(fs.readFileSync('ch21/kviz_pokvareni.gs', 'utf8').replace('const KVIZ', 'globalThis.KVIZ'));
try { pokreni(); console.log('pokvareni kviz nije zaustavljen'); process.exit(1); }
catch (e) { if (!/Pitanje 7/.test(e.message)) { console.log(e.message); process.exit(1); } }
console.log('U REDU');
""", privremena)
    if (KORIJEN / "ch23").is_dir():
        pokreni_node("ch23/shema.gs: pokvareniListic javlja razlog bez poziva modelu", r"""
ucitaj('ch23/shema.gs');
pokvareniListic();
if (stanje.zapisnik[0] !== 'treba točno 5 zadataka') { console.log(stanje.zapisnik[0]); process.exit(1); }
console.log('U REDU');
""", privremena)
    if (KORIJEN / "ch26").is_dir():
        pokreni("ch26/proba.py: MCP-poslužitelj preko stdio, 11 listića za A.5.3",
                [py, "proba.py", "posluzitelj_pokrivenost.py"], KORIJEN / "ch26",
                ["pronadi_materijal", "dio-cjeline", "A.5.3.    11", "B.5.1.     0"],
                paketi=("mcp",))


# ---------------------------------------------------------- probni poziv

def probni_poziv():
    kljuc = os.environ.get(POSTAVKE["varijabla_kljuca"])
    if not kljuc:
        zapis("preskoceno", f"probni poziv: varijabla {POSTAVKE['varijabla_kljuca']} "
                            f"nije postavljena")
        return
    url = (f"{POSTAVKE['osnovni_url']}/models/{POSTAVKE['model']}"
           f":generateContent")
    tijelo = {"contents": [{"parts": [{"text":
              "Objasni razlomak 3/4 jednom rečenicom za 5. razred."}]}],
              "generationConfig": {"responseMimeType": "application/json",
                                   "responseJsonSchema": {
                                       "type": "object", "required": ["recenica"],
                                       "properties": {"recenica": {"type": "string"}}}}}
    zahtjev = urllib.request.Request(
        url, data=json.dumps(tijelo).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": kljuc})
    try:
        with urllib.request.urlopen(zahtjev, timeout=60) as odg:
            p = json.load(odg)
    except urllib.error.HTTPError as e:
        try:
            opis = json.loads(e.read().decode("utf-8"))["error"]["message"]
        except (ValueError, KeyError, TypeError):
            opis = ""
        zapis("palo", f"probni poziv ({POSTAVKE['model']}): kôd {e.code} "
                      f"{opis[:120]} (400 zahtjev ili ključ, 401/403 ključ, "
                      f"402 kredit, 404 ID modela, 429 kvota)")
        return
    except (urllib.error.URLError, TimeoutError) as e:
        zapis("preskoceno", f"probni poziv: nema mreže ({getattr(e, 'reason', e)})")
        return
    try:
        tekst = p["candidates"][0]["content"]["parts"][0]["text"]
        recenica = json.loads(tekst)["recenica"]
        t = p.get("usageMetadata", {})
        zapis("ok", f"probni poziv ({POSTAVKE['model']}): 200, ulaz "
                    f"{t.get('promptTokenCount', '?')}, izlaz "
                    f"{t.get('candidatesTokenCount', '?')} tokena: {recenica[:60]}")
    except (KeyError, IndexError, ValueError):
        zapis("palo", f"probni poziv ({POSTAVKE['model']}): odgovor nije u očekivanom obliku")


# ------------------------------------------------------------------ glavno

def main():
    bez_poziva = "--bez-poziva" in sys.argv[1:]
    mape, podaci = mape_primjera()
    if not mape:
        sys.exit("Nema mapa chNN: pokrenite skriptu iz spremišta primjera.")
    datoteke = list(sve_datoteke(mape + podaci))
    print(f"Dimni test: {len(mape)} mapa poglavlja, {len(datoteke)} datoteka\n")
    with tempfile.TemporaryDirectory() as privremena:
        provjeri_strukturu(mape)
        provjeri_tekst(datoteke)
        provjeri_python(datoteke)
        provjeri_json(datoteke)
        provjeri_csv(datoteke)
        provjeri_javascript(datoteke, privremena)
        provjeri_aplikacije([d for d in datoteke if d.parent.name == "ch24"])
        pokreni_primjere(privremena)
        if bez_poziva:
            zapis("preskoceno", "probni poziv: zatražen --bez-poziva")
        else:
            probni_poziv()
    broj = {s: sum(1 for r, _ in rezultati if r == s) for s in ("ok", "palo", "preskoceno")}
    print(f"\nSažetak: prošlo {broj['ok']}, palo {broj['palo']}, "
          f"preskočeno {broj['preskoceno']}")
    if broj["palo"]:
        print("Palo:")
        for s, opis in rezultati:
            if s == "palo":
                print("  - " + opis)
    else:
        print("Ništa nije palo. Upišite današnji datum u PROVJERENO.md provjerenih mapa.")
    sys.exit(1 if broj["palo"] else 0)


if __name__ == "__main__":
    main()

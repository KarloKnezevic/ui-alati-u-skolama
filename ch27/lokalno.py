"""Bilješke u tablicu „tko, što, do kada“ lokalnim modelom (poglavlje 27).

Puna inačica funkcije pitaj_model: prema polju "dobavljac" u POSTAVKE šalje
upit Ollami na ovom računalu ili dobavljaču u oblaku. Ostatak skripte ne zna
razliku. Samo standardna biblioteka Pythona.
Pokretanje (u mapi ch27, Ollama radi u pozadini): python3 lokalno.py
Čita upit_27_1.txt i biljeske.txt, piše nacrt.md. Nacrt čitate redak po
redak uz bilješke prije bilo kakve uporabe.
"""
import json
import os
import urllib.error
import urllib.request

POSTAVKE = {   # lokalni model; trenutačne vrijednosti: Dodatak A
    "dobavljac": "ollama",
    "osnovni_url": "http://localhost:11434/v1",  # ovo računalo
    "model": "gemma4:e4b",   # naziv kao u: ollama list
}
# Isti tok u oblaku (samo za podatke koji smiju van), npr.:
# POSTAVKE = {
#     "dobavljac": "gemini",
#     "osnovni_url": "https://generativelanguage.googleapis.com/v1beta",
#     "model": "gemini-3.1-flash-lite",
#     "varijabla_kljuca": "GEMINI_API_KEY",   # ključ je u okruženju
# }
# Za OpenAI-kompatibilnu krajnju točku u oblaku "dobavljac" je "openai",
# a osnovni_url, model i varijabla_kljuca prema Dodatku A.


def _kljuc():
    naziv = POSTAVKE.get("varijabla_kljuca")
    if not naziv:
        return None                      # lokalni model ne treba ključ
    kljuc = os.environ.get(naziv)
    if not kljuc:
        raise SystemExit(f"Varijabla okruženja {naziv} nije postavljena "
                         f"u ovom terminalu (Dodatak E).")
    return kljuc


def _posalji(url, tijelo, zaglavlja):
    zahtjev = urllib.request.Request(
        url, data=json.dumps(tijelo).encode("utf-8"),
        headers={"Content-Type": "application/json", **zaglavlja})
    try:
        with urllib.request.urlopen(zahtjev, timeout=600) as odg:
            return json.load(odg)
    except urllib.error.HTTPError as e:
        opis = e.read().decode("utf-8", "replace")[:300]
        if e.code == 404:
            opis += " (provjerite naziv modela: ollama list)"
        raise SystemExit(f"Poziv nije uspio, kôd {e.code}: {opis}") from None
    except urllib.error.URLError as e:
        raise SystemExit(f"Nema veze s {url} ({e.reason}). Radi li Ollama? "
                         f"Otvorite http://localhost:11434 u pregledniku.") from None


def pitaj_model(upit, shema=None):
    """Vrati tekst ili, uz shemu, podatak (lokalni model ili oblak)."""
    if POSTAVKE["dobavljac"] == "gemini":
        tijelo = {"contents": [{"parts": [{"text": upit}]}]}
        if shema:
            tijelo["generationConfig"] = {"responseMimeType": "application/json",
                                          "responseJsonSchema": shema}
        url = (POSTAVKE["osnovni_url"] + "/models/" + POSTAVKE["model"]
               + ":generateContent")
        p = _posalji(url, tijelo, {"x-goog-api-key": _kljuc()})
        kandidati = p.get("candidates") or [{}]
        dijelovi = kandidati[0].get("content", {}).get("parts") or [{}]
        tekst = dijelovi[0].get("text", "")
    else:                                # "ollama" ili "openai"
        tijelo = {"model": POSTAVKE["model"],
                  "messages": [{"role": "user", "content": upit}]}
        if POSTAVKE["dobavljac"] == "ollama":
            tijelo["temperature"] = 0    # ujednačeniji odgovori
        if shema:   # strukturirani izlaz, kao u poglavlju 23
            tijelo["response_format"] = {"type": "json_schema",
                "json_schema": {"name": "odgovor", "schema": shema}}
        kljuc = _kljuc()
        zaglavlja = {"Authorization": "Bearer " + kljuc} if kljuc else {}
        p = _posalji(POSTAVKE["osnovni_url"] + "/chat/completions",
                     tijelo, zaglavlja)
        tekst = p["choices"][0]["message"]["content"] or ""
    return json.loads(tekst) if shema else tekst


if __name__ == "__main__":
    upit = open("upit_27_1.txt", encoding="utf-8").read()
    biljeske = open("biljeske.txt", encoding="utf-8").read()
    nacrt = pitaj_model(upit.replace("[ZALIJEPITE BILJEŠKE]", biljeske))
    open("nacrt.md", "w", encoding="utf-8").write(nacrt)
    print("Nacrt je u datoteci nacrt.md. Pročitajte ga prije uporabe.")

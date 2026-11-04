"""POSTAVKE i pitaj_model u Pythonu: oblak ili lokalni model, isti oblik.

Python-inačica funkcije pitajModel iz pitajModel.gs (poglavlje 23) i
kostura iz poglavlja 22. Rabi samo standardnu biblioteku. Ključ se čita iz
varijable okruženja čiji je NAZIV u POSTAVKE; u kôdu ga nema.
Vraća tekst ili, uz shemu, podatak (rječnik); inače podiže PogreskaModela
s porukom na hrvatskom. Tokeni i trošak zadnjeg poziva: zadnji_racun().
"""
import json
import os
import urllib.error
import urllib.request

# POSTAVKE: jedino mjesto koje mijenjate (trenutačne vrijednosti: Dodatak A)
POSTAVKE = {
    "dobavljac": "gemini",        # "gemini", "openai" ili "ollama"
    "osnovni_url": "https://generativelanguage.googleapis.com/v1beta",
    "model": "gemini-3.1-flash-lite",
    "varijabla_kljuca": "GEMINI_API_KEY",   # ključ je u okruženju
    "cijena": {"ulaz": 0.25, "izlaz": 1.50},  # USD / 1M tokena
}
# Druge mogućnosti (zamijenite cijeli rječnik):
# OpenAI-kompatibilno (npr. Googleova krajnja točka):
#   {"dobavljac": "openai",
#    "osnovni_url": "https://generativelanguage.googleapis.com/v1beta/openai",
#    "model": "gemini-3.1-flash-lite", "varijabla_kljuca": "GEMINI_API_KEY",
#    "cijena": {"ulaz": 0.25, "izlaz": 1.50}}
# Lokalni model (pogl. 27), bez ključa i bez troška:
#   {"dobavljac": "ollama", "osnovni_url": "http://localhost:11434/v1",
#    "model": "gemma4:e4b", "varijabla_kljuca": "",
#    "cijena": {"ulaz": 0, "izlaz": 0}}

ISTEK_S = 600            # sekundi čekanja; lokalni model zna biti spor


class PogreskaModela(Exception):
    """Poziv nije uspio. U .kod je statusni kôd (0 ako nema veze)."""

    def __init__(self, kod, poruka):
        super().__init__(f"{kod}: {poruka}" if kod else poruka)
        self.kod = kod


_racun = {"ulaz": 0, "izlaz": 0, "usd": 0.0}


def zadnji_racun():
    """Tokeni i trošak zadnjeg poziva: {"ulaz", "izlaz", "usd"}."""
    return dict(_racun)


def _zapamti(ulaz, izlaz):
    c = POSTAVKE.get("cijena", {"ulaz": 0, "izlaz": 0})
    _racun.update(ulaz=ulaz, izlaz=izlaz,
                  usd=(ulaz * c["ulaz"] + izlaz * c["izlaz"]) / 1_000_000)


def _kljuc():
    naziv = POSTAVKE.get("varijabla_kljuca")
    if not naziv:
        return None
    kljuc = os.environ.get(naziv)
    if not kljuc:
        raise PogreskaModela(0, f"Varijabla okruženja {naziv} nije postavljena "
                                f"u ovom terminalu (Dodatak E).")
    return kljuc


def _posalji(url, tijelo, zaglavlja):
    zahtjev = urllib.request.Request(
        url, data=json.dumps(tijelo).encode("utf-8"),
        headers={"Content-Type": "application/json", **zaglavlja})
    try:
        with urllib.request.urlopen(zahtjev, timeout=ISTEK_S) as odg:
            return json.load(odg)
    except urllib.error.HTTPError as e:
        opis = e.read().decode("utf-8", "replace")
        try:
            p = json.loads(opis)
            p = p[0] if isinstance(p, list) and p else p
            opis = p.get("error", {}).get("message", opis)
        except (ValueError, AttributeError):
            pass
        raise PogreskaModela(e.code, opis[:300]) from None
    except urllib.error.URLError as e:
        raise PogreskaModela(0, f"nema veze s {url} ({e.reason})") from None


def _gemini(upit, shema):
    tijelo = {"contents": [{"parts": [{"text": upit}]}]}
    if shema:
        tijelo["generationConfig"] = {"responseMimeType": "application/json",
                                      "responseJsonSchema": shema}
    url = (f"{POSTAVKE['osnovni_url']}/models/{POSTAVKE['model']}"
           f":generateContent")
    p = _posalji(url, tijelo, {"x-goog-api-key": _kljuc()})  # ne u adresi!
    t = p.get("usageMetadata", {})
    _zapamti(t.get("promptTokenCount", 0),
             t.get("candidatesTokenCount", 0) + t.get("thoughtsTokenCount", 0))
    kandidati = p.get("candidates") or [{}]
    dijelovi = kandidati[0].get("content", {}).get("parts") or [{}]
    return dijelovi[0].get("text", "")       # blokiran odgovor: prazan tekst


def _chat_completions(upit, shema):
    """OpenAI-kompatibilna krajnja točka: OpenAI, Gemini, Ollama i dr."""
    tijelo = {"model": POSTAVKE["model"],
              "messages": [{"role": "user", "content": upit}]}
    if POSTAVKE["dobavljac"] == "ollama":
        tijelo["temperature"] = 0            # lokalni model to poštuje
    if shema:
        tijelo["response_format"] = {"type": "json_schema",
            "json_schema": {"name": "odgovor", "schema": shema}}
    kljuc = _kljuc()
    zaglavlja = {"Authorization": f"Bearer {kljuc}"} if kljuc else {}
    p = _posalji(POSTAVKE["osnovni_url"] + "/chat/completions", tijelo, zaglavlja)
    t = p.get("usage") or {}
    _zapamti(t.get("prompt_tokens", 0), t.get("completion_tokens", 0))
    izbori = p.get("choices") or [{}]
    return izbori[0].get("message", {}).get("content") or ""


def pitaj_model(upit, shema=None):
    """Vrati tekst ili, uz shemu, podatak; inače podigni PogreskaModela."""
    _zapamti(0, 0)
    dobavljac = POSTAVKE["dobavljac"]
    if dobavljac == "gemini":
        tekst = _gemini(upit, shema)
    elif dobavljac in ("openai", "ollama"):
        tekst = _chat_completions(upit, shema)
    else:
        raise PogreskaModela(0, f"nepoznat dobavljač u POSTAVKE: {dobavljac}")
    if not shema:
        return tekst
    try:
        return json.loads(tekst)
    except ValueError:
        raise PogreskaModela(200, "odgovor nije JSON") from None


if __name__ == "__main__":         # probni poziv, kao probniPoziv u Apps Scriptu
    shema = {"type": "object", "required": ["recenica"],
             "properties": {"recenica": {"type": "string"}}}
    try:
        print(pitaj_model("Objasni razlomak 3/4 jednom rečenicom za 5. razred.",
                          shema))
        r = zadnji_racun()
        print(f"ulaz {r['ulaz']}, izlaz {r['izlaz']}, USD {r['usd']:.5f}")
    except PogreskaModela as e:
        raise SystemExit(f"Poziv nije uspio: {e}")

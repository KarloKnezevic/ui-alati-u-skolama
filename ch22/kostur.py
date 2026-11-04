import os
from datetime import datetime

POSTAVKE = {   # trenutačne vrijednosti: Dodatak A
    "dobavljac": "gemini",
    "model": "gemini-3.1-flash-lite",
    "varijabla_kljuca": "GEMINI_API_KEY",  # ključ je u okruženju
}

def pitaj_model(upit, shema):
    """Vrati podatak ili podigni jasnu pogrešku (pogl. 23 i 27)."""
    kljuc = os.environ[POSTAVKE["varijabla_kljuca"]]
    ...

def zapisi(poruka):
    with open("zapisnik.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} {poruka}\n")

# Kostur idioma knjige u Pythonu. Poziv modelu još ne postoji: puno tijelo
# funkcije pitaj_model je u ch23/pitaj_model.py (oblak) i ch27/lokalno.py
# (oblak ili lokalni model). Ključ nikad ne piše u kôdu, samo naziv
# varijable okruženja.

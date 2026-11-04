# Analiza kviza: težina p, diskriminacija D i odabiri po pitanju.
# Izmišljeni podaci za vježbu (rezultati_izmisljeni.csv): 24 učenika pod
# šiframa U01-U24, redak KLJUC s točnim odgovorima, razdjelnik ";".
# Isti izračun kao formule iz poglavlja 19, samo u Pythonu.
# Pokretanje: python3 analiza_kviza.py  (u Colabu: prenesite CSV i
# pokrenite ćeliju s ovim kôdom).
import sys
from pathlib import Path

import pandas as pd

# POSTAVKE: datoteka i veličina skupine za D
DATOTEKA = Path(__file__).with_name("rezultati_izmisljeni.csv")
UDIO_SKUPINE = 1 / 3          # gornja i donja trećina razreda
GRAF = "p_i_D.png"            # prazno ("") ako graf ne treba

podaci = pd.read_csv(DATOTEKA, sep=";", index_col="sifra", dtype=str)
kljuc = podaci.loc["KLJUC"]               # redak s točnim odgovorima
ucenici = podaci.drop("KLJUC")            # ključ nije učenik!
if len(ucenici) == 0:
    sys.exit("U datoteci nema nijednog učenika.")

bodovi = (ucenici == kljuc).astype(int)   # 1 točno, 0 netočno
ukupno = bodovi.sum(axis=1)
p = bodovi.mean()                         # težina: udio točnih

# Razvrstavanje po ukupnom rezultatu; "stable" zadržava redoslijed
# učenika s jednakim zbrojem, kao razvrstavanje u tablici.
poredak = ukupno.sort_values(ascending=False, kind="stable").index
k = int(len(ucenici) * UDIO_SKUPINE)
gornja = bodovi.loc[poredak[:k]]
donja = bodovi.loc[poredak[-k:]]
D = gornja.mean() - donja.mean()

print(f"Učenika: {len(ucenici)} (skupine po {k})")
print(f"Prosječan rezultat: {ukupno.mean():.2f} od {bodovi.shape[1]}")
print()
print("Pitanje  p     D      A   B   C   D   ključ")
for pitanje in bodovi.columns:
    odabiri = ucenici[pitanje].value_counts()
    brojevi = "".join(f"{odabiri.get(slovo, 0):>4}" for slovo in "ABCD")
    print(f"{pitanje:<8} {p[pitanje]:.2f}  {D[pitanje]:+.3f} {brojevi}"
          f"   {kljuc[pitanje]}")

print()
print("Za pregled: zadaci s negativnim D")
for pitanje in D[D < 0].index:
    print(" ", pitanje, f"D = {D[pitanje]:+.3f}")

if GRAF:
    try:
        import matplotlib
        matplotlib.use("Agg")            # crta u datoteku, bez prozora
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nPaket matplotlib nije instaliran; graf preskačem.")
    else:
        fig, ax = plt.subplots(figsize=(6, 3.5))
        ax.axhline(0, color="black", lw=0.8)
        ax.axhline(0.2, color="orange", lw=0.8, ls="--")
        ax.scatter(p, D)
        for pitanje in p.index:
            ax.annotate(pitanje, (p[pitanje], D[pitanje]),
                        textcoords="offset points", xytext=(0, 6),
                        ha="center", fontsize=8)
        ax.set_xlabel("težina p (veći broj = lakši zadatak)")
        ax.set_ylabel("diskriminacija D")
        ax.set_xlim(0, 1)
        fig.tight_layout()
        fig.savefig(GRAF, dpi=150)
        print(f"\nGraf je spremljen u {GRAF}.")

import pandas as pd

# Izmišljeni podaci za vježbu (spremište, ch19)
PRETEZAK = 0.3   # granice su primjer; promijenite ih po volji
PRELAGAN = 0.9

podaci = pd.read_csv("../ch19/rezultati_izmisljeni.csv", sep=";",
                     index_col="sifra")
kljuc = podaci.loc["KLJUC"]         # redak s točnim odgovorima
ucenici = podaci.drop("KLJUC")      # ključ nije učenik!
tezina = (ucenici == kljuc).mean()  # p = udio točnih odgovora
print(tezina.round(2))

for zadatak, p in tezina.items():
    if p < PRETEZAK:
        print(zadatak, "je možda pretežak:", round(p, 2))
    elif p > PRELAGAN:
        print(zadatak, "je možda prelagan:", round(p, 2))

# Pokrećite iz mape ch22 (python3 tezina.py): relativna putanja računa se
# od trenutačne mape terminala. U Colabu prenesite CSV i u read_csv
# upišite samo "rezultati_izmisljeni.csv".

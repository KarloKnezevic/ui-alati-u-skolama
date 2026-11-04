# Izmišljeni podaci

Zajednički skupovi za vježbu koje rabi više poglavlja. Svi su izmišljeni:
šifre ne pripadaju nikome, a tekstovi nisu prepisani iz stvarnih radova.
CSV datoteke su u kodiranju UTF-8, s točkom-zarezom kao razdjelnikom (kao
CSV iz hrvatskog Excela); u Google tablice uvozite ih preko
Datoteka > Uvoz > Prijenos, uz automatsko otkrivanje razdjelnika.

| Datoteka | Što je | Gdje se rabi |
|---|---|---|
| `dnevnici_prakse_izmisljeni.csv` | 27 tjednih dnevnika prakse (šifre P-01 do P-30, 9. tjedan), stupci kao u Damirovu obrascu i četiri njegova stupca (komentar, nacrt, odobreno, poslano) | pogl. 21 (list `dnevnici`), 22 (`Poruke.gs`), 25 (tjedni tok) |
| `adrese_izmisljene.csv` | šifra i e-adresa; posvuda stoji `vasa.adresa@example.com`, pa prije probe upišite svoju | pogl. 21 i 23 (list `adrese`) |
| `izvjesca_prakse_izmisljena.csv` | osam izvješća s prakse napisanih za vježbu, u rasporedu lista `radovi`; P-10 sadrži podmetnutu uputu za provjeru zaštite iz upita | pogl. 23 (`obradiRadove`, `tok_povratna.py`), 25 |
| `rubrika_prakticna_vjezba.md` | rubrika s četiri kriterija i tri razine | pogl. 23 (shema povratne informacije) |
| `zlatni_skup_razlomci.csv` | deset pitanja o razlomcima s očekivanim odgovorom: osam običnih i dvije zamke iz pogl. 8, lažna pretpostavka (4. pitanje) i šifra ishoda koju stroj ne može pouzdano znati (5. pitanje) | pogl. 8 (ručno), 23 (`zlatniSkup.gs`), 27 (usporedba s lokalnim modelom) |

Podaci koje rabi samo jedno poglavlje stoje u njegovoj mapi:
`ch19/rezultati_izmisljeni.csv` (rezultati kviza, 24 učenika),
`ch23/ucenici_izmisljeni.csv` (razred 5.b, 30 šifri, staze i interesi),
`ch23/zapisnik_izmisljeni.csv`, `ch26/listici_izmisljeni.txt` i
`ch26/knjiznica/`. Stvarni podaci o učenicima ne idu ni ovamo ni u ijedan
alat iz knjige bez školskog pravila, ni pod šiframa.

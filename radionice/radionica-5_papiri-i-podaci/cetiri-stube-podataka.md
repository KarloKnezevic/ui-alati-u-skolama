# Četiri stube podataka

*Radionica 5 · uvod · prema poglavlju 19 („Što smije u alat“) · za ploču ili ispis*

O tome hoće li tablica smjeti u UI alat odlučuje jedno pitanje iz poglavlja 4: može li se iz nje, makar i neizravno, saznati o kome je riječ. Mogući odgovori slažu se u ljestvicu od četiri stube, od podataka koji nikad ne idu u alat izvan škole do podataka s kojima smijemo raditi što hoćemo. Što je stuba niža, to je manje rizika.

| Stuba | Primjer | Smije li u alat? |
|---|---|---|
| **1 Sirovi podaci** | `[Ime Prezime]; OIB; 5.c; MAT 2; 14 izostanaka; mjera` – izvoz iz e-Dnevnika, imenik | ✘ Ni u jedan UI alat izvan škole |
| **2 Šifre umjesto imena** | `U07; 5.c; P1 B; P2 A; …; 6` – šifra se može povezati s djetetom: i dalje osobni podatak | ⚠ Samo školski alat s ugovorom, ako pravila škole dopuštaju |
| **3 Zbrojevi** | `P2: A 10, B 11, C 2, D 1` – koliko je učenika izabralo koji odgovor, bez redaka po učeniku | ✔ Smije u alat, ako nijedna skupina nema samo 1–3 učenika |
| **4 Izmišljeni podaci** | datoteka za vježbu iz spremišta; nijedan stvaran učenik | ✔ Smije u alat |

Prve dvije stube su osobni podaci: šifra (pseudonimizacija) skriva ime, ali ne i dijete. Zbrojevi i izmišljeni podaci nisu podaci ni o kome, uz jedan uvjet: skupina od jednog do troje učenika u razredu se lako prepozna. Na biralištu s troje birača i rezultatom „3:0“ tajnosti više nema.

Na ovoj radionici radimo samo na četvrtoj stubi: `ch19/rezultati_izmisljeni.csv` iz mape poglavlja 19.

**Provjera izračuna** (iz recepta 19.1): za P2 u izmišljenoj tablici 11 točnih od 24, *p* = 0,46; u gornjoj trećini 7 od 8, u donjoj 1 od 8, *D* = 0,75.

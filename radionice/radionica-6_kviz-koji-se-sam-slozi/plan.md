# Radionica 6 · Kviz koji se sam složi

*Plan za ispis · dio VI knjige (poglavlja 20–24), oslanja se na poglavlja 21 i 22 · 90 minuta*

Na šestoj radionici prvi put otvaramo kȏd, ali nitko ne mora programirati.

**Za koga.** Sudionici prvih triju radionica; programersko predznanje nije potrebno.

**Ishodi.** Sudionik
1. vidi kako kviz zapisan u JSON-u postaje Google obrazac i datoteka GIFT za Loomen;
2. na ispisu skripte pokaže gdje se čita ulaz, a gdje nastaje izlaz;
3. poruku o pogrešci pretvori u hipotezu i popravak.

**Priprema voditelja.** Recept 21.3 („Kviz iz JSON-a u Google obrascu i GIFT za Loomen“) proveden do kraja na računu na kojem je dopušten Apps Script; za kviz bez podataka o učenicima dovoljan je osobni račun. Iz spremišta: Tomislavov kviz i skripta iz mape `ch21/`, preuređena funkcija `napraviKviz` iz mape `ch22/` (ista je na slici 22.1 u knjizi, s brojevima redaka) i pokvarena inačica s jednom namjerno ubačenom pogreškom ([pokvarena-inacica.md](pokvarena-inacica.md)). Ispišite skriptu s brojevima redaka i [poruku o pogrešci](poruka-o-pogresci.md), po jedan primjerak za par. Pokvarenu inačicu pokrenite jednom sami i provjerite da poruka na vašem računu glasi kao na ispisu.

**Oprema.** Jedno računalo s projektorom i voditeljevim računom (scenarij B iz poglavlja 14). Parovi rade na papiru, s olovkom.

## Tijek

| Min. | Dio | Što se radi |
|---|---|---|
| 10 | uvod | Pravilo „pročitaj prije nego što pokreneš“ (popis 10). |
| 15 | demonstracija | Recept 21.3 na jednom računalu, do gotovog obrasca. |
| 40 | rad u parovima | Čitanje skripte na papiru: olovkom zaokružiti ulaz, izlaz i redak koji bi se mijenjao za drugi kviz (20 min). Zatim pokvarena inačica: parovi dobiju poruku o pogrešci na papiru i po receptu „Od poruke o pogrešci do popravka“ (poglavlje 22) najprije zapišu hipotezu, pa je provjere s asistentom (20 min). |
| 15 | rasprava | Koja dopuštenja skripta traži i što bi koga zaustavilo da je sam pokrene. |
| 10 | refleksija | Izlazna kartica. |

## Materijali

- Spremište: kviz i skripta (`ch21/`), preuređena funkcija `napraviKviz` (`ch22/`), pokvarena inačica ([pokvarena-inacica.md](pokvarena-inacica.md)).
- Poruka o pogrešci za ispis, s mjestom za hipotezu: [poruka-o-pogresci.md](poruka-o-pogresci.md).
- Upiti: [21.3 Kviz u JSON za skriptu](../../predlosci/upiti/ch21/21.03_kviz-u-json-za-skriptu.md) (ako netko želi vlastiti kviz), [22.1 Od poruke o pogrešci do najmanje promjene](../../predlosci/upiti/ch22/22.01_od-poruke-o-pogresci-do-najmanje-promjene.md).
- Kontrolni popis [10 Pročitaj prije nego što pokreneš](../../predlosci/kontrolni-popisi/10_procitaj-prije-nego-sto-pokrenes.md).
- [Izlazna kartica](izlazna-kartica.md).

## Pravilo podataka

Za vrijeme radionice u obrazac upisujemo samo izmišljene odgovore. Prije nego što kȏd zalijepimo asistentu, provjerimo da u njemu nema ključeva, adresa e-pošte ni podataka o učenicima: šalje se samo kȏd.

## Pitanje na kartici

„Što prvo radite kad skripta javi pogrešku?“

## Do sljedećeg aktiva

Vlastiti kviz iz JSON-a na osobnom računu ili, za opreznije, jedna skripta pročitana do kraja.

## Je li uspjela?

Radionica je uspjela ako većina kartica točno odgovara na pitanje i navodi korak koji je izvediv: jedan recept, jedan razred, jedan dan. Kartice su bez imena i ne izlaze iz aktiva.

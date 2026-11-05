Provjereno: ch26
- Datum posljednje provjere: 5. 11. 2026. (dimni test `scripts/provjeri_primjere.py --bez-poziva`: prošlo 69, palo 0)
- Python: 3.13.1; paket mcpjoš nije provjereno==2.3.0
- Model u POSTAVKE: nema (poslužitelj ne poziva model; model bira domaćin)
- Model za pretraživanje po značenju: Qwen/Qwen3-Embedding-0.6B (za usporedbu BAAI/bge-m3); sentence-transformers==6.2.0
- Domaćin: poslužitelj provjeren klijentom iz SDK-a preko stdio; u Janu i asistentu na računalu još nije isproban
- Kontrolna provjera: python proba.py ispisuje alat pronadi_materijal i 11 listića za A.5.3
- Napomena: prva objava uz knjigu. Stavke označene „još nije provjereno“ provjeravaju se u stvarnom okruženju pri prvom polugodišnjem servisu.

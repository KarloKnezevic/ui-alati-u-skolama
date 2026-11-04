# Poglavlje 27: model na vlastitom računalu

`lokalno.py` je puna inačica funkcije `pitaj_model`: prema polju
`dobavljac` u `POSTAVKE` šalje upit Ollami na ovom računalu
(`http://localhost:11434/v1`) ili, ako tako upišete, dobavljaču u oblaku.
Na dnu je pet redaka koji spajaju `upit_27_1.txt` (upit „Tko, što, do kada“
za mali lokalni model) i `biljeske.txt` (izmišljene bilješke s Petrina
sastanka) i spremaju `nacrt.md`. `test_hrvatskog_obrazac.csv` je prazna
tablica za vlastiti test hrvatskog jezika (deset zadataka, dva lokalna
modela i jedan u oblaku).

Pokretanje: instalirajte Ollamu, `ollama pull gemma4:e4b`, provjerite da
naziv ne završava s `cloud`, isključite Wi-Fi i u ovoj mapi upišite
`python3 lokalno.py`. Paketi nisu potrebni. Whisper za prijepis vlastite
glasovne bilješke instalirajte u virtualno okruženje točno zadanom
inačicom, `pip install -r requirements-whisper.txt`, uz besplatni program
`ffmpeg` (Mac: `brew install ffmpeg`; Windows: `choco install ffmpeg`), a
zatim `whisper biljeska.m4a --model turbo --language Croatian
--output_format txt`. Pri prvom pokretanju Whisper preuzima težine modela,
pa tada treba internet; poslije radi bez njega. Snimke i fotografije nakon
provjere obrišite.

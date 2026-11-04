# Poglavlje 23: API, strukturirani izlaz i trideset listića

Apps Script za poziv modelu bez prozora za razgovor. `pitajModel.gs` sadrži
`POSTAVKE`, `pitajModel`, drugu provedbu `pitajOpenAI_`, pomoćne funkcije
`racun_` i `neuspjeh_` te `probniPoziv`. `shema.gs` je shema listića
(`SHEMA_LISTICA`, ista kao `shema_listica.json`) s funkcijama
`provjeriListic_`, `probniListic` i `pokvareniListic`. `listici.gs` sadrži
predložak (`ISHOD`, `STAZE`, `DOKUMENT_ID`, `popuni_`) i robusnu petlju
`obradiRazred` s pomoćnim funkcijama. `povratna.gs` je isti tok za nacrte
povratne informacije prema rubrici (`obradiRadove`, shema u
`shema_povratne.json`) sa slanjem tek nakon odobrenja, `zlatniSkup.gs`
pokreće zlatni skup nakon promjene modela, a `dobavljaci.gs` i
`curl_primjeri.sh` pokazuju isti poziv za Claude, OpenAI-jev Responses API
i iz terminala.

Redoslijed prati recepte iz poglavlja: ključ u Script Properties pod
nazivom `GEMINI_API_KEY`, zatim `pitajModel.gs` i `probniPoziv`, pa
`shema.gs`, pa `listici.gs` s listovima `ucenici` (uvezite
`ucenici_izmisljeni.csv`), `predlozak` (u A1 tekst iz
`predlozak_listic.txt`) i `zapisnik`. `zapisnik_izmisljeni.csv` je primjer
zapisnika iz poglavlja (31 uspješan poziv, jedan 429, ukupno 0,074 USD).
Za tok povratne informacije uvezite
`../podaci_izmisljeni/izvjesca_prakse_izmisljena.csv` kao list `radovi`, a
`predlozak_povratna.txt` zalijepite u A1 lista `predlozak_povratna`.

Isti tok u Pythonu, za vlastito računalo, Colab ili lokalni model: u
`pitaj_model.py` su `POSTAVKE` i `pitaj_model`, a `tok_listici.py` i
`tok_povratna.py` rade s CSV datotekama i pišu u mapu `izlaz/`. Trebaju
samo standardnu biblioteku: postavite ključ u varijablu okruženja (Dodatak
E) i pokrenite `python3 pitaj_model.py` za probni poziv, zatim
`python3 tok_listici.py`. Ključ nikad ne upisujte u kôd ni u tablicu koju
dijelite; učenički radovi ne idu u besplatni sloj.

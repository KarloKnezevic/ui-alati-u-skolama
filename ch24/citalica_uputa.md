# Čitalica: uputa za kolege (jedna stranica)

**Što radi.** Na projektoru se jedna po jedna pojavljuju riječi iz teksta
„Voda oko nas“, krupno, tamno na svijetlom. Djeca čitaju naglas; učiteljica
upravlja s razrednog računala. Razina 1 ima deset kratkih riječi, razina 2
pet dugih. Na kraju kruga piše „Pročitali smo sve riječi!“.

**Pokretanje.** Datoteku `citalica.html` kopirajte na radnu površinu
razrednog računala i otvorite je dvoklikom. Internet ne treba, prijava ne
treba, a aplikacija ništa ne sprema: ni imena, ni rezultate, ni u preglednik.

**Tipke.** Enter na početku: Kreni. Tipke 1 i 2: izbor razine. Razmaknica
ili strelica desno: sljedeća riječ. Esc: povratak na početak (prekinuti krug
se ne pamti). Gumb „Čuj riječ“ izgovara riječ hrvatskim glasom računala i
pojavljuje se samo ako takav glas postoji (na Windowsima se dodaje u
postavkama govora).

**Kako se mijenjaju riječi.** Datoteku otvorite u Bloku za pisanje (Notepad)
ili TextEditu kao običan tekst. Na vrhu skripte je popis `RIJECI`:

    const RIJECI = {
      1: ["voda", "kiša", ...],
      2: ["putovanje", "zalijevanje", ...]
    };

Svaka riječ stoji u ravnim navodnicima, a riječi odvaja zarez. Spremite kao
UTF-8, s nastavkom `.html`, i odigrajte jedan krug prije sata.

**Testni popis koji je prošla inačica 1.0** (20. 11. 2026., razredno
računalo, isključen Wi-Fi): kliknuti sve; krivi unos; mali i velik zaslon;
projektor pri dnevnom svjetlu; bez miša; bez interneta; dvadeset igara;
pretraga kôda (`localStorage`, `sessionStorage`, `cookie`, `fetch`, `http`:
nijedan pogodak). Test ponavljamo jednom u polugodištu.

Čitalica 1.0 · Jelena Babić, PŠ Bijeli Jasen · izrađeno uz pomoć UI alata ·
CC BY-SA 4.0

# Stanje alata

**Stanje: studeni 2026. (datum zadnjeg ažuriranja: 4. 11. 2026.)**

Cijene, planovi i uvjeti korištenja UI alata mijenjaju se brzo, pa je za svaku odluku mjerodavna službena stranica dobavljača, a ne ova tablica.

> Ovo je živa inačica dodatka A knjige „Korištenje alata umjetne inteligencije u školama“. Dodatak u knjizi bilježi stanje 2. studenoga 2026.; ovdje ga ažuriramo nakon objave, a svaku promjenu upisujemo u [Povijest promjena](#povijest-promjena) na dnu stranice.

## Sadržaj

- [Kako čitati tablice](#kako-čitati-tablice)
- [Tablica kriterija po alatu](#tablica-kriterija-po-alatu)
- [Tutorski načini](#tutorski-načini)
- [Dob i privatnost po alatu](#dob-i-privatnost-po-alatu)
- [Financijske razine](#financijske-razine)
- [Školske i institucijske licence](#školske-i-institucijske-licence)
- [Preimenovano, ugašeno, gasi se](#preimenovano-ugašeno-gasi-se)
- [Automatizacija i gradnja](#automatizacija-i-gradnja)
- [API: krajnje točke, ID-jevi i cijene](#api-krajnje-točke-id-jevi-i-cijene)
- [Lokalni modeli](#lokalni-modeli)
- [Tečajevi i UI pismenost](#tečajevi-i-ui-pismenost)
- [Kako provjeriti je li išta od ovoga još točno](#kako-provjeriti-je-li-išta-od-ovoga-još-točno)
- [Povijest promjena](#povijest-promjena)

---

Ovaj dio knjige zastarijeva najbrže. Poglavlja smo pisali tako da vrijede i kad se nazivi promijene, a ovdje stoje upravo ti nazivi: modeli, planovi, cijene, kvote, ID-jevi i putanje izbornika. Stanje smo zabilježili **2. studenoga 2026.** Samo u godini pisanja knjige ugašena je Sora, NotebookLM i Le Chat dobili su nova imena, a svi veliki dobavljači zamijenili su vodeće modele. Zato vrijedi jednostavno pravilo: **prije odluke provjerite živu inačicu** ovog dodatka (ovu stranicu, s datumom zadnjeg ažuriranja na vrhu), a zatim službenu stranicu dobavljača.

Dodatak ne ocjenjuje alate. Nećete naći zvjezdice, ukupne ocjene ni riječ „najbolji“. Umjesto toga uz svaki alat u istom retku stoje cijena, besplatna razina i njezino ograničenje, hrvatski jezik, postupanje s podacima i najniža dob. Što je za vaš razred važnije, procjenjujete vi, uz pravila iz poglavlja 4, 5 i 13.

### Kako čitati tablice

Kako do alata dolazi nastavnik u Hrvatskoj, pokazuju četiri oznake: **BESPLATNO**, **DJELOMIČNO BESPLATNO**, **PLAĆENO** i **ŠKOLSKA LICENCA**. Cijene u USD navodimo onako kako ih dobavljač objavljuje, **bez poreza**; Hrvatska ima 25 % PDV-a, pa je konačan iznos na blagajni za četvrtinu veći. EUR navodimo samo ondje gdje ga dobavljač izravno prikazuje za Hrvatsku ili EU.

Pouzdanost označavamo ovako:

| Oznaka | Značenje |
|---|---|
| bez oznake | stavka je potvrđena na službenom izvoru |
| *(djel.)* | službeni izvor bio je samo djelomično dostupan ili podatak potvrđuju sekundarni izvori |
| *(provj.)* | podatak nismo uspjeli potvrditi ili su izvori proturječni, pa ga prije odluke valja provjeriti |
| – | podatak nismo provjeravali |

Ako neka stavka s oznakom *(provj.)* do objave ne bude potvrđena, iz knjige je izostavljamo.

## Tablica kriterija po alatu

Redoslijed u tablici nije poredak kakvoće. Počinjemo sa školskim računom jer ga svaki nastavnik i učenik u Hrvatskoj već ima: identitet **AAI@EduHr** (ime.prezime@skole.hr) otvara Microsoft 365, Google Workspace for Education, CARNET info, Edutorij i e-Dnevnik ([CARNET id](https://www.carnet.hr/en/usluga/carnet-id/)). Canva for Education ne prijavljuje vas preko AAI@EduHr, ali adresu @skole.hr prihvaća kao dokaz da ste nastavnik. Za sve ostale alate iz tablice potreban je osobni račun, a s njim i osobni uvjeti korištenja.

U stupcu „Hrvatski“ riječ *izlaz* znači da alat piše na hrvatskom, ali da kvaliteta tog teksta (pravopis, ijekavica, srbizmi, anglizmi) za aktualne modele u trenutku pisanja ove knjige (studeni 2026.) nije neovisno izmjerena; zato vrijede postupci provjere iz poglavlja 8. Brojevi uz naziv alata vode na službene izvore.

*Tablica A.1. Kriteriji po alatu, stanje 2. studenoga 2026. Bez ukupne ocjene; redoslijed prati dostupnost preko AAI@EduHr i europski kontekst.*

#### Školski račun (AAI@EduHr, @skole.hr)

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Microsoft 365 A1<br>**ŠKOLSKA LICENCA**<br>izvori: [1](https://www.microsoft.com/en-us/education/products/copilot-in-education) [2](https://www.carnet.hr/obavijest-office-365-a1-edu-licence/) [3](https://www.carnet.hr/obavijest-o-koristenju-microsoft-365-aplikacija/) | 0 EUR (osigurava CARNET) | Word, Excel, PowerPoint samo na webu i mobitelu; Teams, Fokusirani čitač; OneDrive 50 GB (učenici 25 GB), bez dokupa. Copilot Chat, Study and Learn i Teach („Poduči“) Microsoft daje uz A1, ali je li Copilot Chat uključen na skole.hr, nije poznato *(provj.)*. Power Automate Free. | Reading Coach i Reading Progress; Study and Learn na popisu jezika; Learning Zone ne generira *(djel.)* | Zaštita podataka poduzeća, bez treniranja modela. Copilot Chat za učenike: ispod 13 blokiran, 13–17 samo ako ga administrator uključi ([izvor](https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/enable-copilot-chat-for-learners)) |
| Google Workspace for Education<br>**ŠKOLSKA LICENCA**<br>izvori: [1](https://www.carnet.hr/en/usluga/google-workspace/) [2](https://edu.google.com/intl/ALL_us/ai/gemini-for-education/) | 0 EUR (aktivira korisnik sam) | Classroom, Drive, Dokumenti; na skole.hr samo osnovne (Core) usluge. Gemini for Education i Gemini Notebook uključeni su bez naknade u sva izdanja, ali je li Gemini uključen na skole.hr, nije poznato *(provj.)*. | Gemini u Classroomu na jezicima Classrooma i Geminija; sučelje *(provj.)* | Bez ljudskog pregleda i treniranja. Sve dobi, uz dodatne zaštite ispod 18; nastavničke funkcije u Classroomu samo 18+ |
| Canva for Education<br>**BESPLATNO**<br>izvori: [1](https://www.canva.com/education/) [2](https://brain.hr/en/canva-education-sve-napredne-funkcionalnosti-dostupne-besplatno-za-nastavnike-i-ucenike/) | 0 EUR za nastavnike i učenike OŠ i SŠ | Provjera statusa adresom @skole.hr ili dokazom o zaposlenju, ponovno svake tri godine *(djel.)*. Canva AI (bivši Magic Studio) troši „uporabe“; točne kvote *(provj.)* | – | – |

#### Opći asistenti (osobni račun)

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| ChatGPT (OpenAI)<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://chatgpt.com/pricing) [2](https://help.openai.com/en/articles/20001354) [3](https://openai.com/policies/row-terms-of-use/) | Go 8 USD, Plus 20 USD (s PDV-om oko 23–24 EUR *(provj.)*), Pro od 100 USD | Free: tekst uz zaštite od zlouporabe, Study mode, projekti; ograničeni prijenosi, slike, glas i deep research; kontekst 27K tokena (oko 12 stranica). Mogući oglasi na Free i Go *(provj. za HR)*. Model: GPT-6 Sol za plaćene *(djel.)*, Luna za Free i Go *(provj.)* | izlaz | Treniranje na razgovorima dok se ne isključi; privremeni razgovor bez treniranja. 13+, ispod 18 uz dopuštenje roditelja |
| Gemini (Google, osobni)<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://gemini.google/hr/subscriptions/?hl=hr) [2](https://support.google.com/gemini/answer/13594961?hl=en) [3](https://9to5google.com/2026/10/13/gemini-app-4-argon/) | AI Plus 4,99 EUR, AI Pro 22,99 EUR (cijene za HR) | Bez plana: Flash-Lite u načinu Auto, kontekst 32K; Canvas, Deep Research, kvizovi, kartice, Audio Overviews, slike, Gemini Live. Gemini 4 Argon postupno stiže pretplatnicima AI Pro i Ultra; u EU-u *(provj.)* | izlaz | Uz uključen Keep Activity ljudi pregledavaju dio razgovora (čuvanje do 3 godine). 13+; plaćeni planovi u EGP-u 18+ |
| Claude (Anthropic)<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://claude.com/pricing) [2](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan) [3](https://www.anthropic.com/legal/consumer-terms) | Pro 20 USD mjesečno ili 17 USD uz godišnju naplatu (200 USD); EUR *(provj.)* | Free: Sonnet i Haiku (bez Opusa), ograničenje svakih 5 sati i tjedno; Artifacts, do 5 projekata, inkognito razgovori. Nema popusta za nastavnike | izlaz | Treniranje dok se ne isključi; inkognito bez treniranja. **18+**, nije za učenike OŠ i SŠ |
| Microsoft Copilot (potrošački)<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.microsoft.com/hr-hr/microsoft-365/buy/compare-all-microsoft-365-products) [2](https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot) [3](https://www.geekwire.com/2026/microsoft-unveils-all-in-one-copilot-app-taking-on-anthropic-and-openai-in-new-push-to-boost-adoption/) | M365 Personal 10 EUR/mj. (99 EUR/god.), Premium 23 EUR/mj. (229 EUR/god.) | Nova jedinstvena aplikacija od 18. 8. 2026.; Copilot Pro se više ne prodaje. Modeli u besplatnoj inačici *(provj.)* | – | Stara aplikacija: treniranje dok se ne isključi, EGP nije izuzet; 13+. Nova aplikacija: izuzeća, put izbornika i dob *(provj.)* |
| Mistral Vibe (bivši Le Chat)<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://mistral.ai/pricing) | Pro 14,99 USD; EUR *(provj.)*; studentski Pro 5,99 USD samo za studente | Free uz ograničenja. Europska tvrtka (Francuska) | izlaz | Isključivanje treniranja (opt-out) na tri od četiri plana *(djel.)*; za Free i najnižu dob *(provj.)* |
| Perplexity<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.perplexity.ai/help-center/en/articles/12590157-what-is-education-pro) [2](https://www.perplexity.ai/hub/legal/terms-of-service) | Pro 20 USD (17 uz godišnju naplatu) *(djel.)* | Neograničene brze pretrage, ograničen broj „Pro“ pretraga. Education Pro samo za sveučilišnu razinu, **ne** za OŠ i SŠ | – | Treniranje *(provj.)*. 13+, maloljetnici samo uz roditelja |
| DeepSeek<br>izvori: [1](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html) [2](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10097450) | – | Modeli V4-Pro i V4.1-Flash. Ne preporučuje se za bilo kakve podatke učenika | – | „Primarno za odrasle“, ispod 18 uz skrbnika. Talijansko tijelo za zaštitu podataka ograničilo je obradu (30. 1. 2025.) |
| Grok (xAI)<br>**ne preporučuje se za rad s učenicima**<br>izvori: [1](https://x.ai/legal/terms-of-service) [2](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_203) [3](https://www.commonsensemedia.org/press-releases/grok-ai-chatbot-not-safe-for-teens-common-sense-media-report-finds) [4](https://www.npr.org/2025/07/09/nx-s1-5462609/grok-elon-musk-antisemitic-racist-content) | planovi od 8 USD *(provj.)* | Uvjeti izrijekom navode grub jezik, seksualne situacije i nasilje. EK je 26. 1. 2026. otvorila postupak prema DSA-u; Common Sense Media: „not safe for teens“; antisemitski sadržaj 8. 7. 2025. | – | 13+, 13–17 uz roditelja; treniranje *(provj.)* |
| Meta AI<br>izvori: [1](https://www.france24.com/en/live-news/20250414-meta-to-train-ai-models-on-european-users-public-data) [2](https://techcrunch.com/2026/01/23/meta-pauses-teen-access-to-ai-characters-ahead-of-new-version/) | – | U WhatsAppu, Instagramu, Facebooku i Messengeru. Nije nastavni alat, ali je tema digitalne pismenosti: učenici ga susreću bez vlastite odluke | – | U EU-u trenira na javnim objavama odraslih (pravo prigovora); računi mlađih od 18 isključeni *(djel.)* |

#### Rad nad vlastitim izvorima

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Gemini Notebook (do 16. 7. 2026. NotebookLM)<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://support.google.com/gemininotebook/answer/17670842) [2](https://edu.google.com/intl/ALL_us/ai-gemini-notebook/) | uz AI Plus 2×, uz AI Pro 4× veća kvota | Kvota se obnavlja svakih 5 sati do tjednog maksimuma (fiksnih dnevnih brojki od 2. 9. 2026. nema); oko 50 izvora po bilježnici *(provj.)*; kvote u Workspace for Education *(provj.)* | izlaz (razgovor, vodiči, Audio i Video Overview) | U Workspace for Education bez treniranja, sve dobi ako ga administrator uključi; „Cinematic“ video samo engl. i 18+ |

#### Obrazovne platforme (američke)

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Khanmigo<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.khanmigo.ai/pricing) | obitelji 4 USD/mj. (SAD) | Za nastavnike besplatno; vrijedi li za Hrvatsku *(provj.)* | nije testiran | – |
| MagicSchool<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.magicschool.ai/pricing) | Plus 12,99 USD/mj. ili 99,96 USD godišnje | Free za pojedinačne nastavnike (80+ alata); Student Rooms nisu besplatni; američki standardi | neprovjereno | Ugovor o obradi (DPA) samo uz Enterprise |
| Brisk, Diffit, Curipod<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.briskteaching.com/plans) [2](https://curipod.com/pricing) [3](https://www.commonsensemedia.org/sites/default/files/featured-content/files/csm-ai-risk-assessment-ai-teacher-assistants-final.pdf) | Brisk plaćeno samo za škole; Diffit Premium oko 14,99 USD *(provj.)* | Brisk Free ograničen; Diffit osnovni plan; Curipod uz tjedna ograničenja | neprovjereno | Common Sense Media (2025.) testirao je Curipod (ne Brisk ni Diffit): ukupna ocjena UI asistenata za nastavnike „Moderate Risk“ |

#### Dizajn i prezentacije

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Gamma<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.eesel.ai/blog/gamma-pricing) | Plus 12 USD/mj. (9 uz godišnju naplatu; EU oko 10 EUR) *(provj.)* | 400 jednokratnih kredita koji se ne obnavljaju; do 10 slajdova | – | – |
| Napkin<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.napkin.ai/pricing) [2](https://brain.hr/wp-content/uploads/2026/03/Pregled-alata.pdf) | Plus 9 USD/mj. (godišnje) *(djel.)* | 500 kredita tjedno; izvoz s logotipom | – | CARNET: 13+ uz suglasnost roditelja, dakle alat za nastavnika |

#### Kvizovi, interakcija i ploče

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Wayground (do lipnja 2025. Quizizz)<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.softwareadvice.com/student-engagement/quizizz-profile/) | – | Besplatni plan s UI-jem; ograničen broj spremljenih resursa *(provj.)* | – | – |
| Kahoot!<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://kahoot.com/schools/plans/) | UI tek od Kahoot!+ Bronze; akcijske cijene do 8. 11. 2026. | Kahoot! Go besplatan, ali **bez UI-ja** | – | – |
| Mentimeter<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.mentimeter.com/plans/education) | Education Basic 8,99, Pro 14,99 USD po predavaču mjesečno (godišnja naplata) | 50 sudionika mjesečno; Menti AI uključen | – | – |
| Padlet<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://padlet.com/site/subscriptions) | Platinum 10 EUR/mj. ili 80 EUR/god. *(djel.)* | **3 padleta ukupno**, 20 MB po datoteci *(djel.)* | – | – |
| Wordwall<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://wordwall.net/price-plans) | Standard 5 EUR/mj. ili 40 EUR/god.; Pro 7,50 ili 60 EUR | **3 vlastite aktivnosti**; UI samo u plaćenim planovima | – | – |
| Genially<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://genially.com/plans/education/) | EduPro 4,99 EUR/mj. (samo godišnja naplata) | 500 UI kredita godišnje | – | – |

#### Glas, glazba i video (samo nastavnik)

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| ElevenLabs<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://elevenlabs.io/terms-of-use) [2](https://elevenlabs.io/pricing) | Starter 6 USD/mj. | 10.000 kredita mjesečno, nekomercijalno | podržan | **18+**, bez mogućnosti roditeljske privole |
| Suno<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://suno.com/terms-of-service) [2](https://suno.com/pricing) | Pro oko 10 USD/mj. | 50 kredita dnevno, nekomercijalno i uz navođenje | – | 18+ ili 13+ uz izričitu suglasnost roditelja; u EU-u iznad nacionalne dobi za privolu (HR 16) |
| HeyGen<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.heygen.com/terms) [2](https://www.heygen.com/pricing) | – | 3 videa mjesečno do 1 minute, s vodenim žigom | hrvatski glas | **18+** |
| Synthesia<br>izvor: [1](https://docs.synthesia.io/docs/supported-languages) | *(provj.)* | – | prijevod videa | dob *(provj.)* |

#### Pristupačnost i podrška učenju

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Goblin Tools<br>**BESPLATNO**<br>izvor: [1](https://goblin.tools/) | 0 EUR (web) | Bez registracije i oglasa; pazite na aplikacije koje ga oponašaju | višejezičan | – |
| Lexie (Omoguru)<br>**PLAĆENO**<br>izvor: [1](https://www.omoguru.com/hr/lexie-app/) | pretplata nakon probe *(djel.)* | 14 dana probe | hrvatski alat | odluku o uporabi s djetetom donosi stručni tim |
| Read&Write, Speechify<br>izvori: [1](https://www.everway.com/products/read-and-write-education/free-for-teachers/) [2](https://speechify.com/ai-audio/croatian/) | *(provj.)* | Read&Write: premium besplatan za nastavnike u SAD-u, izvan SAD-a *(provj.)*; Speechify besplatna razina *(provj.)* | na iOS-u (R&W); glasovi (Speechify) | – |

#### Pretraživanje literature

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Semantic Scholar<br>**BESPLATNO**<br>izvor: [1](https://www.semanticscholar.org/about) | 0 EUR | više od 200 mil. radova | pretežno engl. | – |
| ResearchRabbit<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://www.researchrabbit.ai/pricing) | RR+ 10 USD/mj. (godišnje) ili 12,50 mjesečno | do 50 polaznih radova | pretežno engl. | – |
| Elicit<br>**DJELOMIČNO BESPLATNO**<br>izvor: [1](https://elicit.com/pricing) | Pro 49 USD/mj. (godišnje) | Basic besplatan | pretežno engl. | – |
| Scite<br>**PLAĆENO**<br>izvor: [1](https://scite.ai/pricing) | Basic 12, Pro 40 USD/mj. (godišnje) | 7-dnevna proba s **automatskom naplatom** | pretežno engl. | – |

#### Jezik: pravopis i prevođenje

| Alat | Cijena za nastavnika | Besplatna razina i ograničenje | Hrvatski | Podaci i najniža dob |
|---|---|---|---|---|
| Ispravi.me (FER)<br>**BESPLATNO**<br>izvor: [1](https://ispravi.me/info/) | javne ustanove uz ugovor; za škole *(provj.)* | besplatan za osobnu uporabu i akademsku zajednicu | hrvatski alat | – |
| DeepL<br>**DJELOMIČNO BESPLATNO**<br>izvori: [1](https://www.deepl.com/en/privacy) [2](https://developers.deepl.com/docs/resources/roadmap-and-release-notes) | Pro (ne pohranjuje trajno tekstove) | Besplatni DeepL **ne smije** primati tekstove s osobnim podacima | podržan od 8. 1. 2026. | Besplatna inačica može rabiti tekstove za poboljšanje modela |
| Grammarly<br>izvor: [1](https://support.grammarly.com/hc/en-us/articles/115000090971-Does-Grammarly-support-languages-other-than-English) | – | – | **ne podržava** | – |

Tri službene stranice cijena koje se najčešće mijenjaju: [planovi ChatGPT-a](https://chatgpt.com/pricing), [Googleovi planovi za Hrvatsku](https://gemini.google/hr/subscriptions/?hl=hr) i [planovi Claudea](https://claude.com/pricing).

**Kad prvi izbor nije dostupan.** Ako školski račun nema uključen UI asistent, a ne želite ovisiti o jednom američkom dobavljaču, preporučeni redoslijed alternativa jest: potrošački **Microsoft Copilot** (isti ekosustav kao školski račun, ali osobni uvjeti), **Mistral Vibe** (europska tvrtka, kvaliteta na hrvatskom nije neovisno mjerena), **Grok** samo kao primjer u raspravi o procjeni alata, nikad za rad s učenicima, i na kraju **lokalni modeli** u LM Studiju ili Ollami (odjeljak [Lokalni modeli](#lokalni-modeli)), kod kojih podaci ne napuštaju vaše računalo. Od svih kategorija iz tablice jedna je u trenutku pisanja ove knjige (studeni 2026.) pedagoški najvažnija, pa joj dajemo vlastitu tablicu.

## Tutorski načini

Tutorski način mijenja ponašanje asistenta: umjesto gotovog odgovora postavlja pitanja, daje savjete i provjerava razumijevanje. Istraživanja sažeta u poglavlju 14 upozoravaju da neograničen „stroj za odgovore“ može naštetiti učenju, a da pedagoške zaštite tu štetu uglavnom uklanjaju. Tablica A.2 pokazuje gdje se takav način u trenutku pisanja ove knjige (studeni 2026.) nalazi i pod kojim uvjetom.

*Tablica A.2. Tutorski načini po dobavljaču, studeni 2026.*

| Dobavljač | Naziv | Gdje i pod kojim uvjetom |
|---|---|---|
| Microsoft | Study and Learn Agent | školski račun A1/A3/A5 uz uključen Copilot Chat; za učenike K–12 predodabran; hrvatski na popisu jezika (kvaliteta nije ocijenjena) |
| OpenAI | Study mode | svi planovi ChatGPT-a, uključujući Free *(djel.)* |
| Google | Guided Learning (LearnLM) | aplikacija Gemini, gumb **Learn** ili **More tools → Guided Learning**; integracija OpenStax samo engl., SAD, 18+ *(djel.)* |
| Anthropic | learning mode | Claude for Education (sveučilišta); u potrošačkim planovima *(provj.)* |
| Perplexity | Learn Mode | dostupnost proturječna *(provj.)* |

Izvori: [Microsoft: Study and Learn Agent](https://support.microsoft.com/en-us/education/copilot/study-learn-agent), [OpenAI: Study mode](https://chatgpt.com/features/study-mode/), [Google: learning tools in Gemini Apps](https://support.google.com/gemini/answer/16448384).

Za učenike OŠ i SŠ u Hrvatskoj u obzir dolazi samo prvi redak, i to tek ako je Copilot Chat na školskom računu uključen. Ostali tutorski načini žive na osobnim računima, a za njih vrijede dobne granice iz sljedećeg odjeljka.

## Dob i privatnost po alatu

Tablica A.3 sažima što piše u uvjetima korištenja i kako se isključuje treniranje na vašim razgovorima. Putanje izbornika navodimo onako kako glase u engleskom sučelju; ako imate hrvatsko, potražite dio postavki o privatnosti ili podacima.

*Tablica A.3. Najniža dob prema uvjetima i postupanje s razgovorima na osobnim računima, studeni 2026.*

| Alat | Najniža dob (uvjeti) | Treniranje na razgovorima | Kako isključiti ili sigurniji način |
|---|---|---|---|
| ChatGPT | 13+, ispod 18 uz roditelja | da, dok se ne isključi | **Settings → Data controls →** „Improve the model for everyone“; **Temporary chat**. Roditeljski nadzor ne prikazuje roditelju razgovore |
| Gemini (osobni) | 13+; plaćeni planovi u EGP-u 18+ | da, ako je Keep Activity uključen | isključiti Keep Activity (razgovori se tada čuvaju 72 sata); privremeni razgovor; zadano automatsko brisanje nakon 18 mjeseci |
| Claude | **18+** | da, dok se ne isključi | postavke privatnosti; inkognito razgovor |
| Copilot (osobni, stara aplikacija) | 13+ | da, dok se ne isključi; EGP nije izuzet | copilot.com → profil → **Privacy** → „Training on conversation activity“ i „Training on voice conversations“. Nova aplikacija *(provj.)* |
| M365 Copilot Chat (školski) | ispod 13 nedostupan; 13–17 ako administrator uključi | **ne** (zaštita podataka poduzeća) | – |
| Gemini for Education (školski) | sve dobi, zaštite ispod 18 | **ne** | – |
| Perplexity | 13+ uz roditelja | *(provj.)* | – |
| DeepSeek | „primarno za odrasle“ | *(provj.)* | ne unositi nikakve podatke |
| Grok | 13+ uz roditelja | *(provj.)* | ne preporučuje se |
| ElevenLabs, HeyGen | **18+** | – | samo nastavnik |
| Suno | 18+ ili 13+ uz suglasnost roditelja | – | samo nastavnik |

Izvori: [OpenAI: kako se podaci rabe za poboljšanje modela](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance), [OpenAI: roditeljski nadzor](https://help.openai.com/en/articles/12315553-managing-parental-controls-in-chatgpt), [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en), [Anthropic: treniranje modela](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training), [Microsoft Copilot: privacy FAQ](https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot), [Microsoft: Copilot Chat za učenike](https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/enable-copilot-chat-for-learners).

Dvije napomene vrijede za sve retke. Prva je hrvatsko pravilo: privola za usluge informacijskog društva valjana je tek od **16 godina** (čl. 19. Zakona o provedbi Opće uredbe o zaštiti podataka, NN 42/2018), pa „13+“ u američkim uvjetima ne znači da trinaestogodišnjak u Hrvatskoj smije sam otvoriti račun (poglavlje 4). Druga je gumb s palcem: **palac gore ili dolje šalje cijeli razgovor dobavljaču i kad je treniranje isključeno**, a kod Claudea se takve povratne informacije čuvaju do pet godina ([uvjeti korištenja](https://www.anthropic.com/legal/consumer-terms)).

> **Isključeno treniranje nije dopuštenje**
>
> Isključivanje treniranja smanjuje rizik, ali ne pretvara osobni račun u školski alat. AZOP preporučuje da se osobni podaci ne unose ni uz isključeno treniranje, osim u prethodno procijenjen, organizacijski kontroliran alat ([AZOP-ova preporuka](https://azop.hr/preporuka-za-sigurno-koristenje-llm-alata/)), a CARNET-ove Smjernice isključuju alate bez ugovorne kontrole nad podacima učenika ([Smjernice, PDF](https://brain.hr/wp-content/uploads/2026/04/Smjernice-za-primjenu-AI.pdf)).

S time je rečeno što alati smiju s podacima. Ostaje pitanje koliko stoje.

## Financijske razine

Stvarni proračun hrvatskog nastavnika za UI alate iznosi nula eura: škole plaćene alate sustavno ne nabavljaju, a pretplate u pravilu ne nadoknađuju. Zato je svaki recept u knjizi izvediv besplatno. Tablica A.4 pokazuje što donosi svaka sljedeća razina. Razine smo objasnili i slikovno prikazali u poglavlju 5, pa ovdje stoje samo brojke.

*Tablica A.4. Financijske razine za nastavnika, studeni 2026. Iznosi u EUR s PDV-om ondje gdje ih dobavljač tako prikazuje; USD bez PDV-a.*

| Razina | Što dobivate | Ograda |
|---|---|---|
| **0 EUR** | Školski račun (M365 A1 i Google Workspace for Education), besplatne razine općih asistenata, Gemini Notebook na osobnom računu, Canva for Education, besplatni planovi alata za kvizove i ploče, Goblin Tools, Ispravi.me, DeepL Free, Gemini API besplatni sloj, Apps Script, Colab, lokalni modeli | dovoljno za sve recepte u knjizi; UI na školskom računu *(provj.)* |
| **oko 5 EUR** | Google AI Plus 4,99 EUR/mj. (400 GB, dvostruka kvota Gemini Notebooka, Flash model); Wordwall Standard 5 EUR/mj. ili 40 EUR/god.; Genially EduPro 4,99 EUR/mj. | gubi li AI Plus pristup Pro modelu *(provj.)* |
| **oko 10 EUR** | Microsoft 365 Personal 10 EUR/mj. ili 99 EUR/god. (Copilot u Wordu, Excelu, PowerPointu, Outlooku i OneNoteu, veća kvota); ChatGPT Go 8 USD (mogući oglasi); Padlet Platinum 10 EUR/mj.; MagicSchool Plus 12,99 USD | Mistral Pro (14,99 USD) stoji između razina |
| **oko 23 EUR** | Google AI Pro 22,99 EUR/mj.; Microsoft 365 Premium 23 EUR/mj. ili 229 EUR/god.; ChatGPT Plus 20 USD; Claude Pro 20 USD (17 uz godišnju naplatu); Perplexity Pro 20 USD *(djel.)* | EUR za ChatGPT Plus i Claude Pro *(provj.)* |

Izvori: [Google AI planovi za HR](https://gemini.google/hr/subscriptions/?hl=hr), [Microsoft 365 za HR](https://www.microsoft.com/hr-hr/microsoft-365/buy/compare-all-microsoft-365-products), [ChatGPT](https://chatgpt.com/pricing), [Claude](https://claude.com/pricing), [Wordwall](https://wordwall.net/price-plans), [Genially](https://genially.com/plans/education/), [Padlet](https://padlet.com/site/subscriptions), [MagicSchool](https://www.magicschool.ai/pricing), [Mistral](https://mistral.ai/pricing).

Godišnje jedna pretplata najviše razine stoji **oko 230–290 EUR** (Google AI Pro oko 276 EUR, M365 Premium 229 EUR, ChatGPT Plus prema procjeni 276–288 EUR), dok M365 Personal stoji 99 EUR, a Google AI Plus oko 60 EUR godišnje. Pretplate iznad toga (ChatGPT Pro od 100 USD, Claude Max i Ultra 100 i 200 USD, Google AI Ultra 106,05 ili 229,99 EUR) nisu namijenjene nastavnicima.

> **Pet zamki na blagajni**
>
> 1. **Automatska obnova** nakon probe: Scite nakon sedam dana, Diffit nakon šezdeset, Googleova studentska godina nakon dvanaest mjeseci.
> 2. **Akcijske cijene** (npr. Kahoot! do 8. 11. 2026.) pri obnovi se vraćaju na punu cijenu.
> 3. **Samo godišnja naplata**: Genially, Mentimeter Pro i, prema čestim pitanjima, Kahoot!.
> 4. **Besplatne razine s tvrdim stropom**: Padlet 3 ploče ukupno, Wordwall 3 aktivnosti (brisanje ne vraća mjesto), Gamma 400 kredita jednom zauvijek, Kahoot! Go bez UI-ja, Mentimeter 50 sudionika mjesečno.
> 5. **Hrvatski troši više tokena** (oko 1,5 puta više od engleskog), pa besplatne kvote brže nestaju.
>
> Najviše jedna pretplata, mjesečna, i to tek kad stalno nailazite na ograničenja. Plaćeni privatni račun **ne rješava zaštitu podataka učenika**.

Za ustanove vrijede drukčije cijene i drukčiji ugovori, o čemu govori sljedeći odjeljak.

## Školske i institucijske licence

Sustavnu nabavu plaćenih UI alata za hrvatske škole u trenutku pisanja ove knjige (studeni 2026.) nismo pronašli, a nastavnici u istraživanju projekta BrAIn traže upravo „osiguravanje trajnih licenci i preporuke o alatima“ ([sažetak nalaza istraživanja BrAIn](https://brain.hr/wp-content/uploads/2026/03/BrAIn_istrazivanje_nalazi.pdf)). Tablica A.5 zato služi ravnatelju ili aktivu koji o nabavi razgovara s osnivačem.

*Tablica A.5. Školske i institucijske licence, studeni 2026.*

| Ponuda | Cijena | Stanje u RH |
|---|---|---|
| M365 Copilot Chat, Study and Learn, Teach | bez naknade uz A1/A3/A5 | ovisi o CARNET-u *(provj.)* |
| Microsoft 365 Copilot (puni) | 18 USD po korisniku mjesečno (akademski, cijena iz listopada 2025.) | nema naznaka nabave |
| Gemini for Education, Gemini Notebook, Classroom | bez naknade u svim izdanjima Workspace for Education | ovisi o CARNET-u *(provj.)* |
| Google AI Pro for Education | 20 USD po korisniku mjesečno uz godišnju, 24 USD uz mjesečnu naplatu; samo 18+; kupuje ustanova | nema naznaka nabave |
| ChatGPT Edu | bez javne cijene; primjer: Politecnico di Torino 103,12 EUR godišnje po korisniku, osobna licenca koju plaća podnositelj | – |
| Claude for Education | ugovara ustanova (sveučilišta) | – |
| Padlet for Schools | od 700 EUR godišnje (10 nastavnika) *(djel.)* | – |
| Mentimeter Education | Basic 8,99, Pro 14,99 USD po predavaču mjesečno (godišnje) | – |
| Canva for Education | besplatno (OŠ i SŠ) | dostupno uz @skole.hr |

Izvori: [Microsoft 365 Copilot, akademska ponuda](https://www.microsoft.com/en-us/education/blog/2025/10/designing-microsoft-365-copilot-to-empower-educators-students-and-staff/), [Google AI Pro for Education](https://knowledge.workspace.google.com/admin/generative-ai/workspace-with-gemini/ai-pro-for-education), [izdanja Workspace for Education](https://edu.google.com/intl/ALL_us/workspace-for-education/editions/compare-editions/), [Politecnico di Torino: ChatGPT Edu](https://it.polito.it/en/support/manuals/activation-of-the-chatgpt-edu-service-for-faculty-and-staff), [Padlet](https://padlet.com/site/subscriptions), [Mentimeter](https://www.mentimeter.com/plans/education).

Jedna se zabluda ponavlja u radionicama: „to je besplatno za nastavnike“. ChatGPT for Teachers, Claude for Teachers i Googleov program s ISTE-om vezani su uz američku verifikaciju i **ne vrijede u Hrvatskoj** ([ChatGPT for Teachers](https://twitter.com/OpenAI/status/1991218197530378431), [Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)). Hrvatskom nastavniku dostupni su njihovi besplatni tečajevi (odjeljak [Tečajevi i UI pismenost](#tečajevi-i-ui-pismenost)), ne radni prostori. Licence se mijenjaju sporije od proizvoda. Proizvodi se, kako pokazuje sljedeći odjeljak, mijenjaju svakih nekoliko tjedana.

## Preimenovano, ugašeno, gasi se

Samo 2026. godina i samo veliki dobavljači donose četrnaest promjena. Zbog toga knjiga uči kategorije (opći asistent, bilježnica nad izvorima, tutorski način, prilagođeni asistent), a ne proizvode: kategorija preživi preimenovanje, gumb ne. Tablica A.6 uz svaku promjenu navodi što učiniti s vlastitim materijalima i skriptama.

*Tablica A.6. Što se promijenilo i što učiniti, studeni 2026.*

| Prije | Sada | Datum | Što učiniti |
|---|---|---|---|
| NotebookLM | Gemini Notebook (notebook.google) | 16. 7. 2026. | stare poveznice preusmjeravaju; od 23. 10. 2026. i povezana aplikacija u Geminiju |
| Le Chat (Mistral) | Vibe | oko svibnja 2026. *(djel.)* | ista adresa chat.mistral.ai |
| Quizizz | Wayground | lipanj 2025. | u knjizi: Wayground |
| Magic Studio (Canva) | Canva AI | – | u knjizi: Canva AI |
| Sora (OpenAI) | ugašena; OpenAI nema potrošačko generiranje videa | 26. 4. 2026. *(djel.)* | video: Google Flow uz plaćeni plan |
| DALL·E 2 i 3 u API-ju | ChatGPT Images 2.5; API `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | 12. 5. 2026. | promijeniti ID u skriptama |
| `gpt-image-1`; `gpt-image-1-mini` | isto kao gore | 23. 10. 2026.; 1. 12. 2026. | promijeniti ID prije gašenja |
| GPT-4o, GPT-4.1, GPT-4.1 mini, o4-mini u ChatGPT-u | GPT-6 (Sol, Luna) | 13. 2. 2026. | stari primjeri s GPT-4o su zastarjeli |
| Custom GPT-ovi | dodaci (engl. *plugins*: vještine, MCP-poslužitelji) | gašenje 11. 12. 2026. *(provj.)* | prenose se upute i datoteke, ne model, akcije, dijeljenje ni razgovori; upute čuvajte kao tekst (poglavlje 20) |
| Gemovi (osobni računi) | vještine (engl. *skills*) | prijelaz 17. 11., uklanjanje 17. 12. 2026. *(provj.)* | u EU-u, plan i dob *(provj.)* |
| Gemovi (Workspace for Education) | vještine | ne prije 1. 6. 2027. | Gemovi iz Classrooma postaju vještine kao nacrti |
| Opal, Gems by Google Labs | gase se | studeni 2026. | izvesti upute na vrijeme |
| Excel `=COPILOT()` | ukinuto; formule vraćaju `#NAME?` | 14. 9. 2026. | primjere izbaciti iz radnih tablica |
| Gemini CLI s osobnim računom | Antigravity CLI (naziv naredbe *(provj.)*) | 18. 6. 2026. | s osobnim računom više ne radi; prijeći na Antigravity CLI |
| ChatGPT agent | ChatGPT Work | 9. 7. 2026. *(provj.)* | na Free i Go ograničeno |
| Copilot Pro (potrošački) | Microsoft 365 Premium; nova aplikacija Copilot | 18. 8. 2026. | postavke privatnosti provjeriti iznova *(provj.)* |

**Vremenska crta 2026.** (slika A.1 u knjizi; datumi nakon 2. studenoga 2026. su najave dobavljača):

| Razdoblje | Promjene |
|---|---|
| Siječanj – ožujak | **13. 2.** GPT-4o izlazi iz ChatGPT-a |
| Travanj – lipanj | **26. 4.** Sora ugašena · **12. 5.** DALL·E ugašen u API-ju · **svibanj** Le Chat postaje Vibe · **18. 6.** Gemini CLI bez osobnog računa |
| Srpanj – rujan | **9. 7.** ChatGPT agent postaje ChatGPT Work · **16. 7.** NotebookLM postaje Gemini Notebook · **18. 8.** nova aplikacija Copilot · **14. 9.** Excelov `=COPILOT()` ukinut |
| Listopad – prosinac | **23. 10.** gpt-image-1 ugašen · **17. 11.** Gemovi prelaze u vještine · **1. 12.** gpt-image-1-mini ugašen · **11. 12.** custom GPT-ovi se gase · **17. 12.** Gemovi uklonjeni |

Izvori: [NotebookLM postaje Gemini Notebook](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html), [Mistral: novosti](https://mistral.ai/news), [Sora 2](https://openai.com/index/sora-2/), [GPT Images 2.5](https://community.openai.com/t/introducing-gpt-images-2-5-in-the-api-and-chatgpt/1395897), [povlačenje GPT-4o](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models), [gašenje custom GPT-ova](https://help.openai.com/en/articles/20001519), [Virtualization Review o custom GPT-ovima](https://virtualizationreview.com/articles/2026/09/28/openai-to-retire-custom-gpts-replace-them-with-plugins.aspx), [Gemovi u vještine](https://support.google.com/gemini/answer/18560919?hl=en), [Gemovi u Classroomu](https://support.google.com/edu/classroom/answer/16534159), [funkcija COPILOT](https://support.microsoft.com/en-us/excel/functions/copilot-function), [Gemini CLI](https://github.com/google-gemini/gemini-cli/discussions/28017), [ChatGPT Work](https://www.digitalapplied.com/blog/chatgpt-work-openai-agent-launch-2026).

Najviše takvih promjena pogađa one koji grade vlastite alate, pa im posvećujemo sljedeća dva odjeljka.

## Automatizacija i gradnja

Poglavlja 21, 22, 24 i 25 opisuju tijekove rada koji ne ovise o proizvodu. Ovdje bilježimo granice samih proizvoda u studenome 2026. Kvote Apps Scripta navodimo odmah, a ostale alate u tablici A.7.

**Google Apps Script.** Kvote za račun gmail.com i za Workspace: jedno izvršavanje traje najviše **6 minuta**; UrlFetch 20.000 odnosno 100.000 poziva dnevno; e-pošta najviše **100 odnosno 1.500 primatelja dnevno**; okidači ukupno 90 minuta odnosno 6 sati dnevno; na gmail.com 250 dokumenata dnevno ([kvote Apps Scripta](https://developers.google.com/apps-script/guides/services/quotas)). API ključ čuva se u **Project Settings → Script properties**, nikad u kȏdu.

*Tablica A.7. Automatizacija bez kȏda i alati za gradnju, studeni 2026.*

#### Tijekovi bez kȏda

| Alat | Besplatno i ograničenje | Plaćeno i napomena |
|---|---|---|
| Power Automate Free | besplatno za školske (Entra) račune; tokovi u oblaku bez dijeljenja, samo standardni konektori | premium konektori i AI Builder plaćeni |
| Zapier | 100 zadataka mjesečno, samo dvokoračni tokovi | Professional od 19,99 USD (godišnje); „AI by Zapier“ samo plaćeno |
| Make | 1.000 kredita mjesečno | broj aktivnih scenarija i cijena Core *(provj.)* |
| n8n | Community Edition besplatna za internu i osobnu uporabu („fair-code“, nije OSI otvoreni kȏd) | oblak: Starter 20 EUR/mj. (godišnje, 2.500 izvršavanja) |
| Google Sheets `=AI()` | – | samo web, **hrvatski nije podržan**; od obrazovnih samo uz AI Pro for Education |

#### Aplikacija iz opisa

| Alat | Besplatno i ograničenje | Plaćeno i napomena |
|---|---|---|
| Gemini Canvas | u besplatnom planu i u Education Fundamentals; izvoz u Docs, Slides i Colab | **svatko s javnom poveznicom može vidjeti i uređivati podatke povezane s aplikacijom**; UI značajke u aplikaciji 18+ |
| Google AI Studio Build | prve dvije aplikacije na Google Cloudu besplatno, bez kartice (novi korisnici) | – |
| Claude Artifacts | na Free *(djel.)*; korištenje objavljenog artefakta troši kvotu korisnika, ne autora | dijeljenje poveznicom sa svakim samo na plaćenim planovima |
| Lovable, Bolt.new, v0, Replit | mali besplatni slojevi (Lovable 5 kredita dnevno, Bolt.new 300.000 tokena dnevno, v0 7 poruka dnevno) | Replit Core 20 USD; besplatni plan *(provj.)* |

#### Asistenti za programiranje

| Alat | Besplatno i ograničenje | Plaćeno i napomena |
|---|---|---|
| Claude Code | **ne** na Free | Pro i više; proširenje za VS Code (1.94.0+) traži pretplatu ili Claude Console |
| OpenAI Codex | na Free i Go samo GPT-6 Luna u aplikaciji za računalo *(djel.)* | svi planovi ChatGPT-a |
| GitHub Copilot Pro | besplatan za verificirane nastavnike akreditiranih ustanova; za OŠ i SŠ *(provj.)* | 10 USD/mj.; učenici: Copilot Student |
| Cursor | Free | Plus 8 USD (samo modeli Grok), Premium 30 USD |
| Google Colab | besplatan; GPU strogo ograničen, sesija najviše 12 sati | Gemini u Colabu 18+, upiti se čuvaju do 18 mjeseci uz mogući ljudski pregled |

Izvori: [Power Automate](https://learn.microsoft.com/en-us/power-platform/admin/power-automate-licensing/types), [Zapier](https://zapier.com/pricing), [Make](https://www.make.com/en/pricing), [n8n: cijene](https://n8n.io/pricing/), [n8n: licencija](https://docs.n8n.io/n8n-community-license), [Fill with Gemini: jezici](https://workspaceupdates.googleblog.com/2026/07/fill-with-gemini-in-sheets-now-available-in-11-additional-languages.html), [Gemini Canvas](https://support.google.com/gemini/answer/16047321?hl=en), [Google AI Studio](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/), [Claude Artifacts: dijeljenje](https://support.claude.com/en/articles/9547008-share-artifacts), [Lovable](https://lovable.dev/pricing), [Bolt.new](https://bolt.new/pricing), [v0](https://v0.app/pricing), [Replit](https://replit.com/pricing), [Claude Code](https://claude.com/product/claude-code), [Claude Code u VS Codeu](https://code.claude.com/docs/en/vs-code), [Codex](https://learn.chatgpt.com/docs/pricing), [GitHub za nastavnike](https://github.com/education/teachers), [Cursor](https://cursor.com/pricing), [Colab FAQ](https://research.google.com/colaboratory/faq.html).

Za tok „novi odgovor u obrascu, UI sažetak, e-pošta nastavniku“ besplatni Zapier ne dostaje jer tok ima više od dva koraka, pa za besplatan rad ostaju Make, Power Automate Free na školskom računu i Apps Script.

**Agentski načini.** **ChatGPT Work** (od 9. 7. 2026.) zamijenio je ChatGPT agent; preglednik u oblaku nije dostupan na planovima Free ni Go *(provj.)*. **Claude in Chrome** i **Claude Cowork** dolaze uz sve plaćene planove, ne uz Free; Anthropic izrijekom upozorava na ubacivanje uputa (engl. *prompt injection*) i savjetuje da se agent ne rabi za bankarstvo i osjetljive podatke ([Claude in Chrome](https://claude.com/claude-in-chrome), [Claude Cowork](https://claude.com/blog/cowork-research-preview)). Googleove agentske radnje („tasks“) **nisu dostupne u EGP-u, dakle ni u Hrvatskoj**, bez obzira na plan ([Tasks in Gemini Apps](https://support.google.com/gemini/answer/17094507?hl=en)). Pravilo iz poglavlja 25 ostaje: agenti samo za niskorizične zadatke na javnim stranicama, nikad s e-Dnevnikom ni s podacima učenika.

Kad tijek rada preraste klikanje, prelazi u skriptu koja poziva API. Tu se nazivi mijenjaju najbrže.

## API: krajnje točke, ID-jevi i cijene

U poglavlju 23 sve što ovisi o dobavljaču stoji u jednoj konstanti `POSTAVKE` na vrhu skripte. Kad dobavljač ugasi model, mijenjate **samo redak `model`** (i redak `cijena` ako pratite trošak); ako mijenjate dobavljača, mijenjate još i `dobavljac`, `osnovniUrl` i `svojstvoKljuca`. Tablica A.8 donosi vrijednosti za ta polja, provjerene 2. studenoga 2026.

*Tablica A.8. Krajnje točke, autentifikacija i strukturirani izlaz, studeni 2026.*

| Dobavljač | Krajnja točka i zaglavlja | Strukturirani izlaz |
|---|---|---|
| Gemini, generateContent | `POST .../v1beta/models/{model}:generateContent` na `generativelanguage.googleapis.com`; ključ u zaglavlju `x-goog-api-key` ili kao `?key=` *(provj.)* | `generationConfig.responseMimeType = "application/json"` uz `responseSchema` |
| Gemini, Interactions | `POST .../v1beta/interactions`; zaglavlje `x-goog-api-key`; tijelo `{"model", "input"}` | `response_format` s `mime_type` i `schema` |
| Claude, Messages | `POST https://api.anthropic.com/v1/messages`; `x-api-key`, `anthropic-version: 2023-06-01` | `output_config.format` s `type: json_schema`; stari `output_format` je zastario |
| OpenAI, Responses | `POST https://api.openai.com/v1/responses`; `Authorization: Bearer` | `text.format` s `type: json_schema`, `strict: true` |

Izvori: [Gemini API: generateContent](https://ai.google.dev/api/generate-content), [Gemini API: Interactions](https://ai.google.dev/gemini-api/docs/text-generation), [Gemini API: strukturirani izlaz](https://ai.google.dev/gemini-api/docs/structured-output), [Claude: strukturirani izlaz](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [OpenAI: strukturirani izlaz](https://developers.openai.com/api/docs/guides/structured-outputs).

**ID-jevi modela.** Kod Geminija su stabilni `gemini-4-argon` (vodeći), `gemini-3.8-flash`, `gemini-3.6-flash`, `gemini-3.5-flash-lite` i `gemini-3.1-flash-lite`; u pretpregledu su `gemini-3.1-pro-preview` i `gemini-3-flash-preview`. Ugašeni su `gemini-2.0-flash`, `gemini-3-pro-preview` i `gemini-3.1-flash-lite-preview`, a Gemini 2.5 radi samo dotadašnjim korisnicima. Alias `gemini-flash-latest` mijenja se uz najavu dva tjedna unaprijed ([Gemini API: modeli](https://ai.google.dev/gemini-api/docs/models)). Gemini 4 i modeli 3.6 i noviji **zanemaruju `temperature`, `top_p` i `top_k`**; za sada uz upozorenje, a u budućnosti uz pogrešku 400 ([Gemini API: strategije upita](https://ai.google.dev/gemini-api/docs/prompting-strategies)). Kod Claudea su ID-jevi `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5` i `claude-fable-5-1`, s kontekstom do milijun tokena ovisno o modelu ([pregled modela](https://platform.claude.com/docs/en/about-claude/models/overview)); za upravljanje računalom modeli 5.5 rabe isključivo alat `computer_toolset_20260801` ([computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)). Kod OpenAI-ja ID-jevi i cijene stoje u tablici A.9; `chatgpt-4o-latest` ugašen je 17. 2. 2026., a ostale snimke GPT-4o rade do 14. 1. 2027.

Cijene su sa službenih stranica: [cijene Gemini API-ja](https://ai.google.dev/gemini-api/docs/pricing), [cijene Claudea](https://claude.com/pricing) i [cijene OpenAI API-ja](https://developers.openai.com/api/docs/pricing).

*Tablica A.9. Cijene API-ja u USD za milijun tokena (ulaz / izlaz), standardni način, studeni 2026. Skupna obrada (Batch) kod sva tri dobavljača oko 50 % je jeftinija.*

| Model (ID) | Ulaz / izlaz | Napomena |
|---|---|---|
| `gemini-3.1-flash-lite` | 0,25 / 1,50 | besplatni sloj; Batch 0,125 / 0,75 |
| `gemini-3.5-flash-lite` | 0,30 / 2,50 | besplatni sloj |
| `gemini-3.8-flash`, `gemini-3.6-flash` | 0,75 / 3,75 | **od 1. 1. 2027.: 1,50 / 7,50** |
| `gemini-4-argon` | 2 / 10 | **od 1. 12. 2026.: 4 / 20**; bez besplatnog sloja |
| `claude-haiku-5-5` | 0,10 / 0,50 do 100K; 0,50 / 2,50 iznad | nema besplatnog sloja *(djel.)* |
| `claude-sonnet-5-5` | 2 / 10 | |
| `claude-opus-5-5` | 4 / 20 | |
| `claude-fable-5-1` | 10 / 50 | |
| `gpt-5-nano` | 0,05 / 0,40 | cijene OpenAI-ja za kratki kontekst (do 272K) |
| `gpt-6-luna` | 0,10 / 0,50 | |
| `gpt-5-mini` | 0,25 / 2,00 | |
| `gpt-6.1-terra` | 1 / 5 | |
| `gpt-6.1-sol` | 2 / 10 | |
| `gpt-6-astra` | 10 / 50 | Batch i Flex oko 50 % jeftiniji |

**Trideset listića.** Izračun iz poglavlja 23: 30 personaliziranih radnih listića po 1.000 ulaznih i 1.500 izlaznih tokena čine 30.000 ulaznih i 45.000 izlaznih tokena. Na `gemini-3.1-flash-lite` to je oko **0,075 USD**, na `claude-haiku-5-5` oko 0,026 USD, na `gpt-5-nano` oko 0,02 USD. Modeli za rasuđivanje naplaćuju tokene rasuđivanja kao izlaz, pa stvarni trošak može biti višestruko veći, a hrvatski tekst troši oko 1,5 puta više tokena od engleskog. Postavite limit potrošnje na računu.

> **Besplatni sloj Gemini API-ja**
>
> Prema cjeniku Google sadržaj iz besplatnog sloja rabi za poboljšanje svojih proizvoda, uz mogući ljudski pregled ([cjenik Gemini API-ja](https://ai.google.dev/gemini-api/docs/pricing)). Dodatni uvjeti Gemini API-ja od 23. 3. 2026. za korisnike u EGP-u, Švicarskoj i UK-u i u besplatnom sloju primjenjuju pravila plaćenog sloja ([dodatni uvjeti](https://ai.google.dev/gemini-api/terms)) *(djel., provj. prije objave)*. U svakom slučaju, osobni podaci učenika ne idu u API ni na jednom sloju.

Postoji i put na kojem nema ni ključa ni računa ni cjenika: model na vlastitom računalu.

## Lokalni modeli

U poglavlju 27 naučili smo razlikovati tri stvari koje se često miješaju: program *otvorenog kȏda*, model *otvorenih težina* s vlastitom licencom i *besplatan, ali zatvoren* program. Tablica A.10 primjenjuje tu podjelu na stanje u studenome 2026.

*Tablica A.10. Programi i modeli za rad na vlastitom računalu, studeni 2026.*

| Naziv | Vrsta i licenca | Napomena |
|---|---|---|
| Ollama | program, otvoreni kȏd (MIT), besplatan | naredbeni redak i lokalni API na `localhost:11434`; oznaka `:cloud` znači izvršavanje **u oblaku**; plaćeni oblak Pro 20 USD, Max 100 USD |
| LM Studio | program, besplatan i za poslovnu uporabu (od 8. 7. 2025.) | **zatvoreni kȏd**: besplatan ne znači otvoren |
| Jan | program, otvoreni kȏd (Apache 2.0) | radi bez mreže, poslužitelj na `localhost:1337`, podržava MCP |
| Gemma 4 (Google) | model otvorenih težina, Apache 2.0 | veličine E2B, E4B (128K), 26B MoE, 31B (256K); `gemma4` u Ollami je E4B; zvuk samo E2B i E4B; 12B samo u Ollami (podrijetlo *(provj.)*) |
| gpt-oss (OpenAI) | otvorene težine, Apache 2.0 | `gpt-oss:20b` oko 14 GB, za računalo sa 16 GB memorije; `gpt-oss:120b` |
| Qwen, Mistral Small | otvorene težine, vlastite licence | Qwen 3.5, 3.6, 3.8; Mistral Small 3.2 (24B) |

Izvori: [Ollama: knjižnica](https://ollama.com/library), [Ollama: cijene](https://ollama.com/pricing), [LM Studio besplatan za posao](https://lmstudio.ai/blog/free-for-work), [Jan](https://github.com/janhq/jan), [Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/), [gemma4 u Ollami](https://ollama.com/library/gemma4), [gpt-oss u Ollami](https://ollama.com/library/gpt-oss).

Okvirno, uz četverobitnu kvantizaciju *(djel.)*: s 8 GB memorije Gemma 4 E2B ili E4B ili Qwen 3.5 4B; sa 16 GB `gpt-oss:20b` ili Qwen 3.5 9B; s 32 GB i više Gemma 4 26B ili 31B. Bez grafičkog procesora rad je spor, a računala s Apple Siliconom za to su praktična. Popis modela s veličinama vodi [Ollamina knjižnica](https://ollama.com/library).

Instalacija modela posao je jedne večeri. Znanje o tome kako UI odgovorno rabiti traži više vremena, pa slijede besplatni tečajevi.

## Tečajevi i UI pismenost

Akt o UI-ju nakon Omnibusa (čl. 4., od 27. 7. 2026.) traži od onih koji uvode UI sustave da poduzimaju mjere za potporu razvoju pismenosti u području umjetne inteligencije svojeg osoblja ([AI Literacy – Questions & Answers](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers)); što to znači za školu, opisuje poglavlje 13. Tablica A.11 navodi besplatne programe koji su u trenutku pisanja ove knjige (studeni 2026.) dostupni nastavniku u Hrvatskoj. Većina je na engleskom.

*Tablica A.11. Besplatni tečajevi i programi UI pismenosti, studeni 2026.*

| Resurs | Tko | Opseg i jezik |
|---|---|---|
| [Elements of AI](https://www.elementsofai.com/) | Sveučilište u Helsinkiju, MinnaLearn | vlastitim tempom; **hrvatska inačica** od 23. 11. 2020. (prijevod pod vodstvom CroAI-ja) |
| [Experience AI](https://experience-ai.org/en/) | Raspberry Pi Foundation i Google DeepMind | lekcije i trotjedni tečaj za nastavnike; **hr-HR** među 28 inačica (koje jedinice *(provj.)*) |
| [„Poboljšajte podučavanje i učenje uz Copilot Chat“](https://learn.microsoft.com/hr-hr/training/modules/enhance-teaching-learning-microsoft-copilot/) | Microsoft Learn | 9 jedinica; **hrvatski** (strojni prijevod) |
| [BrAIn webinari, „Nastavnici za nastavnike“](https://www.carnet.hr/javni-poziv-za-sudjelovanje-u-programu-edukacija-nastavnici-za-nastavnike-u-sklopu-projekta-brain/) | CARNET | hrvatski; raspored za 2026./2027. *(provj.)* |
| [AI Fluency for Educators](https://anthropic.skilljar.com/ai-fluency-for-educators) | Anthropic | 4 lekcije, oko 3 sata, certifikat; engl.; nije potreban račun |
| AI Fluency for pK-12 Educators | Anthropic i Teach For America | oko 4 sata, Coursera; engl. |
| [Generative AI for Educators with Gemini](https://grow.google/ai-for-educators/) | Grow with Google | oko 2 sata, certifikat; **samo engl.** |
| [ChatGPT Foundations for Teachers](https://www.coursera.org/learn/chatgpt-foundations-for-teachers) | OpenAI (Coursera) | 7 modula, oko 5 sati; engl. |
| [ChatGPT Foundations for K–12 Educators](https://www.commonsense.org/education/training/chatgpt-k12-foundations) | Common Sense i OpenAI | 1 sat, 8 lekcija; engl. |
| [AI-Powered Teaching with Microsoft Education](https://learn.microsoft.com/en-us/training/paths/ai-powered-teaching-microsoft-education/) | Microsoft Learn | 9 modula; engl. |
| [AI Guidance for Schools Toolkit](https://www.teachai.org/toolkit) | TeachAI | 7 načela za školska pravila; engl., CC BY-NC-SA 4.0 |
| [AI Literacy Lessons](https://www.commonsense.org/education/collections/ai-literacy-lessons-for-grades-6-12) | Common Sense Education | lekcije o UI-ju za 6.–12. razred (za mlađe medijska pismenost); engl. |
| [Day of AI](https://www.dayofai.org/) | MIT RAISE | PreK–12, bez UI alata; engl. |

Googleov program s ISTE-om, namijenjen šest milijuna nastavnika, samo je za SAD. Sve u ovom dodatku vrijedilo je 2. studenoga 2026. Ostaje zadnje i najkorisnije pitanje: kako sami provjeriti vrijedi li još.

## Kako provjeriti je li išta od ovoga još točno

Za provjeru jednog alata dovoljno je deset minuta i pet koraka. Isti postupak rabimo pri servisu sustava iz poglavlja 28.

1. **Službena stranica cijena.** Otvorite cjenik dobavljača, a ne članak o njemu. Ako je cijena u USD, dodajte 25 % PDV-a ili otvorite blagajnu do koraka prije plaćanja i pročitajte iznos u EUR.
2. **Stranica pomoći o privatnosti.** Potražite rečenicu o tome rabe li se razgovori za treniranje i kako se to isključuje. Usporedite putanju izbornika s tablicom A.3.
3. **Uvjeti korištenja i najniža dob.** U uvjetima potražite riječi „age“, „minimum“ ili „parent“. Uz to vrijedi hrvatska granica od 16 godina za privolu.
4. **Dokumentacija modela.** Za skripte otvorite popis modela i stranicu o zastarijevanju (engl. *deprecations*). Ako vašeg ID-ja više nema, promijenite redak `model` u `POSTAVKE`.
5. **Datum zadnje izmjene.** Na dnu stranice ili u zaglavlju dokumentacije potražite datum. Stranica bez datuma ili starija od šest mjeseci nije dokaz da se ništa nije promijenilo.

> **Što provjeriti prvo**
>
> Ovih jedanaest stavki mijenja preporuke u knjizi, pa ih provjeravamo prije svakog izdanja. Datum zadnje provjere upisujemo u [Povijest promjena](#povijest-promjena).
>
> 1. Je li Copilot Chat (i Study and Learn) uključen na skole.hr, za nastavnike i za učenike od 13 do 17 godina. Najbrže: prijava računom @skole.hr na m365copilot.com ili upit na helpdesk@skole.hr.
> 2. Jesu li Gemini for Education i Gemini Notebook uključeni na Google Workspaceu skole.hr (prijava na gemini.google.com i notebook.google).
> 3. Nova aplikacija Microsoft Copilot: izuzeća od treniranja za EGP, put do isključivanja, najniža dob i modeli u besplatnoj inačici.
> 4. Cijene u EUR na blagajni za ChatGPT Plus i Go, Claude Pro, Mistral Pro i Perplexity Pro.
> 5. Gašenje custom GPT-ova 11. 12. 2026. i plan potreban za dodatke; prijelaz s ChatGPT agenta na ChatGPT Work.
> 6. Gemovi i vještine: dostupnost u EU-u, potreba plaćenog plana, dob, uvjet Keep Activity; rok za Education (ne prije 1. 6. 2027.).
> 7. Koji model dobiva ChatGPT Free u Hrvatskoj i prikazuju li se oglasi.
> 8. Gemini 4 Argon u EU-u; gubi li Google AI Plus pristup Pro modelu.
> 9. Nacionalni zakon o provedbi Akta o UI-ju i tijelo za nadzor tržišta.
> 10. Hrvatski naslov Uredbe (EU) 2026/1744 i odredbe o subjektima koji uvode visokorizične sustave nakon Omnibusa.
> 11. Kvote Gemini Notebooka u Workspace for Education.

Tko provjeri ovih jedanaest stavki, zna je li dodatak u knjizi još pouzdan vodič ili se treba osloniti na ovu živu inačicu. Poglavlja knjige vrijede u oba slučaja.

---

## Povijest promjena

Najnoviji zapis stoji na vrhu. Uz svaki zapis navodimo datum i što se promijenilo; ako se promjena tiče recepta ili skripte, navodimo i poglavlje.

| Datum | Promjena |
|---|---|
| 4. 11. 2026. | Prva objava, jednaka dodatku A u izdanju knjige (stanje 2. 11. 2026.). |

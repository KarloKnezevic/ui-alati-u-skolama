// POSTAVKE: jedino mjesto koje mijenjate (Dodatak A)
const POSTAVKE = {
  dobavljac: 'gemini',             // ili 'openai'
  osnovniUrl: 'https://generativelanguage.googleapis.com/v1beta',
  model: 'gemini-3.1-flash-lite',  // stabilan ID, 11/2026.
  svojstvoKljuca: 'GEMINI_API_KEY',
  cijena: { ulaz: 0.25, izlaz: 1.50 } // USD / 1M tokena
};
// Za OpenAI-kompatibilnu krajnju točku (tablica „Isti posao, četiri
// formata“) mijenjaju se samo POSTAVKE, npr. za Googleovu:
//   dobavljac: 'openai',
//   osnovniUrl: 'https://generativelanguage.googleapis.com/v1beta/openai',
// Model, svojstvo s ključem i cijena ostaju isti. Ključ nikad nije ovdje,
// nego u Project Settings > Script Properties.

function pitajModel(upit, shema) {
  const kljuc = PropertiesService.getScriptProperties()
    .getProperty(POSTAVKE.svojstvoKljuca);
  if (!kljuc) throw new Error('Nema ključa u svojstvima.');
  if (POSTAVKE.dobavljac === 'openai')
    return pitajOpenAI_(upit, shema, kljuc);
  const url = POSTAVKE.osnovniUrl + '/models/' +
    POSTAVKE.model + ':generateContent';
  const tijelo = {
    contents: [{ parts: [{ text: upit }] }],
    generationConfig: {
      responseMimeType: 'application/json',
      responseJsonSchema: shema }
  };
  const odg = UrlFetchApp.fetch(url, {
    method: 'post', contentType: 'application/json',
    headers: { 'x-goog-api-key': kljuc }, // ne u adresi!
    payload: JSON.stringify(tijelo),
    muteHttpExceptions: true
  });
  if (odg.getResponseCode() !== 200) return neuspjeh_(odg);
  const p = JSON.parse(odg.getContentText());
  const t = p.usageMetadata || {};
  const c = (p.candidates || [])[0];      // blokiran odgovor nema dijelova
  const tekst = c && c.content && c.content.parts ? c.content.parts[0].text : '';
  const izlaz = (t.candidatesTokenCount || 0) +
    (t.thoughtsTokenCount || 0);
  return racun_(tekst, t.promptTokenCount || 0, izlaz);
}

// Isti posao preko OpenAI-kompatibilne krajnje točke (chat/completions).
// Vraća isti „račun“ kao pitajModel, pa ostatak skripte ne zna razliku.
function pitajOpenAI_(upit, shema, kljuc) {
  const tijelo = { model: POSTAVKE.model,
    messages: [{ role: 'user', content: upit }] };
  if (shema) tijelo.response_format = { type: 'json_schema',
    json_schema: { name: 'odgovor', schema: shema } };
  const odg = UrlFetchApp.fetch(POSTAVKE.osnovniUrl + '/chat/completions', {
    method: 'post', contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + kljuc },
    payload: JSON.stringify(tijelo), muteHttpExceptions: true });
  if (odg.getResponseCode() !== 200) return neuspjeh_(odg);
  const p = JSON.parse(odg.getContentText());
  const t = p.usage || {};
  const c = (p.choices || [])[0];
  const tekst = c && c.message && c.message.content ? c.message.content : '';
  return racun_(tekst, t.prompt_tokens || 0, t.completion_tokens || 0);
}

// Uspješan poziv: statusni kôd, tekst, tokeni i cijena u dolarima
// (tokeni x cijena iz POSTAVKE / milijun).
function racun_(tekst, ulaz, izlaz) {
  const usd = (ulaz * POSTAVKE.cijena.ulaz +
    izlaz * POSTAVKE.cijena.izlaz) / 1000000;
  return { kod: 200, tekst: tekst, greska: '',
    ulaz: ulaz, izlaz: izlaz, usd: usd };
}

// Neuspješan poziv: isti oblik, bez teksta i bez troška, s kratkim opisom
// pogreške koji je dobavljač vratio (401, 402, 404, 429, 5xx ...).
function neuspjeh_(odg) {
  const kod = odg.getResponseCode();
  let opis = odg.getContentText();
  try {
    let p = JSON.parse(opis);
    if (Array.isArray(p)) p = p[0] || {};     // neki dobavljači vraćaju popis
    if (p.error) opis = p.error.message || p.error.status || opis;
  } catch (e) { /* odgovor nije JSON: ostaje izvorni tekst */ }
  return { kod: kod, tekst: '', greska: String(opis).slice(0, 300),
    ulaz: 0, izlaz: 0, usd: 0 };
}

function probniPoziv() {
  const shema = { type: 'object', required: ['recenica'],
    properties: { recenica: { type: 'string' } } };
  const odg = pitajModel(
    'Objasni razlomak 3/4 jednom rečenicom za 5. razred.', shema);
  Logger.log(odg.kod + ' ' + (odg.tekst || odg.greska));
  Logger.log('ulaz ' + odg.ulaz + ', izlaz ' + odg.izlaz);
}

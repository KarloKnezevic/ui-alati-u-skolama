// Još dva dobavljača iza iste funkcije pitajModel: Claude (Messages API)
// i OpenAI (Responses API). Polja prema tablici „Isti posao, četiri
// formata“ u poglavlju 23; nazive i cijene provjerite u Dodatku A.
//
// Kako ih uključiti:
// 1. Ovu datoteku dodajte u isti projekt kao pitajModel.gs.
// 2. U pitajModel, odmah ispod retka s pitajOpenAI_, dodajte:
//      if (POSTAVKE.dobavljac === 'claude')
//        return pitajClaude_(upit, shema, kljuc);
//      if (POSTAVKE.dobavljac === 'openai-responses')
//        return pitajOpenAIResponses_(upit, shema, kljuc);
// 3. U POSTAVKE upišite vrijednosti za izabranog dobavljača, npr.
//      Claude: dobavljac: 'claude',
//              osnovniUrl: 'https://api.anthropic.com/v1',
//              model: 'claude-haiku-5-5',
//              svojstvoKljuca: 'ANTHROPIC_API_KEY',
//              cijena: { ulaz: 0.10, izlaz: 0.50 }
//      OpenAI: dobavljac: 'openai-responses',
//              osnovniUrl: 'https://api.openai.com/v1',
//              model: 'gpt-6-luna',
//              svojstvoKljuca: 'OPENAI_API_KEY',
//              cijena: { ulaz: 0.10, izlaz: 0.50 }
//    Ključ ide u Script Properties pod tim nazivom, nikad u kôd.
// Obje funkcije vraćaju isti „račun“ (racun_, neuspjeh_ iz pitajModel.gs).
// OpenAI u strogom načinu (strict: true) traži da svaki objekt u shemi ima
// "additionalProperties": false i da su sva polja u "required". Shema
// listića to ima; malu shemu iz probniPoziv za probu dopunite.
// Claude (studeni 2026.) ne podržava minItems veći od 1 ni maxItems (inače
// vraća 400), pa ih pitajClaude_ prije slanja uklanja; broj zadataka tada
// provjerava provjeriListic_. Zaglavlje anthropic-version: 2023-06-01 i dalje
// vrijedi; u novijoj inačici 2026-10-21 zahtjev ne smije slati temperature.

function pitajClaude_(upit, shema, kljuc) {
  const tijelo = { model: POSTAVKE.model, max_tokens: 4000,
    messages: [{ role: 'user', content: upit }] };
  if (shema) tijelo.output_config = {
    format: { type: 'json_schema', schema: zaClaude_(shema) } };
  const odg = UrlFetchApp.fetch(POSTAVKE.osnovniUrl + '/messages', {
    method: 'post', contentType: 'application/json',
    headers: { 'x-api-key': kljuc, 'anthropic-version': '2023-06-01' },
    payload: JSON.stringify(tijelo), muteHttpExceptions: true });
  if (odg.getResponseCode() !== 200) return neuspjeh_(odg);
  const p = JSON.parse(odg.getContentText());
  const t = p.usage || {};
  const dio = (p.content || []).filter(function (d) {
    return d.type === 'text'; })[0];
  return racun_(dio ? dio.text : '', t.input_tokens || 0,
    t.output_tokens || 0);
}

// Kopija sheme bez ograničenja broja elemenata koja Claude ne prima.
function zaClaude_(shema) {
  return JSON.parse(JSON.stringify(shema), function (kljuc, vrijednost) {
    if (kljuc === 'maxItems') return undefined;
    if (kljuc === 'minItems' && vrijednost > 1) return undefined;
    return vrijednost;
  });
}

function pitajOpenAIResponses_(upit, shema, kljuc) {
  const tijelo = { model: POSTAVKE.model, input: upit };
  if (shema) tijelo.text = { format: { type: 'json_schema',
    name: 'odgovor', strict: true, schema: shema } };
  const odg = UrlFetchApp.fetch(POSTAVKE.osnovniUrl + '/responses', {
    method: 'post', contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + kljuc },
    payload: JSON.stringify(tijelo), muteHttpExceptions: true });
  if (odg.getResponseCode() !== 200) return neuspjeh_(odg);
  const p = JSON.parse(odg.getContentText());
  const t = p.usage || {};
  let tekst = '';                          // tekst je u dijelovima "output_text"
  (p.output || []).forEach(function (o) {
    (o.content || []).forEach(function (c) {
      if (c.type === 'output_text') tekst += c.text;
    });
  });
  return racun_(tekst, t.input_tokens || 0, t.output_tokens || 0);
}

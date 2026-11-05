#!/usr/bin/env bash
# Isti probni poziv kao probniPoziv u pitajModel.gs, četiri puta, naredbom
# curl iz terminala (macOS i Linux). Ključ se čita iz varijable okruženja;
# postavite je kao u Dodatku E (read -s ...; export ...), nikad u ovu datoteku.
# Pokretanje jednog primjera: bash curl_primjeri.sh gemini
# (ili openai-kompatibilno, claude, openai). ID-jeve modela provjerite u Dodatku A.
set -euo pipefail

UPIT="Objasni razlomak 3/4 jednom rečenicom za 5. razred."
SHEMA='{"type": "object", "required": ["recenica"], "additionalProperties": false,
        "properties": {"recenica": {"type": "string"}}}'

case "${1:-gemini}" in
  gemini)          # Gemini API, generateContent; ključ u zaglavlju, ne u adresi
    curl -sS "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent" \
      -H "x-goog-api-key: ${GEMINI_API_KEY:?Postavite GEMINI_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"contents\": [{\"parts\": [{\"text\": \"$UPIT\"}]}],
           \"generationConfig\": {\"responseMimeType\": \"application/json\",
                                  \"responseJsonSchema\": $SHEMA}}"
    ;;
  openai-kompatibilno)   # ista Googleova usluga u OpenAI-jevu formatu
    curl -sS "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions" \
      -H "Authorization: Bearer ${GEMINI_API_KEY:?Postavite GEMINI_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"model\": \"gemini-3.1-flash-lite\",
           \"messages\": [{\"role\": \"user\", \"content\": \"$UPIT\"}],
           \"response_format\": {\"type\": \"json_schema\",
             \"json_schema\": {\"name\": \"odgovor\", \"schema\": $SHEMA}}}"
    ;;
  claude)          # Claude, Messages API
    curl -sS "https://api.anthropic.com/v1/messages" \
      -H "x-api-key: ${ANTHROPIC_API_KEY:?Postavite ANTHROPIC_API_KEY}" \
      -H "anthropic-version: 2023-06-01" \
      -H "Content-Type: application/json" \
      -d "{\"model\": \"claude-haiku-5-5\", \"max_tokens\": 500,
           \"output_config\": {\"format\": {\"type\": \"json_schema\", \"schema\": $SHEMA}},
           \"messages\": [{\"role\": \"user\", \"content\": \"$UPIT\"}]}"
    ;;
  openai)          # OpenAI, Responses API
    curl -sS "https://api.openai.com/v1/responses" \
      -H "Authorization: Bearer ${OPENAI_API_KEY:?Postavite OPENAI_API_KEY}" \
      -H "Content-Type: application/json" \
      -d "{\"model\": \"gpt-6-luna\", \"input\": \"$UPIT\",
           \"text\": {\"format\": {\"type\": \"json_schema\", \"name\": \"odgovor\",
                                  \"strict\": true, \"schema\": $SHEMA}}}"
    ;;
  *)
    echo "Nepoznat dobavljač: $1 (gemini, openai-kompatibilno, claude, openai)" >&2
    exit 1
    ;;
esac
echo

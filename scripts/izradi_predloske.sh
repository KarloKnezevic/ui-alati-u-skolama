#!/bin/bash
# Izradi .docx (za uređivanje u Wordu) i .pdf (za ispis) iz predložaka u Markdownu.
#   bash scripts/izradi_predloske.sh
# Treba: pandoc 3 i LuaLaTeX (TeX Live s fontovima XCharter i Inter).
set -e
K="$(cd "$(dirname "$0")/.." && pwd)"
P="$K/scripts/predlosci"
for mapa in predlosci/dokumenti predlosci/kontrolni-popisi; do
  mkdir -p "$K/$mapa/word" "$K/$mapa/pdf"
  for md in "$K/$mapa"/*.md; do
    ime=$(basename "$md" .md)
    [ "$ime" = "README" ] && continue
    pandoc "$md" --lua-filter="$P/filter.lua" --reference-doc="$P/reference.docx" \
      -o "$K/$mapa/word/$ime.docx"
    pandoc "$md" --lua-filter="$P/filter.lua" --pdf-engine=lualatex \
      -V papersize=a4 -V geometry:margin=2cm -V lang=hr \
      -V mainfont=XCharter -V sansfont=Inter -V fontsize=11pt \
      -V colorlinks=true -V linkcolor=uiTamnoPlava -V urlcolor=uiTamnoPlava \
      -H "$P/zaglavlje.tex" -o "$K/$mapa/pdf/$ime.pdf"
    echo "  $mapa/$ime"
  done
done

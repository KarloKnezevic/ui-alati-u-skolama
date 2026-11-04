-- Prilagodbe za Word i PDF:
--  * relativne poveznice na .md postaju običan tekst;
--  * popis čije stavke počinju kućicom ☐ postaje popis s kućicama
--    (u PDF-u kvadratić umjesto točke, u Wordu odlomci s ☐ bez točke);
--  * preostale ☐ u PDF-u crtaju se kao kvadratić.
local KUCICA = '☐'

local function Link(el)
  if el.target:match('%.md') and not el.target:match('^https?:') then
    return el.content
  end
end

local function bez_kucice(blokovi)
  local prvi = blokovi[1]
  if prvi and (prvi.t == 'Plain' or prvi.t == 'Para') then
    local s = prvi.content
    if s[1] and s[1].t == 'Str' and s[1].text == KUCICA then
      s:remove(1)
      if s[1] and s[1].t == 'Space' then s:remove(1) end
      return true
    end
  end
  return false
end

local function BulletList(el)
  for _, stavka in ipairs(el.content) do
    local p = stavka[1]
    if not (p and p.content and p.content[1] and p.content[1].t == 'Str' and p.content[1].text == KUCICA) then
      return nil
    end
  end
  for _, stavka in ipairs(el.content) do bez_kucice(stavka) end
  if FORMAT:match('latex') then
    return {
      pandoc.RawBlock('latex', '{\\renewcommand{\\labelitemi}{\\large$\\square$}'),
      el,
      pandoc.RawBlock('latex', '}')
    }
  else
    local out = {}
    for _, stavka in ipairs(el.content) do
      local p = stavka[1]
      local sadrzaj = pandoc.List({pandoc.Str(KUCICA), pandoc.Space()})
      sadrzaj:extend(p.content)
      table.insert(out, pandoc.Para(sadrzaj))
      for i = 2, #stavka do table.insert(out, stavka[i]) end
    end
    return out
  end
end

local function Str(el)
  if FORMAT:match('latex') and el.text:find(KUCICA, 1, true) then
    local dijelovi = {}
    local i = 1
    while true do
      local a, b = el.text:find(KUCICA, i, true)
      if not a then break end
      if a > i then table.insert(dijelovi, pandoc.Str(el.text:sub(i, a - 1))) end
      table.insert(dijelovi, pandoc.RawInline('latex', '$\\square$'))
      i = b + 1
    end
    if i <= #el.text then table.insert(dijelovi, pandoc.Str(el.text:sub(i))) end
    return dijelovi
  end
end

-- Najprije popisi (dok je ☐ još običan tekst), zatim preostale kućice.
return {{Link = Link, BulletList = BulletList}, {Str = Str}}

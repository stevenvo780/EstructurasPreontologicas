-- Sanitiza glifos que no están disponibles en las fuentes del PDF.
-- Solo afecta la salida de Pandoc; no modifica el manuscrito fuente.

local replacements = {
  ["📑"] = "Indice",
  ["✅"] = "SI",
  ["⚠"] = "ADVERTENCIA",
  ["✓"] = "SI",
  ["✗"] = "NO",
  ["𝓔"] = "E",
  ["ℓ"] = "l",
  ["—"] = "-",
  ["–"] = "-",
  ["‑"] = "-",
  ["−"] = "-",
}

local function sanitize(text)
  for source, target in pairs(replacements) do
    text = text:gsub(source, target)
  end
  return text
end

function Str(el)
  el.text = sanitize(el.text)
  return el
end

function Code(el)
  -- Evita celdas desbordadas por identificadores monoespaciados sin cortes.
  local text = sanitize(el.text):gsub("_", "-")
  return pandoc.Str(text)
end

function CodeBlock(el)
  -- Convierte bloques verbatim en líneas monoespaciadas que sí pueden envolver.
  local inlines = {}
  local text = sanitize(el.text):gsub("_", "-") .. "\n"
  for line in text:gmatch("(.-)\n") do
    local first = true
    for token in line:gmatch("%S+") do
      if not first then
        table.insert(inlines, pandoc.Space())
      end
      table.insert(inlines, pandoc.Code(token))
      first = false
    end
    table.insert(inlines, pandoc.LineBreak())
  end
  return pandoc.Div({pandoc.Plain(inlines)}, pandoc.Attr("", {"code-wrap"}))
end

function Table(el)
  -- Fuerza columnas de ancho relativo para que longtable pueda envolver texto.
  local n = #el.colspecs
  if n == 0 then
    return el
  end

  local compact = 0
  for _, spec in ipairs(el.colspecs) do
    local alignment = tostring(spec[1])
    if alignment == "AlignRight" or alignment == "AlignCenter" then
      compact = compact + 1
    end
  end

  local compact_width = n >= 6 and 0.10 or 0.12
  local remaining = 1.0 - compact * compact_width
  local regular = n - compact
  local regular_width = regular > 0 and remaining / regular or 1.0 / n

  for _, spec in ipairs(el.colspecs) do
    local alignment = tostring(spec[1])
    if alignment == "AlignRight" or alignment == "AlignCenter" then
      spec[2] = compact_width
    else
      spec[2] = regular_width
    end
  end
  return el
end

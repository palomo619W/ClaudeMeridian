#!/usr/bin/env python3
"""Utilidades sin dependencias externas para escribir y leer archivos .docx y .xlsx.

La usan exportar_docx.py, exportar_xlsx.py y los scripts que leen fichas o historiales.
Solo requiere la biblioteca estándar de Python 3.
"""
import datetime
import re
import zipfile
from xml.sax.saxutils import escape

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
S_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
DOC_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

COLOR_ACENTO = "1F4E79"
COLOR_TABLA = "D9E2F3"


def _x(text):
    """Escapa texto para XML y quita caracteres de control no válidos."""
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(text))
    return escape(text, {'"': "&quot;"})


def _core_props(title):
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f"<dc:title>{_x(title)}</dc:title><dc:creator>Trafficker digital</dc:creator>"
        f'<dcterms:created xsi:type="dcterms:W3CDTF">{now}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{now}</dcterms:modified>'
        "</cp:coreProperties>"
    )


# ---------------------------------------------------------------------------
# DOCX
# ---------------------------------------------------------------------------

INLINE = re.compile(r"(\*\*[^*]+\*\*|__[^_]+__|\*[^*\s][^*]*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def _runs(text, bold=False, italic=False, size=None, color=None):
    """Convierte texto con formato Markdown en línea (**negrita**, *cursiva*, `código`, [enlace](url)) a runs."""
    out = []
    for part in INLINE.split(text):
        if not part:
            continue
        b, i, mono = bold, italic, False
        if (part.startswith("**") and part.endswith("**")) or (part.startswith("__") and part.endswith("__")):
            part, b = part[2:-2], True
        elif part.startswith("`") and part.endswith("`"):
            part, mono = part[1:-1], True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            part, i = part[1:-1], True
        elif part.startswith("[") and "](" in part:
            label, url = part[1:-1].split("](", 1)
            part = f"{label} ({url})" if url.startswith("http") else label
        props = ""
        if mono:
            props += '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>'
        if b:
            props += "<w:b/>"
        if i:
            props += "<w:i/>"
        if color:
            props += f'<w:color w:val="{color}"/>'
        if size:
            props += f'<w:sz w:val="{size}"/>'
        rpr = f"<w:rPr>{props}</w:rPr>" if props else ""
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{_x(part)}</w:t></w:r>')
    return "".join(out)


def _p(text, style=None, ppr_extra="", **run_kw):
    ppr = ""
    if style or ppr_extra:
        ppr = "<w:pPr>" + (f'<w:pStyle w:val="{style}"/>' if style else "") + ppr_extra + "</w:pPr>"
    return f"<w:p>{ppr}{_runs(text, **run_kw)}</w:p>"


def _split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def _is_sep(line):
    return bool(re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$", line))


def _table(rows):
    ncols = max(len(r) for r in rows)
    width = 9360 // max(ncols, 1)
    grid = "".join(f'<w:gridCol w:w="{width}"/>' for _ in range(ncols))
    xml = [
        "<w:tbl><w:tblPr><w:tblStyle w:val=\"TablaMarketing\"/><w:tblW w:w=\"5000\" w:type=\"pct\"/>"
        "<w:tblLook w:val=\"04A0\" w:firstRow=\"1\" w:lastRow=\"0\" w:firstColumn=\"0\" w:lastColumn=\"0\" "
        "w:noHBand=\"0\" w:noVBand=\"1\"/></w:tblPr>",
        f"<w:tblGrid>{grid}</w:tblGrid>",
    ]
    for ri, row in enumerate(rows):
        row = row + [""] * (ncols - len(row))
        trpr = "<w:trPr><w:tblHeader/></w:trPr>" if ri == 0 else ""
        cells = []
        for cell in row:
            shade = f'<w:shd w:val="clear" w:color="auto" w:fill="{COLOR_TABLA}"/>' if ri == 0 else ""
            paras = "".join(_p(t, style="TablaTexto", bold=(ri == 0)) for t in re.split(r"<br\s*/?>", cell)) \
                or _p("", style="TablaTexto")
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}</w:tcPr>{paras}</w:tc>')
        xml.append(f"<w:tr>{trpr}{''.join(cells)}</w:tr>")
    xml.append("</w:tbl>")
    # Párrafo vacío tras la tabla: Word lo exige antes de otra tabla y da aire visual.
    xml.append('<w:p><w:pPr><w:spacing w:after="60"/></w:pPr></w:p>')
    return "".join(xml)


def markdown_to_body(md):
    """Convierte Markdown (títulos, listas, tablas, citas, código, separadores) en XML del cuerpo de Word."""
    lines = md.replace("\r\n", "\n").split("\n")
    body, i = [], 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(f'<w:p><w:pPr><w:pStyle w:val="Codigo"/></w:pPr>'
                            f'<w:r><w:t xml:space="preserve">{_x(lines[i])}</w:t></w:r></w:p>')
                i += 1
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and _is_sep(lines[i + 1]):
            rows = [_split_row(s)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            body.append(_table(rows))
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            level = len(m.group(1))
            style = {1: "Title", 2: "Heading1", 3: "Heading2"}.get(level, "Heading3")
            body.append(_p(m.group(2).strip().strip("#").strip(), style=style))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            body.append('<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" '
                        f'w:color="{COLOR_ACENTO}"/></w:pBdr></w:pPr></w:p>')
            i += 1
            continue
        if s.startswith(">"):
            body.append(_p(re.sub(r"^>\s?", "", s), style="Cita"))
            i += 1
            continue
        m = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        if m:
            level = min(len(m.group(1).replace("\t", "  ")) // 2, 2)
            text = m.group(2)
            text = re.sub(r"^\[ \]\s*", "☐ ", text)
            text = re.sub(r"^\[[xX]\]\s*", "☑ ", text)
            body.append(_p(text, ppr_extra=f'<w:pStyle w:val="Vineta"/><w:numPr><w:ilvl w:val="{level}"/>'
                                           '<w:numId w:val="1"/></w:numPr>'))
            i += 1
            continue
        m = re.match(r"^(\s*)(\d+[.)])\s+(.*)$", line)
        if m:
            level = min(len(m.group(1).replace("\t", "  ")) // 2, 2)
            left = 360 + level * 360
            body.append(_p(f"{m.group(2)} {m.group(3)}",
                           ppr_extra=f'<w:spacing w:after="60"/><w:ind w:left="{left}" w:hanging="360"/>'))
            i += 1
            continue
        # Párrafo normal: une líneas consecutivas.
        buf = [s]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|```|[-*+]\s|\d+[.)]\s|-{3,})",
                                                                   lines[i].strip()):
            buf.append(lines[i].strip())
            i += 1
        body.append(_p(" ".join(buf)))
    return "".join(body)


DOCX_STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri"/>
<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="es-ES"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" w:color="{COLOR_ACENTO}"/></w:pBdr><w:spacing w:after="240"/></w:pPr>
<w:rPr><w:b/><w:color w:val="{COLOR_ACENTO}"/><w:sz w:val="40"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr>
<w:rPr><w:b/><w:color w:val="{COLOR_ACENTO}"/><w:sz w:val="30"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr>
<w:rPr><w:b/><w:color w:val="2E74B5"/><w:sz w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/>
<w:pPr><w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="2"/></w:pPr>
<w:rPr><w:b/><w:sz w:val="23"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Cita"><w:name w:val="Cita"/><w:basedOn w:val="Normal"/>
<w:pPr><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="{COLOR_ACENTO}"/></w:pBdr>
<w:shd w:val="clear" w:color="auto" w:fill="F2F6FB"/><w:ind w:left="360"/></w:pPr><w:rPr><w:i/><w:color w:val="404040"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Vineta"><w:name w:val="Viñeta"/><w:basedOn w:val="Normal"/><w:pPr><w:spacing w:after="60"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Codigo"><w:name w:val="Código"/><w:basedOn w:val="Normal"/>
<w:pPr><w:shd w:val="clear" w:color="auto" w:fill="F2F2F2"/><w:spacing w:after="0"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/><w:sz w:val="18"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="TablaTexto"><w:name w:val="Texto de tabla"/><w:basedOn w:val="Normal"/>
<w:pPr><w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/></w:pPr><w:rPr><w:sz w:val="19"/></w:rPr></w:style>
<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>
<w:tblPr><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
<w:style w:type="table" w:styleId="TablaMarketing"><w:name w:val="Tabla Marketing"/><w:basedOn w:val="TableNormal"/>
<w:tblPr><w:tblBorders><w:top w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:left w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/>
<w:bottom w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:right w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/>
<w:insideH w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="A6A6A6"/></w:tblBorders>
<w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/><w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""

DOCX_NUMBERING = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="{W_NS}">
<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="360"/></w:pPr></w:lvl>
<w:lvl w:ilvl="1"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="◦"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl>
<w:lvl w:ilvl="2"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="▪"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="1080" w:hanging="360"/></w:pPr></w:lvl>
</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>"""


def write_docx(path, markdown, title="Documento", footer_text=None):
    """Escribe un .docx a partir de texto Markdown."""
    body = markdown_to_body(markdown)
    footer_text = footer_text or title
    sect = ('<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter"/>'
            '<w:pgSz w:w="12240" w:h="15840"/>'
            '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/>'
            "</w:sectPr>")
    document = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}"><w:body>{body}{sect}</w:body></w:document>')
    footer = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="{W_NS}" xmlns:r="{R_NS}">'
              '<w:p><w:pPr><w:jc w:val="right"/></w:pPr>'
              f'<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:t xml:space="preserve">{_x(footer_text)} · Página </w:t></w:r>'
              '<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="begin"/></w:r>'
              '<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
              '<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="separate"/></w:r>'
              '<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:t>1</w:t></w:r>'
              '<w:r><w:rPr><w:color w:val="808080"/><w:sz w:val="16"/></w:rPr><w:fldChar w:fldCharType="end"/></w:r>'
              "</w:p></w:ftr>")
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
        '<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>'
        '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        "</Types>")
    rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{PKG_REL}">'
            f'<Relationship Id="rId1" Type="{DOC_REL}/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            "</Relationships>")
    doc_rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{PKG_REL}">'
                f'<Relationship Id="rIdStyles" Type="{DOC_REL}/styles" Target="styles.xml"/>'
                f'<Relationship Id="rIdNumbering" Type="{DOC_REL}/numbering" Target="numbering.xml"/>'
                f'<Relationship Id="rIdFooter" Type="{DOC_REL}/footer" Target="footer1.xml"/>'
                "</Relationships>")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("docProps/core.xml", _core_props(title))
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", DOCX_STYLES)
        z.writestr("word/numbering.xml", DOCX_NUMBERING)
        z.writestr("word/footer1.xml", footer)
        z.writestr("word/_rels/document.xml.rels", doc_rels)


def read_docx_text(path):
    """Devuelve el texto de un .docx, un párrafo por línea (las viñetas se devuelven como '- texto')."""
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    lines = []
    for para in re.findall(r"<w:p[ >].*?</w:p>|<w:p/>", xml, re.S):
        texts = re.findall(r"<w:t[^>]*>(.*?)</w:t>", para, re.S)
        text = "".join(texts)
        for a, b in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'"), ("&amp;", "&")):
            text = text.replace(a, b)
        if "<w:numPr>" in para and text:
            text = "- " + text
        lines.append(text)
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# XLSX
# ---------------------------------------------------------------------------

NUM_RE = re.compile(r"^-?\d+(\.\d+)?$")
NUM_COMA_RE = re.compile(r"^-?\d+,\d+$")  # decimal con coma: 10,94
PCT_RE = re.compile(r"^-?\d+([.,]\d+)?\s*%$")


def _col(n):
    s = ""
    n += 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def _cell(ref, value, header=False):
    if header:
        return f'<c r="{ref}" s="1" t="inlineStr"><is><t>{_x(str(value).strip())}</t></is></c>'
    if isinstance(value, bool):
        value = str(value)
    if isinstance(value, (int, float)):
        return f'<c r="{ref}" s="3"><v>{value}</v></c>'
    v = "" if value is None else str(value).strip()
    plain = v.replace("**", "").strip()
    if NUM_COMA_RE.match(plain):
        plain = plain.replace(",", ".")
    if NUM_RE.match(plain):
        return f'<c r="{ref}" s="3"><v>{plain}</v></c>'
    if PCT_RE.match(plain):
        return f'<c r="{ref}" s="4"><v>{float(plain.rstrip("% ").strip().replace(",", ".")) / 100}</v></c>'
    if not plain:
        return f'<c r="{ref}" s="2"/>'
    return f'<c r="{ref}" s="2" t="inlineStr"><is><t>{_x(plain)}</t></is></c>'


def _sheet_xml(rows):
    ncols = max((len(r) for r in rows), default=1)
    widths = []
    for c in range(ncols):
        longest = max((len(str(r[c])) if c < len(r) and r[c] is not None else 0) for r in rows) if rows else 10
        widths.append(min(max(10, longest * 1.1 + 2), 60))
    cols = "".join(f'<col min="{i + 1}" max="{i + 1}" width="{w:.1f}" customWidth="1"/>' for i, w in enumerate(widths))
    data = []
    for ri, row in enumerate(rows):
        cells = "".join(_cell(f"{_col(ci)}{ri + 1}", v, header=(ri == 0)) for ci, v in enumerate(row))
        data.append(f'<row r="{ri + 1}">{cells}</row>')
    last = f"{_col(ncols - 1)}{max(len(rows), 1)}"
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="{S_NS}" xmlns:r="{R_NS}">'
            f'<dimension ref="A1:{last}"/>'
            '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/><selection pane="bottomLeft" activeCell="A2" sqref="A2"/>'
            "</sheetView></sheetViews>"
            f'<sheetFormatPr defaultRowHeight="15"/><cols>{cols}</cols><sheetData>{"".join(data)}</sheetData>'
            "</worksheet>")


XLSX_STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="{S_NS}">
<numFmts count="1"><numFmt numFmtId="164" formatCode="0.0%"/></numFmts>
<fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><sz val="11"/><color rgb="FFFFFFFF"/><name val="Calibri"/></font></fonts>
<fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FF{COLOR_ACENTO}"/><bgColor indexed="64"/></patternFill></fill></fills>
<borders count="2"><border><left/><right/><top/><bottom/><diagonal/></border>
<border><left style="thin"><color rgb="FFBFBFBF"/></left><right style="thin"><color rgb="FFBFBFBF"/></right>
<top style="thin"><color rgb="FFBFBFBF"/></top><bottom style="thin"><color rgb="FFBFBFBF"/></bottom><diagonal/></border></borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="5">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="center" wrapText="1"/></xf>
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1"><alignment vertical="top"/></xf>
<xf numFmtId="164" fontId="0" fillId="0" borderId="1" xfId="0" applyNumberFormat="1" applyBorder="1" applyAlignment="1"><alignment vertical="top"/></xf>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""


def _sheet_name(name, used):
    name = re.sub(r"[\[\]:*?/\\]", " ", str(name)).strip() or "Hoja"
    name = name[:31]
    base, n = name, 2
    while name.lower() in used:
        suffix = f" ({n})"
        name = base[:31 - len(suffix)] + suffix
        n += 1
    used.add(name.lower())
    return name


def write_xlsx(path, sheets, title="Libro"):
    """Escribe un .xlsx. `sheets` es una lista de (nombre, filas); la primera fila es el encabezado."""
    if not sheets:
        sheets = [("Hoja1", [[""]])]
    used, names = set(), []
    for name, _ in sheets:
        names.append(_sheet_name(name, used))
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
        '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
        '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        + "".join(f'<Override PartName="/xl/worksheets/sheet{i + 1}.xml" '
                  'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                  for i in range(len(sheets)))
        + "</Types>")
    rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{PKG_REL}">'
            f'<Relationship Id="rId1" Type="{DOC_REL}/officeDocument" Target="xl/workbook.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
            "</Relationships>")
    workbook = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="{S_NS}" xmlns:r="{R_NS}">'
                '<bookViews><workbookView/></bookViews><sheets>'
                + "".join(f'<sheet name="{_x(n)}" sheetId="{i + 1}" r:id="rId{i + 1}"/>' for i, n in enumerate(names))
                + "</sheets></workbook>")
    wb_rels = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{PKG_REL}">'
               + "".join(f'<Relationship Id="rId{i + 1}" Type="{DOC_REL}/worksheet" Target="worksheets/sheet{i + 1}.xml"/>'
                         for i in range(len(sheets)))
               + f'<Relationship Id="rId{len(sheets) + 1}" Type="{DOC_REL}/styles" Target="styles.xml"/>'
               "</Relationships>")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("docProps/core.xml", _core_props(title))
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/styles.xml", XLSX_STYLES)
        for i, (_, rows) in enumerate(sheets):
            z.writestr(f"xl/worksheets/sheet{i + 1}.xml", _sheet_xml(rows or [[""]]))


def _unescape(t):
    for a, b in (("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'"), ("&amp;", "&")):
        t = t.replace(a, b)
    return t


def read_xlsx_rows(path, sheet=0):
    """Lee una hoja de un .xlsx (índice o nombre) y devuelve una lista de filas (listas de texto)."""
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        shared = []
        if "xl/sharedStrings.xml" in names:
            sx = z.read("xl/sharedStrings.xml").decode("utf-8")
            for si in re.findall(r"<si>(.*?)</si>", sx, re.S):
                shared.append(_unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S))))
        wb = z.read("xl/workbook.xml").decode("utf-8")
        sheets = re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb)
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        targets = dict((rid, tgt) for tgt, rid in re.findall(r'Target="([^"]+)"[^>]*Id="([^"]+)"', rels))
        targets.update(dict(re.findall(r'Id="([^"]+)"[^>]*Target="([^"]+)"', rels)))
        if isinstance(sheet, str):
            rid = next(r for n, r in sheets if n == sheet)
        else:
            rid = sheets[sheet][1]
        target = targets[rid].lstrip("/")
        target = target if target.startswith("xl/") else "xl/" + target
        xml = z.read(target).decode("utf-8")
    rows = []
    for row in re.findall(r"<row[^>]*>(.*?)</row>", xml, re.S):
        values = {}
        for attrs, inner in re.findall(r"<c ([^>]*?)(?:/>|>(.*?)</c>)", row, re.S):
            ref = re.search(r'r="([A-Z]+)\d+"', attrs)
            if not ref:
                continue
            col = 0
            for ch in ref.group(1):
                col = col * 26 + ord(ch) - 64
            t = re.search(r't="([^"]+)"', attrs)
            t = t.group(1) if t else "n"
            if t == "s":
                v = re.search(r"<v>(.*?)</v>", inner or "")
                val = shared[int(v.group(1))] if v else ""
            elif t == "inlineStr":
                val = _unescape("".join(re.findall(r"<t[^>]*>(.*?)</t>", inner or "", re.S)))
            else:
                v = re.search(r"<v>(.*?)</v>", inner or "")
                val = _unescape(v.group(1)) if v else ""
            values[col - 1] = val
        if values:
            rows.append([values.get(i, "") for i in range(max(values) + 1)])
    return rows


def markdown_tables(md):
    """Extrae las tablas de un texto Markdown como [(título_previo, filas)]."""
    lines = md.replace("\r\n", "\n").split("\n")
    out, heading, i = [], "Tabla", 0
    while i < len(lines):
        s = lines[i].strip()
        m = re.match(r"^#{1,6}\s+(.*)$", s)
        if m:
            heading = m.group(1).strip()
        if s.startswith("|") and i + 1 < len(lines) and _is_sep(lines[i + 1]):
            rows = [_split_row(s)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            clean = [[re.sub(r"\*\*|__|`", "", c) for c in r] for r in rows]
            out.append((re.sub(r"^\d+\.\s*", "", heading), clean))
            continue
        i += 1
    return out

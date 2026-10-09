#!/usr/bin/env python3
"""Build a self-contained, printable HTML study guide from the COA Markdown notes."""
import html
import re
import pathlib

import markdown

BASE = pathlib.Path(__file__).resolve().parent
SRC = BASE / "COA Notes - Unit 1 & Unit 2.md"
OUT = BASE / "COA Notes - Unit 1 & Unit 2.html"
MERMAID_JS = BASE / "mermaid.min.js"

CSS = """
:root { color-scheme: light; }
* { box-sizing: border-box; }
body {
  font-family: "Segoe UI", "Inter", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.62; color: #1c2431; background: #f4f6f9;
  margin: 0; padding: 0;
}
.page { max-width: 1140px; margin: 0 auto; padding: 34px 46px 90px;
  background: #fff; box-shadow: 0 2px 22px rgba(20,35,70,.10); }
header.doc { border-bottom: 3px solid #2f6fde; margin-bottom: 20px; padding-bottom: 12px; }
header.doc h1 { margin: 0 0 6px; font-size: 2.05rem; color: #14315e; letter-spacing: -.5px; }
header.doc p { margin: 3px 0; color: #55607a; font-size: .95rem; }

h1, h2, h3, h4 { color: #14315e; line-height: 1.28; margin-top: 1.7em; }
h1 { font-size: 1.85rem; border-bottom: 3px solid #2f6fde; padding-bottom: 7px; }
h2 { font-size: 1.5rem; border-bottom: 2px solid #d6e0f2; padding-bottom: 5px; }
h3 { font-size: 1.22rem; color: #1c4c96; }
h4 { font-size: 1.05rem; color: #2c3e5f; }

p, li { font-size: .985rem; }
strong { color: #10305c; }
hr { border: 0; border-top: 2px dashed #ccd6ea; margin: 40px 0; }

table { border-collapse: collapse; width: 100%; margin: 16px 0 22px; font-size: .92rem; }
th, td { border: 1px solid #c9d4e8; padding: 8px 11px; text-align: left; vertical-align: top; }
th { background: #e8eefb; color: #14315e; font-weight: 700; }
tr:nth-child(even) td { background: #f7f9fd; }

blockquote { margin: 16px 0; padding: 10px 18px; background: #eef4ff;
  border-left: 5px solid #2f6fde; color: #23406e; font-style: italic; }
blockquote p { margin: 5px 0; }

code { background: #eef1f7; padding: 1.5px 5px; border-radius: 4px;
  font-family: "JetBrains Mono", "Fira Code", Consolas, monospace; font-size: .88em; color: #b02a5b; }
pre { background: #131a26; color: #dbe4f5; padding: 16px 18px; border-radius: 8px;
  overflow-x: auto; font-size: .87rem; line-height: 1.5; }
pre code { background: none; color: inherit; padding: 0; }

/* --- Mermaid diagrams --- */
.mermaid { background: #fbfcff; border: 1.5px solid #cdd8ee; border-radius: 10px;
  padding: 20px 14px; margin: 24px 0; text-align: center; overflow-x: auto; }
.mermaid svg { max-width: 100%; height: auto; }

.badge { display: inline-block; background: #2f6fde; color: #fff; border-radius: 5px;
  padding: 2px 10px; font-size: .78rem; font-weight: 700; letter-spacing: .6px;
  text-transform: uppercase; margin-right: 8px; vertical-align: middle; }

@media print {
  body { background: #fff; font-size: 10.5pt; }
  .page { box-shadow: none; max-width: none; padding: 0; }
  h1, h2, h3 { page-break-after: avoid; }
  table, pre, .mermaid { page-break-inside: avoid; }
  .mermaid { border-color: #999; }
}
"""

JS = """
<script src="mermaid.min.js"></script>
<script>
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    securityLevel: 'loose',
    flowchart: { htmlLabels: true, curve: 'basis', nodeSpacing: 45, rankSpacing: 55 },
    themeVariables: {
      fontFamily: 'Segoe UI, Inter, Arial, sans-serif',
      fontSize: '14px',
      primaryColor: '#e8eefb',
      primaryTextColor: '#14315e',
      primaryBorderColor: '#2f6fde',
      lineColor: '#5b7bb5',
      secondaryColor: '#eafaf0',
      tertiaryColor: '#fff4e5'
    }
  });
</script>
"""

MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)


def build() -> None:
    text = SRC.read_text(encoding="utf-8")

    # Park mermaid blocks so the markdown renderer leaves them alone.
    blocks: list[str] = []

    def stash(m: re.Match) -> str:
        blocks.append(
            '<div class="mermaid">\n' + html.escape(m.group(1).strip()) + "\n</div>"
        )
        return f"\n\n@@MERMAID{len(blocks) - 1}@@\n\n"

    text = MERMAID_RE.sub(stash, text)

    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )

    for i, block in enumerate(blocks):
        marker = f"@@MERMAID{i}@@"
        # markdown wraps the marker in <p>; swap the whole paragraph for the diagram.
        for candidate in (f"<p>{marker}</p>", marker):
            if candidate in body:
                body = body.replace(candidate, block)
                break
        else:
            raise RuntimeError(f"placeholder {marker} not found in output")

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>COA Notes — Unit 1 &amp; Unit 2 (with Flowcharts)</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">
<header class="doc">
  <p><span class="badge">Unit 1 + Unit 2</span> Complete study notes with flowcharts</p>
  <p>Source: M. Morris Mano, <em>Computer System Architecture</em>, 3rd ed.
     &nbsp;·&nbsp; Companion topics (Von Neumann, generations, MIPS/MFLOPS, Amdahl's law)
     from standard architecture references.<br>
     <strong>View → Print</strong> (or Ctrl+P) for a PDF-ready copy.</p>
</header>
{body}
</div>
{JS}
</body>
</html>
"""
    OUT.write_text(doc, encoding="utf-8")
    print(f"wrote {OUT}  ({OUT.stat().st_size / 1024:.0f} KB, {len(blocks)} flowcharts)")


if __name__ == "__main__":
    build()

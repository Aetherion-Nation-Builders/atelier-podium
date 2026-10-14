#!/usr/bin/env python3
"""Write background.svg, the Atelier DMG window background (660 x 400 pt), with outlined text.

    pip install fonttools
    python3 packaging/macos/dmg/atelier-background.py FONTS_DIR
    python3 packaging/macos/dmg/generate.py      # then render it (see README.md)

FONTS_DIR holds Archivo-Variable.ttf and GeistMono-Variable.ttf (SIL OFL 1.1), e.g. atelier-gate's
assets/fonts/. Only their outlines end up in the SVG; no font file is added to this repository.
"""
import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

import os

HERE = os.path.dirname(os.path.abspath(__file__))
NAME, TAGLINE, ICON = "Atelier Podium", "Presentations and slide shows", "../../../assets/app-icon/deckcraft.svg"
BLACK, IVORY, OCHRE = "#141210", "#efe6d2", "#d9a441"


def load(fonts, name, **axes):
    f = TTFont(os.path.join(fonts, name))
    if axes:
        f = instantiateVariableFont(f, axes)
    return f


def text_path(font, text, x, y, size, tracking=0.0):
    """SVG path data for `text` with its baseline-left at (x, y), `size` px tall em."""
    upem = font["head"].unitsPerEm
    s = size / upem
    cmap = font.getBestCmap()
    gs = font.getGlyphSet()
    hmtx = font["hmtx"]
    pen = SVGPathPen(gs)
    cx = x
    for ch in text:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[g].draw(tp)
        cx += hmtx[g][0] * s + tracking * size
    return pen.getCommands(), cx - x


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    fonts = sys.argv[1]
    name, tagline, icon, out = NAME, TAGLINE, ICON, os.path.join(HERE, "background.svg")
    title = load(fonts, "Archivo-Variable.ttf", wght=620, wdth=100)
    mono = load(fonts, "GeistMono-Variable.ttf", wght=400)
    t_d, t_w = text_path(title, name, 268, 72, 32)
    if t_w > 356:  # keep the title inside the rule
        t_d, t_w = text_path(title, name, 268, 72, 32 * 356 / t_w)
    sub = f"{tagline.upper()} · AETHERION NATION"
    sub_d, sub_w = text_path(mono, sub, 268, 112, 8.5, 0.15)
    if sub_w > 356:  # long taglines: shrink to the rule's width
        sub_d, _ = text_path(mono, sub, 268, 112, 8.5 * 356 / sub_w, 0.15)
    foot_d, _ = text_path(mono, "DRAG ONTO APPLICATIONS TO INSTALL", 268, 358, 9.5, 0.15)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="660" height="400" viewBox="0 0 660 400">
<!-- Atelier DMG window background: the app icon on volcanic black, Ivory field, ochre accent.
     Text is outlined (Archivo, Geist Mono; SIL OFL 1.1), so rendering needs no fonts. -->
<defs><pattern id="hatch" width="2.6" height="2.6" patternUnits="userSpaceOnUse" patternTransform="rotate(-38)">
  <rect width="2.6" height="1.05" fill="{BLACK}"/></pattern></defs>
<rect width="660" height="400" fill="{IVORY}"/>
<rect width="232" height="400" fill="{BLACK}"/>
<image href="{icon}" x="16" y="100" width="200" height="200"/>
<line x1="232.5" y1="0" x2="232.5" y2="400" stroke="{OCHRE}" stroke-width="2"/>
<line x1="267" y1="88.5" x2="624" y2="88.5" stroke="{BLACK}" stroke-width="0.6"/>
<path d="M271.5,81.5 L276,88.5 L271.5,95.5 L267,88.5 Z" fill="{OCHRE}"/>
<path d="M408,204 L465,200 L463,189 L492,205 L463,221 L465,210 L408,206 Z" fill="url(#hatch)"/><path d="M408,204 L465,200 L463,189 L492,205 L463,221 L465,210 L408,206 Z" fill="none" stroke="{BLACK}" stroke-width="0.9" stroke-linejoin="round"/>
<line x1="267" y1="335.5" x2="624" y2="335.5" stroke="{BLACK}" stroke-width="0.6"/>
<path fill="{BLACK}" d="{t_d}"/>
<path fill="{BLACK}" fill-opacity="0.72" d="{sub_d}"/>
<path fill="{BLACK}" fill-opacity="0.72" d="{foot_d}"/>
</svg>
'''
    open(out, "w").write(svg)


if __name__ == "__main__":
    main()

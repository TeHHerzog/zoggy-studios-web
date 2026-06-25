"""Graven Veil Display v0.1 — Build OTF+WOFF2 via FontBuilder."""
import xml.etree.ElementTree as ET, re, os
from fontTools.fontBuilder import FontBuilder
from fontTools.ttLib.woff2 import compress

SRC = r"C:\Users\Zog\Downloads\graven_veil_font_concept_pack\graven_veil_concept_sheet.svg"
OUT = r"C:\Antigravity\Zoggy studios\apps\darkfantasy\public\fonts\graven_veil"
N = {"svg":"http://www.w3.org/2000/svg"}
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
SCARS = ("#A3C113","#A33232","#8A5AC2","#6FA6B8")
NS = "{http://www.w3.org/2000/svg}"

def extract():
    root = ET.parse(SRC).getroot(); gs = []
    for g in root.iter(f"{NS}g"):
        tr = g.get("transform",""); m = re.search(r'translate\(([^)]+)\)', tr)
        if not m: continue
        p = m.group(1).split(","); gx, gy = float(p[0].strip()), float(p[1].strip())
        if not (1880 < gy < 3100): continue
        ms = re.search(r'scale\(([^)]+)\)', tr); sc = float(ms.group(1)) if ms else 0.2
        if g.findall(f"{NS}polyline")+g.findall(f"{NS}line")+g.findall(f"{NS}polygon"):
            gs.append((g, gx, gy, sc))
    hits = {}
    for t in root.iter(f"{NS}text"):
        lb = (t.text or "").strip()
        if lb not in CHARS: continue
        tx, ty = float(t.get("x",0)), float(t.get("y",0))
        if not (2070 < ty < 2900): continue
        for g, gx, gy, sc in gs:
            if abs(gx - (tx + 26)) < 30: hits[lb] = (g, sc); break
    return hits

def make_svg(c, g, sc):
    e = []
    for el in g:
        tg = el.tag.split("}")[-1]; sw = float(el.get("stroke-width",72))*sc
        if el.get("stroke","") in SCARS: continue
        if tg == "line":
            x1,y1 = float(el.get("x1"))*sc, float(el.get("y1"))*sc
            x2,y2 = float(el.get("x2"))*sc, float(el.get("y2"))*sc
            e.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#DDD5C3" stroke-width="{sw:.1f}" stroke-linecap="square"/>')
        elif tg == "polyline":
            pts = " ".join(f"{float(p.split(',')[0])*sc:.1f},{float(p.split(',')[1])*sc:.1f}" for p in el.get("points","").split() if "," in p)
            e.append(f'<polyline points="{pts}" fill="none" stroke="#DDD5C3" stroke-width="{sw:.1f}" stroke-linecap="square" stroke-linejoin="miter"/>')
        elif tg == "polygon":
            pts = " ".join(f"{float(p.split(',')[0])*sc:.1f},{float(p.split(',')[1])*sc:.1f}" for p in el.get("points","").split() if "," in p)
            e.append(f'<polygon points="{pts}" fill="#DDD5C3"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><g>{"".join(e)}</g></svg>'

def build():
    gl = extract(); chars = sorted(gl.keys())
    print(f"Glyphs: {len(chars)} — {''.join(chars)}")
    if len(chars) < 20: print("Too few glyphs, aborting"); return

    gn = [".notdef"] + [f"uni{ord(c):04X}" for c in chars]
    fb = FontBuilder(1000, isTTF=True)
    fb.setupGlyphOrder(gn)
    cmap = {0: ".notdef"}
    for c in chars: cmap[ord(c)] = f"uni{ord(c):04X}"
    fb.setupCharacterMap(cmap)
    from fontTools.ttLib.tables._g_l_y_f import Glyph
    fb.setupGlyf({n: Glyph() for n in gn})
    fb.setupHorizontalMetrics({n: (800, 0) for n in gn})
    fb.setupHorizontalHeader(ascent=920, descent=-180)
    fb.setupNameTable({"familyName":"Graven Veil Display","styleName":"Regular"})
    fb.setupOS2(sTypoAscender=920, sTypoDescender=-180, usWeightClass=400, usFirstCharIndex=32, usLastCharIndex=90)
    fb.setupPost()

    nd = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect x="100" y="100" width="800" height="800" fill="none" stroke="#DDD5C3" stroke-width="20"/></svg>'
    from fontTools.ttLib.tables.DefaultTable import DefaultTable
    st = DefaultTable("SVG "); sp = []
    sp.append(f'<svgDoc startGlyphID="0" endGlyphID="0"><![CDATA[{nd}]]></svgDoc>')
    for i, c in enumerate(chars, 1):
        g, sc = gl[c]
        sp.append(f'<svgDoc startGlyphID="{i}" endGlyphID="{i}"><![CDATA[{make_svg(c, g, sc)}]]></svgDoc>')
    st.data = ('<version value="1"/>' + "".join(sp)).encode("utf-8")
    fb.font["SVG "] = st

    os.makedirs(os.path.join(OUT,"build"), exist_ok=True)
    otf = os.path.join(OUT,"build","GravenVeilDisplay-Regular.otf")
    fb.font.save(otf); print(f"OTF: {otf}")
    woff2 = otf.replace(".otf",".woff2")
    compress(otf, woff2); print(f"WOFF2: {woff2}")

if __name__ == "__main__":
    build()

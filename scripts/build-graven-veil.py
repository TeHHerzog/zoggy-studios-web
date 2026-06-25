"""Graven Veil Display v0.1 — Font Builder"""
import xml.etree.ElementTree as ET, re, os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import cmap_format_4
from fontTools.ttLib.woff2 import compress

SRC = r"C:\Users\Zog\Downloads\graven_veil_font_concept_pack\graven_veil_concept_sheet.svg"
OUT = r"C:\Antigravity\Zoggy studios\apps\darkfantasy\public\fonts\graven_veil"
N = {"svg":"http://www.w3.org/2000/svg"}
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
SCARS = ("#A3C113","#A33232","#8A5AC2","#6FA6B8")

def extract():
    root = ET.parse(SRC).getroot()
    gs = []
    for g in root.findall(".//svg:g", N):
        tr = g.get("transform","")
        m = re.search(r'translate\(([^)]+)\)', tr)
        if not m: continue
        p = m.group(1).split(",")
        gx, gy = float(p[0].strip()), float(p[1].strip())
        if not (1880 < gy < 3100): continue
        ms = re.search(r'scale\(([^)]+)\)', tr)
        if not ms: continue
        any_el = g.findall(".//svg:polyline",N)+g.findall(".//svg:line",N)+g.findall(".//svg:polygon",N)
        if any_el: gs.append((g, gx, gy, float(ms.group(1))))
    hits = {}
    for t in root.findall(".//svg:text", N):
        lb = (t.text or "").strip()
        if lb not in CHARS: continue
        tx, ty = float(t.get("x",0)), float(t.get("y",0))
        if not (2070 < ty < 2900): continue
        for g, gx, gy, sc in gs:
            if abs(gx - (tx + 26)) < 30:
                hits[lb] = (g, sc); break
    return hits

def glyph_svg_str(g, sc):
    el = []
    for c in g:
        tg = c.tag.split("}")[-1]
        sw = float(c.get("stroke-width",72)) * sc
        if c.get("stroke","") in SCARS: continue
        if tg == "line":
            x1,y1 = float(c.get("x1"))*sc,float(c.get("y1"))*sc
            x2,y2 = float(c.get("x2"))*sc,float(c.get("y2"))*sc
            el.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#DDD5C3" stroke-width="{sw:.1f}" stroke-linecap="square"/>')
        elif tg == "polyline":
            pts = " ".join(f"{float(p.split(',')[0])*sc:.1f},{float(p.split(',')[1])*sc:.1f}" for p in c.get("points","").split() if "," in p)
            el.append(f'<polyline points="{pts}" fill="none" stroke="#DDD5C3" stroke-width="{sw:.1f}" stroke-linecap="square" stroke-linejoin="miter"/>')
        elif tg == "polygon":
            pts = " ".join(f"{float(p.split(',')[0])*sc:.1f},{float(p.split(',')[1])*sc:.1f}" for p in c.get("points","").split() if "," in p)
            el.append(f'<polygon points="{pts}" fill="#DDD5C3"/>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><g>{"".join(el)}</g></svg>'

def build():
    gl = extract()
    chars = sorted(gl.keys())
    print(f"Glyphs: {len(chars)} — {''.join(chars)}")
    if len(chars) < 20:
        print("Fewer glyphs than expected, aborting."); return

    font = TTFont()
    font.setGlyphOrder([".notdef"]+[f"uni{ord(c):04X}" for c in chars])
    names = font.getGlyphOrder()
    
    # cmap
    from fontTools.ttLib.tables._c_m_a_p import cmap_format_4
    c = cmap_format_4(4); c.platEncID=3; c.platID=3; c.format=4
    c.cmap = {0:".notdef"}
    for ch in chars: c.cmap[ord(ch)] = f"uni{ord(ch):04X}"
    from fontTools.ttLib import newTable
    font["cmap"] = newTable("cmap")
    font["cmap"].tableVersion = 0
    font["cmap"].tables = [c]
    
    # head
    from fontTools.ttLib.tables._h_e_a_d import table__h_e_a_d
    h = table__h_e_a_d()
    h.tableVersion=1.0; h.fontRevision=1.0; h.unitsPerEm=1000
    h.created=1782358200; h.modified=1782358200
    h.magicNumber=0x5F0F3CF5; h.checkSumAdjustment=0
    h.flags=0x000B; h.macStyle=0; h.lowestRecPPEM=8
    h.fontDirectionHint=2; h.indexToLocFormat=0; h.glyphDataFormat=0
    h.xMin=0; h.yMin=-180; h.xMax=1000; h.yMax=920
    font["head"] = h
    
    # hhea
    from fontTools.ttLib.tables._h_h_e_a import table__h_h_e_a
    hh = table__h_h_e_a()
    hh.ascent=920; hh.descent=-180; hh.lineGap=80
    hh.advanceWidthMax=1000; hh.minLeftSideBearing=0; hh.minRightSideBearing=0
    hh.xMaxExtent=1000; hh.caretSlopeRise=1; hh.caretSlopeRun=0
    hh.numberOfHMetrics=len(names)
    font["hhea"] = hh
    
    # hmtx
    from fontTools.ttLib.tables._h_m_t_x import table__h_m_t_x
    hm = table__h_m_t_x()
    hm.metrics = {n:(800,0) for n in names}
    font["hmtx"] = hm
    
    # maxp
    from fontTools.ttLib.tables._m_a_x_p import table__m_a_x_p
    mx = table__m_a_x_p()
    mx.tableVersion=0x00010000; mx.numGlyphs=len(names)
    mx.maxPoints=0; mx.maxContours=0; mx.maxCompositePoints=0
    mx.maxCompositeContours=0; mx.maxZones=2; mx.maxTwilightPoints=0
    mx.maxStorage=0; mx.maxFunctionDefs=0; mx.maxInstructionDefs=0
    mx.maxStackElements=0; mx.maxSizeOfInstructions=0
    mx.maxComponentElements=0; mx.maxComponentDepth=0
    font["maxp"] = mx
    
    # name
    from fontTools.ttLib.tables._n_a_m_e import table__n_a_m_e
    nm = table__n_a_m_e()
    for nid,pid,eid,lid,s in [(1,3,1,0x409,"Graven Veil Display"),(2,3,1,0x409,"Regular"),(4,3,1,0x409,"Graven Veil Display"),(6,3,1,0x409,"GravenVeilDisplay-Regular")]:
        nm.setName(s, nid, pid, eid, lid)
    font["name"] = nm
    
    # OS/2
    from fontTools.ttLib.tables.O_S_2f_2 import table_O_S_2f_2
    o = table_O_S_2f_2()
    o.version=4; o.xAvgCharWidth=800; o.usWeightClass=400; o.usWidthClass=4
    o.fsType=4; o.ySubscriptXSize=650; o.ySubscriptYSize=600
    o.ySubscriptXOffset=0; o.ySubscriptYOffset=75
    o.ySuperscriptXSize=650; o.ySuperscriptYSize=600
    o.ySuperscriptXOffset=0; o.ySuperscriptYOffset=350
    o.yStrikeoutSize=50; o.yStrikeoutPosition=300
    o.fsSelection=64; o.usFirstCharIndex=32; o.usLastCharIndex=90
    o.sTypoAscender=920; o.sTypoDescender=-180; o.sTypoLineGap=80
    o.usWinAscent=1000; o.usWinDescent=200; o.sxHeight=650; o.sCapHeight=880
    o.usDefaultChar=0; o.usBreakChar=32; o.achVendID="NONE"
    o.ulUnicodeRange1=7
    font["OS/2"] = o
    
    # post
    from fontTools.ttLib.tables._p_o_s_t import table__p_o_s_t
    po = table__p_o_s_t()
    po.formatType=2.0; po.isFixedPitch=0; po.underlinePosition=-100; po.underlineThickness=50
    font["post"] = po
    
    # SVG table
    from fontTools.ttLib.tables.DefaultTable import DefaultTable
    svg_tbl = DefaultTable("SVG ")
    svg_parts = []
    nd = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect x="100" y="100" width="800" height="800" fill="none" stroke="#DDD5C3" stroke-width="20"/></svg>'
    svg_parts.append(f'<svgDoc startGlyphID="0" endGlyphID="0"><![CDATA[{nd}]]></svgDoc>')
    for i,ch in enumerate(chars,1):
        g,sc = gl[ch]
        sv = glyph_svg_str(g,sc)
        svg_parts.append(f'<svgDoc startGlyphID="{i}" endGlyphID="{i}"><![CDATA[{sv}]]></svgDoc>')
    svg_tbl.data = ('<version value="1"/>' + "".join(svg_parts)).encode("utf-8")
    font["SVG "] = svg_tbl
    
    os.makedirs(os.path.join(OUT,"build"), exist_ok=True)
    otf = os.path.join(OUT,"build","GravenVeilDisplay-Regular.otf")
    font.save(otf)
    print(f"OTF: {otf}")
    woff2 = otf.replace(".otf",".woff2")
    compress(otf, woff2)
    print(f"WOFF2: {woff2}")

if __name__ == "__main__":
    build()

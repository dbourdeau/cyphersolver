# grep Tomokiyo unsolved.htm and Lasry GL.htm (fetched 15 Nov 2026) for terms, tags stripped
import re, sys, html
SP = r"C:/Users/dbour/AppData/Local/Temp/claude/6aac94263cec761a/affdd813-6a99-4218-ad82-979b1febcbe9/scratchpad/"
for name in ("unsolved.htm", "GL.htm"):
    raw = open(SP + name, encoding="utf8", errors="replace").read()
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw)))
    for term in sys.argv[1:]:
        hits = [m.start() for m in re.finditer(re.escape(term), t, re.I)]
        print(f"{name} {term!r}: {len(hits)}")
        for h in hits[:3]:
            print("   ...", t[max(0, h-120):h+160])

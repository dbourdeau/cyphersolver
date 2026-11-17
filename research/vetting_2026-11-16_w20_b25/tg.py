"""grep Tomokiyo (unsolved.htm) and Lasry (GL.htm) local copies, fetched 15 Nov 2026"""
import re, sys, html
D = 'C:/Users/dbour/AppData/Local/Temp/claude/6aac94263cec761a/affdd813-6a99-4218-ad82-979b1febcbe9/scratchpad'
for f in ('unsolved.htm', 'GL.htm'):
    raw = open(D + '/' + f, 'rb').read()
    for enc in ('utf-8', 'shift_jis', 'cp1252'):
        try: t = raw.decode(enc); break
        except Exception: pass
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t)); t = re.sub(r'\s+', ' ', t)
    for term in sys.argv[1:]:
        hits = [m.start() for m in re.finditer(re.escape(term), t, re.I)]
        print(f, repr(term), len(hits))
        for h in hits[:4]: print('   ...', t[max(0, h-120):h+160])

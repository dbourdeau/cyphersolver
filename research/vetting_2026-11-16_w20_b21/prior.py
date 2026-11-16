"""Grep Tomokiyo's unsolved.htm and Lasry's GL.htm (copies fetched 15 Nov 2026) for terms. Usage: prior.py term ..."""
import re, sys, html
S = r'C:/Users/dbour/AppData/Local/Temp/claude/6aac94263cec761a/affdd813-6a99-4218-ad82-979b1febcbe9/scratchpad/'
for name in ('unsolved.htm', 'GL.htm'):
    raw = open(S + name, 'rb').read()
    for enc in ('utf8', 'shift_jis', 'cp1252'):
        try: t = raw.decode(enc); break
        except Exception: pass
    t = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', t)).split())
    for q in sys.argv[1:]:
        hits = [m.start() for m in re.finditer(re.escape(q), t, re.I)]
        print(f'{name} | {q} | {len(hits)}', ' || '.join(t[max(0,h-80):h+80] for h in hits[:3]))

"""Grep Tomokiyo's unsolved.htm and Lasry's GL.htm (fetched 15 Nov 2026) for terms, tags stripped."""
import re, html, sys
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
for name in ('unsolved.htm', 'GL.htm'):
    raw = open(SP + '/' + name, 'rb').read()
    for enc in ('utf-8', 'shift_jis', 'cp1252'):
        try: t = raw.decode(enc); break
        except UnicodeDecodeError: pass
    s = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t)))
    for term in sys.argv[1:]:
        hits = [m.start() for m in re.finditer(re.escape(term), s, re.I)]
        print(f'{name} {term!r}: {len(hits)} hit(s)')
        for h in hits[:4]:
            print('   ...', s[max(0, h-150):h+150])

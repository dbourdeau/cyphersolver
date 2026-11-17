"""Grep Tomokiyo (unsolved.htm) and Lasry (GL.htm), both fetched 15 Nov 2026, tag-stripped.
python -I -X utf8 tl.py term [term ...]"""
import sys, re
P = 'C:/Users/dbour/AppData/Local/Temp/claude/6aac94263cec761a/affdd813-6a99-4218-ad82-979b1febcbe9/scratchpad/'
for f in ('unsolved.htm.txt', 'GL.htm.txt'):
    t = open(P + f, encoding='utf8').read()
    for term in sys.argv[1:]:
        hits = [m.start() for m in re.finditer(re.escape(term), t, re.I)]
        print(f'{f} "{term}": {len(hits)} hit(s)')
        for h in hits[:6]:
            print('   ...', t[max(0, h - 150):h + 200].replace('\n', ' '))

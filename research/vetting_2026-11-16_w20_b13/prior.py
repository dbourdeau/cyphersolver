"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 2667: ['Henneberg', 'Meiningen', '2661', 'Anna Maria', 'Albrecht', 'Poppo'],
 1696: ['Landsberg', 'Schmidtman', 'Fürstenberg', 'W 004', 'Westfalen'],
 2653: ['Geroldseck', 'von der Leyen', '111 Nr. 304', 'Karlsruhe'],
 2437: ['Niebuhr', 'Stein', '1199', 'Cap.C.I'],
 2896: ['Hamdani', 'Ismaili', 'Isma', 'MS 1662', 'Tayyibi'],
 2897: ['Ismaili', 'MS 1291', 'Tayyibi', 'Zahid'],
 2898: ['MS 1313', 'Walid', 'Bohra'],
 2224: ['Kerecsényi', 'Kerecsenyi', 'Nádasdy', 'Nadasdy', 'E 185'],
 2082: ['Webb', 'Danforth', 'Matthew Bridge', 'SBd-116'],
 1293: ['Treat Paine', 'Lavinia', 'RTP2'],
 2081: ['Sbd-133', 'cipher diary', 'Massachusetts Historical'],
 1295: ['Kimball', 'Griswold', 'fa0549'],
 2089: ['Wilcox', 'Berrien', 'Michigan State'],
 1299: ['Kerlérec', 'Kerlerec', 'Louisiane', 'Louisiana', 'C13A'],
 1910: ['Wesselényi', 'Wesselenyi', 'E 199', 'Murány', 'Vegyes iratok'],
 2489: ['Rákóczi', 'Rakoczi', 'Nathanael', 'G 15'],
 1908: ['Teleki', 'P 1238', 'R672'],
 1904: ['Károlyi', 'Karolyi', 'Szluha', 'Ordody', 'Nagyszegi', 'P 396'],
}
ids = [int(a) for a in sys.argv[1:]] or list(TERMS)
for i in ids:
    print('=' * 20, i)
    for t in TERMS[i]:
        for name, src in (('TOMOKIYO', T), ('LASRY', G)):
            hits = [m.start() for m in re.finditer(re.escape(t), src, re.I)]
            if hits:
                print(f'  {name} {t!r}: {len(hits)} hit(s); first: ...{" ".join(src[max(0,hits[0]-120):hits[0]+160].split())}...')
            else:
                print(f'  {name} {t!r}: 0')
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py'] + TERMS[i], capture_output=True, text=True, encoding='utf8', cwd='../..')
    print('  KNOWN.PY:'); print('   ' + '\n   '.join((r.stdout + r.stderr).strip().splitlines()[:30]))

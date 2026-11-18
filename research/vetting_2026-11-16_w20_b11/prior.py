"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 2502: ['Westphal', 'Linden', 'Königreich Westphalen', 'Nr. 393'],
 2602: ['Wedel', 'Nl Wedel', 'Kabinettsordre'],
 2596: ['Woellner', 'Wöllner', 'Rosenkreuz', 'Rosicruc'],
 2608: ['Goertz', 'Görtz', 'Thulemeier', 'Blumenthal', 'Wilhelmine'],
 2501: ['Lusi', 'Spiridion', 'Lombard'],
 2503: ['Scharnhorst', 'Boyen'],
 2622: ['Strangford', 'Miltitz'],
 1620: ['OBA 2987', 'OBA Nr. 2987', 'Tiergart', 'Tirgart', 'Prokurator', 'procurator'],
 2595: ['22442', '22687', '23213', 'Kasimir', 'Schönberg', 'Schoenberg'],
 2505: ['27275', 'Klingenbeck'],
 1157: ['Wickham', '38M49'],
 1134: ['Sinzendorf', 'Harrach', 'Span. Varia', 'Spanien Varia'],
 2655: ['Günterode', 'Guenterode', 'Keudel', 'Nr. 712', 'Politisches Archiv', 'Philipp'],
 1725: ['Spanien Varia 28', '4172844', 'Pötting', 'Poetting', 'Einsichtsakten'],
 1708: ['Spanien Varia 52', '4291348', 'Wiener Frieden', 'Ripperd', 'Königsegg'],
 1713: ['Spanien Varia 58-1', '4327122', 'Rosenberg'],
 1726: ['Spanien Varia 58-2', '4328197', 'Lebzeltern', 'Neny'],
 1220: ['Rym', 'Ungnad', 'Türkei I', 'Turkei I', 'R392'],
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
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py'] + TERMS[i], capture_output=True, text=True, encoding='utf8')
    print('  KNOWN.PY:'); print('   ' + '\n   '.join((r.stdout + r.stderr).strip().splitlines()[:40]))

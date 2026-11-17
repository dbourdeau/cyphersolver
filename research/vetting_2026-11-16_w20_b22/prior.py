"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 2688: ['Martinuzzi', 'Fráter György', 'Frater Georg', 'Fasc. 431'],
 2682: ['Malvezzi', 'Türkei I', 'Karton 8', 'Kt. 8'],
 2681: ['Czernovich', 'Cernovic', 'Csernovics', 'Czernović'],
 2679: ['Stöckl', 'Stoeckl', 'Stockl', 'Zasius'],
 2680: ['Provisionali', 'Karton 28', 'Kt. 28'],
 2584: ['Karton 34', 'Kt. 34', 'Ungnad', '47910'],
 2684: ['Nádasdy', 'Nadasdy', 'Fasc. 309', 'Fasc. 310'],
 2685: ['Zrínyi', 'Zrinyi', 'Gembicki', 'Fasc. 296'],
 1632: ['B 113', 'Albrecht', 'Riga', 'Limpurg'],
 2878: ['Montauti', 'M0320', 'Stanford'],
 2154: ['M. E. Read', 'Cooke diaries', '2670A', 'Pilbara'],
 2220: ['Teleki', 'Kaszoni', 'Kászoni', 'C.Tel.81'],
 2221: ['Kende', 'Teleki', 'C.Ken'],
 2219: ['Rhédey', 'Rhedey', 'Teleki', 'C.Tel.30'],
 2095: ['Shafter', 'Southwest Collection', 'Texas Tech'],
 2786: ['Carteret', 'ADM 1/1665', 'Pomone'],
 2785: ['Hillyar', 'ADM 1/1948', 'Phoebe', 'Essex'],
 2787: ['Rainier', 'Osborn', 'ADM 1/2253', 'Arrogant'],
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

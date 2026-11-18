"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 1221: ['Ungnad', 'Sinzendorff', 'Sinzendorf', 'Breuner', 'Türkei I', 'Kt. 4'],
 1222: ['Pezzen', 'Breuner', 'Türkei I', 'R1590'],
 1223: ['Eizing', 'Eitzing', 'Pezzen', 'Türkei I'],
 1224: ['Pezzen', 'Petzen', 'Türkei I'],
 1225: ['Kreckwitz', 'Krekwitz', 'Starzer', 'Ungnad', 'Türkei I'],
 2456: ['Rüstem', 'Rustem', 'Rusztem', 'Fasc. 418', 'Ungarische Akten', 'Malvezzi', 'Petrovich'],
 1286: ['Georgia', 'Georgian', 'Jordania', 'Mdivani', 'hou01502'],
 2032: ['Drach', 'E 1 M', 'Darmstadt'],
 2507: ['Sparr', 'Georg II', 'D 4', 'Darmstadt'],
 1628: ['2594', '2613', 'Oldenburg', 'Johann Friedrich', 'John Frederick', 'Philipp von Hessen', 'Philip of Hesse', 'HStAM'],
 1196: ['Mizon', 'Dalziel', 'Porto-Novo', 'Ms 5892', 'Percher'],
 2523: ['gendarm', 'santarm', 'Helsinki', 'Finland'],
 2522: ['Topelius', 'Chifferskrift'],
 2147: ['Danite', 'Denver', 'Dougherty', 'Kansas'],
 2548: ['Friesland', 'inv. 713', '7-14', 'Willem V', 'Orangist'],
 2581: ['MHC', 'Koç', 'Koc University', 'Refet', 'Muzaffer', '1921'],
 1938: ['Casenowe', 'Dufauk', 'MS 647', 'Lambeth'],
 1990: ['MS 941', 'Cardinal Albert', 'Lambeth', 'Archduke Albert'],
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

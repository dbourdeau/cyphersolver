"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
WT = SP + r'\wt'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 1776: ['SP 36/65', 'John Smart', 'Smart'],
 2789: ['SP 54/41', 'Gleneves', 'Glenevis', 'Andrew Clerck', 'Cameron'],
 907: ['Lamplugh', 'Pile', 'SP 18', 'Whitley'],
 879: ['SP 84/161', 'Refin', 'Middelburg'],
 1802: ['SP 84/161', 'Refin'],
 2790: ['SP 32/14', 'Ruvigny', 'Sparr'],
 2795: ['SP 35/30', 'R W', 'Atterbury'],
 2798: ['SP 46/124', 'Bronyng', 'wadmoll', 'Hobson'],
 2927: ['Pointis', 'Londonderry', 'SP 63/352', '32499'],
 2921: ['Danett', 'SP 83/16', 'Salcedo'],
 1146: ['SP 81/44', 'SP 81/46', 'SP 84/130', 'SP 77/28', 'SP 81/37', 'SP 81/38', 'SP 77/6', 'Gerbier', 'Kendall', 'Stanning'],
 1158: ['WO 1/923', 'WO 1/924', 'Bouillon', 'Roznel'],
 2546: ['Reyd', 'Wier', 'Wyer', 'inv. nr. 808'],
 2551: ['Padentiana', 'Harlingen', '273-03'],
 2918: ['Rebbe', 'Peter Gail', 'Trumbull', 'Downshire'],
 1163: ['Kinkel', 'Minna Werner'],
 1292: ['Gordon', 'Battle Papers', '02769'],
 1426: ['Frick', 'Carnegie', 'Homestead'],
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
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py'] + TERMS[i], capture_output=True, text=True, encoding='utf8', cwd=WT)
    print('  KNOWN.PY:'); print('   ' + '\n   '.join((r.stdout + r.stderr).strip().splitlines()[:40]))

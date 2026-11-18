"""Run known.py per lead on its terms, drop self-hits (leads.json, the source sweeps, the audit); grep Tomokiyo/Lasry lists.
python -I -X utf8 prior.py"""
import subprocess, re, html, sys, os
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
def strip(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
TOMO, GL = strip(SP + r'\unsolved.htm'), strip(SP + r'\GL.htm')
TERMS = {
 '2730': (['fr. 3329', 'fr. 3409', 'fr. 4717', 'Humieres', 'Humières', 'Roncherolles', 'Maineville'], ['3329', '3409', '4717', 'Humi', 'Roncherolles', 'Maineville', 'Mayneville']),
 '2749': (['NAF 22330', 'Breiffenstein', 'Riedet'], ['22330', 'Breiff', 'Riedet', 'Delft']),
 '2727': (['fr. 3375', 'fr. 4697', 'fr. 4691', 'Scipione Gonzaga', 'Camillo Volta', 'Guazzo'], ['3375', '4697', '4691', 'Volta', 'Scipione', 'Guazzo']),
 '2728': (['fr. 3422'], ['3422']),
 '2725': (['fr. 3641', 'Ibarra', 'Mendoza'], ['3641', 'Ibarra', 'Mendoza', 'Feria']),
 '2729': (['fr. 3624', 'fr. 3625', 'fr. 3614', 'fr. 3634', 'fr. 3646', 'Montholon', 'Lauriere', 'Marchant'], ['3624', '3625', '3614', '3634', '3646', 'Montholon', 'Lauri', 'Marchant', 'Regnyer']),
 '2736': (['fr. 3586', 'fr. 3575', 'Ventadour'], ['3586', '3575', 'Ventadour']),
 '2743': (['fr. 3457', 'Ossat'], ['3457', 'Ossat']),
 '2748': (['NAF 3145', 'NAF 3146', 'Chanvallon', 'Breval', 'Voillot'], ['3145', '3146', 'Chanvallon', 'Champvallon', 'Breval', 'Voillot']),
 '2737': (['fr. 3659', 'Monteleon', 'Monteleón'], ['3659', 'Montele']),
 '2740': (['fr. 3796'], ['3796']),
 '2738': (['fr. 3693', 'Blainville', 'Mende'], ['3693', 'Blainville', 'Mende']),
 '2739': (['fr. 3837', 'fr. 3758', 'fr. 3854', 'Bouthillier', 'Guron', 'Chatillon', 'Châtillon', 'Conti'], ['3837', '3758', '3854', 'Bouthillier', 'Guron', 'Chatillon', 'Châtillon', 'Conti']),
 '2741': (['fr. 4137', 'Sabran'], ['4137', 'Sabran']),
 '2915': (['fr. 23202', 'Fouquet'], ['23202', 'Fouquet']),
 '2745': (['fr. 23202', 'R7894', 'R7895', 'R7896', 'R7897'], ['23202', 'Fouquet']),
 '2747': (['fr. 23227', 'fr. 23228', 'Roslet', 'Noailles'], ['23227', '23228', 'Roslet', 'Noailles']),
 '2751': (['NAF 4543', 'Audibert', 'Le Dran'], ['4543', 'Audibert', 'musical', 'musique']),
}
SKIP = ('leads.json', 'sweep_2026-11-14_omont_bnf', 'sweep_2026-11-15_omont_naf', 'audit_2026-11-16_omont', 'vetting_2026-11-16_w20')
def ctx(T, w):
    out = []
    for m in re.finditer(re.escape(w), T):
        out.append(re.sub(r'\s+', ' ', T[max(0, m.start()-150):m.end()+150]))
        if len(out) >= 4: break
    return out
ids = sys.argv[1:] or list(TERMS)
for i in ids:
    kt, gt = TERMS[i]
    print('#' * 20, i)
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', 'research/archive_sweep_2026-10/known.py'] + kt, capture_output=True, text=True, encoding='utf8')
    for line in r.stdout.splitlines():
        if line.startswith('==') or not any(s in line for s in SKIP):
            print(line[:400])
    for name, T in (('TOMOKIYO', TOMO), ('LASRY GL', GL)):
        for w in gt:
            for c in ctx(T, w):
                print(f'  [{name} {w}] {c}')

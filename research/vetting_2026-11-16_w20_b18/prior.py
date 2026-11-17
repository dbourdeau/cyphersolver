"""Run known.py and grep Tomokiyo unsolved.htm / Lasry GL.htm (fetched 15 Nov 2026) for each lead's terms."""
import re, subprocess, sys, html
SP = r'C:\Users\dbour\AppData\Local\Temp\claude\6aac94263cec761a\affdd813-6a99-4218-ad82-979b1febcbe9\scratchpad'
WT = SP + r'\wt'
def txt(p):
    t = open(p, encoding='utf8', errors='replace').read()
    return html.unescape(re.sub(r'<[^>]+>', ' ', t))
T = txt(SP + r'\unsolved.htm'); G = txt(SP + r'\GL.htm')
TERMS = {
 2833: ['Autogr. 15/1', 'Ferdinand', 'Graz', 'Rudolf II', 'Rudolph'],
 2837: ['Cod. 9521', 'Fedeli', 'Piccolomini', 'cifra manifesta'],
 2836: ['Ser. n. 4832', 'Stammbuch', 'Epstein', 'Ankersberg', 'Haschka'],
 2109: ['Hilandar', 'Chilandar', 'Athos', 'litorea'],
 2650: ['Ali Ekrem', 'Open Jerusalem', 'Jerusalem', 'Ottoman'],
 2087: ['Hiram', 'Brown diar', 'Astoria', 'Oregon', 'Schiwek'],
 2893: ['Laud Or', 'Galen', 'Bodleian', 'Savage-Smith'],
 2517: ['Millet', 'Lionne', 'Brandebourg', 'Jeurs'],
 1915: ['Saint-Priest', 'Saint Priest', 'Tott', 'Turquie', 'Choiseul'],
 2799: ['Braye', 'Duke of York', 'YPIC', 'Parliamentary Archives'],
 2889: ['E16470', 'Penn Museum', 'papyrus', 'Moritz'],
 2718: ['Friesland', 'Frise', 'Tresoar', '646/2', 'Formulaires'],
 1964: ['Berczeny', 'Bercsényi', 'Bercsenyi', 'O-77382', 'Braci Czeskich'],
 1965: ['Rákóczi', 'Rakoczi', 'O-77570', 'Poznań', 'Poznan'],
 1966: ['Dupleix', '380667', 'Dodwell', 'Bussy', 'Dauteuil'],
 2938: ['Prediger', 'Yonge', 'Cape of Good', 'Dundas', 'CO 48'],
 2397: ['Maria Carolina', 'Carolina', 'ca_9568899', 'Naples'],
 2519: ['Neville-Rolfe', 'Rolfe', 'Dufferin', 'D1071'],
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

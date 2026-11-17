"""Fetch a BnF Archives et manuscrits notice and print each component line mentioning chiffr/clef/gallica.
python -I -X utf8 am.py cc497913 [cc...]"""
import sys, os, re, html, time, urllib.request
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'am')
for cid in sys.argv[1:]:
    p = os.path.join(D, cid + '.html')
    if not os.path.exists(p):
        r = urllib.request.urlopen(urllib.request.Request(f'https://archivesetmanuscrits.bnf.fr/ark:/12148/{cid}', headers={'User-Agent': 'Mozilla/5.0'}), timeout=90)
        open(p, 'wb').write(r.read()); time.sleep(1)
    t = open(p, encoding='utf8', errors='replace').read()
    g = sorted(set(re.findall(r'gallica\.bnf\.fr/ark:/12148/(btv1b\w+)', t)))
    t2 = html.unescape(re.sub(r'<[^>]+>', '\n', t))
    lines = [re.sub(r'\s+', ' ', x).strip() for x in t2.split('\n')]
    lines = [x for x in lines if x]
    print('=====', cid, 'gallica:', g)
    for i, x in enumerate(lines[:60]):
        if i < 40 and ('Français' in x or 'Anc.' in x or 'Nouvelles' in x): print('  H', x[:200])
    for i, x in enumerate(lines):
        if re.search(r'chiffr|[Cc]lef|déchiff', x):
            print('  ', ' | '.join(lines[max(0,i-1):i+1])[:500])

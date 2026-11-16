"""Probe BnF Archives et manuscrits notices (cc ids) to find a 'Français N' volume and its Gallica ark.
NOID check char computed locally; one request a second.  python -I -X utf8 am_probe.py <ccnum> [...]"""
import sys, re, html, time, urllib.request, os
X = '0123456789bcdfghjkmnpqrstvwxz'
def chk(s): return X[sum(i * X.index(c) for i, c in enumerate(s, 1) if c in X) % 29]
OUT = sys.argv[1] if os.path.isdir(sys.argv[1]) else None
def get(cc):
    u = f'https://archivesetmanuscrits.bnf.fr/ark:/12148/{cc}{chk(cc)}'
    r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)
    t = r.read().decode('utf8', 'replace')
    m = re.search(r'Sommaire Informations bibliographiques\s*(.*?)(?:Rechercher|$)', re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)))))
    g = sorted(set(re.findall(r'gallica\.bnf\.fr/ark:/12148/(btv1b\w+?)(?:[.&"/]|$)', t)))
    return u, t, (m.group(1)[:160] if m else '?'), g
args = sys.argv[2:] if OUT else sys.argv[1:]
for a in args:
    cc = 'cc' + a
    try:
        u, t, title, g = get(cc)
        print(cc, '|', title, '|', g, flush=True)
        if OUT: open(os.path.join(OUT, cc + '.html'), 'w', encoding='utf8').write(t)
    except Exception as e:
        print(cc, 'ERR', e, flush=True)
    time.sleep(1)

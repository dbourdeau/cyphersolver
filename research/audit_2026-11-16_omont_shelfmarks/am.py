"""BnF Archives et manuscrits helper for the Omont shelfmark audit (16 Nov 2026).

fetch(n)    -> notice for cc<n> (cached under CACHE, one request a second, check char computed locally)
parse(html) -> dict(shelf, old, crumb, items=[(no, text, folio)], gallica=[arks])
find_fr(N)  -> notice of 'Français N' (Ancien fonds and others), walking cc ids from a guess
CLI: python -I -X utf8 am.py fr 3654      |  python -I -X utf8 am.py cc 50106
"""
import os, re, sys, html, time, json, urllib.request

X = '0123456789bcdfghjkmnpqrstvwxz'
CACHE = os.environ.get('AMCACHE') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'amcache')
os.makedirs(CACHE, exist_ok=True)
_last = [0.0]


def chk(s):
    return X[sum(i * X.index(c) for i, c in enumerate(s, 1) if c in X) % 29]


def url(n):
    cc = f'cc{n}'
    return f'https://archivesetmanuscrits.bnf.fr/ark:/12148/{cc}{chk(cc)}'


def fetch(n):
    p = os.path.join(CACHE, f'cc{n}.html')
    if os.path.exists(p) and os.path.getsize(p) > 2000:
        return open(p, encoding='utf8').read()
    wait = 1.1 - (time.time() - _last[0])
    if wait > 0:
        time.sleep(wait)
    try:
        r = urllib.request.urlopen(urllib.request.Request(url(n), headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)
        t = r.read().decode('utf8', 'replace')
    except Exception as e:
        t = f'ERROR {e}'
    _last[0] = time.time()
    open(p, 'w', encoding='utf8').write(t)
    return t


def text(t):
    t = re.sub(r'<script.*?</script>|<style.*?</style>', '', t, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', t)))


def parse(t):
    s = text(t)
    d = {'shelf': None, 'old': None, 'crumb': None, 'items': [], 'gallica': [], 'head': ''}
    m = re.search(r'Accueil Présentation de l\'IR (.*?) Rechercher dans l\'IR', s)
    if m:
        d['crumb'] = m.group(1)
    m = re.search(r'Sommaire Informations bibliographiques (.*?)(?: Index index Contenu|$)', s)
    body = m.group(1) if m else ''
    m = re.match(r'(.*?) • (.*?) • (.*?)(?= 1 |$)', body)
    d['head'] = body[:300]
    m = re.search(r'Cote : ([^R]*?) Réserver', s)
    if m:
        d['shelf'] = m.group(1).strip()
    m = re.search(r'Ancienne cote : (.*?) (?=[A-Z][a-zé])', s)
    if m:
        d['old'] = m.group(1).strip()
    # items: "• 12 Lettre ... Fol. 26" ; split on ' • ' then number prefix
    for part in body.split(' • '):
        mm = re.match(r'(\d+[a-z]?(?: bis)?) (.*)$', part)
        if mm:
            fol = re.search(r'Fol\. ?([\dIVXLC][^ ]*(?: ?[-–] ?\d+)?(?: v[°o])?)\s*$', mm.group(2))
            d['items'].append([mm.group(1), mm.group(2), fol.group(1) if fol else ''])
    # On the notice page the "Fol. N" printed after item k-1 is item k's folio (checked against Omont's
    # printed "(Fol. N.)" for fr. 3654 and fr. 3657). Shift the folios one item down.
    prev = ''
    for it in d['items']:
        it[2], prev = prev, it[2]
        it[1] = re.sub(r'\s*Fol\. ?\S+(?: ?[-–] ?\d+)?(?: v[°o])?\s*$', '', it[1])
    d['gallica'] = sorted(set(re.findall(r'gallica\.bnf\.fr/ark:/12148/(btv1b\w+?)(?:[.&"/\s]|$)', t)))
    return d


def shelfnum(d):
    m = re.search(r'Français (\d+)', d.get('shelf') or '')
    return int(m.group(1)) if m else None


def find_fr(N, guess=None, tries=12):
    """Walk cc ids until the notice's shelfmark is Français N. Returns (cc, parsed) or (None, None)."""
    idx = os.path.join(CACHE, '_frmap.json')
    mp = json.load(open(idx)) if os.path.exists(idx) else {}
    if str(N) in mp:
        return mp[str(N)], parse(fetch(mp[str(N)]))
    n = guess or (N + 46450)
    seen = set()
    for _ in range(tries):
        if n in seen:
            break
        seen.add(n)
        d = parse(fetch(n))
        k = shelfnum(d)
        if k is not None:
            mp[str(k)] = n
            json.dump(mp, open(idx, 'w'))
        if k == N:
            return n, d
        if k is None:
            n += 1
            continue
        n += (N - k)
    return None, None


def shelfrange(d, fonds='Français'):
    """(a, b) of the notice's shelfmark: 'Français 3654' -> (3654, 3654); 'Français 20500-20576' -> (20500, 20576)."""
    m = re.search(fonds + r' (\d+)(?:-(\d+))?\b', d.get('head') or '')
    if not m:
        return None
    a = int(m.group(1))
    return a, int(m.group(2) or a)


def interp(N, lo, hi, fonds='Français', tries=14):
    """Interpolation search for the notice holding `fonds N` between cc lo and cc hi (a monotonic block)."""
    rl = shelfrange(parse(fetch(lo)), fonds)
    rh = shelfrange(parse(fetch(hi)), fonds)
    for _ in range(tries):
        if not rl or not rh or hi - lo < 1:
            break
        if rl[0] <= N <= rl[1]:
            return lo, parse(fetch(lo))
        if rh[0] <= N <= rh[1]:
            return hi, parse(fetch(hi))
        g = lo + max(1, min(hi - lo - 1, round((N - rl[1]) * (hi - lo) / max(1, rh[0] - rl[1]))))
        d = parse(fetch(g))
        r = shelfrange(d, fonds)
        if not r:
            g2 = g + 1
            d = parse(fetch(g2)); r = shelfrange(d, fonds); g = g2
            if not r:
                break
        if r[0] <= N <= r[1]:
            return g, d
        if N < r[0]:
            hi, rh = g, r
        else:
            lo, rl = g, r
    return None, None


def loupe(n, term):
    """Full-text search inside the notice of cc<n> (the site's 'loupe'); returns [(compid, text)].
    Finds components beyond the 30 shown on the notice page."""
    import urllib.parse
    safe = re.sub(r'[^\w]+', '_', term)
    p = os.path.join(CACHE, f'loupe_{n}_{safe}.html')
    if os.path.exists(p):
        t = open(p, encoding='utf8').read()
    else:
        wait = 1.1 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        u = (f'https://archivesetmanuscrits.bnf.fr/affichageDetailsComposants.html?eadCid=FRBNFEAD{n:09d}'
             f'&typeIndex=TEXTE_LIBRE_LOCAL&val={urllib.parse.quote(term)}')
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'replace')
        except Exception as e:
            t = f'ERROR {e}'
        _last[0] = time.time()
        open(p, 'w', encoding='utf8').write(t)
    out = []
    for m in re.finditer(r'href="(FRBNFEAD\d+_[\w]+)">(.*?)</a>', t, re.S):
        out.append((m.group(1), re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', m.group(2)))).strip()))
    return out


def comp(compid):
    """One component's full display (folio etc.)."""
    p = os.path.join(CACHE, f'comp_{compid}.html')
    if os.path.exists(p):
        t = open(p, encoding='utf8').read()
    else:
        wait = 1.1 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        u = f'https://archivesetmanuscrits.bnf.fr/ajaxGetCompDisplay.html?eadCompId={compid}'
        try:
            t = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read().decode('utf8', 'replace')
        except Exception as e:
            t = f'ERROR {e}'
        _last[0] = time.time()
        open(p, 'w', encoding='utf8').write(t)
    return text(t)


def ciph(n):
    """All cipher components of cc<n>: union of loupe hits for chiffre / chiffres / chiffrée(s) / chiffré(s)."""
    seen = {}
    for term in ('chiffre', 'chiffres', 'chiffrée', 'chiffrées'):
        for cid, tx in loupe(n, term):
            seen[cid] = tx
    return seen


def show(n, d, filt=None):
    print(f'cc{n} {url(n)} | {d["shelf"]} | old {d["old"]} | {d["crumb"]} | gallica {d["gallica"]}')
    print('  head:', d['head'][:200])
    for no, tx, fol in d['items']:
        if filt is None or re.search(filt, tx, re.I):
            print(f'  {no}: {tx[:260]}')


if __name__ == '__main__':
    a = sys.argv[1:]
    filt = os.environ.get('FILT')
    if a[0] == 'fr':
        for N in a[1:]:
            n, d = find_fr(int(N))
            if n:
                show(n, d, filt)
            else:
                print('fr', N, 'NOT FOUND')
    else:
        for c in a[1:]:
            d = parse(fetch(int(c)))
            show(int(c), d, filt)

# Mesure unique n° 2 (PREREG-2 § 4, route A). Usage : python3 -I measure2.py <dossier>
import sys, random, os
D = sys.argv[1]
key = {}
for ln in open(os.path.join(D, 'KEY-2.tsv'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    c, v = ln.rstrip('\n').split('\t')[:2]
    key[c] = v.lower()
def norm(s):
    s = s.lower().replace('å', 'aa').replace('j', 'i').replace('w', 'v')
    return ''.join(ch for ch in s if 'a' <= ch <= 'z' or ch in 'æø')
toks = []  # (label, doubled)
for ln in open(os.path.join(D, 'H2-CHIFFRE.txt'), encoding='utf-8'):
    if not ln.startswith('L'): continue
    for t in ln.split()[1:]:
        if t in '|:;,.' or t == '[rayé]': continue
        if t == '[?]': toks.append(('?', False)); continue
        dbl = t.endswith('^'); toks.append((t.rstrip('^'), dbl))
R = norm(open(os.path.join(D, 'R-CLAIR.txt'), encoding='utf-8').read().split('\n---\n', 1)[1])
def decode(k):
    out = []
    for c, dbl in toks:
        v = k.get(c)
        if v is None: out.append('?'); continue
        v = norm(v) or '?'
        if dbl: v = v + v[-1]
        out.extend(v)
    return out
def sw(a, b):
    n, m = len(a), len(b)
    H = [[0]*(m+1) for _ in range(n+1)]; best = (0, 0, 0)
    for i in range(1, n+1):
        ai = a[i-1]; Hi = H[i]; Hp = H[i-1]
        for j in range(1, m+1):
            d = Hp[j-1] + (1 if ai == b[j-1] and ai != '?' else -1)
            v = max(d, Hp[j]-1, Hi[j-1]-1, 0); Hi[j] = v
            if v > best[0]: best = (v, i, j)
    i, j = best[1], best[2]; eq = 0; A = []; B = []
    while i > 0 and j > 0 and H[i][j] > 0:
        s = 1 if a[i-1] == b[j-1] and a[i-1] != '?' else -1
        if H[i][j] == H[i-1][j-1] + s:
            eq += (s == 1); A.append(a[i-1]); B.append(b[j-1]); i -= 1; j -= 1
        elif H[i][j] == H[i-1][j] - 1:
            A.append(a[i-1]); B.append('-'); i -= 1
        else:
            A.append('-'); B.append(b[j-1]); j -= 1
    return best[0], eq, ''.join(reversed(A)), ''.join(reversed(B))
dec = decode(key); N = len(dec); Nl = sum(1 for x in dec if x != '?')
sc, eq, A, B = sw(dec, R)
car = eq / N
present = sorted({c for c, _ in toks if c in key}); vals = [key[c] for c in present]
rnd = random.Random(1814); ctl = []
for _ in range(200):
    p = vals[:]; rnd.shuffle(p); k2 = dict(key); k2.update(zip(present, p))
    d2 = decode(k2); s2, e2, _, _ = sw(d2, R); ctl.append(e2 / len(d2))
mx = max(ctl); mean = sum(ctl)/len(ctl); marge = car - mx
verdict = 'VALIDÉ' if car >= 0.85 and marge >= 0.30 else ('PARTIEL' if marge >= 0.30 else 'ÉCHEC')
print(f'H2 positions={N} lettres décodées={Nl} (positions « ? »={N-Nl}) R={len(R)} lettres')
print(f'car (décisif, /positions)={car:.3f}  car/lettres décodées={eq/Nl:.3f}  score SW={sc}  égalités={eq}')
print(f'témoins n=200 graine 1814 moy={mean:.3f} max={mx:.3f}  marge={marge:.3f}  -> {verdict}')
print('décodage H2 :', ''.join(dec))
print('alignement H2:', A)
print('alignement R :', B)

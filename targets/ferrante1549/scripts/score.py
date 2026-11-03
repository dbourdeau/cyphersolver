import sys, random, re
# usage: score.py key transcription linefilter clearfile [start end]
# Decodes the chosen lines and compares them with the clear text; 200 shuffled tables as control.


def loadk(f):
    d = {}
    for l in open(f, encoding='utf8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        d[p[0]] = p[1]
    return d


def norm(s):
    s = s.lower().replace('v', 'u').replace('y', 'i').replace('h', '')
    return re.sub('[^a-z]', '', s)


def lcs(a, b):
    n, m = len(a), len(b)
    prev = [0] * (m + 1)
    for i in range(n):
        cur = [0] * (m + 1)
        for j in range(m):
            cur[j + 1] = max(prev[j] + 1 if a[i] == b[j] else 0, prev[j + 1], cur[j])
        prev = cur
    return prev[m]


def runs(a, b, L=4):
    cov = [0] * len(a)
    S = set(b[i:i + L] for i in range(len(b) - L + 1))
    for i in range(len(a) - L + 1):
        if a[i:i + L] in S:
            for j in range(i, i + L):
                cov[j] = 1
    return sum(cov) / max(1, len(a))


k = loadk(sys.argv[1])
pat = re.compile(sys.argv[3])
toks = []
for l in open(sys.argv[2], encoding='utf8'):
    if l.startswith('#') or not l.strip():
        continue
    t = l.split()
    if pat.match(t[0]):
        toks += [s for s in t[1:] if not s.endswith('_') and s != '/']
clear = norm(' '.join(l for l in open(sys.argv[4], encoding='utf8') if not l.startswith('#')))
if len(sys.argv) > 5:
    clear = clear[int(sys.argv[5]):int(sys.argv[6])]


def dec(kk):
    return ''.join(norm(kk[s]) if s in kk else '#' for s in toks)


p = dec(k)
print('signs', len(toks), 'with a value', sum(1 for s in toks if s in k), 'decoded letters', len(p.replace('#', '')), 'clear letters', len(clear))
print('unknown:', sorted(set(s for s in toks if s not in k)))
print(p)
print('letters in order shared with clear text (LCS/decoded): %.3f' % (lcs(p.replace('#', ''), clear) / len(p.replace('#', ''))))
print('share of decoded letters in runs of 4+ found in clear text: %.3f' % runs(p, clear))
vals = list(k.values())
keys = list(k)
R = random.Random(1)
res = []
rr = []
for i in range(200):
    v = vals[:]
    R.shuffle(v)
    q = dict(zip(keys, v))
    x = dec(q)
    res.append(lcs(x.replace('#', ''), clear) / max(1, len(x.replace('#', ''))))
    rr.append(runs(x, clear))
print('200 shuffled tables: LCS mean %.3f max %.3f; runs mean %.3f max %.3f' % (sum(res) / 200, max(res), sum(rr) / 200, max(rr)))

"""Alignement EM dur code -> sous-chaîne du clair, sur plusieurs exemplaires d'un même texte.
usage: align.py <spec.json> <out_prefix>
spec = {"letters":[{"name":"L1","plain":"<fichier clair>","copies":["transcr/A_286_p1.txt+transcr/A_287_p1.txt", ...]}],
        "seed": {"225":"wij", ...}, "iters":15}
Fichiers de transcription : lignes de nombres ; {mots en clair} ; [biffé] ignoré ; '#' commentaires ; '?' suffixe = incertain."""
import sys, json, re, math, collections, unicodedata
def norm(s):
    s = s.lower().replace('v','w').replace('é','e').replace('ü','y')
    return ''.join(ch for ch in s if ch.isalpha())
def read_copy(spec):
    toks = []
    for f in spec.split('+'):
        for line in open(f, encoding='utf-8'):
            line = line.split('#')[0]
            line = re.sub(r'\[[^\]]*\]', ' ', line)
            for m in re.finditer(r'\{([^}]*)\}|(\d+)\??', line):
                if m.group(1) is not None:
                    w = norm(m.group(1))
                    if w: toks.append(('P', w))
                else: toks.append(('C', m.group(2)))
    return toks
def read_plain(f):
    t = []
    for line in open(f, encoding='utf-8'):
        if line.startswith('#'): continue
        t.append(re.sub(r'\(\?\)', '', line))
    return norm(' '.join(t))
MAXK = 7; SKIP = 9.0
def lp_prior(s):
    k = len(s)
    if k == 0: return math.log(0.01)
    PK = {1:0.45,2:0.28,3:0.15,4:0.07,5:0.03,6:0.015,7:0.01}
    return math.log(PK.get(k,0.005)) - k*math.log(20)
def align(toks, P, cnt, tot, alpha=0.5, band=None):
    n, m = len(toks), len(P); INF = 1e18
    # dp[i][j]
    dp = [dict() for _ in range(n+1)]; dp[0] = {0: (0.0, None)}
    # allow skipping plain chars at the very start/end freely-ish
    for j in range(1, m+1): dp[0][j] = (SKIP*j*0.3, ('skip', 0, j-1))
    for i in range(n):
        typ, v = toks[i]; cur = dp[i]; nxt = dp[i+1]
        # also allow plain skips within row i (deletions): process j increasing
        for j in sorted(cur):
            c0 = cur[j][0]
            if j < m:
                c1 = c0 + SKIP
                if j+1 not in cur or cur[j+1][0] > c1: cur[j+1] = (c1, ('skip', i, j))
        for j, (c0, _) in cur.items():
            if typ == 'P':
                L = len(v)
                for k in range(max(0, L-2), L+3):
                    if j+k > m: break
                    s = P[j:j+k]; d = edit(v, s)
                    c = c0 + 4.0*d
                    if j+k not in nxt or nxt[j+k][0] > c: nxt[j+k] = (c, ('tok', i, j))
            else:
                d = cnt.get(v, {}); t = tot.get(v, 0)
                for k in range(0, MAXK+1):
                    if j+k > m: break
                    s = P[j:j+k]
                    p = (d.get(s, 0) + alpha*math.exp(lp_prior(s))) / (t + alpha)
                    c = c0 - math.log(p)
                    if j+k not in nxt or nxt[j+k][0] > c: nxt[j+k] = (c, ('tok', i, j))
        # prune
        if len(nxt) > 400:
            best = sorted(nxt.items(), key=lambda kv: kv[1][0])[:400]; dp[i+1] = dict(best)
    # end: allow skipping rest of plain
    endrow = dp[n]; bestj, bestc = None, INF
    for j, (c, _) in endrow.items():
        cc = c + SKIP*0.3*(m-j)
        if cc < bestc: bestc, bestj = cc, j
    # backtrack
    out = []; i, j = n, bestj
    while i > 0 or j > 0:
        c, bp = dp[i][j]
        if bp is None: break
        kind, pi, pj = bp
        if kind == 'skip':
            j = pj; continue
        out.append((toks[pi], P[pj:j])); i, j = pi, pj
    return bestc, out[::-1]
def edit(a, b):
    prev = list(range(len(b)+1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j]+1, cur[j-1]+1, prev[j-1]+(ca != cb)))
        prev = cur
    return prev[-1]
def main():
    spec = json.load(open(sys.argv[1])); outp = sys.argv[2]
    cnt = collections.defaultdict(dict); tot = collections.Counter()
    for c, s in spec.get('seed', {}).items(): cnt[c][norm(s)] = 5; tot[c] += 5
    jobs = []
    for L in spec['letters']:
        P = read_plain(L['plain'])
        for cp in L['copies']: jobs.append((L['name'], cp, read_copy(cp), P))
    for it in range(spec.get('iters', 12)):
        newc = collections.defaultdict(collections.Counter); total = 0; res = []
        for name, cp, toks, P in jobs:
            c, out = align(toks, P, cnt, tot); total += c; res.append((name, cp, out))
            for (typ, v), s in out:
                if typ == 'C': newc[v][s] += 1
        cnt = collections.defaultdict(dict); tot = collections.Counter()
        for c, s in spec.get('seed', {}).items(): cnt[c][norm(s)] = 5; tot[c] += 5
        for v, d in newc.items():
            for s, k in d.items(): cnt[v][s] = cnt[v].get(s, 0) + k; tot[v] += k
        print('iter', it, round(total, 1), flush=True)
    with open(outp + '_align.txt', 'w') as f:
        for name, cp, out in res:
            f.write('== %s %s\n' % (name, cp))
            f.write(' '.join('%s=%s' % (v if t == 'C' else '{'+v+'}', s or '∅') for (t, v), s in out) + '\n')
    table = {v: dict(collections.Counter(d).most_common()) for v, d in sorted(cnt.items(), key=lambda kv: int(kv[0]))}
    json.dump(table, open(outp + '_table.json', 'w'), ensure_ascii=False, indent=0)
main()

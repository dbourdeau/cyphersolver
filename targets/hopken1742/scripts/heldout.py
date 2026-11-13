"""Held-out test of a frozen key on a glossed passage.
python heldout.py <key.tsv> <transcription.txt> <gloss.tsv> [shuffles]
For each run (rows given in gloss.tsv) the groups are aligned to the gloss letters by dynamic programming: each group
takes one contiguous piece (0-7 letters) of the normalised gloss; cost 0 if the piece equals the group's key value,
1 otherwise; a group not in the key costs 0.5 for any piece. A group 'matches' when its value equals its piece.
Normalisation: lower case, accents dropped, letters only (digits kept), j->i, v->u, w->u, y kept; å/ä->a, ö->o.
Word codes are compared through a fixed list of equivalents (below), stated in NOTES.md.
Control: the key's values shuffled among its groups (default 500 times)."""
import sys, re, random, unicodedata
sys.path.insert(0, __file__.rsplit('scripts', 1)[0] + 'scripts')
from decrypt import load_key, tokens
EQ = {'tractat': 'traite', 'ottporten': 'porte', 'storviziren': 'grandvizir', 'grefwen': 'comte', 'sultan': 'sultan',
      'ryssland': 'russie', 'swerige': 'suede', 'frankrike': 'france', 'konglmajt': 'roi', 'ambassadeur': 'ambassadeur'}
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^a-z0-9]', '', s)
    return s.replace('j', 'i').replace('v', 'u').replace('w', 'u')
def nv(v): return norm(EQ.get(v, v))
def rows_of(spec, allrows):
    # spec like H01-H08 or H09-H10a or H10b ; a = groups before the first clear token, b = after it
    lo, _, hi = spec.partition('-'); hi = hi or lo
    labs = [r for r, _ in allrows]
    def p(x): return (x[:3], x[3:] if len(x) > 3 else '')
    (l0, s0), (l1, s1) = p(lo), p(hi); i0, i1 = labs.index(l0), labs.index(l1); out = []
    for i in range(i0, i1 + 1):
        toks = allrows[i][1]; ci = [k for k, t in enumerate(toks) if t[0] == 'clear']
        g = list(range(len(toks)))
        if i == i0 and s0 == 'b': g = [k for k in g if k > ci[0]]
        if i == i1 and s1 == 'a': g = [k for k in g if k < ci[0]]
        if i == i0 and s0 == 'a' and i0 == i1: g = [k for k in g if k < ci[0]]
        out += [toks[k][1] for k in g if toks[k][0] == 'g']
    return out
def align(groups, key, gloss):
    n, m = len(groups), len(gloss); INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    for i in range(n):
        v = key.get(groups[i]); vv = nv(v) if v is not None else None
        for j in range(m + 1):
            if D[i][j] >= INF: continue
            for L in range(0, 8):
                if j + L > m: break
                c = 0.5 if vv is None else (0 if gloss[j:j + L] == vv else 1)
                if D[i][j] + c < D[i + 1][j + L]: D[i + 1][j + L] = D[i][j] + c; B[i + 1][j + L] = (j, L)
    j = m; match = 0; known = 0; i = n
    if D[n][m] >= INF: return 0, sum(1 for g in groups if g in key)
    while i > 0:
        pj, L = B[i][j]; v = key.get(groups[i - 1])
        if v is not None:
            known += 1
            if gloss[pj:pj + L] == nv(v): match += 1
        j = pj; i -= 1
    return match, known
def score(key, runs):
    M = K = N = 0
    for groups, gl in runs:
        m, k = align(groups, key, gl); M += m; K += k; N += len(groups)
    return M, K, N
if __name__ == '__main__':
    key = load_key(sys.argv[1]); allrows = []
    for l in open(sys.argv[2], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        lab, rest = l.split(' ', 1); allrows.append((lab, tokens(rest.strip())))
    runs = []
    for l in open(sys.argv[3], encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        r, spec, text = l.rstrip('\n').split('\t'); runs.append((rows_of(spec, allrows), norm(text)))
    M, K, N = score(key, runs)
    print('groups %d, in key %d, matching the gloss %d (%.0f%% of all, %.0f%% of those in key)' % (N, K, M, 100 * M / N, 100 * M / max(K, 1)))
    S = int(sys.argv[4]) if len(sys.argv) > 4 else 500; random.seed(1); vals = list(key.values()); gs = list(key.keys()); res = []
    for _ in range(S):
        random.shuffle(vals); res.append(score(dict(zip(gs, vals)), runs)[0])
    print('shuffled control over %d shuffles: mean %.1f, max %d' % (S, sum(res) / S, max(res)))

"""Print the alignment of groups to gloss pieces (from heldout.py's DP): python pairs.py key transcription gloss.tsv > pairs.tsv"""
import sys
sys.path.insert(0, __file__.rsplit('scripts', 1)[0] + 'scripts')
from heldout import load_key, tokens, rows_of, norm, nv
def align_pairs(groups, key, gloss):
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
    out = []; j = m
    for i in range(n, 0, -1):
        pj, L = B[i][j]; out.append((groups[i - 1], key.get(groups[i - 1], ''), gloss[pj:pj + L])); j = pj
    return out[::-1]
key = load_key(sys.argv[1]); allrows = []
for l in open(sys.argv[2], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab, rest = l.split(' ', 1); allrows.append((lab, tokens(rest.strip())))
print('# run\tgroup\tfrozen value\tgloss piece\tmatch')
for l in open(sys.argv[3], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    r, spec, text = l.rstrip('\n').split('\t')
    for g, v, p in align_pairs(rows_of(spec, allrows), key, norm(text)):
        print('%s\t%s\t%s\t%s\t%s' % (r, g, v, p, 'K' if v and nv(v) == p else ('new' if not v else 'diff')))

"""Flexible key-free alignment of Bletchley's A115 body text to the ciphertext.
Plaintext = [wildcard prefix of length PRE] + body tokens (alternatives, optional X after each, up to MAXINS short wildcard
insertions between tokens) + wildcard suffix to length N. Wildcards take part in no constraint.
Constraints: plaintext pair <-> cipher pair is a partial bijection. Ranks candidates by satisfied equalities.
Usage: align115h.py L TOL PRE_MIN PRE_MAX [MODE drop|ins]"""
import sys, collections, heapq
import os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'orpo1942'))  # dk.py and msgs.txt stay in ../orpo1942 (split 14 Oct 2026)
import dk
L = int(sys.argv[1]); TOL = int(sys.argv[2]); PMIN = int(sys.argv[3]); PMAX = int(sys.argv[4])
MODE = sys.argv[5] if len(sys.argv) > 5 else 'drop'
MAXINS = 2
import os
RAW = open(os.environ.get('SRC', str(pathlib.Path(__file__).resolve().parent.parent / 'orpo1942' / 'msgs.txt'))).read().split('#A115\t')[1].split('\n')[0].replace(' ', '')
if MODE == 'drop': C = RAW[1:]; N = 222
else: C = '?' + RAW; N = 224
CP = [C[i:i + 2] for i in range(0, N, 2)]
LAY = dk.layout(N, L)
done_at = collections.defaultdict(list)
for k, (i, j) in enumerate(LAY): done_at[max(i, j)].append(k)

BODY = [['AN', ''], ['STRASSE', 'STRASZE', 'STR'], ['BOBRUISK', 'BOBRUIISK'], ['', 'STRIQ'], ['MOGILEW', 'MOHILEW'],
        ['PARTISANENKAMPF', 'PARTISANENKAMPFES'],
        ['SEQZEHN', 'EINSSEQS', 'SECHZEHN'], ['MANN'], ['VON', ''], ['POL', 'POLIZEI', 'PB', ''],
        ['BATL', 'BTL', 'BATAILLON', ''], ['EINUNDFUENFZIG', 'FUENFEINS', 'FUNFEINS'], ['GEFALLEN'],
        ['DAS'], ['DORF'], ['BORKI', 'BOREI'], ['IN'], ['DEM'], ['WAFFEN'], ['UND', 'U'], ['MUNITION'], ['GEFUNDEN'],
        ['WURDEN'], ['WURDE'], ['DEM'], ['ERDBODEN'], ['GLEIQGEMAQT', 'GLEICHGEMACHT'], ['DIE'],
        ['EINWOHNERSQAFT', 'EINWOHNERSCHAFT', 'EINWOHNER', 'BEVOELKERUNG'], ['LIQUIDIERT']]
ALTS = [sorted(set(w + s for w in opts for s in ('', 'X'))) for opts in BODY]
INS = ['?' * k for k in range(1, 7)]

best = []   # (score, text)
P = ['?'] * N
def check(pos, e, m, inv, viol, ok):
    m2, inv2 = m, inv
    for p in range(pos, e):
        for k in done_at[p]:
            i, j = LAY[k]; pp = P[i] + P[j]; cc = CP[k]
            if '?' in pp or '?' in cc: continue
            if m2.get(pp, cc) != cc or inv2.get(cc, pp) != pp:
                viol += 1
                if viol > TOL: return None
            else:
                if pp in m2 or cc in inv2: ok += 1
                if pp not in m2: m2 = dict(m2); m2[pp] = cc
                if cc not in inv2: inv2 = dict(inv2); inv2[cc] = pp
    return m2, inv2, viol, ok

def dfs(t, pos, m, inv, viol, ok, nins, trail):
    if t == len(ALTS):
        if pos <= N:
            for q in range(pos, N): P[q] = '?'
            r = check(pos, N, m, inv, viol, ok)
            if r is not None:
                heapq.heappush(best, (r[3] - 2 * r[2], ''.join(P[:pos]), pos));
                if len(best) > 20: heapq.heappop(best)
        return
    opts = [(w, 0) for w in ALTS[t]]
    if nins < MAXINS and t > 0: opts += [(ins + w, 1) for ins in INS for w in ALTS[t]]
    for w, di in opts:
        e = pos + len(w)
        if e > N: continue
        for q, ch in enumerate(w): P[pos + q] = ch
        r = check(pos, e, m, inv, viol, ok)
        if r is not None: dfs(t + 1, e, r[0], r[1], r[2], r[3], nins + di, trail)
        for q in range(pos, e): P[q] = '?'

for pre in range(PMIN, PMAX + 1):
    for q in range(N): P[q] = '?'
    dfs(0, pre, {}, {}, 0, 0, 0, [])
best.sort(reverse=True)
print('L', L, 'TOL', TOL, 'pre', PMIN, PMAX, MODE)
for s, txt, pos in best[:8]: print(s, pos, txt)

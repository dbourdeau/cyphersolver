"""Exact backtracking alignment of Bletchley's A115 plaintext to the ciphertext, key-free.
Token alternatives + optional X after each token; constraint: plaintext pair <-> cipher pair must be a partial bijection
(tolerating TOL violations for reception garbles). Usage: align115c.py cipherfile L TOL [order]"""
import sys, collections
import os, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'orpo1942'))  # dk.py and msgs.txt stay in ../orpo1942 (split 14 Oct 2026)
import dk
src = sys.argv[1]; L = int(sys.argv[2]); TOL = int(sys.argv[3]); ORDER = sys.argv[4] if len(sys.argv) > 4 else 'B'
C = open(src).read().split('#A115\t')[1].split('\n')[0].replace(' ', '')[1:]
N = 222
CP = [C[i:i + 2] for i in range(0, N, 2)]
LAY = dk.layout(N, L)
# for each plaintext position, the pair it belongs to and its partner position; pair complete when max(i,j) placed
done_at = collections.defaultdict(list)
for k, (i, j) in enumerate(LAY): done_at[max(i, j)].append(k)

X = 'X'
ADDR = [['AN'], ['RF', 'RFSS', 'REIQSFUEHRERSS'], ['SS', ''], ['UND'], ['QEF'], ['ORPO', 'DERORPO', 'DORPO']]
BODY = [['AN'], ['STRASSE', 'STRASZE'], ['BOBRUISK'], ['', 'STRIQ'], ['MOGILEW', 'MOGILEV'], ['PARTISANENKAMPF'],
        ['SEQZEHN', 'EINSSEQS', 'EINSXSEQS'], ['MANN'], ['VON'], ['POL', 'POLIZEI'],
        ['BATL', 'BTL', 'BATAILLON'], ['EINUNDFUENFZIG', 'FUENFEINS', 'FUENFXEINS', 'FUNFEINS'], ['GEFALLEN'],
        ['DAS'], ['DORF'], ['BOREI'], ['IN'], ['DEM'], ['WAFFEN'], ['UND'], ['MUNITION'], ['GEFUNDEN'], ['WURDEN'], ['WURDE'],
        ['DEM'], ['ERDBODEN'], ['GLEIQGEMAQT'], ['DIE'], ['EINWOHNERSQAFT'], ['LIQUIDIERT']]
SIG = [['VON', ''], ['HOEHEREN', 'HOEHERER', 'DER', 'HSSPF', 'HSSUPF'], ['SS', ''], ['UND', ''], ['POLFUEHRER', 'POLIZEIFUEHRER', ''],
       ['RUSSLAND', 'RUSZLAND'], ['MITTE']]
TOK = []
for part in ORDER: TOK += {'A': ADDR, 'B': BODY, 'S': SIG}[part]
ALTS = [sorted(set(w + s for w in opts for s in ('', X))) for opts in TOK]
ALTS = [[a for a in alts] for alts in ALTS]

sols = []
P = [''] * N
def dfs(t, pos, m, inv, viol, trail):
    if pos > N: return
    if t == len(ALTS):
        if pos >= N - 2:  # allow up to 2 filler letters at end
            sols.append((viol, ''.join(P[:pos]), trail)); 
        return
    for w in ALTS[t]:
        e = pos + len(w)
        if e > N: continue
        for q, ch in enumerate(w): P[pos + q] = ch
        m2, inv2, v2, ok = m, inv, viol, True
        added = []
        for p in range(pos, e):
            for k in done_at[p]:
                i, j = LAY[k]; pp = P[i] + P[j]; cc = CP[k]
                if m2.get(pp, cc) != cc or inv2.get(cc, pp) != pp:
                    v2 += 1
                    if v2 > TOL: ok = False; break
                else:
                    if pp not in m2: m2 = dict(m2); m2[pp] = cc
                    if cc not in inv2: inv2 = dict(inv2); inv2[cc] = pp
            if not ok: break
        if ok: dfs(t + 1, e, m2, inv2, v2, trail + [w])
dfs(0, 0, {}, {}, 0, [])
sols.sort()
print('L', L, 'order', ORDER, 'solutions', len(sols))
for s in sols[:10]: print(s[0], len(s[1]), s[1])

"""Monotone-table annealer for R4350 (Görtz 1717), adapted from swieten1757/msolve.py for German.
Hypothesis: the code is an alphabetical one-part list of letters/syllables/words, so the code->unit map is
non-decreasing. Clear words in the text are kept as literal context. usage: python msolve_de.py seed iters [bonus]
env RUNS=file (default runs.txt), MAXM (codes per unit, default 3), INIT=key.json"""
import sys, os, json, random, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.stdout.reconfigure(encoding='utf-8')
from lang import lm
HERE = os.path.dirname(os.path.abspath(__file__))
M = lm.load('de-modern', order=5, spaces=False)

def load_runs():
    runs = []
    for line in open(os.path.join(HERE, os.environ.get('RUNS', 'runs.txt')), encoding='utf-8'):
        line = line.split('#')[0].strip()
        if line: runs.append(line.split())
    return runs

V = 'aeiou'; C = 'bcdfghklmnprstwz'
def inventory():
    s = set('abcdefghiklmnopqrstuvwxyz')
    for c in C:
        for v in V: s.add(c + v)
    for v in V:
        for c in 'bcdfghklmnprstz': s.add(v + c)
    s |= {'ch','sch','st','sp','ck','ng','nd','nt','ns','rt','rs','ss','tt','ll','ff','tz','pf','qu','ei','ie','au','eu',
          'en','er','es','em','ein','eine','einer','und','der','die','das','den','dem','des','ist','nicht','mit','von',
          'zu','sie','sich','ich','wir','so','auch','als','wie','aber','oder','man','wird','werden','wurde','nach','bey',
          'vor','durch','fur','uber','haben','hat','sein','seyn','konig','czar','schweden','dennemarck','engelland',
          'preussen','hannover','frieden','friede','krieg','majestat','land','lande','ung','heit','keit','lich','isch',
          'chen','ten','ter','gen','ge','be','ver','zer','er','ent','an','auf','aus','bis','dass','doch','noch','nur',
          'wenn','weil','was','welche','solche','diese','dieser','seine','ihre','kan','konte','muss','soll','solte'}
    return sorted(s)
INV = inventory()

def main():
    seed = int(sys.argv[1]); iters = int(sys.argv[2]); BONUS = float(sys.argv[3]) if len(sys.argv) > 3 else 1.8
    rnd = random.Random(seed); runs = load_runs()
    codes = sorted({int(x) for r in runs for x in r if x.isdigit()})
    ci = {c: i for i, c in enumerate(codes)}; n = len(codes); K = len(INV)
    seqs = [[ci[int(x)] if x.isdigit() else x for x in r] for r in runs]
    MAXM = int(os.environ.get('MAXM', '3'))
    g = sorted(rnd.choices(range(K), k=n))
    def fix(g):
        run = 1
        for k in range(1, n):
            run = run + 1 if g[k] == g[k-1] else 1
            if run > MAXM: return False
        return True
    while not fix(g): g = sorted(rnd.choices(range(K), k=n))
    if os.environ.get('INIT'):
        ik = json.load(open(os.path.join(HERE, os.environ['INIT'])))
        g = [INV.index(ik[str(c)]) if ik.get(str(c)) in INV else 0 for c in codes]
        for k in range(1, n): g[k] = max(g[k], g[k-1])
    def text(g): return [''.join(INV[g[t]].upper() if 0 else (INV[g[t]] if isinstance(t, int) else t.upper()) for t in s) for s in seqs]
    def score(g):
        tot = 0.0; L = 0
        for s in seqs:
            idx = M.encode(''.join(INV[g[t]] if isinstance(t, int) else t for t in s))
            tot += M.score_idx(idx); L += len(idx)
        return tot + BONUS * L - 0.4 * sum(len(INV[x]) > 2 for x in g)
    cur = score(g); best, bestg = cur, g[:]
    T0, T1 = 8.0, 0.2
    for it in range(iters):
        T = T0 * (T1 / T0) ** (it / iters); ng = g[:]
        if rnd.random() < 0.7:
            i = rnd.randrange(n); a = ng[i-1] if i else 0; b = ng[i+1] if i < n-1 else K-1
            ng[i] = rnd.randint(a, b)
        else:
            i = rnd.randrange(n); j = min(n, i + rnd.randint(2, 25)); d = rnd.choice((-1, 1)) * rnd.randint(1, 5)
            for k in range(i, j): ng[k] += d
            if not (all(0 <= ng[k] < K for k in range(i, j)) and (i == 0 or ng[i-1] <= ng[i]) and (j == n or ng[j-1] <= ng[j])): continue
        if not fix(ng): continue
        s = score(ng)
        if s >= cur or rnd.random() < math.exp((s - cur) / T):
            g, cur = ng, s
            if cur > best: best, bestg = cur, g[:]
    print('seed', seed, 'best', round(best, 1))
    print('\n'.join(text(bestg)))
    json.dump({str(c): INV[bestg[i]] for i, c in enumerate(codes)}, open(os.path.join(HERE, f'mkey_{seed}.json'), 'w'), ensure_ascii=False)
if __name__ == '__main__': main()

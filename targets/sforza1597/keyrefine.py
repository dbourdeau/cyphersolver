"""Word-segmentation-guided refinement of a substitution key (cluster -> letter).
usage: python keyrefine.py tokens.txt solver_out.txt out_prefix [sweeps]"""
import sys, re, math, collections, random
sys.path.insert(0, 'ctts')
corpus = open('ctts/lm_qc/italian.txt', encoding='utf-8', errors='ignore').read().lower()
corpus = corpus.translate(str.maketrans({'à': 'a', 'è': 'e', 'é': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u', 'j': 'i', 'k': 'c', 'w': 'v', 'y': 'i', 'z': 's'}))
ws = collections.Counter(re.findall('[a-z]+', corpus)); N = sum(ws.values())
def norm(w): return re.sub(r'(.)\1+', r'\1', w.replace('u', 'v'))
nw = collections.Counter()
for w, c in ws.items(): nw[norm(w)] += c
two = {'di', 'il', 'la', 'le', 'lo', 'ne', 'ma', 'se', 'si', 'mi', 'ti', 'ci', 'vi', 'da', 'in', 'vn', 'su', 'ha', 'io', 'tv', 'ed', 'et', 'de', 'el', 'li', 'al', 'ai', 'an', 'ad', 'ch', 'co', 'cv', 'va', 'vi', 'ho', 'mo'}
MINW = int(__import__('os').environ.get('KR_MINW', 4))
cost = {w: -math.log(c / N) for w, c in nw.items() if (len(w) >= MINW and c >= 4)}
UNK = 10.0
def seg_cost(t):
    n = len(t); best = [1e9] * (n + 1); best[0] = 0
    for i in range(n):
        b = best[i]
        if b >= 1e9: continue
        if b + UNK < best[i + 1]: best[i + 1] = b + UNK
        for L in range(2, 13):
            if i + L > n: break
            c = cost.get(t[i:i + L])
            if c is not None and b + c < best[i + L]: best[i + L] = b + c
    return best[n]
toks = [l.split() for l in open(sys.argv[1]).read().strip().split('\n')]
key = {}
for line in open(sys.argv[2], encoding='utf-8'):
    m = re.match(r'^([s\d|]+) - ([A-Za-z])$', line.strip())
    if m:
        for c in m.group(1).split('|'): key[c] = m.group(2).lower()
types = sorted({t for l in toks for t in l}); letters = list('abcdefghilmnopqrstvxz')
def text(k): return [''.join(k.get(t, 'a') for t in l) for l in toks]
def total(k): return sum(seg_cost(s) for s in text(k))
def cover(k):
    cov = 0; tot = 0
    for s in text(k):
        n = len(s); best = [(1e9, 0)] * (n + 1); best[0] = (0, 0)
        # reuse DP but track covered letters in words >=5
        sc = [1e9] * (n + 1); cv = [0] * (n + 1); sc[0] = 0
        for i in range(n):
            if sc[i] >= 1e9: continue
            if sc[i] + UNK < sc[i + 1]: sc[i + 1] = sc[i] + UNK; cv[i + 1] = cv[i]
            for L in range(2, 13):
                if i + L > n: break
                c = cost.get(s[i:i + L])
                if c is not None and sc[i] + c < sc[i + L]: sc[i + L] = sc[i] + c; cv[i + L] = cv[i] + (L if L >= 5 else 0)
        cov += cv[n]; tot += n
    return cov / tot
base = total(key); print('start cost', round(base), 'coverage', round(cover(key), 3), flush=True)
sweeps = int(sys.argv[4]) if len(sys.argv) > 4 else 3
for sw in range(sweeps):
    changed = 0
    order = types[:]; random.seed(sw); random.shuffle(order)
    for t in order:
        cur = key.get(t, 'a'); bestL, bestC = cur, base
        for L in letters:
            if L == cur: continue
            key[t] = L; c = total(key)
            if c < bestC - 1e-6: bestL, bestC = L, c
        key[t] = bestL
        if bestL != cur: changed += 1; base = bestC
    print('sweep', sw + 1, 'changed', changed, 'cost', round(base), 'coverage', round(cover(key), 3), flush=True)
open(sys.argv[3] + '_key.txt', 'w').write('\n'.join(f'{t} - {L.upper()}' for t, L in sorted(key.items())) + '\n')
open(sys.argv[3] + '_text.txt', 'w').write('\n'.join(text(key)) + '\n')

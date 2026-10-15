"""R722 second three-figure code: anneal group -> Italian syllable.
Score = it-cinquecento char LM over each coded segment (segments bounded by clear text, spaces removed)
      + run bonus: groups g and g+1 that share a consonant and step one vowel (a e i o u) earn a reward,
        the layout R701 p.3 shows (209-213 va..vu, 244 ra 245 re, 366-370 la..lu).
Usage: python solve722.py [restarts] [iters]"""
import re, sys, math, random, collections
sys.path.insert(0, '../..')
from lang import lm

V = 'aeiou'
CONS = ['b','c','d','f','g','l','m','n','p','qu','r','s','t','v','z','ch','gh','gl','gn','sc','st','pr','tr','gr','br','cr','fr','pi','gi','ci']
SYL = [c + v for c in CONS for v in V] + list(V) + ['l','n','r','s','m','t','d','c','p'] + \
      ([] if __import__('os').environ.get('NOWORDS') else ['il','di','che','per','non','et','del','al','con','in']) + ['il','che','gli','e']
SYL = sorted(set(SYL))

def parse(path='r722_groups.txt'):
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'^#.*$', '', t, flags=re.M)
    t = re.sub(r'^\d\d ', '', t, flags=re.M)
    t = re.sub(r'<[^>]*>', ' | ', t, flags=re.S)
    segs, cur = [], []
    for x in re.findall(r'\||\b\d{3}\b', t):
        if x == '|':
            if cur: segs.append(cur); cur = []
        else: cur.append(int(x))
    if cur: segs.append(cur)
    return segs

def split(s):
    for c in sorted(CONS, key=len, reverse=True):
        if s.startswith(c) and len(s) == len(c) + 1 and s[-1] in V: return c, V.index(s[-1])
    if s in V: return '', V.index(s)
    return None, None

RB = float(__import__('os').environ.get('RB','6'))
BASE = float(__import__('os').environ.get('BASE', '2.6'))
MAXH = 2
TD = 0.99999
R701 = {}
for base, c in [(209,'v'),(231,'s'),(322,'pr'),(333,'ch'),(366,'l'),(375,'d'),(510,'st')]:
    for k, v in enumerate(V): R701[base + k] = c + v
R701[244] = 'ra'; R701[245] = 're'
FIX = dict(R701) if __import__('os').environ.get('R701') else {}
FIX.update({525: 'il', 245: 're', 334: 'che', 541: 'gli', 449: 'e'})

def main(restarts=6, iters=60000, seed=1):
    M = lm.load('it-cinquecento', order=5, spaces=False)
    segs = parse()
    types = sorted({g for s in segs for g in s})
    sp = {s: split(s) for s in SYL}
    occ = collections.defaultdict(set)
    for i, s_ in enumerate(segs):
        for g in s_: occ[g].add(i)
    def segscore(key, i):
        t = ''.join(key[g] for g in segs[i]); return M.score(t) + BASE * len(t)
    def hom(key, syl): return sum(1 for x in key.values() if x == syl)
    def runb(key, g):
        if g not in key or g + 1 not in key: return 0.0
        a, b = sp[key[g]], sp[key[g + 1]]
        return RB if (a[0] is not None and a[0] == b[0] and b[1] == a[1] + 1) else 0.0
    rnd = random.Random(seed); best = None
    for r in range(restarts):
        key = {g: FIX.get(g, rnd.choice(SYL)) for g in types}
        ss = [segscore(key, i) for i in range(len(segs))]
        cur = sum(ss) + sum(runb(key, g) for g in types); T = 8.0
        for it in range(iters):
            g = rnd.choice(types)
            if g in FIX: continue
            old = key[g]
            if rnd.random() < 0.3 and (g - 1) in key and sp[key[g - 1]][0] is not None and sp[key[g-1]][1] < 4:
                c, vi = sp[key[g - 1]]; key[g] = c + V[vi + 1]
            else:
                key[g] = rnd.choice(SYL)
            if key[g] == old or hom(key, key[g]) > MAXH: key[g] = old; continue
            ob = runb({**key, g: old}, g - 1) + runb({**key, g: old}, g)
            nb = runb(key, g - 1) + runb(key, g)
            news = {i: segscore(key, i) for i in occ[g]}
            d = sum(news[i] - ss[i] for i in news) + nb - ob
            if d >= 0 or rnd.random() < math.exp(d / T):
                cur += d
                for i in news: ss[i] = news[i]
            else: key[g] = old
            T = max(0.3, T * TD)
        print(f'restart {r} score {cur:.1f}', flush=True)
        if best is None or cur > best[0]: best = (cur, dict(key))
    cur, key = best
    print('best', round(cur, 1))
    for s in segs: print(' '.join(key[g] for g in s), '   ||', ''.join(key[g] for g in s))
    print(' '.join(f'{g}={key[g]}' for g in types))

if __name__ == '__main__':
    a = sys.argv[1:]
    main(int(a[0]) if a else 6, int(a[1]) if len(a) > 1 else 60000)

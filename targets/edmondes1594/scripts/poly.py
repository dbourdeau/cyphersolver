"""Polyphonic substitution solver for the printed Edmondes cipher (HMC Salisbury IV pp. 559-560).

Model: every printed cipher letter stands for one plain letter, or (if the print merged two manuscript signs, or the
cipher itself gives a sign two values) for one of two plain letters. Several printed letters may stand for the same
plain letter (homophones). Given a key, the best reading of each segment is found exactly by dynamic programming
under a letter-quadgram model of 1590s English (lm.py). Key score = mean log10 probability per letter of the best
reading, minus LAM per printed letter given two values. Search: simulated annealing over keys.

Usage: python3 -I poly.py [--seed N] [--iters N] [--lam X] [--init shift|random] [--ct FILE] [--segs a-b]
"""
import sys, os, re, random, math, json, argparse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lm
PA = lm.PA
M, FLOOR = lm.load(4)
_t = lm.corpus(); UNI = {a: (_t.count(a) + 1) / (len(_t) + 24) for a in PA}; del _t
CHIW = 0.5
PRIMARY_LOCK = False

def read_ct(path):
    segs, labels = [], []
    for l in open(path):
        if l[:1] not in 'AB' or ' ' not in l: continue
        lab, body = l.split(' ', 1)
        body = re.sub(r'\[[^\]]*\]', ' | ', body)
        for k, part in enumerate(body.split('|')):
            t = re.sub('[^a-z]', '', part)
            if len(t) >= 3:
                segs.append(t); labels.append(f'{lab}.{k}')
    return segs, labels

def q(s):
    return M.get(s, FLOOR)

def best_reading(seg, key):
    """key: dict cipher letter -> tuple of 1 or 2 plain letters. Exact DP with 3-letter history."""
    states = {'': (0.0, '')}
    for ch in seg:
        new = {}
        for hist, (sc, txt) in states.items():
            for p in key[ch]:
                h4 = hist + p
                add = q(h4) if len(h4) == 4 else 0.0
                nh = h4[-3:]
                v = sc + add
                if nh not in new or v > new[nh][0]:
                    new[nh] = (v, txt + p)
        states = new
    sc, txt = max(states.values())
    return sc, txt

def score(segs, key, lam):
    tot = 0.0; n = 0; out = []
    for s in segs:
        sc, txt = best_reading(s, key)
        tot += sc; n += max(1, len(s) - 3); out.append(txt)
    duals = sum(1 for v in key.values() if len(v) == 2)
    body = ''.join(out); N = len(body)
    chi = sum((body.count(a) - N*UNI[a])**2 / (N*UNI[a] + 1) for a in PA) / N
    return tot / n - lam * duals - CHIW * chi, out

SHIFT = {c: PA[(PA.index(c) + 7) % 24] for c in PA}  # Caesar shift of 7 in the 24-letter alphabet
SHIFT['v'] = 'c'; SHIFT['j'] = 'i'

def anneal(segs, letters, rng, iters, lam, init, fixed=None, T0=0.02):
    fixed = fixed or {}
    if init == 'shift':
        key = {c: (SHIFT.get(c, 'e'),) for c in letters}
    else:
        key = {c: (rng.choice('etaoinshrdlu'),) for c in letters}
    key.update(fixed)
    free = [c for c in letters if c not in fixed]
    cur, _ = score(segs, key, lam); best = (cur, dict(key))
    T = T0
    for it in range(iters):
        c = rng.choice(free); old = key[c]; r = rng.random()
        if PRIMARY_LOCK and c in SHIFT:
            nv = (SHIFT[c], rng.choice(PA)) if r < 0.85 else (SHIFT[c],)
        elif r < 0.65:
            nv = (rng.choice(PA),) + old[1:]
        elif r < 0.9:
            nv = (old[0], rng.choice(PA))
        else:
            nv = (old[0],) if len(old) == 2 else (rng.choice(PA), old[0])
        if len(nv) == 2 and nv[0] == nv[1]: nv = (nv[0],)
        key[c] = nv
        sc, _ = score(segs, key, lam)
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            cur = sc
            if sc > best[0]: best = (sc, dict(key))
        else:
            key[c] = old
        T = max(0.0005, T0 * (1 - it / iters))
    return best

def keystr(key):
    return ' '.join(c + '=' + '/'.join(key[c]) for c in sorted(key))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--ct', default=os.path.join(HERE, '..', 'transcription', 'pass1.txt'))
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--iters', type=int, default=20000)
    ap.add_argument('--lam', type=float, default=0.03)
    ap.add_argument('--init', default='random')
    ap.add_argument('--shuffle', type=int, default=0, help='shuffle the letters across all segments with this seed (control)')
    ap.add_argument('--restarts', type=int, default=1)
    ap.add_argument('--chiw', type=float, default=0.5)
    ap.add_argument('--lock', action='store_true', help='each letter keeps its shift-7 value as one option; search only the second value')
    ap.add_argument('--fix', default='', help='comma list like a=h,b=i or a=h/x')
    a = ap.parse_args()
    CHIW = a.chiw
    PRIMARY_LOCK = a.lock
    segs, labels = read_ct(a.ct)
    if a.shuffle:
        allc = list(''.join(segs)); random.Random(a.shuffle).shuffle(allc)
        it = iter(allc); segs = [''.join(next(it) for _ in s) for s in segs]
    letters = sorted(set(''.join(segs)))
    rng = random.Random(a.seed); best = (-99, None)
    for r in range(a.restarts):
        fx = {kv.split('=')[0]: tuple(kv.split('=')[1].split('/')) for kv in a.fix.split(',') if kv}
        b = anneal(segs, letters, rng, a.iters, a.lam, a.init, fixed=fx)
        if b[0] > best[0]: best = b
    sc, out = score(segs, best[1], a.lam)
    raw, _ = score(segs, best[1], 0.0)
    print(json.dumps({'score': round(sc, 4), 'raw': round(raw, 4), 'seed': a.seed, 'shuffle': a.shuffle, 'init': a.init,
                      'lam': a.lam, 'key': keystr(best[1])}))
    for lab, t in zip(labels, out): print(lab, t)

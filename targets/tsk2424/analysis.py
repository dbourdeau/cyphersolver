"""Sign statistics and shuffle controls for a token transcription (shared by tsk2424 and tsk2437).
Usage: python analysis.py <transcription file> [--drop '?']
Lines look like 'L1: tok tok . tok -'; '-', '.', '|' are dividers (kept for word-length stats, dropped for sign stats)."""
import sys, random, math, collections
import numpy as np

path = sys.argv[1]
drop = set()
if '--drop' in sys.argv:
    drop = set(sys.argv[sys.argv.index('--drop') + 1].split(','))
DIV = {'-', '.', '|'}
lines = []
for l in open(path, encoding='utf-8'):
    if l.startswith('L') and ':' in l:
        lines.append(l.split(':', 1)[1].split())
signs = [[t for t in ln if t not in DIV and t not in drop] for ln in lines]
flat = [t for ln in signs for t in ln]
N = len(flat)
cnt = collections.Counter(flat)
V = len(cnt)


def ic(seq):
    c = collections.Counter(seq)
    n = len(seq)
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def ent(seq):
    c = collections.Counter(seq)
    n = len(seq)
    return -sum(v / n * math.log2(v / n) for v in c.values())


def rep_ngrams(ls, n):
    seen = collections.Counter()
    for ln in ls:
        for i in range(len(ln) - n + 1):
            seen[tuple(ln[i:i + n])] += 1
    return sum(1 for v in seen.values() if v > 1), sum(v for v in seen.values() if v > 1)


print('signs', N, 'distinct', V, 'lines', len(lines), 'per line', [len(s) for s in signs])
print('IC %.4f (uniform %.4f)  entropy %.3f bits (max %.3f)' % (ic(flat), 1 / V, ent(flat), math.log2(V)))
print('top', cnt.most_common(12))
random.seed(5)
res = collections.defaultdict(list)
for _ in range(300):
    sh = flat[:]
    random.shuffle(sh)
    pos = 0
    ls = []
    for s in signs:
        ls.append(sh[pos:pos + len(s)])
        pos += len(s)
    res['ic'].append(ic(sh))
    for n in (2, 3, 4):
        res['r%d' % n].append(rep_ngrams(ls, n)[0])
for n in (2, 3, 4):
    obs = rep_ngrams(signs, n)[0]
    a = np.array(res['r%d' % n])
    print('repeated %d-grams: observed %d, shuffle mean %.1f sd %.1f, z %.2f' % (n, obs, a.mean(), a.std(), (obs - a.mean()) / (a.std() or 1)))
a = np.array(res['ic'])
print('IC shuffle mean %.4f (same as observed by construction)' % a.mean())
# bigram dependence: conditional entropy vs shuffle
def cond_ent(ls):
    big = collections.Counter()
    uni = collections.Counter()
    for ln in ls:
        for x, y in zip(ln, ln[1:]):
            big[(x, y)] += 1
            uni[x] += 1
    n = sum(big.values())
    return -sum(v / n * math.log2(v / uni[x]) for (x, y), v in big.items())


obs = cond_ent(signs)
ce = []
for _ in range(300):
    sh = flat[:]
    random.shuffle(sh)
    pos = 0
    ls = []
    for s in signs:
        ls.append(sh[pos:pos + len(s)])
        pos += len(s)
    ce.append(cond_ent(ls))
ce = np.array(ce)
print('H(next|prev) observed %.3f, shuffle mean %.3f sd %.3f, z %.2f (plug-in estimate; V=%d small-sample bias is the same in both)' % (obs, ce.mean(), ce.std(), (obs - ce.mean()) / ce.std(), V))
# position: first and last sign of lines
first = collections.Counter(s[0] for s in signs if s)
last = collections.Counter(s[-1] for s in signs if s)
print('line-initial', first.most_common(6), ' line-final', last.most_common(6))
# word lengths by dividers
wl = collections.Counter()
for ln in lines:
    cur = 0
    for t in ln:
        if t in DIV:
            if cur:
                wl[cur] += 1
            cur = 0
        elif t not in drop:
            cur += 1
    if cur:
        wl[cur] += 1
print('group lengths between dividers', sorted(wl.items()))

"""Held-out test as written in test/TEST_PLAN.md.
Usage: python3 -I heldout_test.py <key.tsv> <heldout transcription> [n_shuffles=200]"""
import os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kcommon import parse, norm, align


def load_key(path):
    k = {}
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        f = l.rstrip('\n').split('\t')
        k[int(f[0])] = [norm(f[1])]
    return k


def score(groups, text, key):
    out, _, _ = align(groups, text, key)
    scored = [(gi, how) for gi, sl, how in out if groups[gi]['kind'] == 'code']
    hit = sum(1 for gi, how in scored if how == 'match')
    return hit, len(scored)


key = load_key(sys.argv[1])
pages = parse(sys.argv[2])
nsh = int(sys.argv[3]) if len(sys.argv) > 3 else 200
groups, text = [], ''
for p in pages:
    for L in p['lines']:
        text += norm(L['gloss'])
        groups += L['codes']
hit, n = score(groups, text, key)
print('key %s: %d/%d = %.3f' % (os.path.basename(sys.argv[1]), hit, n, hit / n))
rng = random.Random(1759)
codes = sorted(key)
vals = [key[c] for c in codes]
sh = []
for s in range(nsh):
    v = vals[:]
    rng.shuffle(v)
    h, _ = score(groups, text, dict(zip(codes, v)))
    sh.append(h / n)
sh.sort()
print('shuffled keys (%d): mean %.3f, median %.3f, max %.3f' % (nsh, sum(sh) / nsh, sh[nsh // 2], sh[-1]))
print('groups scored', n, '| lost/numeral groups not scored', sum(1 for g in groups if g['kind'] != 'code'))

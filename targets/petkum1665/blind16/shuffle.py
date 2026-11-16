"""shuffle.py : shuffled-key control for the blind Paulmyer decodes of 16 Nov 2026 (python3 -I, run from anywhere).

Each frozen BLIND.tsv is decoded with the frozen key (_key_frozen/key_v5.tsv, upstream targets/petkum1665/key_v5.tsv
of commit 89e25ef) by the same token rule as decode_once.py ('~' and '?' stripped for lookup). Only spelled values
are scored: a key row whose value is 1-3 letters (a-z) and not 'et' is a spelled sign; a code word (longer value),
a sign not in the key, or an unknown token breaks the run. Spelled runs are joined with single spaces, normalised
with lang.lm.norm(.., 'early') and scored with the repo model fr-1600-letters (French 1570-1640 letters, order 5,
spaces) as mean log-probability per scored character (lm.per_char).
Shuffle: the values of all spelled key rows are permuted among those signs (random.Random(seed).shuffle of the
value list), the same tokens decoded and scored again, 5,000 times per seed. Reported: real score, count of shuffles
>= real, max shuffle score. Pass bar (fixed before the run): fewer than 5 of 5,000 at or above the real score, at
both seeds 20261112 and 7. Short texts may fail; a failing document is filed as a recorded result, not a reading.
Nothing here edits a frozen file.
"""
import sys, os, re, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, ROOT)
from lang import lm

KF = os.path.join(HERE, '_key_frozen', 'key_v5.tsv')
KEY_SHA = '1d0cf98298f269ef3b6079ef9a61f6c12dfa66d6021df63b3ade5e2e7549eeee'
SEEDS = (20261112, 7); N = 5000; MODEL = 'fr-1600-letters'

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def load_key():
    key = {}
    for l in open(KF, encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p = l.rstrip('\n').split('\t'); key[p[0]] = p[1]
    return key

def spelled(v): return re.fullmatch(r'[a-z]{1,3}', v) is not None and v != 'et'

def runs(folder, key):
    bl = os.path.join(folder, 'BLIND.tsv')
    assert sha(bl) == open(os.path.join(folder, 'FREEZE_blind.txt'), encoding='utf8').read().split()[0], 'BLIND hash mismatch'
    out = []
    for l in open(bl, encoding='utf8'):
        if l.startswith('#') or not l.strip() or l.startswith('image\t'): continue
        cur = []
        for raw in l.rstrip('\n').split('\t')[2].split():
            t = raw.replace('~', '').replace('?', '')
            if t in key and spelled(key[t]): cur.append(t)
            else:
                if cur: out.append(cur)
                cur = []
        if cur: out.append(cur)
    return out

def main(folders):
    assert sha(KF) == KEY_SHA, 'key hash mismatch'
    key = load_key(); m = lm.load(MODEL)
    signs = sorted(s for s in key if spelled(key[s])); vals = [key[s] for s in signs]
    lines = ['# shuffle_out.txt: shuffled-key control, model %s, %d shuffles per seed, seeds %s; %d spelled key rows permuted' % (MODEL, N, SEEDS, len(signs)),
             '# key_v5.tsv sha256 %s; shuffle.py sha256 %s' % (KEY_SHA, sha(os.path.abspath(__file__))),
             '# doc\tseed\tspelled_tokens\tscored_chars\treal\tcount_ge_real\tmax_shuffle\tmean_shuffle\tverdict']
    for f in folders:
        R = runs(f, key); ntok = sum(map(len, R))
        def dec(mp): return lm.norm(' '.join(''.join(mp[t] for t in r) for r in R), 'early')
        real = m.per_char(dec(key)); nch = len(m.encode(dec(key))); res = []
        for seed in SEEDS:
            r = random.Random(seed); ge = 0; mx = -1e9; tot = 0.0
            for _ in range(N):
                v = vals[:]; r.shuffle(v); s = m.per_char(dec(dict(zip(signs, v))))
                ge += s >= real; mx = max(mx, s); tot += s
            res.append(ge)
            lines.append('%s\t%d\t%d\t%d\t%.4f\t%d\t%.4f\t%.4f\t%s' % (os.path.basename(os.path.normpath(f)), seed, ntok, nch, real, ge, mx, tot / N, 'pass' if ge < 5 else 'FAIL'))
        lines.append('%s\toverall\t\t\t\t\t\t\t%s' % (os.path.basename(os.path.normpath(f)), 'PASS (both seeds < 5/5000)' if all(g < 5 for g in res) else 'FAIL'))
        print('\n'.join(lines[-3:]), flush=True)
    return lines

if __name__ == '__main__':
    out = main(sys.argv[1:])
    open(os.path.join(HERE, 'shuffle_out.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

"""Sense measure for the *_signs.txt files (stats.py counts every sign that has a key value, sense or not).

A sign counts as read-as-sense only when its letter sits inside a word of 16th-c. French (vocabulary from the
lang/ corpora behind fr-1530-despatches, 'early' normalisation) or of the short list of proper names below,
found by a best-coverage segmentation of each line's read letters. '?' breaks words. A run of read letters
between '?' shorter than 4 counts as unread (too short to be checked). Nulls ('.') are left out of both sides;
'#' (name code read from its gloss) and 'N' (numeral) count as read.
Usage: python sense.py R3697_signs.txt [R4232_signs.txt ...] [-v]
"""
import os, re, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm, corpora

NAMES = {'rangone', 'hieronymus', 'hieronimo', 'vesprim', 'vesprym', 'turc', 'sansacque', 'gueny', 'anthone',
         'leyve', 'marseille', 'provence', 'gennes', 'naples', 'secile', 'sicile', 'barberousse', 'forest',
         'vaulx', 'garde', 'hongrie', 'suisses', 'empereur'}
SINGLE = {'a', 'y', 'e', 'o'}
ELIDED = {'l', 'd', 's', 'n', 'm', 'c', 't', 'qu', 'z'}  # l' d' s' n' m' c' t' qu', plural -z
EXTRA = {'umbre', 'quelz', 'mediterranee', 'mediteranee', 'naples', 'ladicte', 'seur', 'meu'}


def vocab():
    cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'work', 'vocab_fr1530.txt')
    if os.path.exists(cache):
        return set(open(cache, encoding='utf-8').read().split())
    t = corpora.text(['fr-1520s-diplomatic'])
    c = collections.Counter(lm.norm(t, 'early').split())
    v = {w for w, n in c.items() if n >= 2 and (len(w) > 1 or w in SINGLE)}
    open(cache, 'w', encoding='utf-8').write('\n'.join(sorted(v)))
    return v


def segment(s, V):
    """max letters covered by vocabulary words; returns (covered, words)"""
    n = len(s); best = [(0, [])] + [None] * n
    for i in range(1, n + 1):
        cand = (best[i - 1][0], best[i - 1][1] + ['<' + s[i - 1] + '>'])
        for j in range(max(0, i - 18), i):
            w = s[j:i]
            if w in V and best[j][0] + len(w) > cand[0]:
                cand = (best[j][0] + len(w), best[j][1] + [w])
        best[i] = cand
    return best[n]


def measure(path, V, verbose=False):
    """lines are joined in file order (words run over line ends); '?' and a blank label change break runs"""
    read = tot = 0; stream = []
    for line in open(path, encoding='utf-8'):
        if not line.strip() or line.startswith('#'): continue
        lab, body = line.split(None, 1)
        sig = [ch for ch in body.strip().replace(' ', '') if ch != '.']
        tot += len(sig)
        read += sum(1 for ch in sig if ch in '#N')
        stream.append(''.join('?' if ch in '#N' else ch for ch in sig))
    for run in re.split(r'\?+', ''.join(stream)):
        if len(run) < 4:
            if run and verbose: print('  short, not counted:', run)
            continue
        cov, ws = segment(lm.norm(run, 'early').replace(' ', ''), V)
        read += cov
        if verbose: print(' '.join(ws))
    return read, tot


if __name__ == '__main__':
    V = vocab() | NAMES | ELIDED | EXTRA
    files = [a for a in sys.argv[1:] if not a.startswith('-')]
    R = T = 0
    for f in files:
        r, t = measure(f, V, '-v' in sys.argv)
        R += r; T += t
        print('%s: %d / %d non-null signs read as sense = %.1f%%' % (f, r, t, 100 * r / t))
    if len(files) > 1: print('all: %d / %d = %.1f%%' % (R, T, 100 * R / T))

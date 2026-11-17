"""shuffle.py : shuffled-key control for the blind sibling decodes of 16 Nov 2026 (python3 -I, run from anywhere).

For each document folder given, the frozen BLIND.tsv is decoded with the frozen key (FREEZE/key_upstream.tsv, the
upstream key.tsv of commit 89e25ef) exactly as decode_once.py does it (first option of an [a|b] alternative; blots,
drawn symbols {S:..}, marks and struck tokens are not letters and are left out), the decoded words are joined with
single spaces, normalised with lang.lm.norm(.., 'early') and scored with the repo model de-1640s
(lang/models.json: German 1600-1670, order 5, spaces) as mean log-probability per scored character
(lm.per_char). Then the plaintext values of the key's single-letter rows are permuted among the cipher signs
(random.Random(seed).shuffle of the value list; every permutation allowed, not only reciprocal ones), the same text
is decoded and scored, 5,000 times per seed. Reported: real score, count of shuffles >= real, max shuffle score.
Pass bar (fixed before the run): fewer than 5 of 5,000 at or above the real score, at both seeds 20261112 and 7.
Nothing here edits a frozen file.
"""
import sys, os, re, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, ROOT)
from lang import lm
import numpy as np

KF = os.path.join(HERE, 'FREEZE', 'key_upstream.tsv')
KEY_SHA = 'c734821ef7ae8d062d63873fee0642e42db9fc4eebcd9a8d7355afb8e2aea2fe'
SEEDS = (20261112, 7); N = 5000; MODEL = 'de-1640s'

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def load_key():
    k = {}
    for l in open(KF, encoding='utf-8'):
        if l.startswith('#') or l.startswith('cipher\t') or not l.strip(): continue
        f = l.rstrip('\n').split('\t')
        if len(f[0]) == 1: k[f[0]] = f[1]
    return k

def cipher_words(folder):
    bl = os.path.join(folder, 'BLIND.tsv')
    assert sha(bl) == open(os.path.join(folder, 'FREEZE_blind.txt')).read().split()[0], 'BLIND.tsv hash mismatch'
    rows = [l.rstrip('\n').split('\t') for l in open(bl, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]
    out = []
    for img, ln, tok, cw in rows:
        if tok.startswith('{struck:') or re.fullmatch(r'\{S:[^}]*\}', tok): continue
        w = []; i = 0
        while i < len(tok):
            if tok[i] == '{': i = tok.index('}', i) + 1; continue
            if tok[i] == '[':
                j = tok.index(']', i); w.append(tok[i+1:j].split('|')[0].lower()); i = j + 1
            else:
                w.append(tok[i].lower()); i += 1
        if w: out.append(''.join(w))
    return out

def main(folders):
    assert sha(KF) == KEY_SHA, 'key hash mismatch'
    key = load_key(); m = lm.load(MODEL)
    signs = sorted(key); vals = [key[s] for s in signs]
    lines = ['# shuffle_out.txt: shuffled-key control, model %s, %d shuffles per seed, seeds %s' % (MODEL, N, SEEDS),
             '# key sha256 %s; shuffle.py sha256 %s' % (KEY_SHA, sha(os.path.abspath(__file__))),
             '# doc\tseed\tscored_chars\treal\tcount_ge_real\tmax_shuffle\tmean_shuffle\tverdict']
    for f in folders:
        words = cipher_words(f)
        text = ' '.join(words)
        def dec(mapping): return lm.norm(''.join(mapping.get(c, c) if c != ' ' else ' ' for c in text), 'early')
        real = m.per_char(dec(key)); n_ch = len(m.encode(dec(key)))
        res = []
        for seed in SEEDS:
            r = random.Random(seed); ge = 0; mx = -1e9; tot = 0.0
            for _ in range(N):
                v = vals[:]; r.shuffle(v); s = m.per_char(dec(dict(zip(signs, v))))
                ge += s >= real; mx = max(mx, s); tot += s
            res.append(ge)
            lines.append('%s\t%d\t%d\t%.4f\t%d\t%.4f\t%.4f\t%s' % (os.path.basename(os.path.normpath(f)), seed, n_ch, real, ge, mx, tot / N,
                                                       'pass' if ge < 5 else 'FAIL'))
        lines.append('%s\toverall\t\t\t\t\t\t%s' % (os.path.basename(os.path.normpath(f)), 'PASS (both seeds < 5/5000)' if all(g < 5 for g in res) else 'FAIL'))
        print('\n'.join(lines[-3:]), flush=True)
    return lines

if __name__ == '__main__':
    out = main(sys.argv[1:])
    open(os.path.join(HERE, 'shuffle_out.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')

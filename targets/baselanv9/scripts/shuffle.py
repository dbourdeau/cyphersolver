"""Shuffle control. The frozen key's values are permuted among the key's base tokens (the modifier tokens +^ +_ +" and
the two rules stay as they are), 5,000 keys per seed (20261112 and 7). Each shuffled key decodes the same held-out
transcription. Two statistics:
  (1) la-letters language model, mean log-probability per character (order 5, with spaces), all held-out and per page;
  (2) for H2 and H1, the share of clear-copy letters reproduced (same Levenshtein scoring as score_clear.py, strict).
Reports real vs shuffles: mean, sd, best shuffle, z, and how many shuffles reach the real value."""
import sys, os, random, statistics, re
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, '/home/claude/keyless/_cs')
from lang import lm
from common import read_tx, split_sign
import score_clear as SC  # noqa: E402  (runs the clear scoring once on import; harmless)

D = '/home/claude/keyless/round40c/basel_anv9/'
key, rules = {}, {}
for ln in open(D + 'KEY.tsv'):
    p = ln.rstrip('\n').split('\t')
    if ln.startswith('token'):
        continue
    if p[0] == '#RULE':
        rules[p[1]] = p[2]; continue
    key[p[0]] = '' if p[1] == '-' else p[1]
VOW = 'aeiou'
MODS = {'+^', '+_', '+"'}
FIXED = {'D2'}  # rule-driven
perm_tokens = sorted(t for t in key if t not in MODS and t not in FIXED)


def dec_words(words, k):
    out = []
    for w in words:
        toks = []
        for s in w:
            if s in ('Eq', 'Fill'):
                continue
            toks += split_sign(s)
        o, prev = '', ''
        for t in toks:
            if t == 'D2':
                v = [c for c in o if c in VOW]; s2 = v[-1] if v else 'i'
            elif t == '+"':
                s2 = prev
            else:
                s2 = k.get(t, '?')
            o += s2; prev = s2
        out.append(o)
    return out


PAGES = {'H1': 'tx/f015r.txt', 'H2': 'tx/f159r.txt', 'H3': 'tx/f034r_p34.txt'}
TX = {h: read_tx(D + f) for h, f in PAGES.items()}
M = lm.load('la-letters')


def lm_score(k, pages):
    words = []
    for h in pages:
        for lid, ws in TX[h]:
            words += dec_words(ws, k)
    txt = ' '.join(w.replace('?', ' ') for w in words)
    return M.per_char(lm.norm(txt, 'latin'))


clearH2 = {}
for ln in open(D + 'score/CLEAR_H2_f167r.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    a, b = ln.rstrip('\n').split('\t'); clearH2[a] = SC.letters(SC.norm(b, True))
clearH1 = SC.letters(SC.norm(' '.join(l for l in open(D + 'score/CLEAR_H1_f109v.txt') if not l.startswith('#')), True))
clearH3 = {}
for ln in open(D + 'score/CLEAR_H3_f123r.txt'):
    if ln.startswith('#') or not ln.strip(): continue
    a, b = ln.rstrip('\n').split('\t'); clearH3[a] = SC.letters(SC.norm(b, True))


def clear_counts(k, h):
    tot = mt = 0
    if h in ('H2', 'H3'):
        ref = clearH2 if h == 'H2' else clearH3
        for lid, ws in TX[h]:
            d = ''.join(dec_words(ws, k))
            e, m_ = SC.lev(d, ref.get(lid, '')); tot += len(ref.get(lid, '')); mt += m_
        return mt, tot
    d = ''.join(''.join(dec_words(ws, k)) for lid, ws in TX['H1'])
    e, m_ = SC.lev(d, clearH1)
    return m_, len(clearH1)


def clear_all(k):
    m = t = 0
    for h in ('H1', 'H2', 'H3'):
        a, b = clear_counts(k, h); m += a; t += b
    return m / t


def clear_score(k, h):
    if h == 'H3':
        a, b = clear_counts(k, h); return a / b
    if h == 'H2':
        tot = mt = 0
        for lid, ws in TX['H2']:
            d = ''.join(dec_words(ws, k))
            e, m_ = SC.lev(d, clearH2.get(lid, '')); tot += len(clearH2.get(lid, '')); mt += m_
        return mt / tot
    d = ''.join(''.join(dec_words(ws, k)) for lid, ws in TX['H1'])
    e, m_ = SC.lev(d, clearH1)
    return m_ / len(clearH1)


out = []
STATS = [('LM all held-out', lambda k: lm_score(k, ['H1', 'H2', 'H3'])),
         ('LM H1', lambda k: lm_score(k, ['H1'])),
         ('LM H2', lambda k: lm_score(k, ['H2'])),
         ('LM H3 (pentacle rims)', lambda k: lm_score(k, ['H3'])),
         ('clear-match H2', lambda k: clear_score(k, 'H2')),
         ('clear-match H1', lambda k: clear_score(k, 'H1')),
         ('clear-match H3', lambda k: clear_score(k, 'H3')),
         ('clear-match all held-out', clear_all)]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
for seed in (20261112, 7):
    rnd = random.Random(seed)
    keys = []
    vals = [key[t] for t in perm_tokens]
    for i in range(N):
        v = vals[:]; rnd.shuffle(v)
        k = dict(key); k.update(dict(zip(perm_tokens, v)))
        keys.append(k)
    for name, fn in STATS:
        ks = keys
        real = fn(key)
        ss = [fn(k) for k in ks]
        mu = statistics.mean(ss); sd = statistics.pstdev(ss) or 1e-9
        beat = sum(s >= real for s in ss)
        out.append('%-38s seed %-9d tokens permuted %d  real %.3f  shuffles mean %.3f sd %.3f best %.3f  z %.1f  shuffles>=real %d/%d'
                   % (name, seed, len(perm_tokens), real, mu, sd, max(ss), (real - mu) / sd, beat, len(ss)))
        print(out[-1], flush=True)
open(D + 'score/shuffle_out.txt', 'w').write('\n'.join(out) + '\n')

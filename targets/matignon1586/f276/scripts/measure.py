"""Coverage of a sign-by-sign reading (f. 276, f. 179) after the rule in targets/matignon1586/measure.py: a cipher sign
counts as READ only if it has a value (not '?') and its letters fall inside a sense run of at least MINWORDS lexical
words totalling at least MINLETTERS letters. A word is lexical if it occurs at least MINCOUNT times in the corpus of a
shared lang/ model (default fr-1600-letters = fr-henri4, Lettres missives de Henri IV), normalised with that model's
scheme, or is one of the one-letter words a / y. Lines are joined. Word signs (=de, =que ...) are words. An unkeyed sign
('?') inside a run is a CONTEXT token: it does not break the run and is never counted read (the target's measure.py
lets its language model supply that letter; here it simply passes through).
Control: the same rule with the letter values permuted among the signs (shuffled key).
    python measure.py read_final.txt [n_shuffles] [--model fr-1600-letters] [--mincount 20]
"""
import os, sys, re, math, random, argparse, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..')
sys.path.insert(0, ROOT)
from lang import lm, corpora

MINWORDS, MINLETTERS = 3, 10
A = 'abcdefghilmnopqrstuxz'
UNK = 7.0

def norm(w, scheme):
    return lm.norm(w, scheme).replace('y', 'i')      # the cipher has one sign class for i/y; j->i, v->u from 'early'

def lexicon(model, mincount):
    spec = lm.registry()[0][model]
    cnt = collections.Counter(norm(corpora.text(spec['sources']), spec['norm']).split())
    tot = sum(cnt.values())
    return {w: math.log(c / tot) for w, c in cnt.items() if c >= mincount and (len(w) >= 2 or w in ('a', 'i'))}, spec['norm']

def seg(s, LEX):
    """Viterbi word segmentation of a letter string; unknown stretches cost UNK per letter and come back as [..]"""
    n = len(s); best = [(0.0, [])] + [(-1e18, None)] * n
    for i in range(n):
        if best[i][1] is None: continue
        sc, path = best[i]
        for j in range(i + 1, min(n, i + 16) + 1):
            w = s[i:j]
            if w in LEX: c, tok = LEX[w], w
            else: c, tok = -UNK * (j - i) - 3, '[' + w + ']'
            if sc + c > best[j][0]: best[j] = (sc + c, path + [tok])
    return best[n][1] or []

def load(p, scheme):
    out = []
    for l in open(p, encoding='utf-8'):
        m = re.match(r'^\s*(L\d\d):\s*(.+)$', l)
        if not m or m.group(2).startswith('['): continue
        toks = []
        for t in m.group(2).split():
            if t == '###': toks.append(('w', 'et'))
            elif t.startswith('='): toks.append(('w', norm(t[1:].split('/')[0], scheme)))
            elif t.startswith('[') or t == '|': continue
            else:
                v = t.split('/')[0].replace('?', '').replace('y', 'i')
                toks.append(('l', v) if v and all(c in A for c in v) else ('?', ''))
        out.append(toks)
    return out

def read_flags(toks, LEX, tr=None):
    words = []                                       # (kind, n_letters, sign indices); kind True=lexical, False, 'ctx'
    i = 0
    while i < len(toks):
        k, v = toks[i]
        if k == 'w': words.append((v in LEX or v in ('a', 'i'), len(v), [i])); i += 1; continue
        if k == '?': words.append(('ctx', 0, [i])); i += 1; continue
        j = i
        while j < len(toks) and toks[j][0] == 'l': j += 1
        s = ''.join(toks[x][1] for x in range(i, j))
        owner = [x for x in range(i, j) for _ in toks[x][1]]     # letter -> its sign (a sign may give two letters)
        if tr: s = s.translate(tr)
        pos = 0
        for w in seg(s, LEX):
            n = len(w.strip('[]')); words.append((not w.startswith('['), n, sorted(set(owner[pos:pos + n])))); pos += n
        i = j
    read = [False] * len(toks); run = []
    def flush():
        lex = [w for w in run if w[0] is True]
        if len(lex) >= MINWORDS and sum(w[1] for w in lex) >= MINLETTERS:
            for w in lex:
                for x in w[2]: read[x] = True
    for w in words + [(False, 0, [])]:
        if w[0]: run.append(w)
        else: flush(); run = []
    return read

def measure(lines, LEX, tr=None):
    toks = [t for l in lines for t in l]
    f = read_flags(toks, LEX, tr)
    return sum(f), len(f)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('n', nargs='?', type=int, default=20)
    ap.add_argument('--model', default='fr-1600-letters'); ap.add_argument('--mincount', type=int, default=20)
    a = ap.parse_args()
    LEX, scheme = lexicon(a.model, a.mincount)
    lines = load(a.file, scheme)
    r, n = measure(lines, LEX); print(f'read {r}/{n} signs = {r/n:.1%}  (lexicon: {a.model}, mincount {a.mincount})')
    random.seed(2); sh = []
    for _ in range(a.n):
        p = list(A); random.shuffle(p); sh.append(measure(lines, LEX, str.maketrans(A, ''.join(p)))[0] / n)
    sh.sort(); print(f'{a.n} shuffled keys: median {sh[a.n//2]:.1%}, max {sh[-1]:.1%}')

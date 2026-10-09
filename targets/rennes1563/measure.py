"""Measure the share of cipher tokens read as sense, per letter and overall.

For each letter there is a token file (one cipher line per line, `tok` or `tok=a|b`, '-' = null) and an
aligned reading `aligned/<id>.txt` with the same number of non-comment lines. A reading line is a run of
words; `{n}` = n unread tokens; `~word` = probable (forced or context-filled, NOT counted as sense);
`+word` = clear text written in the cipher line (quoted tokens), not counted.
The script aligns every token to the reading using only the token's candidate values (glyphs.G, the
token's own `=a|b`, and the per-letter EXTRA values below, each justified in NOTES/the reading files).
A line that cannot be aligned is an error: the reading claims letters the signs do not give.
Each sense word is checked against a 16th-c. French vocabulary (fr-1520s-diplomatic + fr-henri4 corpora);
unknown words are listed so that a reader can judge them.

Sense = tokens attributed to non-probable words (nulls go with the word that follows them).
Usage: PYTHONUTF8=1 python measure.py [-v]
"""
import os, re, sys, unicodedata
from functools import lru_cache
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from glyphs import G

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('j', 'i').replace('v', 'u')

# per-letter value tables for bare tokens (the transcription files use different token names per hand)
P139 = dict(zx='s', Sr='-', gl='m|o', x4='x', blot='-|i', d='e', qq='que', hk='i', do='-', b='e|p', lt='vous', eq='-',
            sl='-', et='t', mJ='i|e', a1='n|i', x1='e', TT='pour', G='t', R='r', ss='o', z='a|p', S='a|-', La='d',
            mu='u', Lo='-|l', io='i', c='s|t', sh='y|et', f='ff', C='o', at='g', B='l', g='u|o', eta='a|n', sig='l',
            zs='s', lam='u', k='i', zy='-', pi='h', Rx='-', m='c|i', cg='g', Vb='qui', th='m', yn='-', s3='r',
            ll='ss', star='b', E='f|h|c', pl='bien', plus='y', md='ce', w='u', T='y', N='l', pour='-', que='-',
            est='-', en='-', bien='bien', RR='-', dar='-', tp='et', nn='nn')
P139.update({'9': 'n', '3': 'c', '4': 'f|x'})
P139.update(yn='d|-', cg='o|g', est='-|est', blot='-', en='-|en', d3='m', plus='y|vostre')  # 5 Oct pass: ÿ = d (Tomokiyo's script-v-dot); ç = o (chose)
LETTERS = [
    # id, token file, aligned reading, bare-token table (None = glyphs.G)
    ('f55', 'f55_v2.txt', 'aligned/f55.txt', None),
    ('p357', 'c390_p357.txt', 'aligned/p357.txt', None),
    ('p358', 'c390_p358.txt', 'aligned/p358.txt', None),
    ('c392', 'c392_p231n.txt', 'aligned/c392.txt', None),
    ('p139', 'c390_p139_v4.txt', 'aligned/p139.txt', P139),
]
# values added this pass, per letter: token -> extra candidates (see NOTES 'Push to 95%' for evidence)
EXTRA = {
    # p.357: values stated in c390_p357_reading.md (crossed t = b; small z/r = a; al2 = u; # = est; Rv = e;
    # hh = the doubled-cross et; pp = pour (⊥⊥); small y = n)
    # f.55: f55_v2_reading.md glossed-sibling pass: sc = le, bar (⊥) = pour, dag (‡) = con, gd = me, ss (ſſ) = o,
    # N = l, r5 = r (5 = r glossed in 'prendray')
    'f55': dict(sc=['le'], bar=['pour'], dag=['con'], gd=['me'], ss=['o'], N=['l'], r5=['r']),
    # c392: c392_p231_reading.md value table: z = p (as on p.138, escript), V = d (advis), δ = con/com
    'c392': dict(z=['p'], V=['d'], E=['ff'], z2=['a'], dl=['con'], **{'del': ['con']}),
    'p357': dict(tx=['b'], ry=['a'], al2=['u'], sh=['est', 'y'], Rv=['e'], hh=['et'], pp=['pour'], yy=['n'], pl2=['vostre']),
}

def cands(tok, table, extra):
    if tok.startswith('"'):
        return None
    if '=' in tok and not tok.startswith('='):
        name, v = tok.split('=', 1)
        vals = v.split('|')
    else:
        name = tok
        vals = (table.get(tok) if table and tok in table else G.get(tok, '?')).split('|')
    vals = vals + extra.get(name, [])
    return sorted({'' if x == '-' else norm(x) for x in vals if x != '?'}, key=len, reverse=True)

def parse_reading(line):
    units = []  # ('c', char, wid) | ('g', None, wid)
    words = []  # (text, status)
    for w in line.split():
        m = re.fullmatch(r'(~?)\{(\d+)\}(\S*)', w)
        if m:
            wid = len(words); words.append((m.group(3) or '{%s}' % m.group(2), 'prob' if m.group(1) else 'gap'))
            units += [('g', None, wid)] * int(m.group(2)); continue
        st = 'sense'
        if w[0] == '~': st, w = 'prob', w[1:]
        elif w[0] == '+': st, w = 'clear', w[1:]
        wid = len(words); words.append((w, st))
        for ch in norm(re.sub(r"[^\w]", '', w)):
            units.append(('c', ch, wid))
    return units, words

def align(toks, units):
    n, m = len(toks), len(units)
    sys.setrecursionlimit(10000)
    @lru_cache(None)
    def f(i, j):
        if i == n: return () if j == m else None
        t = toks[i]
        if t is None:  # clear token: must sit on a clear word; handled by reading '+word'
            return None
        if j < m and units[j][0] == 'g':
            r = f(i + 1, j + 1)
            if r is not None: return ((i, j, 1),) + r
        for v in t:
            if v == '':
                r = f(i + 1, j)
                if r is not None: return ((i, j, 0),) + r
                continue
            k = len(v)
            if j + k <= m and all(units[j + x][0] == 'c' and units[j + x][1] == v[x] for x in range(k)):
                r = f(i + 1, j + k)
                if r is not None: return ((i, j, k),) + r
        return None
    return f(0, 0)

def vocab():
    import collections
    V = collections.Counter()
    root = os.path.join(HERE, '..', '..', 'lang', 'corpora')
    for fn in ('fr-1520s-diplomatic.txt', 'fr-henri4.txt'):
        p = os.path.join(root, fn)
        if os.path.exists(p):
            V.update(re.findall(r'[a-z]+', norm(open(p, encoding='utf-8', errors='ignore').read())))
    return V

def main(verbose=False):
    V = vocab()
    tot = {'sense': 0, 'prob': 0, 'gap': 0, 'n': 0}
    unknown = set()
    for lid, tf, rf, table in LETTERS:
        tl = [l.split() for l in open(os.path.join(HERE, tf), encoding='utf-8') if l.strip() and not l.startswith('#')]
        rl = [l.rstrip('\n') for l in open(os.path.join(HERE, rf), encoding='utf-8') if l.strip() and not l.startswith('#')]
        assert len(tl) == len(rl), (lid, len(tl), len(rl))
        c = {'sense': 0, 'prob': 0, 'gap': 0, 'n': 0}
        for ln, (tk, rd) in enumerate(zip(tl, rl), 1):
            clear = [t for t in tk if t.startswith('"')]
            tk = [t for t in tk if not t.startswith('"')]
            units, words = parse_reading(' '.join(w for w in rd.split() if not w.startswith('+')))
            toks = tuple(tuple(cands(t, table, EXTRA.get(lid, {}))) for t in tk)
            path = align(toks, tuple(units))
            if path is None:
                print(f'!! {lid} l.{ln}: reading does not align with the signs'); print('   ', ' '.join(tk)); print('   ', rd)
                c['gap'] += len(tk); c['n'] += len(tk); continue
            for (i, j, k) in path:
                wid = units[j][2] if j < len(units) else (units[-1][2] if units else None)
                st = words[wid][1] if wid is not None else 'gap'
                c[{'sense': 'sense', 'prob': 'prob', 'gap': 'gap'}.get(st, 'sense')] += 1
                c['n'] += 1
            for w, st in words:
                if st == 'sense':
                    if "|" in w: continue
                    for part in re.split(r"[’'\-]", w):
                        p = norm(re.sub(r'[^\w]', '', part))
                        if len(p) > 1 and V and V[p] < 1: unknown.add(p)
            if verbose:
                print(f'{lid} l.{ln}: ' + rd)
        print(f"{lid:5s} tokens {c['n']:4d}  sense {c['sense']/c['n']:.3f}  probable {c['prob']/c['n']:.3f}  unread {c['gap']/c['n']:.3f}")
        for k in tot: tot[k] += c[k]
    print(f"ALL   tokens {tot['n']:4d}  sense {tot['sense']/tot['n']:.3f}  probable {tot['prob']/tot['n']:.3f}  unread {tot['gap']/tot['n']:.3f}")
    if unknown: print('sense words not in the 16th-c. vocabulary:', ' '.join(sorted(unknown)))

if __name__ == '__main__':
    main('-v' in sys.argv)

"""Statistics of the note and the test of the Durham key table (SAD.250/1/81) against it.

    python analysis.py [--null N]

Reads transcription.txt (the note) and table_key.tsv (the table's two Arabic-letter number columns N1 and N2,
confidence H/M/L per reading; sin not read). The Arabic letter frequencies come from lang/corpora/ar-wikipedia-sample.txt
(fetch it with `python -m lang.corpora ar-wikipedia-sample`; unigram frequencies of the 28 letters only).

It does not decrypt anything. For each column, as read and with each group's digits reversed, it maps the note's groups
to letters through the column and asks whether the result looks like Arabic more than a random assignment of the
same letters to the same values does.
"""
import math, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LETTERS = 'ابتثجحخدذرزسشصضطظعغفقكلمنهوي'
FOLD = {'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ة': 'ه', 'ى': 'ي', 'ؤ': 'و', 'ئ': 'ي'}


def groups():
    out = []
    for ln in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        if not ln.startswith('#'):
            out += ln.split()
    return out


def arabic_freq():
    p = os.path.join(ROOT, 'lang', 'corpora', 'ar-wikipedia-sample.txt')
    t = open(p, encoding='utf-8').read()
    t = ''.join(FOLD.get(c, c) for c in t)
    c = Counter(ch for ch in t if ch in LETTERS)
    n = sum(c.values())
    return {l: c[l] / n for l in LETTERS}, n


def key():
    rows = [ln.rstrip('\n').split('\t') for ln in open(os.path.join(HERE, 'table_key.tsv'), encoding='utf-8')][1:]
    return {r[1]: dict(n1=(r[2], r[3]) if r[2] else None, n2=(r[4], r[5]) if len(r) > 4 and r[4] else None) for r in rows}


def score(g, mapping, lp):
    """Mean log-probability per mapped group, and the share of groups that map."""
    tot = 0.0; k = 0
    for v in g:
        if v in mapping:
            ls = mapping[v]
            tot += sum(lp[l] for l in ls) / len(ls); k += 1
    return (tot / k if k else float('-inf')), k / len(g)


def main():
    nnull = 2000
    if '--null' in sys.argv: nnull = int(sys.argv[sys.argv.index('--null') + 1])
    g = groups(); n = len(g); c = Counter(g)
    ic = sum(v * (v - 1) for v in c.values()) / (n * (n - 1))
    print(f'note: {n} groups, {len(c)} distinct, IC {ic:.4f} (uniform over 28: {1 / 28:.4f})')
    print('first digit :', sorted(Counter(x[0] for x in g).items()))
    print('second digit:', sorted(Counter(x[1] for x in g).items()))
    # digit-pattern test: the note's groups sit in a grid (first digit F, second digit S); a table that encoded the
    # note should sit in the same grid, and random two-digit numbers over the digits 1-9 would not.
    F = set('1235678'); S = set('245789')
    inside = lambda v: v[0] in F and v[1] in S
    print(f'\ndigit grid (first in {sorted(F)}, second in {sorted(S)}): note {sum(inside(v) for v in g) / n:.0%} of groups; '
          f'random two-digit values over 1-9: {len(F) * len(S) / 81:.0%}')
    Kt = key()
    for col in ('n1', 'n2'):
        vals = [d[col][0] for d in Kt.values() if d[col]]
        print(f'   table {col.upper()} (as read): {sum(inside(v) for v in vals)} of {len(vals)} values inside the grid '
              f'({sum(inside(v) for v in vals) / len(vals):.0%}); first digits {sorted(Counter(v[0] for v in vals).items())}; '
              f'second digits {sorted(Counter(v[1] for v in vals).items())}')
    f, nc = arabic_freq()
    lp = {l: math.log(f[l]) for l in LETTERS}
    top = sorted(f.items(), key=lambda kv: -kv[1])[:6]
    print(f'\nArabic letter frequencies ({nc} letters of the corpus): ' + ', '.join(f'{l} {p:.3f}' for l, p in top))
    rng = random.Random(1)
    K = key()
    CONF = str.maketrans('46', '32')       # glyph pairs easily confused: 4 for 3, 6 for 2
    for col, rev, eq in [(c_, r_, e_) for c_ in ('n1', 'n2') for e_ in (False, True) for r_ in (False, True)]:
        if True:
            def canon(v):
                return v.translate(CONF) if eq else v
            gg = [canon(v) for v in g]; cc = Counter(gg)
            m = {}
            for l, d in K.items():
                if d[col]:
                    v = d[col][0][::-1] if rev else d[col][0]
                    m.setdefault(canon(v), []).append(l)
            obs, cov = score(gg, m, lp)
            letters = [l for ls in m.values() for l in ls]
            vals = list(m)
            ge = 0
            for _ in range(nnull):
                rng.shuffle(letters)
                it = iter(letters)
                mm = {v: [next(it) for _ in m[v]] for v in vals}
                s, _c = score(g, mm, lp)
                if s >= obs: ge += 1
            topv = cc.most_common(1)[0][0]
            alif = K['ا'][col][0][::-1] if (K['ا'][col] and rev) else (K['ا'][col][0] if K['ا'][col] else None)
            alif = canon(alif) if alif else None
            print(f'\n{col.upper()} {"digits reversed" if rev else "as read"}{", 3=4 and 2=6" if eq else ""}: {len(m)} values read, '
                  f'{cov:.0%} of the note\'s groups map; mean log p per mapped group {obs:.3f}; '
                  f'random reassignment of the same letters does as well or better in {ge / nnull:.1%} of {nnull} draws')
            print(f'   commonest group {topv} (x{c[topv]}) ->', m.get(topv, 'not among the values read'),
                  f'| alif = {alif}, occurrences in the note: {cc[alif] if alif else "-"}')
    print('\nA key that read the note would map most groups and score clearly above its random reassignments '
          '(small fraction above); alif and lam would be among the commonest groups.')


if __name__ == '__main__':
    main()

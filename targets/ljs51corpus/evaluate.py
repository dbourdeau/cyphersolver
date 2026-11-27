"""Evaluate segment.py against the by-eye counts of the chain records (eval_set.json, built by build_evalset.py).

    python evaluate.py                       # tuning and test set, summary per tier
    python evaluate.py --split test -v       # held-out set only, per chain and per line
    python evaluate.py --seg segment_v1      # score another segmenter module (the old one is segment_v1.py)
    python evaluate.py --ref                 # the old reference pages (tashifi counts, ff. 14v-16v, 9r, 63v, 73v)

Scores:
  per line   (chains with by-eye per-line counts): share of lines exact and within one sign; a line the segmenter
             classes as Arabic counts 0 signs.  Divider counts per line only where a block has no dividers.
  per chain  sum over the chain's lines of signs found vs the chain's by-eye total: total error % =
             sum |found - expected| / sum expected; the same for dividers, and the share of chains whose divider
             count is within 10 % (at least +-1) of the by-eye count ('divider accuracy').
Tiers (see build_evalset.py): eye = by eye on the master; checked = overlay-checked segmenter counts (+-2..6 per
chain); segmenter = old segmenter counts (agreement only, not truth); rough = +-8, totals only.  Headline = eye+checked.
"""
import sys, os, json, importlib
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def _run(args):
    mod, n, ov = args
    S = importlib.import_module(mod)
    if ov:
        S.P.update(ov)
    try:
        lines = S.segment_page(n)
    except Exception as e:
        import traceback
        print('image %d FAILED: %s' % (n, traceback.format_exc()))
        return n, None
    out = {}
    for L in lines:
        its = L.get('items', [])
        out[L['index']] = dict(kind=L['kind'], signs=sum(1 for it in its if it['kind'] == 'sign'),
                               dividers=sum(1 for it in its if it['kind'] == 'divider'))
    return n, out


def run_pages(mod, images, procs=8, ov=None):
    with Pool(procs) as pool:
        return dict(pool.map(_run, [(mod, n, ov) for n in sorted(images)]))


def found_at(pages, im, li):
    L = (pages.get(im) or {}).get(li)
    if not L or L['kind'] != 'cipher':
        return 0, 0, L['kind'] if L else 'none'
    return L['signs'], L['dividers'], 'cipher'


def score(chains, pages, verbose=False):
    R = dict(nl=0, exact=0, within1=0, lerr=0, lexp=0, ndl=0, dexact=0,
             nc=0, cerr=0, cexp=0, ndc=0, derr=0, dexp=0, dok=0)
    for c in chains:
        fs = fd = 0
        rows = []
        if c['tier'] == 'rough':     # rough estimates (ff. 1r, 1v): a fresh line finding can renumber a pale page, so
            for im in sorted({im for im, li in c['slots']}):    # the whole page's cipher lines are counted
                for li, L in (pages.get(im) or {}).items():
                    if L['kind'] == 'cipher':
                        fs += L['signs']; fd += L['dividers']
        for im, li in ([] if c['tier'] == 'rough' else c['slots']):
            s, d, k = found_at(pages, im, li)
            fs += s; fd += d
            rows.append((im, li, s, d, k))
        if c['lines']:
            for L, (im, li, s, d, k) in zip(c['lines'], rows):
                e = L['signs']
                R['nl'] += 1; R['exact'] += s == e; R['within1'] += abs(s - e) <= 1
                R['lerr'] += abs(s - e); R['lexp'] += e
                if L['dividers'] is not None:
                    R['ndl'] += 1; R['dexact'] += d == L['dividers']
        if isinstance(c['signs_total'], int):
            R['nc'] += 1; R['cerr'] += abs(fs - c['signs_total']); R['cexp'] += c['signs_total']
        if isinstance(c['dividers_total'], int):
            e = c['dividers_total']
            R['ndc'] += 1; R['derr'] += abs(fd - e); R['dexp'] += e
            R['dok'] += abs(fd - e) <= max(1, 0.1 * e)
        if verbose:
            print('%-8s %-5s %-9s signs %4d / %-4s div %3d / %-4s' % (c['chain_id'], c['split'], c['tier'], fs,
                  c['signs_total'], fd, c['dividers_total']))
            if c['lines']:
                print('   ' + ' '.join('%d:%d%s%+d' % (im, li, '' if k == 'cipher' else 'A', s - L['signs'])
                                       for L, (im, li, s, d, k) in zip(c['lines'], rows)))
    return R


def fmt(R):
    p = lambda a, b: 100.0 * a / b if b else float('nan')
    return ('lines %3d  within1 %5.1f%%  exact %5.1f%%  line err %5.1f%% | chains %2d  total err %5.1f%% | '
            'div: chain err %5.1f%%  acc %5.1f%% (%d)%s' % (
                R['nl'], p(R['within1'], R['nl']), p(R['exact'], R['nl']), p(R['lerr'], R['lexp']),
                R['nc'], p(R['cerr'], R['cexp']), p(R['derr'], R['dexp']), p(R['dok'], R['ndc']), R['ndc'],
                ('  line-div exact %d/%d' % (R['dexact'], R['ndl'])) if R['ndl'] else ''))


def evaluate(mod='segment', split=None, verbose=False, procs=8, ov=None):
    es = json.load(open(os.path.join(HERE, 'eval_set.json'), encoding='utf8'))['chains']
    if split:
        es = [c for c in es if c['split'] == split]
    images = {im for c in es for im, li in c['slots']}
    pages = run_pages(mod, images, procs, ov)
    res = {}
    for sp in ('tune', 'test'):
        for tiers, name in ((('eye', 'checked'), 'eye+checked'), (('eye',), 'eye'), (('checked',), 'checked'),
                            (('segmenter',), 'segmenter'), (('rough',), 'rough')):
            cs = [c for c in es if c['split'] == sp and c['tier'] in tiers]
            if not cs:
                continue
            if verbose and name not in ('eye+checked',):
                print('\n---- %s / %s' % (sp, name))
            R = score(cs, pages, verbose and name != 'eye+checked')
            res[(sp, name)] = R
    # lines classed cipher on the scored pages that belong to no chain (headings, verse, compiler's lines; a few may be
    # cipher rows the records do not cover, e.g. red-gloss figure rows)
    allc = json.load(open(os.path.join(HERE, 'eval_set.json'), encoding='utf8'))['chains']
    inchain = {(im, li) for c in allc for im, li in c['slots']}
    for sp in ('tune', 'test'):
        ims = {im for c in es if c['split'] == sp for im, li in c['slots']}
        xl = [(im, li, L['signs']) for im in sorted(ims) for li, L in (pages.get(im) or {}).items()
              if L['kind'] == 'cipher' and (im, li) not in inchain]
        res[(sp, 'extra')] = dict(lines=len(xl), signs=sum(x[2] for x in xl))
    print('\nsegmenter module: %s%s' % (mod, ('  overrides %s' % ov) if ov else ''))
    for (sp, name), R in res.items():
        if name == 'extra':
            print('%-4s cipher lines outside every chain on these pages: %d (%d signs)' % (sp, R['lines'], R['signs']))
        else:
            print('%-4s %-11s %s' % (sp, name, fmt(R)))
    return res


# ---- the old reference pages -------------------------------------------------------------------------------------
REF = {
    33: [14, 14, 17, 17, 13, 14, 16], 34: [16, 14, 15, 16, 15, 16, 13, 15, 15, 14, 11, 13, 18],
    35: [17, 15, 16, 12, 15, 14, 15, 15, 14, 13, 13, 16, 15, 15], 36: [16, 13, 14, 15, 17, 14, 13, 16, 15, 15, 14, 12, 16],
    37: [14, 15, 16, 14, 15, 1], 131: [15, 14, 15, 14, 15, 6, None, None, None, None, None, None],
    22: [None, 14, 14, 13, 15, 15, 9], 151: [15, 14, 16, 15, 10],
}


def evaluate_ref(mod='segment'):
    """The tashifi reference counts (from an earlier automatic count checked by eye, +-1): cipher lines of the page in
    order, aligned to the found cipher lines (a missing or extra line costs 25)."""
    S = importlib.import_module(mod)
    nl = nok = nexact = err = tot = 0
    for n, exp in sorted(REF.items()):
        cl = [L for L in S.segment_page(n) if L['kind'] == 'cipher']
        found = [sum(1 for it in L['items'] if it['kind'] == 'sign') for L in cl]
        for fi, ei in align(found, exp):
            if ei is None or exp[ei] is None:
                continue
            e = exp[ei]; f = found[fi] if fi is not None else 0
            nl += 1; nok += abs(f - e) <= 1; nexact += f == e; err += abs(f - e); tot += e
    print('reference pages: lines %d  within1 %.0f%%  exact %.0f%%  error %.1f%%' % (nl, 100 * nok / nl, 100 * nexact / nl,
                                                                                     100 * err / tot))


def align(found, exp):
    n, m = len(found), len(exp)
    INF = 1e9
    D = [[INF] * (m + 1) for _ in range(n + 1)]
    B = [[None] * (m + 1) for _ in range(n + 1)]
    D[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i][j] >= INF:
                continue
            if i < n and j < m:
                e = exp[j]
                c = 0 if e is None else abs(found[i] - e)
                if D[i][j] + c < D[i + 1][j + 1]:
                    D[i + 1][j + 1] = D[i][j] + c; B[i + 1][j + 1] = (i, j)
            if i < n and D[i][j] + 25 < D[i + 1][j]:
                D[i + 1][j] = D[i][j] + 25; B[i + 1][j] = (i, j)
            if j < m and D[i][j] + 25 < D[i][j + 1]:
                D[i][j + 1] = D[i][j] + 25; B[i][j + 1] = (i, j)
    pairs = []
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj = B[i][j]
        pairs.append((pi if pi != i else None, pj if pj != j else None))
        i, j = pi, pj
    return pairs[::-1]


if __name__ == '__main__':
    a = sys.argv[1:]
    mod = a[a.index('--seg') + 1] if '--seg' in a else 'segment'
    split = a[a.index('--split') + 1] if '--split' in a else None
    if '--ref' in a:
        evaluate_ref(mod)
    else:
        ov = {}
        if '--set' in a:
            for kv in a[a.index('--set') + 1].split(','):
                k, v = kv.split('=')
                ov[k] = float(v) if '.' in v else int(v)
        evaluate(mod, split, '-v' in a, ov=ov)

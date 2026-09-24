"""Eight hypotheses: stress tests of the coronal rule from new angles, and three probes of words and archives.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the eight.

H1  The coronal rule survives dropping whichever single coronal e/o sign supports it most.
H2  The rule holds in word types attested only once (hapax), not only in frequent words.
H3  The rule holds in word-initial syllables.
H4  With consonants as the unit, coronal consonants have higher e/o shares than non-coronals (rank test).
H5  Reduplicated Linear A words (a sign repeated in succession) are entry labels more often than other words.
H6  Reduplicated Knossos personal names are more Minoan-shaped (stem-scored) than other Knossos names.
H7  Tablets of the same commodity share vocabulary more than tablets of different commodities (sides merged,
    transaction terms removed).
H8  Single signs on sealings match the first sign of a word attested at the same site more often than chance.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher11g as G  # noqa: E402

F, X, T, B, D, Db, V = G.F, G.X, G.T, G.B, G.D, G.Db, G.V
ROOT = B.ROOT
rng = G.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
RARE, COR, NONCOR = X.RARE, X.COR, X.NONCOR
f_or = lambda ws: X.log_or_v(ws, RARE)


def H1():
    signs = sorted({x for w in LA for x in w if grid(x) and grid(x)[0] in COR and grid(x)[1] in RARE})
    drops = {s: f_or([w for w in LA if s not in w]) for s in signs}
    worst = min(drops, key=drops.get)
    kept = [w for w in LA if worst not in w]
    real, p, nm = X.compare(kept, LB, f_or)
    record('H1 leave one sign out', 'The coronal rule survives dropping its most influential sign',
           {'dropped': worst.upper(), 'logOR_without': round(drops[worst], 3), 'logOR_LB': round(f_or(LB), 3), 'p': round(p, 4)},
           {'logOR after dropping each sign': {s.upper(): round(v, 3) for s, v in sorted(drops.items(), key=lambda kv: kv[1])}})
    return p


def H2():
    toks = Counter(w for _, _, w in B.words_of())
    hapax = [w for w in LA if toks.get(w, 0) == 1]
    real, p, nm = X.compare(hapax, LB, f_or)
    record('H2 hapax words', 'The coronal rule holds in words attested once',
           {'logOR_hapax': round(f_or(hapax), 3), 'logOR_LB': round(f_or(LB), 3), 'p': round(p, 4), 'words': len(hapax)}, {})
    return p


def H3():
    first = [w[:1] for w in LA]
    lb_first = [w[:1] for w in LB]
    real, p, nm = X.compare(first, lb_first, f_or)
    record('H3 initial syllables', 'The coronal rule holds in word-initial syllables',
           {'logOR_LA_initial': round(f_or(first), 3), 'logOR_LB_initial': round(f_or(lb_first), 3), 'p': round(p, 4)}, {})
    return p


def H4():
    share = T.eo_by_cons(LA)
    cs = [c for c in share if c in COR | NONCOR]
    vals = [share[c] for c in cs]
    is_cor = [c in COR for c in cs]
    stat = lambda flags: V.auc([v for v, f in zip(vals, flags) if f], [v for v, f in zip(vals, flags) if not f])
    real, p, nm = X.shuffle_test(stat, is_cor, reps=20000)
    lb = T.eo_by_cons(LB)
    lcs = [c for c in lb if c in COR | NONCOR]
    lb_auc = V.auc([lb[c] for c in lcs if c in COR], [lb[c] for c in lcs if c in NONCOR])
    record('H4 consonants as the unit', 'Coronal consonants rank above non-coronals in e/o share',
           {'auc': round(real, 3), 'p': round(p, 4), 'consonants': {c: round(share[c], 3) for c in sorted(cs, key=lambda c: -share[c])}},
           {'Linear B auc': round(lb_auc, 3)})
    return p


redup = lambda w: any(w[i] == w[i + 1] for i in range(len(w) - 1))


def H5():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    words = sorted(fn)
    ent = {w: fn[w].most_common(1)[0][0] == 'entry label' for w in words}
    flags = [redup(w) for w in words]

    def stat(fl):
        a = [ent[w] for w, f in zip(words, fl) if f]
        b = [ent[w] for w, f in zip(words, fl) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, flags)
    record('H5 reduplicated words are names', 'Reduplicated Linear A words are entry labels more often',
           {'redup_entry': f"{sum(ent[w] for w, f in zip(words, flags) if f)}/{sum(flags)}",
            'other_entry': f"{sum(ent[w] for w, f in zip(words, flags) if not f)}/{len(words) - sum(flags)}", 'p': round(p, 4)},
           {'reduplicated words': sorted('-'.join(w).upper() for w, f in zip(words, flags) if f)})
    return p


def H6():
    a = [w for w in T.KN_N if redup(w)]
    b = [w for w in T.KN_N if not redup(w)]
    real, p, nm = T.label_perm(lambda x, y: V.auc([X.stem_score(w) for w in x], [X.stem_score(w) for w in y]), a, b)
    record('H6 reduplicated Knossos names', 'Reduplicated Knossos names are more Minoan-shaped (stem-scored)',
           {'auc': round(real, 3), 'p': round(p, 4), 'n': [len(a), len(b)]}, {'examples': sorted('-'.join(w) for w in a)[:15]})
    return p


def H7():
    tabs = [(k, t) for k, t in X.TABS.items() if len(t['com']) == 1 and len(t['words'] - X.TERMS) >= 2]
    names = [k for k, _ in tabs]
    words = {k: t['words'] - X.TERMS for k, t in tabs}
    jac = {}
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            jac[(a, b)] = len(words[a] & words[b]) / len(words[a] | words[b])

    def stat(labs):
        cm = dict(zip(names, labs))
        same = [v for (a, b), v in jac.items() if cm[a] == cm[b]]
        diff = [v for (a, b), v in jac.items() if cm[a] != cm[b]]
        return sum(same) / len(same) - sum(diff) / len(diff)
    real, p, nm = X.shuffle_test(stat, [next(iter(t['com'])) for _, t in tabs])
    record('H7 commodity vocabularies', 'Single-commodity tablets of the same commodity share vocabulary',
           {'jaccard_diff': round(real, 4), 'p': round(p, 4), 'tablets': len(names)}, {})
    return p


def H8():
    initials = defaultdict(set)
    for r, t, w in B.words_of():
        initials[r['site']].add(w[0])
    seal = []
    for r in B.READ['records']:
        if r['support'] in B.SEAL:
            for t in r['tokens']:
                if t['cls'] == 'single-sign' and re.fullmatch(r'[A-Z]{1,2}[0-9]?', t['label']):
                    seal.append((t['label'].lower(), r['site']))
    sites = [s for _, s in seal]
    stat = lambda st: sum(sig in initials.get(s, set()) for (sig, _), s in zip(seal, st)) / len(seal)
    real, p, nm = X.shuffle_test(stat, sites)
    record('H8 sealing signs are local initials', 'Sealing signs match word initials from their own site more than chance',
           {'share': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'sealing_signs': len(seal)},
           {'sites': dict(Counter(sites))})
    return p


TESTS = [H1, H2, H3, H4, H5, H6, H7, H8]


def main():
    ps = {}
    for fn in TESTS:
        try:
            ps[fn.__name__] = fn()
        except Exception as ex:
            import traceback
            traceback.print_exc()
            out[fn.__name__] = {'error': str(ex)}
    tested = sorted([(p, k) for k, p in ps.items() if p is not None])
    m, cut = len(tested), 0
    for i, (p, k) in enumerate(tested, 1):
        if p <= 0.05 * i / m:
            cut = i
    supported = [k for _, k in tested[:cut]]
    res = {'method': __doc__.strip(), 'primary_p': ps, 'bh_supported': supported, 'details': out}
    (ROOT / 'reading/decipher8h_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()

"""Four hypotheses that use the R/T vowel rule (e/o after R and T; decipher8h, decipher6j) as a tool to find place
names and names, and one replication.

Collapse: in every word, a syllable with consonant r or t and vowel e or o is rewritten with i or u (re -> ri,
to -> tu). If Minoan e/o after R/T were variants of i/u, some Minoan words should match only after the collapse.
The Keftiu names of BM 5647 were considered and set aside: seven names are too few to test, and a recent study
reads them as Hellenized Cretan names (JAEI 2025).

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the four.

N1  Under the collapse, Linear A words match Knossos-only place names and ethnics more often than Pylos-only ones
    (per Linear B word), beyond the exact matches.
N2  The R/T collapse gains more Linear A - Knossos personal-name matches than the same collapse applied to other
    consonants (p m w k q j). Control: Pylos names.
N3  On SigLA's transcription, i~e and u~o alternations fall after dentals more than other vowel alternations do.
N5  Linear A heading words match Knossos-only place names (exactly or under the collapse) more often than entry
    labels do.
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher6m as M  # noqa: E402

L6, K, X, T, B, D, V, F = M.L6, M.K, M.X, M.T, M.B, M.D, M.V, M.L6.K.J.I.H.G.F
G = M.L6.K.J.I.H.G
ROOT = B.ROOT
rng = M.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
RT = set('rt')
NONRT = set('pmwkqj')


def collapse(w, cons):
    return tuple((grid(x)[0] + {'e': 'i', 'o': 'u'}[grid(x)[1]]) if grid(x) and grid(x)[0] in cons and grid(x)[1] in 'eo' else x for x in w)


def new_matches(la, lb, cons):
    lbs = set(lb)
    lbc = defaultdict(set)
    for w in lb:
        lbc[collapse(w, cons)].add(w)
    return {w: sorted(lbc[collapse(w, cons)]) for w in la if w not in lbs and collapse(w, cons) in lbc}


def topo(site_only):
    return [w for w in site_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 2]


KN_T, PY_T = topo(V.kn_only), topo(V.py_only)


def N1():
    la = [w for w in LA if len(w) >= 2]
    rate = lambda lbw: len({x for v in new_matches(la, lbw, RT).values() for x in v}) / max(1, len(lbw))
    real, p, nm = T.label_perm(lambda a, b: rate(a) - rate(b), KN_T, PY_T, reps=REPS)
    record('N1 place names under the collapse', 'Under the R/T collapse Linear A words match Knossos place names more than Pylos ones',
           {'KN_rate': round(rate(KN_T), 4), 'PY_rate': round(rate(PY_T), 4), 'p': round(p, 4), 'n': [len(KN_T), len(PY_T)]},
           {'new Knossos place-name matches': {'-'.join(w).upper(): ['-'.join(x) for x in v] for w, v in new_matches(la, KN_T, RT).items()},
            'new Pylos place-name matches': {'-'.join(w).upper(): ['-'.join(x) for x in v] for w, v in new_matches(la, PY_T, RT).items()}})
    return p


def N2():
    la = [w for w in LA if len(w) >= 2]
    g = lambda names, cons: len(new_matches(la, names, cons))
    real = g(T.KN_N, RT) - g(T.KN_N, NONRT)
    boot = []
    for _ in range(REPS):
        smp = [rng.choice(la) for _ in la]
        boot.append(len(new_matches(smp, T.KN_N, RT)) - len(new_matches(smp, T.KN_N, NONRT)))
    p = (sum(b <= 0 for b in boot) + 1) / (len(boot) + 1)
    record('N2 name matches under the R/T collapse', 'The R/T collapse gains more Knossos name matches than a collapse after other consonants',
           {'gain_RT': g(T.KN_N, RT), 'gain_other': g(T.KN_N, NONRT), 'bootstrap p': round(p, 4)},
           {'new Knossos matches (R/T)': {'-'.join(w).upper(): ['-'.join(x) for x in v] for w, v in new_matches(la, T.KN_N, RT).items()},
            'Pylos control': {'RT': g(T.PY_N, RT), 'other': g(T.PY_N, NONRT)}})
    return p


def N3():
    alts = F.vowel_alternations(G.SIG)
    target = lambda v: v in (frozenset('ie'), frozenset('uo'))
    is_t = [target(v) for _, v in alts]
    dent = [c in F.DENT for c, _ in alts]

    def stat(flags):
        a = [d for d, f in zip(dent, flags) if f]
        b = [d for d, f in zip(dent, flags) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, is_t, reps=REPS)
    record('N3 dental alternations in SigLA', 'On SigLA, i~e and u~o alternations fall after dentals more than other vowel alternations',
           {'dental_share_ie_uo': round(sum(d for d, f in zip(dent, is_t) if f) / max(1, sum(is_t)), 3),
            'dental_share_other': round(sum(d for d, f in zip(dent, is_t) if not f) / max(1, len(is_t) - sum(is_t)), 3),
            'p': round(p, 4), 'alternations': [sum(is_t), len(is_t) - sum(is_t)]},
           {'lineara.xyz (round 20, F1)': '19/21 vs 66%, p 0.022'})
    return p


def N5():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    head = [w for w, c in fn.items() if c.most_common(1)[0][0] == 'heading']
    ent = [w for w, c in fn.items() if c.most_common(1)[0][0] == 'entry label']
    kt = set(KN_T)
    ktc = {collapse(w, RT) for w in KN_T}
    hit = lambda w: w in kt or collapse(w, RT) in ktc
    real, p, nm = T.label_perm(lambda a, b: sum(map(hit, a)) / len(a) - sum(map(hit, b)) / len(b), head, ent, reps=REPS)
    record('N5 headings as place names', 'Linear A headings match Knossos place names more often than entry labels do',
           {'headings': f'{sum(map(hit, head))}/{len(head)}', 'entries': f'{sum(map(hit, ent))}/{len(ent)}', 'p': round(p, 4)},
           {'heading matches': sorted('-'.join(w).upper() for w in head if hit(w)), 'entry matches': sorted('-'.join(w).upper() for w in ent if hit(w))})
    return p


TESTS = [N1, N2, N3, N5]


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
    (ROOT / 'reading/decipher4n_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()

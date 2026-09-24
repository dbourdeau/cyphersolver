"""Six hypotheses following decipher7k.py: Khania's vowel spelling, values for the local signs, and whether the
R/T vowel rule is language or scribal habit.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the six.

L1  Khania uses e/o after R and T more than Haghia Triada does.
L2  Khania uses e/o more than Haghia Triada overall.
L3  Khania's Linear A is closer to Linear B in syllable use than Haghia Triada's is.
L4  Words with a local (single-site) unread sign have a twin elsewhere in Linear A, identical except for a known
    syllable in that slot, more often than words with widespread unread signs.
L7  Words with e/o after consonants other than R and T are attested outside Haghia Triada more often than other words.
L10 Haghia Triada scribes differ in how often they write e/o after R and T (if they do not, the rule is language).
"""
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher7k as K  # noqa: E402

J, I, X, T, B, D, V = K.J, K.I, K.X, K.T, K.B, K.D, K.V
ROOT = B.ROOT
rng = K.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
RARE = X.RARE
RT = set('rt')
KH = D.site_words(lambda s: s == 'Khania')
HT = D.site_words(lambda s: s == 'Haghia Triada')


def rt_eo(ws):
    s = [grid(x)[1] in RARE for w in ws for x in w if grid(x) and grid(x)[0] in RT]
    return sum(s) / max(1, len(s))


def eo_all(ws):
    s = [grid(x)[1] in RARE for w in ws for x in w if grid(x)]
    return sum(s) / max(1, len(s))


def L1():
    real, p, nm = T.label_perm(lambda a, b: rt_eo(a) - rt_eo(b), KH, HT, reps=REPS)
    record('L1 Khania e/o after R/T', 'Khania uses e/o after R and T more than Haghia Triada',
           {'KH': round(rt_eo(KH), 3), 'HT': round(rt_eo(HT), 3), 'p': round(p, 4), 'words': [len(KH), len(HT)]}, {})
    return p


def L2():
    real, p, nm = T.label_perm(lambda a, b: eo_all(a) - eo_all(b), KH, HT, reps=REPS)
    record('L2 Khania e/o overall', 'Khania uses e/o more than Haghia Triada overall',
           {'KH': round(eo_all(KH), 3), 'HT': round(eo_all(HT), 3), 'p': round(p, 4)}, {})
    return p


def L3():
    stat = lambda kh, ht: I.jsd_prof(ht, LB) - I.jsd_prof(kh, LB)
    real, p, nm = T.label_perm(stat, KH, HT, reps=REPS)
    record('L3 Khania closer to Linear B', 'Khania Linear A is closer to Linear B in syllable use than Haghia Triada',
           {'jsd_KH_LB': round(I.jsd_prof(KH, LB), 4), 'jsd_HT_LB': round(I.jsd_prof(HT, LB), 4), 'p': round(p, 4)}, {})
    return p


def L4():
    known = defaultdict(list)
    for w in D.LA:
        for i in range(len(w)):
            if grid(w[i]) or re.fullmatch(r'[a-z]+[0-9]', w[i] or ''):
                known[(len(w), i, w[:i] + w[i + 1:])].append(w[i])
    items = []
    for w in D.LA:
        ur = [i for i, x in enumerate(w) if D.UNREAD.match(x)]
        if len(ur) == 1:
            i = ur[0]
            twins = known.get((len(w), i, w[:i] + w[i + 1:]), [])
            items.append((w, w[i], w[i].upper() in K.LOCAL or w[i] in K.LOCAL, sorted(set(twins))))
    flags = [loc for _, _, loc, _ in items]
    has = [bool(t) for *_, t in items]

    def stat(fl):
        a = [h for h, f in zip(has, fl) if f]
        b = [h for h, f in zip(has, fl) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, flags, reps=REPS)
    twins = [f"{'-'.join(w).upper()} ~ {', '.join(t_.upper() for t_ in tw)}" for w, x, loc, tw in items if tw]
    record('L4 twins for local signs', 'Words with a local unread sign have a twin with a known sign more often',
           {'local_with_twin': f"{sum(h for h, f in zip(has, flags) if f)}/{sum(flags)}",
            'widespread_with_twin': f"{sum(h for h, f in zip(has, flags) if not f)}/{len(flags) - sum(flags)}", 'p': round(p, 4)},
           {'all twins (word ~ known signs in that slot)': twins})
    return p


def L7():
    sites = defaultdict(set)
    for r, t, w in B.words_of():
        sites[w].add(r['site'])
    words = [w for w in sites if all(grid(x) for x in w)]
    other_eo = {w: any(grid(x)[0] and grid(x)[0] not in RT and grid(x)[1] in RARE for x in w) for w in words}
    outside = {w: bool(sites[w] - {'Haghia Triada'}) for w in words}
    flags = [other_eo[w] for w in words]

    def stat(fl):
        a = [outside[w] for w, f in zip(words, fl) if f]
        b = [outside[w] for w, f in zip(words, fl) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, flags, reps=REPS)
    record('L7 non-R/T e/o words are regional', 'Words with e/o after other consonants are attested outside HT more often',
           {'with': f"{sum(outside[w] for w, f in zip(words, flags) if f)}/{sum(flags)}",
            'without': f"{sum(outside[w] for w, f in zip(words, flags) if not f)}/{len(flags) - sum(flags)}", 'p': round(p, 4)}, {})
    return p


def L10():
    rows = []
    for r, t, w in B.words_of():
        if r['site'] != 'Haghia Triada':
            continue
        s = X.SCRIBE_W.get(X.whole(r['name']))
        if not s:
            continue
        for x in w:
            if grid(x) and grid(x)[0] in RT:
                rows.append((s, grid(x)[1] in RARE))
    by = Counter(s for s, _ in rows)
    rows = [r for r in rows if by[r[0]] >= 15]
    names = [s for s, _ in rows]
    real, p, nm = X.shuffle_test(lambda fl: X.chi2(list(zip(names, fl))), [f for _, f in rows], reps=REPS)
    record('L10 scribes and the R/T rule', 'Haghia Triada scribes differ in how often they write e/o after R/T',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'syllables': len(rows)},
           {'e/o share after R/T by scribe': {s: round(sum(f for s2, f in rows if s2 == s) / n, 2) for s, n in Counter(names).items()}})
    return p


TESTS = [L1, L2, L3, L4, L7, L10]


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
    (ROOT / 'reading/decipher6l_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()

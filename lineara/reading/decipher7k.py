"""Seven hypotheses following decipher6j.py: local signs, regional units, the geography of the Knossos names, and
replications of the R/T vowel pattern.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the seven.

K1  Signs attested at only one site stand in entry labels (names) more often than widespread unread signs do.
K2  Those local signs stand word-finally more often than widespread unread signs do.
K3  Grain entries at Haghia Triada carry fractions less often than grain entries elsewhere (a smaller unit there).
K4  Counts of men (VIR) differ by site too. A unit explanation of J6 predicts they do not.
K5  Linear A words that match Knossos words (exactly or as a stem plus one syllable) come from sites near Knossos
    (Knossos, Tylissos, Arkhanes, Iouktas, Malia) more often than chance.
K6  The richer vowel set after R/T (J3) replicates on SigLA's transcription.
K7  It holds at Khania and at Zakros separately.
"""
from collections import Counter, defaultdict
import json
from math import log
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher6j as J  # noqa: E402

I, X, T, B, D, V, G = J.I, J.X, J.T, J.B, J.D, J.V, J.I.H.G
ROOT = B.ROOT
rng = J.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
NEAR_KN = {'Knossos', 'Tylissos', 'Arkhanes', 'Iouktas', 'Malia'}


# ------------------------------------------------------------------ local signs
def unread_words():
    rows = []
    sites = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word-with-unknown-sign':
                signs = t['label'].split('-')
                for i, x in enumerate(signs):
                    if re.fullmatch(r'\*\d+[A-Z]?', x):
                        rows.append((x, t.get('function'), i == len(signs) - 1, r['site']))
                        sites[x].add(r['site'])
    cnt = Counter(x for x, *_ in rows)
    local = {x for x, s in sites.items() if len(s) == 1 and cnt[x] >= 3}
    return rows, local


ROWS, LOCAL = unread_words()


def local_test(field):
    flags = [x in LOCAL for x, *_ in ROWS]
    vals = [(f == 'entry label') if field == 'entry' else fin for _, f, fin, _ in ROWS]

    def stat(fl):
        a = [v for v, f in zip(vals, fl) if f]
        b = [v for v, f in zip(vals, fl) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, flags, reps=REPS)
    a = [v for v, f in zip(vals, flags) if f]
    b = [v for v, f in zip(vals, flags) if not f]
    return real, p, f'{sum(a)}/{len(a)}', f'{sum(b)}/{len(b)}'


def K1():
    r, p, a, b = local_test('entry')
    record('K1 local signs in names', 'Single-site unread signs stand in entry labels more than widespread unread signs',
           {'local': a, 'widespread': b, 'p': round(p, 4)}, {'local signs': sorted(LOCAL)})
    return p


def K2():
    r, p, a, b = local_test('final')
    record('K2 local signs word-final', 'Single-site unread signs stand word-finally more than widespread unread signs',
           {'local': a, 'widespread': b, 'p': round(p, 4)}, {})
    return p


# ------------------------------------------------------------------ regional units
def entries_with_fraction():
    rows = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for tok in r['tokens']:
            ents[tok['entry']].append(tok)
        for _, toks in ents.items():
            com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in toks if t['cls'] == 'commodity' and re.findall(r'[A-Z]{3,}', t['label'])]
            has_num = any(t['cls'] == 'number' for t in toks)
            has_frac = any(t['cls'].startswith('fraction') for t in toks)
            if com and (has_num or has_frac):
                rows.append((r['site'], com[0], has_frac))
    return rows


def K3():
    rows = [(s, f) for s, c, f in entries_with_fraction() if c == 'GRA']
    is_ht = [s == 'Haghia Triada' for s, _ in rows]
    fr = [f for _, f in rows]

    def stat(fl):
        a = [v for v, f in zip(fr, fl) if f]
        b = [v for v, f in zip(fr, fl) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, is_ht, reps=REPS, lower=True)
    record('K3 grain fractions by site', 'Grain entries at Haghia Triada carry fractions less often than elsewhere',
           {'HT': f"{sum(f for f, h in zip(fr, is_ht) if h)}/{sum(is_ht)}", 'elsewhere': f"{sum(f for f, h in zip(fr, is_ht) if not h)}/{len(is_ht) - sum(is_ht)}",
            'p': round(p, 4)}, {'sites elsewhere': dict(Counter(s for s, _ in rows if s != 'Haghia Triada'))})
    return p


def K4():
    rows = [(x['record'], x['q']) for x in T.ENTRIES if x['com'] == 'VIR' and x['q'] > 0]
    site = {r['name']: r['site'] for r in B.READ['records']}
    rows = [(site[rec], log(q)) for rec, q in rows if rec in site]
    sc = Counter(s for s, _ in rows)
    rows = [r for r in rows if sc[r[0]] >= 5]
    vals = [v for _, v in rows]
    mu = sum(vals) / len(vals)

    def ss(labs):
        g = defaultdict(list)
        for s, v in zip(labs, vals):
            g[s].append(v)
        return sum(len(x) * (sum(x) / len(x) - mu) ** 2 for x in g.values())
    real, p, nm = X.shuffle_test(ss, [s for s, _ in rows], reps=REPS)
    record('K4 counts of men by site', 'Counts of men (VIR) differ by site (a unit explanation of J6 predicts not)',
           {'between_SS': round(real, 3), 'null_mean': round(nm, 3), 'p': round(p, 4), 'entries': len(rows)},
           {'geometric means': {s: round(2.718281828 ** (sum(v for s2, v in rows if s2 == s) / n), 1) for s, n in Counter(s for s, _ in rows).items()}})
    return p


# ------------------------------------------------------------------ geography of the Knossos names
def K5():
    kn = set(V.kn_only)
    sites = defaultdict(set)
    for r, t, w in B.words_of():
        sites[w].add(r['site'])
    words = sorted(sites)
    match = {w: (w in kn) or any((w + (s,)) in kn for s in ('ro', 'no', 'to', 'ko', 'so', 'jo', 'ta', 'ja', 'mo', 'qo', 'wo', 'de', 'we'))
             for w in words}
    near = {w: bool(sites[w] & NEAR_KN) for w in words}
    flags = [match[w] for w in words]

    def stat(fl):
        a = [near[w] for w, f in zip(words, fl) if f]
        return sum(a) / max(1, len(a))
    real, p, nm = X.shuffle_test(stat, flags, reps=REPS)
    record('K5 Knossos matches from nearby sites', 'Linear A words matching Knossos words come from sites near Knossos more than chance',
           {'near_share_matched': round(real, 3), 'near_share_all': round(sum(near.values()) / len(words), 3), 'p': round(p, 4),
            'matched_words': sum(flags)},
           {'matched words by site': dict(Counter(s for w in words if match[w] for s in sites[w]))})
    return p


# ------------------------------------------------------------------ replications of J3
def entropy_gap(ws):
    return J.entropy_by_class(ws, True) - J.entropy_by_class(ws, False)


def K6():
    real, p, nm = T.label_perm(lambda a, b: entropy_gap(a) - entropy_gap(b), G.SIG, LB, reps=REPS)
    record('K6 R/T vowels in SigLA', 'The richer vowel set after R/T replicates on SigLA\'s transcription',
           {'SigLA_gap': round(entropy_gap(G.SIG), 3), 'LB_gap': round(entropy_gap(LB), 3), 'p': round(p, 4)}, {'lineara.xyz gap': round(entropy_gap(LA), 3)})
    return p


def K7():
    res = {}
    ps = []
    for s in ('Khania', 'Zakros'):
        ws = D.site_words(lambda x, s=s: x == s)
        real, p, nm = T.label_perm(lambda a, b: entropy_gap(a) - entropy_gap(b), ws, LB, reps=REPS)
        res[s] = {'gap': round(entropy_gap(ws), 3), 'p': round(p, 4), 'words': len(ws)}
        ps.append(p)
    p = max(ps)  # both must hold: the larger p is the test of the conjunction
    record('K7 R/T vowels at Khania and Zakros', 'The richer vowel set after R/T holds at Khania and at Zakros separately',
           {'p (larger of the two)': round(p, 4), **res}, {'Linear B gap': round(entropy_gap(LB), 3)})
    return p


TESTS = [K1, K2, K3, K4, K5, K6, K7]


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
    (ROOT / 'reading/decipher7k_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()

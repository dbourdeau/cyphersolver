"""Nine hypotheses on questions not yet asked: what drives the shared commodity vocabularies (decipher8h H7), how
Linear A at Knossos relates to Knossos Linear B, where the signs Linear B dropped cluster, and regional practice.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the nine. Per-tablet tests merge sides a and b.

I1  Single-commodity tablets of the same commodity share entry labels (persons) more than other tablets.
I2  Single-commodity tablets of the same commodity share heading words more than other tablets.
I3  Linear A words from Knossos use syllables more like Knossos Linear B than Linear A words from other sites do.
I4  The R/T e/o rule (e/o after coronals) is weaker in Linear A from Knossos than from other sites.
I5  Signs with no Linear B value are commoner in religious words than in administrative words.
I6  Special signs (PA3, RA2, PU2, TA2) are commoner in religious words than in administrative words.
I7  Commodity ligatures (OLE+KI, OLE+U, ...) are site-specific: adjunct and site are associated beyond chance.
I8  Heading words are attested at two or more sites more often than entry labels (terms travel, persons do not).
I9  Entry-label names at Haghia Triada differ in syllable profile from entry-label names elsewhere.
"""
from collections import Counter, defaultdict
import json
from math import log2
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher8h as H  # noqa: E402

G, F, X, T, B, D, Db, V = H.G, H.F, H.X, H.T, H.B, H.D, H.Db, H.V
ROOT = B.ROOT
rng = H.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
RARE = X.RARE
whole = X.whole
FRACTION_LETTERS = {'A', 'B', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'L2', 'L3', 'L4', 'L6'}


def jsd_prof(a, b):
    ca, cb = Counter(x for w in a for x in w), Counter(x for w in b for x in w)
    na, nb = sum(ca.values()), sum(cb.values())
    keys = set(ca) | set(cb)
    p = {k: ca[k] / na for k in keys}
    q = {k: cb[k] / nb for k in keys}
    m = {k: (p[k] + q[k]) / 2 for k in keys}
    kl = lambda x: sum(x[k] * log2(x[k] / m[k]) for k in keys if x[k] > 0)
    return (kl(p) + kl(q)) / 2


# ------------------------------------------------------------------ I1, I2
def tablet_functions():
    tabs = defaultdict(lambda: {'ent': set(), 'head': set(), 'com': set()})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        t = tabs[whole(r['name'])]
        for tok in r['tokens']:
            if tok['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', tok['label'])
                if m:
                    t['com'].add(m[0])
            if tok['cls'] == 'word' and tok['label'] not in X.TERMS:
                if tok.get('function') == 'entry label':
                    t['ent'].add(tok['label'])
                elif tok.get('function') == 'heading':
                    t['head'].add(tok['label'])
    return tabs


TF = tablet_functions()


def shared_by_commodity(key):
    tabs = [(k, t) for k, t in TF.items() if len(t['com']) == 1 and t[key]]
    names = [k for k, _ in tabs]
    sets = {k: t[key] for k, t in tabs}
    share = {(a, b): bool(sets[a] & sets[b]) for i, a in enumerate(names) for b in names[i + 1:]}

    def stat(labs):
        cm = dict(zip(names, labs))
        same = [v for (a, b), v in share.items() if cm[a] == cm[b]]
        diff = [v for (a, b), v in share.items() if cm[a] != cm[b]]
        return sum(same) / max(1, len(same)) - sum(diff) / max(1, len(diff))
    real, p, nm = X.shuffle_test(stat, [next(iter(t['com'])) for _, t in tabs], reps=REPS)
    return real, p, nm, len(names)


def I1():
    r, p, nm, n = shared_by_commodity('ent')
    record('I1 persons by commodity', 'Same-commodity tablets share entry labels more than other tablets',
           {'diff_share_pairs_sharing': round(r, 4), 'null_mean': round(nm, 4), 'p': round(p, 4), 'tablets': n}, {})
    return p


def I2():
    r, p, nm, n = shared_by_commodity('head')
    record('I2 headings by commodity', 'Same-commodity tablets share heading words more than other tablets',
           {'diff_share_pairs_sharing': round(r, 4), 'null_mean': round(nm, 4), 'p': round(p, 4), 'tablets': n}, {})
    return p


# ------------------------------------------------------------------ Knossos Linear A
LA_KN = D.site_words(lambda s: s == 'Knossos')
LA_OTHER = D.site_words(lambda s: s != 'Knossos')
LB_KN = [w for w in V.kn_only if T.clean(w)]


def I3():
    stat = lambda kn, oth: jsd_prof(oth, LB_KN) - jsd_prof(kn, LB_KN)
    real, p, nm = T.label_perm(stat, LA_KN, LA_OTHER, reps=REPS)
    # control: the same comparison against Pylos Linear B, where no continuity is expected
    lb_py = [w for w in V.py_only if T.clean(w)]
    rc, pc, _ = T.label_perm(lambda kn, oth: jsd_prof(oth, lb_py) - jsd_prof(kn, lb_py), LA_KN, LA_OTHER, reps=REPS)
    record('I3 Knossos Linear A and Knossos Linear B', 'Linear A words from Knossos are closer to Knossos Linear B than other Linear A words are',
           {'jsd_KN_LA_to_KN_LB': round(jsd_prof(LA_KN, LB_KN), 4), 'jsd_other_LA_to_KN_LB': round(jsd_prof(LA_OTHER, LB_KN), 4),
            'p': round(p, 4), 'words': [len(LA_KN), len(LA_OTHER)]},
           {'same comparison against Pylos Linear B': {'diff': round(rc, 4), 'p': round(pc, 4)}})
    return p


def I4():
    f = lambda ws: X.log_or_v(ws, RARE)
    real, p, nm = T.label_perm(lambda kn, oth: f(oth) - f(kn), LA_KN, LA_OTHER, reps=REPS)
    record('I4 rule weaker at Knossos', 'The R/T e/o rule is weaker in Linear A from Knossos than elsewhere',
           {'logOR_Knossos': round(f(LA_KN), 3), 'logOR_other': round(f(LA_OTHER), 3), 'p': round(p, 4), 'words': [len(LA_KN), len(LA_OTHER)]}, {})
    return p


# ------------------------------------------------------------------ signs Linear B dropped
def register_types():
    rel, adm = set(), set()
    for r in B.READ['records']:
        target = adm if r['support'] in B.ADMIN else (None if r['support'] in B.SEAL else rel)
        if target is None:
            continue
        for t in r['tokens']:
            if t['cls'] in ('word', 'word-with-unknown-sign', 'term'):
                parts = t['label'].split('-')
                if len(parts) >= 2:
                    target.add(tuple(parts))
    return sorted(rel - adm), sorted(adm - rel)


REL, ADM = register_types()


def sign_share(pred):
    return lambda ws: sum(1 for w in ws for x in w if pred(x)) / max(1, sum(len(w) for w in ws))


def I5():
    unread = lambda x: x.startswith('*') or not re.fullmatch(r'[A-Z]+[0-9]?', x)
    f = sign_share(unread)
    real, p, nm = T.label_perm(lambda a, b: f(a) - f(b), REL, ADM, reps=REPS)
    record('I5 dropped signs in religious words', 'Signs with no Linear B value are commoner in religious words',
           {'religious_share': round(f(REL), 4), 'admin_share': round(f(ADM), 4), 'p': round(p, 4), 'n': [len(REL), len(ADM)]},
           {'unread signs in religious words': Counter(x for w in REL for x in w if unread(x)).most_common(8)})
    return p


def I6():
    special = lambda x: x in ('PA3', 'RA2', 'PU2', 'TA2', 'RA3', 'AU', 'NWA')
    f = sign_share(special)
    real, p, nm = T.label_perm(lambda a, b: f(a) - f(b), REL, ADM, reps=REPS)
    record('I6 special signs in religious words', 'Special signs are commoner in religious words',
           {'religious_share': round(f(REL), 4), 'admin_share': round(f(ADM), 4), 'p': round(p, 4)}, {})
    return p


# ------------------------------------------------------------------ regional practice
def I7():
    rows = []
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'commodity' and '+' in t['label']:
                parts = t['label'].split('-')[-1].split('+')
                base = re.sub(r'[a-z]+$', '', parts[0].lstrip('*'))
                for adj in parts[1:]:
                    if adj not in FRACTION_LETTERS and re.fullmatch(r'[A-Z]{1,2}[0-9]?', adj):
                        rows.append((r['site'], base + '+' + adj))
    sites = Counter(s for s, _ in rows)
    rows = [x for x in rows if sites[x[0]] >= 3]
    labs = [s for s, _ in rows]
    stat = lambda ls: X.chi2(list(zip(ls, [a for _, a in rows])))
    real, p, nm = X.shuffle_test(stat, labs, reps=REPS)
    tab = defaultdict(Counter)
    for s, a in rows:
        tab[s][a] += 1
    record('I7 ligatures by site', 'Commodity ligature adjuncts are associated with sites',
           {'chi2': round(real, 2), 'null_mean': round(nm, 2), 'p': round(p, 4), 'tokens': len(rows)},
           {'by site': {s: dict(c.most_common(6)) for s, c in tab.items()}})
    return p


def I8():
    sites = defaultdict(set)
    fn = defaultdict(Counter)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] == 'word' and t['label'] not in X.TERMS:
                sites[t['label']].add(r['site'])
                fn[t['label']][t.get('function')] += 1
    words = [w for w, c in fn.items() if c.most_common(1)[0][0] in ('heading', 'entry label')]
    is_head = [fn[w].most_common(1)[0][0] == 'heading' for w in words]
    multi = {w: len(sites[w]) >= 2 for w in words}

    def stat(flags):
        a = [multi[w] for w, f in zip(words, flags) if f]
        b = [multi[w] for w, f in zip(words, flags) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, is_head, reps=REPS)
    record('I8 terms travel, persons stay', 'Heading words are attested at two or more sites more often than entry labels',
           {'heading_multi_site': f"{sum(multi[w] for w, f in zip(words, is_head) if f)}/{sum(is_head)}",
            'entry_multi_site': f"{sum(multi[w] for w, f in zip(words, is_head) if not f)}/{len(words) - sum(is_head)}", 'p': round(p, 4)},
           {'multi-site headings': sorted(w for w, f in zip(words, is_head) if f and multi[w])})
    return p


def I9():
    by = defaultdict(set)
    for r in B.READ['records']:
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') == 'entry label' and t['label'] not in X.TERMS:
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(re.fullmatch(r'[a-z]+[0-9]?', x) for x in w):
                    by['HT' if r['site'] == 'Haghia Triada' else 'other'].add(w)
    ht, oth = sorted(by['HT'] - by['other']), sorted(by['other'] - by['HT'])
    real, p, nm = T.label_perm(jsd_prof, ht, oth, reps=REPS)
    record('I9 regional names', 'Entry-label names at Haghia Triada differ in syllable profile from names elsewhere',
           {'jsd': round(real, 4), 'null_mean': round(nm, 4), 'p': round(p, 4), 'names': [len(ht), len(oth)]}, {})
    return p


TESTS = [I1, I2, I3, I4, I5, I6, I7, I8, I9]


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
    (ROOT / 'reading/decipher9i_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()


def I9_control():
    """Added after the run: the same HT-vs-elsewhere comparison on administrative words that are not entry labels."""
    by = defaultdict(set)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] == 'word' and t.get('function') != 'entry label' and t['label'] not in X.TERMS:
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(re.fullmatch(r'[a-z]+[0-9]?', x) for x in w):
                    by['HT' if r['site'] == 'Haghia Triada' else 'other'].add(w)
    ht, oth = sorted(by['HT'] - by['other']), sorted(by['other'] - by['HT'])
    real, p, nm = T.label_perm(jsd_prof, ht, oth, reps=REPS)
    return {'jsd': round(real, 4), 'null_mean': round(nm, 4), 'p': round(p, 4), 'words': [len(ht), len(oth)]}

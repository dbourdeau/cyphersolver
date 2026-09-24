"""Eleven hypotheses: the Linear A -u / Knossos -o lead of decipher15c.py F2 tested on its own, and replications of
the coronal rule and the consonant rows on SigLA's independent transcription.

Each has a prediction stated before the test ran and one primary test with its own null. Benjamini-Hochberg at
5% runs across the eleven.

The -u / -o correspondence
G1  Linear A words ending in -Cu have a Knossos personal name X-Co (same stem, same consonant, final o) more often
    than Linear A words ending in another vowel do. Control: Pylos names.
G2  G1 holds without the R row.
G3  Linear A final -Ci corresponds to Knossos -Ce more often than other final vowels do.
G4  Knossos names built on a Linear A stem (stem + one syllable) end in -o more often than other Knossos names.
G18 Linear A words ending in -a match Knossos names exactly more often than words ending in -u (Greek keeps -a
    and changes -u).
G16 Linear A words ending in -u are entry labels (names) more often than words with other final vowels.
Replications and extensions of the coronal rule and the rows
G8  The coronal rule (e/o after coronals) holds in SigLA's independent transcription, against Linear B.
G13 The consonant-row cohesion of decipher10 Y1 holds in SigLA's transcription.
G10 The coronal rule holds site by site: sites with 30+ word types show a positive log odds ratio more than chance.
G11 Knossos scribes with more Minoan-shaped names use more special signs (ra2, pu2, ta2, a2, a3, au, ...).
G14 Knossos words written with undeciphered signs follow the coronal rule in their readable syllables more than
    other Knossos words do.
"""
from collections import Counter, defaultdict
import json
from math import comb
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import decipher15c as F  # noqa: E402

X, T, B, D, Db, V = F.X, F.T, F.B, F.D, F.Db, F.V
ROOT = B.ROOT
rng = F.rng
REPS = 2000
out = D.out
out.clear()
record = D.record
grid = D.grid
LA, LB = X.LA, X.LB
RARE = X.RARE
KN_N, PY_N = T.KN_N, T.PY_N
VOW = 'aeiou'


# ------------------------------------------------------------------ the -u / -o correspondence
def final_rate(words, target_names, v_la, v_lb, cons_ok=lambda c: True):
    names = set(target_names)
    elig = [w for w in words if len(w) >= 2 and grid(w[-1]) and grid(w[-1])[0] and cons_ok(grid(w[-1])[0])]
    hit = lambda w: (w[:-1] + (grid(w[-1])[0] + v_lb,)) in names
    fv = [grid(w[-1])[1] for w in elig]

    def stat(vs):
        a = [hit(w) for w, v in zip(elig, vs) if v == v_la]
        b = [hit(w) for w, v in zip(elig, vs) if v != v_la]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real = stat(fv)
    labs = list(fv)
    null = []
    for _ in range(REPS):
        rng.shuffle(labs)
        null.append(stat(labs))
    matches = sorted(f"{'-'.join(w).upper()} ~ {'-'.join(w[:-1] + (grid(w[-1])[0] + v_lb,))}" for w in elig if grid(w[-1])[1] == v_la and hit(w))
    rate = lambda v: (sum(hit(w) for w in elig if grid(w[-1])[1] == v), sum(1 for w in elig if grid(w[-1])[1] == v))
    return real, B.pv(null, real), matches, {v: rate(v) for v in VOW}


def G1():
    r, p, m, rates = final_rate(LA, KN_N, 'u', 'o')
    pr, pp, pm, prates = final_rate(LA, PY_N, 'u', 'o')
    record('G1 Linear A -u = Knossos -o', 'Linear A words in -Cu have a Knossos name X-Co more often than words in other vowels',
           {'diff': round(r, 4), 'p': round(p, 4), 'rates (hits, words) by Linear A final vowel': rates},
           {'matches': m, 'Pylos control': {'diff': round(pr, 4), 'p': round(pp, 4), 'matches': pm}})
    return p


def G2():
    r, p, m, rates = final_rate(LA, KN_N, 'u', 'o', cons_ok=lambda c: c != 'r')
    record('G2 -u = -o without R', 'G1 holds without the R row',
           {'diff': round(r, 4), 'p': round(p, 4), 'rates': rates}, {'matches': m})
    return p


def G3():
    r, p, m, rates = final_rate(LA, KN_N, 'i', 'e')
    dent = final_rate(LA, KN_N, 'i', 'e', cons_ok=lambda c: c in F.DENT)
    record('G3 Linear A -i = Knossos -e', 'Linear A final -Ci corresponds to Knossos -Ce more than other final vowels do',
           {'diff': round(r, 4), 'p': round(p, 4), 'rates': rates}, {'matches': m, 'dental consonants only': {'diff': round(dent[0], 4), 'p': round(dent[1], 4)}})
    return p


def G4():
    la = set(LA)
    built = [w for w in KN_N if len(w) >= 3 and w[:-1] in la]
    other = [w for w in KN_N if w not in set(built)]
    ends_o = lambda w: bool(grid(w[-1])) and grid(w[-1])[1] == 'o'
    real, p, nm = T.label_perm(lambda a, b: sum(map(ends_o, a)) / len(a) - sum(map(ends_o, b)) / len(b), built, other)
    record('G4 Greek -o on Minoan stems', 'Knossos names built on a Linear A stem end in -o more often than other Knossos names',
           {'built_on_LA': f'{sum(map(ends_o, built))}/{len(built)}', 'other': f'{sum(map(ends_o, other))}/{len(other)}', 'p': round(p, 4)},
           {'endings of names built on Linear A stems': dict(Counter(w[-1] for w in built).most_common(10))})
    return p


def G18():
    names = set(KN_N)
    a = [w for w in LA if len(w) >= 2 and grid(w[-1]) and grid(w[-1])[1] == 'a']
    u = [w for w in LA if len(w) >= 2 and grid(w[-1]) and grid(w[-1])[1] == 'u']
    real, p, nm = T.label_perm(lambda x, y: sum(w in names for w in x) / len(x) - sum(w in names for w in y) / len(y), a, u)
    record('G18 -a kept, -u changed', 'Linear A words in -a match Knossos names exactly more often than words in -u',
           {'a_exact': f'{sum(w in names for w in a)}/{len(a)}', 'u_exact': f'{sum(w in names for w in u)}/{len(u)}', 'p': round(p, 4)},
           {'exact -a matches': sorted('-'.join(w).upper() for w in a if w in names)})
    return p


def G16():
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    major = {w: c.most_common(1)[0][0] for w, c in fn.items() if grid(w[-1])}
    words = sorted(major)
    is_u = [grid(w[-1])[1] == 'u' for w in words]
    ent = {w: major[w] == 'entry label' for w in words}

    def stat(flags):
        a = [ent[w] for w, f in zip(words, flags) if f]
        b = [ent[w] for w, f in zip(words, flags) if not f]
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    real, p, nm = X.shuffle_test(stat, is_u)
    record('G16 -u words are names', 'Linear A words ending in -u are entry labels more often than words with other finals',
           {'u_entry_share': round(sum(ent[w] for w, f in zip(words, is_u) if f) / max(1, sum(is_u)), 3),
            'other_entry_share': round(sum(ent[w] for w, f in zip(words, is_u) if not f) / max(1, len(words) - sum(is_u)), 3),
            'p': round(p, 4), 'n': [sum(is_u), len(words) - sum(is_u)]}, {})
    return p


# ------------------------------------------------------------------ SigLA replications
def sigla_words():
    docs = json.loads((ROOT / 'data/sigla_decoded.json').read_text(encoding='utf-8'))
    val = {}
    for d in docs:
        for a in d['attestations']:
            try:
                v = a['values_raw']['fields'][0]['fields'][0]
            except (KeyError, IndexError, TypeError):
                v = None
            val[(d['name'], a['n'])] = v
    words = set()
    for d in json.loads((ROOT / 'data/sigla_words.json').read_text(encoding='utf-8')):
        for w in d['words']:
            if not w['confident_signs']:
                continue
            vs = [val.get((d['name'], n)) for n in w['attestations']]
            if len(vs) >= 2 and all(isinstance(v, str) and re.fullmatch(r'[a-z]+[0-9]?', v) for v in vs):
                words.add(tuple(vs))
    return sorted(words)


SIG = sigla_words()


def G8():
    f = lambda ws: X.log_or_v(ws, RARE)
    real, p, nm = X.compare(SIG, LB, f)
    record('G8 coronal rule in SigLA', 'The coronal rule holds in SigLA\'s independent transcription',
           {'logOR_SigLA': round(f(SIG), 3), 'logOR_LB': round(f(LB), 3), 'p': round(p, 4), 'sigla_words': len(SIG)},
           {'logOR_lineara_xyz': round(f(LA), 3), 'word types shared with lineara.xyz': len(set(SIG) & set(LA))})
    return p


def G13():
    r, p, n = D.grid_similarity(SIG, 'cons')
    record('G13 consonant rows in SigLA', 'Consonant-row cohesion holds in SigLA\'s transcription',
           {'diff': r, 'p': round(p, 4), 'signs': n}, {'lineara.xyz value (decipher10 Y1)': 0.0748})
    return p


def G10():
    sites = sorted({r['site'] for r in B.READ['records']})
    rows = []
    for s in sites:
        ws = D.site_words(lambda x, s=s: x == s)
        if len(ws) >= 30:
            rows.append((s, len(ws), round(X.log_or_v(ws, RARE), 3)))
    pos = sum(1 for _, _, v in rows if v > 0)
    n = len(rows)
    p = sum(comb(n, k) for k in range(pos, n + 1)) / 2 ** n
    record('G10 coronal rule site by site', 'Sites with 30+ word types show a positive log odds ratio more often than chance',
           {'positive': f'{pos}/{n}', 'sign_test_p': round(p, 4)}, {'sites (name, words, logOR)': rows, 'Linear B logOR': round(X.log_or_v(LB, RARE), 3)})
    return p


# ------------------------------------------------------------------ Knossos scribes and undeciphered-sign words
SPECIAL = {'ra2', 'ra3', 'pu2', 'ta2', 'a2', 'a3', 'au', 'ro2', 'nwa', 'pte', 'dwe', 'dwo', 'twe', 'two'}


def G11():
    per = defaultdict(lambda: {'names': [], 'spec': 0, 'signs': 0})
    kn = set(KN_N)
    for _, r in B.LB_RECS:
        if r.get('site') != 'Knossos' or not r.get('scribe'):
            continue
        d = per[r['scribe']]
        for t in r.get('transliteratedWords', []):
            tl = t.strip().lower()
            if '-' in tl and not any(ch in tl for ch in '[]?'):
                w = tuple(tl.split('-'))
                d['signs'] += len(w)
                d['spec'] += sum(x in SPECIAL for x in w)
                if w in kn:
                    d['names'].append(w)
    rows = [(s, sum(map(X.stem_score, d['names'])) / len(d['names']), d['spec'] / d['signs']) for s, d in per.items()
            if len(d['names']) >= 5 and d['signs'] >= 60]
    xs, ys = [r[1] for r in rows], [r[2] for r in rows]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = B.pv(null, real)
    record('G11 Minoan names and special signs by scribe', 'Knossos scribes with more Minoan-shaped names use more special signs',
           {'spearman': round(real, 3), 'p': round(p, 4), 'scribes': len(rows)}, {})
    return p


def G14():
    kn = [w for w in V.kn_only if len(w) >= 2]
    star = [tuple(x for x in w if not x.startswith('*')) for w in kn if not T.clean(w)]
    plain = [w for w in kn if T.clean(w)]
    f = lambda ws: X.log_or_v(ws, RARE)
    real, p, nm = X.compare(star, plain, f)
    record('G14 coronal rule in undeciphered-sign words', 'Knossos words with undeciphered signs follow the coronal rule more than other Knossos words',
           {'logOR_star_words': round(f(star), 3), 'logOR_other_KN': round(f(plain), 3), 'p': round(p, 4), 'n': [len(star), len(plain)]}, {})
    return p


TESTS = [G1, G2, G3, G4, G18, G16, G8, G13, G10, G11, G14]


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
    (ROOT / 'reading/decipher11g_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + '\n', encoding='utf-8')
    print('\nprimary p:', {k: round(v, 4) for k, v in ps.items()})
    print('survive BH at 5%:', supported)


if __name__ == '__main__':
    main()

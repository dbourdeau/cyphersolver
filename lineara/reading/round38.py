"""Round 38 (loop round 10 of 10): replications of this loop's surviving results on other data or definitions.

AA1  Q-row signs are word-initial more often than in Linear B (round 29 P6), on SigLA's transcription.
AA2  Two pure vowel signs in succession are rarer than in Linear B (P2, reversed there), on SigLA.
AA3  Words end in a pure vowel sign less often than in Linear B (P9, reversed there), on SigLA.
AA4  e/o follow T more than non-coronals, more than in Linear B (round 30 Q1), on SigLA.
AA5  e/o follow Q more than K, more than in Linear B (Q3), on SigLA.
AA6  Equal amounts stand on neighbouring lines beyond chance (round 33 V17), in lists outside Haghia Triada.
AA7  The first entry is the unique largest beyond chance (V16), in lists of four or more entries.
AA9  Words on the same tablet share first signs beyond chance (round 31 S6), on SigLA's tablets (unique words,
     within-site shuffle).
AA10 Knossos names begin with a Q-row sign more often than Thebes/Mycenae/Tiryns names (round 37 Z1).
AA11 Linear A's vowel profile is closer to Pre-Greek stems than to a random (not length-matched) Greek sample (Z7).
"""
from collections import Counter, defaultdict
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round30 as Q  # noqa: E402
import round33 as VV  # noqa: E402
import round37 as Z  # noqa: E402

G, T, B, X = R.G, R.T, R.B, R.X
SIG, LB = G.SIG, R.LB
grid = R.grid


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4)}, {}


def AA1():
    return cmp(SIG, LB, lambda ws: P.initial_share(ws, lambda x: P.cons(x) == 'q'), 'Q-row signs word-initial (SigLA vs Linear B)')


def AA2():
    return cmp(SIG, LB, lambda ws: P.share(ws, lambda w: any(P.vow(w[i]) and P.vow(w[i + 1]) for i in range(len(w) - 1))), 'Two vowel signs in succession rarer (SigLA vs Linear B)', lower=True)


def AA3():
    return cmp(SIG, LB, lambda ws: P.share(ws, lambda w: P.vow(w[-1])), 'Final pure vowel signs rarer (SigLA vs Linear B)', lower=True)


def AA4():
    return cmp(SIG, LB, lambda ws: Q.lor(ws, 't', Q.NONCOR), 'e/o follow T (SigLA vs Linear B)')


def AA5():
    return cmp(SIG, LB, lambda ws: Q.lor(ws, 'q', 'k'), 'e/o follow Q more than K (SigLA vs Linear B)')


def shuffle_lists(lists, stat):
    real = stat(lists)
    null = []
    for _ in range(R.REPS):
        sh = []
        for q in lists:
            q2 = list(q)
            R.rng.shuffle(q2)
            sh.append(q2)
        null.append(stat(sh))
    return real, R.pv_hi(null, real), sum(null) / len(null)


def AA6():
    site = {r['name']: r['site'] for r in B.READ['records']}
    lists = [[x['q'] for x in rec['rows']] for rec in VV.RECS if len(rec['rows']) >= 3 and site[rec['name']] != 'Haghia Triada']
    real, p, nm = shuffle_lists(lists, lambda ls: sum(1 for q in ls for i in range(len(q) - 1) if q[i] == q[i + 1] and q[i] != 1))
    return p, 'Equal amounts on neighbouring lines outside Haghia Triada (1s excluded)', {'adjacent_equal': real, 'null': round(nm, 1), 'p': round(p, 4), 'lists': len(lists)}, {}


def AA7():
    lists = [[x['q'] for x in rec['rows']] for rec in VV.RECS if len(rec['rows']) >= 4 and all(x['q'] > 0 for x in rec['rows'])]
    real, p, nm = shuffle_lists(lists, lambda ls: sum(q[0] == max(q) and q.count(max(q)) == 1 for q in ls))
    return p, 'The first entry is the unique largest (lists of 4+)', {'first_is_max': f'{real}/{len(lists)}', 'null': round(nm, 1), 'p': round(p, 4)}, {}


def sigla_docs():
    docs = json.loads((R.ROOT / 'data/sigla_decoded.json').read_text(encoding='utf-8'))
    val, kind, site = {}, {}, {}
    for d in docs:
        kind[d['name']] = d.get('kind_raw')
        site[d['name']] = d.get('site')
        for a in d['attestations']:
            try:
                val[(d['name'], a['n'])] = a['values_raw']['fields'][0]['fields'][0]
            except (KeyError, IndexError, TypeError):
                pass
    out = {}
    for d in json.loads((R.ROOT / 'data/sigla_words.json').read_text(encoding='utf-8')):
        if kind.get(d['name']) != 'Tablet':
            continue
        ws = set()
        for w in d['words']:
            vs = [val.get((d['name'], n)) for n in w['attestations']]
            if w['confident_signs'] and len(vs) >= 2 and all(isinstance(v, str) and re.fullmatch(r'[a-z]+[0-9]?', v) for v in vs):
                ws.add(tuple(vs))
        if len(ws) >= 3:
            out[d['name']] = (site[d['name']], sorted(ws))
    return out


def AA9():
    docs = sigla_docs()
    items = [(k, docs[k][0], w[0]) for k in sorted(docs) for w in docs[k][1]]

    def stat(signs):
        by = defaultdict(list)
        for (k, _, _), s in zip(items, signs):
            by[k].append(s)
        return sum(sum(n * (n - 1) for n in Counter(v).values()) for v in by.values())
    real = stat([s for *_, s in items])
    idx = defaultdict(list)
    for i, (_, st, _) in enumerate(items):
        idx[st].append(i)
    null = []
    for _ in range(R.REPS):
        sh = [s for *_, s in items]
        for ii in idx.values():
            v = [sh[i] for i in ii]
            R.rng.shuffle(v)
            for i, x in zip(ii, v):
                sh[i] = x
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Tablet-mates share first signs (SigLA tablets, unique words, within-site shuffle)', {'pairs': real, 'null': round(sum(null) / len(null), 1), 'p': round(p, 4), 'tablets': len(docs)}, {}


def AA10():
    main = {'Thebes', 'Mycenae', 'Tiryns', 'Vases - Thebes', 'Vases - Tiryns', 'Vases - Mycenae', 'Midea'}
    ma = [w for w, s in B.LB_SITES.items() if s and s <= main and T.CAT.get(w) == 'anthroponym' and T.clean(w) and len(w) >= 2]
    q = lambda ws: sum(1 for w in ws if grid(w[0]) and grid(w[0])[0] == 'q') / len(ws)
    return cmp(T.KN_N, ma, q, 'Knossos names begin with Q more often than Thebes/Mycenae/Tiryns names')


def AA11():
    la = Z.prof(R.LA, 'v')
    f = lambda pre, grk: Z.jsd(la, Z.prof(grk, 'v')) - Z.jsd(la, Z.prof(pre, 'v'))
    real = f(T.PRE, T.GRK_U)
    pool, k, null = list(T.PRE) + list(T.GRK_U), len(T.PRE), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(f(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, 'Linear A vowel profile closer to Pre-Greek than to an unmatched Greek sample', {'jsd_PreGreek': round(Z.jsd(la, Z.prof(T.PRE, 'v')), 4), 'jsd_Greek_unmatched': round(Z.jsd(la, Z.prof(T.GRK_U, 'v')), 4), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round38', 'replications of the loop results', __doc__, [AA1, AA2, AA3, AA4, AA5, AA6, AA7, AA9, AA10, AA11])

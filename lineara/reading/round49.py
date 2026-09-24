"""Round 49: twenty hypotheses following the strongest results of the two loops. Benjamini-Hochberg at 5% across
all twenty.

Consonant repetition
TT1  Neighbouring syllables share a consonant with different signs (TA-TI, not SA-SA) more often than in Linear B.
TT2  Consonant repetition holds in Linear A entry labels (names) against Linear B.
TT3  It holds at Haghia Triada and elsewhere separately (the larger p is the primary).
TT4  Pre-Greek words share a consonant across different neighbouring signs more often than Greek words.
TT11 Consonant-by-consonant repetition rates correlate between Linear A and Pre-Greek more than between Linear A
     and Greek.
TT12 Repetition is concentrated at the start of the word (first two syllables) more than in Linear B.
TT13 When the consonant repeats, the vowel changes more often in Linear A than in Linear B.
Vowels
TT5  Within e/o syllables, o is commoner after R and Q and e after T, N and S, more than in Linear B.
TT19 Pre-Greek's choice of e or o depends on the consonant more than Greek's (normalised MI).
Pre-Greek and Eteocretan
TT16 Eteocretan words begin with an a-syllable more often than Greek.
TT17 Pre-Greek stems end on a more restricted set of consonants (relative to initials) than Greek stems.
TT18 Pre-Greek words begin with a pure vowel less often than Greek words.
Bookkeeping
TT6  Different scribes order the same pair of commodities the same way more often than chance.
TT21 Haghia Triada and the other sites order the same pairs of commodities the same way more often than chance.
TT14 Oil comes before wine on tablets that record both, more often than not.
TT7  The last entry of a list is its unique smallest more often than chance.
TT22 Lists of men are ordered largest-first beyond chance.
TT15 Scribes who total their lists more often also order them more strictly largest-first (Spearman over scribes).
TT20 Lists that carry a total record larger summed amounts than lists without one.
Religious prefixes
TT8  Vowel-initial religious words are an attested Linear A word plus the vowel more often than vowel-initial
     administrative words.
"""
from collections import Counter, defaultdict
from math import comb, log
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round39 as BB  # noqa: E402
import round40 as CC  # noqa: E402
import round41 as DD  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402
import round37 as Z  # noqa: E402
import vigorous2 as W2  # noqa: E402

B, T, X, D = R.B, R.T, R.X, R.D
grid, cons, vow = R.grid, P.cons, P.vow
LA, LB, PRE, GRK = R.LA, R.LB, T.PRE, T.GRK
harm = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1]) and w[i] != w[i + 1]) / max(1, sum(len(w) - 1 for w in ws))
rep = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def TT1():
    return cmp(LA, LB, harm, 'Same consonant, different sign, in neighbouring syllables: Linear A vs Linear B')


def TT2():
    return cmp(DD.ENT, LB, rep, 'Consonant repetition in Linear A entry labels vs Linear B')


def TT3():
    res, ps = {}, []
    for name, pred in (('HT', lambda s: s == 'Haghia Triada'), ('other', lambda s: s != 'Haghia Triada')):
        ws = D.site_words(pred)
        r, p, nm = R.compare(ws, LB, rep)
        res[name] = {'rate': round(rep(ws), 4), 'p': round(p, 4)}
        ps.append(p)
    return max(ps), 'Consonant repetition at HT and elsewhere, each vs Linear B', {**res, 'LB': round(rep(LB), 4), 'p (larger)': round(max(ps), 4)}, {}


def TT4():
    return cmp(PRE, GRK, harm, 'Pre-Greek: same consonant, different sign, vs Greek')


def cons_rates(ws):
    tot, hit = Counter(), Counter()
    for w in ws:
        for i in range(len(w) - 1):
            c = cons(w[i])
            if c:
                tot[c] += 1
                hit[c] += cons(w[i + 1]) == c
    return {c: hit[c] / tot[c] for c in tot if tot[c] >= 20}


def TT11():
    la = cons_rates(LA)

    def stat(pre, grk):
        p_, g_ = cons_rates(pre), cons_rates(grk)
        cs = sorted(set(la) & set(p_) & set(g_))
        return B.spearman([la[c] for c in cs], [p_[c] for c in cs]) - B.spearman([la[c] for c in cs], [g_[c] for c in cs])
    real = stat(PRE, GRK)
    pool, k, null = list(PRE) + list(GRK), len(PRE), []
    for _ in range(500):
        R.rng.shuffle(pool)
        null.append(stat(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, 'Repetition rates by consonant: Linear A correlates with Pre-Greek more than with Greek', {'rho_diff': round(real, 3), 'null': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def TT12():
    def f(ws):
        first = [cons(w[0]) and cons(w[0]) == cons(w[1]) for w in ws if len(w) >= 3]
        later = [cons(w[i]) and cons(w[i]) == cons(w[i + 1]) for w in ws if len(w) >= 3 for i in range(1, len(w) - 1)]
        return sum(map(bool, first)) / len(first) - sum(map(bool, later)) / len(later)
    return cmp(LA, LB, f, 'Repetition concentrated in the first two syllables, more than in Linear B')


def TT13():
    def f(ws):
        pairs = [(w[i], w[i + 1]) for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])]
        return sum(a != b for a, b in pairs) / max(1, len(pairs))
    return cmp(LA, LB, f, 'When the consonant repeats, the vowel changes more often than in Linear B')


def TT5():
    def f(ws):
        e = [(cons(x), grid(x)[1]) for w in ws for x in w if grid(x) and grid(x)[1] in 'eo' and cons(x)]
        a = [v == 'o' for c, v in e if c in 'rq']
        b = [v == 'o' for c, v in e if c in 'tns']
        return sum(a) / max(1, len(a)) - sum(b) / max(1, len(b))
    return cmp(LA, LB, f, 'o prefers R/Q and e prefers T/N/S, more than in Linear B')


def TT19():
    real = CC.nmi(PRE)[0] - CC.nmi(GRK)[0]
    pool, k, null = list(PRE) + list(GRK), len(PRE), []
    for _ in range(500):
        R.rng.shuffle(pool)
        null.append(CC.nmi(pool[:k])[0] - CC.nmi(pool[k:])[0])
    p = R.pv_hi(null, real)
    return p, 'Pre-Greek e/o choice depends on the consonant more than Greek\'s', {'nmi_pre': round(CC.nmi(PRE)[0], 3), 'nmi_greek': round(CC.nmi(GRK)[0], 3), 'p': round(p, 4)}, {}


def TT16():
    a, b = Z.eteo()
    return cmp(a, b, lambda ws: sum(1 for w in ws if grid(w[0]) and grid(w[0])[1] == 'a') / len(ws), 'Eteocretan begins with a-syllables more often than Greek')


def TT17():
    return cmp(PRE, GRK, lambda ws: BB.ent(BB.dist(ws, -1)) - BB.ent(BB.dist(ws, 0)), 'Pre-Greek stems end on more restricted consonants', lower=True)


def TT18():
    return cmp(PRE, GRK, lambda ws: sum(1 for w in ws if vow(w[0])) / len(ws), 'Pre-Greek words begin with a pure vowel less often', lower=True)


def scribe_seqs():
    out = []
    for rec in GG.VV.RECS:
        s = GG.seq_of(rec)
        sc = X.SCRIBE_W.get(X.whole(rec['name']))
        if len(s) >= 2 and sc:
            out.append((sc, s))
    return out


def group_agreement(items):
    """items: (group, sequence). For each commodity pair, the majority direction per group; share of group pairs that agree."""
    dirs = defaultdict(lambda: defaultdict(Counter))
    for g, s in items:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                a, b = s[i], s[j]
                key = tuple(sorted((a, b)))
                dirs[key][g][(a, b) == key] += 1
    agree = tot = 0
    for key, byg in dirs.items():
        maj = [c[True] > c[False] for c in byg.values() if c[True] != c[False]]
        for i in range(len(maj)):
            for j in range(i + 1, len(maj)):
                tot += 1
                agree += maj[i] == maj[j]
    return agree / max(1, tot), tot


def shuffle_items(items, reps=R.REPS):
    real, n = group_agreement(items)
    null = []
    for _ in range(reps):
        sh = []
        for g, s in items:
            s2 = list(s)
            R.rng.shuffle(s2)
            sh.append((g, s2))
        null.append(group_agreement(sh)[0])
    return real, R.pv_hi(null, real), sum(null) / len(null), n


def TT6():
    real, p, nm, n = shuffle_items(scribe_seqs())
    return p, 'Different scribes order commodity pairs the same way', {'agreement': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'scribe_pairs': n}, {}


def TT21():
    items = [('HT' if FF.SITE[rec['name']] == 'Haghia Triada' else 'other', GG.seq_of(rec)) for rec in GG.VV.RECS if len(GG.seq_of(rec)) >= 2]
    real, p, nm, n = shuffle_items(items)
    return p, 'HT and the other sites order commodity pairs the same way', {'agreement': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'pairs': n}, {}


def TT14():
    seqs = [s for s in GG.seqs_where(lambda r: True) if 'OLE' in s and 'VIN' in s]
    k = sum(s.index('OLE') < s.index('VIN') for s in seqs)
    n = len(seqs)
    p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else 1.0
    return p, 'Oil comes before wine more often than not', {'oil_first': f'{k}/{n}', 'sign_test_p': round(p, 4)}, {}


def TT7():
    lists = [[x['q'] for x in rec['rows']] for rec in FF.RECS if len(rec['rows']) >= 3 and all(x['q'] > 0 for x in rec['rows'])]
    real, p, nm = FF.shuffle_within(lists, lambda ls: sum(q[-1] == min(q) and q.count(min(q)) == 1 for q in ls))
    return p, 'The last entry is the unique smallest more often than chance', {'last_is_min': f'{real}/{len(lists)}', 'null': round(nm, 1), 'p': round(p, 4)}, {}


def TT22():
    lists = [[x['q'] for x in rec['rows']] for rec in FF.RECS if len(rec['rows']) >= 4 and any(x['com'] == 'VIR' for x in rec['rows'])]
    stat = lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls))
    real, p, nm = FF.shuffle_within(lists, stat)
    return p, 'Lists of men are ordered largest-first beyond chance', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(lists)}, {}


def TT15():
    by = defaultdict(lambda: {'tot': [], 'tau': []})
    for rec in FF.RECS:
        sc = X.SCRIBE_W.get(X.whole(rec['name']))
        if not sc or len(rec['rows']) < 3:
            continue
        by[sc]['tot'].append(rec['total'])
        by[sc]['tau'].append(W2.tau([x['q'] for x in rec['rows']]))
    rows = [(sum(v['tot']) / len(v['tot']), sum(v['tau']) / len(v['tau'])) for v in by.values() if len(v['tot']) >= 3]
    xs, ys = [a for a, _ in rows], [b for _, b in rows]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'Scribes who total more also order more strictly largest-first', {'spearman': round(real, 3), 'p': round(p, 4), 'scribes': len(rows)}, {}


def TT20():
    items = [rec for rec in FF.RECS if len(rec['rows']) >= 2 and sum(x['q'] for x in rec['rows']) > 0]
    r_, p, a, b = R.flag_compare(items, lambda r: r['total'], lambda r: log(sum(x['q'] for x in r['rows'])))
    return p, 'Totalled lists record larger summed amounts', {'with_total_mean_log_sum': a, 'without': b, 'p': round(p, 4)}, {}


def TT8():
    la = set(R.D.LA)
    rel = sorted({w for _, _, w in B.LA_RELIG if vow(w[0]) and len(w) >= 3})
    adm = sorted({w for _, _, w in B.LA_ADMIN if vow(w[0]) and len(w) >= 3} - set(rel))
    f = lambda ws: sum(1 for w in ws if w[1:] in la) / max(1, len(ws))
    return cmp(rel, adm, f, 'Vowel-initial religious words are vowel + attested word more often than administrative ones')


if __name__ == '__main__':
    R.run('round49', 'twenty follow-ups to the strongest results', __doc__,
          [TT1, TT2, TT3, TT4, TT11, TT12, TT13, TT5, TT19, TT16, TT17, TT18, TT6, TT21, TT14, TT7, TT22, TT15, TT20, TT8])

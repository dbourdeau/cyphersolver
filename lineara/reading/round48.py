"""Round 48 (second loop, round 10 of 10): replications of the second loop's results.

LL1  Neighbouring syllables repeat the consonant more than in Linear B (round 39 BB6), on SigLA.
LL2  Final consonants are more restricted relative to initial ones than in Linear B (BB11), on SigLA.
LL3  e versus o depends on the consonant more than in Linear B (round 40 CC5), on SigLA.
LL4  The commodity order (round 43 FF9) holds with grain removed.
LL5  Agreement with Linear B's commodity order (round 44 GG3) holds on pairs not involving grain.
LL6  Unread signs are word-initial more often than known signs (round 45 HH1), at Haghia Triada and elsewhere
     separately (the larger p is the primary).
LL7  NI is followed directly by a number more often than other single signs (HH11), at HT and elsewhere separately.
LL8  Religious words begin with a pure vowel more often than administrative ones (round 46 II2), on SigLA.
LL9  Lists with a total are more strictly largest-first (round 43 FF1), in lists of five or more entries.
LL10 Pre-Greek words repeat neighbouring consonants more than Greek (round 47 KK2), against an unmatched sample.
"""
from collections import Counter, defaultdict
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round39 as BB  # noqa: E402
import round40 as CC  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402
import round45 as HH  # noqa: E402
import round47 as KK  # noqa: E402
import round38 as AA  # noqa: E402

B, T, G = R.B, R.T, R.G
SIG, LB = G.SIG, R.LB


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4)}, {}


def LL1():
    return cmp(SIG, LB, KK.rep_c, 'Neighbouring consonant repetition (SigLA vs Linear B)')


def LL2():
    return cmp(SIG, LB, lambda ws: BB.ent(BB.dist(ws, -1)) - BB.ent(BB.dist(ws, 0)), 'Final consonants more restricted (SigLA vs Linear B)', lower=True)


def LL3():
    real, n = CC.nmi(SIG)
    null = []
    for _ in range(500):
        smp, k = [], 0
        while k < n:
            w = R.rng.choice(LB)
            smp.append(w)
            k += sum(1 for x in w if R.grid(x) and R.grid(x)[0] and R.grid(x)[1] in 'eo')
        null.append(CC.nmi(smp)[0])
    p = R.pv_hi(null, real)
    return p, 'e versus o depends on the consonant (SigLA)', {'nmi_SigLA': round(real, 3), 'nmi_LB': round(sum(null) / len(null), 3), 'p': round(p, 4)}, {}


def LL4():
    ss = [[g for g in s if g != 'GRA'] for s in GG.seqs_where(lambda r: True)]
    ss = [s for s in ss if len(s) >= 2]
    real, p, nm = FF.shuffle_within(ss, GG._asym)
    return p, 'The commodity order holds with grain removed', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(ss)}, {}


def LL5():
    lb = GG.lb_pairs()
    major = {}
    for (a, b), n in lb.items():
        if 'GRA' in (a, b):
            continue
        if n + lb[(b, a)] >= 3 and n > lb[(b, a)]:
            major[frozenset((a, b))] = (a, b)
    ss = [[g for g in s if g in GG.GOODS and g != 'GRA'] for s in GG.seqs_where(lambda r: True)]
    ss = [s for s in ss if len(s) >= 2]

    def agree(seqs):
        hit = tot = 0
        for s in seqs:
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    k = frozenset((s[i], s[j]))
                    if k in major:
                        tot += 1
                        hit += (s[i], s[j]) == major[k]
        return hit / max(1, tot)
    real, p, nm = FF.shuffle_within(ss, agree)
    return p, 'Agreement with Linear B order on pairs without grain', {'agreement': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4)}, {'Linear B orders used': ['<'.join(v) for v in major.values()]}


def split_site(fn_items, flag, value, text):
    res, ps = {}, []
    for name, pred in (('HT', lambda s: s == 'Haghia Triada'), ('other', lambda s: s != 'Haghia Triada')):
        items = fn_items(pred)
        r_, p, a, b = R.flag_compare(items, flag, value)
        res[name] = {'flagged': a, 'rest': b, 'p': round(p, 4)}
        ps.append(p)
    return max(ps), text, {**res, 'p (larger)': round(max(ps), 4)}, {}


def LL6():
    def items(pred):
        ws = sorted({tuple(w) for w in HH.word_tokens(lambda r: pred(r['site']))})
        return [(bool(HH.UNREAD.match(x)), i == 0) for w in ws for i, x in enumerate(w)]
    return split_site(items, lambda o: o[0], lambda o: o[1], 'Unread signs word-initial more often, at HT and elsewhere')


def LL7():
    def items(pred):
        return HH.singles(lambda r: r['support'] in B.ADMIN and pred(r['site']))
    return split_site(items, lambda x: x[0] == 'NI', lambda x: x[1], 'NI followed by a number more often, at HT and elsewhere')


def LL8():
    docs = json.loads((R.ROOT / 'data/sigla_decoded.json').read_text(encoding='utf-8'))
    kind = {d['name']: d.get('kind_raw') for d in docs}
    val = {}
    for d in docs:
        for a in d['attestations']:
            try:
                val[(d['name'], a['n'])] = a['values_raw']['fields'][0]['fields'][0]
            except (KeyError, IndexError, TypeError):
                pass
    rel, adm = set(), set()
    for d in json.loads((R.ROOT / 'data/sigla_words.json').read_text(encoding='utf-8')):
        k = kind.get(d['name']) or ''
        target = adm if k == 'Tablet' else (None if any(x in k for x in ('Nodule', 'Roundel', 'Sealing', 'sealing', 'nodule', 'roundel')) else rel)
        if target is None:
            continue
        for w in d['words']:
            vs = [val.get((d['name'], n)) for n in w['attestations']]
            if w['confident_signs'] and len(vs) >= 2 and all(isinstance(v, str) and re.fullmatch(r'[a-z]+[0-9]?', v) for v in vs):
                target.add(tuple(vs))
    rel, adm = sorted(rel - adm), sorted(adm - rel)
    f = lambda ws: sum(1 for w in ws if R.grid(w[0]) and R.grid(w[0])[0] == '') / max(1, len(ws))
    return cmp(rel, adm, f, 'Religious words vowel-initial more often (SigLA)')


def LL9():
    items = [rec for rec in FF.RECS if FF.SITE[rec['name']] == 'Haghia Triada' and len(rec['rows']) >= 5]
    import vigorous2 as W2
    r_, p, a, b = R.flag_compare(items, lambda r: r['total'], lambda r: W2.tau([x['q'] for x in r['rows']]))
    return p, 'Lists with a total more strictly largest-first (5+ entries)', {'with_total_tau': a, 'without': b, 'p': round(p, 4)}, {}


def LL10():
    return cmp(T.PRE, T.GRK_U, KK.rep_c, 'Pre-Greek consonant repetition against an unmatched Greek sample')


if __name__ == '__main__':
    R.run('round48', 'replications of the second loop', __doc__, [LL1, LL2, LL3, LL4, LL5, LL6, LL7, LL8, LL9, LL10])

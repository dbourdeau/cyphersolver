"""Round 47 (second loop, round 9 of 10): this loop's findings in the other records.

KK1  Linear B's commodity order agrees with Linear A's majority order more at Knossos than at Pylos.
KK2  Pre-Greek words repeat the consonant of neighbouring syllables more often than Greek words (length-matched).
KK3  Pre-Greek words repeat a whole syllable in succession more often than Greek words.
KK4  Eteocretan repeats neighbouring consonants more often than Greek.
KK5  Eteocretan repeats a whole syllable more often than Greek.
KK6  Pre-Greek words begin with an a-syllable more often than Greek words.
KK7  Knossos-only place names begin with a Q-row sign more often than Pylos-only ones.
KK8  Knossos-only common words begin with a Q-row sign more often than Pylos-only ones.
KK9  Knossos-only common words repeat neighbouring consonants more often than Pylos-only ones.
KK10 Pre-Greek words contain Z-row syllables more often than Greek words.
"""
from collections import Counter
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round37 as Z  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402

B, T, V = R.B, R.T, R.V
cons = P.cons
PRE, GRK = T.PRE + [], T.GRK + []
rep_c = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))
rep_s = lambda ws: sum(1 for w in ws if any(w[i] == w[i + 1] for i in range(len(w) - 1))) / max(1, len(ws))


def cmp(a, b, f, text):
    r, p, nm = R.compare(a, b, f)
    return p, text, {'target': round(f(a), 4), 'comparison': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def la_major():
    c = Counter()
    for rec in GG.VV.RECS:
        s = GG.seq_of(rec)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                c[(s[i], s[j])] += 1
    return {frozenset(k): k for k, n in c.items() if n > c[(k[1], k[0])]}


def lb_seqs(site):
    out = []
    for _, r in B.LB_RECS:
        if r.get('site') != site:
            continue
        seq = []
        for t in r.get('transliteratedWords', []):
            m = re.match(r'^\*?([A-Z]{3,})', t.strip())
            if m:
                g = {'HORD': 'GRA'}.get(m.group(1), m.group(1))
                if g in GG.GOODS and g not in seq:
                    seq.append(g)
        if len(seq) >= 2:
            out.append(seq)
    return out


def KK1():
    major = la_major()

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
    kn, py = lb_seqs('Knossos'), lb_seqs('Pylos')
    r, p, nm = R.compare(kn, py, agree)
    return p, 'Linear B commodity order agrees with Linear A more at Knossos than at Pylos', {'KN': round(agree(kn), 3), 'PY': round(agree(py), 3), 'p': round(p, 4), 'n': [len(kn), len(py)]}, {}


def KK2():
    return cmp(PRE, GRK, rep_c, 'Pre-Greek words repeat neighbouring consonants more often')


def KK3():
    return cmp(PRE, GRK, rep_s, 'Pre-Greek words repeat a whole syllable more often')


def KK4():
    a, b = Z.eteo()
    return cmp(a, b, rep_c, 'Eteocretan repeats neighbouring consonants more often')


def KK5():
    a, b = Z.eteo()
    return cmp(a, b, rep_s, 'Eteocretan repeats a whole syllable more often')


def KK6():
    f = lambda ws: sum(1 for w in ws if R.grid(w[0]) and R.grid(w[0])[1] == 'a') / len(ws)
    return cmp(PRE, GRK, f, 'Pre-Greek words begin with an a-syllable more often')


def topo(site_only):
    return [w for w in site_only if T.CAT.get(w) in ('toponym', 'ethnic') and T.clean(w) and len(w) >= 2]


def common(site_only):
    return [w for w in site_only if T.CAT.get(w) == 'other' and T.clean(w) and len(w) >= 2]


qinit = lambda ws: sum(1 for w in ws if cons(w[0]) == 'q') / max(1, len(ws))


def KK7():
    return cmp(topo(V.kn_only), topo(V.py_only), qinit, 'Knossos place names begin with Q more often')


def KK8():
    return cmp(common(V.kn_only), common(V.py_only), qinit, 'Knossos common words begin with Q more often')


def KK9():
    return cmp(common(V.kn_only), common(V.py_only), rep_c, 'Knossos common words repeat neighbouring consonants more often')


def KK10():
    return cmp(PRE, GRK, lambda ws: sum(1 for w in ws if any(cons(x) == 'z' for x in w)) / len(ws), 'Pre-Greek words contain Z-row syllables more often')


if __name__ == '__main__':
    R.run('round47', "this loop's findings in the other records", __doc__, [KK1, KK2, KK3, KK4, KK5, KK6, KK7, KK8, KK9, KK10])

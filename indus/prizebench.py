"""The prize-aligned bench (owner's review, 24 Sept 2026; PROGRESS.md 'Prize-aligned tiers'). Ranked as a panel would
judge a decipherment:

1 V  meaning score: share of sign tokens read as sense AND checked against outside evidence (strict: the copper-tablet
     animal equations; numerals reported beside it, their sense being the count itself).
2 C  positive-control gate: methods proposing sound values or readings must first recover a known answer (Linear B ->
     Greek). Lists the methods and whether they passed.
3 U  vault: share of tokens in texts never used to fix the values (B's new lines) read as sense with values fixed
     beforehand. Zero while no sound value has passed (progress.VALUES).
4 WORD task: hide a name body (the signs before the ending) in a held-out line; rank every name body seen in training
     by the model's probability of the whole line; top-1 / top-10 accuracy against a frequency baseline.
5 SIGN task: hide one sign of a held-out line; rank the 150 commonest training signs by the probability of the whole
     line (left-to-right plus right-to-left model, set 204); top-1 / top-5 accuracy against a frequency baseline.
"""
import math
from collections import Counter

import rtools as R
from famlm import M3, fit3

GATE = {'character-LM key scorer (set 205, lmkey.py)': "passed: Ventris's Linear B key beats 100 of 100 shuffles on held-out "
                                                      'lines with a Greek model; 9 of 100 shuffles as good with a Sanskrit model',
        'substitution-phonetics test (set 179)': 'passed: recovers Linear B syllable pairs as Greek-phonetic, p = 0.001',
        'picture-referent method (sets 233-235)': 'passed: on Linear B it qualifies 143 words against 2 by chance and recovers '
                                                  'known word-ideogram pairs (a-mo-ta ROTA, ko-wa MUL; set 234 key misnamed)',
        'blind key fitting per language (set 207, keyfit.py)': 'failed: fitted freely, Linear B fits Sanskrit best '
                                                               '(Greek last / third; 0 of 30 Ventris values recovered)',
        'world rebus search (set 181)': 'no Linear B control run',
        'published sign-value keys (key bench, sets 115, 135)': "failed: on Linear B, Ventris's values beat their shuffles in "
                                                                 'only 59-89% (linb_control.md: 11-41 of 100 shuffles as good)'}


def meaning(DL, anchors):
    tot = sum(len(t) for t in DL)
    strict = sum(1 for t in DL for g in t if g in anchors) / tot
    nums = sum(1 for t in DL for g in t if g in R.NUMS) / tot
    return strict, nums


def _lp(m, t, w):
    return sum(math.log2(max(sum(w[k] * r[k] for k in w), 1e-12)) for r in m.rows(t, True))


def sign_task(tr, te, keys, ncand=150):
    # set 204 (SB1-SB2): the line is scored left-to-right and right-to-left, log-probabilities summed
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    freq = Counter(g for t in tr for g in t)
    cands = [g for g, n in freq.most_common(ncand)]
    top1 = top5 = base1 = base5 = n = 0
    for t in te:
        for i, g in enumerate(t):
            sc = sorted(cands, key=lambda c: -(_lp(m, t[:i] + (c,) + t[i + 1:], w) + _lp(mb, tuple(reversed(t[:i] + (c,) + t[i + 1:])), wb)))
            n += 1
            top1 += sc[0] == g
            top5 += g in sc[:5]
            base1 += cands[0] == g
            base5 += g in cands[:5]
    return top1 / n, top5 / n, base1 / n, base5 / n, n


def word_task(tr, te, keys):
    w, _ = fit3(tr, keys)
    m = M3(tr)
    bodies = Counter()
    for t in tr:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            bodies[tuple(nm[0])] += 1
    cands = [b for b, c in bodies.most_common()]
    top1 = top10 = base1 = base10 = n = 0
    for t in te:
        nm = R.name_of(list(t))
        if not (nm and nm[0]):
            continue
        b = tuple(nm[0])
        j = next((j for j in range(len(t) - len(b) + 1) if tuple(t[j:j + len(b)]) == b), None)
        if j is None:
            continue
        pre, post = t[:j], t[j + len(b):]
        sc = sorted(cands, key=lambda c: -_lp(m, pre + c + post, w))
        n += 1
        top1 += sc[0] == b
        top10 += b in sc[:10]
        base1 += cands[0] == b
        base10 += b in cands[:10]
    return top1 / n, top10 / n, base1 / n, base10 / n, n


def referent_fixed(DL):
    """Set 233 (RF1-RF2): share of sign tokens in texts written on 3+ individually made pictured objects (copper,
    incised tablets) with one picture on 80%+ of them: the referent is fixed by the picture (not a reading)."""
    import rtools as R
    from predict_test200 import objects
    from predict_test233 import qualifying
    A, B, rowsA, recs, F = R.load_all()
    objs = objects(F, recs, ('TAB:C', 'TAB:I'))
    q = qualifying(objs)
    # set 237 (PL1-PL2): + tokens of qualifying sign pairs on the individually made tablets used
    from predict_test237 import merged, qual
    from predict_test254 import frag_objects
    # audit after set 247: part-texts merged; set 254: pictured damaged tablets' legible runs added (no pair across a gap)
    qp = {p: m for p, m in qual(merged(objs + frag_objects(('TAB:C', 'TAB:I')))).items() if '|' not in p}
    used = {t for t, m in objs}
    # set 243 (MR1-MR2): + qualifying pairs on moulded tablets (distinct texts = independent designs)
    mo = objects(F, recs, ('TAB:B',))
    qm = {p: m for p, m in qual(merged(mo + frag_objects(('TAB:B',)))).items() if '|' not in p}
    usedm = {t for t, m in mo}
    cov = 0
    for t in DL:
        if t in q:
            cov += len(t)
            continue
        mark = set()
        for pool, qq in ((used, qp), (usedm, qm)):
            if t in pool:
                for i in range(len(t) - 1):
                    if t[i:i + 2] in qq:
                        mark |= {i, i + 1}
        cov += len(mark)
    return cov / sum(len(t) for t in DL), len(q) + len(qp) + len(qm)

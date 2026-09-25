"""The decipherment progress metric, measured the same way every loop (PROGRESS.md).

S  structure: held-out bits per sign on a fixed 80/20 split (seed 2026) of the distinct lines of A + B, with the best
   model registered so far (MODEL below); also as a share of the unigram entropy explained.
R  roles: share of sign tokens (distinct lines) whose job is fixed by a tested rule (ROLE_RULES below).
M  meanings: share of sign tokens whose sign has an externally anchored meaning (ANCHORS below).
P  sound values: signs with a sound value that passed a registered held-out test (VALUES below).
L  language: candidate families not yet excluded by registered tests (FAMILIES below).

A component changes only when a registered set (PREDICTIONS.md) supports the change; the entry that changed it is
named in the comment beside it. Usage: python progress.py [label]  (appends a row to results/progress_log.tsv).
"""
import math
import os
import random
import sys
from collections import Counter

import rtools as R
from predict_test103 import CL
from predict_test125 import M2, fit, xent
from predict_test108 import genre
from predict_test161 import heading

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = {'keys': ['trik', 'pos', 'end', 'f4k'], 'kn': True}  # set 125; ftri 194, f4 199, f4k 210; trik 211. 'first' (213) withdrawn: it conditioned position 0 on itself, a leak (correction after set 223)
ANCHORS = {'749': 'markhor goat', '341': 'rhinoceros', '753': 'hare', '777': 'markhor goat / horned archer'}  # copper-tablet equations (fourth pass)
VALUES = {}                                                   # no sound value has passed a registered test
CAGED = {'226', '232', '153', '236', '241', '144', '393', '895', '466', '804', '878', '689'}  # set 184
DEPICT = ('human', 'tool', 'plant', 'fish')                   # set 178 (DC1-DC3, DC5): depiction classes confirmed by use on B
FAMILIES = {'Dravidian': 'open', 'Indo-Aryan': 'open', 'Burushaski / isolate': 'open', 'unknown (lost) language': 'open',
            'Sumerian': 'excluded (Q1, H7, TY1, LN1)', 'Elamite': 'excluded (head-initial order; Q1)',
            'Munda': 'excluded if the fish names are stars (class split, eleventh pass)'}


def data():
    A, B, rowsA, recs, F = R.load_all()
    DL = sorted({tuple(t) for t in A + B})
    rnd = random.Random(2026)
    ls = list(DL)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    return DL, ls[:k], ls[k:]


def structure(tr, te):
    from famlm import score3
    bits, w = score3(tr, te, MODEL['keys'], MODEL['kn'])
    uni = Counter(g for t in tr for g in list(t) + ['</s>'])
    n = sum(uni.values())
    h1 = -sum(v / n * math.log2(v / n) for v in uni.values())
    return bits, h1


def roles(DL):
    tot = got = 0
    by = Counter()
    for t in DL:
        num_before = False
        nm = R.name_of(list(t))
        # set 176 (LP5): body signs before the head of a parsed name are modifiers (head-final name grammar, H7, DT1-DT4)
        mods, bhead = set(), None
        # set 177 (VP7-VP8): bare lines (no ending) end in a name head 70% of the time; last sign = head, rest = modifiers
        if not nm and len(t) >= 2 and genre(t) == 'bare':
            bhead, mods = len(t) - 1, set(range(len(t) - 1))
        if nm and len(nm[0]) >= 2:
            off = next((j for j in range(len(t) - len(nm[0]) + 1) if tuple(t[j:j + len(nm[0])]) == nm[0]), None)
            if off is not None:
                mods = set(range(off, off + len(nm[0]) - 1))
        for i, g in enumerate(t):
            role = None
            if g in R.NUMS:
                role = 'numeral'
            elif g in R.END:
                role = 'ending'
            elif g in CL:
                role = 'closer'
            elif g in CAGED:
                role = 'caged marker'  # set 184 (CG1-CG2, CG6): the cage replaces the ending
            elif g in ('400', '90') and i > 0 and (t[i - 1] in R.END or t[i - 1] in CL):
                role = 'post-ending marker'
            elif i == 0 and heading(t):
                role = 'heading'
            elif (i + 1 < len(t) and t[i + 1] in R.END) or i == bhead:
                role = 'name head'
            elif num_before:
                role = 'counted sign'
            elif i in mods:
                role = 'name modifier'
            elif i + 1 < len(t) and t[i + 1] in R.NUMS and (i == 0 or t[i - 1] not in R.NUMS) and genre(t) == 'count':
                role = 'count label'  # set 215 (CT1-CT3): the slot before a count is restricted (A, B; also without the heading)
            num_before = g in R.NUMS
            tot += 1
            if role:
                got += 1
                by[role] += 1
    return got / tot, by, tot


def meanings(DL):
    tot = sum(len(t) for t in DL)
    n = sum(1 for t in DL for g in t if g in R.NUMS or g in ANCHORS)
    return n / tot


def meanings_plus(DL):
    from predict_test178 import depiction
    dep = depiction()
    tot = sum(len(t) for t in DL)
    n = sum(1 for t in DL for g in t if g in R.NUMS or g in ANCHORS or dep.get(g) in DEPICT)
    return n / tot


def grammar_coverage(DL):
    # set 191: G = share of distinct lines fully parsed by grammar.py (A lines = progress.py's DL; B = M77 additions)
    from grammar import coverage, heads_from
    from signs import load
    heads = heads_from(DL)
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    return coverage(DL, heads), coverage(DB, heads)


def grammar_margin(DL):
    # set 193: G margin = share of real lines parsed by G2 minus share of the same lines parsed after shuffling
    # set 216 (GL1-GL3): + LABEL-COUNT, labels = A's ten commonest pre-count signs
    from grammar import head_stats, heads_from, lexical, margin, parse11
    from predict_test215 import slots
    from signs import load
    heads = heads_from(DL)
    hc, mc = head_stats(DL)
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    DA = sorted({tuple(t) for t in R.load_all()[0]})
    labels = {g for g, v in Counter(sl[0] for sl in (slots(t) for t in DA if genre(t) == 'count') if sl).most_common(10)}
    occ = Counter(g for t in DA for g in t)
    hd = Counter(t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0)
    low = {g for g in occ if occ[g] >= 3 and hd[g] / occ[g] < 0.05 and lexical(g)}
    last = Counter(t[-1] for t in DA)
    endp = {g for g in occ if occ[g] >= 5 and last[g] / occ[g] >= 0.5 and lexical(g)}
    first = Counter(t[0] for t in DA)
    openp = {g for g in occ if occ[g] >= 5 and first[g] / occ[g] >= 0.5 and lexical(g)}
    f = lambda t: parse11(t, heads, hc, mc, labels, low, endp, openp) is not None  # sets 221 (EDGE-DOUBLE), 222 (CAGED-POST), 250 (LOW-POST), 261 (CAGE-OPEN), 262 (END-PRONE), 263 (BODY-400, HEADING-BODY), 264 (OPEN-PRONE)
    return margin(DL, f), margin(DB, f)


def main(label='measure'):
    DL, tr, te = data()
    bits, h1 = structure(tr, te)
    r, by, tot = roles(DL)
    m = meanings(DL)
    mp = meanings_plus(DL)
    p = len(VALUES)
    ga, gb = grammar_coverage(DL)
    ma, mb = grammar_margin(DL)
    from lbench import world_strict
    lw, lg = world_strict()  # sets 196 (LT1-LT3), 220 (LS1-LS2, no prefixes): world language groups the Indus profile excludes
    open_f = [f for f, s in FAMILIES.items() if s == 'open']
    # Indus-prize tiers (PROGRESS.md; prizebench.py)
    from prizebench import GATE, meaning, sign_task, word_task
    vs, vn = meaning(DL, ANCHORS)
    from prizebench import referent_fixed
    vr, nq = referent_fixed(DL)
    gate = sum(v.startswith('passed') for v in GATE.values())
    u = 0.0 if not VALUES else float('nan')
    w1, w10, wb1, wb10, wn = word_task(tr, te, MODEL['keys'])
    s1, s5, sb1, sb5, sn = sign_task(tr, te, MODEL['keys'])
    print('Tier 1 V  checked meaning: %.3f%% of tokens (numerals %.1f%%); referent fixed by the picture (not read) %.2f%% (%d texts, set 233)' % (100 * vs, 100 * vn, 100 * vr, nq))
    print('Tier 2 C  positive-control gate: %d of %d methods passed' % (gate, len(GATE)))
    print('Tier 3 U  vault: %.1f%%' % (100 * u))
    print('Tier 6 WORD top-1 %.1f%% top-10 %.1f%% (frequency %.1f%% / %.1f%%; %d names)' % (100 * w1, 100 * w10, 100 * wb1, 100 * wb10, wn))
    print('Tier 7 SIGN top-1 %.1f%% top-5 %.1f%% (frequency %.1f%% / %.1f%%; %d signs)' % (100 * s1, 100 * s5, 100 * sb1, 100 * sb5, sn))
    print('S  structure: %.3f bits/sign held out (unigram %.3f; %.1f%% explained)' % (bits, h1, 100 * (h1 - bits) / h1))
    print('R  roles: %.1f%% of %d tokens (%s)' % (100 * r, tot, ', '.join('%s %d' % kv for kv in by.most_common())))
    print('M  meanings: %.1f%% of tokens anchored; M+ with depiction classes confirmed by use %.1f%%' % (100 * m, 100 * mp))
    print('G  grammar: %.1f%% of distinct lines parsed (B check %.1f%%); G margin over shuffled lines %.1f points (B %.1f)' % (100 * ga, 100 * gb, 100 * ma, 100 * mb))
    print('P  sound values: %d' % p)
    print('L  language: %d families open (%s); L world: %.1f%% of WALS genera excluded (Grambank %.1f%% of families)' % (len(open_f), ', '.join(open_f), 100 * lw, 100 * lg))
    row = '\t'.join([label, '%.3f' % bits, '%.1f' % (100 * (h1 - bits) / h1), '%.1f' % (100 * r), '%.1f' % (100 * m), str(p),
                     str(len(open_f)), '%.1f' % (100 * mp), '%.1f' % (100 * ga), '%.1f' % (100 * gb), '%.1f' % (100 * ma), '%.1f' % (100 * mb), '%.1f' % (100 * lw), '%.1f' % (100 * lg),
                     '%.3f' % (100 * vs), str(gate), '%.1f' % (100 * u), '%.1f' % (100 * w10), '%.1f' % (100 * s1), '%.1f' % (100 * s5), '%.2f' % (100 * vr)])
    log = os.path.join(HERE, 'results', 'progress_log.tsv')
    head = 'label\tS_bits\tS_explained_pct\tR_roles_pct\tM_meanings_pct\tP_values\tL_open\tMplus_pct\tG_pct\tG_B_pct\tGmargin_A\tGmargin_B\tLworld_WALS\tLworld_GB\tV_checked_pct\tC_gate\tU_vault_pct\tWORD_top10_pct\tSIGN_top1_pct\tSIGN_top5_pct\tV_referent_pct'
    old = open(log, encoding='utf-8').read().splitlines()[1:] if os.path.exists(log) else []
    with open(log, 'w', encoding='utf-8') as f:
        f.write(head + '\n')
        for x in old:
            f.write(x + '\t' * max(0, 20 - x.count('\t')) + '\n')
        f.write(row + '\n')
    return bits, r, m, p, len(open_f)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'measure')

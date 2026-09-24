"""Hundred-and-sixty-third registered prediction set (PREDICTIONS.md, LM1-LM10): length-matched and shuffled baselines
for the capture-recapture profiles (Indus, Linear B, Ur III). Writes results/predict_test163.md."""
import csv
import json
import os
import random
from collections import Counter

import predict_test13 as T
import rtools as R
import ur3_seals
from predict_test152 import LINB, classes
from predict_test157 import kind, profile

random.seed(183)
N = 1000


def prof_sets(a, b):
    """Profile from two {item: count} Counters."""
    return profile({'a': a, 'b': b})


def shuffled_shared(a, b, n=N):
    """a, b: sets of tuples. Shuffle units within each catch keeping item lengths; shared counts."""
    out = []
    la, lb = [len(x) for x in a], [len(x) for x in b]
    ua, ub = [u for x in a for u in x], [u for x in b for u in x]
    for _ in range(n):
        random.shuffle(ua)
        random.shuffle(ub)
        sa, sb, i, j = set(), set(), 0, 0
        for L in la:
            sa.add(tuple(ua[i:i + L]))
            i += L
        for L in lb:
            sb.add(tuple(ub[j:j + L]))
            j += L
        out.append(len(sa & sb))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-third registered predictions: length-matched and shuffled baselines', 'predict_test163')
    cities = ('Mohenjo-daro', 'Harappa')
    ind = {c: Counter() for c in cities}
    ind_e = {e: {c: set() for c in cities} for e in ('740', '520')}
    lines3 = {c: Counter() for c in cities}
    for r in F:
        c = recs[r['sealid']][3]
        if r['type'].startswith('SEAL') and c in cities:
            for b, e in {x for x in R.names_in(r) if x[0]}:
                ind[c][b + (e,)] += 1
                ind_e[e][c].add(b + (e,))
            for ln in {tuple(l_) for l_ in r['seq'] if len(l_) == 3}:
                lines3[c][ln] += 1
    site = {}
    for ln in open(os.path.join(LINB, 'corpus_damos_documents.jsonl'), encoding='utf-8'):
        d = json.loads(ln)
        site[d['id']] = d['site']
    per, tit = classes()
    lb = {'Knossos': Counter(), 'Pylos': Counter()}
    seen = set()
    with open(os.path.join(LINB, 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            s = site.get(r['doc_id'])
            if s in lb and r['word'] in per and r['status'] == 'complete' and r['uncertain'] == '0' and r['erased'] == '0' and r['badsign'] == '0':
                if (r['doc_id'], r['word']) not in seen:
                    seen.add((r['doc_id'], r['word']))
                    lb[s][tuple(r['word'].split('-'))] += 1
    U = ur3_seals.load()
    leg = {}
    for (text, seal), o in U.items():
        leg.setdefault(tuple(tuple(l_) for l_ in o['lines']), set()).add(o['site'])
    ur_leg = {'Umma': Counter(), 'Girsu': Counter()}
    ur_own = {'Umma': Counter(), 'Girsu': Counter()}
    for lg, ss in leg.items():
        flat = tuple(cf for l_ in lg for cf, pos in l_)
        own = next((cf for cf, pos in lg[0] if pos == 'PN'), None) if lg else None
        for s in ss:
            if s in ur_leg:
                ur_leg[s][flat] += 1
                if own:
                    ur_own[s][(own,)] += 1
    byL = lambda d, L: {k: Counter({x: n for x, n in v.items() if len(x) == L}) for k, v in d.items()}
    pr = lambda d: prof_sets(*d.values())
    res = {}
    for key, L in (('LM1', 3), ('LM2', 4)):
        pi, pl = pr(byL(ind, L)), pr(byL(lb, L))
        res[L] = (pi, pl)
        q = pi['ratio'] / max(1e-9, pl['ratio'])
        rd.rec(key, 'at %d units, Indus names like Linear B persons' % L, 'Indus %s ratio %.2f; Linear B %s ratio %.2f; quotient %.2f' % (
            pi['n'], pi['ratio'], pl['n'], pl['ratio'], q), 0.5 <= q <= 2)
    p2, po = pr(byL(ind, 2)), pr(ur_own)
    q = p2['ratio'] / po['ratio']
    rd.rec('LM3', 'Indus 2-sign names like Ur III owners', 'Indus %s ratio %.2f; Ur III owners %s ratio %.2f; quotient %.2f' % (p2['n'], p2['ratio'], po['n'], po['ratio'], q), 0.5 <= q <= 2)
    p3i, p3u = pr(lines3), pr(byL(ur_leg, 3))
    rd.rec('LM4', '3-unit texts are open in both', 'Indus 3-sign lines %s: %.2f, %.2f, %.2f -> %s; Ur III 3-lemma legends %s: %.2f, %.2f, %.2f -> %s' % (
        p3i['n'], p3i['ratio'], p3i['shared'], p3i['one'], kind(p3i), p3u['n'], p3u['ratio'], p3u['shared'], p3u['one'], kind(p3u)),
        kind(p3i) == kind(p3u) == 'person-like')

    def shuf(key, title, d):
        a, b = [set(v) for v in d.values()]
        real = len(a & b)
        sh = shuffled_shared(a, b)
        below = sum(x < real for x in sh)
        m = sum(sh) / len(sh)
        rd.rec(key, title, 'real shared %d; shuffled mean %.1f (max %d); real above %d of %d; excess %.1f' % (real, m, max(sh), below, len(sh), real / max(1e-9, m)), below >= 0.95 * len(sh))
        return real / max(1e-9, m), real, m
    ex_i = shuf('LM5', 'Indus names recur beyond combinatorics', ind)
    shuf('LM6', 'Linear B persons recur beyond combinatorics', lb)
    shuf('LM7', 'Ur III legends recur beyond combinatorics', ur_leg)
    exs = {}
    for e in ('740', '520'):
        a, b = ind_e[e].values()
        sh = shuffled_shared(a, b, 300)
        exs[e] = len(a & b) / max(1e-9, sum(sh) / len(sh))
    rd.rec('LM8', '520 names recur more than 740 names', 'excess 520 %.1f, 740 %.1f' % (exs['520'], exs['740']), exs['520'] > exs['740'])
    a, b = [set(v) for v in ur_own.values()]
    sho = shuffled_shared(a, b, 100)
    ex_o = len(a & b) / max(1e-9, sum(sho) / len(sho))
    rd.rec('LM9', 'Indus names recur less than Sumerian names', 'excess Indus %.1f, Ur III owners %.1f (owners are single lemmas: shuffling cannot change them, so the owner excess is 1 by construction)' % (
        ex_i[0], ex_o), ex_i[0] < ex_o)
    si = [(L, pr(byL(ind, L))['shared']) for L in range(2, 7)]
    sl = [(L, pr(byL(lb, L))['shared']) for L in range(2, 6)]
    ri = T.spearman([L for L, s in si], [s for L, s in si])
    rl = T.spearman([L for L, s in sl], [s for L, s in sl])
    rd.rec('LM10', 'sharing falls with length', 'Indus %s (Spearman %.2f); Linear B %s (Spearman %.2f)' % (
        ', '.join('%d: %.2f' % x for x in si), ri, ', '.join('%d: %.2f' % x for x in sl), rl), ri < 0 and rl < 0)
    rd.finish()


if __name__ == '__main__':
    main()

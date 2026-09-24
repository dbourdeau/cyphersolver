"""Restoring broken inscriptions, scored against intact copies (fuller ICIT-derived corpus; see icit_full.py).

A prize criterion is that a reading 'predict unknown signs in broken texts'. Here the answer key is real: many
texts exist in several copies, so a broken copy often has an intact twin.

R1  Cases: single-line texts broken at exactly one edge (reading start or reading end), no missing sign inside,
    2+ legible signs L. The true lost sign next to the break comes from intact lines that end with L (break at
    the start) or begin with L (break at the end) and are longer than L; the commonest such sign is the answer.
R2  Prediction without parallels: a model trained on intact lines that do NOT contain L anywhere (so the answer
    cannot be looked up). Predictors: (a) the commonest sign in that position (start / end of a line); (b) the
    neighbour: the sign most often found next to L's edge sign on that side; (c) (b) plus the line position
    (e.g. after a name-final sign at the reading end, the ending grid); (d) an interpolation of the two edge signs
    (trigram), the neighbour and the edge prior. Top-1 and top-5 accuracy.
R3  The same with parallels allowed (the standard method): how often an intact line in the rest of the corpus
    supplies the answer (a check that the answer key is consistent).

Usage: python restore.py path/to/icit_full_records_indusscript_net.csv
Writes results/restore.md.
"""
import os
import sys
from collections import Counter, defaultdict

import icit_full

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def contains(t, L):
    n = len(L)
    return any(t[i:i + n] == L for i in range(len(t) - n + 1))


def main(path):
    rows = icit_full.objects(path)
    intact = []
    for r in rows:
        for ln in r['raw']:
            if not (ln['broken_start'] or ln['broken_end'] or ln['gap']) and len(ln['signs']) >= 2:
                intact.append(tuple(ln['signs']))
    cases = []
    for r in rows:
        if len(r['raw']) != 1:
            continue
        ln = r['raw'][0]
        if ln['gap'] or ln['broken_start'] == ln['broken_end']:
            continue
        L = tuple(ln['signs'])
        if len(L) < 2:
            continue
        side = 'start' if ln['broken_start'] else 'end'
        truths = Counter()
        for t in intact:
            if len(t) > len(L):
                if side == 'start' and t[-len(L):] == L:
                    truths[t[-len(L) - 1]] += 1
                if side == 'end' and t[:len(L)] == L:
                    truths[t[len(L)]] += 1
        if truths:
            cases.append((r['cisi'] or r['sealid'], side, L, truths.most_common(1)[0][0], len(truths)))
    say('# Restoring broken inscriptions, scored against intact copies')
    say()
    say('- intact lines of 2+ signs: %d; broken single-line texts with an intact twin that fixes the lost sign: %d '
        '(broken at the reading start %d, at the end %d; with more than one candidate among the twins %d).' % (
            len(intact), len(cases), sum(1 for c in cases if c[1] == 'start'), sum(1 for c in cases if c[1] == 'end'),
            sum(1 for c in cases if c[4] > 1)))
    say()
    res = defaultdict(lambda: [0, 0, 0])
    detail = Counter()
    for cid, side, L, truth, _ in cases:
        train = [t for t in intact if not contains(t, L)]
        pos = Counter(t[0] if side == 'start' else t[-1] for t in train)
        nb = Counter()
        nbpos = Counter()
        edge = L[0] if side == 'start' else L[-1]
        for t in train:
            for i in range(len(t)):
                if side == 'start' and i + 1 < len(t) and t[i + 1] == edge:
                    nb[t[i]] += 1
                    if i == 0:
                        nbpos[t[i]] += 1
                if side == 'end' and i > 0 and t[i - 1] == edge:
                    nb[t[i]] += 1
                    if i == len(t) - 1:
                        nbpos[t[i]] += 1
        # (d) interpolated model: two edge signs (trigram), one (bigram), line-edge prior
        e2 = L[:2] if side == 'start' else L[-2:]
        tri = Counter()
        for t in train:
            for i in range(len(t) - 2):
                if side == 'start' and tuple(t[i + 1:i + 3]) == tuple(e2):
                    tri[t[i]] += 1
                if side == 'end' and tuple(t[i:i + 2]) == tuple(e2):
                    tri[t[i + 2]] += 1
        sc = Counter()
        nt, nn, npp = sum(tri.values()), sum(nb.values()), sum(pos.values())
        for g in set(tri) | set(nb) | set(pos):
            sc[g] = (0.5 * tri[g] / nt if nt else 0) + (0.35 * nb[g] / nn if nn else 0) + 0.15 * pos[g] / max(npp, 1)
        preds_d = [g for g, _ in sc.most_common(5)]
        preds = {'(a) commonest sign at that edge': [g for g, _ in pos.most_common(5)],
                 '(b) commonest neighbour of the edge sign': [g for g, _ in nb.most_common(5)],
                 '(c) neighbour at the line edge': [g for g, _ in (nbpos or nb).most_common(5)],
                 '(d) two edge signs + neighbour + edge (interpolated)': preds_d}
        for k, p in preds.items():
            res[k][0] += bool(p) and p[0] == truth
            res[k][1] += truth in p
            res[k][2] += 1
        if side == 'end':
            detail['end: truth is an ending (740/520)'] += truth in ('740', '520')
            detail['end: truth is an ending and (c) gets it'] += truth in ('740', '520') and bool(preds['(c) neighbour at the line edge']) and preds['(c) neighbour at the line edge'][0] == truth
        else:
            detail['start: truth is a heading sign'] += truth in ('817', '820', '861', '2', '60', '1')
            detail['start: truth is a heading sign and (c) gets it'] += truth in ('817', '820', '861', '2', '60', '1') and bool(preds['(c) neighbour at the line edge']) and preds['(c) neighbour at the line edge'][0] == truth
    say('## R2 Prediction without parallels (texts containing the legible part withheld)')
    say()
    say('| predictor | top-1 | top-5 |')
    say('|---|---|---|')
    for k, (a, b, n) in res.items():
        say('| %s | %d of %d (%.0f%%) | %d (%.0f%%) |' % (k, a, n, 100 * a / n, b, 100 * b / n))
    say()
    say('- %s.' % '; '.join('%s: %d' % kv for kv in detail.items()))
    say()
    say('## R3 With parallels (the standard method)')
    say()
    say('- By construction every case has an intact twin in the corpus; a restorer with the whole corpus would '
        'recover the sign in all %d, choosing the commonest continuation where twins differ (%d cases).' % (
            len(cases), sum(1 for c in cases if c[4] > 1)))
    say()
    say('Examples: %s.' % '; '.join('%s (%s broken) %s -> %s' % (c, s, ' '.join(L), t) for c, s, L, t, _ in cases[:10]))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'restore.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])

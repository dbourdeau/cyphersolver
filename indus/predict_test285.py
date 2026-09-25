"""Two-hundred-and-eighty-fifth registered prediction set (PREDICTIONS.md, CB1-CB4): decipherment loop 110, the tier 3
restorations (sets 283-284, 49 cases) against a context baseline instead of the frequency baseline. Context baseline:
the commonest sign seen between the gap's two neighbours in the copy-free training lines (line edges as neighbours),
else the commonest sign after the left neighbour, else before the right neighbour, else the commonest sign. Lexical
cases: M77 reading is not a heading sign (817 / 820 / 861), not 740 / 520 / 400 / 90, not a closer. The model's
predictions are those recorded by sets 283-284 (re-derived here from the same procedure).
Writes results/predict_test285.md."""
import csv
import os
from collections import Counter, defaultdict

import rtools as R
from predict_test103 import CL
from predict_test283 import copy_of
from progress import data

HERE = os.path.dirname(os.path.abspath(__file__))


def ctx_pred(train, t, k):
    s = ('<s>',) + t + ('</s>',)
    L, Rn = s[k], s[k + 2]
    mid, aft, bef, uni = Counter(), Counter(), Counter(), Counter()
    for u in train:
        v = ('<s>',) + tuple(u) + ('</s>',)
        for i in range(1, len(v) - 1):
            uni[v[i]] += 1
            if v[i - 1] == L:
                aft[v[i]] += 1
                if v[i + 1] == Rn:
                    mid[v[i]] += 1
            if v[i + 1] == Rn:
                bef[v[i]] += 1
    for c in (mid, aft, bef, uni):
        if c:
            return c.most_common(1)[0][0]


def main():
    rd = R.Round('Two-hundred-and-eighty-fifth registered predictions: decipherment loop 110, tier 3 restorations against a context baseline', 'predict_test285')
    DL, tr, te = data()
    cases = []
    with open(os.path.join(HERE, 'results', 'predict_test283.md'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('- ') and ': M77 ' in ln and 'predicted' in ln:
                head, rest = ln[2:].split(': M77 ')
                text = ' '.join(head.split()[1:]) if not head.startswith('- ') else head[2:]
                g = rest.split(';')[0]
                pred = rest.split('predicted ')[1].strip().rstrip('.').split()
                cases.append((tuple(text.split()), g, pred))
    with open(os.path.join(HERE, 'results', 'restoration_m77_new.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            cases.append((tuple(r['text_with_gap'].split()), r['m77'], r['predicted_top5'].split()))
    heads = {'817', '820', '861'}
    m1 = c1 = ml = cl = nl = 0
    for t, g, pred in cases:
        k = t.index('???')
        train = [u for u in DL if not copy_of(t, k, u)]
        cp = ctx_pred(train, t, k)
        m1 += pred[0] == g
        c1 += cp == g
        lex = g not in heads and g not in ('740', '520', '400', '90') and g not in CL
        if lex:
            nl += 1
            ml += pred[0] == g
            cl += cp == g
    n = len(cases)
    rd.say('- %d cases (%d lexical).' % (n, nl))
    rd.say()
    rd.rec('CB1', 'model top-1 beats the context baseline on all cases', '%d against %d of %d' % (m1, c1, n), m1 > c1)
    rd.rec('CB2', 'and on the lexical cases', '%d against %d of %d' % (ml, cl, nl), ml > cl)
    rd.rec('CB3', 'model top-1 is 20%+ on the lexical cases', '%d of %d' % (ml, nl), ml >= 0.2 * nl)
    rd.rec('CB4', 'progress rule: none (validation of the tier 3 line; a failure of CB1 downgrades it)', 'CB1 %s' % (m1 > c1), False)
    rd.finish()


if __name__ == '__main__':
    main()

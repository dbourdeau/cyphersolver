"""Two-hundred-and-thirty-fourth registered prediction set (PREDICTIONS.md, LR1-LR4): decipherment loop 59, the set-233
picture-referent method on Linear B (words and ideograms), against known commodity words. Writes
results/predict_test234.md."""
import os
import random
import re
from collections import Counter, defaultdict

import lang_names as L
import rtools as R

MEASURE = set('T M Z S N L P O X V Q'.split())
KNOWN = {'a-mo': 'ROTA', 'i-qo': 'EQU', 'pa-ka-na': '*233', 'e-ke-a': '*254', 'sa-sa-ma': 'SA', 'ko-ri-ja-do-no': 'KO', 'i-qi-ja': 'BIG'}


def lines():
    out = []
    for ln in open(os.path.join(L.SP, 'linb', 'corpus_damos_lines.txt'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if len(p) < 3:
            continue
        toks = p[2].split()
        words = [t for t in toks if re.match(r'^[a-z0-9*]+(-[a-z0-9*]+)+$', t)]
        ideo = None
        for t in toks:
            if re.match(r'^[A-Z*][A-Z0-9*+]*$', t) and not t.isdigit():
                b = t.split('+')[0]
                if b in MEASURE or (b.isalpha() and len(b) <= 2):
                    continue
                ideo = b
                break
        if ideo and words:
            out.append((words, ideo))
    return out


def qualify(ls):
    occ = defaultdict(list)
    for ws, i in ls:
        for w in set(ws):
            occ[w].append(i)
    out = {}
    for w, ii in occ.items():
        if len(ii) >= 3:
            k, v = Counter(ii).most_common(1)[0]
            if v / len(ii) >= 0.8:
                out[w] = k
    return out


def main():
    rd = R.Round('Two-hundred-and-thirty-fourth registered predictions: decipherment loop 59, a Linear B control for the picture-referent method', 'predict_test234')
    ls = lines()
    q = qualify(ls)
    rd.say('- lines with words and a non-measure ideogram: %d; qualifying word types: %d.' % (len(ls), len(q)))
    rd.say('- known pairs: %s.' % '; '.join('%s / %s -> %s' % (w, i, q.get(w, 'not qualifying')) for w, i in KNOWN.items()))
    rd.say()
    rec = [w for w, i in KNOWN.items() if q.get(w) == i]
    rd.rec('LR1', '3+ of 7 known pairs recovered', 'recovered: %s' % (', '.join(rec) or 'none'), len(rec) >= 3)
    ideos = [i for ws, i in ls]
    rnd = random.Random(234)
    nulls = []
    for _ in range(1000):
        rnd.shuffle(ideos)
        nulls.append(len(qualify([(ws, i) for (ws, _), i in zip(ls, ideos)])))
    q95 = sorted(nulls)[949]
    rd.rec('LR2', 'more qualifying words than with shuffled ideograms', '%d against shuffles median %d, 95th percentile %d' % (len(q), sorted(nulls)[500], q95), len(q) > q95)
    wrong = [w for w, i in KNOWN.items() if w in q and q[w] != i]
    rd.rec('LR3', 'no known word with a wrong ideogram', 'wrong: %s' % (', '.join('%s -> %s' % (w, q[w]) for w in wrong) or 'none'), not wrong)
    rd.rec('LR4', 'progress rule', 'LR1 %s, LR2 %s' % (len(rec) >= 3, len(q) > q95), len(rec) >= 3 and len(q) > q95)
    rd.finish()


if __name__ == '__main__':
    main()

"""Map ICIT glyph ids to Mahadevan (M77) sign numbers by aligning the texts the two
corpora share (most objects are in both, transcribed independently).

Hard EM: start from a weak frequency prior plus the jar anchor (740 = MSg342); each
round, every ICIT line is matched to the M77 line of the same length that scores best
under the current sign map, confident matches (clear margin over the runner-up)
re-estimate the map, repeat. Writes data/icit_m77_map.tsv (glyph, M77 sign, pairs,
share) and prints the agreement.

Usage: python align_m77.py path/to/m77_indusscript_real_corpus.csv
"""
import csv
import math
import os
import sys
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))


def main(path):
    icit = [ln for r in load() for ln in r['seq'] if len(ln) >= 3]
    m77 = []
    for r in csv.DictReader(open(path, encoding='utf-8')):
        s = r['sign_sequence'].split()
        if len(s) >= 3 and 'MSg0' not in s:
            m77.append((r['inscription_id'], s))
    by_len = defaultdict(list)
    for tid, s in m77:
        by_len[len(s)].append((tid, s))
    fi = Counter(g for ln in icit for g in ln)
    fm = Counter(g for _, s in m77 for g in s)
    ni, nm = sum(fi.values()), sum(fm.values())

    # prior: signs of similar relative frequency are more likely to correspond
    def prior(i, m):
        return -abs(math.log((fi[i] / ni) / (fm[m] / nm)))

    logp = {}
    for i in fi:
        row = {m: prior(i, m) for m in fm}
        z = math.log(sum(math.exp(v) for v in row.values()))
        logp[i] = {m: v - z for m, v in row.items()}
    # anchors from line sets repeated many times in both corpora (copper and Harappa
    # tablets), matched by length, repeat count and jar position:
    #   ICIT 806 845 61 407 850 900 740 (x10)  = M77 389 407 124 169 373 287 342 (x10)
    #   ICIT 235 705 33 845 407 321 407 (x12)  = M77 65 336 89 407 169 183 169 (x10)
    #   ICIT 503 615 752 740 (x29)             = M77 204 245 358 342 (x19)
    #   ICIT 176 740 400 (x29)                 = M77 48 342 176 (x41)
    anchors = {'740': '342', '806': '389', '845': '407', '61': '124', '407': '169',
               '405': '169', '850': '373', '900': '287', '235': '65', '705': '336',
               '33': '89', '321': '183', '503': '204', '615': '245', '752': '358',
               '176': '48', '400': '176'}
    for i, m in anchors.items():
        logp[i] = {x: (0.0 if x == 'MSg' + m else -12.0) for x in fm}
    floor = -12.0

    for it in range(12):
        pairs = Counter()
        kept = 0
        for ln in icit:
            best = second = (-1e9, None)
            for tid, s in by_len[len(ln)]:
                sc = sum(logp[a].get(b, floor) for a, b in zip(ln, s))
                if sc > best[0]:
                    best, second = (sc, (tid, s)), best
                elif sc > second[0]:
                    second = (sc, (tid, s))
            if best[1] and best[0] - second[0] > 2.0 and best[0] / len(ln) > -3.0:
                kept += 1
                for a, b in zip(ln, best[1][1]):
                    pairs[a, b] += 1
        # re-estimate with add-0.1 smoothing over the M77 signs seen with each glyph
        tot = Counter()
        for (a, b), c in pairs.items():
            tot[a] += c
        new = {}
        for i in fi:
            row = {m: floor for m in fm}
            for (a, b), c in pairs.items():
                if a == i:
                    row[b] = math.log((c + 0.1) / (tot[i] + 0.1 * len(fm)))
            if tot[i] == 0:
                row = logp[i]
            new[i] = row
        logp = new
        agree = sum(max((c for (a, b), c in pairs.items() if a == i), default=0) for i in tot)
        print('round %d: %d confident line matches, %d aligned signs, %.1f%% on the top M77 sign'
              % (it + 1, kept, sum(tot.values()), 100 * agree / max(1, sum(tot.values()))))

    with open(os.path.join(HERE, 'data', 'icit_m77_map.tsv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['icit', 'm77', 'pairs', 'share', 'icit_count'])
        for i in sorted(tot, key=lambda g: -tot[g]):
            m, c = max(((b, c) for (a, b), c in pairs.items() if a == i), key=lambda x: x[1])
            w.writerow([i, m, c, '%.2f' % (c / tot[i]), fi[i]])


if __name__ == '__main__':
    main(sys.argv[1])

"""Blind restoration (set 255): predict each single illegible sign (ICIT 000) inside a line with intact edges, with the
two-direction SIGN model trained on all clean distinct lines; write the top 5 to results/restoration_predictions.tsv
without printing them, and a worklist (no predictions) to results/restoration_worklist.tsv."""
import csv
import os
from collections import Counter

import icit_full
import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data


def gaps():
    A, B, rowsA, recs, F = R.load_all()
    icit_full.LINES_REVERSED = True
    out = []
    for rec in icit_full.records(R.FPATH):
        for li, ln in enumerate(icit_full.lines_of(rec[34])):
            s = ln['signs']
            if sum(1 for g in s if g is None) == 1 and '?' not in s:
                i = s.index(None)
                if 0 < i < len(s) - 1 and not ln['broken_start'] and not ln['broken_end']:
                    out.append((rec[0], rec[1], rec[3], rec[20], li, i, tuple(s)))
    return out


def main():
    DL, tr, te = data()
    keys = MODEL['keys']
    wf, _ = fit3(DL, keys)
    mf = M3(DL)
    rdl = [tuple(reversed(t)) for t in DL]
    wb, _ = fit3(rdl, keys)
    mb = M3(rdl)
    cands = [g for g, n in Counter(g for t in DL for g in t).most_common(150)]
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'results', 'restoration_predictions.tsv'), 'w', encoding='utf-8', newline='') as f, \
            open(os.path.join(here, 'results', 'restoration_worklist.tsv'), 'w', encoding='utf-8', newline='') as w:
        pf, pw = csv.writer(f, delimiter='\t', lineterminator='\n'), csv.writer(w, delimiter='\t', lineterminator='\n')
        pf.writerow(['id', 'line', 'pos', 'top1', 'top2', 'top3', 'top4', 'top5'])
        pw.writerow(['id', 'cisi', 'site', 'type', 'line', 'pos', 'text_with_gap'])
        for sid, cisi, site, typ, li, i, s in gaps():
            sc = {}
            for c in cands:
                u = s[:i] + (c,) + s[i + 1:]
                sc[c] = _lp(mf, u, wf) + _lp(mb, tuple(reversed(u)), wb)
            top = sorted(cands, key=lambda c: -sc[c])[:5]
            pf.writerow([sid, li, i] + top)
            pw.writerow([sid, cisi, site, typ, li, i, ' '.join('???' if g is None else g for g in s)])
    print('written')


if __name__ == '__main__':
    main()

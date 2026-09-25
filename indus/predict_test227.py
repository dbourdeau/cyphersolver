"""Two-hundred-and-twenty-seventh registered prediction set (PREDICTIONS.md, CS1-CS5): decipherment loop 52, the grammar
learned at one site scored on another (margin over shuffled lines). Writes results/predict_test227.md."""
from collections import Counter

import rtools as R
from grammar import head_stats, heads_from, margin, parse5
from predict_test108 import genre
from predict_test215 import slots


def learned(lines):
    H = heads_from(lines)
    hc, mc = head_stats(lines)
    labels = {g for g, v in Counter(s[0] for s in (slots(t) for t in lines if genre(t) == 'count') if s).most_common(10)}
    return lambda t: parse5(t, H, hc, mc, labels) is not None


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-seventh registered predictions: decipherment loop 52, one grammar across sites', 'predict_test227')
    by = {'MD': set(), 'H': set(), 'other': set()}
    for r in F:
        k = 'MD' if r['site'] == 'Mohenjo-daro' else ('H' if r['site'] == 'Harappa' else 'other')
        for ln in r['seq']:
            if ln:
                by[k].add(tuple(ln))
    by = {k: sorted(v) for k, v in by.items()}
    rd.say('- distinct lines: %s.' % ', '.join('%s %d' % (k, len(v)) for k, v in by.items()))
    rd.say()
    fmd, fh, fboth = learned(by['MD']), learned(by['H']), learned(by['MD'] + by['H'])
    m_md_h, m_h_md, m_both_o = margin(by['H'], fmd), margin(by['MD'], fh), margin(by['other'], fboth)
    w_md, w_h, w_both = margin(by['MD'], fmd), margin(by['H'], fh), margin(by['MD'] + by['H'], fboth)
    rd.rec('CS1', 'Mohenjo-daro grammar on Harappa', 'margin %.1f points (within Mohenjo-daro %.1f)' % (100 * m_md_h, 100 * w_md), m_md_h >= 0.25)
    rd.rec('CS2', 'Harappa grammar on Mohenjo-daro', 'margin %.1f points (within Harappa %.1f)' % (100 * m_h_md, 100 * w_h), m_h_md >= 0.25)
    rd.rec('CS3', 'both cities on the other sites', 'margin %.1f points (within %.1f)' % (100 * m_both_o, 100 * w_both), m_both_o >= 0.20)
    gaps = [w_md - m_md_h, w_h - m_h_md, w_both - m_both_o]
    rd.rec('CS4', 'cross-site within 10 points of within-site', 'gaps %s points' % ', '.join('%.1f' % (100 * g) for g in gaps), all(g <= 0.10 for g in gaps))
    ok = m_md_h >= 0.25 and m_h_md >= 0.25 and m_both_o >= 0.20
    rd.rec('CS5', 'progress rule', 'CS1 %s, CS2 %s, CS3 %s' % (m_md_h >= 0.25, m_h_md >= 0.25, m_both_o >= 0.20), ok)
    rd.finish()


if __name__ == '__main__':
    main()

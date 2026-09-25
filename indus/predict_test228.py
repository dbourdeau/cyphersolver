"""Two-hundred-and-twenty-eighth registered prediction set (PREDICTIONS.md, OT1-OT5): decipherment loop 53, the grammar
learned on one object type or period scored on another. Writes results/predict_test228.md."""
import rtools as R
from grammar import margin
from predict_test196 import period
from predict_test227 import learned


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-twenty-eighth registered predictions: decipherment loop 53, one grammar across object types and periods', 'predict_test228')
    by = {}
    for r in F:
        ty = 'seal' if r['type'].startswith('SEAL') else ('tab' if r['type'].startswith('TAB') else 'other')
        per = period(recs[r['sealid']][8]) if r['site'] == 'Harappa' and r['sealid'] in recs else None
        for ln in r['seq']:
            if ln:
                by.setdefault(ty, set()).add(tuple(ln))
                if per:
                    by.setdefault(per, set()).add(tuple(ln))
    by = {k: sorted(v) for k, v in by.items()}
    fs, ft, fl = learned(by['seal']), learned(by['tab']), learned(by['late'])
    st, ts, le = margin(by['tab'], fs), margin(by['seal'], ft), margin(by['early'], fl)
    ss = margin(by['seal'], fs)
    rd.rec('OT1', 'seal grammar on tablets', 'margin %.1f points (%d lines)' % (100 * st, len(by['tab'])), st >= 0.20)
    rd.rec('OT2', 'tablet grammar on seals', 'margin %.1f points' % (100 * ts), ts >= 0.20)
    rd.rec('OT3', 'late Harappa grammar on early Harappa', 'margin %.1f points (%d lines)' % (100 * le, len(by['early'])), le >= 0.20)
    rd.rec('OT4', 'tablets are a different genre', 'seal -> seal %.1f, seal -> tablet %.1f points' % (100 * ss, 100 * st), ss - st >= 0.05)
    rd.rec('OT5', 'progress rule', 'OT1 %s, OT3 %s' % (st >= 0.20, le >= 0.20), st >= 0.20 and le >= 0.20)
    rd.finish()


if __name__ == '__main__':
    main()

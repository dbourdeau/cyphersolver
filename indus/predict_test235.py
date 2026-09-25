"""Two-hundred-and-thirty-fifth registered prediction set (PREDICTIONS.md, LD1-LD3): decipherment loop 60, the Linear B
referent control with a fresh key in DAMOS ideogram naming. Writes results/predict_test235.md."""
import rtools as R
from predict_test234 import lines, qualify

KEY = {'a-mo-ta': 'ROTA', 'e-ra-wa': 'OLIV', 'ko-wa': 'MUL', 'pa-we-a': '*146'}


def main():
    rd = R.Round('Two-hundred-and-thirty-fifth registered predictions: decipherment loop 60, the Linear B referent control in DAMOS naming', 'predict_test235')
    q = qualify(lines())
    rd.say('- pairs: %s.' % '; '.join('%s / %s -> %s' % (w, i, q.get(w, 'not qualifying')) for w, i in KEY.items()))
    rd.say()
    rec = [w for w, i in KEY.items() if q.get(w) == i]
    wrong = [w for w, i in KEY.items() if w in q and q[w] != i]
    rd.rec('LD1', '2+ of 4 recovered', 'recovered: %s' % (', '.join(rec) or 'none'), len(rec) >= 2)
    rd.rec('LD2', 'none with another ideogram', 'other: %s' % (', '.join('%s -> %s' % (w, q[w]) for w in wrong) or 'none'), not wrong)
    rd.rec('LD3', 'progress rule', 'LD1 %s' % (len(rec) >= 2), len(rec) >= 2)
    rd.finish()


if __name__ == '__main__':
    main()

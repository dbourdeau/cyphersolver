"""Hundred-and-eighty-eighth registered prediction set (PREDICTIONS.md, SX1-SX5): decipherment loop 13, more training text
for S. F's extra distinct lines added to progress.py's training lines; the fixed test lines unchanged. Writes
results/predict_test188.md."""
import rtools as R
from predict_test125 import M2, fit, xent
from progress import MODEL, data


def score(tr, te):
    w = fit(tr, MODEL['keys'], MODEL['kn'])
    m = M2(tr)
    return xent([r for t in te for r in m.rows(t, MODEL['kn'])], w)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-eighth registered predictions: decipherment loop 13, more training text for S', 'predict_test188')
    DL, tr, te = data()
    have = set(DL)
    tes = set(te)
    extra_all = sorted({tuple(ln) for r in F for ln in r['seq'] if ln} - have - tes)
    extra_seal = sorted({tuple(ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if ln} - have - tes)
    extra_nocu = sorted({tuple(ln) for r in F if r['type'] != 'TAB:C' for ln in r['seq'] if ln} - have - tes)
    rd.say('- training lines %d; test lines %d; extra F lines: all %d, seals %d, without copper %d.' % (len(tr), len(te), len(extra_all), len(extra_seal), len(extra_nocu)))
    rd.say()
    s0 = score(tr, te)
    s1 = score(tr + extra_all, te)
    rd.rec('SX1', 'all extra F lines', 'S %.3f -> %.3f (gain %.3f); threshold 0.03' % (s0, s1, s0 - s1), s0 - s1 >= 0.03)
    s2 = score(tr + extra_seal, te)
    rd.rec('SX2', 'extra seal lines only', 'S %.3f -> %.3f (gain %.3f); threshold 0.01' % (s0, s2, s0 - s2), s0 - s2 >= 0.01)
    seen0 = {g for t in tr for g in t}
    seen1 = seen0 | {g for t in extra_all for g in t}
    tt = [g for t in te for g in t]
    u0 = sum(g not in seen0 for g in tt) / len(tt)
    u1 = sum(g not in seen1 for g in tt) / len(tt)
    rd.rec('SX3', 'fewer unseen test signs', 'unseen %.2f%% -> %.2f%%' % (100 * u0, 100 * u1), (u0 - u1) >= 0.005)
    s4 = score(tr + extra_nocu, te)
    rd.rec('SX4', 'not only the copper tablets', 'S %.3f -> %.3f (gain %.3f); threshold 0.02' % (s0, s4, s0 - s4), s0 - s4 >= 0.02)
    rd.rec('SX5', 'progress rule', 'SX1 gain %.3f' % (s0 - s1), s0 - s1 >= 0.03)
    rd.finish()


if __name__ == '__main__':
    main()

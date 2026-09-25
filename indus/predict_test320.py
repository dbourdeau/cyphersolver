"""Three-hundred-and-twentieth registered prediction set (PREDICTIONS.md, SC1-SC3): decipherment loop 145, the SIGN task
with 250 candidates instead of 150 (a hidden sign outside the 150 commonest can never be ranked first). Two-direction
model unchanged. Writes results/predict_test320.md."""
import rtools as R
from prizebench import sign_task
from progress import MODEL, data


def main():
    rd = R.Round('Three-hundred-and-twentieth registered predictions: decipherment loop 145, SIGN with 250 candidates', 'predict_test320')
    DL, tr, te = data()
    a1, a5 = sign_task(tr, te, MODEL['keys'])[:2]
    b1, b5 = sign_task(tr, te, MODEL['keys'], ncand=250)[:2]
    rd.say('- 150 candidates %.2f%% / %.2f%%; 250 candidates %.2f%% / %.2f%%.' % (100 * a1, 100 * a5, 100 * b1, 100 * b5))
    rd.say()
    rd.rec('SC1', 'SIGN top-1 rises by 0.1 point or more', '%.2f%% -> %.2f%%' % (100 * a1, 100 * b1), b1 - a1 >= 0.001)
    rd.rec('SC2', 'SIGN top-5 does not fall', '%.2f%% -> %.2f%%' % (100 * a5, 100 * b5), b5 >= a5)
    rd.rec('SC3', 'progress rule: SC1 and SC2 (the SIGN task uses 250 candidates)', 'SC1 %s, SC2 %s' % (b1 - a1 >= 0.001, b5 >= a5), b1 - a1 >= 0.001 and b5 >= a5)
    rd.finish()


if __name__ == '__main__':
    main()

"""Two-hundred-and-seventy-fourth registered prediction set (PREDICTIONS.md, WB1-WB4): decipherment loop 99, a
two-direction scorer for the WORD task. Each candidate body is scored by the left-to-right model plus the right-to-left
model on the reversed line (as the SIGN task, set 204), against the left-to-right score alone (prizebench.word_task).
Writes results/predict_test274.md."""
from collections import Counter

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data


def nb(t):
    nm = R.name_of(list(t))
    return tuple(nm[0]) if nm and nm[0] else None


def main():
    rd = R.Round('Two-hundred-and-seventy-fourth registered predictions: decipherment loop 99, a two-direction WORD scorer', 'predict_test274')
    DL, tr, te = data()
    keys = MODEL['keys']
    w, _ = fit3(tr, keys)
    m = M3(tr)
    rtr = [tuple(reversed(x)) for x in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    bodies = Counter(nb(t) for t in tr if nb(t))
    cands = [b for b, c in bodies.most_common()]
    f1 = f10 = t1 = t10 = n = 0
    for t in te:
        b = nb(t)
        if not b:
            continue
        j = next((j for j in range(len(t) - len(b) + 1) if tuple(t[j:j + len(b)]) == b), None)
        if j is None:
            continue
        pre, post = tuple(t[:j]), tuple(t[j + len(b):])
        fw = {c: _lp(m, pre + c + post, w) for c in cands}
        bw = {c: _lp(mb, tuple(reversed(pre + c + post)), wb) for c in cands}
        s1 = sorted(cands, key=lambda c: -fw[c])
        s2 = sorted(cands, key=lambda c: -(fw[c] + bw[c]))
        n += 1
        f1 += s1[0] == b
        f10 += b in s1[:10]
        t1 += s2[0] == b
        t10 += b in s2[:10]
    rd.say('- %d test names; left-to-right top-1 %d, top-10 %d; two-direction top-1 %d, top-10 %d.' % (n, f1, f10, t1, t10))
    rd.say()
    rd.rec('WB1', 'WORD top-10 rises by 1 point or more', '%.1f%% -> %.1f%%' % (100 * f10 / n, 100 * t10 / n), t10 - f10 >= 0.01 * n)
    rd.rec('WB2', 'WORD top-1 does not fall', '%.1f%% -> %.1f%%' % (100 * f1 / n, 100 * t1 / n), t1 >= f1)
    rd.rec('WB3', 'progress rule: WB1 and WB2', 'top-10 %.1f%%, top-1 %.1f%%' % (100 * t10 / n, 100 * t1 / n), t10 - f10 >= 0.01 * n and t1 >= f1)
    rd.finish()


if __name__ == '__main__':
    main()

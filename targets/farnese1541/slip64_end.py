"""Fourth pass helper: dictionary words (it_words + degeminated) that end exactly at a line position, start in a
range, with at most one slip.  python slip64_end.py 64v.6 13 16 26 [suffix]"""
import sys
import probe, wordfit
from slip64_fit import enc_word
lab, a, b, e = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
suf = sys.argv[5] if len(sys.argv) > 5 else ''
i0, _ = probe.span(lab)
end = i0 + e
W = wordfit.load_words()
res = []
for w in W:
    if suf and not w.endswith(suf):
        continue
    if len(w) < 3:
        continue
    for s in range(i0 + a - 1, i0 + b):
        for j, p, ns in enc_word(s, w, end):
            if j == end:
                res.append((ns, -W[w], w, s - i0 + 1, ' '.join(p)))
for r in sorted(res)[:60]:
    print(r)

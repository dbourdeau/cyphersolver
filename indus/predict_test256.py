"""Two-hundred-and-fifty-sixth registered prediction set (PREDICTIONS.md, WR1-WR4): decipherment loop 81, WORD task with
names composed by the head-final name grammar. Candidates = the training name bodies plus every modifier sequence (a
body minus its head, seen 3+ times) joined to every head (seen 3+ times). Control: the same parts in the reverse
order (head first). Writes results/predict_test256.md."""
from collections import Counter

import rtools as R
from famlm import M3, fit3
from prizebench import _lp
from progress import MODEL, data


def nb(t):
    nm = R.name_of(list(t))
    return tuple(nm[0]) if nm and nm[0] else None


def run(tr, te, cands):
    w, _ = fit3(tr, MODEL['keys'])
    m = M3(tr)
    out = []
    for t in te:
        b = nb(t)
        if not b:
            continue
        j = next((j for j in range(len(t) - len(b) + 1) if tuple(t[j:j + len(b)]) == b), None)
        if j is None:
            continue
        pre, post = tuple(t[:j]), tuple(t[j + len(b):])
        sc = sorted(cands, key=lambda c: (-_lp(m, pre + c + post, w), c))
        out.append((b, sc[:10]))
    return out


def main():
    rd = R.Round('Two-hundred-and-fifty-sixth registered predictions: decipherment loop 81, WORD task with composed names', 'predict_test256')
    DL, tr, te = data()
    trb = Counter(nb(t) for t in tr if nb(t))
    seen = sorted(trb, key=lambda b: (-trb[b], b))
    hc = Counter(b[-1] for b in trb.elements())
    mc = Counter(b[:-1] for b in trb.elements())
    heads = sorted(h for h, c in hc.items() if c >= 3)
    mods = sorted(x for x, c in mc.items() if c >= 3)
    comp = sorted({x + (h,) for x in mods for h in heads} - set(seen))
    ctrl = sorted({(h,) + x for x in mods for h in heads} - set(seen))
    rd.say('- training bodies %d; heads %d, modifier sequences %d; composed %d, control %d.' % (len(seen), len(heads), len(mods), len(comp), len(ctrl)))
    base = run(tr, te, seen)
    new = run(tr, te, seen + comp)
    con = run(tr, te, seen + ctrl)
    n = len(base)
    b10 = sum(b in s for b, s in base)
    n10 = sum(b in s for b, s in new)
    c10 = sum(b in s for b, s in con)
    comp_s = set(comp)
    nc = sum(b in s and b in comp_s for b, s in new)
    ctrl_hits = sum(b in s and b not in trb for b, s in con)
    rd.say('- test names %d; top-10: seen only %d, with composed %d, with control %d; top-1 %d / %d.' % (n, b10, n10, c10, sum(b == s[0] for b, s in base), sum(b == s[0] for b, s in new)))
    rd.say()
    rd.rec('WR1', 'WORD top-10 rises by 1 point or more with composed names', '%.1f%% -> %.1f%%' % (100 * b10 / n, 100 * n10 / n), n10 - b10 >= 0.01 * n)
    rd.rec('WR2', 'at least 3 never-seen test names reach the top 10', '%d composed names in the top 10' % nc, nc >= 3)
    rd.rec('WR3', 'head-final composition beats head-first (control)', 'top-10 %d against %d; unseen hits %d against %d' % (n10, c10, nc, ctrl_hits), n10 > c10 and nc > ctrl_hits)
    rd.rec('WR4', 'progress rule: WR1 and WR3', 'WORD top-10 %.1f%%' % (100 * n10 / n), n10 - b10 >= 0.01 * n and n10 > c10 and nc > ctrl_hits)
    rd.finish()


if __name__ == '__main__':
    main()

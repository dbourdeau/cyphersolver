"""Hundred-and-ninth registered prediction set (PREDICTIONS.md, BC1-BC20): the bare-line closers. Writes
results/predict_test109.md."""
from collections import Counter

import predict_test13 as T
import rtools as R

HEAD = ('817', '820', '861')


def toks(lines, s):
    return [(t, i) for t in lines for i in range(len(t)) if t[i] == s]


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-ninth registered predictions: the bare-line closers', 'predict_test109')
    DL = sorted({tuple(t) for t in AB})
    heads = {b[-1] for b, e in T.names(AB) if b}
    rd.say('- tokens: %s.' % {s: len(toks(DL, s)) for s in ('368', '390', '595', '615', '400')})
    rd.say()

    def bc1(lines, key, lab):
        x = toks(lines, '368')
        rd.thr(key, '368 closes lines%s' % lab, '368 tokens line-final', sum(i == len(t) - 1 for t, i in x), len(x), 0.5)
    bc1(DL, 'BC1', '')
    x = toks(DL, '390')
    rd.thr('BC2', '390 is counted', '390 tokens after a numeral', sum(i > 0 and t[i - 1] in R.NUMS for t, i in x), len(x), 0.5)
    x = toks(DL, '595')
    rd.thr('BC3', "595 follows 95", '595 tokens after 95 (%s)' % dict(Counter(t[i - 1] for t, i in x if i > 0).most_common(4)),
           sum(i > 0 and t[i - 1] == '95' for t, i in x), len(x), 0.3)

    def bc4(lines, key, lab):
        x = toks(lines, '615')
        rd.thr(key, '615 is doubled%s' % lab, '615 tokens next to 615', sum((i > 0 and t[i - 1] == '615') or (i + 1 < len(t) and t[i + 1] == '615') for t, i in x), len(x), 0.3)
    bc4(DL, 'BC4', '')
    b4 = [(t, i) for t, i in toks(DL, '400') if not (i > 0 and t[i - 1] in R.END)]
    rd.thr('BC5', 'bare 400 follows a head', 'bare-400 tokens after a name head', sum(i > 0 and t[i - 1] in heads for t, i in b4), len(b4), 0.5)
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    bare4 = lambda t: any(g == '400' and not (i > 0 and t[i - 1] in R.END) for i, g in enumerate(t))
    x = [ty for s, ty, t in FD if bare4(t)]
    rd.thr('BC6', 'bare 400 is a tablet sign', 'bare-400 lines on tablets', sum(ty == 'TAB' for ty in x), len(x), 0.6)
    x = [ty for s, ty, t in FD if '368' in t]
    rd.thr('BC7', '368 is a seal sign', '368 lines on seals', sum(ty == 'SEA' for ty in x), len(x), 0.7)
    p368 = {t[i - 1] for t, i in toks(DL, '368') if i > 0}
    p740 = {t[i - 1] for t, i in toks(DL, '740') if i > 0}
    j = len(p368 & p740) / max(1, len(p368 | p740))
    rd.rec('BC8', '368 and 740 take different words', 'Jaccard %.3f; threshold 0.3' % j, j <= 0.3)
    x = toks(DL, '368')
    rd.thr('BC9', '368 follows a heading', '368 tokens after a heading sign', sum(i > 0 and t[i - 1] in HEAD for t, i in x), len(x), 0.1)
    v = []
    for t, i in toks(DL, '390'):
        if i > 0 and t[i - 1] in R.NUMS:
            j_ = i - 1
            while j_ > 0 and t[j_ - 1] in R.NUMS:
                j_ -= 1
            v.append(sum(R.NUMS[g][0] for g in t[j_:i]))
    rd.thr('BC10', '390 is counted high', 'values 3+ before 390', sum(x_ >= 3 for x_ in v), len(v), 0.9)
    x = [ty for s, ty, t in FD if '390' in t]
    rd.thr('BC11', '390 is a seal sign', '390 lines on seals', sum(ty == 'SEA' for ty in x), len(x), 0.7)

    def bc12(lines, key, lab):
        x = toks(lines, '615')
        rd.thr(key, '615 sits inside%s' % lab, '615 tokens medial', sum(0 < i < len(t) - 1 for t, i in x), len(x), 0.7)
    bc12(DL, 'BC12', '')
    num = lambda t: any(g in R.NUMS for g in t)
    rd.gtl('BC13', '615 lines count', 'numeral, lines with 615', [num(t) for t in DL if '615' in t], [num(t) for t in DL if '615' not in t])
    pc = Counter(t[i - 1] for t, i in b4 if i > 0)
    rd.thr('BC14', 'few things before bare 400', 'four commonest (%s)' % ', '.join('%s x%d' % kv for kv in pc.most_common(4)), sum(n for _, n in pc.most_common(4)), sum(pc.values()), 0.4)
    p74 = {t[i - 2] for t, i in toks(DL, '400') if i > 1 and t[i - 1] in R.END}
    pb = set(pc)
    j = len(pb & p74) / max(1, len(pb | p74))
    rd.rec('BC15', 'two different 400s', 'Jaccard %.3f; threshold 0.3' % j, j <= 0.3)
    all595 = [r['type'] for r in F for ln in r['seq'] for g in ln if g == '595']
    rd.thr('BC16', '595 is a copper word', '595 tokens on copper', sum(ty == 'TAB:C' for ty in all595), len(all595), 0.3)
    rd.gtl('BC17', '368 is Mohenjo-daran', '368 lines, Mohenjo-daro', ['368' in t for s, ty, t in FD if s == 'Mohenjo-daro'], ['368' in t for s, ty, t in FD if s == 'Harappa'])
    BL = sorted({tuple(t) for t in B})
    bc1(BL, 'BC18', ' (B)')
    bc4(BL, 'BC19', ' (B)')
    bc12(sorted({t for s, ty, t in FD}), 'BC20', " (F')")
    rd.finish()


if __name__ == '__main__':
    main()

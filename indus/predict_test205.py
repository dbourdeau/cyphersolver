"""Two-hundred-and-fifth registered prediction set (PREDICTIONS.md, GA1-GA6): decipherment loop 30, a character-LM key
scorer against the Linear B gate (order chosen on odd lines, judged on even lines, Sanskrit specificity control);
the two-direction WORD task. Writes results/predict_test205.md."""
import csv
import os
import re
from collections import Counter

import bench
import lang_names as L
import rtools as R
from famlm import M3, fit3
from lmkey import CharLM, score
from linb_control import adjust
from prizebench import _lp
from progress import MODEL, data
from signs import load as sload

LB = os.path.join(L.SP, 'linb')


def lb_lines():
    vals = {}
    for r in csv.DictReader(open(os.path.join(LB, 'syllabograms.csv'), encoding='utf-8')):
        if r['value'] and r['value'] != '?':
            vals[r['sign']] = r['value']
    lines = []
    for ln in open(os.path.join(LB, 'corpus_damos_lines.txt'), encoding='utf-8'):
        parts = ln.rstrip('\n').split('\t')
        if len(parts) < 3:
            continue
        signs = []
        for tok in parts[2].split():
            if tok.startswith('~') or not re.match(r'^[a-z0-9*]+(-[a-z0-9*]+)*$', tok) or tok.isdigit():
                continue
            signs.extend(tok.split('-'))
        if len(signs) >= 3:
            lines.append(signs)
    key = {g: vals[g] for g in {s for t in lines for s in t} if g in vals}
    return lines, key


def gate(lines, key, lm, shuffles):
    real = score(lines, key, lm)
    sims = sorted(score(lines, k2, lm) for k2 in shuffles)
    return real, sims, sum(1 for x in sims if x >= real)


def word2(tr, te, keys):
    wf, _ = fit3(tr, keys)
    mf = M3(tr)
    rtr = [tuple(reversed(t)) for t in tr]
    wb, _ = fit3(rtr, keys)
    mb = M3(rtr)
    bodies = Counter(tuple(nm[0]) for nm in (R.name_of(list(t)) for t in tr) if nm and nm[0])
    cands = [b for b, c in bodies.most_common()]
    f10 = b10 = n = 0
    for t in te:
        nm = R.name_of(list(t))
        if not (nm and nm[0]):
            continue
        b = tuple(nm[0])
        j = next((j for j in range(len(t) - len(b) + 1) if tuple(t[j:j + len(b)]) == b), None)
        if j is None:
            continue
        pre, post = t[:j], t[j + len(b):]
        sf = {c: _lp(mf, pre + c + post, wf) for c in cands}
        sb = {c: _lp(mb, tuple(reversed(pre + c + post)), wb) for c in cands}
        n += 1
        f10 += b in sorted(cands, key=lambda c: -sf[c])[:10]
        b10 += b in sorted(cands, key=lambda c: -(sf[c] + sb[c]))[:10]
    return f10 / max(1, n), b10 / max(1, n), n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-fifth registered predictions: decipherment loop 30, a key scorer against the Linear B gate; two-direction WORD', 'predict_test205')
    lines, key = lb_lines()
    freq = Counter(s for t in lines for s in t)
    odd, even = lines[1::2], lines[0::2]
    gk = [adjust(w.strip()) for w in open(os.path.join(LB, 'greek', 'greek_translit_wordlist.txt'), encoding='utf-8') if w.strip()]
    sk = [k1.lower() for k1, mem, syl in L.skt()]
    shuf = list(bench.shuffles(key, freq, n=100, band=10))
    best = None
    for order in (2, 3, 4, 5):
        lm = CharLM(gk, order)
        real, sims, ge = gate(odd, key, lm, shuf)
        z = (real - sims[50]) / max(1e-9, sims[-1] - sims[0])
        rd.say('- design (odd lines), order %d: real %.3f, shuffles median %.3f, as good %d of 100.' % (order, real, sims[50], ge))
        if best is None or (ge, -z) < (best[1], -best[2]):
            best = (order, ge, z)
    order = best[0]
    rd.say('- chosen order %d.' % order)
    rd.say()
    rg, sg, geg = gate(even, key, CharLM(gk, order), shuf)
    rd.rec('GA1', "Greek model: Ventris's key beats 95 of 100 shuffles", 'real %.3f bits/char; shuffles median %.3f (%.3f to %.3f); %d of 100 as good' % (rg, sg[50], sg[0], sg[-1], geg), geg <= 5)
    rs, ss, ges = gate(even, key, CharLM(sk, order), shuf)
    rd.rec('GA2', 'Sanskrit model: not language-blind', 'real %.3f; shuffles median %.3f; %d of 100 as good' % (rs, ss[50], ges), ges > 5)
    rd.rec('GA3', 'larger margin with Greek', 'margin over shuffle median: Greek %.3f, Sanskrit %.3f bits/char' % (rg - sg[50], rs - ss[50]), rg - sg[50] > rs - ss[50])
    DL, tr, te = data()
    f10, b10, n = word2(tr, te, MODEL['keys'])
    rd.rec('GA4', 'two-direction WORD, fixed test', 'top-10 forward %.1f%%, two-direction %.1f%% (%d names)' % (100 * f10, 100 * b10, n), b10 - f10 >= 0.01)
    DA = sorted({tuple(t) for t in A})
    DBx = sorted({tuple(ln) for r in sload(only_m77=True) for ln in r['seq'] if ln} - set(DA))[:300]
    fa, ba, na = word2(DA, DBx, MODEL['keys'])
    rd.rec('GA5', 'and A -> B', 'top-10 forward %.1f%%, two-direction %.1f%% (%d names)' % (100 * fa, 100 * ba, na), ba > fa)
    ok = (geg <= 5 and ges > 5) or (b10 - f10 >= 0.01 and ba > fa)
    rd.rec('GA6', 'progress rule', 'gate %s; WORD %s' % (geg <= 5 and ges > 5, b10 - f10 >= 0.01 and ba > fa), ok)
    rd.finish()


if __name__ == '__main__':
    main()

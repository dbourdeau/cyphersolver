"""Unsupervised word segmentation of the Indus texts (Goldwater, Griffiths and Johnson 2006/2009:
the unigram Dirichlet-process model, Gibbs-sampled over word boundaries).

A word is a run of signs; its prior probability is P0(w) = p_end (1 - p_end)^(n-1) prod P(sign);
the model prefers a small, reused vocabulary. Nothing about the known structure is given to it.

S1  The segmentation of the corpus (lines of 2+ signs, ICIT-derived, with the M77 additions as a
    second run): number of word types and tokens, mean word length, the commonest words.
S2  Do its boundaries fall where the structure says units end? Boundary rate after the opening
    formula [817/820/861]+[2/60/1], before the ending 740/520, and elsewhere; the same model on
    the texts with their signs shuffled within each line (the null: what the segmenter finds in
    sign soup of the same frequencies).
S3  The lexicon against the tablets and seals: share of word tokens that are one sign, two, three.

Writes results/segment.md.
"""
import math
import os
import random
from collections import Counter

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
ALPHA, P_END = 20.0, 0.5


def say(s=''):
    OUT.append(s)
    print(s)


class Seg:
    def __init__(self, lines, seed):
        self.rng = random.Random(seed)
        self.lines = lines
        sf = Counter(g for ln in lines for g in ln)
        n = sum(sf.values())
        self.ps = {g: c / n for g, c in sf.items()}
        # boundary after position i (i < len-1); start random
        self.b = [[self.rng.random() < 0.5 for _ in range(len(ln) - 1)] for ln in lines]
        self.cnt = Counter()
        self.tot = 0
        for k in range(len(lines)):
            for w in self.words(k):
                self.cnt[w] += 1
                self.tot += 1

    def words(self, k):
        ln, b = self.lines[k], self.b[k]
        out, s = [], 0
        for i in range(len(ln) - 1):
            if b[i]:
                out.append(tuple(ln[s:i + 1]))
                s = i + 1
        out.append(tuple(ln[s:]))
        return out

    def p0(self, w):
        p = P_END * (1 - P_END) ** (len(w) - 1)
        for g in w:
            p *= self.ps[g]
        return p

    def pw(self, w, extra=Counter(), et=0):
        return (self.cnt[w] + extra[w] + ALPHA * self.p0(w)) / (self.tot + et + ALPHA)

    def sweep(self, temp=1.0):
        for k in range(len(self.lines)):
            ln, b = self.lines[k], self.b[k]
            for i in range(len(ln) - 1):
                # word spans around boundary i
                s = i
                while s > 0 and not b[s - 1]:
                    s -= 1
                e = i + 1
                while e < len(ln) - 1 and not b[e]:
                    e += 1
                left, right, whole = tuple(ln[s:i + 1]), tuple(ln[i + 1:e + 1]), tuple(ln[s:e + 1])
                if b[i]:
                    self.cnt[left] -= 1
                    self.cnt[right] -= 1
                    self.tot -= 2
                else:
                    self.cnt[whole] -= 1
                    self.tot -= 1
                p_no = self.pw(whole)
                p_yes = self.pw(left) * self.pw(right, Counter({left: 1}), 1)
                p_no, p_yes = p_no ** (1 / temp), p_yes ** (1 / temp)
                yes = self.rng.random() < p_yes / (p_yes + p_no)
                b[i] = yes
                if yes:
                    self.cnt[left] += 1
                    self.cnt[right] += 1
                    self.tot += 2
                else:
                    self.cnt[whole] += 1
                    self.tot += 1

    def run(self, iters=300):
        for it in range(iters):
            temp = max(1.0, 3.0 * (1 - it / (0.7 * iters)) + 1.0 * (it / (0.7 * iters)))
            self.sweep(temp)
        return self


def slots(ln):
    """Structural boundary labels for each gap: 'opener' after the formula, 'ending' before 740/520, else ''."""
    lab = [''] * (len(ln) - 1)
    if len(ln) >= 3 and ln[0] in ('817', '820', '861') and ln[1] in ('2', '60', '1'):
        lab[1] = 'opener'
    for i in range(len(ln) - 1):
        if ln[i + 1] in ('740', '520') and ln[i] not in ('740', '520'):
            lab[i] = 'ending'
    return lab


def rates(seg):
    c, n = Counter(), Counter()
    for ln, b in zip(seg.lines, seg.b):
        for lab, x in zip(slots(ln), b):
            key = lab or 'elsewhere'
            n[key] += 1
            c[key] += x
    return {k: (c[k], n[k]) for k in n}


def main():
    say('# Unsupervised word segmentation (Goldwater DP unigram model)')
    say()
    for lab, rows in (('ICIT-derived', load()), ('M77 additions', load(only_m77=True))):
        lines = [[g for g in ln if g != '?'] for r in rows for ln in r['seq']]
        lines = [ln for ln in lines if len(ln) >= 2]
        seg = Seg(lines, 1).run()
        words = Counter(w for k in range(len(lines)) for w in seg.words(k))
        ntok = sum(words.values())
        say('## %s: %d lines' % (lab, len(lines)))
        say()
        say('- S1 word types %d, tokens %d, mean length %.2f signs; one-sign words %.0f%%, two %.0f%%, three+ %.0f%%.' % (
            len(words), ntok, sum(len(w) * c for w, c in words.items()) / ntok,
            100 * sum(c for w, c in words.items() if len(w) == 1) / ntok,
            100 * sum(c for w, c in words.items() if len(w) == 2) / ntok,
            100 * sum(c for w, c in words.items() if len(w) >= 3) / ntok))
        say('- commonest multi-sign words: %s.' % ', '.join(
            ['[%s] x%d' % (' '.join(w), c) for w, c in words.most_common(200) if len(w) >= 2][:20]))
        real = rates(seg)
        shuf = []
        for ln in lines:
            u = list(ln)
            random.Random(len(shuf)).shuffle(u)
            shuf.append(u)
        segn = Seg(shuf, 2).run()
        null = rates(segn)
        say('- S2 boundary rate (share of gaps the model cuts): %s; sign-shuffled lines: %s.' % (
            ', '.join('%s %d/%d (%.0f%%)' % (k, c, n, 100 * c / n) for k, (c, n) in sorted(real.items())),
            ', '.join('%s %.0f%%' % (k, 100 * c / n) for k, (c, n) in sorted(null.items()))))
        wn = Counter(w for k in range(len(shuf)) for w in segn.words(k))
        say('- the null model: word types %d, mean length %.2f.' % (
            len(wn), sum(len(w) * c for w, c in wn.items()) / sum(wn.values())))
        say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'segment.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()

"""A slot grammar of the whole text against n-gram models, on unseen texts.

The rules found so far - an optional heading (817/820/861 + 2/60/1), a name, an ending (740 / 520) chosen by the
name's last sign, an optional second slot (400 / 90 / 151) - are put together as one probabilistic model and compared
with plain sign n-grams on how well they predict texts they were not trained on (cross-entropy, bits per sign; lower
is better).

Models (all trained on the ICIT-derived lines, tested on the held-out lines: M77 additions + the fuller corpus's
texts not in the dump; lines with unknown signs left out; a closed vocabulary of all signs, add-k smoothing):
  unigram; bigram and trigram with interpolation (Witten-Bell-style weights by context count);
  slot grammar: P(heading form) x P(name | a bigram model trained on names only) x P(ending | the name's last sign,
  backed off to the ending's overall rate) x P(second slot | ending); texts that do not parse into these slots fall
  back to the bigram.
  slot + trigram: the slot grammar with the trigram inside the name.

Usage: python grammar_model.py path/to/icit_full_records_indusscript_net.csv
Writes results/grammar_model.md.
"""
import math
import os
import sys
from collections import Counter, defaultdict

import icit_full
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPEN = ('817', '820', '861')
MID = ('2', '60', '1')
ENDS = ('740', '520')
SEC = ('400', '90', '151')


def say(s=''):
    OUT.append(s)
    print(s)


class NGram:
    def __init__(self, lines, n, V, k=0.05):
        self.n, self.V, self.k = n, V, k
        self.c = [defaultdict(Counter) for _ in range(n)]
        for t in lines:
            s = ['<s>'] * (n - 1) + list(t) + ['</s>']
            for i in range(n - 1, len(s)):
                for o in range(n):
                    self.c[o][tuple(s[i - o:i])][s[i]] += 1

    def p(self, hist, w):
        pr = (self.c[0][()][w] + self.k) / (sum(self.c[0][()].values()) + self.k * (len(self.V) + 1))
        for o in range(1, self.n):
            h = tuple(hist[-o:])
            cc = self.c[o].get(h)
            if not cc:
                continue
            tot, typ = sum(cc.values()), len(cc)
            lam = tot / (tot + typ)
            pr = lam * cc[w] / tot + (1 - lam) * pr
        return pr

    def logp(self, t):
        s = ['<s>'] * (self.n - 1) + list(t) + ['</s>']
        return sum(math.log2(self.p(s[i - self.n + 1:i], s[i])) for i in range(self.n - 1, len(s)))


def parse(t):
    t = list(t)
    head = None
    if len(t) >= 3 and t[0] in OPEN and t[1] in MID:
        head, t = (t[0], t[1]), t[2:]
    sec = end = None
    if len(t) >= 3 and t[-1] in SEC and t[-2] in ENDS:
        sec, end, t = t[-1], t[-2], t[:-2]
    elif len(t) >= 2 and t[-1] in ENDS:
        end, t = t[-1], t[:-1]
    if not t:
        return None
    return head, t, end, sec


class Slot:
    def __init__(self, lines, V, inner_n=2):
        self.big = NGram(lines, 2, V)
        parsed = [parse(t) for t in lines]
        self.heads = Counter(p[0] for p in parsed if p)
        self.names = NGram([p[1] for p in parsed if p], inner_n, V)
        self.end_given = defaultdict(Counter)
        self.end_all = Counter()
        self.sec_given = defaultdict(Counter)
        for p in parsed:
            if not p:
                continue
            self.end_given[p[1][-1]][p[2]] += 1
            self.end_all[p[2]] += 1
            if p[2]:
                self.sec_given[p[2]][p[3]] += 1
        self.npar = sum(1 for p in parsed if p)

    def logp(self, t):
        p = parse(t)
        if not p:
            return self.big.logp(t)
        head, name, end, sec = p
        lp = math.log2((self.heads[head] + 0.5) / (self.npar + 0.5 * (len(self.heads) + 1)))
        lp += self.names.logp(name)
        c = self.end_given.get(name[-1], Counter())
        tot = sum(c.values())
        base = (self.end_all[end] + 0.5) / (sum(self.end_all.values()) + 1.5)
        lam = tot / (tot + 2)
        lp += math.log2(lam * (c[end] / tot if tot else 0) + (1 - lam) * base)
        if end:
            s = self.sec_given[end]
            lp += math.log2((s[sec] + 0.5) / (sum(s.values()) + 2))
        return lp


def main(path):
    train = [tuple(ln) for r in load() for ln in r['seq'] if len(ln) >= 2]
    have = {tuple(tuple(ln) for ln in r['seq']) for r in load()}
    held_rows = [r for r in load(only_m77=True) if r['flat']]
    held_rows += [r for r in icit_full.objects(path, intact_only=True)
                  if r['seq'] and tuple(tuple(ln) for ln in r['seq']) not in have]
    held = [tuple(ln) for r in held_rows for ln in r['seq'] if len(ln) >= 2 and '?' not in ln]
    V = {g for t in train + held for g in t}
    models = {'unigram': NGram(train, 1, V), 'bigram': NGram(train, 2, V), 'trigram': NGram(train, 3, V),
              'slot grammar (bigram names)': Slot(train, V, 2), 'slot grammar (trigram names)': Slot(train, V, 3)}
    ntok = sum(len(t) + 1 for t in held)
    say('# A slot grammar against n-grams on unseen texts')
    say()
    say('- training lines: %d (ICIT-derived); held-out lines: %d (M77 additions + fuller-corpus texts not in the dump), '
        '%d sign positions incl. the end of line; vocabulary %d; held-out lines that parse into the slots: %d (%.0f%%).' % (
            len(train), len(held), ntok, len(V), sum(1 for t in held if parse(t)), 100 * sum(1 for t in held if parse(t)) / len(held)))
    say()
    say('| model | cross-entropy, bits per sign (held out) |')
    say('|---|---|')
    for k, m in models.items():
        say('| %s | %.3f |' % (k, -sum(m.logp(t) for t in held) / ntok))
    say()
    say('A slot grammar that does as well as, or better than, a trigram with far fewer free choices captures the '
        'structure the n-grams learn; the difference in bits per sign is the part of the texts the rules do not explain.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'grammar_model.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])

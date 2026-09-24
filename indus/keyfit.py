"""Blind key fitting (set 207): sign values fitted to a language by annealing, the character-LM objective scored on
half the lines, the fitted key judged on the other half. Every language gets the same freedom; the control is the
same fit on lines whose signs are shuffled within each line (order destroyed, frequencies kept)."""
import math
import random
import re
from collections import Counter, defaultdict

from lmkey import CharLM


def units(words, k=90):
    c = Counter()
    for w in words:
        for u in re.findall(r'[^aeiou]*[aeiou]+', w):
            c[u] += 1
    return [u for u, n in c.most_common(k)]


class Fit:
    def __init__(self, lines, lm, inv, seed=0):
        self.lines, self.lm, self.inv = lines, lm, inv
        self.rnd = random.Random(seed)
        self.signs = sorted({g for t in lines for g in t})
        self.key = {g: self.rnd.choice(inv) for g in self.signs}
        self.where = defaultdict(set)
        for i, t in enumerate(lines):
            for g in t:
                self.where[g].add(i)
        self.cache = [self.lm.lp(self.dec(t)) for t in lines]
        self.total = sum(self.cache)

    def dec(self, t, key=None):
        k = key or self.key
        return ''.join(k[g] for g in t)

    def run(self, iters=20000, t0=0.5, t1=0.01):
        for it in range(iters):
            T = t0 * (t1 / t0) ** (it / iters)
            g = self.rnd.choice(self.signs)
            old = self.key[g]
            new = self.rnd.choice(self.inv)
            if new == old:
                continue
            self.key[g] = new
            idx = self.where[g]
            nv = {i: self.lm.lp(self.dec(self.lines[i])) for i in idx}
            d = sum(nv[i] - self.cache[i] for i in idx)
            if d >= 0 or self.rnd.random() < math.exp(d / T):
                for i, v in nv.items():
                    self.cache[i] = v
                self.total += d
            else:
                self.key[g] = old
        return self.key


def shuffle_within(lines, seed=0):
    rnd = random.Random(seed)
    return [tuple(rnd.sample(list(t), len(t))) for t in lines]

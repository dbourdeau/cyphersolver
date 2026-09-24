"""A key scorer by character language model (set 205): a decoded line, values joined without dividers, scored by a
character n-gram model of the claimed language trained on its word list. Positive control on Linear B (Ventris's
values against shuffles), as the gate the prize bench (tier 2) asks for."""
import math
from collections import Counter, defaultdict


class CharLM:
    def __init__(self, words, order=4, k=0.5):
        self.n, self.k = order, k
        self.c = defaultdict(Counter)
        chars = set()
        for w in words:
            s = '^' * (order - 1) + w + '$'
            chars |= set(w)
            for i in range(order - 1, len(s)):
                self.c[s[i - order + 1:i]][s[i]] += 1
        self.V = len(chars) + 1
        self.tot = {h: sum(v.values()) for h, v in self.c.items()}

    def lp(self, text):
        s = '^' * (self.n - 1) + text + '$'
        out = 0.0
        for i in range(self.n - 1, len(s)):
            h = s[i - self.n + 1:i]
            out += math.log2((self.c[h][s[i]] + self.k) / (self.tot.get(h, 0) + self.k * self.V))
        return out / (len(s) - self.n + 1)


def score(lines, key, lm):
    vals = [lm.lp(''.join(key.get(g, '') for g in t)) for t in lines if any(g in key for g in t)]
    return sum(vals) / max(1, len(vals))

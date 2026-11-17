"""Modèle de langue par caractères (suédois ancien), lissage par décompte absolu interpolé (D=0,75), ordre ORDER.
Alphabet fixe de 29 lettres. Contexte remis à zéro en début de segment (début de suite chiffrée ou après un code inconnu)."""
import math, collections
ALPHA = 'abcdefghijklmnopqrstuvwxyzåäö'; A = len(ALPHA); ORDER = 5; D = 0.75
def norm(s):
    s = s.lower().replace('é','e').replace('ü','y').replace('v','w')
    return ''.join(c for c in s if c in ALPHA)
class LM:
    def __init__(self, text):
        self.c = [collections.defaultdict(collections.Counter) for _ in range(ORDER)]
        for line in text.split('\n'):
            line = norm(line)
            for i, ch in enumerate(line):
                for k in range(ORDER):
                    if i - k < 0: break
                    self.c[k][line[i-k:i]][ch] += 1
        self.tot = [{h: sum(v.values()) for h, v in ck.items()} for ck in self.c]
        self.typ = [{h: len(v) for h, v in ck.items()} for ck in self.c]
        self.cache = {}
    def p(self, h, ch):
        key = (h, ch)
        if key in self.cache: return self.cache[key]
        if h == '':
            n = self.tot[0].get('', 0); cnt = self.c[0][''][ch]
            r = (max(cnt - D, 0) + D * self.typ[0].get('', 0) / A) / n
        else:
            k = len(h); lower = self.p(h[1:], ch); n = self.tot[k].get(h, 0)
            if n == 0: r = lower
            else:
                cnt = self.c[k][h].get(ch, 0)
                r = (max(cnt - D, 0) + D * self.typ[k][h] * lower) / n
        self.cache[key] = r; return r
    def ll(self, seg):
        """somme des log2 p et nombre de caractères pour un segment continu"""
        s = 0.0
        for i, ch in enumerate(seg):
            s += math.log2(self.p(seg[max(0, i-ORDER+1):i], ch))
        return s, len(seg)

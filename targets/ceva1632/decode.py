"""Decipher a 346-cipher digit stream by beam search under a character LM.

Every '6' is a word separator (no code of this cipher contains a 6), so the
cut points are certain; what is not is whether the next code is a two-digit
homophone/null or a three-digit nomenclator element.  A position-indexed beam
resolves that with an Italian character model, preferring the nomenclator
codes Lasry already met in the four letters he read.

Scoring is incremental: DenseLM keeps a flat table of log P(c | previous
order-1 chars), so each emitted character costs one array lookup.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from cipher import KEY, NULLS, NOMEN
from lang import lm

DEAD = {'%02d' % i for i in range(100)} - set(KEY) - NULLS

P_NOMEN_KNOWN = -1.5
P_NOMEN_NEW = -5.0
P_NOMEN_UNVALUED = None   # if set: penalty for a known code that has no value yet (Oct 2026)
P_NULL = -0.4
P_NOISE = -12.0

class Ctx:
    """Incremental DenseLM context."""
    def __init__(self, model):
        self.m = model
        self.A = model.A
        self.k = model.order
        self.mod = self.A ** (self.k - 1)
        self.idx = model.index

    def start(self):
        c = 0
        for ch in ' ' * (self.k - 1):
            c = (c * self.A + self.idx[ch]) % self.mod
        return c

    def step(self, ctx, s):
        """Emit the characters of s; return (new ctx, log-prob)."""
        lp = 0.0
        for ch in s:
            i = self.idx.get(ch)
            if i is None:
                continue
            j = ctx * self.A + i
            lp += float(self.m.lp[j])
            ctx = j % self.mod
        return ctx, lp

def load_nomen():
    g = json.load(open(os.path.join(HERE, 'gold.json'), encoding='utf-8'))
    return {t for _, row in g for t, _ in row if t.isdigit() and len(t) == 3}

def decode(stream, model, nomen, beam=250, w_lm=1.0):
    C = Ctx(model)
    n = len(stream)
    lanes = [dict() for _ in range(n + 1)]     # ctx -> (score, text, tokens)
    lanes[0][C.start()] = (0.0, '', [])
    for i in range(n):
        if not lanes[i]:
            continue
        items = sorted(lanes[i].items(), key=lambda kv: -kv[1][0])[:beam]
        for ctx, (sc, text, toks) in items:
            if stream[i] == '6':
                moves = [(1, ' ', '6', 0.0)]
            else:
                moves = []
                two = stream[i:i + 2]
                if len(two) == 2 and two not in DEAD:
                    if two in NULLS:
                        moves.append((2, '', two, P_NULL))
                    else:
                        moves.append((2, KEY[two], two, 0.0))
                three = stream[i:i + 3]
                if len(three) == 3 and '6' not in three and (three[1:] in KEY or three[1:] in NULLS):
                    moves.append((3, NOMEN.get(three, ' '), '#' + three,
                                  (P_NOMEN_KNOWN if (three in NOMEN or P_NOMEN_UNVALUED is None)
                                   else P_NOMEN_UNVALUED) if three in nomen else P_NOMEN_NEW))
                if not moves:
                    moves = [(1, '', '?' + stream[i], P_NOISE)]
            for adv, emit, tok, pen in moves:
                nctx, lp = C.step(ctx, emit)
                cand = (sc + pen + w_lm * lp, text + emit, toks + [tok])
                cur = lanes[i + adv].get(nctx)
                if cur is None or cand[0] > cur[0]:
                    lanes[i + adv][nctx] = cand
    end = lanes[n]
    if not end:
        for i in range(n, -1, -1):
            if lanes[i]:
                end = lanes[i]; break
    return max(end.values(), key=lambda v: v[0])

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('stream_file')
    ap.add_argument('--model', default='it-cinquecento')
    ap.add_argument('--beam', type=int, default=400)
    a = ap.parse_args()
    model = lm.load(a.model)
    nomen = load_nomen()
    for line in open(a.stream_file, encoding='utf-8'):
        s = ''.join(c for c in line if c.isdigit())
        if not s:
            continue
        print(decode(s, model, nomen, a.beam)[1])

if __name__ == '__main__':
    main()

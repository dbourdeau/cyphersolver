"""Hundred-and-seventy-sixth registered prediction set (PREDICTIONS.md, LP1-LP8): decipherment loop 1, structure and
roles. New model components (role, cls, nval) on top of set 125's mixture, weights by EM on a development split of the
training lines; evaluated on progress.py's fixed test split. Writes results/predict_test176.md."""
import math
import random
from collections import Counter, defaultdict

import numpy as np

import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test125 import M2
from progress import data, roles
from signs import load

BUCKET = lambda v: str(v) if v <= 4 else ('5-8' if v <= 8 else '9+')


def lrole(g):
    if g == '<s>':
        return 'start'
    if g in R.NUMS:
        return 'numeral'
    if g in R.END:
        return 'ending'
    if g in CL:
        return 'closer'
    if g in ('400', '90'):
        return 'marker'
    if g in ('817', '820', '861'):
        return 'heading'
    return 'other'


class M3(M2):
    def __init__(self, train, k=30, seed=7):
        super().__init__(train)
        self.crole = defaultdict(Counter)
        self.cnval = defaultdict(Counter)
        nxt = defaultdict(Counter)
        tok = Counter(g for t in train for g in t)
        for t in train:
            s = ['<s>'] + list(t) + ['</s>']
            run = 0
            for i in range(1, len(s)):
                w = s[i]
                self.crole[lrole(s[i - 1])][w] += 1
                prev = s[i - 1]
                run = run + R.NUMS[prev][0] if prev in R.NUMS else 0
                if prev in R.NUMS:
                    self.cnval[BUCKET(run)][w] += 1
                nxt[s[i - 1]][w] += 1
        common = [g for g, n in tok.items() if n >= 10]
        ctx = [g for g, n in Counter(w for c in nxt.values() for w in c.elements()).most_common(150)]
        X = np.array([[nxt[g][c] for c in ctx] for g in common], dtype=float)
        X = X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-9)
        rng = np.random.default_rng(seed)
        C = X[rng.choice(len(X), k, replace=False)]
        for _ in range(25):
            lab = np.argmax(X @ C.T, axis=1)
            for j in range(k):
                if (lab == j).any():
                    c = X[lab == j].mean(axis=0)
                    C[j] = c / max(np.linalg.norm(c), 1e-9)
        self.cls = {g: int(l) for g, l in zip(common, np.argmax(X @ C.T, axis=1))}
        self.ccls = defaultdict(Counter)
        for t in train:
            s = ['<s>'] + list(t) + ['</s>']
            for i in range(1, len(s)):
                self.ccls[self.cls.get(s[i - 1], 'rare' if s[i - 1] != '<s>' else 'start')][s[i]] += 1

    def rows(self, t, kn=False):
        base = super().rows(t, kn)
        s = ['<s>'] + [g if g in self.vocab else '<unk>' for g in t] + ['</s>']
        raw = ['<s>'] + list(t) + ['</s>']
        run = 0
        for i in range(1, len(s)):
            w, prev = s[i], raw[i - 1]
            r = base[i - 1]
            r['role'] = self.sm(self.crole[lrole(prev)], w)
            r['cls'] = self.sm(self.ccls[self.cls.get(prev, 'rare' if prev != '<s>' else 'start')], w)
            run = run + R.NUMS[prev][0] if prev in R.NUMS else 0
            r['nval'] = self.sm(self.cnval[BUCKET(run)], w) if prev in R.NUMS else self.sm(self.c['uni'], w)
        return base


def em(rows, keys, it=60):
    w = {k: 1 / len(keys) for k in keys}
    P = np.array([[r[k] for k in keys] for r in rows])
    wv = np.array([w[k] for k in keys])
    for _ in range(it):
        mix = P * wv
        post = mix / mix.sum(axis=1, keepdims=True)
        wv = post.mean(axis=0)
    return dict(zip(keys, wv))


def xent(rows, w):
    return sum(-math.log2(max(sum(w[k] * r[k] for k in w), 1e-12)) for r in rows) / len(rows)


def evaluate(tr, te, keys, seed=11):
    rnd = random.Random(seed)
    ls = list(tr)
    rnd.shuffle(ls)
    k = int(0.8 * len(ls))
    m_dev = M3(ls[:k])
    w = em([r for t in ls[k:] for r in m_dev.rows(t, True)], keys)
    m = M3(tr)
    return xent([r for t in te for r in m.rows(t, True)], w), w


def main():
    rd = R.Round('Hundred-and-seventy-sixth registered predictions: decipherment loop 1, structure and roles', 'predict_test176')
    DL, tr, te = data()
    base = ['tri', 'pos', 'end']
    b0, w0 = evaluate(tr, te, base)
    rd.say('- baseline mixture (tri + pos + end, EM weights): %.3f bits per sign.' % b0)
    rd.say()
    res = {}
    for key, comp, thr in (('LP1', 'role', 0.03), ('LP2', 'cls', 0.03), ('LP3', 'nval', 0.02)):
        x, w = evaluate(tr, te, base + [comp])
        res[comp] = x
        rd.rec(key, 'adding %s' % comp, '%.3f against %.3f (gain %.3f; weight %.2f); threshold %.2f' % (x, b0, b0 - x, w[comp], thr), b0 - x >= thr)
    best, bw = evaluate(tr, te, base + ['role', 'cls', 'nval'])
    rd.rec('LP4', 'the best combination', 'all three %.3f against %.3f (gain %.3f; weights %s); threshold 0.05' % (
        best, b0, b0 - best, ', '.join('%s %.2f' % kv for kv in bw.items())), b0 - best >= 0.05)
    # roles
    r0, by0, tot = roles(DL)
    mod = 0
    for t in DL:
        nm = R.name_of(list(t))
        if nm and len(nm[0]) >= 2:
            mod += sum(1 for g in nm[0][:-1] if g not in R.NUMS)
    r1 = r0 + mod / tot
    rd.rec('LP5', 'the modifier role', 'R %.1f%% -> %.1f%% (+%d modifier tokens, numerals already counted)' % (100 * r0, 100 * r1, mod), r1 > 0.70)

    def slots(lines):
        out = defaultdict(Counter)
        for t in lines:
            nm = R.name_of(list(t))
            if nm and nm[0]:
                b = nm[0]
                for i, g in enumerate(b):
                    out[g]['head' if i == len(b) - 1 else 'mod'] += 1
            else:
                for g in t:
                    out[g]['out'] += 1
        return out
    st, ss = slots(tr), slots(te)
    mods = {g for g, c in st.items() if c['mod'] > c['head'] and c['mod'] > c['out']}
    heads = {g for g, c in st.items() if c['head'] >= c['mod'] and c['head'] > c['out']}
    a = sum(ss[g]['mod'] + ss[g]['head'] for g in mods)
    b = sum(sum(ss[g].values()) for g in mods)
    rd.thr('LP6', 'modifiers stay in name bodies', 'test tokens of training modifiers inside name bodies', a, b, 0.8)
    a = sum(ss[g]['head'] for g in heads)
    b = sum(ss[g]['head'] + ss[g]['mod'] for g in heads)
    rd.thr('LP7', 'heads stay heads', 'test name-body tokens of training heads that are heads', a, b, 0.5)
    BL = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    rnd = random.Random(2026)
    rnd.shuffle(BL)
    k = int(0.8 * len(BL))
    bb0, _ = evaluate(BL[:k], BL[k:], base)
    bb1, _ = evaluate(BL[:k], BL[k:], base + ['role', 'cls', 'nval'])
    rd.rec('LP8', 'the gain holds on B', 'B: %.3f against %.3f' % (bb1, bb0), bb1 < bb0)
    rd.finish()


if __name__ == '__main__':
    main()

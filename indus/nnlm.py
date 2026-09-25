"""A small LSTM sign model (set 218 design), trained on training lines only, used as one more mixture component 'nn'
beside the n-gram components (famlm.M3). Deterministic (seeded); CPU."""
import math
import random

import torch
import torch.nn as nn

from famlm import M3


class LSTMLM(nn.Module):
    def __init__(self, V, emb=64, hid=128, drop=0.3):
        super().__init__()
        self.e = nn.Embedding(V, emb)
        self.l = nn.LSTM(emb, hid, batch_first=True)
        self.d = nn.Dropout(drop)
        self.o = nn.Linear(hid, V)

    def forward(self, x):
        h, _ = self.l(self.d(self.e(x)))
        return self.o(self.d(h))


def train_lm(lines, epochs=25, seed=0, lr=3e-3, dev=None):
    torch.manual_seed(seed)
    rnd = random.Random(seed)
    voc = ['<pad>', '<s>', '</s>', '<unk>'] + sorted({g for t in lines for g in t})
    idx = {g: i for i, g in enumerate(voc)}
    m = LSTMLM(len(voc))
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    data = [[1] + [idx[g] for g in t] + [2] for t in lines]
    best, best_state = None, None
    for ep in range(epochs):
        m.train()
        rnd.shuffle(data)
        for b in range(0, len(data), 32):
            batch = data[b:b + 32]
            L = max(map(len, batch))
            x = torch.tensor([s[:-1] + [0] * (L - len(s)) for s in batch])
            y = torch.tensor([s[1:] + [0] * (L - len(s)) for s in batch])
            loss = nn.functional.cross_entropy(m(x).reshape(-1, len(voc)), y.reshape(-1), ignore_index=0)
            opt.zero_grad()
            loss.backward()
            opt.step()
        if dev:
            h = xent_lines(m, idx, dev)
            if best is None or h < best:
                best, best_state = h, {k: v.clone() for k, v in m.state_dict().items()}
    if best_state:
        m.load_state_dict(best_state)
    m.eval()
    return m, idx


def probs(m, idx, t):
    """P(actual token) at each position of t + </s>."""
    s = [1] + [idx.get(g, 3) for g in t] + [2]
    with torch.no_grad():
        p = torch.softmax(m(torch.tensor([s[:-1]])), -1)[0]
    return [p[i, s[i + 1]].item() for i in range(len(s) - 1)]


def xent_lines(m, idx, lines):
    m.eval()
    tot = n = 0
    for t in lines:
        for q in probs(m, idx, t):
            tot -= math.log2(max(q, 1e-12))
            n += 1
    m.train()
    return tot / n


def with_nn(model, idx):
    class M5(M3):
        def rows(self, t, kn=False):
            out = super().rows(t, kn)
            for r, q in zip(out, probs(model, idx, t)):
                r['nn'] = q
            return out
    return M5

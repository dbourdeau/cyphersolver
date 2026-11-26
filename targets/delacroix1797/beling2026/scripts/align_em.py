#!/usr/bin/env python3
"""Monotone alignment of a sequence of code groups with a candidate plaintext.

Model: every code group emits one chunk of the plaintext, in order. A chunk is
  - nothing (a null), or
  - 1..K letters inside one word, or
  - one to three whole words (at most K letters in all).
The same group should emit the same chunk wherever it occurs. Parameters are
fitted by expectation-maximisation (forward-backward) from a start that knows
only the mean chunk length; the final alignment is the Viterbi path.

Nothing here knows any value of the real code. Written 21 Nov 2026 before the
draft transcription was read (see TEST_PLAN.md).
"""
import math
import re
import unicodedata
import numpy as np

K = 15          # longest chunk in letters
P_NULL = 0.02   # prior probability that a group emits nothing
P_SKIP = 0.005  # weight for leaving one whole plaintext word uncoded after a group


def normalise(text):
    """Lower-case, strip accents, keep letters and digits; return list of words."""
    t = unicodedata.normalize("NFD", text.lower())
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    t = t.replace("œ", "oe").replace("æ", "ae")
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return t.split()


def read_cipher(path):
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("frame"):
            continue
        out.extend(int(x) for x in line.split())
    return out


class Plain:
    def __init__(self, words):
        self.words = words
        self.letters = "".join(words)
        self.N = len(self.letters)
        wid = []
        for w, word in enumerate(words):
            wid.extend([w] * len(word))
        self.wid = np.array(wid, dtype=np.int32)
        starts = np.zeros(self.N + 1, dtype=bool)
        ends = np.zeros(self.N + 1, dtype=bool)   # ends[j] true if a word ends just before j
        pos = 0
        for word in words:
            starts[pos] = True
            pos += len(word)
            ends[pos] = True
        self.starts, self.ends = starts, ends
        ws, pos = [], 0
        for word in words:
            ws.append((pos, pos + len(word)))
            pos += len(word)
        self.w_start = np.array([a for a, b in ws], dtype=np.int64)
        self.w_end = np.array([b for a, b in ws], dtype=np.int64)
        # a skipped word carries the same 26**-length letter factor as a coded one
        self.lskip = math.log(P_SKIP) - (self.w_end - self.w_start) * math.log(26.0)
        # chunk ids: cid[j, k] for chunk letters[j:j+k]; -1 if not allowed
        self.chunk_index = {"": 0}
        self.chunks = [""]
        cid = -np.ones((self.N + 1, K + 1), dtype=np.int32)
        cid[:, 0] = 0
        for j in range(self.N):
            for k in range(1, K + 1):
                e = j + k
                if e > self.N:
                    break
                same_word = self.wid[j] == self.wid[e - 1]
                whole = starts[j] and ends[e] and (self.wid[e - 1] - self.wid[j] <= 2)
                if not (same_word or whole):
                    continue
                s = self.letters[j:e]
                c = self.chunk_index.get(s)
                if c is None:
                    c = len(self.chunks)
                    self.chunk_index[s] = c
                    self.chunks.append(s)
                cid[j, k] = c
        self.cid = cid
        self.C = len(self.chunks)
        self.clen = np.array([len(s) for s in self.chunks], dtype=np.int32)


def base_measure(plain, n_tokens, mu_scale=1.0):
    """Prior over chunks: Poisson length prior with the mean implied by the two
    lengths, times 26**-length (uniform over letter strings). With this base
    measure every complete alignment has the same letter factor, so the prior
    prefers no alignment over another except through chunk lengths."""
    mu = mu_scale * plain.N / (n_tokens * (1 - P_NULL))
    plen = np.array([math.exp(-mu) * mu ** k / math.factorial(k) for k in range(K + 1)])
    plen[0] = 0.0
    plen = plen / plen.sum() * (1 - P_NULL)
    plen[0] = P_NULL
    p0 = plen[plain.clen] * (26.0 ** (-plain.clen.astype(float)))
    return p0


NEG = -1e30


def _emission_logs(theta_g, own_i, n_g, p0, alpha, tau=1.0):
    """Leave-one-out emission for one token: the counts of its group minus its
    own expected counts, plus the prior. tau < 1 flattens the whole emission
    (used only in early rounds when a tempering schedule is set)."""
    loo = np.maximum(theta_g - own_i, 0.0)
    pr = (loo + alpha * p0) / (max(n_g - 1.0, 0.0) + alpha)
    # "emits nothing" is never learned: it would be consistent everywhere and
    # so would swallow repeated groups. It always costs the fixed prior weight.
    pr[0] = P_NULL
    lg = np.log(np.maximum(pr, 1e-300))
    return lg if tau == 1.0 else lg * tau


def _bandmask(plain, n):
    """Optional band: token i may start only within band*N letters of the diagonal."""
    b = getattr(plain, 'band', None)
    if not b:
        return None
    N = plain.N
    j = np.arange(N + 1)[None, :]
    centre = (np.arange(n)[:, None] + 0.5) * N / n
    return np.abs(j - centre) <= b * N


def forward_backward(groups, plain, counts, own, ng, p0, alpha):
    """Log-domain forward-backward with leave-one-out emissions.
    counts: [G, C] expected counts from the previous round; own: [n, C] each
    token's own share of them. Returns new counts, new own, log-likelihood."""
    n, N = len(groups), plain.N
    cid = plain.cid
    valid = cid >= 0
    cidc = np.where(valid, cid, 0)
    C = counts.shape[1]
    la = np.full((n + 1, N + 1), NEG)
    la[0, 0] = 0.0
    Ls = []
    bandmask = _bandmask(plain, n)
    for i in range(n):
        g = groups[i]
        le = _emission_logs(counts[g], own[i], ng[g], p0, alpha, getattr(plain, 'tau', 1.0))
        L = np.where(valid, le[cidc], NEG)
        if bandmask is not None:
            L = np.where(bandmask[i][:, None], L, NEG)
        Ls.append(L.astype(np.float32))
        a = la[i]
        nxt = a + L[:, 0]
        for k in range(1, K + 1):
            nxt[k:] = np.logaddexp(nxt[k:], a[:N + 1 - k] + L[:N + 1 - k, k])
        nxt[plain.w_end] = np.logaddexp(nxt[plain.w_end], nxt[plain.w_start] + plain.lskip)
        la[i + 1] = np.maximum(nxt, NEG)
    loglik = la[n, N]
    if loglik <= NEG / 2:
        return None, None, -np.inf
    lb = np.full(N + 1, NEG)
    lb[N] = 0.0
    new_counts = np.zeros_like(counts)
    new_own = np.zeros_like(own)
    for i in range(n - 1, -1, -1):
        L = Ls[i].astype(np.float64)
        a = la[i]
        lbs = lb.copy()
        lbs[plain.w_start] = np.logaddexp(lb[plain.w_start], lb[plain.w_end] + plain.lskip)
        lb = lbs
        T = np.full((N + 1, K + 1), NEG)
        T[:, 0] = L[:, 0] + lb
        for k in range(1, K + 1):
            T[:N + 1 - k, k] = L[:N + 1 - k, k] + lb[k:]
        post = np.exp(np.maximum(a[:, None] + T - loglik, -700.0))
        o = np.bincount(cidc.ravel(), weights=post.ravel(), minlength=C)
        new_own[i] = o
        new_counts[groups[i]] += o
        m = T.max(axis=1)
        lb = np.maximum(m + np.log(np.exp(T - m[:, None]).sum(axis=1)), NEG)
    return new_counts, new_own, float(loglik)


def viterbi(groups, plain, counts, own, ng, p0, alpha):
    n, N = len(groups), plain.N
    cid = plain.cid
    valid = cid >= 0
    cidc = np.where(valid, cid, 0)
    V = np.full(N + 1, NEG)
    V[0] = 0.0
    back = np.zeros((n, N + 1), dtype=np.int8)
    skipfrom = -np.ones((n, N + 1), dtype=np.int32)
    bandmask = _bandmask(plain, n)
    for i in range(n):
        g = groups[i]
        le = _emission_logs(counts[g], own[i], ng[g], p0, alpha)
        L = np.where(valid, le[cidc], NEG)
        if bandmask is not None:
            L = np.where(bandmask[i][:, None], L, NEG)
        best = V + L[:, 0]
        arg = np.zeros(N + 1, dtype=np.int8)
        for k in range(1, K + 1):
            cand = V[:N + 1 - k] + L[:N + 1 - k, k]
            seg = best[k:]
            better = cand > seg
            best[k:] = np.where(better, cand, seg)
            arg[k:] = np.where(better, k, arg[k:])
        sk = best[plain.w_start] + plain.lskip
        took = sk > best[plain.w_end]
        skipped = np.zeros(N + 1, dtype=bool)
        skipped[plain.w_end[took]] = True
        best[plain.w_end[took]] = sk[took]
        skipfrom[i][plain.w_end[took]] = plain.w_start[took]
        V = np.maximum(best, NEG)
        back[i] = arg
    if V[N] <= NEG / 2:
        return None, -np.inf
    spans = []
    j = N
    for i in range(n - 1, -1, -1):
        if skipfrom[i, j] >= 0:
            j = int(skipfrom[i, j])
        k = int(back[i, j])
        spans.append((j - k, j))
        j -= k
    spans.reverse()
    return spans, V[N]


def fit(cipher, words, iters=30, alpha=0.3, verbose=False, band=None, temper=None, mu_scale=1.0):
    """Run EM and return dict with spans (per token), chunks, statistics.

    Emissions are leave-one-out: a token is never explained by its own count,
    so a group seen once always emits from the prior, and a repeated group is
    explained only by what its other occurrences are aligned to."""
    types = sorted(set(cipher))
    gidx = {g: i for i, g in enumerate(types)}
    groups = np.array([gidx[g] for g in cipher], dtype=np.int32)
    plain = Plain(words)
    plain.band = band
    p0 = base_measure(plain, len(cipher), mu_scale)
    G, n = len(types), len(cipher)
    ng = np.bincount(groups, minlength=G).astype(float)
    counts = np.zeros((G, plain.C))
    own = np.zeros((n, plain.C))
    loglik = -np.inf
    for it in range(iters):
        tau = 1.0 if not temper else min(1.0, temper[0] + (1 - temper[0]) * it / float(temper[1]))
        plain.tau = tau
        counts, own, loglik = forward_backward(groups, plain, counts, own, ng, p0, alpha)
        if counts is None:
            return None
        if verbose:
            print("iter", it, "loglik %.1f" % loglik, flush=True)
    plain.tau = 1.0
    spans, vscore = viterbi(groups, plain, counts, own, ng, p0, alpha)
    if spans is None:
        return None
    chunks = [plain.letters[a:b] for a, b in spans]
    res = {"spans": spans, "chunks": chunks, "loglik": float(loglik), "N": plain.N,
           "n_tokens": n, "n_types": G}
    res.update(consistency(cipher, chunks, plain.N))
    return res


def consistency(cipher, chunks, N):
    """S_tok: among tokens of groups that occur at least twice, the share whose
    non-empty chunk is shared by at least one other token of the same group.
    S_let: letters of those tokens' chunks / all plaintext letters."""
    by = {}
    for g, c in zip(cipher, chunks):
        by.setdefault(g, []).append(c)
    rep_tokens = agree_tokens = agree_letters = 0
    for g, cs in by.items():
        if len(cs) < 2:
            continue
        rep_tokens += len(cs)
        cnt = {}
        for c in cs:
            cnt[c] = cnt.get(c, 0) + 1
        for c, m in cnt.items():
            if c and m >= 2:
                agree_tokens += m
                agree_letters += m * len(c)
    return {"S_tok": agree_tokens / max(rep_tokens, 1), "S_let": agree_letters / max(N, 1),
            "rep_tokens": rep_tokens, "agree_tokens": agree_tokens}


def table_from(cipher, chunks):
    """group -> (modal chunk, support of modal, occurrences)."""
    by = {}
    for g, c in zip(cipher, chunks):
        by.setdefault(g, []).append(c)
    tab = {}
    for g, cs in by.items():
        cnt = {}
        for c in cs:
            cnt[c] = cnt.get(c, 0) + 1
        best = sorted(cnt.items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))[0]
        tab[g] = (best[0], best[1], len(cs))
    return tab

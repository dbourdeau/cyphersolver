"""Shared routines for the Whitworth 1708 test (alignment, table rule, held-out scoring).

A "run" is a maximal sequence of code groups between words written in clear; its plaintext is the
printed text between the same clear words, reduced to lower-case letters and digits.
Groups are strings of digits; a disputed group is None (treated as unknown everywhere).
"""
import math, random, re
from collections import Counter, defaultdict

MAXSEG = 16          # longest stretch of plaintext one group may stand for
P_STOP = 0.4         # geometric length prior (neutral over segmentations of a fixed string)
ALPHA = 0.5          # weight of the base distribution against observed counts


def norm(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())


def logp0(seg):
    n = len(seg)
    return math.log(P_STOP) + (n - 1) * math.log(1 - P_STOP) - n * math.log(36.0)


class Aligner:
    """Segment each run's plaintext into one piece per group so that equal numbers get equal pieces.
    Model: for each number a Chinese-restaurant distribution over pieces; base measure uniform over
    segmentations. Blocked Gibbs sampling per run with annealing, then repeated best-path passes."""

    def __init__(self, runs, seed=0):
        self.runs = runs                      # list of (groups, text)
        self.rng = random.Random(seed)
        self.seg = [None] * len(runs)         # current segmentation: list of pieces per run
        self.c = defaultdict(Counter)         # counts[number][piece]
        self.tot = Counter()
        self.ok = [self._feasible(g, t) for g, t in runs]

    @staticmethod
    def _feasible(groups, text):
        return len(groups) <= len(text) <= len(groups) * MAXSEG and len(groups) > 0

    def _lp(self, num, piece):
        if num is None:
            return logp0(piece)
        return math.log((self.c[num][piece] + ALPHA * math.exp(logp0(piece))) / (self.tot[num] + ALPHA))

    def _remove(self, r):
        if self.seg[r] is None:
            return
        for num, piece in zip(self.runs[r][0], self.seg[r]):
            if num is not None:
                self.c[num][piece] -= 1
                self.tot[num] -= 1
        self.seg[r] = None

    def _add(self, r, pieces):
        self.seg[r] = pieces
        for num, piece in zip(self.runs[r][0], pieces):
            if num is not None:
                self.c[num][piece] += 1
                self.tot[num] += 1

    def _lattice(self, r, temp, sample):
        groups, text = self.runs[r]
        k, n = len(groups), len(text)
        NEG = float('-inf')
        # fwd[i][j]: groups 0..i-1 cover text[:j]
        fwd = [[NEG] * (n + 1) for _ in range(k + 1)]
        fwd[0][0] = 0.0
        back = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(k):
            rem = k - i - 1
            for j in range(n + 1):
                a = fwd[i][j]
                if a == NEG:
                    continue
                for L in range(1, MAXSEG + 1):
                    j2 = j + L
                    if j2 > n or n - j2 < rem or n - j2 > rem * MAXSEG:
                        continue
                    s = a + self._lp(groups[i], text[j:j2]) / temp
                    if sample:
                        b = fwd[i + 1][j2]
                        fwd[i + 1][j2] = s if b == NEG else max(b, s) + math.log1p(math.exp(-abs(b - s)))
                    elif s > fwd[i + 1][j2]:
                        fwd[i + 1][j2] = s
                        back[i + 1][j2] = L
        pieces = []
        j = n
        for i in range(k, 0, -1):
            if sample:
                cands, ws = [], []
                for L in range(1, MAXSEG + 1):
                    j0 = j - L
                    if j0 < 0 or fwd[i - 1][j0] == NEG:
                        continue
                    cands.append(L)
                    ws.append(fwd[i - 1][j0] + self._lp(groups[i - 1], text[j0:j]) / temp)
                m = max(ws)
                ws = [math.exp(w - m) for w in ws]
                L = self.rng.choices(cands, ws)[0]
            else:
                L = back[i][j]
            pieces.append(text[j - L:j])
            j -= L
        pieces.reverse()
        return pieces, fwd[k][n]

    def fit(self, sweeps=60, final=8):
        order = [r for r in range(len(self.runs)) if self.ok[r]]
        for r in order:                       # random start
            self._add(r, self._lattice(r, 1.0, True)[0])
        for s in range(sweeps):
            temp = max(1.0, 4.0 * (1 - s / (0.7 * sweeps)))   # anneal from 4 to 1
            self.rng.shuffle(order)
            for r in order:
                self._remove(r)
                self._add(r, self._lattice(r, temp, True)[0])
        for s in range(final):
            for r in order:
                self._remove(r)
                self._add(r, self._lattice(r, 1.0, False)[0])
        return self

    def loglik(self):
        """Joint log probability of the current segmentation (exchangeable, computed sequentially)."""
        c = defaultdict(Counter); tot = Counter(); ll = 0.0
        for r, (groups, text) in enumerate(self.runs):
            if self.seg[r] is None:
                continue
            for num, piece in zip(groups, self.seg[r]):
                if num is None:
                    ll += logp0(piece); continue
                ll += math.log((c[num][piece] + ALPHA * math.exp(logp0(piece))) / (tot[num] + ALPHA))
                c[num][piece] += 1; tot[num] += 1
        return ll


def table_from_alignment(runs, segs):
    """The table rule.
    Tier A: a number seen at least twice whose pieces all agree (one dissent allowed from four sightings up).
    Tier B: a number seen once whose two neighbours in its run are each a run edge or a tier A number
    aligned to its tier A value."""
    occ = defaultdict(list)
    for r, (groups, text) in enumerate(runs):
        if segs[r] is None:
            continue
        for i, (num, piece) in enumerate(zip(groups, segs[r])):
            if num is not None:
                occ[num].append((r, i, piece))
    tierA = {}
    for num, lst in occ.items():
        if len(lst) < 2:
            continue
        cnt = Counter(p for _, _, p in lst)
        piece, top = cnt.most_common(1)[0]
        if top == len(lst) or (len(lst) >= 4 and top == len(lst) - 1):
            tierA[num] = piece
    tierB = {}
    for num, lst in occ.items():
        if len(lst) != 1:
            continue
        r, i, piece = lst[0]
        groups = runs[r][0]
        def fixed(k):
            if k < 0 or k >= len(groups):
                return True
            g = groups[k]
            return g in tierA and segs[r][k] == tierA[g]
        if fixed(i - 1) and fixed(i + 1):
            tierB[num] = piece
    return tierA, tierB


def stable_table(runs, seeds, sweeps=60):
    """Run the aligner once per seed; keep an entry only if every seed gives it the same value and tier-free."""
    tables, fits = [], []
    for sd in seeds:
        al = Aligner(runs, seed=sd).fit(sweeps=sweeps)
        A, B = table_from_alignment(runs, al.seg)
        tables.append((A, B)); fits.append((al.loglik(), sd, al))
    keep = {}
    first = {**tables[0][1], **tables[0][0]}
    for num, piece in first.items():
        if all({**B, **A}.get(num) == piece for A, B in tables):
            tier = 'A' if all(num in A for A, B in tables) else 'B'
            keep[num] = (piece, tier)
    best = max(fits, key=lambda f: f[0])
    return keep, best, fits


def score_run(groups, text, table):
    """Best tiling of the run's plaintext: a group in the table either stands for exactly its value (a hit)
    or, like a group not in the table, for any 1..MAXSEG characters (no hit). Returns (hits, covered groups,
    letters under hits, tiled?). An untileable run scores no hits."""
    k, n = len(groups), len(text)
    cov = sum(1 for g in groups if g is not None and g in table)
    NEG = -1
    best = [[NEG] * (n + 1) for _ in range(k + 1)]
    best[0][0] = 0
    for i in range(k):
        g = groups[i]
        v = table.get(g) if g is not None else None
        for j in range(n + 1):
            a = best[i][j]
            if a == NEG:
                continue
            if v and text.startswith(v, j):
                j2 = j + len(v)
                s = a + 1000 + len(v)          # hits first, then letters under hits
                if s > best[i + 1][j2]:
                    best[i + 1][j2] = s
            for L in range(1, MAXSEG + 1):
                j2 = j + L
                if j2 > n:
                    break
                if a > best[i + 1][j2]:
                    best[i + 1][j2] = a
    b = best[k][n]
    if b == NEG:
        return 0, cov, 0, False
    return b // 1000, cov, b % 1000, True


def score_letter(runs, table):
    hits = cov = letters = total_letters = total_groups = untiled = 0
    for groups, text in runs:
        h, c, l, ok = score_run(groups, text, table)
        hits += h; cov += c; letters += l
        total_letters += len(text); total_groups += len(groups)
        untiled += (not ok)
    return dict(hits=hits, covered=cov, groups=total_groups, hit_letters=letters, letters=total_letters,
                untiled_runs=untiled, H=(hits / cov if cov else 0.0), coverage=(cov / total_groups if total_groups else 0.0),
                letter_share=(letters / total_letters if total_letters else 0.0))


def control_shuffled_values(runs, table, n, seed):
    """Control 1: the table's values dealt out again at random among the table's numbers."""
    rng = random.Random(seed)
    nums = sorted(table); vals = [table[x] for x in nums]
    out = []
    for _ in range(n):
        v = vals[:]; rng.shuffle(v)
        out.append(score_letter(runs, dict(zip(nums, v)))['H'])
    return sorted(out)


def control_rotated_runs(runs, table):
    """Control 2: the true table, each run scored against the plaintext of another run (every rotation)."""
    out = []
    for shift in range(1, len(runs)):
        rot = [(runs[i][0], runs[(i + shift) % len(runs)][1]) for i in range(len(runs))]
        out.append(score_letter(rot, table)['H'])
    return sorted(out)


def pct(sorted_vals, q):
    if not sorted_vals:
        return float('nan')
    i = min(len(sorted_vals) - 1, int(math.ceil(q * len(sorted_vals))) - 1)
    return sorted_vals[max(i, 0)]

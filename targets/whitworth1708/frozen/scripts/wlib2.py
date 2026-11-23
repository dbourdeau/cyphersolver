"""Second Whitworth test: build runs from the interlined originals (State Papers Online, stamped ff. 90 and 110)
and align them with the office's own words, keeping near the place where each word is written.

Input format (transcriptions/spo_f090_deciphered.txt, spo_f110_deciphered.txt): code groups, each followed, where
the office wrote a word above, by that word in square brackets; '[NOTHING ABOVE]' where groups have no word above;
words outside brackets are written in clear. The helper who typed these files attached each word to the groups it
stands above by eye, and is sometimes one or two groups out, so the attachment is used only as a band, not as fact.
"""
import math, re, difflib
from wlib import Aligner, MAXSEG, norm, table_from_alignment


def parse_interlined(path):
    """Returns the list of tokens: ('G', group, alternatives, place) / ('I', word, place) / ('N', '', place) /
    ('W', word, place)."""
    toks = []; page = '?'
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('## page'):
            page = line.split()[2]; continue
        m = re.match(r'(L\d+):\s*(.*)', line)
        if not m:
            continue
        place = f'p{page} {m.group(1)}'
        for part in re.findall(r'\[[^\]]*\]|\{[^}]*\}|\S+', m.group(2)):
            if part.startswith('['):
                if 'NOTHING ABOVE' in part:
                    toks.append(('N', '', place)); continue
                for w in part.strip('[]').split():
                    toks.append(('I', 'and' if w == '&' else w, place))
            elif part.startswith('{x:'):
                continue
            else:
                t = part.rstrip('=')
                mm = re.fullmatch(r'\{\^(.+)\}', t)
                if mm:
                    t = mm.group(1)
                if re.fullmatch(r'[\d?]+(\|[\d?]+)*', t):
                    a = t.split('|'); toks.append(('G', a[0], a[1:], place))
                elif t == '(?)' or re.search(r'[A-Za-z0-9]', t) or t == '&':
                    toks.append(('W', t, place))
    return toks


def duplicate_groups(merged, adjudication, letter):
    """The duplicate's groups in order: the reading both blind transcribers agreed on, else None."""
    out = []
    for l in open(merged, encoding='utf-8').read().splitlines()[1:]:
        idx, kind, status, a, b = (l.split('\t') + [''] * 5)[:5]
        if kind == 'W':
            continue
        out.append(a if status == 'agree' else None)
    return out


def confirmed_groups(toks, dup):
    """A group of the original counts as read only if the helper gave no alternative and the duplicate's agreed
    blind reading at the same place in sequence is the same number. Everything else becomes None (unknown)."""
    og = [t for t in toks if t[0] == 'G']
    keyo = [t[1] if not t[2] and '?' not in t[1] else f'o{i}' for i, t in enumerate(og)]
    keyd = [g if g is not None else f'd{i}' for i, g in enumerate(dup)]
    sm = difflib.SequenceMatcher(None, keyo, keyd, autojunk=False)
    ok = [False] * len(og)
    for a, b, n in sm.get_matching_blocks():
        for k in range(n):
            ok[a + k] = True
    it = iter(ok)
    out = []
    for t in toks:
        if t[0] == 'G':
            out.append(('G', t[1] if next(it) else None, t[2], t[3]))
        else:
            out.append(t)
    return out, sum(ok), len(ok)


def runs_from_tokens(toks):
    """Runs = maximal stretches of groups between words in clear. For each run: groups, the office's text
    (letters and digits of the words written above, in order), and the helper's path: points (groups so far,
    characters so far) after each word or 'nothing above' mark."""
    runs = []; cur = None
    def close():
        nonlocal cur
        if cur and cur['groups']:
            k, n = len(cur['groups']), len(cur['text'])
            if cur['path'][-1] != (k, n):
                cur['path'].append((k, n))
            runs.append(cur)
        cur = None
    for t in toks:
        if t[0] == 'W':
            close(); continue
        if cur is None:
            cur = dict(groups=[], text='', path=[(0, 0)], place=t[-1], words=[])
        if t[0] == 'G':
            cur['groups'].append(t[1])
        elif t[0] == 'I':
            cur['text'] += norm(t[1]); cur['words'].append(t[1])
            cur['path'].append((len(cur['groups']), len(cur['text'])))
        elif t[0] == 'N':
            cur['path'].append((len(cur['groups']), len(cur['text'])))
    close()
    return runs


def band(path, k, n, D):
    """lo[j], hi[j]: the range of 'groups consumed' allowed when j characters are consumed: within D groups of the
    helper's path."""
    lo = [k] * (n + 1); hi = [0] * (n + 1)
    for (g0, t0), (g1, t1) in zip(path, path[1:]):
        for j in range(t0, t1 + 1):
            lo[j] = min(lo[j], g0 - D); hi[j] = max(hi[j], g1 + D)
    lo[0] = 0; hi[0] = 0; lo[n] = k; hi[n] = k
    return lo, hi


class BandAligner(Aligner):
    """wlib.Aligner with the lattice restricted to a band round the helper's path (D groups either side).
    D=None: no band (the first test's aligner). A run that cannot be cut inside its band loses its band."""

    def __init__(self, runs, paths, D, seed=0):
        super().__init__(runs, seed)
        self.bands = []
        self.unbanded = 0
        for (groups, text), path in zip(runs, paths):
            k, n = len(groups), len(text)
            if D is None or not self._feasible(groups, text):
                self.bands.append(None); continue
            b = band(path, k, n, D)
            self.bands.append(b)
        for r in range(len(runs)):
            if self.ok[r] and self.bands[r] is not None and not self._reachable(r):
                self.bands[r] = None; self.unbanded += 1

    def _reachable(self, r):
        groups, text = self.runs[r]; k, n = len(groups), len(text); lo, hi = self.bands[r]
        cur = {0}
        for i in range(k):
            nxt = set()
            for j in cur:
                for L in range(1, MAXSEG + 1):
                    j2 = j + L
                    if j2 > n:
                        break
                    if lo[j2] <= i + 1 <= hi[j2]:
                        nxt.add(j2)
            cur = nxt
            if not cur:
                return False
        return n in cur

    def _lattice(self, r, temp, sample):
        b = self.bands[r]
        if b is None:
            return super()._lattice(r, temp, sample)
        lo, hi = b
        groups, text = self.runs[r]
        k, n = len(groups), len(text)
        NEG = float('-inf')
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
                    if not (lo[j2] <= i + 1 <= hi[j2]):
                        continue
                    s = a + self._lp(groups[i], text[j:j2]) / temp
                    if sample:
                        bb = fwd[i + 1][j2]
                        fwd[i + 1][j2] = s if bb == NEG else max(bb, s) + math.log1p(math.exp(-abs(bb - s)))
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
                    if not (lo[j] <= i <= hi[j]):
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


def stable_table2(runs, paths, D, seeds, sweeps=60):
    """As wlib.stable_table, with the band aligner: an entry is kept only if every seed gives it the same value."""
    tables = []; fits = []
    for sd in seeds:
        al = BandAligner(runs, paths, D, seed=sd).fit(sweeps=sweeps)
        A, B = table_from_alignment(runs, al.seg)
        tables.append((A, B)); fits.append((al.loglik(), sd, al))
    keep = {}
    first = {**tables[0][1], **tables[0][0]}
    for num, piece in first.items():
        if all({**B, **A}.get(num) == piece for A, B in tables):
            keep[num] = (piece, 'A' if all(num in A for A, B in tables) else 'B')
    return keep, max(fits, key=lambda f: f[0]), fits


def load_build(letters):
    """letters: list of (interlined file, merged duplicate tsv, adjudication tsv, name). Returns runs [(groups,
    text)], paths, and a description."""
    runs = []; paths = []; info = []
    for spo, merged, adj, name in letters:
        toks = parse_interlined(spo)
        toks, ok, tot = confirmed_groups(toks, duplicate_groups(merged, adj, name))
        rr = runs_from_tokens(toks)
        for r in rr:
            runs.append((r['groups'], r['text'])); paths.append(r['path'])
        info.append(dict(letter=name, groups=tot, confirmed=ok, runs=len(rr),
                         letters=sum(len(r['text']) for r in rr)))
    return runs, paths, info


# ---- direct entries (one group under one word) and the combined table ----
from collections import Counter, defaultdict


def gloss_units(toks):
    """The helper's attachments: [groups, word(s)] for each bracketed gloss, groups = those typed since the
    previous gloss, 'nothing above' mark or clear word."""
    out = []; g = []; prev = None
    for t in toks:
        if t[0] == 'G':
            g.append(t[1])
        elif t[0] == 'I':
            if prev == 'I' and not g and out:
                out[-1][1] += norm(t[1])
            else:
                out.append([g, norm(t[1])]); g = []
        else:
            g = []
        prev = t[0]
    return out


def direct_table(units):
    """Number -> word for numbers that stand alone under a word at least once and always under the same word.
    Returns (table, sightings, numbers with conflicting words)."""
    c = defaultdict(Counter)
    for g, w in units:
        if len(g) == 1 and g[0] is not None and w:
            c[g[0]][w] += 1
    table = {k: v.most_common(1)[0][0] for k, v in c.items() if len(v) == 1}
    return table, {k: sum(v.values()) for k, v in c.items()}, {k for k, v in c.items() if len(v) > 1}


class SeededAligner(BandAligner):
    """Band aligner whose counts start with the direct entries (weight w per sighting, never removed)."""

    def __init__(self, runs, paths, D, seed=0, direct=None, sightings=None, weight=2):
        super().__init__(runs, paths, D, seed)
        for num, word in (direct or {}).items():
            n = weight * (sightings or {}).get(num, 1)
            self.c[num][word] += n; self.tot[num] += n


def combined_table(runs, paths, units, D, seeds, sweeps=60, weight=2):
    """Final rule of the second test.
    Tier S: direct entry (one group under one word, never under a different word).
    Tier A / B: the first test's table rule applied to the seeded alignment, for numbers with no direct sighting,
    kept only if every seed gives the same value."""
    direct, sight, conflict = direct_table(units)
    tables = []; fits = []
    for sd in seeds:
        al = SeededAligner(runs, paths, D, seed=sd, direct=direct, sightings=sight, weight=weight).fit(sweeps=sweeps)
        A, B = table_from_alignment(runs, al.seg)
        tables.append((A, B)); fits.append((al.loglik(), sd, al))
    keep = {k: (v, 'S') for k, v in direct.items()}
    first = {**tables[0][1], **tables[0][0]}
    for num, piece in first.items():
        if num in sight:                      # has a direct sighting (kept above, or conflicting: left out)
            continue
        if all({**B, **A}.get(num) == piece for A, B in tables):
            keep[num] = (piece, 'A' if all(num in A for A, B in tables) else 'B')
    return keep, max(fits, key=lambda f: f[0]), fits, conflict


def load_build2(letters):
    runs = []; paths = []; info = []; units = []
    for spo, merged, adj, name in letters:
        toks = parse_interlined(spo)
        toks, ok, tot = confirmed_groups(toks, duplicate_groups(merged, adj, name))
        rr = runs_from_tokens(toks)
        for r in rr:
            runs.append((r['groups'], r['text'])); paths.append(r['path'])
        u = gloss_units(toks); units.extend(u)
        info.append(dict(letter=name, groups=tot, confirmed=ok, runs=len(rr), letters=sum(len(r['text']) for r in rr),
                         gloss_units=len(u), one_group_units=sum(len(g) == 1 for g, w in u)))
    return runs, paths, units, info

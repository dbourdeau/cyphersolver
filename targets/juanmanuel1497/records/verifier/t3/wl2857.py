"""Fixed word list and segmentation measure for the catalogue 2857 test (TEST_PLAN_2857.md).

Word list = all forms of output/claver1497_2026-11-16/wordlist_claver_es.tsv (with their counts) plus every form of
Hernando del Pulgar's Cronica (Valencia 1780, IA bub_gb_RB9nAr9N5AkC djvu text) seen at least twice, each normalised
by spnorm.norm (copied unchanged from output/claver1497_2026-11-16/scripts/spnorm.py). Counts are summed.

measure(text): text is a list of segments (strings over a-z and '?'); segments are separated by code groups.
Each segment is normalised letter by letter (the spnorm character rules; doubled letters other than l collapsed)
and segmented by a Viterbi search: a dictionary word costs -ln(count/N), an unknown character costs U.
Result: share of letters (holes '?' included in the denominator) lying inside dictionary words of length >= LMIN.
"""
import math, re, unicodedata, sys
from collections import Counter

U = 10.0


def norm(w):  # == spnorm.norm
    w = w.lower().replace('ç', 'c').replace('z', 'c').replace('ñ', 'n')
    w = unicodedata.normalize('NFD', w); w = ''.join(c for c in w if unicodedata.category(c) != 'Mn')
    w = w.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('k', 'c').replace('w', 'u')
    w = re.sub(r'([a-km-z])\1+', r'\1', w)
    if len(w) > 1 and w[0] == 'h': w = w[1:]
    return w


def norm_string(s):
    """Character rules of norm() on a running string; '?' kept; no initial-h rule (word starts are unknown)."""
    s = s.lower().replace('ç', 'c').replace('z', 'c').replace('ñ', 'n')
    s = s.replace('v', 'u').replace('j', 'i').replace('y', 'i').replace('k', 'c').replace('w', 'u')
    return re.sub(r'([a-km-z])\1+', r'\1', s)


def build(claver_tsv, pulgar_txt):
    c = Counter()
    for row in open(claver_tsv, encoding='utf8'):
        w, n = row.rstrip('\n').split('\t')
        c[norm(w)] += int(n)
    pc = Counter()
    txt = open(pulgar_txt, encoding='utf8', errors='replace').read()
    for w in re.findall(r"[^\W\d_]+", txt):
        pc[norm(w)] += 1
    for w, n in pc.items():
        if n >= 2 and w:
            c[w] += n
    return c


class Seg:
    def __init__(self, counts):
        self.N = sum(counts.values())
        self.cost = {w: -math.log(n / self.N) for w, n in counts.items() if w}
        self.maxlen = max(len(w) for w in self.cost)

    def segment(self, s):
        n = len(s); best = [0.0] + [math.inf] * n; back = [None] * (n + 1)
        for i in range(1, n + 1):
            c = best[i - 1] + U
            if c < best[i]:
                best[i], back[i] = c, (i - 1, False)
            for j in range(max(0, i - self.maxlen), i):
                w = s[j:i]
                if '?' in w:
                    continue
                k = self.cost.get(w)
                if k is not None and best[j] + k < best[i]:
                    best[i], back[i] = best[j] + k, (j, True)
        toks, i = [], n
        while i > 0:
            j, isw = back[i]; toks.append((s[j:i], isw)); i = j
        return toks[::-1]

    def measure(self, segments, lmin):
        cov = tot = 0; out = []
        for seg in segments:
            s = norm_string(seg)
            tot += len(s)
            for w, isw in self.segment(s):
                if isw and len(w) >= lmin:
                    cov += len(w)
                out.append(w if isw else w.upper())
        return (cov / tot if tot else 0.0), out


def run_measure(seg, segments, minrun_letters, minrun_tokens):
    """Variant used by the plan: a dictionary word counts only inside a RUN of consecutive dictionary-word tokens
    (no unknown character between them, within one segment) that has at least minrun_tokens tokens and at least
    minrun_letters letters. Share = counted letters / all letters (holes included)."""
    cov = tot = 0; out = []
    for sgm in segments:
        s = norm_string(sgm); tot += len(s)
        toks = seg.segment(s); run = []
        def flush():
            nonlocal cov
            if len(run) >= minrun_tokens and sum(len(w) for w in run) >= minrun_letters:
                cov += sum(len(w) for w in run); out.append('[' + ' '.join(run) + ']')
            else:
                out.extend(run)
        for w, isw in toks + [('', False)]:
            if isw:
                run.append(w)
            else:
                flush(); run = []
                if w: out.append(w.upper())
    return (cov / tot if tot else 0.0), out


def build_claver_only(claver_tsv):
    c = Counter()
    for row in open(claver_tsv, encoding='utf8'):
        w, n = row.rstrip('\n').split('\t')
        c[norm(w)] += int(n)
    return c


def sandwich_measure(seg, segments, lmin=3):
    """Letters in dictionary words of length >= lmin, plus letters of shorter dictionary words that stand directly
    between two such words (or between such a word and a segment edge). Share over all letters, holes included."""
    cov = tot = 0; out = []
    for sgm in segments:
        s = norm_string(sgm); tot += len(s)
        toks = seg.segment(s)
        longw = [isw and len(w) >= lmin for w, isw in toks]
        for i, (w, isw) in enumerate(toks):
            ok = longw[i]
            if isw and not ok:
                left = (i == 0) or longw[i - 1]
                right = (i == len(toks) - 1) or longw[i + 1]
                ok = left and right and not (i == 0 and i == len(toks) - 1)
            if ok:
                cov += len(w)
            out.append(w if (isw and ok) else (w.lower() if isw else w.upper()) + ('*' if isw else ''))
    return (cov / tot if tot else 0.0), out


def build_claver_pulgar_long(claver_tsv, pulgar_txt, minlen=4, mincount=2):
    """Claver list (all forms) + Pulgar forms of at least minlen letters seen at least mincount times."""
    c = build_claver_only(claver_tsv)
    pc = Counter()
    txt = open(pulgar_txt, encoding='utf8', errors='replace').read()
    for w in re.findall(r"[^\W\d_]+", txt):
        pc[norm(w)] += 1
    for w, n in pc.items():
        if n >= mincount and len(w) >= minlen:
            c[w] += n
    return c

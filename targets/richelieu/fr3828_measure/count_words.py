"""Read share over cipher words only (README Conventions, 16 and 19 Nov 2026; issue #728), per letter.

Usage:  python fr3828_measure/count_words.py fr3828_measure/word_count.tsv
A code (C) or isolated word code (W) is one word; a run (R) is split at spaces and apostrophes. Holes: {x} probable,
[x] restored, ‹…› unresolved. Read: >= 95% of cipher words, or, under 40 words, holes <= max(2, 5%) (the floor).
"""
import re, sys, collections
tot = collections.OrderedDict()
for l in open(sys.argv[1], encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    L, u, r = l.rstrip('\n').split('\t'); s, h = tot.get(L, (0, 0))
    if u in 'CW':
        hole = r[0] in '{[‹'; s += 0 if hole else 1; h += 1 if hole else 0
    else:
        for w in re.findall(r"\{[^}]*\}|\[[^\]]*\]|‹[^›]*›|[^\s']+", r):
            if w[0] in '{[‹': h += len(re.findall(r"[^\s']+", w.strip('{}[]‹›')))
            else: s += 1
    tot[L] = (s, h)
S = H = 0
for L, (s, h) in tot.items():
    n = s + h; S += s; H += h
    cls = 'read' if (s / n >= 0.95 or (n < 40 and h <= max(2, 0.05 * n))) else 'read in part'
    flo = ' (floor, < 40 words)' if s / n < 0.95 and cls == 'read' else ''
    print(f"{L}\t{s}/{n}\t{s/n:.3f}\tholes {h}\t{cls}{flo}")
print(f"TOTAL\t{S}/{S+H}\t{S/(S+H):.3f}")

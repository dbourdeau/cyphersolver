"""Shared code for the Code No. 15 key build and held-out test (output/code15_1793_2026-11-28)."""
import csv, re, math
from functools import lru_cache

SUFFIX = {'=': ('s', 'es'), '+': ('ed', 'd'), 'x': ('ed', 'd')}

def load_groups(path):
    docs = {}
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        docs.setdefault(r['doc'], []).append((int(r['line']), int(r['pos']), r['group']))
    return docs

def parse(tok):
    """-> (number or None if unreadable/doubtful, mark, deleted)"""
    if tok.startswith('[del'):
        return None, '=' if tok.endswith('=') else '', True
    mark = ''
    m = re.match(r'^([0-9?\[\]]+)([=+x#]*)$', tok)
    if not m:
        return None, '', False
    num, marks = m.group(1), m.group(2)
    for c in '=+x':
        if c in marks: mark = c
    if '?' in num or '[' in num:
        return None, mark, False
    return num, mark, False

def words_of(text):
    return [re.sub(r'[^a-z]', '', w.lower()) for w in text.split() if re.sub(r'[^a-z]', '', w.lower())]

def matches(value, mark, piece):
    if piece == value: return True
    for s in SUFFIX.get(mark, ()):
        if piece == value + s: return True
    return False

def base_of(mark, piece):
    """Possible base values for a group with this mark covering this piece."""
    out = [piece]
    for s in SUFFIX.get(mark, ()):
        if piece.endswith(s) and len(piece) > len(s): out.append(piece[:-len(s)])
    return out

def pieces_from(words, wi, ci):
    """All pieces a group can take starting at word wi, char ci: (piece, new_wi, new_ci, kind)."""
    w = words[wi]; out = []
    for cj in range(ci + 1, len(w) + 1):
        kind = 'word' if (ci == 0 and cj == len(w)) else 'part'
        nwi, nci = (wi + 1, 0) if cj == len(w) else (wi, cj)
        out.append((w[ci:cj], nwi, nci, kind))
    if ci == 0 and wi + 1 < len(words):
        out.append((w + ' ' + words[wi + 1], wi + 2, 0, 'phrase'))
    return out

def align(groups, words, score):
    """groups: list of (num, mark). Best monotone segmentation; returns (total, [(group index, piece)])."""
    import sys
    sys.setrecursionlimit(100000)
    G, Wn = len(groups), len(words)
    @lru_cache(maxsize=None)
    def best(gi, wi, ci):
        if gi == G:
            return (0.0, ()) if wi == Wn else (-1e9, ())
        if wi >= Wn:
            return (-1e9, ())
        # remaining groups must be <= remaining characters roughly
        bestv = (-1e9, ())
        for piece, nwi, nci, kind in pieces_from(words, wi, ci):
            s = score(groups[gi], piece, kind)
            sub = best(gi + 1, nwi, nci)
            if sub[0] <= -1e8: continue
            v = s + sub[0]
            if v > bestv[0]:
                bestv = (v, ((gi, piece),) + sub[1])
        return bestv
    r = best(0, 0, 0)
    best.cache_clear()
    return r[0], list(r[1])

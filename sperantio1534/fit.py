"""Fit lexicon words to the sign stream.

The seed key reads, but several signs are homophones or look-alikes merged in
transcription (4 = e/i, o = b, # = o, O = l/b ...). Rather than force one value per
sign, each sign carries a set of possible values (ALT); a Viterbi pass over the
letter's sign stream then chooses the segmentation into corpus words that scores best.
Unmatchable stretches are emitted raw, in <>, and counted as unread.

Usage: python fit.py 248   (Latin pages)   |   python fit.py 250   (German pages)
"""
import collections
import os
import pickle
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import corpora, lm

import dec

HERE = os.path.dirname(os.path.abspath(__file__))
MAXW = 16

# Alternatives per sign: seed value first, then the look-alike/homophone values that
# the gloss and the clear passages show are also possible.
EXTRA = {
    '4': 'ei', 'o': 'bo', '#': 'oc', 'O': 'lbt', 'd': 'lt', 'E': 'd', 'b': 'hb',
    'H': 'uv', '3': 'u', 'V': 'uv', 'c': 'ck', 'n': 'cn', 'K': 'ck', 'e': 'xch',
    'z': '', '(': '', 'B': 'sd', 'G': 'dg', 'J': 'p', 'u': 'tn', 't': 'lgn',
    'W': 's', 'j': 'a', 'l': 't', 'k': 'u', 'p': 'i', 'I': 'l', 'T': 'g',
    '%': 'e', '&': 'q', '8': 'n', '9': 'o', 'R': '', 'N': '', 'X': '', '1': '',
    'f': 'f', '6': 'd', 'Z': 'q', 'F': 't', 'U': 'h', 'Y': 'h', 'a': 'p',
    'A': 'p', 'D': 'f', 'L': 's', 'M': 'm', 'P': 'o', 'Q': 'a', 'm': 'i',
    'q': 'n', 's': 'a', 'v': 'r', 'w': 'e', 'x': 's', 'y': 't', '5': 'a',
    '7': 'm', '@': 't', 'g': 'r', 'h': 'i',
}


# Two-letter values: the German pages spell ch / ck / sch with a single sign.
DIGRAPH = {'d': ['ch'], 'K': ['ch', 'ck'], 'c': ['ch', 'ck'], 'e': ['ch'], 'L': ['sch'],
           'B': ['ss'], 'W': ['ss'], 'f': ['ff'], 'z': ['tz'], 'u': ['th']}


def alts(key):
    a = {}
    for sg, v in key.items():
        s = set(EXTRA.get(sg, ''))
        if v and v != '_' and len(v) == 1:
            s.add(v)
        a[sg] = s
    for sg, v in EXTRA.items():
        a.setdefault(sg, set(v))
    for sg, vs in DIGRAPH.items():
        a.setdefault(sg, set()).update(vs)
    return a


def lexicon(which):
    cache = os.path.join(HERE, 'lex_%s.pkl' % which)
    if os.path.exists(cache):
        return pickle.load(open(cache, 'rb'))
    if which == 'la':
        text, scheme = corpora.text(['la-gutenberg']), 'latin'
    else:
        text, scheme = corpora.text(['de-dta-1470-1610']), 'early'
    lex = collections.Counter(lm.norm(text, scheme, spaces=True).split())
    lex = collections.Counter({w: c for w, c in lex.items() if len(w) <= MAXW})
    pickle.dump(lex, open(cache, 'wb'))
    return lex


def stream(pages):
    """(signs, line-index) for the pages wanted, clear passages marked as '|'."""
    sgs, marks = [], []
    for pg, n, s in dec.lines(os.path.join(HERE, 'transcription.txt')):
        if not pg.startswith(pages):
            continue
        for t in dec.tokens(s):
            if t.startswith('['):
                sgs.append(('CLEAR', t[1:-1]))
            elif t != ':':
                sgs.append(('S', t))
        marks.append((pg, n, len(sgs)))
    return sgs, marks


def fits(sets, w):
    """True if each sign in turn can spell one or two letters of w, using up all of both."""
    reach = {0}
    for st in sets:
        nxt = set()
        for p in reach:
            if p < len(w) and w[p] in st:
                nxt.add(p + 1)
            if p + 1 < len(w) and w[p:p + 2] in st:
                nxt.add(p + 2)
        if not nxt:
            return False
        reach = nxt
    return len(w) in reach


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else '248'
    lang = 'la' if which == '248' else 'de'
    key = dec.load_key(os.path.join(HERE, 'key.txt'))
    A = alts(key)
    lex = lexicon(lang)
    tot = sum(lex.values())
    import math
    logp = {w: math.log(c / tot) for w, c in lex.items()}
    TRIE = {}
    for w in logp:
        d = TRIE
        for ch in w:
            d = d.setdefault(ch, {})
        d['$'] = w

    sgs, marks = stream(('248',) if which == '248' else ('250', '251'))
    n = len(sgs)
    # candidate words startable at each position
    best = [-1e18] * (n + 1)
    back = [None] * (n + 1)
    best[0] = 0.0
    for i in range(n):
        if best[i] <= -1e17:
            continue
        kind, val = sgs[i]
        if kind == 'CLEAR':
            sc = best[i] - 1.0
            if sc > best[i + 1]:
                best[i + 1], back[i + 1] = sc, (i, '[%s]' % val, True)
            continue
        # walk the trie: each sign spells one or two letters, so several trie nodes
        # stay live at once; every node that is a word end gives a candidate.
        live = {(): None}
        nodes = [TRIE]
        L = 0
        cur = [TRIE]
        while cur and L < MAXW and i + L < n:
            k, sg = sgs[i + L]
            if k == 'CLEAR':
                break
            st = A.get(sg, set())
            if not st:
                break
            L += 1
            nxt = []
            for nd in cur:
                for v in st:
                    d = nd
                    for ch in v:
                        d = d.get(ch)
                        if d is None:
                            break
                    if d is not None:
                        nxt.append(d)
            cur = nxt
            for nd in cur:
                w = nd.get('$')
                if w:
                    sc = best[i] + logp[w] - 1.0
                    if sc > best[i + L]:
                        best[i + L], back[i + L] = sc, (i, w, True)
        # fall back: one sign emitted raw
        sc = best[i] - 12.0
        if sc > best[i + 1]:
            best[i + 1], back[i + 1] = sc, (i, key.get(sgs[i][1], '?'), False)

    out, i = [], n
    while i > 0:
        j, w, ok = back[i]
        out.append((j, w, ok))
        i = j
    out.reverse()

    pos2line = {}
    prev = 0
    for pg, ln, end in marks:
        for p in range(prev, end):
            pos2line[p] = (pg, ln)
        prev = end
    cur, buf, res = None, [], []
    for j, w, ok in out:
        pl = pos2line.get(j, cur)
        if pl != cur and buf:
            res.append((cur, buf))
            buf = []
        cur = pl
        buf.append(w if ok else '<%s>' % w)
    if buf:
        res.append((cur, buf))
    for (pg, ln), ws in res:
        print('%s %s %s' % (pg, ln, ' '.join(ws)))


if __name__ == '__main__':
    main()

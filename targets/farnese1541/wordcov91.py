"""Word coverage of an unspaced Italian decode: Viterbi segmentation with a unigram model of the Nuntiaturberichte
word list (../vatican5/it_words.json, 30,000 words), unknown stretches charged per letter. Coverage = share of letters that
fall in known words of >= minlen letters.

  from wordcov91 import coverage, segment
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
_W = None


def words():
    global _W
    if _W is None:
        wl = json.load(open(os.path.join(HERE, '..', 'vatican5', 'it_words.json'), encoding='utf-8'))
        tot = sum(c for _, c in wl)
        _W = {w.replace('j', 'i').replace('v', 'u'): math.log(c / tot) for w, c in wl if c >= 3}
    return _W


def segment(text, unk=-12.0, maxlen=18):
    W = words()
    n = len(text)
    best = [0.0] + [-1e18] * n
    back = [0] * (n + 1)
    for j in range(1, n + 1):
        for i in range(max(0, j - maxlen), j):
            w = text[i:j]
            s = W.get(w)
            if s is None:
                if j - i > 1:
                    continue
                s = unk
            if best[i] + s > best[j]:
                best[j] = best[i] + s; back[j] = i
    out, j = [], n
    while j > 0:
        i = back[j]; out.append(text[i:j]); j = i
    return out[::-1]


def coverage(text, minlen=3):
    text = ''.join(c for c in text if c.isalpha())
    W = words()
    seg = segment(text)
    good = sum(len(w) for w in seg if len(w) >= minlen and w in W)
    return good / max(1, len(text)), seg

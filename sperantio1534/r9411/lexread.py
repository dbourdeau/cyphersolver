"""Lexicon reading for the R9412 decrypt.

Two jobs:
  measure  - segment the space-less decrypt into words from the period corpus (Viterbi over unigram word
             probabilities) and report the share of characters that land in real words. This is a direct
             measure of "reads as sense", unlike an n-gram score.
  repair   - hill-climb transcription changes (shape neighbours only) and accept one ONLY when it raises
             that share. An n-gram score can be improved by turning a word into a non-word; word coverage
             cannot.

  python kaa4591/r9411/lexread.py measure DECRYPT
  python kaa4591/r9411/lexread.py repair TRANSCRIPTION KEY OUT
"""
import math, re, sys, os, collections

ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
CORPUS = os.path.join(ROOT, 'lang', 'corpora', 'de-dta-1470-1610.txt')

def lexicon():
    freq = collections.Counter()
    with open(CORPUS, encoding='utf8', errors='ignore') as f:
        for line in f:
            for w in re.findall(r'[a-zäöüß]+', line.lower()):
                freq[w] += 1
    total = sum(freq.values())
    return freq, total

FREQ, TOTAL = lexicon()
MAXW = 18
LOGP = {w: math.log(c / TOTAL) for w, c in FREQ.items() if c >= 3}
UNK = math.log(1e-9)

def segment(s):
    n = len(s)
    best = [(-1e18, 0)] * (n + 1); best[0] = (0.0, 0)
    for i in range(1, n + 1):
        for k in range(1, min(MAXW, i) + 1):
            w = s[i - k:i]
            sc = LOGP.get(w, UNK - 2.0 * k)
            v = best[i - k][0] + sc
            if v > best[i][0]: best[i] = (v, k)
    out = []; i = n
    while i > 0:
        k = best[i][1]; out.append(s[i - k:i]); i -= k
    return out[::-1]

MINLEN = int(os.environ.get('LEX_MINLEN', '5'))

def coverage(s):
    """share of characters in LONG words the period corpus has.

    Short words are excluded on purpose: any string of letters decomposes into 'und', 'sch', 'den' and the
    like, so counting them rewards garbage. Only words of MINLEN letters or more (default 5) count."""
    words = segment(s)
    good = sum(len(w) for w in words if len(w) >= MINLEN and w in LOGP)
    return good / max(len(s), 1), words

def load_lines(path):
    out = []
    for l in open(path, encoding='utf8'):
        m = re.match(r'(\d+) (.*)', l.strip())
        if m: out.append((m.group(1), re.sub('[A-Z]+', ' ', m.group(2)).replace('·', '')))
    return out

if sys.argv[1] == 'measure':
    lines = load_lines(sys.argv[2])
    tot = good = 0
    for n, t in lines:
        for part in t.split():
            c, words = coverage(part)
            good += c * len(part); tot += len(part)
            if len(sys.argv) > 3: print(n, ' '.join(words))
    print(f'word coverage {good/tot:.3f} over {tot} chars')

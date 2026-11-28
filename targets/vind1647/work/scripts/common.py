"""Shared helpers for the vind1647 runs: read a transcription, build a letter 4-gram model from a lexicon of this
repository (lang/lexicons/<lang>.json.gz, words weighted by frequency, with word boundaries).
The language is taken from the environment variable VIND_LANG (la, da or de; default la)."""
import gzip, json, math, os, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]                      # targets/vind1647/work/scripts -> repository root
LANG = os.environ.get('VIND_LANG', 'la')
LEX = REPO / 'lang' / 'lexicons' / ('%s.json.gz' % LANG)
TRANS = HERE.parents[1] / 'transcription_frozen.txt'
ROMAN_KEEP = ('in', 'id', 'mi', 'di', 'dum', 'cum', 'mox', 'dic', 'dux', 'lux', 'uix')

def norm(w):
    w = w.lower()
    if LANG == 'la': w = w.replace('j', 'i').replace('v', 'u')
    w = w.replace('æ', 'ae').replace('ø', 'oe').replace('å', 'aa').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    return re.sub('[^a-z]', '', w)

def read_lines(path=TRANS):
    """Return [(line number, cipher word)], joining a word hyphenated with '=' at line end to the next line's first word."""
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip():
            continue
        body = line.split('#')[0]
        num, rest = body.split(None, 1)
        out.append((int(num), rest.split()))
    words = []; carry = None
    for num, ws in out:
        for i, w in enumerate(ws):
            if carry is not None:
                w = carry + w; carry = None
            if w.endswith('=') and i == len(ws) - 1:
                carry = w[:-1]; continue
            words.append((num, w))
    return words

def lexicon():
    """Lexicon words, normalised; words made only of Roman-numeral letters are left out unless listed in ROMAN_KEEP."""
    d = json.load(gzip.open(LEX))
    lex = {}
    for w, f in d.items():
        n = norm(w)
        if n and (not re.fullmatch('[ivxlcdm]+', n) or n in ROMAN_KEEP):
            lex[n] = lex.get(n, 0) + f
    return lex

def model(lex, n=4):
    counts = {}; tot = 0
    for w, f in lex.items():
        s = ' ' + w + ' '
        for i in range(len(s) - n + 1):
            g = s[i:i + n]; counts[g] = counts.get(g, 0) + f; tot += f
    floor = math.log10(0.01 / tot)
    return {g: math.log10(c / tot) for g, c in counts.items()}, floor

def score(text, m, floor, n=4):
    s = ' ' + text + ' '
    return sum(m.get(s[i:i + n], floor) for i in range(len(s) - n + 1))

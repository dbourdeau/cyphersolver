"""v2 verify sweep (23 Oct 2026): score a reading body with every conjectural or supplied word counted as a hole.

    python v2_score.py <file> [lang]       file: a reading (body after '## Reading', else the whole file)

Before scoring, every bracket that marks a conjecture or a supplied word becomes one explicit hole per word it holds:
[word?] [?word] [x?] [word] (lower-case, i.e. not a resolved code such as [SUA MAESTA]) and part-words like
[ne]glect. A bare mark ([...] [?] {?}) is one unread word; a mark that carries its size ([... 4], [3 groups]) is that
many (14 Nov 2026). Not holes (16 Nov 2026): view and line markers ([v006r] [f. 12r] [image 3]), a read sign or code
given with its value ([sign = Venetorum], [94=ce]) and a bold code number's value in brackets (**94,** [le marquis]).
Prints the plain score (_check_reading word list) and the explicit-hole score (b17 HOLES=1).
"""
import os, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr


def body_of(t):
    m = re.search(r'^## Reading(?![ \t]*(?:notes?|conventions|marks|review|check))[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M | re.I)
    return m.group(1) if m else t


EDITORIAL = {'autograph', 'sic', 'clear', 'cipher', 'margin', 'in margin', 'signature', 'signed', 'seal', 'address',
             'dorse', 'endorsement', 'blank', 'struck', 'cancelled', 'struck out', 'postscript', 'verso', 'recto', 'clear text',
             'in cipher', 'in clear', 'date', 'docket'}


# A hole mark that carries its size (14 Nov 2026, owner decision: the read share counts holes by words, not by marks).
# "[... 4]" / "[… 4]" / "{... 4}" = four unread words. Forms already in use are recognised too: "[3 groups]",
# "[... 3 words]", "[2 unread]", "[?2 groups, 5 letters]", "[name, 9 groups unresolved]". The dots must be followed
# by a space: "[..1]" and "[?100]" stay one unread code. Letters, signs and figures are not words and give no size.
SIZED_DOTS = re.compile(r'\s*(?:\.{3,}|…)\s+(?:about\s+|c\.\s*|~\s*)?(\d{1,3})\s*(?:(?:unread\s+)?(?:words?|groups?)|unread)?\s*')
SIZED_UNIT = re.compile(r'(?<![\w.])(\d{1,3})\s+(?:unread\s+)?(?:words?|groups?|unread)\b(?!\s+(?:struck|cancelled|deleted|in\s+clear))', re.I)


def sized(inner):
    """Number of unread words a hole mark says it covers, or None when the mark carries no size."""
    m = SIZED_DOTS.fullmatch(inner)
    if not m and len(inner) <= 60:
        m = SIZED_UNIT.search(inner)
    return max(1, int(m.group(1))) if m else None


# View, page and line markers that are not text (16 Nov 2026, R23 scan): [v006r] [12r] [106v] [image 3] [img 4]
# [view 6] [frame 0099] [canvas 52] [page 2] [col. 2]. A bare number [202] stays an unvalued code (one hole).
MARKER = re.compile(r'\[(?:v\d{1,4}[rv]|\d{1,4}[rv]|(?:image|img|view|frame|canvas|scan|IMG)\.?\s*\d{1,5}[rv]?(?:\s*(?:left|right|[rv]))?)\]', re.I)
# A read sign or code given with its value (16 Nov 2026, R23 scan: beatrice1482 "[sign = Venetorum]"): the value is
# read, not supplied. The left side is a sign, a symbol, a number or nothing; a "?" or a word such as "missing"
# keeps it a hole, and a left side that is a folio marker ("[f. 6r = P3]") makes it a marker.
GLOSS_EQ = re.compile(r'\[([^\]\n=?]{0,12})=([^\]\n?]+)\]')
GLOSS_LEFT = re.compile(r'\s*(?:sign|code|cipher|group|\d{1,5}|[^\w\s]{1,3}|[A-Za-z]{1,3}\d{0,4})?\s*', re.I)
GLOSS_STOP = re.compile(r'missing|unread|lost|illegible|uncertain|doubtful|unclear|unresolved|not read|\.\.|…', re.I)
MARKER_LEFT = re.compile(r'\s*(?:(?:f|fol|p|pp|l)\.?\s*\d+[rv]?|(?:image|img|view|frame|canvas|scan)\.?\s*\d+[rv]?)\s*', re.I)


def gloss_eq(m):
    left, right = m.group(1), m.group(2)
    if MARKER_LEFT.fullmatch(left): return ' '
    if not GLOSS_LEFT.fullmatch(left) or GLOSS_STOP.search(right) or not re.search(r'[^\W\d_]', right) or len(right.split()) > 6:
        return m.group(0)
    return ' ' + right.strip() + ' '


# A code written as a bold number with its value in brackets right after it (16 Nov 2026, R23 scan: nevers1587
# "**94,** [le marquis]"): the value is read from the key, not supplied. Only after a bold number: a plain number
# before a bracket is as often a date or a folio ("30 [Aprilis]", "1586 [clear]").
# The value goes inside the bold, so that a reading that marks its cipher in bold counts it as a cipher word.
CODE_GLOSS = re.compile(r'(\*\*\d{1,5}[,.;:]?\*\*)[,.;:]?[ \t]*\[([^\]\n?…]*[^\W\d_][^\]\n?…]*)\]')


def holes(t):
    def rep(m):
        inner = m.group(1)
        n = sized(inner)
        if n is not None:
            return ' '.join(['[?]'] * n)
        if re.fullmatch(r'[\s\d.?…*+-]*', inner) or len(inner.strip()) <= 2:   # [Π] [R] [#]: one unread sign
            return '[?]'
        words = re.findall(r'[^\W\d_]+', inner)
        if not inner.lstrip().startswith('?') and (len(words) >= 5 or inner.strip().lower() in EDITORIAL):
            return ' '   # a quoted clear passage ("[… selon que …]") or an editorial note ("[autograph]"): not text read here
        if '?' in inner or inner == inner.lower():
            n = max(1, len(re.findall(r'[^\W\d_]+', inner)))
            return ' '.join(['[?]'] * n)
        return m.group(0)
    t = re.sub(r'\[(?:l|ll|f|ff|fol|p|pp|c|col|line|page)\.?\s*[\divxlcrv,\s–-]+\]', ' ', t, flags=re.I)   # [l. 12] [f. 79v]: markers
    t = MARKER.sub(' ', t)                                        # [v006r] [12r] [image 3] [view 6] [frame 0099]: markers
    t = GLOSS_EQ.sub(gloss_eq, t)                                 # [sign = Venetorum] [94=ce]: a read sign or code
    t = CODE_GLOSS.sub(lambda m: m.group(1)[:-2] + ' ' + m.group(2) + '**', t)   # **94,** [le marquis]: a read code's value
    # {+x} supplied, {-x} dropped (14 Nov 2026, after Brice Dudout, PR #565). Standing alone, {+word} is a word the
    # reader supplied: a hole; {-x} is a group the reader dropped: not text. Inside a word (actuellemen{+t}, pro{-u}c)
    # they mark a one-letter emendation of a word that is read from the cipher: the word stays read.
    t = re.sub(r'(?<![^\W\d_])\{\+[^}\n]*\}(?![^\W\d_])', lambda m: ' '.join(['[?]'] * max(1, len(re.findall(r'[^\W\d_]+', m.group(0))))), t)
    t = re.sub(r'(?<![^\W\d_])\{-[^}\n]*\}(?![^\W\d_])', ' ', t)
    t = re.sub(r'\{\+([^}\n?]*)\}', r'\1', t)
    t = re.sub(r'\{-[^}\n?]*\}', '', t)
    t = re.sub(r'\{([^}\n]*\?[^}\n]*|[\s.…]*|\s*(?:\.{3,}|…)\s+\d{1,3}[^}\n]{0,20})\}',lambda m: rep(re.match(r'(.*)', m.group(1))), t)   # {?} {?word} {…}: unread
    t = re.sub(r'\[([^\]\n]*)\]', rep, t)
    t = re.sub(r'(\w*)\[\?\](\w*)', lambda m: '[?]' if (m.group(1) or m.group(2)) else m.group(0), t)
    return t


def score(text, lang, all_known):
    saved = cr._LEX.get(lang)
    if all_known:
        class _All(dict):
            def __contains__(self, k): return True
        cr._LEX[lang] = _All()
    try:
        return cr.score_text(text, lang)
    finally:
        if all_known:
            if saved is None: cr._LEX.pop(lang, None)
            else: cr._LEX[lang] = saved


if __name__ == '__main__':
    f, lang = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'en')
    b = holes(body_of(pathlib.Path(f).read_text(encoding='utf8')))
    if os.environ.get('SHOW'): print(b)
    cr.lexicon(lang)
    p, h = score(b, lang, False), score(b, lang, True)
    print(f'{f}: plain {p["clean_share"]} ({p["clean"]}/{p["sentences"]}), explicit holes {h["clean_share"]} '
          f'({h["clean"]}/{h["sentences"]}), hole rate {h["hole_rate"]}, words {h["words"]}')

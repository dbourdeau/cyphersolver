"""v2 verify sweep (23 Oct 2026): score a reading body with every conjectural or supplied word counted as a hole.

    python v2_score.py <file> [lang]       file: a reading (body after '## Reading', else the whole file)

Before scoring, every bracket that marks a conjecture or a supplied word becomes one explicit hole per word it holds:
[word?] [?word] [x?] [word] (lower-case, i.e. not a resolved code such as [SUA MAESTA]) and part-words like
[ne]glect. A bare mark ([...] [?] {?}) is one unread word; a mark that carries its size ([... 4], [3 groups]) is that
many (14 Nov 2026). Prints the plain score (_check_reading word list) and the explicit-hole score (b17 HOLES=1).
"""
import os, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'docs')); sys.path.insert(0, str(ROOT))
import _check_reading as cr


def body_of(t):
    m = re.search(r'^## Reading[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
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
    t = re.sub(r'\[(?:l|ll|f|ff|fol|p|pp|c|line|page)\.?\s*[\divxlcrv,\s–-]+\]', ' ', t, flags=re.I)   # [l. 12] [f. 79v]: markers
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

"""List the sentences Dan's checker counts as not clean, with their hole words (diagnostic only)."""
import sys, re, os
sys.path.insert(0, sys.argv[1]); sys.path.insert(0, os.path.join(sys.argv[1], 'docs'))
import _check_reading as C
raw = open(sys.argv[2], encoding='utf8').read(); text = C.clean_text(raw)
lang, cov = C.detect(text); text = C.CODE.sub(' CODEWORD ', text); lex = C.lexicon(lang)
others = [C.lexicon(lg) for lg in C.languages() if lg != lang]
for s in C.sentences(text):
    ws = [(w, gap) for tok in s for w, gap in C.words_of(tok)]
    known = lambda lx: sum(1 for w, gap in ws if not gap and (w in lx or w == 'codeword'))
    best = max([lex] + others, key=known) if known(lex) < len(ws) else lex
    holes = [w for w, gap in ws if gap or not (w in best or w == 'codeword')]
    if len(holes) > max(1, len(ws) // 10): print(len(ws), holes)

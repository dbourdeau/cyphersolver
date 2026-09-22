"""Measure the reading of R9426: cipher tokens read as sense / all cipher tokens.

A letter token counts as read when the word it belongs to reads as German or as a proper
name. Words still not read are named in UNREAD_WORDS; words that read as a name whose
bearer has not been identified are in NAMES_UNIDENTIFIED and count as read (the plaintext
is recovered, the prosopography is not). Nomenclator groups count as read only where the
group's meaning is established; only 248 = "und" is, from its own contexts.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from solve import parse, is_code
from decode import dec, K as KEY

UNREAD_WORDS = {'tarceen', 'gegainer', 'unaerherschaffen', 'situs'}
NAMES_UNIDENTIFIED = {'leicker', 'dernersen', 'agentemarreo'}
CODES_READ = {'248': 'und'}

if __name__ == '__main__':
    P = parse()
    tok = read = ctok = cread = 0
    unread, names = [], []
    for lid, items in P:
        for it in items:
            if it[0] != 'word': continue
            w = it[1]
            if is_code(w):
                for t in w:
                    if t in KEY:                 # a single cipher letter: an initial
                        tok += 1; read += 1; continue
                    ctok += 1
                    if t in CODES_READ: cread += 1
            else:
                d = dec(w); tok += len(w)
                if d in UNREAD_WORDS: unread.append((lid, d))
                else:
                    read += len(w)
                    if d in NAMES_UNIDENTIFIED: names.append((lid, d))
    total, allread = tok + ctok, read + cread
    print(f'letter tokens {tok}, read {read}')
    print(f'code tokens   {ctok}, read {cread}  ({ctok - cread} nomenclator tokens open)')
    print(f'all tokens    {total}, read {allread}  = {allread / total:.3%}')
    print(f'words not read ({len(unread)}):', ', '.join(d for _, d in unread))
    print(f'names not identified ({len(names)}):', ', '.join(d for _, d in names))

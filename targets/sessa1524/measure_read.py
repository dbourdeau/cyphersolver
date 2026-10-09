"""Measure the share of cipher tokens read as sense in an (a)/(b) reading file (r9873_cipher.txt, r9898_cipher.txt).

Each (b) line is the reading of the (a) line above it. A (b) word is a run of hyphen-joined pieces, one piece per
cipher token (code group or letter sign); clear-text quotes, "...", "/", "¶" and (glosses) are skipped. A word counts
as read as sense when (1) it has no open group ([x] with no '=value') and no {..} letters-without-sense, and (2) the
assembled word scores at or above THRESH per character on the Spanish model es-golden-age (lang/), or, folded for
period spelling (ortho(): y/ll/i, u/v/b, z/c, h, doubled letters), is a word of the es-golden-age/es-gutenberg corpora
or of the folder's clear decipherments; a spelled run that does not make a Spanish word is not counted. Tentative values ([x=value]) are counted as read and reported.
usage: python measure_read.py <file> [--list]   (--list prints the words that fail the language test)
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm  # noqa: E402

THRESH = -4.5
HERE = os.path.dirname(os.path.abspath(__file__))
VOCAB_FILES = [os.path.join(HERE, '..', '..', 'lang', 'corpora', f) for f in
               ('es-quijote.txt', 'es-vasto-memorias.txt', 'es-gutenberg.txt')] +               [os.path.join(HERE, f) for f in ('clear_f140.txt', 'clear_f172.txt', 'clear_f324.txt')]


def ortho(w):
    """Collapse 16th-c. Spanish spelling variation: the clerk writes y for i and ll (yeismo), v/u/b, z/c/ç,
    drops h, doubles s; a word is compared in this folded form."""
    import unicodedata
    w = ''.join(c for c in unicodedata.normalize('NFD', w.lower()) if not unicodedata.combining(c))
    w = w.replace('ll', 'y').replace('y', 'i').replace('v', 'b').replace('u', 'b').replace('h', '')
    w = w.replace('z', 'c').replace('qu', 'c').replace('x', 'j').replace('g', 'j')
    w = re.sub(r'n(?=[pb])', 'm', w)
    return re.sub(r'(.)+', r'', w)


def vocab():
    v = set()
    for f in VOCAB_FILES:
        if os.path.exists(f):
            for w in re.findall(r'[A-Za-zÀ-ÿ]+', open(f, encoding='utf-8', errors='ignore').read()):
                v.add(ortho(w))
    return v


def words_of(body):
    body = re.sub(r'"[^"]*"', ' ', body)
    body = re.sub(r'\((?:[^()]*)\)', ' ', body)
    body = body.replace('...', ' ').replace('¶', ' ').replace('/', ' ')
    out = []
    for w in re.findall(r'\{[^}]*\}|(?:\[[^\]]*\]|[^\s\[])+', body):
        out.append(w)
    return out


def main():
    path = sys.argv[1]
    show = '--list' in sys.argv
    m = lm.load('es-golden-age')
    V = vocab()
    tot = read = opn = garb = tent = 0
    fails = []
    words = []          # a word broken over two reading lines ("a-d-ve-s-a-r-" / "-io-s") is joined
    for ln in open(path, encoding='utf-8'):
        mm = re.match(r'\s*\d+[bd]\s+(.*)', ln)
        if not mm:
            continue
        ws = words_of(mm.group(1))
        if ws and words and words[-1].endswith('-') and ws[0].startswith('-') and not words[-1].startswith('{'):
            words[-1] = words[-1] + ws.pop(0)
        words.extend(ws)
    if True:
        for w in words:
            if w.startswith('{'):
                n = len([p for p in re.split(r'[\s-]+', w.strip('{}')) if p])
                tot += n
                garb += n
                continue
            pieces = [p for p in re.split(r'-(?![^\[]*\])', w) if p]
            n = len(pieces)
            if n == 0:
                continue
            tot += n
            groups = re.findall(r'\[([^\]]*)\]', w)
            if any('=' not in g for g in groups):
                opn += n
                continue
            tent += sum(1 for g in groups if '=' in g)
            word = re.sub(r'\[[^=\]]*=([^\]]*)\]', r'\1', w)
            word = re.sub(r'[^A-Za-zÀ-ÿñÑçÇ ]', '', word.replace('-', '')).replace('ç', 'c').replace('ñ', 'n')
            if not word:
                tot -= n
                continue
            # period spelling: n before p/b (sienpre, enbio) is written m in the model's corpus
            word = re.sub(r'n(?=[pb])', 'm', word.lower()).replace('embi', 'envi')
            s = m.per_char(lm.norm(' ' + word + ' ', 'early'))
            if s >= THRESH or all(ortho(x) in V for x in word.split()):
                read += n
            else:
                garb += n
                fails.append((round(s, 2), w))
    print(f'{path}: tokens {tot}; read as sense {read} ({read / tot:.1%}); open groups {opn}; '
          f'letters without sense {garb}; tentative values counted as read {tent}')
    if show:
        for s, w in sorted(fails):
            print(s, w)


if __name__ == '__main__':
    main()

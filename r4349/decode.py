"""Decode the f. 19v colophon of Uppsala UB C 513 (DECODE R4349).

Each vowel is written as the letter after it in the Latin alphabet (i/j and u/v one letter each):
a->b, e->f, i->k, o->p, u->x. Consonants stand for themselves. The rubricated initial A of "Anno" is not enciphered.

The inverse is not unique: cipher b is plain a or b (liber), f is e or f, p is o or p (scriptus, presens, pro).
k and x are read as i and u only: neither occurs as a consonant in the text, and the shared Latin model folds k into c,
so it cannot judge them. The b/f/p choices are made by a beam search over the whole colophon under that model, so
context decides cases like prp = pro/oro. Each word's choice and the margin over the best alternative are printed.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm

AMBIG = {'b': 'ab', 'f': 'ef', 'k': 'i', 'p': 'op', 'x': 'u'}


def candidates(word):
    opts = [AMBIG.get(c, c) for c in word]
    return [''.join(t) for t in itertools.product(*opts)]


def main(path, beam=200):
    m = lm.load('la')
    text = open(path, encoding='utf8').read().lower()
    words = text.replace('-\n', '').split()   # rejoin words hyphenated across line ends
    beams = [((), 0.0)]
    for w in words:
        nxt = [(b + (c,), m.per_char(' ' + ' '.join(b + (c,)) + ' ')) for b, _ in beams for c in candidates(w)]
        beams = sorted(set(nxt), key=lambda t: -t[1])[:beam]
    best = beams[0][0]
    for i, w in enumerate(words):
        alts = []
        for c in candidates(w):
            if c != best[i]:
                alt = best[:i] + (c,) + best[i + 1:]
                alts.append((beams[0][1] - m.per_char(' ' + ' '.join(alt) + ' '), c))
        margin = min(alts) if alts else None
        print(f'{w:18s} -> {best[i]:18s}' + (f'  (next {margin[1]}, margin {margin[0]:.3f}/char)' if margin else ''))
    print()
    print(' '.join(best))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ciphertext.txt'))

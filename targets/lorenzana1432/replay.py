"""Adapter for docs/_replay.py: december-key.tsv and april-key.tsv applied to the signs of april.tsv, against the
editorial reading that april.tsv gives beside each line of signs.

april.tsv holds, by manuscript line, the cipher signs (spaces = the editor's word division) and the edited reading of
those signs in the letter's own spelling, with [ ] around a letter supplied (Lore[n]zano, lasci[a]re). That is the
reading compared here. reading-it.md is the same text run on with the clear words and with the spelling regularised
(its header says so), so it is not compared sign for sign.

Three words are split across a line end (isfa-sciare, pietra-chassa, ra-chomandare). The two lines are joined here,
so each is one word, as in the count of 58 cipher words in NOTES.md.

Two notes in the reading column describe clear text beside the cipher, not the cipher ([plain e], [followed by
clear a X, to the Ten]); they are left out.
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIVIDED = True
POLYPHONY = {}
SOURCES = {'key': 'december-key.tsv + april-key.tsv',
           'transcription': 'april.tsv (signs)',
           'reading': 'april.tsv (editorial reading, literal spelling; reading-it.md regularises it)'}
JOIN = {'2': '3', '10': '11a', '18b': '19'}          # a line whose last word runs on into the next line
NOTES = ('[plain e]', '[followed by clear a X, to the Ten]')


def _rows(name):
    with open(os.path.join(HERE, name), encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def _key():
    k = {r['sign']: r['value'] for r in _rows('december-key.tsv')}
    k.update({r['sign']: r['value'] for r in _rows('april-key.tsv')})
    return k


def _lines():
    """[(label, [sign word, ...], reading text)] with the split words joined."""
    rows = _rows('april.tsv')
    out, skip = [], None
    for i, r in enumerate(rows):
        if r['line'] == skip:
            continue
        words = r['signs'].split()
        text = r['editorial reading']
        label = r['line']
        if label in JOIN:
            nxt = rows[i + 1]
            assert nxt['line'] == JOIN[label], (label, nxt['line'])
            w2 = nxt['signs'].split()
            words = words[:-1] + [words[-1] + w2[0]] + w2[1:]
            for n in NOTES:
                text = text.replace(n, ' ')
            text = re.sub(r'-\s*$', '', text.rstrip()) + nxt['editorial reading']
            label = label + '+' + nxt['line']
            skip = nxt['line']
        for n in NOTES:
            text = text.replace(n, ' ')
        out.append((label, words, text))
    return out


def mechanical():
    key = _key()
    return [(label, [[(s, key.get(s)) for s in w] for w in words]) for label, words, _ in _lines()]


def reading():
    return {label: text for label, _, text in _lines()}

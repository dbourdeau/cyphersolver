"""Check the marked readings against the mechanical decryption and count words. Standard library only.

    python scripts/reading.py check      (exit 1 on any unmarked departure)

For every line `lab | text` in the ```marked block of reading_<doc>.md:
  resolve marks to their mechanical side ({x/y} -> x, {+a} -> '', [?word] -> word, the quote marks of a
  not-read stretch dropped), normalise (lower case; drop spaces, punctuation, accents, apostrophes, hyphens and
  the <> around code words) and compare with the same line of decryption_<doc>.txt.
Word classes (see words()): verbatim (no mark); repair (a marked change of a key value, or a dropped stray group);
guess (a context fill of a hole, {[nn]/x} or {[?ddd]/x}, or [?word]); with a hole (letters from the signs around an
unread unit); not read (inside the quote marks). holes = [nn] / [?ddd] tokens left on the reading side.
"""
import pathlib
import re
import sys
import unicodedata

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ['c315', 'c25']
MARK = re.compile(r'\{([^{}/]*)/([^{}]*)\}|\{\+([^{}]*)\}')
GUESS = re.compile(r'\[\?([^\]\d][^\]]*)\]')
OPEN, CLOSE = '«', '»'


def mech(text):
    t = GUESS.sub(lambda m: m.group(1), text)
    t = MARK.sub(lambda m: m.group(1) if m.group(3) is None else '', t)
    return t.replace(OPEN, '').replace(CLOSE, '')


def norm(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower().replace('v', 'u')  # u/v one letter
    return re.sub(r"[\s<>.,;:'’\-!()]", '', s)


TOKEN = re.compile(r'\{([^{}/]*)/([^{}]*)\}|\{\+([^{}]*)\}|\[\?([^\]\d][^\]]*)\]|(\[\??\d+\])|([«»])|(.)', re.S)
HOLE = re.compile(r'\[\??\d+\]')
STRAY, HOLEMARK = '\x01', '\x02'   # placeholders: a dropped stray group, a hole left in the reading


def words(text, inside=False):
    """Classify every word of a marked line by what its letters rest on.

    verbatim  every letter is the mechanical decryption, no mark
    repair    a marked change of a key value ({o/t}, {a/}, {+a}) or a dropped stray group ({[?ddd]/})
    guess     a context fill of a hole ({[nn]/x}, {[?ddd]/x}: the signs do not give these letters) or [?word]
    withhole  letters from the signs with an unread unit or odd group left inside the word
    notread   inside «...»: decoded, sense not established
    holes     unread units / odd groups left on the reading side (counted separately, not words)
    A «...» stretch may run over several lines: `inside` is the state at the start of the line; the state at its end
    is returned with the counts.
    """
    chars, cls = [], []
    for m in TOKEN.finditer(text.replace('V. Ecc.', 'V.Ecc.')):
        x, y, add, guess, hole, quote, ch = m.groups()
        if quote:
            inside = quote == OPEN
            continue
        if ch is not None:
            seq, c = ch, 'v'
        elif hole:
            seq, c = HOLEMARK, 'h'
        elif guess is not None:
            seq, c = guess, 'g'
        elif add is not None:
            seq, c = add, 'r'
        elif HOLE.search(x):
            seq, c = (y, 'f') if y.strip() else (STRAY, 'r')
        else:
            seq, c = y if y else STRAY, 'r'
        for k in seq:
            chars.append(k)
            cls.append(c if k.strip() else ' ')
            cls[-1] = (cls[-1], inside)
    out = {'verbatim': 0, 'repair': 0, 'guess': 0, 'withhole': 0, 'notread': 0, 'holes': 0}
    word = []
    groups = []
    for k, c in zip(chars + [' '], cls + [(' ', False)]):
        if k.isspace():
            if word:
                groups.append(word)
            word = []
        else:
            word.append((k, c))
    merged = []
    for w in groups:
        letters = [k for k, _ in w if k not in (STRAY, HOLEMARK) and re.match(r'\w', k)]
        if not letters and all(k == STRAY for k, _ in w) and merged:
            merged[-1] = merged[-1] + w   # a stray group dropped between words belongs to the word before
        else:
            merged.append(w)
    for w in merged:
        out['holes'] += sum(1 for k, _ in w if k == HOLEMARK)
        letters = [k for k, _ in w if k not in (STRAY, HOLEMARK) and re.match(r'\w', k)]
        if not letters:
            continue
        kinds = {c for _, (c, _) in w}
        if any(ins for _, (_, ins) in w):
            out['notread'] += 1
        elif kinds & {'f', 'g'}:
            out['guess'] += 1
        elif 'h' in kinds:
            out['withhole'] += 1
        elif 'r' in kinds:
            out['repair'] += 1
        else:
            out['verbatim'] += 1
    return out, inside


def check():
    bad = 0
    for d in DOCS:
        md = (ROOT / f'reading_{d}.md').read_text(encoding='utf-8')
        block = md.split('```marked')[1].split('```')[0]
        lines = [l for l in block.strip().split('\n') if l.strip()]
        dec = {}
        for l in (ROOT / f'decryption_{d}.txt').read_text(encoding='utf-8').splitlines():
            lab, t = l.split('\t')
            dec[lab] = t
        tot = {'verbatim': 0, 'repair': 0, 'guess': 0, 'withhole': 0, 'notread': 0, 'holes': 0}
        seen = set()
        inside = False
        for l in lines:
            lab, text = [x.strip() for x in l.split('|', 1)]
            seen.add(lab)
            a, b = norm(mech(text)), norm(dec.get(lab, '#missing#'))
            if a != b:
                bad += 1
                print(f'FAIL {d} {lab}\n  reading->mech: {a}\n  decryption:    {b}')
            counts, inside = words(text, inside)
            for k, v in counts.items():
                tot[k] += v
        missing = set(dec) - seen
        if missing:
            bad += 1
            print(f'FAIL {d}: lines without reading: {sorted(missing)}')
        n = tot['verbatim'] + tot['repair'] + tot['guess'] + tot['withhole'] + tot['notread']
        print(f'{d}: words {n}: verbatim {tot["verbatim"]} ({100 * tot["verbatim"] / n:.1f}%), marked repair {tot["repair"]}, '
              f'context fill or guess {tot["guess"]}, with a hole {tot["withhole"]}, decoded but not read {tot["notread"]}; '
              f'holes {tot["holes"]}; from a gloss 0')
    return bad


if __name__ == '__main__':
    sys.exit(1 if check() else 0)

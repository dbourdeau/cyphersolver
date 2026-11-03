#!/usr/bin/env python3
"""Check the reading against the signs and count its words. Standard library only.

    python scripts/check_marks.py            counts; exit 1 on any failure
    python scripts/check_marks.py --table    also print every marked word with its line

The decryption is rebuilt from the transcription and key.tsv and compared with decryption_15oct_ff34r-35v.txt. The Latin of the cipher
section of the reading (the paragraphs that open with **n) is then walked letter by letter against the signs:

    {a/e}   text a, signs e      changed
    {+s}    no sign              restored
    {+?e}   sign not clear       restored: the letter rests on sense
    {?i}    doubtful sign        on the page, doubtful; also for a value the key marks as proposed
    [Q8 x]  code sign            read
    [Q8? x] code sign, numeral doubtful
    [Q7 ?x] code sign            not read: value from context

Exit 1 if any letter of the reading differs from the signs without a mark, if a doubtful sign is unmarked, or if a mark has no doubtful
sign under it.
"""
import pathlib, re, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decode

ROOT = decode.ROOT
READING = ROOT / 'reading_15oct_ff34r-36r.md'
TOKEN = re.compile(r'\[(?:Q|H)\d\??\s[^\]]*\]|(?:[A-Za-z]|\{[^}]*\})+')


def page_units():
    """The cipher as units (line, value, doubtful): one letter, or one code place."""
    key, proposed = decode.load_key()
    u = []
    for ln, s, doubt in decode.signs():
        v = key[s]
        if v == 'null':
            continue
        doubt = doubt or s in proposed
        if v.startswith('['):
            u.append((ln, v, doubt))
        else:
            u.extend((ln, c, doubt) for c in v)
    return u


def latin():
    t = READING.read_text(encoding='utf8').split('## Cipher')[1].split('Notes on the text')[0]
    t = t.split('\n', 1)[1].strip()
    return ' '.join(re.sub(r'^\*\*\d+ \([^)]*\)\.\*\*', '', p) for p in re.split(r'\n\s*\n', t) if p.startswith('**'))


def parse(w):
    """(reading units, word class) of one token. A unit is (page value or None, marked doubtful)."""
    m = re.match(r'\[((?:Q|H)\d)(\??)\s([^\]]*)\]', w)
    if m:
        cls = 'unread' if m[3].startswith('?') else ('doubtful' if m[2] else 'plain')
        return [(f'[{m[1]}]', bool(m[2]))], cls
    units, cls = [], 'plain'
    for x in re.findall(r'\{[^}]*\}|[A-Za-z]', w):
        if not x.startswith('{'):
            units.append((x.lower(), False))
        elif x.startswith('{+?'):
            units.append((x[3], True))
            cls = 'restored'
        elif x.startswith('{+'):
            cls = 'restored'
        elif x.startswith('{?'):
            units.append((x[2], True))
            cls = 'restored' if cls == 'restored' else 'doubtful'
        elif '/' in x:
            units.append((x[3], False))
            cls = 'restored'
        else:
            raise SystemExit(f'unknown mark {x} in {w}')
    return units, cls


def main():
    bad = 0
    want = '\n'.join(decode.decrypt()) + '\n'
    if decode.OUT.read_text(encoding='utf8') != want:
        print('decryption file differs from transcription + key.tsv')
        bad += 1
    page = page_units()
    i = 0
    words = []
    for w in TOKEN.findall(latin()):
        units, cls = parse(w)
        start = i
        for val, marked in units:
            if i >= len(page):
                print('reading runs past the signs at', w)
                sys.exit(1)
            ln, v, doubt = page[i]
            if v != val:
                print(f'UNMARKED departure at {ln}: reading {w} gives {val}, signs give {v}')
                bad += 1
            if doubt and not marked:
                print(f'UNMARKED doubtful sign at {ln}: {w}')
                bad += 1
            if marked and not doubt:
                print(f'doubt mark with no doubtful sign at {ln}: {w}')
                bad += 1
            i += 1
        words.append((w, cls, page[min(start, len(page) - 1)][0]))
    if i != len(page):
        print(f'signs left over: {i} of {len(page)}')
        bad += 1
    n = len(words)
    c = {k: sum(1 for _, x, _ in words if x == k) for k in ('plain', 'doubtful', 'restored', 'unread')}
    ds = [w for w, x, _ in words if x == 'doubtful']
    pct = lambda a: f'{a} of {n} ({a / n:.1%})'
    key, _ = decode.load_key()
    sg = list(decode.signs())
    letters = sum(len(key[s]) for _, s, _ in sg if key[s] != 'null' and not key[s].startswith('['))
    codes = sum(1 for _, s, _ in sg if key[s].startswith('['))
    print(f'signs {len(sg)} on {len(set(l for l, _, _ in sg))} lines; nulls {sum(key[s] == "null" for _, s, _ in sg)}; letters {letters}; code places {codes}')
    print(f'words {n}: plain {c["plain"]}, on a doubtful sign {c["doubtful"]}, restored or changed {c["restored"]}, unread {c["unread"]}')
    print('reads as sense:', pct(n - c['unread']))
    print('reads as sense, code place with a doubtful numeral out:', pct(n - c['unread'] - sum(w.startswith('[') for w in ds)))
    print('no restored or changed letter:', pct(n - c['unread'] - c['restored']))
    print('firm, every doubtful sign out as well:', pct(c['plain']))
    if '--table' in sys.argv:
        for w, x, ln in words:
            if x != 'plain':
                print(f'{ln}\t{x}\t{w}')
    print('marks: OK' if not bad else f'marks: {bad} FAILED')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

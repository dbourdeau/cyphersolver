"""Held-out test: decrypt the cipher of image 75 with key_frozen.tsv and compare with its contemporary gloss.

    python scripts/heldout.py

Two scores are printed:
  A. the signs as written (L lines). In L03 the clerk wrote a point inside 'underhåldet' (8 . 4 where the gloss needs 84);
  B. the gloss-guided variant (V lines replace L lines where given: 8 . 4 read as 84, the clerk's probable slip).
Where the cipher words of a line match the gloss words one to one, each word is compared group by group. Where a word
and its gloss word differ in length, or the line has more cipher words than gloss words, the groups are aligned with the
gloss letters (difflib) and a group with no gloss letter counts as wrong. u/v/w, i/j/y and å/o count as one letter each.
"""
import difflib, pathlib, re, sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import decrypt
ROOT = decrypt.ROOT
EQ = str.maketrans({'v': 'u', 'w': 'u', 'j': 'i', 'y': 'i', 'å': 'o'})
key = decrypt.load_key(ROOT / 'key_frozen.tsv')

rows = {}
for line in open(ROOT / 'transcription_heldout_075.txt', encoding='utf-8'):
    m = re.match(r'^([LGV])(\d+)\t(.*)$', line.rstrip('\n'))
    if m:
        rows.setdefault(m.group(2), {})[m.group(1)] = m.group(3)


def cipher_words(text):
    words, cur = [], []
    for t in re.findall(r'<[^>]*>|\S+', text):
        if t.startswith('<'):
            continue
        if t == '.':
            if cur:
                words.append(cur)
            cur = []
        else:
            cur.append(t.rstrip('?'))
    if cur:
        words.append(cur)
    return words


def score_word(codes, g):
    """Return (right, wrong, unknown, rendered, exact) for one cipher word against one gloss word."""
    vals = [key.get(c) for c in codes]
    res, right, wrong, unk = [], 0, 0, 0
    if len(codes) == len(g):
        pairs = list(zip(codes, vals, g))
    else:
        a = [v.translate(EQ) if v else '\0' for v in vals]
        b = [ch.lower().translate(EQ) for ch in g]
        pairs = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == 'insert':
                continue
            for k in range(i1, i2):
                j = j1 + (k - i1)
                pairs.append((codes[k], vals[k], g[j] if j < j2 else None))
    for c, v, ch in pairs:
        if v is None:
            unk += 1; res.append(f'[{c}]')
        elif ch is not None and v.translate(EQ) == ch.lower().translate(EQ):
            right += 1; res.append(v)
        else:
            wrong += 1; res.append(f'{{{v}≠{ch if ch else "-"}}}')
    exact = len(codes) == len(g) and wrong == 0 and unk == 0
    return right, wrong, unk, ''.join(res), exact


def run(label, use_variant):
    tot = ok = bad = unk = wok = wtot = 0
    print(f'== {label}')
    for n, r in sorted(rows.items()):
        text = r['V'] if use_variant and 'V' in r else r['L']
        words = cipher_words(text)
        gl = r['G'].split()
        if len(words) != len(gl):
            # a word stop the gloss does not have: align the whole line against the whole gloss
            words, gl = [[c for w in words for c in w]], [''.join(gl)]
            note = '  (cipher stop inside a gloss word: aligned as one)'
        else:
            note = ''
        for codes, g in zip(words, gl):
            right, wrong, u, rendered, exact = score_word(codes, g)
            tot += right + wrong + u; ok += right; bad += wrong; unk += u
            wtot += 1; wok += exact
            extra = '  (length differs)' if len(codes) != len(g) else ''
            print(f'{g:14s} {" ".join(codes):40s} {rendered}{extra}{note}')
    print(f'groups {tot}: right {ok} ({ok / tot:.0%}), wrong {bad}, not in frozen key {unk}; words right {wok}/{wtot}')
    print()


run('A. signs as written (L03: 8 . 4)', False)
run("B. gloss-guided variant (V03: 8 . 4 read as 84, the clerk's probable slip)", True)

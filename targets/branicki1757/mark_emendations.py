"""Write reading_<n>_marked.md: the contributor's reading with every letter the key does not give in [ ]
(decrypt audit, 16 Nov 2026).

reading_446.md, reading_1398.md, reading_1399.md and reading_1400.md are Prabal Gupta's readings, kept as his.
They print the word meant where the decryption has a slip, without a mark. This script does not touch them. It
aligns the letters of each reading with the letters of the mechanical decrypt and writes a copy in which every
letter of the reading that the decrypt does not give stands in [ ]. A word with half or more of its letters not
given, or a word of one or two letters, is bracketed whole. Marks already in the reading ([?word], [de], [795])
are kept and nothing is marked inside them.

The mechanical decrypt is decryption_<n>.txt (key.tsv applied to transcription_<n>.txt; checked identical on every
line, 16 Nov 2026) with each number group replaced by its value in key_with_numbers.tsv (punctuation, nulls and
numbers without a fixed value give no letter), the clear passages of 1399 kept as they stand, and the two
foot-line insertions of 446 put at their marks. For 446 only the section "## En chiffre" is compared.

Not marked: u/v, i/j and i/y; accents; apostrophes, capitals, punctuation and word division; a consonant doubled;
s printed for the z of the key. Letters of the decrypt that the reading drops (diettines printed dietines) cannot
be marked without adding a letter; they are listed in emendations.tsv (kind "dropped").

The script checks that each marked copy, with every [ and ] removed, is the reading with every [ and ] removed.

Usage: python mark_emendations.py            report only
       python mark_emendations.py --write    write reading_<n>_marked.md and emendations.tsv
"""
import os, re, sys, difflib, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
TEXTS = ['446', '1398', '1399', '1400']
OWN = "This is the contributor's reading"          # start of the header line added to his files on 16 Nov 2026
HEADER = ('This file is reading_{n}.md with marks added on 16 Nov 2026 by mark_emendations.py; no letter differs. '
          'Letters in [ ] inside or round a word, without a question mark, are letters that the key does not give '
          '(the output of the key is decryption_{n}.txt, with the number code of key_with_numbers.tsv): the '
          "contributor's corrections of slips, words he supplied, and the wording he chose for a number group. "
          'Not marked: u/v and i/j, accents, word division, a doubled consonant, s for the z of the key. Letters of '
          'the decryption that the reading leaves out are listed in emendations.tsv. None of this was checked '
          'against the scans.')


def fold(c):
    c = unicodedata.normalize('NFD', c.lower())[0]
    return {'v': 'u', 'j': 'i', 'y': 'i'}.get(c, c) if c.isalpha() else ''


def numbers():
    num = {}
    for line in open(os.path.join(HERE, 'key_with_numbers.tsv'), encoding='utf8'):
        if line.startswith('#'):
            continue
        c = line.rstrip('\n').split('\t')
        if c[0].isdigit():
            num[c[0]] = '' if c[1] == '-' else c[1]
    return num


def machine(n, num):
    lines = []
    for line in open(os.path.join(HERE, f'decryption_{n}.txt'), encoding='utf8'):
        if line.startswith('#') or '\t' not in line:
            continue
        lab, text = line.rstrip('\n').split('\t', 1)
        lines.append([lab, text])
    # foot-line insertions of 446: "p2.foot ^desfraix" belongs at the ^ of the page, "p4.foot +ausejour" at the +
    for lab, text in list(lines):
        if lab.endswith('.foot'):
            sign, ins = text[0], text[1:]
            for other in lines:
                if other[0].startswith(lab.split('.')[0] + '.') and not other[0].endswith('.foot') and sign in other[1]:
                    other[1] = other[1].replace(sign, ins, 1)
            lines.remove([lab, text])
    out = []
    for lab, text in lines:
        if n == '1400':
            text = text.replace('[385]', '')     # 385 is fixed for 1399 only; in 1400 it is open and the reading keeps [385]
        text = re.sub(r'\[(\d+)\]', lambda m: ' ' + num.get(m.group(1), '') + ' ', text)
        out.append(''.join(fold(c) for c in text))
    return ''.join(out)


def nw(a, b):
    """Global alignment of two short strings: list of (kind, i, j), kind in eq, sub, ins (only in b), del (only in a)."""
    n, m = len(a), len(b)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for j in range(1, m + 1):
        S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + (2 if a[i - 1] == b[j - 1] else -1), S[i - 1][j] - 1, S[i][j - 1] - 1)
    ops, i, j = [], n, m
    while i or j:
        if i and j and S[i][j] == S[i - 1][j - 1] + (2 if a[i - 1] == b[j - 1] else -1):
            ops.append(('eq' if a[i - 1] == b[j - 1] else 'sub', i - 1, j - 1)); i -= 1; j -= 1
        elif j and S[i][j] == S[i][j - 1] - 1:
            ops.append(('ins', None, j - 1)); j -= 1
        else:
            ops.append(('del', i - 1, None)); i -= 1
    return ops[::-1]


def align(a, b):
    """Anchor on the common runs difflib finds, align each gap between two anchors exactly."""
    ops = []
    for tag, a1, a2, b1, b2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == 'equal':
            ops += [('eq', a1 + k, b1 + k) for k in range(a2 - a1)]
        elif (a2 - a1) * (b2 - b1) > 4_000_000:               # a clear passage only in the reading, or the like
            ops += [('del', i, None) for i in range(a1, a2)] + [('ins', None, j) for j in range(b1, b2)]
        else:
            ops += [(k, None if i is None else a1 + i, None if j is None else b1 + j) for k, i, j in nw(a[a1:a2], b[b1:b2])]
    return ops


def normalisation(kind, i, j, a, b):
    """True for the spelling conventions that are stated in the header and not marked."""
    if kind == 'ins':
        c = b[j]
        return c not in 'aeiou' and ((j > 0 and b[j - 1] == c) or (j + 1 < len(b) and b[j + 1] == c))
    if kind == 'sub':
        if a[i] == 'z' and b[j] == 's':
            return True
    return False


def mark(text, flagged, old):
    """[ ] round the flagged character positions of text; old = positions already inside a bracket (left alone)."""
    res, pos = [], 0
    for tok in re.split(r'(\s+)', text):
        span = range(pos, pos + len(tok)); pos += len(tok)
        letters = [k for k in span if text[k].isalpha() and k not in old]
        fl = [k for k in letters if k in flagged]
        if not tok.strip() or not fl or any(k in old for k in span) and len(fl) * 2 >= len(letters):
            # a word that already carries a bracket ("[?jetter]", "c[...]") is not bracketed whole
            if not tok.strip() or not fl:
                res.append(tok); continue
        whole = (len(fl) * 2 >= len(letters) or len(letters) <= 2) and not any(k in old or text[k] in '[]' for k in span)
        lo, hi = letters[0], letters[-1]
        inside = lambda k: (lo <= k <= hi) if whole else (k in flagged and k not in old)
        s, open_ = '', False
        for k in span:
            now = inside(k)
            # an apostrophe or hyphen between two marked letters stays inside the bracket
            if not whole and not text[k].isalpha() and text[k] in "'’-" and open_ and k + 1 in flagged and k + 1 not in old:
                now = True
            if now and not open_:
                s += '['
            if not now and open_:
                s += ']'
            open_ = now
            s += text[k]
        if open_:
            s += ']'
        res.append(s)
    return ''.join(res)


def strip(t):
    return t.replace('[', '').replace(']', '')


def main(write):
    num = numbers()
    rows, total = [], collections.Counter()
    for n in TEXTS:
        full = open(os.path.join(HERE, f'reading_{n}.md'), encoding='utf8').read()
        if n == '446':
            s = full.index('## En chiffre'); s = full.index('\n', s) + 1
            e = full.index('## En clair', s)
        else:
            s = full.index('\n', full.index(OWN)) + 1                   # after the title and the two header paragraphs
            e = len(full)
        body = full[s:e]
        old, depth = set(), 0
        for k, ch in enumerate(body):
            if ch == '[':
                depth += 1
            if depth:
                old.add(k)
            if ch == ']':
                depth = max(0, depth - 1)
        for m in re.finditer(r'^#.*$', body, re.M):                  # the "## Page 2" headings of 1398
            old.update(range(m.start(), m.end()))
        idx = [k for k, ch in enumerate(body) if k not in old and fold(ch)]
        b = ''.join(fold(body[k]) for k in idx)
        a = machine(n, num)
        words, w = {}, -1
        for mm in re.finditer(r'\S+', body):
            w += 1
            for k in range(mm.start(), mm.end()):
                words[k] = (w, mm.group(0))
        flagged, c = set(), collections.Counter()
        for kind, i, j in align(a, b):
            if kind == 'eq':
                continue
            if normalisation(kind, i, j, a, b):
                c['letters by convention'] += 1; continue
            if kind == 'del':
                c['letters dropped'] += 1
                rows.append((n, '', '', 'dropped', a[i], '', a[max(0, i - 8):i] + '[' + a[i] + ']' + a[i + 1:i + 9]))
                continue
            flagged.add(idx[j]); c['letters marked'] += 1
            rows.append((n, words[idx[j]][0], words[idx[j]][1], 'replaced' if kind == 'sub' else 'supplied',
                         a[i] if kind == 'sub' else '', b[j], a[max(0, (i or 0) - 8):(i or 0)]))
        new_body = mark(body, flagged, old)
        assert strip(new_body) == strip(body), n
        c['words marked'] = len({words[k][0] for k in flagged}); c['words'] = len({words[k][0] for k in idx})
        c['places'] = new_body.count('[') - body.count('[')
        total.update(c)
        print(n, dict(c))
        if write:
            new = full[:s] + new_body + full[e:]
            own = full[full.index(OWN):full.index('\n', full.index(OWN))]     # the header line of the contributor's file
            assert new.count(own) == 1
            new = new.replace(own, HEADER.format(n=n))
            assert strip(new).replace(strip(HEADER.format(n=n)), strip(own)) == strip(full), n
            open(os.path.join(HERE, f'reading_{n}_marked.md'), 'w', encoding='utf8').write(new)
    print('total', dict(total))
    if write:
        with open(os.path.join(HERE, 'emendations.tsv'), 'w', encoding='utf8') as f:
            f.write('# written by mark_emendations.py: every letter of reading_<n>.md that the mechanical decrypt does not give\n'
                    '# (replaced, supplied) and every letter of the decrypt that the reading leaves out (dropped).\n'
                    'letter\tword no.\tword\tkind\tdecrypt\treading\tdecrypt context\n')
            for r in rows:
                f.write('\t'.join(str(x) for x in r) + '\n')


if __name__ == '__main__':
    main('--write' in sys.argv)

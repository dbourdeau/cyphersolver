"""Mark every place where a hand reading departs from the mechanical decrypt (decrypt audit, 16 Nov 2026).

The mechanical decrypt of a letter is read/machine_R<rec>.txt: key.json applied to cipher/R<rec>.txt, nothing
edited (checked on 16 Nov 2026: identical, letter for letter, in all ten letters). The hand readings
read/R<rec>_reading.md printed the word meant where the decoded string was not a French word, with no mark.
This script aligns the letters of each reading (the text under "## Reading") with the letters of the machine
decrypt and puts [ ] round every letter of the reading that the decrypt does not give. A word with half or more
of its letters not given, or a word of one or two letters, is bracketed whole. Marks already in the file
([...], [?], [?word], [word], the sigla [S./.]) are kept and nothing is marked inside them.

Not marked (stated in the header line the script adds to each file):
  u/v, i/j and i/y; accents; apostrophes, capitals, punctuation and word division;
  a consonant doubled (aparences printed apparences);
  m printed for the n of the key before p, b or m (inpossible printed impossible);
  s printed for the z of the key (degrez printed degres).
Letters of the decrypt that the reading drops cannot be marked without adding a letter; they are listed in
emendations.tsv (kind "dropped") and counted.

The script adds marks and one header line only. It checks that the text with every [ and ] removed is the same
before and after, and refuses to write otherwise. R1954 is not handled: its partial reading follows
trans/R1954_b29.txt, for which the folder has no machine decrypt.

A file that already carries the header line is skipped, so a second run changes nothing.

Usage: python mark_emendations.py            report only
       python mark_emendations.py --write    rewrite read/R*_reading.md and write emendations.tsv
"""
import os, re, sys, difflib, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
RECS = ['R2078', 'R1958', 'R2079', 'R2080', 'R1959', 'R2081', 'R2082', 'R1044', 'R1043']
HEADER = ('<!-- Marks added 16 Nov 2026 (mark_emendations.py): letters in [ ] inside or round a word, without a '
          'question mark, are letters that key.json applied to the transcription does not give (the output of the '
          'key is read/machine_{rec}.txt); they are the reader\'s corrections of the decoded string, not checked '
          'against the images. Not marked: u/v and i/j, accents, word division, a doubled consonant, m for the n '
          'of the key before p, b or m, and s for the z of the key. Letters of the decoded string that the reading '
          'leaves out are listed in emendations.tsv. -->')


def fold(c):
    c = unicodedata.normalize('NFD', c.lower())[0]
    return {'v': 'u', 'j': 'i', 'y': 'i'}.get(c, c) if c.isalpha() else ''


def machine(rec):
    t = open(os.path.join(HERE, 'read', f'machine_{rec}.txt'), encoding='utf8').read().split('\n', 1)[1]
    t = re.sub(r'\[[^\]]*\]|\{\d+\}|<\d+>', '', t)          # clear passages, stray digits, codes without a value
    return ''.join(fold(c) for c in t)


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
    """True for the three spelling conventions that are stated in the header and not marked."""
    if kind == 'ins':
        c = b[j]
        return c not in 'aeiou' and ((j > 0 and b[j - 1] == c) or (j + 1 < len(b) and b[j + 1] == c))
    if kind == 'sub':
        if a[i] == 'n' and b[j] == 'm' and j + 1 < len(b) and b[j + 1] in 'pbm':
            return True
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
    rows, total = [], collections.Counter()
    for rec in RECS:
        path = os.path.join(HERE, 'read', f'{rec}_reading.md')
        full = open(path, encoding='utf8').read()
        m = re.search(r'^## Reading[^\n]*\n', full, re.M)
        head, body = full[:m.end()], full[m.end():]
        if 'mark_emendations.py' in head:
            print(rec, 'already marked, left as it is (restore the unmarked file to run again)'); continue
        old, depth = set(), 0
        for k, ch in enumerate(body):
            if ch == '[':
                depth += 1
            if depth:
                old.add(k)
            if ch == ']':
                depth = max(0, depth - 1)
        idx = [k for k, ch in enumerate(body) if k not in old and fold(ch)]
        b = ''.join(fold(body[k]) for k in idx)
        a = machine(rec)
        flagged, c = set(), collections.Counter()
        words = {}
        w = -1
        for mm in re.finditer(r'\S+', body):
            w += 1
            for k in range(mm.start(), mm.end()):
                words[k] = (w, mm.group(0))
        pending = []
        for kind, i, j in align(a, b):
            if kind == 'eq':
                continue
            if normalisation(kind, i, j, a, b):
                c['letters by convention'] += 1; continue
            if kind == 'del':
                # attribute the dropped letter to the reading word at that point
                pending.append(i); continue
            flagged.add(idx[j])
            c['letters marked'] += 1
            rows.append((rec, words[idx[j]][0], words[idx[j]][1], 'replaced' if kind == 'sub' else 'supplied',
                         a[i] if kind == 'sub' else '', b[j], a[max(0, (i or 0) - 8):(i or 0)]))
        for i in pending:
            c['letters dropped'] += 1
            rows.append((rec, '', '', 'dropped', a[i], '', a[max(0, i - 8):i] + '[' + a[i] + ']' + a[i + 1:i + 9]))
        new_body = mark(body, flagged, old)
        assert strip(new_body) == strip(body), rec
        assert new_body.replace('[', '').count(']') == new_body.replace(']', '').count('[')
        marked_words = {words[k][0] for k in flagged}
        all_words = {words[k][0] for k in idx}
        c['words marked'] = len(marked_words); c['words'] = len(all_words)
        c['places'] = len(re.findall(r'\[', new_body)) - len(re.findall(r'\[', body))
        total.update(c)
        print(rec, dict(c))
        if write:
            if 'mark_emendations.py' not in head:
                head = head.replace('\n', '\n' + HEADER.format(rec=rec) + '\n', 1)
            open(path, 'w', encoding='utf8').write(head + new_body)
    print('total', dict(total))
    if write:
        with open(os.path.join(HERE, 'emendations.tsv'), 'w', encoding='utf8') as f:
            f.write('# written by mark_emendations.py: every letter of read/R*_reading.md that read/machine_R*.txt does not give\n'
                    '# (replaced, supplied) and every letter of the machine decrypt that the reading leaves out (dropped).\n'
                    'letter\tword no.\tword\tkind\tdecrypt\treading\tdecrypt context\n')
            for r in rows:
                f.write('\t'.join(str(x) for x in r) + '\n')


if __name__ == '__main__':
    main('--write' in sys.argv)

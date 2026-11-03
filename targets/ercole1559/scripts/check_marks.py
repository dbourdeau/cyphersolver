#!/usr/bin/env python3
"""Check a reading against its decryption and count its words. Standard library only.

    python scripts/check_marks.py 76            cc. 76-77, 1576
    python scripts/check_marks.py 50            c. 50r, 1559

The numbered Italian sentences of the reading are aligned letter by letter with the decryption. A word is
counted as clean only if it carries no mark. Marks: <x> restored or changed letter, {x} letter in the signs left
out of the reading, [?x] doubtful. A departure from the signs on a letter with no mark is an error: the script
prints it and exits 1. Elided forms are split at the apostrophe; the digit 7 counts as a word.
"""
import difflib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = {'76': ('reading_cc76-77_1576-04-14.md', 'decryption_cc76-77_1576-04-14.txt'),
         '50': ('reading_cc50-51_1559-05-28.md', 'decryption_cc50r_1559-05-28.txt')}


def fold(c):
    return {'v': 'u', 'j': 'i'}.get(c.lower(), c.lower())


def decryption(doc):
    """Letters in reading order: nulls out, blots kept as ?, the sign L as et."""
    out = []
    lines = [l for l in (ROOT / FILES[doc][1]).read_text(encoding='utf8').splitlines()
             if l.strip() and not l.startswith('#')]
    if doc == '76':
        for i in range(1, len(lines), 2):
            out += [fold(c) for c in lines[i].strip() if c not in '.{}']
    else:
        for l in lines:
            if l.startswith('    plain: '):
                out += [fold(c) for c in l[11:].strip() if c != ' ']
    return ''.join(out).replace('&', 'et')


def reading(doc):
    t = (ROOT / FILES[doc][0]).read_text(encoding='utf8').split('## Departures')[0]
    return [re.sub(r'^\d+\.\s', '', l.strip()) for l in t.splitlines() if re.match(r'\s*\d+\. ', l)]


def parse(sents):
    chars, flags, wid, words = [], [], [], []
    for s in sents:
        s = s.replace("'", ' ').replace('*', '')
        for tok in s.split():
            state, klass, n, buf, i = 'p', set(), len(words), '', 0
            while i < len(tok):
                c = tok[i]
                if tok.startswith('[?', i):
                    state = 'd'; klass.add('d'); i += 2; continue
                if c == ']':
                    state = 'p'; i += 1; continue
                if c == '<':
                    state = 'r'; klass.add('r'); i += 1; continue
                if c == '{':
                    state = 'x'; klass.add('r'); i += 1; continue
                if c in '>}':
                    state = 'p'; i += 1; continue
                if c.isalnum():
                    chars.append(fold(c)); flags.append(state); wid.append(n); buf += c
                i += 1
            if buf:
                words.append((tok, klass))
    return ''.join(chars), flags, wid, words


def main():
    doc = sys.argv[1]
    d = decryption(doc)
    r, fl, wid, words = parse(reading(doc))
    bad, unused = [], []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, d, r, autojunk=False).get_opcodes():
        if tag == 'equal':
            for j in range(j1, j2):
                if fl[j] == 'r':
                    unused.append((words[wid[j]][0], r[j]))
            continue
        if j2 > j1:
            near = {wid[j] for j in range(max(j1 - 1, 0), min(j2 + 1, len(wid)))}
            if any(fl[j] == 'p' for j in range(j1, j2)) and not any(words[w][1] for w in near):
                bad.append((d[max(i1 - 6, 0):i2 + 6], words[wid[j1]][0]))
        else:
            near = {wid[max(j1 - 1, 0)], wid[min(j1, len(wid) - 1)]}
            if not any(words[w][1] for w in near):
                bad.append((d[max(i1 - 6, 0):i2 + 6], words[wid[min(j1, len(wid) - 1)]][0]))
    n = len(words)
    whole = [w for w, k in words if w.startswith('[?') and w.rstrip('.,;:').endswith(']')]
    # a [?two words] mark spans tokens: count each token inside it as doubtful
    rep = [w for w, k in words if k and w not in whole]
    clean = n - sum(1 for w, k in words if k)
    print(f'words {n}; whole words doubtful {len(whole)}; reads as sense {n - len(whole)} ({(n - len(whole)) / n:.1%}); '
          f'repaired or partly doubtful {len(rep)}; no restored or changed letter {clean} ({clean / n:.1%}); '
          f'95% bar {-(-n * 95 // 100)}')
    print('marked words:', ' '.join(w for w, k in words if k))
    if unused:
        print('marked but matching the signs:', unused)
    if bad:
        print('UNMARKED departures:', bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()

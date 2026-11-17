"""Mark in the reading files every place where the reading is not the key's output (16 Nov 2026).

The reading files' own convention is "[word] = emended where the mechanical decrypt differs", but the key replay
(docs/_replay.py) found 340 cipher words that differed with no mark. This script puts the marks in; it changes no
letter of the reading:

  [x]     a letter the key does not give (substituted or supplied), bracketed where it stands;
  [word]  the whole word, when the reading leaves out a sign the key gives a value for;
  {word}  the key's output for a cipher word the reading leaves out (cancelled or superfluous in the manuscript).

Differences that are only i/y, or a value key.txt declares for the sign (third column), are not marked.
Run from the repository root: python targets/memoire1560/mark_emendations.py [--write]
"""
import os, sys, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'docs'))
import _replay as R
import replay as ad

FILES = ('reading_152r-154r.txt', 'reading_154v-156v.txt')
POLY = {u: {R.fold(x) for x in v} for u, v in ad.POLYPHONY.items()}


def letters(raw):
    """-> [(folded letter, raw index, marked, word no)] and the folded string; '[..]' becomes one hole letter."""
    out, depth, word, i, inword = [], 0, -1, 0, False
    while i < len(raw):
        m = re.match(r'\[\s*(\.\.+|…)\s*\]', raw[i:])
        if m:
            word += 1; out.append(('#', i, True, word)); i += m.end(); inword = False; continue
        c = raw[i]
        if c.isspace():
            inword = False
        else:
            if not inword:
                word += 1; inword = True
            if c == '[': depth += 1
            elif c == ']': depth = max(0, depth - 1)
            else:
                for ch in R.fold(c):
                    out.append((ch, i, depth > 0, word))
        i += 1
    return out


def mark_line(words, raw):
    mech, cu, units = R.build_mech(words)
    L = letters(raw)
    read = ''.join(x[0] for x in L)
    pairs = R.align(mech, read, [1.0] * len(mech))
    m2r = {mi: ri for mi, ri in pairs if mi is not None}
    hole = set()
    for mi, ri in m2r.items():
        if ri is not None and read[ri] == '#': hole.add(mi)
    changed = True
    while changed:
        changed = False
        for mi in range(len(mech)):
            if m2r[mi] is None and mi not in hole and (mi - 1 in hole or mi + 1 in hole):
                hole.add(mi); changed = True
    need = set(); whole = set(); inserts = []      # reading letter indexes; reading word numbers; (raw pos, text)
    for mi, ri in pairs:
        if mi is None:
            if read[ri] != '#' and not L[ri][2]: need.add(ri)
        elif ri is not None:
            x, y = mech[mi], read[ri]
            u = units[cu[mi]]
            if y == '#' or x == y or {x, y} == {'i', 'y'}: continue
            if u['b'] - u['a'] == 1 and y in POLY.get(u['unit'], ()): continue
            if not L[ri][2]: need.add(ri)
    # signs the reading leaves out
    k = 0
    while k < len(mech):
        if m2r[k] is None and k not in hole and units[cu[k]]['value'] is not None:
            j = k
            while j < len(mech) and m2r[j] is None and j not in hole: j += 1
            pw = L[m2r[k - 1]][3] if k and m2r.get(k - 1) is not None else None
            nw = L[m2r[j]][3] if j < len(mech) and m2r.get(j) is not None else None
            w0, w1 = units[cu[k]]['word'], units[cu[j - 1]]['word']
            lone = (k == 0 or units[cu[k - 1]]['word'] != w0) and (j == len(mech) or units[cu[j]]['word'] != w1)
            if lone:        # whole cipher word(s) with nothing in the reading
                at = L[m2r[j]][1] if j < len(mech) and m2r.get(j) is not None else len(raw)
                if j < len(mech) and m2r.get(j) is not None:      # back up to the start of that reading word
                    while at and not raw[at - 1].isspace(): at -= 1
                inserts.append((at, '{' + mech[k:j] + '} '))
            else:
                # the sign belongs to the reading word that carries the rest of its cipher word
                own = [L[m2r[q]][3] for q in range(len(mech)) if m2r[q] is not None and units[cu[q]]['word'] in (w0, w1)]
                tgt = pw if pw in own else (nw if nw in own else (own[0] if own else pw if pw is not None else nw))
                if tgt is not None: whole.add(tgt)
            k = j
        else:
            k += 1
    for ri, x in enumerate(L):
        if x[3] in whole and x[0] != '#' and not x[2]: need.add(ri)
    pos = sorted(L[ri][1] for ri in need)
    out, i = list(raw), 0
    edits = []
    while i < len(pos):
        j = i
        while j + 1 < len(pos) and pos[j + 1] == pos[j] + 1: j += 1
        edits.append((pos[i], '[')); edits.append((pos[j] + 1, ']'))
        i = j + 1
    for at, text in inserts: edits.append((at, text))
    for at, text in sorted(edits, key=lambda e: -e[0]):
        out.insert(at, text)
    new = ''.join(out).rstrip()
    new = re.sub(r'\]\[', '', new)                 # adjoining marks are one mark
    return new, len(need), len(inserts)


def main():
    write = '--write' in sys.argv
    mech = dict(ad.mechanical())
    n_letters = n_ins = n_lines = 0
    for fn in FILES:
        p = os.path.join(HERE, fn)
        res = []
        for l in open(p, encoding='utf8'):
            l = l.rstrip('\n')
            if l.startswith('#') or '\t' not in l:
                res.append(l); continue
            lab, raw = l.split('\t', 1)
            if lab not in mech:
                res.append(l); continue
            new, a, b = mark_line(mech[lab], raw)
            n_letters += a; n_ins += b; n_lines += (new != raw)
            res.append(lab + '\t' + new)
        if write:
            open(p, 'w', encoding='utf8', newline='\n').write('\n'.join(res) + '\n')
    print(f'{n_lines} lines changed, {n_letters} letters marked, {n_ins} left-out cipher words written in braces'
          + ('' if write else ' (dry run; --write to save)'))


if __name__ == '__main__':
    main()

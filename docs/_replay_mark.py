"""Write into a reading file the marks the key replay asks for (docs/_replay.py).

    python docs/_replay_mark.py <folder>            # dry run: what would be marked
    python docs/_replay_mark.py <folder> --write    # put the marks in

Works for a target whose adapter's reading() returns a string of the same length as the reading file, position for
position (reading.path names the file; docs/_replay_groups.py does this). It changes no letter of the reading:

    [x]     a letter the key does not give for the group there (substituted or supplied), bracketed where it stands;
    [word]  the whole word, when the reading leaves out a letter the key gives inside it;
    ⟦x⟧     what the key gives for a group that falls between two words of the reading and is left out of it.
Differences that are only i/y, or a declared second value, are not marked. Run the replay again afterwards.
"""
import os, sys, io, re, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import _replay as R

APOS = chr(0x2019) + chr(39)


def letters(raw):
    """-> [(folded letter or '#', raw index, marked, word no)]."""
    out, depth, word, inword = [], 0, -1, False
    for i, c in enumerate(raw):
        if c.isspace():
            inword = False; continue
        if not inword:
            word += 1; inword = True
        if c == '[':
            depth += 1
        elif c == ']':
            depth = max(0, depth - 1)
        else:
            for ch in R.fold(c):
                out.append((ch, i, depth > 0, word))
    return out


def plan(words, raw, poly):
    mech, cu, units = R.build_mech(words)
    L = letters(raw); read = ''.join(x[0] for x in L)
    pairs = R.align(mech, read, [1.0 if units[u]['unit'] is not None else 3.0 for u in cu])
    m2r = {mi: ri for mi, ri in pairs if mi is not None}
    polyset = {u: {R.fold(x) for x in v} for u, v in poly.items()}
    hole = {mi for mi, ri in m2r.items() if ri is not None and read[ri] == '#'}
    changed = True
    while changed:
        changed = False
        for mi in range(len(mech)):
            if m2r[mi] is None and mi not in hole and (mi - 1 in hole or mi + 1 in hole):
                hole.add(mi); changed = True
    need, whole, left = set(), set(), []
    for mi, ri in pairs:
        if mi is None:
            if read[ri] != '#' and not L[ri][2]:
                # a whole inserted word is "added by the reading": left alone, the replay lists it
                w = L[ri][3]
                if any(m2r_r is not None for m2r_r in [next((m for m, r in m2r.items() if r is not None and L[r][3] == w), None)]):
                    need.add(ri)
        elif ri is not None:
            x, y = mech[mi], read[ri]; u = units[cu[mi]]
            if y == '#' or x == y or {x, y} == {'i', 'y'} or x == '#':
                continue
            if u['b'] - u['a'] == 1 and y in polyset.get(u['unit'], ()):
                continue
            if not L[ri][2]:
                need.add(ri)
    k = 0
    while k < len(mech):
        if m2r[k] is None and k not in hole and units[cu[k]]['unit'] is not None and units[cu[k]]['value'] is not None:
            j = k
            while j < len(mech) and m2r[j] is None and j not in hole:
                j += 1
            pw = L[m2r[k - 1]][3] if k and m2r.get(k - 1) is not None else None
            nw = L[m2r[j]][3] if j < len(mech) and m2r.get(j) is not None else None
            if pw is not None and pw == nw:
                whole.add(pw)
            else:
                at = L[m2r[j]][1] if j < len(mech) and m2r.get(j) is not None else None
                if at is not None:
                    while at and not raw[at - 1].isspace() and raw[at - 1] not in APOS: at -= 1
                    while at and raw[at - 1] == '[': at -= 1
                left.append((' '.join(dict.fromkeys(str(units[cu[q]]['unit']) for q in range(k, j))), mech[k:j], at))
            k = j
        else:
            k += 1
    for ri, x in enumerate(L):
        if x[3] in whole and x[0] != '#' and not x[2]:
            need.add(ri)
    return sorted({L[ri][1] for ri in need}), left


def main():
    folder = sys.argv[1]; write = '--write' in sys.argv
    tdir = os.path.join(R.ROOT, 'targets', folder)
    spec = importlib.util.spec_from_file_location('replay_' + folder, os.path.join(tdir, 'replay.py'))
    ad = importlib.util.module_from_spec(spec); sys.path.insert(0, tdir); spec.loader.exec_module(ad)
    path = getattr(ad.reading, 'path', None)
    if not path:
        sys.exit('this adapter does not give positions in its reading file (reading.path)')
    text = io.open(path, encoding='utf8', newline='').read()
    RD = ad.reading(); pos, left = [], []
    for label, words in ad.mechanical():
        raw = RD[label]
        assert len(raw) == len(text), 'reading() is not position-faithful to ' + path
        p, l = plan(words, raw, getattr(ad, 'POLYPHONY', {})); pos += p; left += l
    pos = sorted(set(pos)); out = list(text); edits = []; i = 0
    while i < len(pos):
        j = i
        while j + 1 < len(pos) and pos[j + 1] == pos[j] + 1:
            j += 1
        edits.append((pos[j] + 1, ']')); edits.append((pos[i], '['))
        i = j + 1
    for g, v, at in left:
        if at is not None: edits.append((at, '⟦' + v + '⟧ '))
    note = 'Conventions (key replay, 16 Nov 2026, docs/_replay.py): a letter or word in [ ] is also one the key does not give for the group there; ⟦x⟧ is what the key gives for a group that the text leaves out.'
    h = text.find('# Established text'); h = text.find(chr(10), h) + 1 if h >= 0 else None
    if h and 'Conventions (key replay' not in text: edits.append((h, chr(10) + note + chr(10)))
    for at, ch in sorted(edits, key=lambda e: (-e[0], e[1] == '[')):
        out.insert(at, ch)
    new = ''.join(out).replace('][', '')
    print(f'{folder}: {len(pos)} letters to mark' + ('' if write else ' (dry run; --write to save)'))
    for g, v, at in left:
        print(f'  left out by the reading: group {g} = {v}' + ('' if at is not None else ' (no place found, not written)'))
    if write:
        io.open(path, 'w', encoding='utf8', newline='').write(new)


if __name__ == '__main__':
    main()

"""Catalogue 1523: partial table for the cipher words of López Méndez to Bolívar, 29 Jan 1819.

The table is built FROM the assumed plaintext, so "no conflict" tests consistency only.

  python solve.py             write key.tsv and the decryption file, print the checks
  python solve.py --controls  also run the word-permutation control

Standard library only. Reads the transcription file next to this script.
"""
import pathlib, random, re, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = pathlib.Path(__file__).resolve().parent
TR = next(HERE.glob('transcription*.txt'))
OUT = HERE / TR.name.replace('transcription', 'decryption')

# assumed plaintext, one item per cipher word in document order; ? = no value assigned
WORDS = ['he', 'estado', 'preso', 'cinco', 'veces', 'y', 'he', 'salido', 'con', 'fianza', 'mac', 'gregor', 'para',
         'mar?caibo', 'santafe']
UNVALUED = 't?'

def lines():
    return [l.rstrip() for l in TR.read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')]

def cipher_words():
    """Comma, colon and stop close a word; a line with none of these at its end runs on into the next line."""
    return [w.split() for w in re.split(r'[,:.]', ' '.join(lines())) if w.strip()]

def fit(pairs):
    """Return (key, conflicts) in both directions: one sign to one letter and one letter to one sign."""
    k, back, bad = {}, {}, []
    for plain, signs in pairs:
        for a, b in zip(plain, signs):
            if a == '?' or b == UNVALUED: continue
            if k.setdefault(b, a) != a: bad.append((b, k[b], a))
            if back.setdefault(a, b) != b: bad.append((a, back[a], b))
    return k, bad

def main():
    cw = cipher_words()
    assert len(cw) == len(WORDS) and all(len(p) == len(c) for p, c in zip(WORDS, cw)), 'words do not align'
    pairs = list(zip(WORDS, cw))
    n = sum(map(len, cw))
    written = n - sum(1 for c in cw for s in c if s == UNVALUED)
    key, bad = fit(pairs)
    print(f'signs {n}, valued {written}, distinct valued symbols {len(key)}, conflicts {len(bad)}')
    print('with a digit:', sum(1 for c in cw for s in c if re.search(r'\d', s)))
    single = {}
    for i, (p, c) in enumerate(pairs):
        for s in c: single.setdefault(s, set()).add(p)
    print('symbols found in one word only:', ', '.join(sorted(s for s, v in single.items() if len(v) == 1 and s != UNVALUED)))

    with open(HERE / 'key.tsv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('cipher\tplain\n')
        for c, p in sorted(key.items()): f.write(f'{c}\t{p}\n')

    # decryption, line by line against the transcription
    dec = ['# Decryption of the transcription with key.tsv, line by line. The word division and punctuation are the writer\'s.',
           '# [?] = sign with no value. Accents are not in the cipher. The table is built from the assumed plaintext (NOTES.md).', '']
    for raw in TR.read_text(encoding='utf-8').splitlines():
        if raw.startswith('# f.'): dec.append(raw)
        elif raw.strip() and not raw.startswith('#'):
            dec.append(raw)
            dec.append(re.sub(r'[a-z]\d?\??(?: [a-z]\d?\??)*',
                              lambda m: ''.join(key.get(s, '[?]') for s in m.group(0).split()), raw))
    OUT.write_text('\n'.join(dec) + '\n', encoding='utf-8', newline='\n')

    # re-use check, not a held-out test: the two words were first guessed from context and use no new symbol
    train, _ = fit(pairs[:10])
    for i in (12, 14):
        print('re-use', WORDS[i], ' '.join(cw[i]), '->', ''.join(train.get(s, '#') for s in cw[i]))

    # column order: within one base letter, do the plain letters rise with the digit?
    cols = {}
    for s, p in key.items():
        if s[-1].isdigit(): cols.setdefault(s[0], []).append((int(s[1:]), p))
    for b, v in sorted(cols.items()):
        v.sort(); ok = all(x[1] < y[1] for x, y in zip(v, v[1:]))
        print(f'column {b}:', ' '.join(f'{d}={p}' for d, p in v), '(rising)' if ok else '(not rising)')

    if '--controls' in sys.argv:
        # the 14 words other than mar?caibo; a trial swaps plain words among cipher words of equal length
        core = [i for i in range(len(cw)) if '?' not in WORDS[i]]
        random.seed(1523)
        by_len = {}
        for i in core: by_len.setdefault(len(cw[i]), []).append(i)
        trials, zero, moved = 20000, 0, 0
        for _ in range(trials):
            perm = {i: i for i in core}
            for idx in by_len.values():
                sh = idx[:]; random.shuffle(sh)
                perm.update(zip(idx, sh))
            if not fit([(WORDS[i], cw[perm[i]]) for i in core])[1]:
                zero += 1
                moved += any(WORDS[i] != WORDS[perm[i]] for i in core)
        print(f'control: {trials} trials, {zero} without conflict, of which {moved} differ from the true assignment')

if __name__ == '__main__':
    main()

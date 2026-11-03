"""List the words of reading_marked_c1r.txt by how they rest on the signs, and print the counts used in NOTES.md.

Word division is the one check_marks.py uses: codes count as one word, a word split over two lines (x- / -y) counts once.
Classes:
  verbatim      every letter is a value of its sign, no mark
  convention    only {+x} marks for a double letter written once (a convention of this cipher)
  doubtful      rests on a sign marked doubtful in the transcription ({?x}), settled by sense
  value repair  {a/b}: the reading takes a value the sign does not have (che from a bare 5, et from a bare 4)
  restored      {+x} as a whole word: no sign under it at all (not a read word)
  context       code group read from context only, or a unit not read at all
Standard library only.
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def classify(w):
    if '[' in w and '_?' in w:
        return 'context'
    if re.fullmatch(r'\{\+[^}]*\}[,.]?', w):
        return 'restored'
    if re.search(r'\{[^}+?]*/', w):
        return 'value repair'
    if '{?' in w:
        return 'doubtful'
    if '{+' in w:
        return 'convention'
    return 'verbatim'


def main():
    cls = {}
    for l in (ROOT / 'reading_marked_c1r.txt').read_text(encoding='utf8').splitlines():
        if not l.startswith('L'):
            continue
        ln, _, t = l.partition('\t')
        t = re.sub(r'\[([^\] ]*) ([^\]]*)\]', lambda m: '[' + m[1] + '_' + m[2].replace(' ', '_') + ']', t)
        for w in t.split():
            if w.startswith('-'):
                continue
            cls.setdefault(classify(w), []).append(f'{ln}:{w}')
    for k in ('verbatim', 'convention', 'doubtful', 'value repair', 'restored', 'context'):
        v = cls.get(k, [])
        print(f'{k:13s} {len(v):3d}  ' + ' '.join(v))
    n = sum(len(v) for v in cls.values())
    g = lambda k: len(cls.get(k, []))
    signed = n - g('restored')
    read = g('verbatim') + g('convention') + g('doubtful') + g('value repair')
    print(f'words {n}; sign-bearing {signed} (the restored word has no sign)')
    print(f'read from the signs under the cipher\'s conventions: {read}/{signed} ({100*read/signed:.1f}%)')
    r2 = read - g('value repair')
    print(f'  without the value repairs: {r2}/{signed} ({100*r2/signed:.1f}%)')
    r3 = r2 - g('doubtful')
    print(f'  and without the words on a doubtful sign: {r3}/{signed} ({100*r3/signed:.1f}%)')


if __name__ == '__main__':
    main()

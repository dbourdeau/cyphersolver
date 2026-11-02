"""Language-model decoding of signs the DECODE scans cannot separate.

Each transcribed sign whose glyph class is ambiguous on the binarized images (the h-form with bar, the barred b, the
9 base, the go sign ...) becomes a set of candidate values, taken from the P17 key and from what the same glyph was
shown to mean on the slips aligned with a clear text (f. 5, f. 8, f. 136, see working_key.md). A beam search over the
candidates keeps the readings that score best with the it-cinquecento model (order 5, no spaces). Signs labelled `?`
stay unread: they may take any letter or nothing so the model can continue past them, and are always printed as [?].

usage: python lattice.py <folio> [--control] [--beam N]
  --control  f. 136: compare the chosen values with the labels fixed from the 1597 copy, over the ambiguous signs
Writes texts/f<folio>_lattice.txt (one line per cipher line) unless --control.
"""
import csv, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm

HERE = os.path.dirname(os.path.abspath(__file__))

# glyph class (from the transcription note) -> candidate values
CLASSES = [
    ('ħ', ['l', 'i', 'as', 'ar', 'c', 'is']),
    ('3/5 with bar', ['l', 'i', 'as', 'ar', 'c', 'is']),
    ('b with bar', ['el', 'es', 'er', 'et', 'ev', 'u']),
    ('b with double bar', ['el', 'es', 'er', 'et', 'ev', 'u']),
    ('go/9', ['come', 'quando', 'qua']),
    ('⊢', ['e', 'i']),
    ('ȝ', ['c', 'i', 'l', 'at']),
]
LABEL_CLASSES = {  # when the note gives no glyph, by label
    't': ['t', 'f'],
    'as': ['as', 'i'],
}
WORDS = {'CHE': 'che', 'CON': 'con', 'QUE': 'que', 'QUA': 'qua', 'QUI': 'qui', 'PER': 'per', 'PERCHE': 'perche',
         'NON': 'non', 'QUANTO': 'quanto', 'COME': 'come', 'QUANDO': 'quando', 'PERO': 'pero', 'VUY': 'uui'}
NAMES = {'Soldati': 'gentedarme', 'Roma': 'roma', 'Veneziani': 'uenetiani', 'Duca di Milano': 'ducademilano',
         'Papa': 'papa', 'Marchese di Mantova': 'marchesedemantoa', 'Conte d\'Urbino': 'contedurbino',
         'Re de Ragona': 'redaragona', 'Duca di Ferrara': 'ducadeferrara'}
WILD = list('abcdefghilmnopqrstuz') + ['']


def fixed_value(label):
    base = label.split('#')[0].rstrip('?')
    if base == 'NULL':
        return ''
    if base.startswith('NAME:'):
        return NAMES.get(base[5:], '')
    if base in WORDS:
        return WORDS[base]
    return base.lower()


def candidates(row):
    label, note = row['label'], row.get('note') or ''
    base = label.split('#')[0]
    if base.startswith('?') or base == '':
        return None                                    # unread
    head = note.split(';')[0]
    for key, vals in CLASSES:
        if key in head:
            v = fixed_value(label)
            return list(dict.fromkeys([v] + vals)) if v not in ('',) else vals
    if base.rstrip('?') in LABEL_CLASSES:
        return LABEL_CLASSES[base.rstrip('?')]
    if base.endswith('?') and base.rstrip('?') in WORDS:
        return ['come', 'quando', 'qua']
    return [fixed_value(label)]


def load(folio):
    rows = list(csv.DictReader(open(os.path.join(HERE, 'texts', f'f{folio}_transcription.tsv'), encoding='utf8'),
                               delimiter='\t'))
    return rows


def decode(rows, m, beam=400):
    A, k = m.A, m.order
    idx = m.index
    lp = m.lp
    mod = A ** (k - 1)
    # hypothesis: (score, state, choices)
    hyps = [(0.0, 0, 0, ())]                           # score, ctx int, ctx length, chosen indices
    for row in rows:
        cands = candidates(row)
        opts = WILD if cands is None else cands
        new = {}
        for sc, st, n, ch in hyps:
            for j, val in enumerate(opts):
                s, c, ln = sc, st, n
                for chr_ in val:
                    x = idx.get(chr_)
                    if x is None:
                        continue
                    if ln >= k - 1:
                        s += float(lp[c * A + x])
                    c = (c * A + x) % mod
                    ln += 1
                if cands is None and val == '':
                    s -= 2.0                           # an unread sign usually stands for something
                key = (c, ch[-3:] if False else None)
                h = (s, c, ln, ch + (j,))
                if c not in new or new[c][0] < s:
                    new[c] = h
        hyps = sorted(new.values(), key=lambda h: -h[0])[:beam]
    best = hyps[0]
    out = []
    for row, j in zip(rows, best[3]):
        cands = candidates(row)
        out.append('[?]' if cands is None else cands[j])
    return out


def main():
    folio = sys.argv[1]
    beam = int(sys.argv[sys.argv.index('--beam') + 1]) if '--beam' in sys.argv else 400
    m = lm.load('it-cinquecento', order=5, spaces=False)
    rows = load(folio)
    vals = decode(rows, m, beam)
    if '--control' in sys.argv:
        amb = [(r, v) for r, v in zip(rows, vals) if (candidates(r) or [0, 0]).__len__() > 1]
        ok = sum(1 for r, v in amb if v == fixed_value(r['label']))
        print(f'control f.{folio}: ambiguous signs {len(amb)}, decoder agrees with the copy-fixed label on {ok} '
              f'({ok / max(1, len(amb)):.1%})')
        miss = [(r['line'], r['pos'], fixed_value(r['label']), v) for r, v in amb if v != fixed_value(r['label'])]
        print('disagreements (line, pos, label, decoder):', miss[:40])
        return
    lines = {}
    for r, v in zip(rows, vals):
        lines.setdefault(r['line'], []).append(v)
    path = os.path.join(HERE, 'texts', f'f{folio}_lattice.txt')
    with open(path, 'w', encoding='utf8') as f:
        f.write(f'# f. {folio}: lattice decoding (lattice.py, it-cinquecento order 5, beam {beam}); [?] = unread sign\n')
        for ln in sorted(lines, key=int):
            f.write(f'{ln}\t{"".join(lines[ln])}\n')
    print('wrote', path)


if __name__ == '__main__':
    main()

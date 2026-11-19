import json
k = json.load(open('../../aaymeloglu/key.json'))['signs']
desc = {'+': 'plus/cross +', '11': 'two short vertical strokes (like 11)', 'c': 'c', '2': '2',
'Na': 'short dash (÷ family) with a tick or dot ABOVE it, with or without a dot below',
'Nb': 'short dash (÷ family), usually arched, with a dot BELOW only',
'N': '÷-type dash where the dots cannot be made out',
'Z': 'tall hook sign whose exact form cannot be made out',
'Zh': 'tall slanted stem ending in an open angular hook; no arm to the right at the baseline (may have a bar across the stem)',
'Za': 'the same tall hook with a horizontal arm leaving the stem to the right at the baseline (h- or 4-like)',
'LL': 'd-shape: bowl left of a right-leaning stem, long bar across the ascender',
'Zd': 'S-curve with no foot', 'Zx': 'open h-like sign with an extra cross-stroke',
'5': 'stem turning into an arm to the right at the baseline',
'b': 'plain b, no cross', '3': '3', 'm': 'm', 'eo': 'small o with a flag stroke to the right', 'n': 'n',
'gf': 'long-s shape', 'gd': 'round-backed d with curled top (like ∂)', 'UT': '⊥ (stem standing on a base stroke)',
'8': '8', '7': '7', '6': '6', 'x': 'x', 'xo': 'ω-like', 'P': 'π', 'oo': 'small o on a long underline',
'S': 'σ: o with a long flat top stroke', 'pb': 'b with a hooked flag at the top', 'a': 'a', '9': '9', '4': '4',
'o': 'o', 'L': 'L', 's': 'ς (final-sigma-like)', 'v': 'v / u shape', 'X3': 'ξ or tall 3', 'i': 'ı (dotless short stroke)',
'p': 'p', 'pp': 'p with a barred descender', 'Q': '9 or q with a long crossed or looped descender',
'PSI': 'open cup with a descender', 'PHI': 'closed circle with a vertical stroke through it',
'NN': 'large e-like loop', 'BB': 'cross with dots', 'CC': 'closed triangle', 'B': 'B', 'ET': 'bold λ, or a with a curl',
'D': 'δ', 'TH': 'Λ with a dot inside', 'RC': '2 with a long tail and a raised c', 'RD': '2 with a long tail and a raised hook sign',
'N22': 'the numeral 22 standing as a group', 'Y': 'y-like sign', '6o': '6 with a ring above', '###': 'stroke crossed by three bars',
'##': 'stroke crossed by two bars', 'RR': 'rr-like flourish', '9n': '9 standing alone or closing a group', 'Z°': 'ʒ with a ring',
'F': 'F', 'E9': 'e with a large loop', 'Zo': 'b or 3 with a ring', 'SQZ': 'terminal squiggle', 'Z°x': 'ʒ with a ring, struck through'}
skip = {'/', '/a', '/b', 'u', '?'}
labs = [l for l in k if l not in skip]
assert set(labs) == set(desc), set(labs) ^ set(desc)
rows, m = [], []
for i, l in enumerate(labs, 1):
    s = 'S%02d' % i
    rows.append(f'{s}\t{desc[l]}')
    m.append(f'{s}\t{l}')
open('../blind/SHEET.tsv', 'w').write('label\tshape\n' + '\n'.join(rows) + '\n')
open('../sheet_to_key.tsv', 'w').write('label\tkey_label\n' + '\n'.join(m) + '\n')
print(len(rows))

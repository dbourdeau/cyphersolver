"""Decode the cipher items of BnF fr. 3975 ff. 28 and 30 with key fr. 3995 no. 11 (key.md).

Writes reading.tsv: document, item, sign, value, class (letter / word / code / null).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

ALPHA = {
    'ƥ': 'a', '9': 'a', '◊': 'a', 'x': 'b', 'ƨ': 'c', 'K': 'c', 'ι': 'd', '1': 'd', 'ʃ': 'd',
    'b': 'e', 'h': 'e', '⊕': 'e', 'd': 'g', 'q': 'h', '∂': 'h', 'r': 'i', '7': 'i',
    'm': 'l', 'π': 'l', 't': 'm', 'é': 'n', '2': 'n', 'n': 'o', 'u': 'o', 'ꭓ': 'o',
    'Ŧ': 'p', 'g': 'q', 'z': 'q', 'c': 'r', '6': 'r', 'o': 's', '3': 's', 'a': 't',
    '4': 'u', '+': 'u', 'φ': 'x', '^': 'y', '<': 'y',
}
# capital letters for small words; F here is the small word "et" (this writer's p-sign is Ŧ)
WORDS = {'A': 'la', 'B': 'le', 'C': 'de', 'D': 'au', 'E': 'est', 'F': 'et', 'G': 'je', 'H': 'il',
         'K': 'me', 'L': 'ma', 'M': 'avec', 'N': 'par', 'O': 'pour', 'P': 'que', 'Q': 'qui',
         'R': 'quelle', 'T': 'faire', 'S': 'nous', 'V': 'vous', 'X': 'bien', 'Y': 'fort', 'Z': 'tout'}
CODES = {'94': 'le marquis', '6': "M. d'Entragues", '23': 'la reine de Navarre', '45': "le duc d'Espernon"}
# signs read as nulls in context: ∞ is not in the key (the key's rule: invented signs are nulls);
# ƥ after it in the f.30 run gives no sense as 'a' and is taken with it (see NOTES, Remaining gaps).
NULLS = {('run', 4), ('run', 5), ('dateline', 1)}
# z is the key's q-sign, but in the dateline it stands where n is needed (Randan): this writer's 2 and z
# are one shape (fr. 3413 f. 102: '2 4 7' = qui, 'x n 2' = bon).
OVERRIDE = {('dateline', 4): 'n'}


def decode():
    rows = []
    for line in open(os.path.join(HERE, 'ciphertext.txt'), encoding='utf8'):
        if not line.strip() or line.startswith('#'):
            continue
        rec, fol, kind, *signs = line.split()
        if kind == 'code':
            rows.append((rec, fol, kind, signs[0], CODES[signs[0]], 'code'))
            continue
        for i, s in enumerate(signs):
            if (kind, i) in NULLS:
                rows.append((rec, fol, kind, s, '', 'null'))
            elif (kind, i) in OVERRIDE:
                rows.append((rec, fol, kind, s, OVERRIDE[(kind, i)], 'letter'))
            elif s in WORDS and (s != 'K'):
                rows.append((rec, fol, kind, s, WORDS[s], 'word'))
            else:
                rows.append((rec, fol, kind, s, ALPHA[s], 'letter'))
    return rows


if __name__ == '__main__':
    rows = decode()
    with open(os.path.join(HERE, 'reading.tsv'), 'w', encoding='utf8') as f:
        f.write('record\tfolio\titem\tsign\tvalue\tclass\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    for kind in ('dateline', 'run'):
        print(kind, ' '.join(r[4] or '·' for r in rows if r[2] == kind))
    n = len(rows); nulls = sum(r[5] == 'null' for r in rows)
    print(f'{n} units, {n - nulls} read as sense, {nulls} nulls')

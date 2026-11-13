"""Build the candidate keys of catalogue 1500 from the one crib and the order rule, and freeze them.

    python scripts/build_keys.py        writes key_candidates.tsv and key_frozen.tsv

Crib (run R05 only, 9.13.1.37.3.13.7.9.33 before 'de / Grande'): 'ocupacion' gives o9 c13 u1 p37 a3 i7 n33.
Rule read off those values: vowels on the odd numbers 1-9 (u1 a3 . i7 o9, so e5 fills the gap), consonants on the
odd numbers from 11 in alphabetical order. c13, n33 and p37 fit three orders of the consonants, so all three are
kept as candidates and the held-out test (scripts/heldout.py) chooses between them:
  A  b c d f g h j k l ll m n ñ p q r s t v x y z        (k and ll, no ch)
  B  b c ch d f g h j l ll m n ñ p q r s t v x y z       (ch and ll, no k)
  C  b c ch d f g h j k l m n ñ p q r s t v x y z        (ch and k, no ll)
Written 12 Nov 2026, before any held-out run was decrypted. key_frozen.tsv is candidate A as the test chose it.
"""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
VOW = {1: 'u', 3: 'a', 5: 'e', 7: 'i', 9: 'o'}
ORDERS = {
    'A': 'b c d f g h j k l ll m n ñ p q r s t v x y z',
    'B': 'b c ch d f g h j l ll m n ñ p q r s t v x y z',
    'C': 'b c ch d f g h j k l m n ñ p q r s t v x y z',
}
CRIB = {9: 'o', 13: 'c', 1: 'u', 37: 'p', 3: 'a', 7: 'i', 33: 'n'}


def key(variant):
    k = dict(VOW)
    for i, letter in enumerate(ORDERS[variant].split()):
        k[11 + 2 * i] = letter
    for v, p in CRIB.items():
        assert k[v] == p, (variant, v, k[v], p)
    return k


if __name__ == '__main__':
    rows = ['value\tA\tB\tC\tsource']
    ka, kb, kc = key('A'), key('B'), key('C')
    for v in sorted(set(ka) | set(kb) | set(kc)):
        src = 'crib R05' if v in CRIB else ('vowel gap' if v == 5 else 'order rule')
        rows.append(f'{v}\t{ka.get(v, "")}\t{kb.get(v, "")}\t{kc.get(v, "")}\t{src}')
    (ROOT / 'key_candidates.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    fr = ['# frozen 12 Nov 2026: candidate A of scripts/build_keys.py (crib R05 + order rule), chosen by the held-out test',
          'value\tplain\tsource']
    for v in sorted(ka):
        fr.append(f'{v}\t{ka[v]}\t' + ('crib R05' if v in CRIB else ('vowel gap' if v == 5 else 'order rule')))
    (ROOT / 'key_frozen.tsv').write_text('\n'.join(fr) + '\n', encoding='utf-8')
    print('written')

"""Write key/key_T2.tsv from the frozen key/table_T2.json (and key/table_T.json for the tiers).

Usage (from dudout/):  python3 -I scripts/make_key_tsv.py > key/key_T2.tsv
Tiers: A = seen glossed on the training leaves (338, 377, 401, 421, 429, 461);
       B = interpolated in a syllable row with at least two values seen (row rule);
       A561 = added for T2 from the glosses of image 561 (the portion of measure 1, then spent).
Kinds: letter (14-36), sign (letter homophone), syllable (consonant+vowel rows, 334-337 qua..quo), word (whole word or name).
"""
import json, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T2 = json.load(open(os.path.join(HERE, 'key', 'table_T2.json'), encoding='utf-8'))
T1 = json.load(open(os.path.join(HERE, 'key', 'table_T.json'), encoding='utf-8'))
T, add = T2['T'], set(T2['ajouts'])
obs, intp = set(T1['obs']), set(T1['int'])
BLOCKS = [170, 182, 200, 217, 229, 241, 252, 266, 276, 298, 316, 339, 352, 364, 380]
SYL = {str(b + i) for b in BLOCKS for i in range(5)} | {'334', '335', '336', '337'}
def kind(k):
    if not k.isdigit():
        return 'sign'
    if 14 <= int(k) <= 36:
        return 'letter'
    return 'syllable' if k in SYL else 'word'
def tier(k):
    if k in add:
        return 'A561' if k not in obs else 'A'   # 61 and 92: seen in training, value restated with the article from 561
    return 'A' if k in obs else 'B'
order = sorted(T, key=lambda k: (not k.isdigit(), int(k) if k.isdigit() else 0, k))
print('# key\tvalue\ttier\tkind')
for k in order:
    print('%s\t%s\t%s\t%s' % (k, T[k], tier(k), kind(k)))

"""Sign groups for the ICIT/indus-website glyph ids, identified by rendering the font
(render_glyphs.py) and matching the shapes Parpola describes in 'Study of the Indus
Script' (2005). Loading helpers for data/corpus.tsv.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))

JAR = '740'                      # the most frequent sign; 741/742/745 are jar + strokes
FISH_PLAIN = '220'
FISH = {str(g) for g in (219, 220, 221, 222, 224, 226, 228, 229, 230, 231, 232, 233, 234,
                         235, 236, 240, 241, 242, 243, 244)}
ROOF_FISH = {'235', '236'}       # fish under a 'roof' (236 = the same between strokes)
CRAB = {'798', '794'}            # 'crab' without / with feet
FIG = {str(g) for g in (772, 773, 776, 783, 784, 785, 786)}   # three-branched 'fig'
FIG_CRAB = {'777', '778', '782'}  # 'fig' with the 'crab' inside
EYE = {'809', '832'}             # dot-in-oval, stroke-in-oval
WATER = {'904'}                  # 'two parallel curved lines'
POT = {'700'}                    # U / V 'pot'

# numeral glyphs and their value (strokes); short strokes 1-7, two tiers 13-19, long 31-36
NUMERAL = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '7': 7, '13': 3, '14': 4, '15': 5,
           '16': 6, '17': 7, '18': 8, '19': 8, '31': 1, '32': 2, '33': 3, '34': 4,
           '35': 5, '36': 6, '55': 12}

# composite glyphs that are two or more copies of one sign side by side: split them,
# so that sign repetition is counted as sequence (numerals such as 34 stay whole).
SPLIT = {'219': ['220', '220'], '792': ['809', '809'], '698': ['700', '700'],
         '697': ['700', '700', '700'], '699': ['705', '705'], '617': ['615', '615'],
         '821': ['820', '820'], '791': ['790', '790'], '401': ['400', '400'],
         '191': ['190', '190'], '69': ['70', '70'], '261': ['260', '260'],
         '381': ['380', '380'], '441': ['440', '440'], '479': ['480', '480'],
         '620': ['604', '604'], '629': ['632', '632'], '893': ['892', '892'],
         '389': ['390'] * 4, '799': ['798', '797'], '552': ['550', '551']}

WEST_ASIA = {'Kish', 'Luristan', 'Susa', 'Tell Umma', 'Ur', "Qala'at al-Bahrain",
             "Ra's al-Junayz", 'Salut', 'Karzakan', 'Saar', 'Hajar'}
CENTRAL_ASIA = {'Gonur Depe', 'Altyn Depe', 'Shortughai'}
OUTSIDE = WEST_ASIA | CENTRAL_ASIA | {'Unknown', ''}


def load(split=True):
    """Rows of data/corpus.tsv with 'seq' = reading-order list of lines (lists of ids)."""
    rows = []
    with open(os.path.join(HERE, 'data', 'corpus.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            lines, cur = [], []
            for g in r['signs_reading'].split():
                if g in ('0', '999'):
                    if cur:
                        lines.append(cur)
                    cur = []
                    continue
                cur.extend(SPLIT.get(g, [g]) if split else [g])
            if cur:
                lines.append(cur)
            r['seq'] = lines
            r['flat'] = [g for ln in lines for g in ln]
            rows.append(r)
    return rows


def south_asian(r):
    return r['site'] not in OUTSIDE


if __name__ == '__main__':
    # data/signs_reading.txt: one object per line, reading order, fused repeats split,
    # line breaks dropped; the file docs/_check_profile.py --measure counts.
    with open(os.path.join(HERE, 'data', 'signs_reading.txt'), 'w', encoding='utf-8') as f:
        for r in load():
            if r['flat']:
                f.write(' '.join(r['flat']) + '\n')

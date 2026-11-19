"""Final key and rendering for the Richelieu -> de Rancé cipher letters (BnF fr.3829 f.87, f.89; July 1629).

Run:  python final.py
"""
from parse import load, is_cipher

# Letters: 10-28 = a b c d e f g h i l m n o p q r s t u (scrambled).  29-33 / 34-38 = vowel homophones a e i o u.
KEY = {
    '10': 'c', '11': 'b', '12': 'g', '13': 'p', '14': 'l', '15': 'o', '16': 'r', '17': 'f', '18': 't',
    '19': 'a', '20': 'd', '21': 'i', '22': 'n', '23': 'h', '24': 'm', '25': 's', '26': 'u', '27': 'e', '28': 'q',
    '29': 'a', '30': 'e', '31': 'i', '32': 'o', '33': 'u',
    '34': 'a', '35': 'e', '36': 'i', '37': 'o', '38': 'u',
    '39': 'et',  # Avenel: frontière et menée, Chevreuse et autres (b33, 23 Oct 2026; was 'a')
    '40': 'de', '42': 'la',   # frequent-word codes
}
# Nomenclature (confirmed against Avenel, Lettres de Richelieu III, 1858)
NOMEN = {'43': 'NAME-43?', '47': '47(=17 f)', '51': 'le Roi', '52': 'la Reine mère', '54': 'Monsieur',
         '58': 'Mme de Chevreuse', '59': 'princesse Marie', '60': 'Mme de Longueville',
         '66': 'card. de La Valette', '83': "l'Espagne", '84': "l'Angleterre", '92': 'la Lorraine', '2': '2?'}
# Extension of Nov 2026 from the sibling letters in fr. 3828, 3825, 3835 (texts/key.md, "Extension"): word code 41
# and nine names, each from an Avenel footnote outside the held-out letters. None occurs in ff. 87, 89.
KEY['41'] = 'que'
NOMEN.update({'55': 'M. le Prince', '61': "le duc d'Epernon", '62': 'Montmorency', '67': 'Calori',
              '68': 'le cardinal de Berulle', '69': 'le garde des sceaux', '95': 'Nismes', '96': 'Castres',
              '97': 'Montauban'})

def sym(t):
    if t.startswith('~'):
        b = KEY.get(t[1:]); return (b * 2 if len(b) == 1 else b) if b else f'[{t}]'
    if t in NOMEN: return '{' + NOMEN[t] + '}'
    return KEY.get(t, f'[{t}]')

if __name__ == '__main__':
    for name, lines in load().items():
        print('---', name)
        for toks in lines:
            print(''.join(sym(t) if is_cipher(t) else ' ' + t.replace('_', ' ') + ' ' for t in toks))

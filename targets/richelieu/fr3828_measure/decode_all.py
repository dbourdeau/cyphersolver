"""Decrypt every figure run of texts/fr3828_avenel_figures.txt with the key, unedited (no correction, no choice).

Usage:  python fr3828_measure/decode_all.py texts/fr3828_avenel_figures.txt > texts/fr3828_decryption.txt

KEY and NOMEN are those of final.py @ 9736c436 (Daniel Bourdeau's fr. 3829 key), plus the extension of
Nov 2026 (texts/key.md, "Extension from fr. 3828, 3825, 3835"): 41 = que (word code) and nine nomenclator
figures named by Avenel's footnotes outside the test letters. ⟦...⟧ = a decoded run (·et· ·de· ·la· ·que· =
word codes); {...} = a nomenclator figure; {?NN} = a figure with no value in the key.
"""
import re, sys
KEY = {'10': 'c', '11': 'b', '12': 'g', '13': 'p', '14': 'l', '15': 'o', '16': 'r', '17': 'f', '18': 't',
       '19': 'a', '20': 'd', '21': 'i', '22': 'n', '23': 'h', '24': 'm', '25': 's', '26': 'u', '27': 'e', '28': 'q',
       '29': 'a', '30': 'e', '31': 'i', '32': 'o', '33': 'u', '34': 'a', '35': 'e', '36': 'i', '37': 'o', '38': 'u',
       '39': '·et·', '40': '·de·', '41': '·que·', '42': '·la·'}
NOMEN = {'51': 'le Roi', '52': 'la Reine mère', '54': 'Monsieur', '58': 'Mme de Chevreuse', '59': 'princesse Marie',
         '60': 'Mme de Longueville', '66': 'card. de La Valette', '83': "l'Espagne", '84': "l'Angleterre",
         '92': 'la Lorraine',
         # extension, Nov 2026 (Avenel's footnotes, outside the test letters CLIV and CLV)
         '55': 'M. le Prince', '61': "le duc d'Épernon", '62': 'Montmorency', '67': 'Calori',
         '68': 'le cardinal de Bérulle', '69': 'le garde des sceaux', '95': 'Nismes', '96': 'Castres',
         '97': 'Montauban'}

def dec(run):
    out = ''
    for t in run.split():
        d = t.startswith('~'); f = t.lstrip('~').replace('‹?›', '')
        if not re.fullmatch(r'\d+', f): continue
        if f in NOMEN: out += '{' + NOMEN[f] + '}'; continue
        v = KEY.get(f, '{?' + f + '}'); out += v * 2 if d and len(v) == 1 else v
    return out

HEAD = """# Decryption of fr3828_avenel_figures.txt with the key of texts/key.md (Daniel Bourdeau's fr. 3829 key, final.py
# @ 9736c436, plus the extension of Nov 2026), unedited: nothing corrected, nothing chosen. ⟦...⟧ = a run of figures
# decoded letter by letter (·et· ·de· ·que· ·la· = the word codes 39, 40, 41, 42); {...} = a nomenclator figure;
# {?NN} = a figure with no value in the key. Clear text and Avenel's footnotes kept for context.
# Made by fr3828_measure/decode_all.py. The reading (fr3828_reading.md) makes this into sentences and marks every
# place where it departs from it."""

if __name__ == '__main__':
    t = open(sys.argv[1], encoding='utf-8').read()
    print(HEAD)
    for m in re.finditer(r"== (.*?)\n(.*?)(?=\n== |\Z)", t, re.S):
        print('\n== ' + m.group(1))
        for l in m.group(2).rstrip('\n').splitlines():
            if l.startswith('#'): print(l); continue
            l = re.sub(r"\[([^\]]*)\]", lambda x: '⟦' + dec(x.group(1)) + '⟧' if re.search(r'\d', x.group(1)) else x.group(0), l)
            l = re.sub(r"\{(\d+)\}", lambda x: '{' + NOMEN[x.group(1)] + '}' if x.group(1) in NOMEN
                       else '⟦' + KEY[x.group(1)] + '⟧' if x.group(1) in KEY else '{?' + x.group(1) + '}', l)
            print(l)

"""How well do the CTTS label versions decode rows whose reading is established? For each version of the labels
(corrected, corrected2 ... corrected6) decode known rows left to right and compare the letters with the established
reading (reading_final.md), by difflib ratio over the letter strings (spaces and marks ignored)."""
import json, re, difflib, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
P = Path(r'C:\Users\dbour\cypher\research\ctts\projects\tsnsj479')
H = dict(zip('I U E A N 4 c B d - < p P q w O 6 S X 9 C 7'.split(), 'abgdhwzcvyklmnsefxqrjt'))
H.update({'Bc': 'c', 'J': 'y', '<5': 'k', 'f': 'm', 'a': 't', 's': 'r', '8': 'r', '5': 'r', 'e': 'c', 'b': 'l', 't': 'n', 'n': 'h'})
HL = dict(zip('אבגדהוזחטיכלמנסעפצקרשתן', 'abgdhwzcvyklmnsefxqrjtn'))
# established readings (Hebrew letters as on the page; dots/marks/? stripped), keyed by band
KNOWN = {'S2L09': 'מן תדכר גיראן ידי סלמי', 'S2L07': 'מגזת דמען גרי מן מקלתן', 'S2L06': 'אם הבת אלריח מן טלקא כאטמה',
         'S2L05': 'ואומט אלברק פי אלטלמא מן אטם', 'S1L01': 'חמאמתי כל הדה כדב', 'S1L11': 'אנא אלפקיר אסחאק אליהודי',
         'S1L04': 'למ גואה זבי ויבכ גוה כסהא', 'S1L02': 'אל קער בתאע רחמה יבכ גואה', 'S2L15': 'כסבתאן כסתבאן'}
def exp(s): return ''.join(HL.get(c, '') for c in s)
def dec(boxes, labels, band, side):
    img = band + '.png'; out = ''
    for b in sorted(boxes[img], key=lambda b: b['x']):
        lab = labels[img][str(b['n'])].lstrip('?').rstrip('.')
        if lab.startswith(('_', '#')): continue
        out += ('b' if side == 1 else 't') if lab == '7' else H.get(lab, '*')
    return out
print('version  ' + ' '.join(f'{b:6s}' for b in KNOWN) + '  mean')
for v in ['', '5', '8', '9', '10']:
    try:
        bx = json.load(open(P / f'boxes_corrected{v}.json', encoding='utf-8')); lb = json.load(open(P / f'labels_corrected{v}.json', encoding='utf-8'))
    except FileNotFoundError: continue
    r = []
    for band, e in KNOWN.items():
        r.append(difflib.SequenceMatcher(None, dec(bx, lb, band, int(band[1])), exp(e), autojunk=False).ratio())
    print(f"{('corr' + v):8s} " + ' '.join(f'{x:6.2f}' for x in r) + f'  {sum(r)/len(r):.3f}')
# first pass labels (blind) for comparison
fl = {}
for f in ('labels_s1.json', 'labels_s2.json'): fl.update(json.load(open(P / f, encoding='utf-8'))['labels'])
bx0 = json.load(open(P / 'boxes.json', encoding='utf-8')); r = []
for band, e in KNOWN.items():
    r.append(difflib.SequenceMatcher(None, dec(bx0, fl, band, int(band[1])), exp(e), autojunk=False).ratio())
print(f"{'blind':8s} " + ' '.join(f'{x:6.2f}' for x in r) + f'  {sum(r)/len(r):.3f}')

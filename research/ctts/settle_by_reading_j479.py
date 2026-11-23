"""Settle uncertain boxes by the verified reading (21 Nov 2026). In the rows whose text is established (the Burda lines S2L05-09,
the signature S1L11, S1L01, S1L02, S1L04 and S2L15; reading_final.md) the decoded letters of boxes_corrected8 are aligned with the
verified letters (difflib); an uncertain box (type name with a leading ?) whose letter matches loses its ?. This settles the
letter, not the drawn shape's novelty: those boxes are certain because the verified text needs this sign here, not because they
were checked by eye, so the table is less independent of the reading for them. Reads ...8, writes ...9, settled9.tsv, CTTS files."""
import json, difflib, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
B = json.load(open(P / 'boxes_corrected8.json', encoding='utf-8')); L = json.load(open(P / 'labels_corrected8.json', encoding='utf-8'))
H = dict(zip('I U E A N 4 c B d - < p P q w O 6 S X 9 C 7'.split(), 'abgdhwzcvyklmnsefxqrjt'))
H.update({'Bc': 'c', 'J': 'y', '<5': 'k', 'f': 'm', 'a': 't', 's': 'r', '8': 'r', '5': 'r', 'e': 'c', 'b': 'l', 't': 'n', 'n': 'h', 'y': 'r'})
HL = dict(zip('אבגדהוזחטיכלמנסעפצקרשתן', 'abgdhwzcvyklmnsefxqrjtn'))
KNOWN = {'S2L09': 'מן תדכר גיראן ידי סלמי', 'S2L07': 'מגזת דמען גרי מן מקלתן', 'S2L06': 'אם הבת אלריח מן טלקא כאטמה',
         'S2L05': 'ואומט אלברק פי אלטלמא מן אטם', 'S1L01': 'חמאמתי כל הדה כדב', 'S1L11': 'אנא אלפקיר אסחאק אליהודי',
         'S1L04': 'למ גואה זבי ויבכ גוה כסהא', 'S1L02': 'אל קער בתאע רחמה יבכ גואה', 'S2L15': 'כסבתאן כסתבאן'}
log = []
for band, e in KNOWN.items():
    img = band + '.png'; bx = sorted(B[img], key=lambda b: b['x']); seq = []; ids = []
    for b in bx:
        lab = L[img][str(b['n'])]; base = lab.lstrip('?').rstrip('.')
        if base.startswith(('_', '#')): continue
        seq.append(('b' if band[1] == '1' else 't') if base == '7' else H.get(base, '*')); ids.append((b['n'], lab))
    sm = difflib.SequenceMatcher(None, ''.join(seq), ''.join(HL.get(c, '') for c in e), autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            n, lab = ids[blk.a + k]
            if lab.startswith('?'):
                L[img][str(n)] = lab[1:]; log.append((f'{band}_{n}', lab + ' -> ' + lab[1:]))
json.dump(B, open(P / 'boxes_corrected9.json', 'w', encoding='utf-8'), indent=1)
json.dump(L, open(P / 'labels_corrected9.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'settled9.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\twhat\n'); [fh.write(f'{a}\t{b}\n') for a, b in log]
print(len(log), 'boxes settled by the verified reading')
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected9.json'), '--boxes', 'boxes_corrected9.json'], check=True)

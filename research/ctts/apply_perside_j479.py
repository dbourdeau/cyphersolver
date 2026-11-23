"""Per-side sort of the 7 / dash shapes (21 Nov 2026), on top of round 7. The long `>`-shaped stroke is the yod (`-`) on side 2
(the Burda words גיראן, ידי, גרי, פי, checked against the verified reading) and the scribe's bet on side 1 (S1L02 יבכ,
S1L04 ויבכ); on side 1 it is also the yod in the margin signatures, so the side-1 text 7s stay uncertain. Changes:
 (a) S2L09 x=1008, 1205 and S2L07 x=980 (yods the size rule had made `7`) go back to `-`;
 (b) S2L05's `?7` loop (the resh of אלברק) becomes `?8`;
 (c) the side-1 text 7 boxes not yet marked uncertain (S1L08, S1L13) become uncertain.
Reads boxes/labels_corrected7.json, writes ...8, corrections8.tsv and the CTTS files."""
import json, subprocess, sys
from pathlib import Path
P = Path(__file__).parent / 'projects' / 'tsnsj479'
B = json.load(open(P / 'boxes_corrected7.json', encoding='utf-8')); L = json.load(open(P / 'labels_corrected7.json', encoding='utf-8'))
REVERT = {('S2L09.png', 1008), ('S2L09.png', 1205), ('S2L07.png', 980)}
log = []
for img, bx in B.items():
    for b in bx:
        lab = L[img][str(b['n'])]; new = lab; base = lab.lstrip('?').rstrip('.')
        if (img, b['x']) in REVERT and base == '7':
            new = '-'
        elif img == 'S2L05.png' and base == '7':
            new = '?8'
        elif img.startswith('S1L') and base == '7' and not lab.startswith('?') and img not in ('S1L14.png', 'S1L09.png', 'S1L15.png', 'S1L16.png', 'S1L03.png'):
            new = '?7'
        if new != lab:
            L[img][str(b['n'])] = new; log.append((f"{img[:-4]}_{b['n']}", lab + ' -> ' + new))
json.dump(B, open(P / 'boxes_corrected8.json', 'w', encoding='utf-8'), indent=1)
json.dump(L, open(P / 'labels_corrected8.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
with open(P / 'corrections8.tsv', 'w', encoding='utf-8') as fh:
    fh.write('id\twhat\n'); [fh.write(f'{a}\t{b}\n') for a, b in log]
print(len(log), 'changes:', log)
subprocess.run([sys.executable, str(Path(__file__).parent / 'to_ctts.py'), str(P), str(P / 'labels_corrected8.json'), '--boxes', 'boxes_corrected8.json'], check=True)

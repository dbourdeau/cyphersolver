# Line-by-line decode of the pass-3 transcriptions with the DRAFT key (key/key_draft.json). Run from the target folder:
#   python3 scripts/decode.py .
# '?' = number with no value in the draft key; numbers read '?' or lost in the binding are left out (scripts/data.py clean()).
# On 114L line G32 the first group is the clear date 18/28 (written as a fraction), not a code number; shown as [18/28].
import sys, json
B = sys.argv[1]; sys.path.insert(0, B + '/scripts')
from data import load
key = json.load(open(B + '/key/key_draft.json', encoding='utf-8'))
def out(src, dst, title):
    rows = load(B + '/transcriptions/' + src)
    with open(B + '/decryptions/' + dst, 'w', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write('# Mechanical decode with the DRAFT key (resubstitution 0.65 on its own training text; not validated).\n')
        f.write('# Per line: the numbers, then one letter per number (? = no value). No word division in the cipher.\n\n')
        for lid, gs, gloss, _ in rows:
            if src.startswith('114L') and lid == 'G32' and gs and gs[0] == '28':
                f.write(f'{lid}  [18/28] ' + '.'.join(gs[1:]) + '\n')
                f.write(f'{lid}  [18/28] ' + ''.join(key.get(g, '?') for g in gs[1:]) + '\n\n')
                continue
            f.write(f'{lid}  ' + '.'.join(gs) + '\n')
            f.write(f'{lid}  ' + ''.join(key.get(g, '?') for g in gs) + '\n\n')
out('113R_L01-L18_pass3_final.tsv', '113R_L01-L18_draftkey.txt',
    '# Bonde, Paris, 13 Nov 1675 (second code 1-246): image 113 right, cipher lines L01-L18 (L19-L33 kept aside, see NOTES.md)')
out('114L_G01-G32_pass3_final.tsv', '114L_G01-G32_draftkey.txt',
    '# Bonde, Paris, 13 Nov 1675 (second code 1-246): image 114 left, cipher lines G01-G32 (the end of the letter)')

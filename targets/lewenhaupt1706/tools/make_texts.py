"""Writes the group-by-group decryptions, key.tsv and validation.tsv from a key file and the transcriptions.
usage (from the target folder): python3 -I tools/make_texts.py key/key_K3_after_measure.json
Notation in decryption files: code=value ; code=? (no value in the key) ; {clear text of the document} kept as is ;
[struck-out group] dropped, as in tools/score2.py."""
import sys, re, json
key = json.load(open(sys.argv[1], encoding='utf-8'))
DOCS = {'L3_21feb1706': ['L3_A_301', 'L3_A_302L', 'L3_A_302R', 'L3_A_303L', 'L3_A_303R'],
        'L4_2mar1706': ['L4_A_310_p1', 'L4_A_311L_p1', 'L4_A_311R_p1']}
val = []
for doc, files in DOCS.items():
    out = [f'# {doc}: decryption with {sys.argv[1]} (key fitted after the measurement; see NOTES.md)']
    for f in files:
        out.append(f'# --- {f}')
        for line in open(f'transcription/{f}.txt', encoding='utf-8'):
            if line.startswith('#') or not line.strip(): continue
            line = re.sub(r'\[[^\]]*\]', ' ', line.split('#')[0])
            toks = []
            for m in re.finditer(r'\{([^}]*)\}|(\d+)\??', line):
                if m.group(1) is not None: toks.append('{' + m.group(1) + '}')
                else:
                    c = m.group(2); v = key.get(c)
                    toks.append(f'{c}=' + ('?' if v is None else (v if v else '-')))
                    val.append((c, '?' if v is None else (v if v else '-')))
            out.append(' '.join(toks))
    open(f'{doc}_decryption.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
with open('key.tsv', 'w', encoding='utf-8') as k:
    k.write('# code\tvalue (\'\' = null). Key K3 = frozen K2 + values fitted after the measurement (protocol/K2_changes.tsv, NOTES.md)\n')
    for c in sorted(key, key=int): k.write(f'{c}\t{key[c]}\n')
with open('validation.tsv', 'w', encoding='utf-8') as v:
    v.write('# model: sv-modern\n# source: L3_21feb1706_decryption.txt, L4_2mar1706_decryption.txt (key/key_K3_after_measure.json)\n')
    v.write('# note: group values from the key fitted after the measurement; unknown groups as ?\n')
    for c, r in val: v.write(f'{c}\t{r}\n')
print(len(val), 'tokens', sum(1 for _, r in val if r != '?'), 'with a value')

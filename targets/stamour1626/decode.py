# decode.py - apply the period table of Besancon BM Ms 1580 f. 239 (key_f239.json) to the blind transcription
# of the cipher passages in Ms Granvelle 62 (transcription/ms62_cipher_blind.tsv), passage by passage and line by line.
# Usage: python3 decode.py key_f239.json transcription/ms62_cipher_blind.tsv > decryption_ms62.txt
# Signs not in the table (code numbers, other shapes) are shown as <token>; '|' = visible separator in the manuscript.
import sys, csv, json
K = json.load(open(sys.argv[1], encoding='utf-8'))
dec = {}
for part in ('table', 'au_dessus_des_lettres', 'notes_haut_gauche'):
    dec.update(K[part])
cur = None; line = None; out = []; n_in = n_off = 0
for row in csv.reader(open(sys.argv[2], encoding='utf-8'), delimiter='\t'):
    if not row or row[0].startswith('#') or row[0] == 'img' or len(row) < 5:
        continue
    img, pid, ln, t = row[0], row[1], row[2], row[4].strip().rstrip('?').strip()
    if (img, pid) != cur:
        cur = (img, pid); line = None
        out.append('\n## %s %s' % (img, pid))
    if ln != line:
        line = ln; out.append('\n%-6s ' % ln)
    if t == '':
        continue
    if t == '|':
        out.append(' | '); continue
    if t.startswith('[ill'):
        out.append('[...]'); continue
    if t in dec:
        out.append(dec[t]); n_in += 1
    else:
        out.append('<%s>' % t); n_off += 1
print('# Mechanical decode with the f. 239 table, no correction. %d signs in the table, %d off it (codes and other shapes).' % (n_in, n_off))
print(''.join(out).strip())

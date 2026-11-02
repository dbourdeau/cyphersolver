"""Convert the parallel session's pass-2 transcriptions of ff. 110 and 136 (f<n>_transcription.tsv: folio, line,
pos, label, note) into this folder's per-slip format: f<n>_tokens.tsv (line, sign, value), f<n>_signs.txt (one sign
per token, for docs/_check_profile.py --measure) and the reading f<n>_reading.md (from f<n>_text_peer.md).
Run from this folder: python import_peer.py

The label is the key value with a homophone index (i#2), a word sign in capitals, NULL or ?. A token is null when
labelled NULL or noted as filler (the padding after the title). It is unread when labelled ?, or when the note's
verdict is "unread" (which includes values taken from the 1597 copy only) or "name-open" (the name sign left blank
in the key); "differs" tokens keep their cipher value (Panaro against the copy's Tanaro). This reproduces the
alignment counts in f110_alignment.md (recto 96.5%, verso 69.6%) and f136_alignment_peer.md (98.3%)."""
import re

TITLE = {110: 'Milan 1 Nov 1446', 136: 'Milan 29 Nov 1446'}

for f, place in TITLE.items():
    rows = [l.rstrip('\n').split('\t') for l in open(f'f{f}_transcription.tsv', encoding='utf-8')][1:]
    tok, signs = ['line\tsign\tvalue'], []
    for folio, line, pos, label, note in (r + [''] * (5 - len(r)) for r in rows):
        m = re.search(r'\((agree|variant|differs|unread|null|name-open)', note)
        verdict = m.group(1) if m else ('unread' if re.search(r'unread\s*$', note) else '')
        ln = f'v{line}' if folio.endswith('v') else line
        sign = label or '?'
        if verdict == 'null' or label == 'NULL' or 'filler' in note:
            value = '{null}'
        elif verdict in ('unread', 'name-open') or label in ('', '?'):
            value = '[..]'
        else:
            value = label.split('#')[0]
        tok.append(f'{ln}\t{sign}\t{value}')
        signs.append(sign)
    open(f'f{f}_tokens.tsv', 'w', encoding='utf-8').write('\n'.join(tok) + '\n')
    open(f'f{f}_signs.txt', 'w', encoding='utf-8').write(' '.join(signs) + '\n')
    body = open(f'f{f}_text_peer.md', encoding='utf-8').read().split('\n', 2)[2]
    open(f'f{f}_reading.md', 'w', encoding='utf-8').write(
        f'# BnF italien 1583 f. {f} -- Filippo Maria Visconti to Francesco Sforza, {place} (cipher slip): reading\n\n'
        + body.strip() + '\n')
    n = len(tok) - 1
    nul = sum(1 for t in tok[1:] if t.endswith('{null}')); unr = sum(1 for t in tok[1:] if t.endswith('[..]'))
    print(f'f. {f}: {n} tokens, {nul} nulls, {unr} unread, {(n - nul - unr) / (n - nul):.1%} of non-null read')

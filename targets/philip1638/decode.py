"""Apply key_K3k_read.tsv to transcription.txt, token by token, nothing edited. Writes decryption.txt.

One output block per cipher line (L01 ... L69, L01 and L02 being the two halves of the first written line).
A token with several values in the key prints them all (y|i); a token with no value prints ‹x›; ∅ (null) prints nothing.
Where the key file lists a token twice (0 = b in K3k, 0 = a added after the test), both values are printed (b|a).
"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent

def load_key(name='key_K3k_read.tsv'):
    key = {}
    for line in (HERE / name).read_text(encoding='utf-8').splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('\t')
        c, v = parts[0], parts[1] if len(parts) > 1 else ''
        vals = key.setdefault(c, [])
        for x in v.split('|'):
            if x not in vals:
                vals.append(x)
    return key

def lines():
    return [l.split() for l in (HERE / 'transcription.txt').read_text(encoding='utf-8').splitlines()
            if l.strip() and not l.startswith('#')]

def decode_token(t, key):
    if t not in key:
        return '‹' + t + '›'
    vals = key[t]
    if vals == ['∅']:
        return ''
    return '|'.join(vals)

if __name__ == '__main__':
    key = load_key()
    out = ['# Decryption of AGS EST,LEG,3594,312 line by line with key_K3k_read.tsv (decode.py), nothing edited.',
           '# ‹x› = token without a value; a|b = token with several values in the key; the null ∅ prints nothing.',
           '# The established text is in reading.md (one line = one cipher line; L01 and L02 are printed there as L01-02).']
    ntok = nval = 0
    for i, toks in enumerate(lines(), 1):
        dec = [decode_token(t, key) for t in toks]
        ntok += len(toks)
        nval += sum(1 for d in dec if d.startswith('‹'))
        out.append(f'L{i:02d}\t' + ' '.join(toks))
        out.append('\t' + ' '.join(d for d in dec if d != ''))
    (HERE / 'decryption.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print(f'{len(lines())} lines, {ntok} tokens, {nval} without a value')

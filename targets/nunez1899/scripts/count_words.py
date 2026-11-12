"""Word counts for 9926: telegraphed tokens by kind (clear word, code word valued by the frozen key, code word valued
only from the contemporary translation 9927/9928, hole, telegraphed but not rendered)."""
from common import HERE, read_lines, read_key, decrypt_tokens
key = {}
for ln in open(HERE / 'key.tsv', encoding='utf-8'):
    if ln.startswith('#') or ln.startswith('code\t') or not ln.strip(): continue
    f = ln.rstrip('\n').split('\t'); key[f[0]] = (f[1], f[2])
plain_key = {k: v[0] for k, v in key.items()}
c = dict(clear=0, numbers=0, frozen=0, gloss=0, hole=0, not_rendered=0, signature=0)
for lab, toks in read_lines(HERE / 'transcription_9926.txt'):
    for code, val in decrypt_tokens(toks, plain_key):
        if code == '.': continue
        if lab == 'L22': c['signature'] += 1; continue
        if val is None:
            if lab == 'L16' and code in ('te', 'se') and toks.index(code) in (4, 5): c['not_rendered'] += 1
            elif code.replace('/', '').isdigit(): c['numbers'] += 1
            else: c['clear'] += 1
        else:
            basis = key[code][1]
            c['hole' if basis == 'hole' else 'frozen' if basis.startswith('frozen') else 'gloss'] += 1
c['total_tokens'] = sum(v for k, v in c.items())
print(c)

# usage: decode.py <transcription> [keyfile] : applies key.tsv (default) line by line. Letters lower case, code groups in [BRACKETS],
# nulls dropped (shown as . ), unknown codes as [#n]. No word division is added.
import re, sys
sys.stdout.reconfigure(encoding='utf8')
key = {}
for l in open(sys.argv[2] if len(sys.argv) > 2 else 'key.tsv', encoding='utf8'):
    if not l.startswith('#') and l.strip():
        f = l.rstrip('\n').split('\t')
        key[f[0]] = f[1]
for line in open(sys.argv[1], encoding='utf8'):
    if line.startswith('#') or not line.strip():
        continue
    lab, _, body = line.strip().partition(' ')
    out = []
    for t in re.findall(r'L\^\w+|\d+|\?|[A-Za-z]', body):
        v = key.get(t)
        if t == '?':
            out.append('?')
        elif not v:
            out.append(f'[#{t}]')
        elif v == 'null':
            out.append('.')
        elif len(t) == 1 and t.isalpha() and t not in 'LS':
            out.append(v)
        else:
            out.append(v if t == 'S' or v in ('cc','bb','dd','ff','gg','ll','mm','nn','pp','rr','ss','tt','uu','zz') else f'[{v.upper()}]')
    print(lab, ''.join(out))

"""Decode a sign transcription with a key (sign -> letter, 'x/y' = ambiguous, '-' = null, unknown -> [sign])."""
import sys
def key(path='../key_f128.tsv'):
    return dict(l.rstrip('\n').split('\t') for l in open(path) if l.strip() and not l.startswith('# '))
def dec(signs, k):
    out = []
    for s in signs:
        v = k.get(s)
        if v is None: out.append(f'[{s}]')
        elif v == '-': continue
        elif '/' in v: out.append('(' + v + ')')
        else: out.append(v)
    return ''.join(out)
if __name__ == '__main__':
    k = key(sys.argv[2] if len(sys.argv) > 2 else '../key_f128.tsv')
    for l in open(sys.argv[1]):
        if l.startswith('#') or not l.strip(): continue
        name, s = l.rstrip('\n').split('\t'); print(f'{name}: {dec(s.split(), k)}')

import json, re, sys, os
sys.path.insert(0, '.')
from fam1887 import FAM
key = json.load(open('key1887.json', encoding='utf8'))
def val(t):
    if t in key['sym']: return key['sym'][t]
    if t in FAM:
        f, v = FAM[t]; c = key['fam'].get(f)
        if c is None: return '[' + t + ']'
        return c.replace('V', v)
    return '[' + t + ']'
lines = []
for line in open('../transcription/R1887.txt', encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    lab, rest = line.split(' ', 1)
    out = []; toks = []
    for p in re.split(r'(\[[^\]]*\])', rest.strip()):
        if p.startswith('['): out.append(' ' + p + ' '); continue
        for t in p.split():
            t0 = t if t in key['sym'] else re.sub(r'\^.*', '', t); t0 = {'tt/': 'tt', 'S?': 'S', 'ten?': 'ten', 'sed?': 'sed'}.get(t0, t0)
            if t0 == 'p?': out.append('[p?]'); continue
            out.append(val(t0)); toks.append((t, val(t0)))
    print(lab, ''.join(out))
    if '-v' in sys.argv: print('    ', ' '.join(f'{a}={b}' for a, b in toks))

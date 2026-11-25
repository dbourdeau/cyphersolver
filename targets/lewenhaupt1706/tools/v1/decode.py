"""usage: decode.py <key.json|key_manual.txt> <transcription files...>  -> décodage (code inconnu = ‹n›)"""
import sys, re, json
def load_key(p):
    if p.endswith('.json'): return json.load(open(p, encoding='utf-8'))
    k = {}
    for line in open(p, encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        a = line.split(); k[a[0]] = '' if a[1] == '∅' else a[1]
    return k
K = load_key(sys.argv[1])
for f in sys.argv[2:]:
    print('==', f)
    for line in open(f, encoding='utf-8'):
        if line.startswith('#'): continue
        line = re.sub(r'\[[^\]]*\]', ' ', line.split('#')[0])
        out = []
        for m in re.finditer(r'\{([^}]*)\}|(\d+)\??', line):
            if m.group(1) is not None: out.append(' {' + m.group(1) + '} ')
            else: c = m.group(2); out.append(K[c] if c in K else '‹%s›' % c)
        print(''.join(out))

"""Print each line of a ct file with the Zifra Prima value of every token and its cheap digit-confusion variants."""
import sys, itertools
sys.stdout.reconfigure(encoding='utf-8')
key = {}
for l in open('keys/zifra_prima_R1789.tsv', encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k, v = l.rstrip('\n').split('\t'); key[k] = v
ALT = {'0': '08', '2': '27', '3': '35', '5': '538', '8': '85', '1': '17', '9': '9', '4': '4', '6': '6', '7': '72'}
def var(t):
    b, n = t[0], t[1:].rstrip('?')
    if not n.isdigit(): return []
    out = []
    for c in itertools.product(*[ALT.get(d, d) for d in n]):
        k = b + ''.join(c).lstrip('0')
        if k in key and k not in out: out.append(k)
    return out
for l in open(sys.argv[1], encoding='utf8'):
    if l.startswith('#'): print(l.rstrip()); continue
    out = []
    for t in l.split():
        vs = var(t)
        out.append(t + '{' + '|'.join('%s=%s' % (k, key[k]) for k in vs) + '}')
    print('  '.join(out))

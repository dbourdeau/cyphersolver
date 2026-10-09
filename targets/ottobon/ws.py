"""Worksheet: for each line of a ct file, the Zifra Prima candidates of every token and the beam draft line."""
import sys, itertools, subprocess, os
sys.stdout.reconfigure(encoding='utf-8')
ctf = sys.argv[1]
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
env = dict(os.environ, CLEN='1.45', WPEN='4')
env['WPEN'] = '5'
tag = os.path.basename(ctf).replace('.txt', '')
env['PLAINOUT'] = 'img/dl/plain_' + tag + '.txt'; env['SEQOUT'] = 'img/dl/seq_' + tag + '.json'
bl = subprocess.run([sys.executable, '-I', 'beam.py', ctf], capture_output=True, env=env).stdout.decode('utf8', 'replace').splitlines()
plain = open(env['PLAINOUT'], encoding='utf8').read()
i = 0
for l in open(ctf, encoding='utf8'):
    if l.startswith('# f.'): print(l.strip()); continue
    if l.startswith('#') or not l.strip(): continue
    print('  ' + '  '.join(t + ':' + '/'.join(key[k] if len(key[k]) < 9 else key[k][:8] for k in var(t)) for t in l.split()))
    print('  beam: ' + (bl[i] if i < len(bl) else '')); i += 1
print('PLAIN:', plain)

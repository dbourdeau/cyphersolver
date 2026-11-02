"""Print what the best slider settings actually produce: distinct hits and their neighbours in the source lists."""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.argv = sys.argv[:1]
TAPE = ['7092635814', '1946273508', '8346527190']
def tab(tape, s):
    k = tape.index(s); return {str(i): tape[(k + i) % 10] for i in range(10)}
T = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d+', g)]
m = open('refs/m.txt', encoding='utf-8').read().split('\n')
def show(fam, s, kind, a, b):
    idx = {}
    for i in range(a, b):
        for x in re.findall(r'(?<![\d-])\d{4,5}(?![\d-])', m[i]):
            idx.setdefault(x.zfill(5), i)
    t = [tab(TAPE[j], s[j]) for j in range(3)]
    if kind == 'dec': t = [{v: k for k, v in d.items()} for d in t]
    print('---', fam, s, kind)
    seen = set()
    for g in (g.zfill(5) for f in fam for g in T[f] if len(g) in (4, 5)):
        v = g[0] + t[0][g[1]] + t[1][g[2]] + t[2][g[3]] + g[4]
        if v in idx and v not in seen:
            seen.add(v)
            i = idx[v]
            print('  ', g, '->', v, '|', ' / '.join(x.strip()[:22] for x in m[i-1:i+3]))
    print('   distinct hits', len(seen))
VB = (15044, 15686); Z = (1197, 2060)
show(['w749', 'w746', 'w512', 'w513'], '792', 'dec', *VB)
show(['w752'], '823', 'enc', *VB)
show(['w643'], '307', 'enc', *VB)
show(['w643'], '299', 'dec', *Z)

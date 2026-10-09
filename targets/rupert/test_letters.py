"""Apply a letter table to the transcription: numbers < LIM read as letters ('.' = null), others shown as [n]."""
import re, sys
def table(spec):
    d = {}
    for tok in spec.split(','):
        n, l = tok.split(); d[int(n)] = l
    return d
K125 = table("2 a,3 .,4 e,5 i,6 .,7 .,8 .,9 o,10 v,11 c,12 g,13 l,14 q,15 s,16 x,17 b,18 f,19 k,20 n,21 .,22 p,23 r,24 t,25 w,26 y,27 z,28 d,29 h,30 a,31 e,32 i,33 n,34 o,35 v,36 .,37 f,38 k,39 p,40 m,41 q,42 r,43 .,44 e,45 c,46 z,47 y,48 g,49 e,50 i,51 o,52 e,53 v,54 .,55 a,56 s,57 x,58 a,59 o,60 t,61 w,62 v,63 i,64 a,65 .,66 d,67 e,68 o,69 h,70 .,71 a,72 e,73 i,74 o,75 v,76 v,77 i,78 l,79 m")
def groups(path):
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'#.*', '', t)
    return re.findall(r'\[[^\]]*\]|\S+', t)
def show(path, tab, lim, words=None):
    out = []
    for g in groups(path):
        if g.startswith('['): out.append(g); continue
        m = re.match(r'(\d+)', g)
        if not m: out.append(g); continue
        n = int(m.group(1))
        if n < lim: out.append(tab.get(n, '?%d' % n))
        else: out.append('<%s>' % (words or {}).get(n, n))
    s = ' '.join(out)
    s = re.sub(r'(?<=\b\w) (?=\w\b)', '', s)
    return s
if __name__ == '__main__':
    print(show(sys.argv[1], globals()[sys.argv[2]], int(sys.argv[3])))

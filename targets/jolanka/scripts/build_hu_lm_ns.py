# No-space Hungarian n-gram model (order 5) from the same texts: the cards run words together. python3 -I tools/build_hu_lm_ns.py lm_src out.json.gz
import sys, re, glob, gzip, json, math, collections, os
src, out = sys.argv[1], sys.argv[2]
ALPHA = 'aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz'
def strip_pg(t):
    a = re.search(r'\*\*\* ?START OF.*?\*\*\*', t); b = re.search(r'\*\*\* ?END OF', t)
    return t[a.end() if a else 0 : b.start() if b else len(t)]
N = 5; c = collections.Counter(); c4=collections.Counter(); total=0
for f in sorted(glob.glob(os.path.join(src, 'pg*.txt'))):
    t = strip_pg(open(f, encoding='utf-8', errors='replace').read()).lower().replace('õ','ő').replace('û','ű').replace('ô','ő')
    for para in re.split(r'[^'+ALPHA+r'\s]+', t):
        s = ''.join(ch for ch in para if ch in ALPHA); total += len(s)
        for i in range(len(s)-N+1): c[s[i:i+N]] += 1
        for i in range(len(s)-3): c4[s[i:i+4]] += 1
tot = sum(c.values()); tot4=sum(c4.values())
m = {'language':'hu','order':N,'spaces':False,'alphabet':ALPHA,'chars':total,'floor':math.log10(0.01/tot),
     'logp':{g: round(math.log10(n/tot),3) for g,n in c.items() if n>1}, 'floor4':math.log10(0.01/tot4), 'logp4':{g: round(math.log10(n/tot4),3) for g,n in c4.items()}}
gzip.open(out,'wt',encoding='utf-8').write(json.dumps(m, ensure_ascii=False)); print(total, len(m['logp']), len(m['logp4']))

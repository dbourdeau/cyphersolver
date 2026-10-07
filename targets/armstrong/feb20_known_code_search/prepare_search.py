#!/usr/bin/env python3
"""Prepare reproducible period-character model and normalized code tables. No external writes."""
import collections, json, math, pathlib, re, unicodedata, hashlib
D=pathlib.Path(__file__).resolve().parent

def norm(s):
    s=unicodedata.normalize('NFKD',s.lower())
    return ''.join(c for c in s if 'a'<=c<='z')
raw=(D/'feb20_ciphertext.txt').read_text()
ct=list(map(int,re.findall(r'\d+','\n'.join(l for l in raw.splitlines() if not l.startswith('#')))))
assert len(ct)==369 and len(set(ct))==216
corpus=norm((D/'period_austen_excerpts.txt').read_text())
# Add-alpha conditional character bigram model. Spaces are removed, joining syllables.
u=collections.Counter(corpus); b=collections.Counter(zip(corpus,corpus[1:])); alpha=.1
uni=[(u[chr(97+i)]+alpha)/(len(corpus)+26*alpha)*(1-1e-6) for i in range(26)]+[1e-6]
p=[]
for i in range(27):
    row=[(b[chr(97+i),chr(97+j)]+alpha)/(sum(b[chr(97+i),chr(97+k)] for k in range(26))+26*alpha)*(1-1e-6) for j in range(26)] if i<26 else uni[:26]
    p.extend([math.log(x) for x in row+[1e-6]])
tables={}
for fn in ['WE028.txt']:
    key={}
    for l in (D/fn).read_text(errors='replace').splitlines():
        m=re.match(r'^(\d+);(.*)$',l)
        if m: key[int(m[1])]=m[2]
    tables[fn[:-4]]=(1600,key)
arm=json.load(open('/Users/feyseel/Projects/feyseel-nl/.claude/skills/armstrong-972-cipher/data/key972.json'))['key']
tables['Armstrong972']=(1700,{int(k):v[0]['v'] for k,v in arm.items() if v})
with (D/'search_input.txt').open('w') as f:
    f.write('369\n'+' '.join(map(str,ct))+'\n')
    f.write(' '.join(map(str,map(math.log,uni)))+'\n'+' '.join(map(str,p))+'\n')
    f.write(str(len(tables))+'\n')
    for name,(N,key) in tables.items():
        f.write(f'{name} {N}\n')
        for i in range(N+1):
            s=norm(key.get(i,'')) or '?????'
            codes=[ord(c)-97 if c!='?' else 26 for c in s]
            internal=sum(p[a*27+b] for a,b in zip(codes,codes[1:]))
            hit={'the':1,'of':2,'and':3,'to':4,'a':5}.get(s,0)
            f.write(f'{len(s)} {codes[0]} {codes[-1]} {internal:.12f} {int(i in key and bool(norm(key[i])))} {hit}\n')
(D/'normalized_tables.json').write_text(json.dumps({k:{'modulus':n,'entries':v} for k,(n,v) in tables.items()},indent=2))
meta={'cipher_groups':len(ct),'distinct':len(set(ct)),'small_count':sum(x<100 for x in ct),'training_characters':len(corpus),'training_source':'https://www.gutenberg.org/cache/epub/1342/pg1342.txt','training_work':'Jane Austen, Pride and Prejudice (1813); seven disjoint web-extracted passages','model':'Add-0.1 character bigram conditional log probability; alphabet a-z; no spaces; unknown entry = five question marks with P(?)=1e-6','tables':{k:{'modulus':n,'known_entries':len(v)} for k,(n,v) in tables.items()},'sha256':{fn:hashlib.sha256((D/fn).read_bytes()).hexdigest() for fn in ['feb20_ciphertext.txt','WE028.txt','period_austen_excerpts.txt']}}
(D/'model_metadata.json').write_text(json.dumps(meta,indent=2))
print(json.dumps(meta,indent=2))

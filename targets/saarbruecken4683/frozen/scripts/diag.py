# Diagnostic APRÈS la mesure (non décisif) : groupes chiffrés déchiffrés par K, nombres non couverts
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from norm import norm
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
K=json.load(open(os.path.join(B,'CLE-K.json')))
L={int(k):v for k,v in K['lettres'].items()}; C={int(k):v for k,v in K['codes'].items()}
miss=collections.Counter(); out=[]
for l in open(os.path.join(B,'transcriptions','ARBITRE-297.txt')):
    m=re.match(r'(29\d[rv] L\d+) \| (.*)',l.strip())
    if not m: continue
    s=re.sub(r'\[[^\]]*\]',' ',m.group(2)); r=[]
    for t in re.findall(r'\{[^}]*\}|\?\?|\d+\??',s):
        if t.startswith('{'): r.append(t[1:-1])
        elif t=='??': r.append('·?·')
        else:
            n=int(t.rstrip('?'))
            if n>=200: r.append('<'+C.get(n,str(n)+'?')+'>')
            else:
                c=L.get(n,'?'); 
                if c=='?': miss[n]+=1
                r.append(c.upper())
    out.append(m.group(1)+' | '+' '.join(r))
print('\n'.join(out)); print('non couverts',sum(miss.values()),sorted(miss.items()))

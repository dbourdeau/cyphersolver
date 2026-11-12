# kt2.py (b53): parse tx files; decode with M1 table + sign map v2 + word map. Words shown UPPER-case in decode.
import re,json,os
def tokens(path):
    L=open(path,encoding='utf-8').read().splitlines()
    # FIX b53: only line 1 is a header; b47 kt.py dropped every line starting with the '#' cipher sign
    txt='\n'.join(L[1:] if L and L[0].startswith('# ') else L)
    out=[]
    for tok in re.findall(r'\{[^}]*\}|\S+',txt,flags=re.S):
        if tok.startswith('{'): out.append(('C',' '.join(tok[1:-1].split())))
        else:
            t=tok.replace('"','').replace('?','')
            out.append(('N',t) if t.isdigit() else ('L',t))
    return out
# sign map v2: b47 SIGN with K=s (was o), V=f, '-'=b, P=p, B=i, w=d, D=u, M?; H=g; U,⊥ unknown
SIGN2={"E":"e","y":"n","A":"r","F":"h","Q":"h","D":"u","G":"i","B":"i","X":"o","K":"s","L":"t","Z":"t","#":"c",
       "I":"l","x":"m","O":"a","o":"a","w":"d","H":"g","C":"f","V":"f","PP":"q","⊐":"k","T":"z","J":"k","P":"p","-":"b","U":"k","⊥":"z"}  # b61: PP=q, ⊥=z added  # U=k derived 21:45 (Bedeckung, Erklährung, zurück); added to code 22:15 (held-out 0529 has no U)
def load(table='frozen/table_M3.json',words='frozen/words_FROZEN_v2.json',sign=None):
    here=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    t=json.load(open(os.path.join(here,table)))
    w=json.load(open(os.path.join(here,words))) if os.path.exists(os.path.join(here,words)) else {}
    w={k:v for k,v in w.items() if not k.startswith('_')}
    return t,w,(sign or SIGN2)
def dec1(k,x,t,w,s):
    if k=='N': return t[x] if x in t else (w[x].upper() if x in w else '['+x+']')
    if k=='L': return s.get(x,'<'+x+'>')
    return ' {'+x[-30:]+'} '

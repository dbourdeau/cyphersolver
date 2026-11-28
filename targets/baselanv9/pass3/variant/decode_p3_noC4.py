"""Pass 3 decoder (own code, python3 -I). Rules: RULES_V3.md. One function decode_word(signs, KEY)."""
import re
PAIRS={('Tk','D1'):'re',('Tk','Cl'):'ri',('Ds','D1'):'ti',('Ds','Cl'):'tr',('Cl','Ds'):'rt'}
WORDS={('4','Cl'):'enim',('Lm','Cl'):'autem'}
ATT=('Oe^m','Oe"','Oe~','Oe^','Tk@^','Bx~')
SEP={'^':'m','_':'n'}
VC=re.compile(r'^[aeiou][rst]$')
def load_key(path):
    K={}
    for ln in open(path,encoding='utf-8'):
        p=ln.rstrip('\n').split('\t')
        if p[0]=='token' or p[0].startswith('#'): continue
        K[p[0]]=p[1]
    return K
def split_sign(sg,KEY):
    star='*' in sg; sg=sg.replace('*','')
    if sg.startswith('Tk') and '@' in sg and '^' in sg:      # C1
        sg='Tk@^'+sg[2:].replace('@','',1).replace('^','',1)
    for full in ATT:
        if sg.startswith(full):
            return full,star,[c for c in sg[len(full):]]
    bases=sorted([k for k in KEY]+['D1','D2','D3','Cl','?'],key=lambda s:-len(s))
    base=next((b for b in bases if sg.startswith(b)),None)
    if base is None:
        m=re.match(r'[A-Za-z0-9?]+',sg); b=m.group(0) if m else sg
        return b,star,[c for c in sg[len(b):]]
    return base,star,[c for c in sg[len(base):]]
def decode_word(signs,KEY):
    signs=[s for s in signs if s not in('Eq','Fill')]
    B=[split_sign(s,KEY) for s in signs]
    if tuple(b[0] for b in B) in WORDS and not any(b[2] for b in B):
        return WORDS[tuple(b[0] for b in B)],0
    out='';unk=0;i=0;hist=[];last_d=None
    chi=len(B)>=3 and B[0][0]=='X' and B[1][0]=='Tk' and B[2][0]=='Cl'   # C5
    while i<len(B):
        b,star,mods=B[i]; nxt=B[i+1][0] if i+1<len(B) else None; v=None
        if (b,nxt) in PAIRS and not [m for m in mods if m in '^_"']:
            v=PAIRS[(b,nxt)]; mods=B[i+1][2]; i+=1
        elif b in('D1','Cl'): v=None
        elif b=='D3' and last_d is not None: v=last_d
        elif b in('D2','D3'):
            ref=[x for x in hist if x[1]]
            if ref: v=ref[-1][0]
            else:
                vv=[x for x in hist if x[2] in('Lm','Bx','X')]
                if not vv: vv=[x for x in hist if x[0] in('a','e','i','o','u')]
                v=vv[-1][0] if vv else None
            last_d=v
        elif chi and i==0: v='ch'
        else: v=KEY.get(b)
        tilde=''
        if v is None: piece='[?]'; unk+=1; core=''
        else: piece=v; core=v
        for m in mods:
            if m in SEP:
                if core and VC.match(core): piece=piece[:-1]+SEP[m]+piece[-1]   # C2
                else: piece+=SEP[m]
            elif m=='"': piece+=core
            elif m=='~': tilde='~'
        out+=piece+tilde
        hist.append((core[-1] if core else '',star,b)); i+=1
    return out,unk
def decode_file(path,KEY):
    res=[]
    for ln in open(path,encoding='utf-8'):
        if ln.startswith('#') or '\t' not in ln: continue
        lid,txt=ln.rstrip('\n').split('\t'); dec=[]
        for w in txt.split(' / '):
            sg=w.split()
            if not sg or sg==['Fill']: continue
            d,u=decode_word(sg,KEY)
            if sg[-1]=='Eq': d+='='
            dec.append(d)
        res.append((lid,dec))
    return res

# Score the four remaining lead-892 items as set out in PLAN_malvezzi_rest.md (hashed 15:19 UTC).
# Decoding uses value() and the frozen sign values of the 8-3-12 test unchanged (../lead892_test/scripts/decode.py).
# Code-name normalisation only (no new values): T2's 'Pl' = the sheet code [PI]; '??[numeral12..16]' = numerals 12..16, which the
# frozen rules already read as doubled letters. Code words written in braces get KEY_BRIEF's values (plan, "Frozen key").
import sys, re, json, random
import os
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','..','lead892_test','scripts'))
import decode as D
from decode import value, VAL, norm
O=os.path.join(HERE,'..')+os.sep
CODEWORDS={'ki':'rustanus','ka':'passa','ke':'passa','mis':'iustusdeargento','zus':'hungariaeimperium','zos':'fratergeorgius',
 'zis':'ioannessigismundus','zes':'reginaisabella','zi':'hungaria','li':'venetia','le':'caesarea','cad':'constantinopolis',
 'eb':'orator','bi':'rexgalliae','ab':'galli','ros':'persae','vb':'rexpoloniae','sis':'ibrahimpassa','nis':'iunusbey'}
ITEMS={'8-2-24':(['P%02d'%i for i in range(1,21)]+['Q%02d'%i for i in range(1,7)],'witness/8-2-24_draft_8-2-10_fol74.txt',0.85,False),
 '9-1-2':(['N01','N02','N03'],'witness/9-1-2_19c_decipherment.txt',0.85,False),
 '8-3-10':(['M%02d'%i for i in range(1,11)],'witness/8-3-10_interlinear_fol160r.txt',0.80,True),
 '8-2-22':(['S01','S02','S03','S04','E01','E02','E03','E04','E05','E06'],'witness/8-2-22_interlinear_S_E.txt',0.80,True)}
def load(paths):
    T={}
    for p in paths:
        for line in open(O+p,encoding='utf-8'):
            m=re.match(r'^([A-Z]\d\d):\s*(.*)$',line.strip())
            if m: T[m.group(1)]=m.group(2).split()
    return T
def fix(t):
    if t.startswith('Pl'): t='PI'+t[2:]
    m=re.match(r'^\?\?\[numeral(1[2-6])\]$',t)
    return m.group(1) if m else t
def val(t,V,secondary):
    t=fix(t)
    if t.startswith('{'):
        w=t.strip('{}?').lower()
        if w in CODEWORDS: return [{c} for c in CODEWORDS[w]]
    c=norm(t); cc=c.lower() if (t.startswith('{') or c.lower()=='ras') else c
    if secondary:
        if cc=='U': return [{'g'}]
        if cc=='^': return [{'h'}]
        if cc=='??': return [{'q'}]
    return value(cc,V)
def decode(T,labels,V,secondary=False):
    seq=[]
    for k in labels:
        for t in T.get(k,[]): seq+=val(t,V,secondary)
    return [{x.replace('j','i').replace('v','u').replace('y','i') for x in s} for s in seq if s!='§']
def words_of(path,italian):
    W=[]
    for line in open(O+path,encoding='utf-8'):
        if line.startswith('#'): continue
        line=re.sub(r'^[A-Z]\d\d:','',line).lower().replace('...',' ')
        for w in line.split():
            w=w.replace('?','')
            w=w.replace('j','i').replace('v','u').replace('ae','e')
            if italian: w=w.replace('y','i')
            w=re.sub('[^a-z]','',w)
            if w: W.append(w)
    return W
def score(seq,words):
    ref=''.join(words); a,b=seq,ref; n,m=len(a),len(b)
    import numpy as np
    Dm=np.zeros((n+1,m+1),dtype=np.int32); Dm[:,0]=-np.arange(n+1); Dm[0,:]=-np.arange(m+1)
    for i in range(1,n+1):
        ai=a[i-1]; row=Dm[i-1]
        for j in range(1,m+1):
            Dm[i,j]=max(row[j-1]+(1 if b[j-1] in ai else -1),row[j]-1,Dm[i,j-1]-1)
    i,j=n,m; match=[False]*m; got=['']*m
    while i>0 and j>0:
        if Dm[i,j]==Dm[i-1,j-1]+(1 if b[j-1] in a[i-1] else -1):
            match[j-1]=b[j-1] in a[i-1]; got[j-1]='/'.join(sorted(a[i-1])); i-=1;j-=1
        elif Dm[i,j]==Dm[i-1,j]-1: i-=1
        else: j-=1
    return sum(match)/m, match, got, ref
def wordsread(words,match,got):
    pos=0; wr=0; out=[]
    for w in words:
        mm=match[pos:pos+len(w)]; g=got[pos:pos+len(w)]; pos+=len(w)
        if all(mm): wr+=1; out.append(w)
        else: out.append(''.join(c if ok else '['+(gg or '-')+']' for c,ok,gg in zip(w,mm,g)))
    return wr,' '.join(out)
if __name__=='__main__':
    T1=load(['transcription_T1_latin.txt','transcription_T1_italian.txt']); T2=load(['transcription_T2.txt'])
    res={}
    codes=[c for c,v in VAL.items() if not v.startswith('NOT') and v not in ('null','Imperator Turcorum')]
    vals=[VAL[c] for c in codes]
    for item,(labels,wit,mark,ital) in ITEMS.items():
        words=words_of(wit,ital); r={'witness_letters':len(''.join(words)),'witness_words':len(words),'pass_mark':mark}
        for tag,T in (('T1',T1),('T2',T2)):
            for sec in (False,True):
                sc,match,got,ref=score(decode(T,labels,VAL,sec),words); wr,txt=wordsread(words,match,got)
                key=tag+('_secondary' if sec else '_primary'); r[key]={'letters':round(sc,4),'words_read':wr}
                open(O+f'results/decode_{item}_{key}.txt','w').write(txt+'\n')
        rng=random.Random(1550); cs=[]
        for _ in range(200):
            vv=vals[:]; rng.shuffle(vv); V2=dict(VAL); V2.update(dict(zip(codes,vv)))
            cs.append(score(decode(T2,labels,V2),words)[0])
        r['controls_T2']={'n':200,'mean':round(sum(cs)/len(cs),4),'max':round(max(cs),4)}
        r['pass']=r['T2_primary']['letters']>=mark and r['T2_primary']['letters']>max(cs)
        res[item]=r; print(item,json.dumps(r))
    json.dump(res,open(O+'results/scores.json','w'),indent=1)

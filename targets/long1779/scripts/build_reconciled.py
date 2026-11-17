import sys,re,csv,collections
src,passB,out=sys.argv[1:4]
A={'a':'1','b':'B','c':'c','d':'d','e':'=','f':'j','g':'g','h':'\\','i':'.','j':'.','k':'?','l':'l','m':'+','n':'-','o':'o','p':'p','r':'v','s':'3','t':'t','u':'A','v':'^','w':'~','y':'y','x':'x','q':'q','z':'z',"'":''}
B={'a':'1','b':'0','c':'c','d':'ʃ','e':'-','f':'6','g':'9','h':'\\','i':'.','k':'2','l':'/','m':'m','n':'-','o':'o','p':'ꞔ','q':'?','r':'ʒ','s':'ʒ','t':'L','u':'ɩ','v':'i','w':'m','x':'+','y':':','z':'-',"'":''}
PB={}
for r in csv.reader(open(passB),delimiter='\t'):
    if r[0]=='image': continue
    PB[(r[0],r[1],r[2])]=r[5]
Apages={'15L','15R','16L'}
rows=[];tot=collections.Counter()
for line in open(src):
    if line.startswith('#') or not line.strip(): continue
    img,side,ln,alph,toks=line.rstrip('\n').split('\t',4)
    pa=('first-agent sign transcription: heldout_glyphs.txt' if img+side in Apages else 'first-agent reading only (NOTES_long1779.md sec. 5)') if alph!='-' else ''
    pb=PB.get((img,side,ln),'')
    parts=re.findall(r'\{[^}]*\}|<del:[^>]*>|<ins:[^>]*>|<box:[^>]*>|\([^)]*\)|\S+',toks)
    wn=0
    if alph=='-' or toks.startswith('('):
        rows.append([img,side,ln,alph,pa,pb,'','',toks,'plain' if alph=='-' else 'note']); continue
    for p in parts:
        inner=None
        if p.startswith('<ins:') or p.startswith('<del:') or p.startswith('<box:'):
            inner=p[5:-1].split(); tag=p[1:4]
        items=[(x,tag) for x in inner] if inner is not None else [(p,'')]
        for w,tag in items:
            if w.startswith('{') or w in (',',';','&','---','----',':','.'):
                if w.startswith('{'): rows.append([img,side,ln,alph,pa,pb,'','',w,'plain'])
                continue
            wn+=1
            if w=='?': sig,dec,conf='?','[unread]','U'
            elif w.startswith('#'): sig,dec,conf=w[1:],'[nonsense under key: %s]'%w[1:],'X'
            else:
                conf='H'
                if w.endswith('??'): conf='L'; w=w[:-2]
                elif w.endswith('?'): conf='M'; w=w[:-1]
                if '=' in w: dec,sig=w.split('=',1)
                else:
                    dec=w; K=A if alph=='A' else B
                    sig=''.join(K.get(c.lower(),'?') for c in w)
            if tag: dec=dec+' ('+tag+')'
            rows.append([img,side,ln,alph,pa,pb,str(wn),sig,dec,conf])
            tot[conf]+=1
with open(out,'w') as f:
    f.write('image\tside\tline\talphabet\tpassA\tpassB_shape_codes\tword\treconciled_signs\tdecoded\tconfidence\n')
    for r in rows: f.write('\t'.join(r)+'\n')
n=sum(tot.values())
print('cipher words',n,dict(tot))
print('read H %.1f%%, H+M %.1f%%, any reading %.1f%%, unread %.1f%%, nonsense %.1f%%'%(100*tot['H']/n,100*(tot['H']+tot['M'])/n,100*(tot['H']+tot['M']+tot['L'])/n,100*tot['U']/n,100*tot['X']/n))

import sys,re,random,collections,subprocess,unicodedata,math
A='abcdefghilmnopqrstuxyz'; IX={c:i for i,c in enumerate(A)}
EXTRA='''alteza altezas vuestras senor senores senoria capitan rey reyes reyna venecia venecianos turco francia frances franceses
napoles roma papa embaxador embaxadores cartas carta gente armada gonzalo cordoua garellano gayeta galeras dineros
ducados nueuas paz guerra tregua liga senado dux exercito castillo ciudad italia milan florencia pisa genoua ferrara
mantua marques duque cardenal pontifice ualentin cesar borja alexandre iulio maximiliano emperador alemanes espanoles
soldados caualleros infanteria artilleria fortaleza lugar lugares tierra mar pratica tratado concierto despues antes
dixo dize dizen escriuo escriui scriuo hecho hazer fazer haze manera mucho muchos muy bien mas menos agora ansi asi'''.split()
def words_file():
    L=[l.split() for l in open('words.txt')]; ws=[w for w,_ in L][:500]
    for w in EXTRA:
        w=w.translate(str.maketrans('jvkw','iucu'))
        if w not in ws: ws.append(w)
    return ws
def norm_words(t):
    t=t.lower().replace('ñ','n').replace('ç','c'); t=unicodedata.normalize('NFD',t)
    t=''.join(c for c in t if unicodedata.category(c)!='Mn').translate(str.maketrans('jvkw','iucu'))
    return re.findall(r'[a-z]+',t)
def task(tokens,signs,groups,ws,fix={}):
    S=len(signs);G=len(groups); si={s:i for i,s in enumerate(signs)}; gi={g:i for i,g in enumerate(groups)}
    ids=[si[t] if t in si else S+gi[t] for t in tokens]
    out=[f'{len(A)} {S} {G} {len(ws)} {len(ids)}',' '.join(map(str,ids))]
    for w in ws: out.append(f'{len(w)} '+' '.join(str(IX[c]) for c in w))
    for g,w in fix.items():
        if g in gi: out.append(f'FIX {gi[g]} {ws.index(w)}')
    return '\n'.join(out)+'\n'
def run(tk,iters,R,seed,unk=-12):
    open('task.txt','w').write(tk)
    o=subprocess.run(['./wsa','es.lm','task.txt',str(iters),str(R),str(seed),str(unk)],capture_output=True,text=True).stdout
    sm=list(map(int,o.split('\nSM')[1].split('\n')[0].split())); gw=list(map(int,o.split('\nGW')[1].split('\n')[0].split()))
    best=float(re.search(r'BEST (\S+)',o).group(1)); return best,sm,gw,o
def decode(tokens,signs,groups,ws,sm,gw):
    si={s:i for i,s in enumerate(signs)}; gi={g:i for i,g in enumerate(groups)}; out=[]
    for t in tokens:
        if t in si: out.append((A+'_')[sm[si[t]]])
        else:
            w=gw[gi[t]]; out.append(' ['+(ws[w] if w<len(ws) else ('?'+t if w==len(ws) else '_'+t))+'] ')
    return re.sub(' +',' ',''.join(out))

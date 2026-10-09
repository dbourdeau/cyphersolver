"""Split R116 into stroke-delimited words and decode each with the cifra ordinaria (letters only), for inspection."""
import re, sys
import dec_aj as D
def parse_parts(path="r116_cipher.txt"):
    src=open(path,encoding='utf8').read()
    return [D.parse(p) for p in re.split(r'^#.*$',src,flags=re.M) if p.strip()]
def is_stroke(t,i):
    d,dt=t[i]
    return d in '245' and not dt and i+1<len(t) and t[i+1]==('1',False) and not (i+2<len(t) and t[i+2]==('0',False))
def words(t):
    w=[];cur=[];i=0
    while i<len(t):
        if is_stroke(t,i):
            w.append((cur,t[i][0]));cur=[];i+=2;continue
        cur.append(t[i]);i+=1
    if cur: w.append((cur,None))
    return w
def letters(toks):
    out=[];i=0;n=len(toks)
    while i<n:
        d,dt=toks[i]
        if d=='0' and dt and i+1<n:
            s='0.'+toks[i+1][0];out.append((s,D.KEY.get(s,'?')));i+=2;continue
        if d!='0' and i+1<n and toks[i+1]==('0',False):
            s=d+'0';out.append((s,D.KEY.get(s,'?')));i+=2;continue
        s=d+('.' if dt else '');out.append((s,D.KEY.get(s,'?')));i+=1
    return out
if __name__=='__main__':
    for pi,t in enumerate(parse_parts()):
        for k,(w,st) in enumerate(words(t)):
            L=letters(w)
            print(pi,k,' '.join(s for s,_ in L),'|',''.join(c for _,c in L),'|',st)

# decode_once.py: decodes TRANSCRIPTION.tsv with KEY.tsv, once. No emendation. python3 -I decode_once.py
import re, sys, hashlib
D='/home/claude/keyless/ercole1547/'
def load_key(path=D+'KEY.tsv'):
    base={}; mark={}; special={}
    for l in open(path):
        if l.startswith('#') or not l.strip(): continue
        p=l.rstrip('\n').split('\t')
        if p[0]=='base': base[p[1]]=p[2]
        elif p[0]=='mark': mark[p[1]]=p[2]
        elif p[0]=='special': special[p[1]]=p[2]
    return base,mark,special
FIG={'S01','S02','S11','S12','S13','S17','S03','S24'}   # bases that take raised figures
def dec_token(tok,key):
    base,mark,special=key
    if tok.startswith('.') or tok.startswith('{'): return ''
    t=tok.replace('?','')
    if t in special: return special[t]
    b,_,m=t.partition('^')
    if b not in base: return '?'
    if not m: return base[b]
    if m=='-': return base[b]+base[b]
    if m=='/' and b in FIG: return base[b]+mark['^s']
    v=mark.get('^'+m)
    return base[b]+(v if v is not None else '?')
def decode(key=None,path=D+'TRANSCRIPTION.tsv'):
    key=key or load_key(); out=[]
    for l in open(path):
        if not l.startswith('16v'): continue
        pg,ln,t=l.rstrip('\n').split('\t')
        out.append((pg,int(ln),[dec_token(x,key) for x in t.split()]))
    return out
if __name__=='__main__':
    rows=decode()
    with open(D+'DECODE.txt','w') as f:
        f.write('# ercole1547 first-pass decode (figure of record). KEY.tsv sha256 %s\n'%hashlib.sha256(open(D+'KEY.tsv','rb').read()).hexdigest())
        f.write('# page line [BUILD|HELD-OUT] units separated by spaces; ? = no value; {L4s} = unresolved code sign\n')
        for pg,ln,u in rows:
            f.write('%s\t%d\t%s\t%s\n'%(pg,ln,'HELD-OUT' if ln>=7 else 'BUILD',' '.join(x for x in u if x)))
            f.write('%s\t%d\t%s\t%s\n'%(pg,ln,'joined',''.join(u)))
    print(open(D+'DECODE.txt').read())

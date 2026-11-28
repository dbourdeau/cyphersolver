import sys
def load(path):
    k={}
    for l in open(path,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        f=l.rstrip('\n').split('\t'); k[f[0]]=f[1].split('|')[0]
    return k
def decode(tokens,k):
    out=[]
    for t in tokens:
        if t in ('/','|'): out.append(' '); continue
        v=k.get(t,'?')
        out.append('' if v=='-' else (v if t in k else '['+t+']'))
    return ''.join(out)
if __name__=='__main__':
    k=load(sys.argv[1])
    for line in open(sys.argv[2],encoding='utf8'):
        line=line.split('#')[0].strip()
        if not line: continue
        lab,_,toks=line.partition(':')
        print(lab.strip(),decode(toks.split(),k))

import re,sys
MAPB={'Q':'B','D':'m','G':'g','N':'U','E':'Le','F':'L'}
def load(path,which,prefix):
    out=[]
    for line in open(path,encoding='utf-8'):
        if not line.startswith(prefix): continue
        hdr=' '.join(line.split()[:2]); body=line.rstrip('\n')[len(line.split(' ')[0])+1:]
        body=re.sub(r'^L1\s+\S+\s+','',line.rstrip('\n')) if prefix=='L1' else re.sub(r'^L2\s+\S+\s+','',line.rstrip('\n'))
        body=re.sub(r'\{del:[^}]*\}','',body)
        body=re.sub(r'\{ins:([^}]*)\}',r'\1',body)
        body=re.sub(r'\[([^|\]]*)\|[^\]]*\]',r'\1',body)
        body=re.sub(r'\[([^\]]*)\]',r'\1',body)
        if which=='B':
            body=''.join(MAPB.get(c,c) for c in body)
        body=body.replace('a','o').replace('E','o').replace('b','B').replace('F','L')
        body=body.replace('Le','E')
        out.append((hdr,body))
    return out
def words(lines):
    s=' '.join(b for h,b in lines)
    s=re.sub(r'=\s*','',s)          # line-end continuation
    s=s.replace('-','').replace('/',' ').replace('.','').replace(',','')
    return [w for w in s.split() if w]
if __name__=='__main__':
    for w in words(load(sys.argv[1],sys.argv[2],sys.argv[3])): print(w)

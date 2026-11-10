import re,sys
# table provisoire : rangées appariées 1/9, 3/7, 4/8 (homophones)
A={0:'d',1:'y',3:'a',7:'x',8:'n',9:'t'}
B={0:'o',2:'g',3:'a',4:'c',5:'r',6:'v',8:'f',9:'l'}
C={0:'e',2:'u',3:'i',5:'s',8:'b',9:'p'}
def val(n):
    t,u=divmod(n,10)
    g={1:A,9:A,3:B,7:B,4:C,8:C}.get(t)
    if g is None: return '?'+str(n)
    return g.get(u,'['+str(n)+']')
txt=open(sys.argv[1]).read()
for line in txt.splitlines():
    if line.startswith('#'): continue
    if line.startswith('T'): print('\n'+line); continue
    out=[]
    for tok in re.findall(r'<[^>]*>|\S+',line):
        if tok.startswith('<'): out.append(tok)
        elif re.fullmatch(r'\d\d\??',tok): out.append(val(int(tok[:2])))
        else: out.append('{'+tok+'}')
    s=' '.join(out)
    s=re.sub(r'(?<=[a-z\]\?\d]) (?=[a-z\[\?])','',s)
    print(s)

import sys,re
K={11:'m',12:'f',13:'a',14:'h',15:'e',16:'n',17:'p',18:'g',19:'b',20:'z',21:'d',22:'a',23:'t',24:'u',25:'o',
26:'[Inglesi]',27:'[Venetia]',28:'u',29:'[Consiglio]',30:'l',31:'r',32:'t',33:'c',34:'t',35:'o',36:'c',37:'i',38:'a',39:'o',40:'s'}
def dec(s):
    out=[];i=0
    s=re.sub(r'\s','',s)
    while i<len(s):
        if not s[i].isdigit(): out.append('{'+s[i]+'}');i+=1;continue
        n=int(s[i:i+2]) if i+1<len(s) and s[i+1].isdigit() else None
        if n is None: out.append('<'+s[i]+'>');i+=1;continue
        out.append(K.get(n,'['+str(n)+']'));i+=2
    return ''.join(out)
for line in open(sys.argv[1],encoding='utf-8'):
    if '|' in line:
        tag,ct=line.split('|',1); print(tag.strip(),':',dec(ct.strip()))

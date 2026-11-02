"""Apply the working key to the cipher lines (Lnn ...) inside the ``` block of transcription/d64_transcription.md."""
import re, sys

K = dict(pair.split("=") for pair in """p={c|o|a} C=[C] po=o 6=a o=a 2=a d=e 8=e 1=e q=g m=t a=m h=i F=n T=r b=r TT=s oo=o +=l #=u H=m 3=h 3-=y 4=d x=q O=u 9=v P=c Y=i 0=a qo=o OO=i B=b a.=i b.=r Q=f FI=[Barcelona] -o-=i o-=a ooo=ll |=""".split())

def dec(line):
    out = []
    for tok in re.findall(r'"[^"]*"|\S+', line):
        if tok.startswith('"'):
            out.append(tok.strip('"').upper())
        elif tok == '/':
            out.append(' ')
        else:
            t = tok.replace('(struck)', '').rstrip('?')
            out.append(K.get(t, '[' + t + ']'))
    return ''.join(x if x.isupper() or x == ' ' or x.startswith('[') else x for x in out)

src = open(sys.argv[1]).read()
blk = re.search(r'```(.*?)```', src, re.S).group(1)
for ln in blk.splitlines():
    m = re.match(r'(L\d\d) (.*)', ln)
    if m:
        print(m.group(1), dec(m.group(2)))

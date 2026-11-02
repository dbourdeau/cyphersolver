"""Apply the working 1474 key to the cipher lines (Knn ...) of transcription/d73_transcription.md (first ``` block)."""
import re, sys

K = dict(pair.split("=") for pair in """/.=e oo=e 4={a|r} -o-=s 9.=o -+-=s d=a ro=i 6=n q={i|t} lp=m y°=r 2=c +=a tt=m A= o-=t :.=d
3=b 2f:=o 3°=p me=qu A.=l o#=y e=h l=f 7=n 2:=c 7:=n ::=d 4:=l x.=f e~={u|v} o-o=e""".split())

def dec(line):
    out = []
    for tok in re.findall(r'"[^"]*"|\S+', line):
        if tok.startswith('"'):
            out.append(' ' + tok.strip('"').upper() + ' ')
        elif tok in ('/', '//'):
            out.append(' ')
        else:
            out.append(K.get(tok, '[' + tok + ']'))
    return ''.join(out)

blk = re.search(r'```(.*?)```', open(sys.argv[1]).read(), re.S).group(1)
for ln in blk.splitlines():
    m = re.match(r'(K\d\d) (.*)', ln)
    if m:
        print(m.group(1), dec(m.group(2)))

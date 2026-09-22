import re,sys,glob
G=open('f119_glyphs.txt',encoding='utf8').read().splitlines()
R=open('f119_reading.txt',encoding='utf8').read().splitlines()
for f in sys.argv[1:]:
    for ln in open(f,encoding='utf8'):
        m=re.match(r'(\d\d) \|',ln)
        if m:
            G=[ln.rstrip('\n') if g.startswith(m[1]+' |') else g for g in G]
        m=re.match(r'#R (\d\d) \| (.*)',ln)
        if m:
            n=m[1]; rd=m[2].strip(); unread=rd.count('[?')
            tot=len(re.findall(r"\[[^\]]+\]|'[a-z]+|\S",[g for g in G if g.startswith(n+' |')][0].split('|',1)[1]))
            R=[f"{n} {rd} || {tot} {unread}" if r.startswith(n+' ') else r for r in R]
open('f119_glyphs.txt','w',encoding='utf8').write('\n'.join(G)+'\n')
open('f119_reading.txt','w',encoding='utf8').write('\n'.join(R)+'\n')

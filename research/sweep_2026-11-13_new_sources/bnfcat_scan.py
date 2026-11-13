import re,sys,glob,json,os
D="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/bnfcat/"
cip=re.compile(r'(?:c[hli]{2,3}i?ff?r[ée]?[es]?\b|c[hl]i{1,3}ffre|en\s+chiffre|chiffr[ée]e?s?\b|cliiffre)',re.I)
dec=re.compile(r'd[ée]\s?c[hl]i{1,3}ff?r|dechiff|d[ée]chi?f|interlin|traduction|clef|clé|explication|résolu|dechifrement|déchiffr',re.I)
out=[]
for f in sorted(glob.glob(D+'*.txt')):
    t=open(f,errors='ignore').read()
    t=re.sub(r'[ \t]+',' ',t)
    pos=0
    for m in cip.finditer(t):
        a=max(0,m.start()-350);b=min(len(t),m.end()+350)
        w=t[a:b]
        if m.start()<pos: continue
        pos=m.end()+300
        local=t[max(0,m.start()-120):m.end()+160]
        has=bool(dec.search(local))
        out.append({'vol':os.path.basename(f)[:-4],'off':m.start(),'dec_near':has,'w':w.replace('\n',' ')})
json.dump(out,open(D+'../bnfcat_windows.json','w'),ensure_ascii=False)
import collections
c=collections.Counter((o['vol'],o['dec_near']) for o in out)
for k,v in sorted(c.items()): print(k,v)

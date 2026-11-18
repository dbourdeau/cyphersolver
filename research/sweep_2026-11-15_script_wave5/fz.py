import re,sys
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'-\s*\n\s*','',t); t=re.sub(r'\s+',' ',t)
hd=[(m.start(),m.group(1)) for m in re.finditer(r'(?:(?<=\. )|(?<=\] )|(?<=\) ))(\d{4,5}(?:\s*[-–—]\s*\d{4,5})?)\.\s[A-Z«"\'\^]',t)]
cip=re.compile(r"ch[i1l!jt]{1,2}[fl]{1,3}[rF]\w*|chitf\w*|cryptogr\w*|st[eé]ganogr\w*|[eé]criture secr\w+|en cypher|cifr\w+|jargon",re.I)
import bisect
pos=[p for p,_ in hd]
for m in cip.finditer(t):
    c=t[max(0,m.start()-60):m.end()+60]
    if re.search(r"Chifflet|Chiffrevast|romain|armes|au chiffre|Achille",c): continue
    i=bisect.bisect(pos,m.start())-1
    print(hd[i][1] if i>=0 else '?','|',c)

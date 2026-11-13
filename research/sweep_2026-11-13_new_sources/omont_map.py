import re,json,sys
D="/tmp/claude-0/-home-user-cyphersolver/6cad9ef2-f4c1-5b63-a0df-f48b5a524c6f/scratchpad/newsrc/bnfcat/"
vol=sys.argv[1]
t=open(D+vol+'.txt',errors='ignore').read()
# heading: line with only number (3-5 digits) + optional ., possibly 'bis'
heads=[(m.start(),m.group(1)) for m in re.finditer(r'\n\s*(\d{3,5}(?:[ -]?\d{3,5})?)\.?\s*\n\s*\n',t)]
# "Anc." markers give sequential ids
anc=[(m.start(),m.group(1)) for m in re.finditer(r'\(An[ce]\.?\s*(\d{3,5})',t)]
def heading_for(off):
    h=[x for x in heads if x[0]<=off]
    return h[-1] if h else None
cip=re.compile(r'avec\s+chiffre(?!\s+et\s+d[ée]|\s+et\s+commencement|\s+et\s+traduction)|en\s+chiffres?\b|Chiffres?\.\s*\(Fol|chiffr[ée]es?\b',re.I)
dec=re.compile(r'd[ée]\s?c[hl]i{1,3}ff?r(?!es\s)|dechiff|interlin|traduction|explication',re.I)
rows={}
for m in cip.finditer(t):
    local=t[max(0,m.start()-100):m.end()+150]
    if dec.search(local) : continue
    h=heading_for(m.start())
    rows.setdefault(h[1] if h else None,[]).append(m.start())
for k,v in rows.items():
    if len(v)>=1:
        # title: text after heading
        hs=[x for x in heads if x[1]==k]
        off=hs[0][0] if hs else 0
        title=re.sub(r'\s+',' ',t[off:off+260])
        print(k,len(v),title[:230])

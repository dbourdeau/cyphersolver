"""entry_table.py <words.tsv> <out.tsv>
Entry-count table from IA hOCR word boxes: an entry starts with a word whose left edge lies at the column's
left margin (continuation lines are indented and are skipped). Running heads, page numbers and section
headings are skipped. Output: leaf, col, entry_no, y, first words."""
import sys,re,statistics as st
from collections import defaultdict
W=defaultdict(list); D={}
for l in open(sys.argv[1],encoding='utf8'):
    f=l.rstrip('\n').split('\t'); leaf=int(f[0])
    W[leaf].append((int(f[1]),int(f[2]),int(f[3]),int(f[4]),f[7])); D[leaf]=(int(f[5]),int(f[6]))
out=open(sys.argv[2],'w',encoding='utf8')
for leaf in sorted(W):
    ws=W[leaf]; PW,PH=D[leaf]
    if len(ws)<150: continue
    hs=[w[3]-w[1] for w in ws if len(w[4])>3]; h=st.median(hs)
    # group into physical rows (by y center), across whole page
    ws.sort(key=lambda w:((w[1]+w[3])/2,w[0]))
    rows=[]
    for w in ws:
        yc=(w[1]+w[3])/2
        if rows and abs(yc-rows[-1][0])<h*0.55: rows[-1][1].append(w)
        else: rows.append([yc,[w]])
    # candidate entry starts: first word of a row-segment that begins with a capital letter (allow leading junk)
    starts=[]
    for yc,r in rows:
        r.sort(key=lambda w:w[0])
        # split row into segments separated by big gaps
        seg=[r[0]]
        segs=[]
        for w in r[1:]:
            if w[0]-seg[-1][2]>h*2.2: segs.append(seg); seg=[w]
            else: seg.append(w)
        segs.append(seg)
        for s in segs:
            t=' '.join(w[4] for w in s)
            starts.append((s[0][0],yc,t))
    xs=[x for x,y,t in starts if re.match(r"^[^\w]{0,2}[A-Z][a-zſ'’\"“”/]",t)]
    if len(xs)<20: continue
    # two margins: histogram peaks
    xs.sort()
    mid=PW*0.5
    left=[x for x in xs if x<mid]; right=[x for x in xs if x>=mid]
    if len(left)<8 or len(right)<8: 
        # page may be shifted; split at largest gap
        gaps=max(range(1,len(xs)),key=lambda i:xs[i]-xs[i-1]); left=xs[:gaps]; right=xs[gaps:]
    ma=st.median(left); mb=st.median(right)
    tol=h*1.3
    for c,m in (('a',ma),('b',mb)):
        ent=[(y,t) for x,y,t in starts if abs(x-m)<tol and re.match(r"^[^\w]{0,3}[A-Z]",t) and not re.match(r"^[^\w]{0,3}[A-Z]{1,4}[.,]?\s*$",t) and not re.match(r'^\W*\d',t)]
        # drop running-head row: entries above the first real entry by > 1.5 line pitch are heads
        ent.sort()
        if len(ent)<5: continue
        pitch=st.median([b[0]-a[0] for a,b in zip(ent,ent[1:])])
        # remove items that look like heads: in top region and with spaced capitals
        ent=[e for e in ent if not re.match(r"^\W*([A-Z]\s){1,3}[A-Z]?\W*$",e[1])]
        for i,(y,t) in enumerate(ent):
            out.write(f"{leaf}\t{c}\t{i+1}\t{int(y)}\t{t[:60]}\n")

"""Build a page/column/line table from a word-level OCR dump (words_<ed>.tsv).
Output TSV: leaf, header_number_ocr, col, line, y, text.
Line 1 = first text line under the running head; lines numbered by pitch from the first body row (both columns share a grid)."""
import sys, re, statistics as st
from collections import defaultdict
rows=defaultdict(list); dims={}
for l in open(sys.argv[1],encoding='utf8'):
    leaf,x0,y0,x1,y1,W,H,t=l.rstrip('\n').split('\t')
    leaf=int(leaf); rows[leaf].append((int(x0),int(y0),int(x1),int(y1),t)); dims[leaf]=(int(W),int(H))
out=open(sys.argv[2],'w',encoding='utf8')
for leaf in sorted(rows):
    W,H=dims[leaf]; ws=rows[leaf]
    if len(ws)<60: continue
    hs=[w[3]-w[1] for w in ws if 3<len(w[4])]; h=st.median(hs) if hs else 20
    # text block bounds
    xs=sorted(w[0] for w in ws); left=xs[len(xs)//50]; right=sorted(w[2] for w in ws)[-len(ws)//50]
    # gutter: minimal coverage in middle band
    cov=[0]*(W+1)
    for x0,y0,x1,y1,t in ws:
        for x in range(max(0,x0),min(W,x1)): cov[x]+=1
    lo,hi=int(left+(right-left)*0.38),int(left+(right-left)*0.62)
    g=min(range(lo,hi),key=lambda x:sum(cov[x-3:x+4]))
    # header: topmost cluster
    ys=sorted(w[1] for w in ws)
    top=ys[0]
    # body rows per column
    cols={'a':[],'b':[]}
    for w in ws:
        c='a' if (w[0]+w[2])/2<g else 'b'
        cols[c].append(w)
    allrows={}
    for c,cw in cols.items():
        cw.sort(key=lambda w:(w[1]+w[3])/2)
        rr=[]
        for w in cw:
            yc=(w[1]+w[3])/2
            if rr and abs(yc-rr[-1][0])<h*0.7: rr[-1][1].append(w); rr[-1][0]=(rr[-1][0]*(len(rr[-1][1])-1)+yc)/len(rr[-1][1])
            else: rr.append([yc,[w]])
        allrows[c]=rr
    # pitch from rows that start near column left
    def starts(c):
        rr=allrows[c]
        if not rr: return []
        lx=sorted(min(w[0] for w in r[1]) for r in rr)[len(rr)//4]
        return [r for r in rr if min(w[0] for w in r[1])<lx+h*3 and len(' '.join(w[4] for w in r[1]))>8]
    sa,sb=starts('a'),starts('b')
    diffs=[]
    for s in (sa,sb):
        for i in range(1,len(s)):
            d=s[i][0]-s[i-1][0]
            diffs.append(d)
    if len(diffs)<10: continue
    base=st.median(diffs)
    pitch=st.median([d/round(d/base) for d in diffs if round(d/base)>=1 and abs(d/round(d/base)-base)<base*0.2])
    # header row: rows above first headword start by > 0.8 pitch
    hw=re.compile(r"^[^A-Za-z]{0,3}[A-Z][A-Za-z'’/ſ\"“”\-]{2,}[,.;:]")
    cand=[r for s in (sa,sb) for r in s if hw.match(' '.join(w[4] for w in sorted(r[1])))]
    if not cand: continue
    # first headword-like row that has at least 3 more headword rows within 5 pitches below it
    cand.sort(key=lambda r:r[0])
    first=None
    for r in cand:
        if sum(1 for q in cand if 0<q[0]-r[0]<5.5*pitch)>=3: first=r[0]; break
    if first is None: continue
    # refine anchor: robust phase from all starts
    phases=[((r[0]-first)/pitch)-round((r[0]-first)/pitch) for s in (sa,sb) for r in s if r[0]>=first-pitch*0.3]
    ph=st.median(phases); y1=first+ph*pitch
    header=' '.join(w[4] for c in allrows for r in allrows[c] if r[0]<y1-pitch*0.6 for w in r[1])
    nums=re.findall(r'\b(\d{1,3})\b',header)
    for c in ('a','b'):
        for r in allrows[c]:
            if r[0]<y1-pitch*0.6: continue
            n=round((r[0]-y1)/pitch)+1
            txt=' '.join(w[4] for w in sorted(r[1]))
            out.write(f"{leaf}\t{'/'.join(nums)}\t{c}\t{n}\t{int(r[0])}\t{txt}\n")

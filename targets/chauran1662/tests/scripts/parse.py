#!/usr/bin/env python3
"""Parse transcription files into records. parse(path) -> list of dict(sec, line, groups[list of (raw,num,mark,struck,doubt)], gloss)"""
import re, sys
def norm_group(tok):
    raw=tok
    struck=tok.startswith('X')
    if struck: tok=tok[1:]
    doubt='?' in tok
    # split number and mark
    m=re.match(r'^(\d+)(\?(\[[^\]]*\])?)?(:(.*))?$',tok)
    if not m:
        return dict(raw=raw,num=None,mark=None,struck=struck,doubt=True)
    num=int(m.group(1)); mark=m.group(5) or ''
    mm=re.match(r'^(B1|B2|D1|D2|D3|M|S1|S2|O|P)',mark)
    mk=mm.group(1) if mm else ('' if mark=='' else '?')
    return dict(raw=raw,num=num,mark=mk,struck=struck,doubt=doubt)
def tokenize(s):
    # tokens separated by spaces, but ?(...) descriptions contain spaces
    out=[];cur='';depth=0
    for ch in s.strip():
        if ch in '([': depth+=1
        if ch in ')]': depth=max(0,depth-1)
        if ch==' ' and depth==0:
            if cur: out.append(cur); cur=''
        else: cur+=ch
    if cur: out.append(cur)
    return out
def parse(path):
    recs=[];sec='';cur={}
    for ln in open(path,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if ln.startswith('## '):
            sec=ln[3:]; 
            if sec.lower().startswith('notes'): break
            continue
        m=re.match(r'^L(\d+[a-z]?)\s+([CG]):\s*(.*)$',ln)
        if not m: continue
        n,k,body=m.groups()
        key=(sec,n)
        if k=='C':
            recs.append(dict(sec=sec,line=n,groups=[norm_group(t) for t in tokenize(body)],gloss=None))
        else:
            for r in recs[::-1]:
                if r['sec']==sec and r['line']==n: r['gloss']=body; break
            else:
                recs.append(dict(sec=sec,line=n,groups=[],gloss=body))
    return recs
if __name__=='__main__':
    for p in sys.argv[1:]:
        r=parse(p); print(p,len(r),'lines',sum(len(x['groups']) for x in r),'groups')

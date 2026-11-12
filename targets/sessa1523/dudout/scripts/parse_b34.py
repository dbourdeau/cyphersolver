"""usage: parse_b34.py out.json
Parse Daniel's reading_r9660_b34.txt into (page, line, a, b) records for ff.141v-146v (read only)."""
import re, json, sys
import os
SRC=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','reading_r9660_b34.txt')
L=open(SRC,encoding='utf-8').read().split('\n')
recs=[];page=None;part=1;cur=None
pmap={'f.141r':'141r','f.141v':'141v','f.142r':'142r','f.142v':'142v','f.143r':'143r'}
p2map={'P4 left':'143v','P4 right':'144r','P5 left':'144v','P5 right':'145r','P6 left':'145v','P6 right':'146r','P7 left':'146v','P7 right':'147r'}
for i,ln in enumerate(L,1):
    if 'PART 2' in ln: part=2
    if 'SUMMARY ====' in ln or 'Open groups (with' in ln: page=None
    m=re.match(r'==== (f\.\d+[rv]) ',ln)
    if m: page=pmap[m.group(1)]; continue
    m=re.match(r'=== (P\d (?:left|right))',ln)
    if m: page=p2map[m.group(1)]; continue
    if page is None: continue
    if part==1:
        m=re.match(r'\s*(\d+)a\s(.*)',ln)
        if m: cur={'page':page,'line':m.group(1),'a':m.group(2).strip(),'b':'','src':i}; recs.append(cur); continue
        m=re.match(r'\s*(\d+)b\s(.*)',ln)
        if m and cur and cur['line']==m.group(1): cur['b']=m.group(2).strip()
    else:
        m=re.match(r'\s*(R?\d+) a\s(.*)',ln)
        if m: cur={'page':page,'line':m.group(1),'a':m.group(2).strip(),'b':'','src':i}; recs.append(cur); continue
        m=re.match(r'\s+b\s(.*)',ln)
        if m and cur and not cur['b']: cur['b']=m.group(1).strip()
recs=[r for r in recs if r['page'] not in ('141r','147r')]
json.dump(recs,open(sys.argv[1],'w'),ensure_ascii=False,indent=0)
from collections import Counter
print(Counter(r['page'] for r in recs)); print(sum(len(r['a'].split()) for r in recs),'raw a-items')

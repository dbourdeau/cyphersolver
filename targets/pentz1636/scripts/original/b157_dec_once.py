# dec_once.py tx key : one-shot decode with frozen Pentz-1636 tables. T1 only unless an indicator 62/13 appears (then T2 after 13, as b106). 3-digit and unmapped -> [n]. {x} struck -> skipped. '?' decoded as read.
import sys,re,hashlib
tx,kf=sys.argv[1:3]
assert hashlib.md5(open(tx,'rb').read()).hexdigest()=='1e70795fd31a4ee8c1c30dce00354226','tx md5'
assert hashlib.md5(open(kf,'rb').read()).hexdigest()==sys.argv[3],'key md5'
ns={}; exec(open(kf).read(),ns); T1,T2=ns['T1'],ns['T2']
tab=T1; out=[]
for l in open(tx):
    if not l.startswith('L'): continue
    lid,toks=l.split('|'); o=[]
    for t in toks.split():
        if t in '.,': o.append(t); continue
        if t.startswith('{'): o.append('{x}'); continue
        n=int(t.rstrip('?'))
        if n==62: tab=T1; o.append('<62>'); continue
        if n==13: tab=T2; o.append('<13>'); continue
        v=tab.get(n)
        o.append(v.upper() if v and t.endswith('?') else (v if v else '[%s]'%t))
    print(lid.strip(),' '.join(o)); print('    ',''.join(x if len(x)==1 and x not in '.,' else (' ' if x in '.,' else ' '+x+' ') for x in o))

"""final transcription = pass A + logged patches (patches.tsv); writes trans_final/pNN.txt and disagreements.tsv"""
import os,re,difflib,csv,sys
sys.path.insert(0,'scripts')
os.makedirs('trans_final',exist_ok=True)
P=[r for r in csv.DictReader(open('patches.tsv',encoding='utf8'),delimiter='\t')]
def toks(text):
    out=[]
    for ln,line in enumerate([l for l in text.splitlines() if l.strip()],1):
        line=re.sub(r'^L\d+\s*','',line); line=re.sub(r'\[[^\]]*\]|\{[^}]*\}','',line)
        for t in re.findall(r'\d[\d?]*|[A-Za-z]+',line): out.append((t,ln))
    return out
rows=[]
for n in range(1,27):
    p='%02d'%n
    lines=[l for l in open(f'trans_raw/p{p}_A.txt',encoding='utf8').read().splitlines() if l.strip()]
    reasons={}
    for r in P:
        if r['page']!=p: continue
        i=int(r['line'])-1
        assert r['old'] in lines[i], (p,r)
        lines[i]=lines[i].replace(r['old'],r['new'],1); reasons[i+1]=reasons.get(i+1,'')+r['reason']+'; '
    open(f'trans_final/p{p}.txt','w',encoding='utf8').write('\n'.join(lines)+'\n')
    a=toks(open(f'trans_raw/p{p}_A.txt',encoding='utf8').read()); b=toks(open(f'trans_raw/p{p}_B.txt',encoding='utf8').read())
    f=toks('\n'.join(lines))
    sm=difflib.SequenceMatcher(None,[x[0] for x in a],[x[0] for x in b],autojunk=False)
    fm=difflib.SequenceMatcher(None,[x[0] for x in a],[x[0] for x in f],autojunk=False)
    amap={}
    for op,i1,i2,j1,j2 in fm.get_opcodes():
        if op=='equal':
            for k in range(i2-i1): amap[i1+k]=f[j1+k][0]
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        ln=a[i1][1] if i1<len(a) else a[-1][1]
        fin=' '.join(amap.get(k,'(changed)') for k in range(i1,i2)) if i2>i1 else '(none)'
        rows.append([p,ln,i1,' '.join(x[0] for x in a[i1:i2]),' '.join(x[0] for x in b[j1:j2]),fin,
                     reasons.get(ln,'crop: pass A reading confirmed by eye')])
with open('disagreements.tsv','w',encoding='utf8',newline='') as fh:
    w=csv.writer(fh,delimiter='\t'); w.writerow(['page','lineA','tokpos','passA','passB','final','reason']); w.writerows(rows)
print('disagreements',len(rows))

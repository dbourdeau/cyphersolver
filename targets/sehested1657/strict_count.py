"""Strict recount of reading.md (integration check, 12 Nov 2026). Prints only; writes a JSON file only if a second path is given.
A token is a cipher word or a nomenclator symbol. Read = certain words + symbols whose value a gloss or clear of the time gives.
Holes = probable {words}, restored [words], unresolved words, symbol values given by the sense ([value, prob.]) and open symbols.
usage: python strict_count.py reading.md [out.json]"""
import re,sys,json
t=open(sys.argv[1],encoding='utf8').read()
secs=re.split(r'\n## ',t)[1:]
RESTORED_SKIP={'rayé','tache','tache»'}
rows=[];T=[0]*8
for s in secs:
    lid=s[:3]
    m=re.search(r'# Cipher words (\d+): certain (\d+), probable (\d+), restored (\d+), unresolved (\d+)',s)
    w,c,p,r,u=map(int,m.groups())
    body='\n'.join(l for l in s.split('\n')[1:] if not l.startswith('#'))
    sc=sp=so=0
    for b in re.findall(r'\[([^\]]*)\]',body):
        if b in RESTORED_SKIP: continue
        if b.endswith(', prob.'): sp+=1
        elif b[0].isupper() or b in('alliance','plenipotenz','befehl','defensiv','offensiv'): sc+=1
        else: pass # restored word, already in header count
    so=len(re.findall(r'‹[^›]*›',body))
    if lid=='L14': so-=1  # ‹copeilig› is the unresolved word, counted in header
    tot=w+sc+sp+so; read=c+sc
    rows.append((lid,w,c,p,r,u,sc,sp,so,tot,read,read/tot))
    for i,v in enumerate((w,c,p,r,u,sc,sp,so)): T[i]+=v
for r in rows: print('%s words %4d cert %4d prob %3d rest %2d unres %d | sym cert %3d sense %3d open %2d | tokens %4d read %4d = %.1f%%'%(r[:11]+(100*r[11],)))
w,c,p,r,u,sc,sp,so=T; tot=w+sc+sp+so
print('TOTAL',T,'tokens',tot,'read',c+sc,'= %.2f%%'%(100*(c+sc)/tot),'| lenient(words only) %.2f%%'%(100*(c+p)/w),'| middle %.2f%%'%(100*(c+p+sc+sp)/tot))
print('under95:',[r[0] for r in rows if r[11]<0.95])
if len(sys.argv)>2: json.dump({r[0]:dict(words=r[1],certain=r[2],probable=r[3],restored=r[4],unresolved=r[5],sym_certain=r[6],sym_sense=r[7],sym_open=r[8],tokens=r[9],read=r[10],share=round(r[11],4)) for r in rows},open(sys.argv[2],'w'),indent=1)

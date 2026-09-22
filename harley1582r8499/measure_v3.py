# measure_v3.py: non-null cipher signs on p1-2 of transcription_v2.txt vs the reading in final_v3_p12.txt
import re,sys
NULLS={'3','-2','r','q=','9','ft','xo','rho','d+','0','th','3r','tl','XX','t~','CURL_D','CURL_D_BAR','X_HOOK'}
tot={}
for L in open('transcription_v2.txt',encoding='utf8'):
    m=re.match(r'(p[12]\.\d\d) (.*)',L)
    if not m: continue
    toks=re.sub(r'\[[^\]]*\]',' ',m.group(2)).split()
    tot[m.group(1)]=sum(1 for t in toks if t not in('.',':') and t not in NULLS)
T=U=V=0
for L in open('final_v3_p12.txt',encoding='utf8'):
    m=re.match(r'(p[12]\.\d\d) \| (.*)',L)
    if not m: continue
    u=sum(map(int,re.findall(r'\[\?(\d+)\]',m.group(2))))
    v=sum(map(int,re.findall(r'\{[^}:]*:(\d+)\}',m.group(2))))
    t=tot[m.group(1)]
    if u+v>t: print('OVER',m.group(1),t,u,v)
    if '-v' in sys.argv: print(m.group(1),t,u,v)
    T+=t;U+=U*0+u;V+=v
print(f'# measured: {T} non-null cipher signs on p1-2; unread {U}; read {T-U} = {100*(T-U)/T:.1f}% (of which tentative {V}; firm {T-U-V} = {100*(T-U-V)/T:.1f}%)')

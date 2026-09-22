import sys, json, solve, solve2
NULLS={'3','-2','r','q=','9','ft','xo','rho','d+','0','th','3r','tl','XX'}
CODES={'-w':'the','w':'and','W':'and','k':'faire','l':'wordes','y':'us','o_':'haue','o=':'had','o':'hath','H_':'with','H=':'in',
 'B':'of','B=':'shall','B_':'should','D':'to','D=':'what','D_':'was','EE':'were','EE=':'where','EE_':'will','A=':'my','Ap':'none',
 'q)':'it','(q)':'is','Too':'theconstable','@':'yourhighness','n=':'therebels','n':'carew','-4':'that','G':'council','box':'thelowecountries',
 'C.':'thesaid','C:':'thatthey'}
PIN={'E':'c','xi':'o','7':'m','z':'i','<':'g','#':'e','mu':'n','x':'p','8':'e','ct':'e','^':'n','H':'y','S':'a','v':'a','x=':'e','Z=':'d','h':'k','ex':'s','+':'r'}
R=[]
for r in solve.runs_dotted():
    rr=[]
    for t in r:
        b=t.strip('.')
        if b in NULLS: continue
        if b in CODES: rr.append('@@'+b); continue
        rr.append(b if b in PIN else t)
    if rr: R.append(rr)
solve2.FIXED.clear(); solve2.FIXED.update({'@@'+k:v for k,v in CODES.items()})
if __name__=='__main__':
  s,key,txt=solve2.anneal(R,int(sys.argv[1]),800000,T0=20,W=0.5,order=4,pinned=PIN)
  print(round(float(s),1)); print(txt[:3000])
  json.dump({'key':key,'text':txt},open(f'pin6_{sys.argv[1]}.json','w'))

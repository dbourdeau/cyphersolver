import sys, json, solve, solve2
NULLS={'3','-2','r','q=','9','ft','xo','rho','d+','0','th','3r','tl','XX','NULL_LOOP','NULL_LOOP_BAR','CE_UNSEEN'}
CODES={'-w':'the','AND':'and','W':'and','k':'faire','l':'wordes','o_':'haue','o=':'had','O_SMALL':'hath','H_':'with','H=':'in',
 'B':'of','B=':'shall','B_':'should','D':'to','D=':'what','D_':'was','EE':'were','EE=':'where','EE_':'will','A=':'my','Ap':'none',
 'q)':'it','(q)':'is','Too':'theconstable','CIRC_LOOP':'yourhighness','CIRC_RING':'yourhighness','CIRC_DOT':'thefrenchking','O_BIG':'theemperor','O':'theemperor',
 'n=':'therebels','n':'carew','-4':'that','G':'council','box':'thelowecountries','CROWNED_BOX':'thelowecountries','/':'he','C.':'thesaid','C:':'thatthey','OMEGA_BAR':'whereunto'}
PIN={'ll':'o','sy':'w','ss':'w','SS_TAIL':'r','XUND':'s','X_BAR':'s','e/':'g','E_SLASH':'g','-8':'c','pt':'u','F':'u','d':'i','E':'c','xi':'o','7':'m','z':'i','<':'g','#':'e','mu':'n','x':'p','8':'e','ct':'e','^':'n','H':'y','S':'a','v':'a','x=':'e','Z=':'d','h':'k','ex':'s','+':'r','OMEGA':'d','CURL_D':'c','J+':'n','>':'o','q+':'h','nj':'k','P':'s','f-':'s','Y+':'s','Y_':'t','g+':'t','J':'m','or':'l','U_HOOK':'u'}
R=[]
for r in solve.runs(solve.os.path.join(solve.HERE,'transcription_v2.txt')):
    rr=[]
    for t in r:
        if t in NULLS: continue
        if t in CODES: rr.append('@@'+t); continue
        rr.append(t)
    if rr: R.append(rr)
solve2.FIXED.clear(); solve2.FIXED.update({'@@'+k:v for k,v in CODES.items()})
if __name__=='__main__':
  s,key,txt=solve2.anneal(R,int(sys.argv[1]),1000000,T0=20,W=0.5,order=4,pinned=PIN)
  print(round(float(s),1)); print(txt)
  json.dump({'key':key,'text':txt},open(f'pin9_{sys.argv[1]}.json','w'))

import sys,os,re,math
sys.path.insert(0,'..');from lang import lm
M=lm.load('fr-1600-letters',order=5,spaces=False)
C={'n':'e','u':'e','6':'er','C':'rle','e':'lr','x':'n','X':'tnv','m':'i','M':'noe','O':'o','7':'o',':':'t','~':'t','S':'s','c':'s','3':'da','9':'db','8':'nmvs','4':'c','+':'cqun','l':'asm','k':'as','#':'v','F':'v','P':'pq','Y':'vp','I':'b','B':'bs','D':'r','T':'la','b':'ea','z':'ip','s':'i','H':'l','w':'h','p':'cu','r':'ru','q':'gys','g':'g','π':'d','W':'s','1':'ac','/':'ca','E':'mvl','a':'d','∂':'d','2':'f','y':'aeiou','*':'v'}
W={'leur':'leur','que':'que','des':'des','les':'les','par':'par','la':'la','et':'et','vous':'vous','pour':'pour','qui':'qui'}
toks=open(sys.argv[1],encoding='utf8').read().split()
lat=[]
for t in toks:
    if t.startswith('{'):
        w=t[1:-1];lat.append([W.get(w,'')])
    else: lat.append(list(C.get(t,'?')))
# beam over strings; score with M.per_char-like incremental
def sc(s): 
    s2=lm.norm(s,'early',spaces=False)
    return M.score_idx(M.encode(s2)) if s2 else 0
beam=[('',0.0,[])]
for opts in lat:
    nb=[]
    for s,_,ch in beam:
        for o in opts:
            s2=s+o;nb.append((s2,None,ch+[o]))
    # score last 40 chars window approx full score
    nb=[(s,sc(s[-60:])+0.0,ch) for s,_,ch in nb]
    # use cumulative: rescore full only for ranking
    nb.sort(key=lambda x:-sc(x[0]))
    beam=nb[:60]
print(beam[0][0])

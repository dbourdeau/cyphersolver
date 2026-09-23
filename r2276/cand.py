# cand.py "S1 S2 ..." [maxwords]  -> lexicon words / word pairs matching the sign string under key_v6
import sys,json,re,os
K=json.load(open(os.environ.get('KEY','key_v6.json'),encoding='utf8'))
L=json.load(open(os.environ.get('LEX','lex2.json'),encoding='utf8'))
toks=sys.argv[1].split()
def alt(t):
    if t=='?': return '[a-z]{0,3}'
    vs=K.get(t,'*').split(',')
    if '*' in vs: return '[a-z]{1,6}'
    opts=[v for v in vs if v]
    r='(?:'+'|'.join(re.escape(v) for v in opts)+')'
    return r+('?' if '' in vs else '')
pat=re.compile('^'+''.join(alt(t) for t in toks)+'$')
words=[w for w in L if L[w]>=2]
hits=[(L[w],w) for w in words if pat.match(w)]
hits.sort(reverse=True); print('1w:',[w for c,w in hits[:40]])
if len(sys.argv)>2:
    # two words split
    res=[]
    for i in range(1,len(toks)):
        p1=re.compile('^'+''.join(alt(t) for t in toks[:i])+'$'); p2=re.compile('^'+''.join(alt(t) for t in toks[i:])+'$')
        a=[w for w in words if L[w]>=5 and p1.match(w)]; b=[w for w in words if L[w]>=5 and p2.match(w)]
        for x in a:
            for y in b: res.append((min(L[x],L[y]),x+' '+y))
    res.sort(reverse=True); print('2w:',[w for c,w in res[:60]])

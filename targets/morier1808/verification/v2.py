# PREREG v2 metric (written before the v2 held-out is transcribed)
import sys,json,random,itertools; sys.path.insert(0,'/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/morier-1808/work/scripts'); from common import *
NAMES={'persia','persian','persians','malcolm','malcolms','harford','jones','minto','bagdad','baghdad','bushire','busheer',
 'tehran','teheran','taehran','gardane','bombay','sapphire','pashaw','pacha','pasha','shah','abbas','mirza','gulph','basra',
 'bussora','bussorah','mascat','muscat','ispahan','shiraz','tabriz','erzeroum','constantinople','georgia','napoleon','bonaparte',
 'india','england','britain','british','turkey','turkish','ottoman','russia','russian','russians','france','french','morier',
 'excel','excell','exc','excy','gov','gen','brig','hon','rt','inst','majesty','majestys','esq','capt','col','lieut','secy','sir','lord'}
V=set(vocab())
_W=set(w.strip().lower() for w in open('/usr/share/dict/web2') if w.strip().isalpha())
V|=_W|{w+x for w in _W if len(w)>2 for x in ('s','es','ed','d','ing')}|{w[:-1]+'ing' for w in _W if w.endswith('e') and len(w)>3}
def norm_variants(s):
    opts=[('u','v') if c=='u' else ('i','j') if c=='i' else (c,) for c in s]
    for p in itertools.product(*opts): yield ''.join(p)
def inV(s):
    if len(s)==1: return s in ('a','i')
    return any(v in V for v in norm_variants(s))
def isName(s): return any(v in NAMES for v in norm_variants(s))
def classify(dec):
    """dec: list of decoded words. returns list of labels: word / name / split / fail"""
    n=len(dec); lab=['fail']*n
    for i,s in enumerate(dec):
        if '?' in s: continue
        if isName(s): lab[i]='name'
        elif inV(s): lab[i]='word'
    for i in range(n-1):   # copyist splits: two adjacent non-read pieces whose join is a word or name
        if lab[i]=='fail' or lab[i+1]=='fail':
            j=dec[i]+dec[i+1]
            if '?' not in j and (isName(j) or (len(j)>1 and inV(j))):
                for k in (i,i+1):
                    if lab[k]=='fail': lab[k]='split'
    for i,s in enumerate(dec):  # copyist joins: a fused word that splits into two read words
        if lab[i]=='fail' and '?' not in s:
            for c in range(1,len(s)):
                a,b=s[:c],s[c:]
                if all((len(x)>1 and (inV(x) or isName(x))) or x in ('a','i') for x in (a,b)):
                    lab[i]='join'; break
    return lab
def score(words,m):
    dec=[''.join(m.get(t,'?') for t in w) for w in words]
    lab=classify(dec); n=len(lab)
    return sum(l!='fail' for l in lab)/n, lab, dec
def measure(words,key,seed=1808,N=200):
    S,lab,dec=score(words,key)
    random.seed(seed); nums=sorted(key,key=int); vals=[key[k] for k in nums]; C=[]
    for _ in range(N):
        v=vals[:]; random.shuffle(v); C.append(score(words,dict(zip(nums,v)))[0])
    return S,max(C),lab,dec

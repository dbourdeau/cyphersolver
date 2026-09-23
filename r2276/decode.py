import sys,re,collections
KEY={'d':'a','-':'a','v':'a','2':'b','w':'c','7':'d','3':'d','x':'e','o':'e','z':'e','X':'e','F':'f',
'P':'p','4':'h','Q':'i','k':'i','y':'i','9':'i','t':'l','#':'l','V':'m','R':'n','e':'o','T':'o','0':'p',
'm':'r','g':'s','S':'s','A':'t','J':'t','c':'u','f':'u','b':'u','1':'[de]','n':'[et]'}
def load(files):
    L=[]
    for f in files:
        for line in open(f,encoding='utf8'):
            if line.startswith('#') or ':' not in line: continue
            k,v=line.split(':',1)
            L.append((f.split('.')[0]+'.'+k.strip(),merge([t for t in v.split() if t!='|'])))
    return L
PAIRS={('b','b'):'bb',('3','Z'):'3Z'}
def merge(toks):
    out=[];i=0
    while i<len(toks):
        if i+1<len(toks) and (toks[i],toks[i+1]) in PAIRS: out.append(PAIRS[(toks[i],toks[i+1])]); i+=2
        else: out.append(toks[i]); i+=1
    return out
if __name__=='__main__':
    L=load(sys.argv[1:] or ['p1.txt'])
    c=collections.Counter(t for _,l in L for t in l if t!='...')
    print(sum(c.values()),'signs',len(c),'types'); print(c.most_common())
    for k,l in L:
        print(k, ''.join(KEY.get(t,t if t=='...' else '<'+t+'>') for t in l))

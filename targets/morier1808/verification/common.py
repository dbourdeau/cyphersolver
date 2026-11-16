import re, math, collections
W='/Volumes/SPOF_2/Archives-Veille-cyber/dechiffrements-europe/morier-1808/work'
CORPUS='/Users/bdudout/Documents/Veille cyber/dechiffrements-europe/bunch-1862/dl/lyons_newton.txt'
def load_words(path):
    words=[]; cur=[]
    for line in open(path):
        if line.startswith(('#','@')): continue
        line=line.replace('[del]','X').replace('?','')
        for tok in re.findall(r'\d+|X|\.|,',line):
            if tok=='.':
                if cur: words.append(cur); cur=[]
            elif tok==',': pass
            else: cur.append(tok)
    if cur: words.append(cur)
    return words
def corpus_text():
    t=open(CORPUS,encoding='utf-8',errors='ignore').read()
    i=t.find('*** START'); j=t.find('*** END')
    t=t[i:j] if i>0 else t
    t=re.sub(r'[^a-z]+',' ',t.lower())
    return t
def ngram_model(n=4):
    t=corpus_text(); c=collections.Counter(t[i:i+n] for i in range(len(t)-n+1))
    tot=sum(c.values()); fl=math.log(0.01/tot)
    return {k:math.log(v/tot) for k,v in c.items()}, fl
def vocab():
    return collections.Counter(corpus_text().split())

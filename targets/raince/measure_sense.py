"""measure_sense.py READING [READING2 ...]: fraction of cipher letters read AS SENSE.
Reading lines: 'NN H|M|R | text' under '## p. 29/30/31/105' headings (trans/reading.txt format).
A letter counts only if its word is a period-French word (fr-1530-despatches corpus, u/v i/j folded)
or in NAMES, the word holds no '?', is not followed by '(?)', and the line is not M (machine).
Denominator per line = the machine's non-null letter count for that line (pred.json), or the
reading's own letter count if larger."""
import json,re,sys,collections
SP=r'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6161e4a6-ee3b-46d9-a1bc-b3f7895b5b9b/scratchpad/fr1530.txt'
def fold(w): return w.lower().replace('v','u').replace('j','i').replace('y','i')
try: LEX=set(json.load(open('lexicon.json')))
except FileNotFoundError:
    t=open(SP,encoding='utf8').read().lower()
    c=collections.Counter(fold(w) for w in re.findall(r"[a-zçéèàù]+",t))
    LEX=sorted(w for w,n in c.items() if n>=2 and (len(w)>1 or w in 'aoy'))
    json.dump(LEX,open('lexicon.json','w')); LEX=set(LEX)
NAMES={fold(x) for x in 'venise rome naples pietro anthonio capin cappin bourgoigne savoye doria castiliens admiral bourbon gennes florence medicis colonne sesse seuerin particularitez escripvise roy aragonoys bourguignoms haynoyers flamens vellacos veillacos borachos herrera lopes hortado mantoue hyer'.split()}
EXTRA={fold(x) for x in '''feust pouoit cler capin respondu besoingne imperiaulx peuent conme tention adherens destruict propoz castile conduict
seulx capituler dessusdictz recommandations monstrer esbay deca personnaige satisfaict plainct mesmement discour beaulx partiz
asseureroyent prouffict supediter dedict particularitez dessusdict vould avoi delib'''.split()}
LEX|=NAMES|{'con'}|EXTRA
p=json.load(open('pred.json'))
den={}
for k,v in p.items():
    pg,l,_=k.split('|'); den[(pg,int(l)+1)]=den.get((pg,int(l)+1),0)+(v!='_')
PG={'29':'f29r','30':'f30v','31':'f31r','105':'f105r'}
def joinfix(lines):
    # lines: list of [kind, words]; if last word of a line + first of next forms a lexicon word, mark both good
    pass
def run(fn):
    pg=None; tot=ok=0; prev_tail=None; prevpg=None; per=collections.defaultdict(lambda:[0,0])
    for ln in open(fn,encoding='utf8'):
        m=re.match(r'## p\. (\d+)',ln)
        if m: pg=PG[m.group(1)]; continue
        m=re.match(r'(\d\d) ([HMR]) \| (.*)',ln)
        if not m or not pg: continue
        L,kind,txt=int(m.group(1)),m.group(2),m.group(3)
        txt=txt.replace('(con)','con'); txt=re.sub(r'\[[^\]]*\]','[]',txt)
        words=re.findall(r"[^\s']+(?:\s*\(\?\))?",txt)
        if prev_tail and words and kind!='M':
            a=re.sub(r'[\[\]]','',prev_tail).lower(); b=re.sub(r'[\[\]]','',words[0]).lower()
            if a.isalpha() and b.isalpha() and fold(a+b) in LEX and fold(a) not in LEX: ok+=len(a); per[prevpg][0]+=len(a); joined=True
            else: joined=False
        else: joined=False
        letters=sum(len(re.sub(r'[^a-z?]','',w.split('(')[0].lower())) for w in words)
        good=0
        if kind!='M':
            for wi,w in enumerate(words):
                if wi==0 and joined: good+=len(re.sub(r'[\[\]]','',w)); continue
                if wi==len(words)-1 and w.isalpha() and fold(w) not in LEX: continue
                if '(?)' in w or '[' in w or ']' in w: continue
                core=re.sub(r'[\[\]]','',w).lower()
                if '?' in core or not core.isalpha(): continue
                if fold(core) in LEX: good+=len(core)
        d=max(den.get((pg,L),0),letters)
        tot+=d; ok+=good; per[pg][0]+=good; per[pg][1]+=d
        prev_tail=words[-1] if words and kind!='M' else None; prevpg=pg
    for k,(a,b) in per.items(): print(f'{k}: {a}/{b} = {a/b:.3f}')
    print(f'{fn}: sense {ok}/{tot} = {ok/tot:.3f}')
for f in sys.argv[1:]: run(f)

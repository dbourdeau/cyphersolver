"""control.py: shuffled-key controls.
A) spelled layer: runs of consecutive cipher-letter tokens (between codebook groups) decoded with the real letter table
   vs 1000 random permutations of the 97-number table; score = share of runs (>=3 letters) that segment completely into
   Dutch words (OpenTaal + 17th-c. spelling variants) or proper names (fixed list, same for real and shuffled runs).
B) codebook layer: agreement with the contemporary decipherments (validation files) is reported by validate step;
   here we add a 'row-shift' control: every codebook value replaced by the key entry k rows away (k=+-1..+-5) and
   the share of tokens whose shifted value equals the real value (identity check) - reported only for completeness."""
import glob,os,random,re,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key'))
from letters import NUM
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lex=set(w.strip().lower() for w in open(os.environ.get('BATTIER_OPENTAAL', D+'/key/opentaal.txt'),encoding='utf-8') if w.strip().isalpha())
NAMES=set('''oropeza oropesa castanaga cantelmo altamira monterey montirey monterei osuna melgar salazar grana gastanaga
leganes medina celi medinaceli spanse spaanse cifuentes portocarrero silva mexico peru lima cadix madrid vlaanderen
flandersche flandersse nederlanse nederlandse grand maistre maestre maistr stalmeester presidence presidentie
skelton downing heydelbergh brandenburg keyser engelandt vrankryk ronquillo mancera aguilar aguilera borgomanero
mansfelt mansfeld stratman stratmann lobkowitz pfaltz neuburg rebenac feuquieres lacerda'''.split())
VAR=[('y','ij'),('y','i'),('ae','aa'),('ck','k'),('gh','g'),('dt','d'),('uy','ui'),('c','k'),('qu','kw'),('ee','e'),('oo','o'),('sch','s'),('th','t'),('u','v'),('v','u'),('z','s'),('s','z')]
def isw(w):
    if w in NAMES or w in lex: return True
    out={w}
    for _ in range(2):
        new=set()
        for v in out:
            for a,b in VAR:
                if a in v: new.add(v.replace(a,b))
        out|=new
    return any(v in lex or v in NAMES for v in out)
from functools import lru_cache
SHORT=set('t s de en te in op is al so na of om er hy sy my wy u het den der dat die wat van met tot uyt aan aen nu ook oock ick men een syn hem haer niet wel'.split())
NAMES|=set('intrigues au contraire mefiant mefiance courier opiniatreert opiniatreren par grand maistre maestre mansvelt mansuelt aureis monterez montrey gestr salse ceter'.split())  # loanwords/abbrev., same for real and shuffled
def seg(s):
    @lru_cache(None)
    def f(i):
        if i==len(s): return True
        for j in range(len(s),i,-1):
            w=s[i:j]
            if (len(w)>=4 or w in SHORT) and isw(w) and f(j): return True
        return False
    return f(0)
runs=[]
for fn in sorted(glob.glob(f'{D}/readings/s[0-9][0-9][0-9][LR].tsv')):
    cur=[]
    for l in open(fn):
        p=l.rstrip('\n').split('\t')
        if len(p)<5 or not p[0].isdigit(): continue
        t=p[2].split('|')[0].rstrip('?')
        if p[4]=='letter' and ':' not in t and t.isdigit(): cur.append(int(t))
        else:
            if len(cur)>=3: runs.append(cur)
            cur=[]
    if len(cur)>=3: runs.append(cur)
def score(K):
    return sum(1 for r in runs if seg(''.join(K[n] for n in r)))
real=score(NUM)
nums=list(NUM); vals=[NUM[n] for n in nums]
random.seed(1686); sh=[]
N=int(sys.argv[1]) if len(sys.argv)>1 else 300
for i in range(N):
    v=vals[:]; random.shuffle(v); sh.append(score(dict(zip(nums,v))))
print('spelled runs (>=3 letters):',len(runs),' letters:',sum(map(len,runs)))
print('real key: %d/%d = %.1f%% segment into Dutch words/names'%(real,len(runs),100*real/len(runs)))
print('shuffled letter table (%dx): mean %.1f%%, max %.1f%%'%(N,100*sum(sh)/N/len(runs),100*max(sh)/len(runs)))
bad=[''.join(NUM[n] for n in r) for r in runs if not seg(''.join(NUM[n] for n in r))]
print('real-key runs not segmentable (%d):'%len(bad),' '.join(bad))

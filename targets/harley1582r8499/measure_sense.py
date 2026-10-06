# measure_sense.py: honest sense measure on a final_vN.txt reading.
# T = non-null cipher signs per line (tokens left of '||', clear text in [..] removed, '.' ':' and key nulls skipped).
# unread = [?n]; tentative = {w:n}; nonsense = signs whose reading is read letter-for-letter but does not make sense,
# judged per line in sense_judgement.tsv (line<TAB>signs<TAB>which words). Sense-read = T - unread - tentative - nonsense.
import re,sys
from pathlib import Path
here=Path(__file__).parent
NULLS={'3','-2','r','q=','9','ft','xo','rho','d+','0','th','3r','tl','XX','t~','CURL_D','CURL_D_BAR','X_HOOK','NULL_DAG','NULL_LOOP','NULL_LOOP_BAR','e','3=','r.'}
src=sys.argv[1] if len(sys.argv)>1 else 'final_v8.txt'
jud=sys.argv[2] if len(sys.argv)>2 else 'sense_judgement.tsv'
J={}
if (here/jud).exists():
  for L in open(here/jud,encoding='utf8'):
    if L.strip() and not L.startswith('#'):
      a=L.rstrip('\n').split('\t'); J[a[0]]=int(a[1])
pages={}
for L in open(here/src,encoding='utf8'):
  m=re.match(r'(p\d\.\d\d) \| (.*?) \|\| (.*)',L)
  if not m: continue
  ln,tok,rd=m.groups()
  toks=re.sub(r'\[[^\]]*\]',' ',tok).replace('(q)','Q').split()
  t=sum(1 for x in toks if x not in('.',':') and x not in NULLS)
  u=sum(map(int,re.findall(r'\[\?(\d+)\]',rd)))
  v=sum(map(int,re.findall(r'\{[^}:]*:(\d+)\}',rd)))
  n=J.get(ln,0)
  P=pages.setdefault(ln[:2],[0,0,0,0])
  for i,x in enumerate((t,u,v,n)): P[i]+=x
  if '-v' in sys.argv: print(ln,t,u,v,n)
S=[0,0,0,0]
for p,(t,u,v,n) in sorted(pages.items()):
  print(f'{p}: {t} signs; old measure (non-[?], non-tentative) {100*(t-u-v)/t:.1f}%; sense {t-u-v-n} = {100*(t-u-v-n)/t:.1f}%')
  S=[a+b for a,b in zip(S,(t,u,v,n))]
t,u,v,n=S
print(f'ALL: {t} signs; unread {u}, tentative {v}, nonsense {n}; old measure {100*(t-u-v)/t:.1f}%; SENSE {100*(t-u-v-n)/t:.1f}%')

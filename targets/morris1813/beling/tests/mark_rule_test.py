"""Test: n lower strokes withdraw n letters from the end of the key value. Uses the frozen proposal ledger."""
import csv,json,re,random,collections
K={int(e['code']):(e['historical_reading'] or '') for e in json.load(open('sources/raw/historical1385_review_2026-10-27/historical1385_reference.json'))['entries']}
mp=lambda m:100*(15-(m-1)//100)+(m-100*((m-1)//100))
norm=lambda s:re.sub(r'[^a-z]','',s.lower()).replace('v','u').replace('j','i')
rows=[]
for r in csv.DictReader(open('sources/raw/morris_proposal_opening_completion_2026-10-24/complete_129_row_alignment.csv')):
    if r['status']!='high' or r['tier']!='A':continue
    if re.search(r'[\[\?]',r['raw']):continue
    t=re.findall(r'(\d{1,4})(\{[^}]*\})?',r['raw'])
    if t and all(1<=int(a)<=1600 for a,_ in t):rows.append(([(int(a),b.strip('{}')) for a,b in t],norm(r['plaintext']),r['source_record']))
print('rows',len(rows))
N={'low':1,'2low':2,'3low':3}
def build(t,f):
    return ''.join(f(norm(K[mp(n)]),m) for n,m in t)
def plain(v,m):return v
def rule(v,m):
    k=N.get(m,0);return v[:-k] if k and len(v)>k else v
def wrong(v,m):
    k=N.get(m,0);return v[k:] if k else v      # withdraw from the front instead
def plus(v,m):
    k=N.get(m,0);return v[:-(k+1)] if k and len(v)>k+1 else v  # one letter too many
def minus(v,m):
    k=N.get(m,0);return v[:-(k-1)] if k>1 else v
# only rows containing strokes of 2 or 3: unambiguous
st=[r for r in rows if any(m in('2low','3low') for _,m in r[0])]
one=[r for r in rows if any(m=='low' for _,m in r[0]) and not any(m in('2low','3low') for _,m in r[0])]
def score(rs,f):return sum(build(t,f)==p or build(t,f)+'s'==p or build(t,f)+'ed'==p or build(t,f)+'d'==p for t,p,_ in rs)
for nm,rs in [('rows with 2 or 3 strokes',st),('rows with 1 low mark',one),('rows with no mark',[r for r in rows if all(m=='' or m in('<','^') for _,m in r[0])])]:
    print(nm,len(rs),'no rule',score(rs,plain),'count-from-end',score(rs,rule),'from front',score(rs,wrong),'one too many',score(rs,plus),'one too few',score(rs,minus))
print('hits 2-3 strokes:',[(p,[(K[mp(n)],m) for n,m in t]) for t,p,_ in st if build(t,rule) in (p,p[:-1],p[:-2])][:24])
print('misses 2-3 strokes:',[(p,[(n,K[mp(n)],m) for n,m in t]) for t,p,_ in st if build(t,rule) not in (p,p[:-1],p[:-2])][:16])
# low: withdraw vs double
def dbl(v,m):return v+v[-1] if m=='low' and v else v
def wd(v,m):return v[:-1] if m=='low' and len(v)>1 else v
print('1 mark: withdraw',score(one,wd),'double',score(one,dbl),'either',sum(any(build(t,f) in (p,p[:-1],p[:-2]) for f in (wd,dbl)) for t,p,_ in one),'none',score(one,plain))

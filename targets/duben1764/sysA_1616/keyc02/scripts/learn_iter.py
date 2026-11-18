"""Propose key additions/corrections from alignment output (al.json) of training letters.
Rule (written before use, 17 Nov): unknown group -> value v if v is emitted at >=2 anchored occurrences and is the
majority of anchored occurrences, or at 1 anchored occurrence and >=2 occurrences in all with v, and v non-empty.
Known group -> corrected to v if err occurrences >= 2*ok occurrences and v is the anchored majority with >=2 anchored."""
import json,sys,collections
R=json.load(open(sys.argv[1])); K=json.load(open(sys.argv[2]))
unk=collections.defaultdict(list); err=collections.defaultdict(list); ok=collections.Counter()
for k,r in enumerate(R):
    prev=R[k-1] if k>0 and R[k-1]['src']==r['src'] else None
    nxt=R[k+1] if k+1<len(R) and R[k+1]['src']==r['src'] else None
    anch=bool(prev and prev['type']==1 and prev['known']) and bool(nxt and nxt['type']==1 and nxt['known'])
    if r['known'] is None: unk[r['g']].append((r['emit'],anch))
    elif r['type']==2: err[r['g']].append((r['emit'],anch))
    else: ok[r['g']]+=1
new={}; why={}
for g,l in unk.items():
    a=collections.Counter(e for e,x in l if x and e); al=collections.Counter(e for e,x in l if e)
    if not a: continue
    v,c=a.most_common(1)[0]
    if (c>=2 and c>sum(a.values())/2) or (c==1 and al[v]>=2):
        new[g]=v; why[g]=f'new: anchored {c}/{sum(a.values())}, all {al[v]}/{len(l)}'
for g,l in err.items():
    a=collections.Counter(e for e,x in l if x)
    if not a: continue
    v,c=a.most_common(1)[0]
    if len(l)>=2*max(ok[g],1) and c>=2 and c>sum(a.values())/2:
        new[g]=v; why[g]=f'corr: {K[g][0]!r}->{v!r}, err {len(l)} ok {ok[g]}, anchored {c}'
K2=dict(K)
for g,v in new.items(): K2[g]=[v]
json.dump(K2,open(sys.argv[3],'w'),ensure_ascii=False,indent=0,sort_keys=True)
for g in sorted(new,key=int): print(g,why[g])
print(len(new),'changes',file=sys.stderr)

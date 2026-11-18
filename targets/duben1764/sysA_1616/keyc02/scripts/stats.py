import json,sys,collections
R=json.load(open(sys.argv[1]))
unk=collections.defaultdict(list); err=collections.defaultdict(list); ok=collections.Counter()
for k,r in enumerate(R):
    prev=R[k-1] if k>0 and R[k-1]['src']==r['src'] else None
    nxt=R[k+1] if k+1<len(R) and R[k+1]['src']==r['src'] else None
    anch=(prev is not None and prev['type']==1 and prev['known']) and (nxt is not None and nxt['type']==1 and nxt['known'])
    if r['known'] is None: unk[r['g']].append((r['emit'],anch,r['src'][0]+':'+r['lab']))
    elif r['type']==2: err[r['g']].append((r['emit'],anch,r['src'][0]+':'+r['lab']))
    else: ok[r['g']]+=1
print('UNKNOWN groups',len(unk))
for g,l in sorted(unk.items(),key=lambda x:-len(x[1])):
    c=collections.Counter(e for e,a,s in l if a); c2=collections.Counter(e for e,a,s in l)
    print(g,len(l),'anch:',dict(c.most_common(4)),'all:',dict(c2.most_common(4)))
print('\nKNOWN with errors (err/ok)')
K={k:(v[0] if v else '') for k,v in json.load(open(sys.argv[2])).items()}
for g,l in sorted(err.items(),key=lambda x:-len(x[1])):
    if len(l)>=2 or len(l)>ok[g]:
        c=collections.Counter(e for e,a,s in l if a)
        print(g,repr(K[g]),'err',len(l),'ok',ok[g],'anch:',dict(c.most_common(4)),'all:',dict(collections.Counter(e for e,a,s in l).most_common(3)))

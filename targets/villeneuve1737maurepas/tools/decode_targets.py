import sys,json,re
sys.path.insert(0,sys.argv[1]); from vlib import *
D=sys.argv[2]
K={};ST={}
for l in open(D+"/key/KEY-K2-frozen.tsv").read().split('\n')[1:]:
    if not l: continue
    c,v,n,a,cu,st=l.split('\t'); K[c]='' if v=='-' else v; ST[c]=st
M=json.load(open(f"{T}/merged_cipher.json"))
A=parse(f"{T}/passA_targets.txt")
for pg in sys.argv[3].split(','):
    print('#',pg)
    for no,k,p in A[pg]:
        if k=='T': print(f"L{no:02d} T: {p}"); continue
        if k!='C': continue
        toks=[(t,s) for (l,t,s) in M[pg] if l==no]
        # rebuild with clear words in order from pass A
        out=[]; it=iter(toks)
        merged=[]
        for x in p:
            if x.startswith('«'): merged.append(('CLR',x))
            elif x=='[G]': merged.append(('GAP','[G]'))
        # positions of clear in A line relative to cipher groups
        ci=0; seq=[]
        nA=[x for x in p if not x.startswith('«') and x!='[G]']
        # map: walk A tokens; replace cipher tokens by merged tokens sequentially (counts may differ slightly)
        mt=list(toks); mi=0
        for x in p:
            if x.startswith('«'): seq.append(x)
            elif x=='[G]': seq.append('[G]')
            else:
                if mi<len(mt): t,s=mt[mi]; mi+=1; c=cc(t); v=K.get(c)
                else: continue
                flag='' if (ST.get(c)=='S' and s in('agree','arb-sure')) else '?'
                seq.append(f"{v if v else ('·' if v=='' else '*'+c)}{flag}")
        while mi<len(mt):
            t,s=mt[mi]; mi+=1; c=cc(t); v=K.get(c); seq.append(f"{v if v else ('·' if v=='' else '*'+c)}?")
        print(f"L{no:02d}: "+' '.join(seq))

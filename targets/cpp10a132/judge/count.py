import csv,re
EXP={'p75r':100,'p76r':609,'p76v':428}
tot={p:[0,0,0] for p in EXP}; ok=True
for r in csv.DictReader(open('/tmp/judge_cpp/judge.tsv',encoding='utf-8'),delimiter='\t'):
    s,e,n=int(r['S']),int(r['E']),int(r['N'])
    letters=len(re.sub(r'[^a-z]','',re.sub(r'\{[^}]*\}','',r['decoded'])))
    if s+e+n!=letters: ok=False; print('line mismatch',r['page'],r['line'],s+e+n,letters)
    for i,v in enumerate((s,e,n)): tot[r['page']][i]+=v
pct=lambda s,e,n:100*s/(s+e+n)
for p,(s,e,n) in tot.items():
    print(f"{p}: S {s} E {e} N {n} = {s+e+n} (expected {EXP[p]}, {'OK' if s+e+n==EXP[p] else 'MISMATCH'})  read {s}/{s+e+n} = {pct(s,e,n):.1f}%")
    ok&= s+e+n==EXP[p]
S,E,N=[sum(t[i] for t in tot.values()) for i in range(3)]
print(f"held-out p76v: {pct(*tot['p76v']):.1f}%")
print(f"full: S {S} E {E} N {N} = {S+E+N} (expected 1137) read {S}/{S+E+N} = {pct(S,E,N):.1f}%  line 65%: {'PASS' if pct(S,E,N)>=65 else 'FAIL'}")
print('letter totals:', 'all match' if ok and S+E+N==1137 else 'MISMATCH')

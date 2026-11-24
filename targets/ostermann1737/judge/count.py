import sys,collections
d=collections.defaultdict(lambda:[0,0,0,0])
for i,l in enumerate(open('/tmp/judge_ost/judge.tsv',encoding='utf-8')):
    if i==0: continue
    f=l.rstrip('\n').split('\t'); n=int(f[0]); L,S,E,N=map(int,f[2:6])
    assert S+E+N==L,(l)
    for k,v in enumerate((L,S,E,N)): d[n][k]+=v
def p(lab,a): L,S,E,N=a; print(f"{lab}\tletters={L}\tS={S}\tE={E}\tN={N}\tS%={100*S/(S+E+N):.1f}\t{'PASS' if S/(S+E+N)>=.65 else 'FAIL'}")
for n in sorted(d): p(f"line {n}",d[n])
agg=lambda r:[sum(d[n][k] for n in r) for k in range(4)]
tr,ho,al=agg(range(1,17)),agg(range(17,21)),agg(range(1,21))
p("train 1-16",tr);p("held-out 17-20",ho);p("total 1-20",al)
print("letter check:",al[0],"vs brief 770:",'OK' if al[0]==770 else 'MISMATCH', "| train",tr[0],"vs 622 | held-out",ho[0],"vs 148")

import csv,sys
rows=list(csv.DictReader(open(sys.argv[1] if len(sys.argv)>1 else '/tmp/judge_erc/judge.tsv'),delimiter='\t'))
def f(rs,label):
    S=sum(int(r['S']) for r in rs);E=sum(int(r['E']) for r in rs);N=sum(int(r['N']) for r in rs);T=S+E+N
    print(f"{label}: S={S} E={E} N={N} letters={T} S/letters={S}/{T}={100*S/T:.1f}% {'PASS' if S/T>=0.65 else 'FAIL'}")
for r in rows: f([r],'line '+r['line'])
f([r for r in rows if r['line'] in ('1','2','3','4','5','6')],'build 1-6')
f([r for r in rows if r['line'] in ('7','8')],'held-out 7-8')
f(rows,'total')

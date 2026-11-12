"""ledger74.py -- strict S/E/N for the b74 blind decode (K3 unchanged). python3 -I, stdlib only.
Rules: PARSER.md s5 marks from dec.py (X excluded; ILL=N; CODE/UNK/doubt=E), then downgrades S->E only:
 D1 lookup token differs from b70 pass C and was not adjudicated in favour of b74 (value unverified or wrong);
 D2 same lookup token as b70, and b70 LEDGER_K3 downgraded that unit for a reading reason (emended / not read) -- same token, same defect;
 Catchword 35r.L21 (2 units, repeated at 35v.L1) is outside the denominators, as in b70. Nothing is upgraded."""
import csv,collections
B='/home/claude/en/trackB/b74_selvatico_blind/'
adj={r['n']:r['verdict'] for r in csv.DictReader(open(B+'dec/ADJUDICATION.tsv',encoding='utf-8'),delimiter='\t')}
dis={(r['mine_line'],r['mine_idx']):adj[r['n']] for r in csv.DictReader(open(B+'dec/DISAGREE.tsv',encoding='utf-8'),delimiter='\t')}
AUTO={'code','unkeyed','transcription doubt','struck by writer','illegible',''}
out=open(B+'LEDGER_b74.tsv','w',encoding='utf-8'); out.write('letter\tline\tidx\traw\tvalue\tparser_mark\tmark\treason\n')
T=collections.defaultdict(collections.Counter); T2=collections.defaultdict(collections.Counter); why=collections.Counter()
for r in csv.DictReader(open(B+'dec/ALIGN.tsv',encoding='utf-8'),delimiter='\t'):
    if r['op']=='b70_only': continue
    let=r['letter']; pm=r['mine_mark']; m=pm; reason=''
    if r['mine_line']=='35r.L21': m='CW'; reason='catchword, repeated at 35v.L1: outside denominators'
    elif pm=='X': reason='struck'
    elif pm=='N': reason='illegible'
    elif pm=='E': reason='parser: code/unkeyed/doubt'
    elif r['canon_same']=='0':
        v=dis.get((r['mine_line'],r['mine_idx']))
        if v=='b74': reason='differs from b70; adjudicated for b74'
        else: m='E'; reason='D1 lookup differs from b70 ('+(v or 'b70 unit not S; not adjudicated')+')'
    elif r['b70_mark']=='E' and r['b70_reason'] not in AUTO:
        m='E'; reason='D2 b70 reading downgrade: '+r['b70_reason']
    T[let][m]+=1; why[reason.split(':')[0].split(' (')[0]]+=1
    m2=m
    if pm=='E' and '=' in r['mine_val'] and '?' not in r['mine_raw'] and r['mine_val'].startswith('{'): m2='S'
    T2[let][m2]+=1
    out.write('\t'.join([let,r['mine_line'],r['mine_idx'],r['mine_raw'],r['mine_val'],pm,m,reason])+'\n')
out.close()
tot=collections.Counter(); tot2=collections.Counter()
def show(n,c,c2):
    d=c['S']+c['E']+c['N']
    print(f"{n}: S {c['S']} + E {c['E']} + N {c['N']} = {d}; STRICT {c['S']}/{d} = {100*c['S']/d:.2f}% | outside: struck {c['X']}, catchword {c['CW']} | labelled 2nd figure, codes with a K3 value counted S: {c2['S']}/{d} = {100*c2['S']/d:.2f}%")
for let in ['10Jun','29Jul','08Aug','12Aug']: show(let,T[let],T2[let]); tot+=T[let]; tot2+=T2[let]
show('POOLED',tot,tot2)
print('pooled S check:',' + '.join(str(T[l]['S']) for l in ['10Jun','29Jul','08Aug','12Aug']),'=',tot['S'])
print('reasons:',dict(why))

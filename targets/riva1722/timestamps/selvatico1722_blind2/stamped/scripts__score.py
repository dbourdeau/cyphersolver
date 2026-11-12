"""score.py -- b74. Aligns blind units (dec/units_*.tsv from scripts/dec.py) with b70 LEDGER_K3.tsv rows, per letter (difflib over the whole letter, canonical tokens).
python3 -I, stdlib only. Writes dec/ALIGN.tsv and dec/DISAGREE.tsv; prints all arithmetic."""
import csv,difflib,collections,re,sys
B74='/home/claude/en/trackB/b74_selvatico_blind/'
LED='/home/claude/en/trackB/b70_selvatico_read/LEDGER_K3.tsv'
LET=[('10Jun','L1_10jun'),('29Jul','L2_29jul'),('08Aug','L3_08aug'),('12Aug','L4_12aug')]
def tok(r):
    if r['class']=='X': return '[x]'
    if r['class']=='ILL': return '#'
    return r['canon']
def full(r):
    if r['class'] in('X','ILL'): return tok(r)
    raw=re.sub(r'\[[^\]]*\]','',r['raw'])
    return r['canon']+("'" if "'" in raw else '')+''.join(re.findall(r'\^\d',raw))
led=list(csv.DictReader(open(LED,encoding='utf-8'),delimiter='\t'))
al=open(B74+'dec/ALIGN.tsv','w',encoding='utf-8'); al.write('letter\top\tmine_line\tmine_idx\tmine_raw\tmine_val\tmine_mark\tb70_line\tb70_idx\tb70_raw\tb70_val\tb70_mark\tb70_reason\tcanon_same\tfull_same\n')
tot=collections.Counter(); summ=[]
for let,fn in LET:
    A=list(csv.DictReader(open(B74+'dec/units_%s.tsv'%fn,encoding='utf-8'),delimiter='\t'))
    B=[r for r in led if r['letter']==let]
    sm=difflib.SequenceMatcher(None,[tok(r) for r in A],[tok(r) for r in B],autojunk=False)
    c=collections.Counter()
    def w(op,a,b):
        cs= a is not None and b is not None and tok(a)==tok(b)
        fs= cs and full(a)==full(b)
        c['cols']+=1
        if a is not None and b is not None:
            c['paired']+=1; c['canon_same']+=cs; c['full_same']+=fs
            if b['mark']=='S': c['b70S_paired']+=1; c['b70S_canon_same']+=cs; c['b70S_full_same']+=fs
        elif a is not None: c['mine_only']+=1
        else:
            c['b70_only']+=1
            if b['mark']=='S': c['b70S_unpaired']+=1
        al.write('\t'.join([let,op]+([a['line'],a['idx'],a['raw'],a['value'],a['mark']] if a else ['','','','',''])+([b['line'],b['idx'],b['raw'],b['value'],b['mark'],b['reason']] if b else ['','','','','',''])+[str(int(cs)),str(int(fs))])+'\n')
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':
            for k in range(i2-i1): w('equal',A[i1+k],B[j1+k])
        else:
            n=min(i2-i1,j2-j1)
            for k in range(n): w('differ',A[i1+k],B[j1+k])
            for k in range(i1+n,i2): w('mine_only',A[k],None)
            for k in range(j1+n,j2): w('b70_only',None,B[k])
    c['mine']=len(A); c['b70']=len(B); summ.append((let,c)); tot+=c
def show(n,c):
    assert c['cols']==c['paired']+c['mine_only']+c['b70_only']
    print(f"{n}: my units {c['mine']}, b70 units {c['b70']}; alignment columns = paired {c['paired']} + mine-only {c['mine_only']} + b70-only {c['b70_only']} = {c['cols']}")
    print(f"   lookup-token agreement (digits+underline) = {c['canon_same']}/{c['cols']} = {100*c['canon_same']/c['cols']:.2f}%   [of paired: {c['canon_same']}/{c['paired']} = {100*c['canon_same']/c['paired']:.2f}%]")
    print(f"   full-token agreement (also ' and ^n; ? ignored) = {c['full_same']}/{c['cols']} = {100*c['full_same']/c['cols']:.2f}%")
    d=c['b70S_paired']+c['b70S_unpaired']
    print(f"   b70 S units {d} = paired {c['b70S_paired']} + unpaired {c['b70S_unpaired']}; same lookup token {c['b70S_canon_same']}/{d} = {100*c['b70S_canon_same']/d:.2f}%; lookup disagreements with a b70 S unit = {d-c['b70S_canon_same']}")
for n,c in summ: show(n,c)
show('POOLED',tot)
print('pooled check: canon_same',' + '.join(str(c['canon_same']) for n,c in summ),'=',tot['canon_same'],'; cols',' + '.join(str(c['cols']) for n,c in summ),'=',tot['cols'])
al.close()
# disagreement list
rows=list(csv.DictReader(open(B74+'dec/ALIGN.tsv',encoding='utf-8'),delimiter='\t'))
out=open(B74+'dec/DISAGREE.tsv','w',encoding='utf-8'); out.write('n\tletter\tkind\tmine_line\tmine_idx\tmine_raw\tmine_val\tmine_mark\tb70_line\tb70_idx\tb70_raw\tb70_val\tb70_mark\tb70_reason\n')
n=0; kinds=collections.Counter()
for r in rows:
    if r['b70_mark']!='S' : continue
    if r['full_same']=='1': continue
    kind='LOOKUP' if r['canon_same']=='0' else 'MARK_ONLY'
    if r['op']=='b70_only': kind='MISSING_IN_MINE'
    n+=1; kinds[kind]+=1
    out.write('\t'.join([str(n),r['letter'],kind]+[r[k] for k in ['mine_line','mine_idx','mine_raw','mine_val','mine_mark','b70_line','b70_idx','b70_raw','b70_val','b70_mark','b70_reason']])+'\n')
out.close(); print('disagreements with a b70 S unit:',n,dict(kinds))

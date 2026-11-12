# contract.py -- executable evidence contract for Augustoni 9 Oct 1612 (Estense Campori, Augustoni c.1r)
# Run: python3 -I scripts/contract.py   (from any cwd; paths absolute)
# Inputs (contract/): KEY.tsv, ALIASES.tsv, OVERRIDES.tsv, WORDS.tsv ; frozen R2: b55 tx/aug_R2.txt (md5 88b10684...)
# Outputs (out/): LEDGER_units.tsv, COUNTS.txt, DECODE_consensus.txt, DIFF_vs_b55_consensus.txt, DIFF_vs_b55_marks.tsv, CHECKS.txt
import re, difflib, hashlib, collections
B='/home/claude/en/trackB/b72_augustoni_repair/'
R2TX='/home/claude/en/trackB/b55_augustoni_cpp/tx/aug_R2.txt'
B55CONS='/home/claude/en/trackB/b55_augustoni_cpp/tx/aug_consensus_plaintext.txt'
B55MARKS='/home/claude/en/trackB/b55_augustoni_cpp/work/R2_marks.tsv'
CODES={'I.','PP.','25.'}
checks=[]
def chk(name,ok,detail=''):
    checks.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    return ok
def tsv(p):
    L=[l.rstrip('\n').split('\t') for l in open(p,encoding='utf-8') if l.strip()]
    h=L[0]; return [dict(zip(h,r)) for r in L[1:]]

# ---------- tokenizer ----------
def tokenize(word):
    """A word is either a single code token (I. PP. 25.), '-' (no word), or a sequence of one-character sign labels.
    '&' = abbreviation compound (one unit); '?' = illegible/blotted sign (one unit); 'υ' rounded n-form; 'Z' hapax Z-form."""
    if word in CODES: return [word]
    if word=='-': return []
    return list(word)

# ---------- load contract ----------
KEY={r['sign']:r['plain'] for r in tsv(B+'contract/KEY.tsv')}
ALIAS=collections.defaultdict(dict); ALIAS_SCOPE={}
for r in tsv(B+'contract/ALIASES.tsv'):
    ALIAS[r['transcript']][r['label']]=r['key_label']
OVR={(r['line'],int(r['widx']),int(r['tidx'])):r for r in tsv(B+'contract/OVERRIDES.tsv')}
WORDS=tsv(B+'contract/WORDS.tsv')

def literal(transcript,label):
    """Key decode of one label with the transcript's label aliases. No overrides. None = no key value."""
    if label in CODES or label in ('&','?'): return None
    lab=ALIAS[transcript].get(label,label)
    return KEY.get(lab)

def decode_cons(line,widx,tidx,label):
    """THE decoder: override if one exists for this coordinate, else literal. Returns (value, source)."""
    o=OVR.get((line,widx,tidx))
    if o is not None:
        if o['label']!=label: raise SystemExit(f"OVERRIDE label mismatch at {line}/{widx}/{tidx}: {o['label']} vs {label}")
        return (o['value'] if o['value']!='?' else None), 'OVR'
    if label in CODES or label=='&': return None,'CODE'
    return literal('CONS',label),'LIT'

def parse_accepted(acc,ntok,istoken):
    """accepted -> per-token values (insertions {..} removed) + list of insertions."""
    if istoken: return [acc],[]
    ins=re.findall(r'\{([^}]*)\}',acc)   # writer omissions (emendations) -> conservative variant
    bare=re.sub(r'<[^>]*>','',re.sub(r'\{[^}]*\}','',acc))   # <..> = torn-edge restorations: no unit, no penalty
    if len(bare)!=ntok: raise SystemExit(f"accepted length {len(bare)} != tokens {ntok}: {acc}")
    return list(bare),ins
uv=lambda s: s.replace('v','u') if s else s

# ---------- ledger ----------
units=[]
for w in WORDS:
    line,widx=w['line'],int(w['widx'])
    ct=tokenize(w['consword']); rt=tokenize(w['r2word'])
    if ct:
        vals,ins=parse_accepted(w['accepted'],len(ct),w['consword'] in CODES or w['consword']=='&')
    else: vals,ins=[],[]
    # consensus units
    cons=[]
    for t,lab in enumerate(ct):
        o=OVR.get((line,widx,t))
        cat=(o['category'] if o else ('CODE' if lab in CODES else 'ABBR' if lab=='&' else 'CIPHER'))
        val,src=decode_cons(line,widx,t,lab)
        acc=vals[t]
        lit=literal('CONS',lab)
        if acc=='?' or (o and o['status']=='N'): st='N'; why='no accepted value' if acc=='?' else 'override marks unresolved'
        elif cat in ('CODE','ABBR','CLEAR'): st='E'; why=cat
        elif o: st='E'; why='override: '+o['reason']
        elif uv(lit)==uv(acc): st='S'; why='literal key'
        else: st='MISMATCH'; why=f'literal {lit} != accepted {acc}'
        # conservative variant: words needing an inserted letter are wholly E
        st_c = 'E' if (ins and st=='S') else st
        cons.append(dict(line=line,widx=widx,tidx=t,label=lab,cat=cat,lit=lit,val=val,acc=acc,st=st,st_c=st_c,why=why,ins=''.join(ins),r2lab='',r2lit='',r2st='',r2st_c='',r2why=''))
    # R2 alignment
    amap=list(range(len(rt))) if w['r2align']=='=' else [None if a=='-' else int(a) for a in w['r2align'].split(',')]
    if not chk(f'align length {line}/{widx}',len(amap)==len(rt),f'{len(amap)} vs {len(rt)}'): raise SystemExit
    covered=set()
    r2units=[]
    for i,lab in enumerate(rt):
        ci=amap[i]
        rl=None if lab in CODES or lab in ('&','?') else literal('R2',lab)
        if ci is None:
            r2units.append(dict(line=line,widx=widx,tidx=f'r{i}',label='-',cat='CIPHER',lit='',val='',acc='',st='',st_c='',why='',ins='',
                                r2lab=lab,r2lit=rl,r2st='N',r2st_c='N',r2why='R2 spurious unit (no consensus sign)'))
            continue
        covered.add(ci); c=cons[ci]
        c['r2lab']=lab; c['r2lit']=rl
        if c['st']=='N': s,why='N','consensus unresolved'
        elif c['st']=='E': s,why='E','consensus value is override/code/clear'
        elif uv(rl)==uv(c['acc']): s,why='S','R2 literal key (+R2 aliases) = accepted'
        else: s,why='E',f'R2 literal {rl} != accepted {c["acc"]} (corrected in adjudication)'
        c['r2st']=s; c['r2why']=why; c['r2st_c']=('E' if (s=='S' and c['ins']) else s)
    for ci,c in enumerate(cons):
        if ci not in covered and rt:
            c['r2lab']='-'; c['r2st']='OMIT'; c['r2st_c']='OMIT'; c['r2why']='consensus unit not transcribed by R2'
    units += cons + r2units
chk('no MISMATCH units',all(u['st']!='MISMATCH' for u in units),str([ (u['line'],u['widx'],u['tidx']) for u in units if u['st']=='MISMATCH']))

# ---------- tie WORDS.r2word to the frozen R2 file ----------
md5=hashlib.md5(open(R2TX,'rb').read()).hexdigest()
chk('R2 file md5 = frozen 88b10684...',md5.startswith('88b1068458038758685f7ed6ee6f98cc'),md5)
r2file=[]
for l in open(R2TX,encoding='utf-8'):
    if l.startswith('#') or '|' not in l: continue
    lab=l.split('|')[0].strip(); ws=l.split('|',1)[1].split('||')[0].split()
    r2file += [(lab,x) for x in ws]
r2words=[(w['line'],w['r2word']) for w in WORDS if w['r2word'] not in CODES]
chk('WORDS.r2word sequence == frozen R2 cipher words (codes excluded)',r2file==r2words,f'{len(r2file)} vs {len(r2words)}')

# ---------- write ledger ----------
F=['line','widx','tidx','cat','label','lit','val','acc','ins','st','st_c','why','r2lab','r2lit','r2st','r2st_c','r2why']
with open(B+'out/LEDGER_units.tsv','w',encoding='utf-8') as f:
    f.write('\t'.join(F)+'\n')
    for u in units: f.write('\t'.join(str(u[k]) if u[k] is not None else '' for k in F)+'\n')

# ---------- counts with full arithmetic ----------
order=[]; [order.append(w['line']) for w in WORDS if w['line'] not in order]
def table(sel,key,label):
    out=[f'== {label}','line   S   E   N  (OMIT) | cum S  cum E  cum N']
    cS=cE=cN=cO=0
    for ln in order:
        us=[u for u in sel if u['line']==ln]
        c=collections.Counter(u[key] for u in us)
        cS+=c['S']; cE+=c['E']; cN+=c['N']; cO+=c['OMIT']
        out.append(f"{ln:5} {c['S']:3} {c['E']:3} {c['N']:3}  ({c['OMIT']})  | {cS:5} {cE:6} {cN:6}")
    T=cS+cE+cN
    out.append(f'TOTAL units T = S + E + N = {cS} + {cE} + {cN} = {T}' + (f'   [R2 omissions not in T: {cO}]' if cO else ''))
    if T: out.append(f'strict S/T = {cS}/{T} = {100*cS/T:.2f}% ; assisted (S+E)/T = {cS+cE}/{T} = {100*(cS+cE)/T:.2f}%')
    if cO:
        T2=T+cO
        out.append(f'reference basis (omissions counted N): S/(T+OMIT) = {cS}/{T}+{cO} = {cS}/{T2} = {100*cS/T2:.2f}%')
    return out,(cS,cE,cN,cO)
cons_units=[u for u in units if u['label']!='-']
r2_units=[u for u in units if u['r2lab'] not in ('','-') or u['r2st']=='OMIT']
lines=[]; res={}
for nm,sel,key in [('CONSENSUS, cipher-sign units only (CIPHER), unit rule','cc','st'),
                   ('CONSENSUS, cipher-sign units only, conservative (emended words wholly E)','cc','st_c'),
                   ('CONSENSUS, all units (cipher + codes/abbrev/clear)','ca','st'),
                   ('R2, cipher-sign units only (CIPHER), unit rule','rc','r2st'),
                   ('R2, cipher-sign units only, conservative','rc','r2st_c'),
                   ('R2, all units','ra','r2st')]:
    if sel=='cc': S=[u for u in cons_units if u['cat']=='CIPHER']
    elif sel=='ca': S=cons_units
    elif sel=='rc': S=[u for u in r2_units if u['cat']=='CIPHER']
    else: S=r2_units
    t,r=table(S,key,nm); lines+=t+['']; res[nm]=r
# category breakdown
cc=collections.Counter((u['cat'],u['st']) for u in cons_units)
lines.append('== consensus units by category: '+', '.join(f'{k[0]}:{k[1]}={v}' for k,v in sorted(cc.items())))
rc=collections.Counter((u['cat'],u['r2st']) for u in r2_units)
lines.append('== R2 units by category: '+', '.join(f'{k[0]}:{k[1]}={v}' for k,v in sorted(rc.items())))
lines.append('Clear-text words of the letter are NOT units in any score: only cipher-sign tokens (CIPHER) and the in-cipher codes/abbrev/clear tokens are ledgered.')
open(B+'out/COUNTS.txt','w').write('\n'.join(lines)+'\n')

# ---------- consensus literal decode + diff vs b55 plaintext ----------
dec=collections.OrderedDict()
for w in WORDS:
    if w['consword']=='-': continue
    ct=tokenize(w['consword']); line,widx=w['line'],int(w['widx'])
    if w['consword'] in CODES or w['consword']=='&':
        lit=w['consword']; con=w['accepted']
    else:
        lit=''.join((literal('CONS',l) or '?') for l in ct)
        con=''.join((decode_cons(line,widx,t,l)[0] or '?') for t,l in enumerate(ct))
    dec.setdefault(line,[]).append((w['consword'],lit.upper(),con.upper(),w['accepted'].upper()))
with open(B+'out/DECODE_consensus.txt','w',encoding='utf-8') as f:
    f.write('# line | consensus tokens -> LITERAL (KEY+aliases, no overrides) -> CONTRACT (with OVERRIDES) -> ACCEPTED ({x}=inserted letter, ?=no value)\n')
    for ln,ws in dec.items():
        for cw,lit,con,acc in ws: f.write(f'{ln}\t{cw}\t{lit}\t{con}\t{acc}\n')
# b55 plaintext tokens
def b55tokens(text):
    toks=[]
    for m in re.finditer(r"\?\?\([^)\s]*\)?|[A-Z\[\]?/]+",text):
        t=m.group(0)
        letters=re.sub(r'[^A-Z]','',t)
        if t.startswith('??'): toks.append(t); continue
        if t in ('PP',): continue
        if len(letters)>=2 or (t.startswith('[') and '?' in t): toks.append(t)
    return toks
b55=collections.OrderedDict()
for l in open(B55CONS,encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,text=l.split(None,1); lab='PS1' if lab=='PS' else lab
    b55.setdefault(lab,[]).extend(b55tokens(text))
norm=lambda s: re.sub(r'[\[\]]','',s).upper().replace('V','U')
diffs=[]
for ln in order:
    mine=[(cw,lit,con,acc) for (cw,lit,con,acc) in dec.get(ln,[]) if cw not in CODES and cw!='&']
    theirs=b55.get(ln,[])
    A=[norm(x[2]) for x in mine]; Bn=[norm(x) for x in theirs]
    sm=difflib.SequenceMatcher(a=A,b=Bn,autojunk=False)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal':
            for k in range(i2-i1):
                m=mine[i1+k]; t=theirs[j1+k]
                if m[1]!=m[2] or '[' in t:
                    diffs.append(f'{ln}\tEQUAL-AFTER-NORMALISING\t{m[0]}\tliteral={m[1]}\tcontract={m[2]}\tb55={t}')
        else:
            diffs.append(f'{ln}\t{op.upper()}\tmine={[ (m[0],m[1],m[2]) for m in mine[i1:i2]]}\tb55={theirs[j1:j2]}')
with open(B+'out/DIFF_vs_b55_consensus.txt','w',encoding='utf-8') as f:
    f.write('# Every place the regenerated consensus decode differs from b55 tx/aug_consensus_plaintext.txt (cipher words; codes and [per] abbreviations excluded).\n')
    f.write('# EQUAL-AFTER-NORMALISING = same word once b55 brackets removed and v=u, but b55 used brackets and/or the literal decode needs an override.\n')
    f.write('# REPLACE/INSERT/DELETE = genuine difference in word sequence or spelling.\n')
    for d in diffs: f.write(d+'\n')

# ---------- diff vs b55 R2 marks ----------
mk=[l.rstrip('\n').split('\t') for l in open(B55MARKS) if not l.startswith('#')]
old={}
cnt=collections.Counter()
for r in mk: cnt[r[0]]+=0
wi=collections.Counter()
for r in mk:
    i=wi[r[0]]; wi[r[0]]+=1
    for k,ch in enumerate(r[4]): old[(r[0],i,k)]=ch
oldtot=collections.Counter(old.values())
chk('b55 R2 marks reproduce 535+51+14=600',(oldtot['S'],oldtot['E'],oldtot['N'])==(535,51,14),str(dict(oldtot)))
new={}
for u in units:
    if u['r2st'] in ('S','E','N'):
        # R2 token index
        w=[x for x in WORDS if x['line']==u['line'] and int(x['widx'])==u['widx']][0]
        amap=list(range(len(tokenize(w['r2word'])))) if w['r2align']=='=' else [None if a=='-' else int(a) for a in w['r2align'].split(',')]
        ri = int(u['tidx'][1:]) if isinstance(u['tidx'],str) else amap.index(u['tidx'])
        new[(u['line'],u['widx'],ri)]=(u['r2st'],u['r2why'],u['r2lab'],u['acc'])
chk('R2 unit set == b55 marks unit set (600)',set(new)==set(old),f'{len(new)} vs {len(old)}')
with open(B+'out/DIFF_vs_b55_marks.tsv','w',encoding='utf-8') as f:
    f.write('line\twidx\tr2tok\tR2label\taccepted\tb55\tnew\treason\n')
    tr=collections.Counter()
    for k in sorted(old,key=lambda k:(order.index(k[0]),k[1],k[2])):
        if old[k]!=new[k][0]:
            tr[(old[k],new[k][0])]+=1
            f.write(f'{k[0]}\t{k[1]}\t{k[2]}\t{new[k][2]}\t{new[k][3]}\t{old[k]}\t{new[k][0]}\t{new[k][1]}\n')
    f.write('# transitions: '+', '.join(f'{a}->{b}: {n}' for (a,b),n in sorted(tr.items()))+'\n')
open(B+'out/CHECKS.txt','w').write('\n'.join(checks)+'\n')
print('\n'.join(checks)); print(open(B+'out/COUNTS.txt').read())

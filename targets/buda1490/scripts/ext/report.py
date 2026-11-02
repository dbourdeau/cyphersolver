"""Build key_external.json/.md, align.md, final_reading.md, measure_external.txt, transcription_suspects.md
from ext/alignment.json (output of ext/em_align.py)."""
import json,collections,re,difflib
A=json.load(open('ext/alignment.json')); P=A['path']; L=A['L']; words=A['words']; wid=A['wid']
key14=json.load(open('key_final.json'))
DAM='_'
# ---------- sign table ----------
cnt=collections.defaultdict(collections.Counter); tokc=collections.Counter()
for p in P:
    if p['type']=='skip' or p['sign']==DAM: continue
    v=('*'+p['txt']) if p['type']=='code' else p['txt']
    cnt[p['sign']][v]+=1; tokc[p['sign']]+=p['ntok']
def classify(s):
    c=cnt[s]; n=sum(c.values())
    codes={k[1:]:v for k,v in c.items() if k.startswith('*')}
    if sum(codes.values())>=0.5*n: return 'code',list(codes),c
    if c['']>=0.6*n: return 'null',[''],c
    acc=[k for k,v in c.most_common() if not k.startswith('*') and k!='' and (v>=2 and (v>=0.04*n or v>=5) or n<=2 and v==n)]
    if not acc: acc=[c.most_common(1)[0][0]]
    kind='poly' if len([a for a in acc if len(a)==1])>=2 else ('multi' if len(acc[0])>1 else 'single')
    return kind,acc,c
KEY={}
for s in cnt:
    kind,acc,c=classify(s); KEY[s]={'kind':kind,'values':acc,'n':sum(c.values()),'tokens':tokc[s],'counts':dict(c)}
# overrides judged from contexts (see notes): & stands where the cipher adds 'et' that the minute lacks (3/3)
KEY['&']['kind']='multi'; KEY['&']['values']=['et']; KEY['&']['note']='3/3 at cipher-only "et" (writer additions)'
def k14set(s):
    v=key14.get(s)
    if v is None or v=='#': return None
    return set(v.split('/'))
def ext_ok(s,p):
    k=KEY.get(s)
    if s==DAM or k is None: return False
    if p['type']=='code': return k['kind']=='code' and p['txt'] in k['values']
    if k['kind']=='code': return False
    return p['txt'] in k['values'] or (k['kind']=='null' and p['txt']=='')
# letters -> homophones
hom=collections.defaultdict(list)
for s,k in KEY.items():
    if k['kind'] in('single','poly','multi'):
        for v in k['values']: hom[v].append((s,k['counts'].get(v,0)))
# key comparison
cmp=[]
for s in sorted(KEY,key=lambda s:-KEY[s]['n']):
    k=KEY[s]; ks=k14set(s); ext=set(k['values'])
    if k['kind']=='code': extd='code: '+' / '.join(k['values'])
    elif k['kind']=='null': extd='null'
    else: extd='/'.join(k['values'])
    k14=key14.get(s,'(none)')
    if ks is None: verdict='no key14 value'; bad=k['n']
    else:
        if k['kind']=='code': bad=k['n']; verdict='wrong (is a code sign)' if ks!={''} else 'wrong (null in key14, code sign)'
        elif k['kind']=='null': bad=sum(v for t,v in k['counts'].items() if t not in ks); verdict='right' if ks=={''} else 'wrong (is a null)'
        else:
            bad=sum(v for t,v in k['counts'].items() if t not in ks)
            maj=k['values'][0]; k14maj=key14[s].split('/')[0]
            if ks==ext: verdict='right'
            elif maj==k14maj and ext<ks: verdict='right, but key14 extra value(s) '+'/'.join(sorted(ks-ext))+' not confirmed'
            elif maj==k14maj: verdict='right majority; missing value(s) '+'/'.join(sorted(ext-ks))
            elif maj in ks: verdict='majority wrong (key14 '+k14maj+', external '+maj+')'
            else: verdict='wrong'
    cmp.append((s,k14,extd,k['n'],k['tokens'],verdict,bad))
json.dump({s:{'kind':k['kind'],'values':k['values'],'count':k['n'],'tokens':k['tokens'],'counts':k['counts']} for s,k in KEY.items()},open('key_external.json','w'),indent=1,ensure_ascii=False)
# ---------- per-unit status ----------
units=[p for p in P if p['type']!='skip']
skips=[p for p in P if p['type']=='skip']
page=lambda h:h[:2]
# words: which units cover which word; ok if all covered letters by ok units and no skipped letters
wunits=collections.defaultdict(list); wskip=collections.Counter(); wdam=collections.Counter()
for p in units:
    for i in range(p['a'],p['b']):
        wunits[wid[i]].append(p)
        if p['sign']==DAM: wdam[wid[i]]+=1
for q in skips:
    for i in range(q['a'],q['b']): wskip[wid[i]]+=1
firstline={}
for p in units:
    for i in range(p['a'],p['b']): firstline.setdefault(wid[i],p['line'])
for q in skips:
    for i in range(q['a'],q['b']): firstline.setdefault(wid[i],None)
# fill lines of skipped words from neighbours
lastl='P1L01'
for w in range(len(words)):
    if firstline.get(w): lastl=firstline[w]
    else: firstline[w]=lastl
def wstatus(w):
    us=wunits.get(w,[])
    if not us: return 'absent'
    if wdam[w]: return 'damage'
    if wskip[w]: return 'mismatch'
    if all(ext_ok(p['sign'],p) for p in us): return 'agree'
    return 'mismatch'
# ---------- flags ----------
flags=[]
by_line=collections.OrderedDict()
for p in P:
    ln=p.get('line') or (by_line and next(reversed(by_line)))
    by_line.setdefault(ln,[]).append(p)
def isolated(seq,j):
    nb=[seq[x] for x in (j-1,j+1) if 0<=x<len(seq)]
    return all(q['type']!='skip' and ext_ok(q['sign'],q) for q in nb)
doubt={'mea','ab','deberet'}
suspects=[]
for ln,seq in by_line.items():
    j=0
    while j<len(seq):
        p=seq[j]
        if p['type']=='skip':
            txt=L[p['a']:p['b']]; ws=sorted({words[wid[i]] for i in range(p['a'],p['b'])})
            cls='clear-text reading doubt' if set(ws)&doubt else 'writer variation (clear letters not enciphered)'
            flags.append((ln,'-',txt,cls,' '.join(ws))); j+=1; continue
        if p['sign']==DAM:
            flags.append((ln,'_',p['txt'],'damage','')); j+=1; continue
        if not ext_ok(p['sign'],p) and not (p['sign']=='&' and p['txt']==''):
            # run
            k=j
            while k<len(seq) and (seq[k]['type']=='skip' or not ext_ok(seq[k]['sign'],seq[k])) and seq[k].get('sign')!=DAM: k+=1
            run=seq[j:k]
            ws=sorted({words[wid[i]] for q in run for i in range(q['a'],q['b'])})
            sig=' '.join(q['sign'] if q['type']!='skip' else '<-'+L[q['a']:q['b']]+'>' for q in run)
            txt=' '.join((q['sign']+'='+(q['txt'] or '0')) if q['type']!='skip' else '-'+L[q['a']:q['b']] for q in run)
            if p['sign']=='&': cls='writer variation (et added by the cipher writer)'
            elif set(ws)&doubt: cls='clear-text reading doubt'
            elif len(run)==1 and p['txt']=='' and KEY[p['sign']]['kind']!='null': cls='writer variation (sign with no clear counterpart: added letter/word)'
            elif len(run)==1 and len(p['txt'])==1 and isolated(seq,j) and len(KEY[p['sign']]['values'][0])==1:
                cls='transcription error? (%s read, clear implies a sign for "%s")'%(p['sign'],p['txt'])
                exp=[s for s,c in sorted(hom.get(p['txt'],[]),key=lambda x:-x[1])][:3]
                pos=sum(q['ntok'] for q in seq[:j] if q['type']!='skip')+1
                suspects.append((ln,pos,p['sign'],p['txt'],exp,' '.join(ws)))
            else: cls='writer variation (different word/spelling/order)'
            flags.append((ln,sig,txt,cls,' '.join(ws))); j=k; continue
        j+=1
# ---------- align.md ----------
with open('align.md','w') as f:
    f.write('# Alignment of DL 46150 (p1r-p4r round 6) with the clear minute (clear_running.txt)\n\n')
    f.write('Made by ext/em_align.py (EM dynamic-programming alignment, 6 iterations) and ext/report.py. ')
    f.write('Per line: the sign units (pair rules applied: oH, Ho, LL=6/6A+gA, Ga/Gp, veD = v e D/x, ve = v e, nq/ni, Om), the clear letters each unit was aligned to (`·` = no letter, `{word}` = code sign for whole word(s), `<abc>` = clear letters with no sign), then the Latin words. Flags below each line.\n\n')
    for ln,seq in by_line.items():
        cells=[]
        for p in seq:
            if p['type']=='skip': cells.append(('', '<'+L[p['a']:p['b']]+'>'))
            elif p['type']=='code': cells.append((p['sign'],'{'+p['txt']+'}'))
            else: cells.append((p['sign'],p['txt'] or '·'))
        ws=[]; 
        for p in seq:
            for i in range(p['a'],p['b']):
                if not ws or ws[-1]!=wid[i]: ws.append(wid[i])
        f.write(f'## {ln}\n\n```\n')
        row1=[];row2=[]
        for a,b in cells:
            w=max(len(a),len(b)); row1.append(a.ljust(w)); row2.append(b.ljust(w))
        # wrap at ~100 chars
        i=0
        while i<len(row1):
            l1=l2=''
            while i<len(row1) and len(l1)+len(row1[i])<110: l1+=row1[i]+' '; l2+=row2[i]+' '; i+=1
            f.write(l1.rstrip()+'\n'+l2.rstrip()+'\n')
        f.write('```\nLatin: '+' '.join(words[w] for w in ws)+'\n\n')
        fl=[x for x in flags if x[0]==ln]
        for x in fl: f.write(f'- FLAG `{x[1]}` → {x[2]} — **{x[3]}** ({x[4]})\n')
        f.write('\n')
# ---------- transcription_suspects.md ----------
with open('transcription_suspects.md','w') as f:
    f.write('# Transcription suspects from the external alignment\n\nIsolated one-sign disagreements (both neighbours agree with the clear text). p*r.txt NOT changed; each needs an image check. Crops: ext/crops/ if made.\n\n| line | token # in line | sign read | clear letter | usual signs for that letter | clear word | crop |\n|---|---|---|---|---|---|---|\n')
    for s in suspects:
        cr={'P1':'crops/L%s.png'%s[0][3:],'P2':'crops_p2/','P3':'crops_p3/','P4':'crops_p4/'}[s[0][:2]]
        f.write(f'| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {", ".join(s[4])} | {s[5]} | {cr} |\n')
# ---------- final_reading.md ----------
def unitread(p):
    s=p['sign']
    if s==DAM: return '⟨'+p['txt']+'⟩' if p['txt'] else '⟨·⟩'
    k=KEY.get(s)
    if k['kind']=='null': return ''
    if k['kind']=='code': return p['txt'] if p['type']=='code' else '['+k['values'][0]+']'
    if p['txt'] in k['values']: return p['txt']
    return k['values'][0]
with open('final_reading.md','w') as f:
    f.write('# Final reading of DL 46150 under key_external\n\nLatin as the signs give it (key_external.json; a polyphonic sign takes the value of its set that the alignment chose). ⟨..⟩ = letters lost to damage, filled from the clear minute. `[?]` = the signs disagree with the clear minute; the clear form follows in (parentheses). (-word) = word of the minute with no sign in the cipher. +xyz[?] = letters the cipher has and the minute does not (added word or letters). CODE(...) = one code sign standing for the words in brackets. A word is printed on the line where its first sign stands.\n\n')
    wl=collections.defaultdict(str); wline={}; codew={}; extra=collections.defaultdict(str)
    for p in P:
        if p['type']=='skip':
            for i in range(p['a'],p['b']): wl[wid[i]]+=''
            continue
        if p['type']=='code':
            ws=sorted({wid[i] for i in range(p['a'],p['b'])})
            codew[ws[0]]=(ws,p['sign'])
            for x in ws: wline.setdefault(x,p['line']); wl[x]+=''
            continue
        r=unitread(p)
        if p['b']==p['a']:
            if r: extra[(p['a'],p['line'])]+=r
            continue
        w=wid[p['a']]
        wl[w]+=r; wline.setdefault(w,p['line'])
    last='P1L01'
    for w in range(len(words)):
        if w in wline: last=wline[w]
        else: wline[w]=last
    wend_=[0]*len(words)
    for i,x in enumerate(wid): wend_[x]=i+1
    for (a,ln),x in list(extra.items()):
        if a==0: lines0=x
    inside={x for ws,_ in codew.values() for x in ws[1:]}
    cur=None; lines=collections.OrderedDict()
    for ln in by_line: lines[ln]=[]
    for w in range(len(words)):
        if w in inside: continue
        if w in codew:
            ws,sg=codew[w]; lines[wline[w]].append('CODE('+' '.join(words[x] for x in ws)+')')
            for (a,ln),x in list(extra.items()):
                if a==wend_[ws[-1]]: lines[ln].append('+'+x+'[?]'); del extra[(a,ln)]
            continue
        got=wl[w]; clear=words[w]; plain=re.sub(r'[⟨⟩]','',got)
        if got=='': t='(-'+clear+')'
        elif plain==clear: t=got
        else: t=f'{got}[?]({clear})'
        lines[wline[w]].append(t)
        for (a,ln),x in list(extra.items()):
            if a==wend_[w]: lines[ln].append('+'+x+'[?]'); del extra[(a,ln)]
    nq=0
    for ln,toks in lines.items():
        if ln[:2]!=cur: cur=ln[:2]; f.write(f'\n## Page {cur[1]}\n\n')
        nq+=sum('[?]' in t for t in toks)
        f.write(f'**{ln}** '+' '.join(toks)+'\n\n')
    f.write(f'\n[?] marks: {nq}\n')
# ---------- measure ----------
pages=['P1','P2','P3','P4']
ms=[]
tot=collections.Counter()
for pg in pages+['ALL']:
    us=[p for p in units if pg=='ALL' or p['line'].startswith(pg)]
    T=sum(p['ntok'] for p in us); Td=sum(p['ntok'] for p in us if p['sign']==DAM)
    Ta=sum(p['ntok'] for p in us if ext_ok(p['sign'],p))
    W=[w for w in range(len(words)) if pg=='ALL' or (firstline[w] or '').startswith(pg)]
    st=collections.Counter(wstatus(w) for w in W)
    ms.append((pg,T,Ta,Td,len(W),st))
# blind reading accuracy
blind=[];bl=[]
for l in open('reading.md'):
    m=re.match(r'\*\*(P\dL\d+)\*\*',l)
    if m: cl=m.group(1)
    if l.startswith('- Latin:'):
        for t in l[8:].split():
            blind.append((cl,t))
bw=[]
for c,t in blind:
    if t.startswith('-') and bw and bw[-1][0]!=c: bw.pop(); t=t[1:]
    bw.append((c,t))
seqb=[re.sub(r'\[\?\]','',t).lower() for c,t in bw]
sm=difflib.SequenceMatcher(None,seqb,words,autojunk=False)
match=[False]*len(seqb)
for a,b,n in sm.get_matching_blocks():
    for x in range(n): match[a+x]=True
read=[i for i,(c,t) in enumerate(bw) if '[?]' not in t and '[' not in t and not t.startswith('-') and re.fullmatch(r'[a-z]+',t)]
hyph=[i for i,(c,t) in enumerate(bw) if t.startswith('-') or t.endswith('-')]
bpage=collections.defaultdict(lambda:[0,0])
for i in read:
    bpage[bw[i][0][:2]][0]+=1; bpage[bw[i][0][:2]][1]+=match[i]
wrongs=[(bw[i][0],seqb[i]) for i in read if not match[i]]
qread=[i for i,(c,t) in enumerate(bw) if t.endswith('[?]')]
with open('measure_external.txt','w') as f:
    f.write('External measure (ext/report.py on ext/alignment.json; key_external.json). Token = cipher sign (pair units count their signs). A token agrees when its unit emits a value of its key_external entry at the aligned clear position. Damage = lost signs (_), kept separate.\n')
    f.write('Word = word of the clear minute (clear_running.txt, date line dropped). agree = every letter covered by agreeing units, no unenciphered letters; damage = has a lost sign; absent = no cipher counterpart at all.\n\n')
    for pg,T,Ta,Td,NW,st in ms:
        f.write(f"{pg}: tokens {T}  agree {Ta} ({100*Ta/T:.1f}%; of undamaged {100*Ta/(T-Td):.1f}%)  damage {Td} ({100*Td/T:.1f}%)  |  clear words {NW}  agree {st['agree']} ({100*st['agree']/NW:.1f}%; of undamaged {100*st['agree']/(NW-st['damage']):.1f}%)  mismatch {st['mismatch']}  damage {st['damage']}  absent {st['absent']}\n")
    nr=len(read); nm=sum(match[i] for i in read)
    f.write(f'\nBlind-reading accuracy (key14 reading, reading.md "Latin:" lines; words not marked [?], not [...], not line-split fragments; exact match after difflib word alignment with the clear text):\n')
    for pg in pages: r,m=bpage[pg]; f.write(f'  {pg}: read {r}  exact {m} ({100*m/max(r,1):.1f}%)\n')
    f.write(f'  TOTAL: read {nr}  exact {nm} ({100*nm/nr:.1f}%)\n')
    qm=sum(match[i] for i in qread)
    f.write(f'  words the reading marked [?]: {len(qread)}, of which exactly right after dropping [?]: {qm}\n')
    f.write('\nRead words not matching the clear text exactly:\n')
    for c,t in wrongs: f.write(f'  {c} {t}\n')
# key md
with open('key_external.md','w') as f:
    f.write('# key_external: key rebuilt from the clear minute (key from external plaintext)\n\nCounts = aligned occurrences (units; damage excluded). Values = accepted values (>=2 cases and >=4%); the full count table shows every string the alignment gave the sign, including strays (misalignments, transcription errors or writer variation). Tokens = cipher signs in those units.\n\n')
    f.write('## Comparison with key14, sign by sign\n\n| sign | key14 | external | n | tokens | verdict | units not covered by key14 value |\n|---|---|---|---|---|---|---|\n')
    for r in cmp: f.write('| `%s` | %s | %s | %d | %d | %s | %d |\n'%r)
    f.write('\n## Full table with counts\n\n| sign | kind | counts |\n|---|---|---|\n')
    for s in sorted(KEY,key=lambda s:-KEY[s]['n']):
        k=KEY[s]; f.write(f"| `{s}` | {k['kind']} | {', '.join((t or '0')+':'+str(v) for t,v in sorted(k['counts'].items(),key=lambda x:-x[1]))} |\n")
    f.write('\n## Homophones per letter\n\n')
    for v in sorted(hom): f.write(f"- **{v}**: "+', '.join(f'`{s}` {c}' for s,c in sorted(hom[v],key=lambda x:-x[1]))+'\n')
    f.write('\n## Code signs\n\n'+''.join(f"- `{s}` ({k['n']}): "+'; '.join(f'{t[1:]} {v}' for t,v in k['counts'].items() if t.startswith('*'))+'\n' for s,k in KEY.items() if k['kind']=='code'))
    f.write('\n## Nulls\n\n'+', '.join(f"`{s}` ({k['n']})" for s,k in KEY.items() if k['kind']=='null')+'\n')
print(open('measure_external.txt').read()[:3000])
for r in cmp:
    if not r[5].startswith('right') or r[6]: print(r)
print(len(flags),'flags', collections.Counter(x[3].split(' (')[0] for x in flags)); print(len(suspects),'suspects')

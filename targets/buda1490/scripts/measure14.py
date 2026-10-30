"""measure14: strict word/token measure of ann14.txt against the dec14 decrypt (key14.json, p1r..p4r.txt).
Syntax as measure12: word | word=norm (read, writer spelling) | word~norm (NOT read: letter mismatch) |
?word[=norm] ([?], NOT read) | [letters ...] (unread; est. max(1,round(len/6)) words) | '-' continues a word.
'#' in a bracket = code group or sign with no value. '_' = lost sign -> damage.
Polyphony: decrypt letter 'U' (oo/ooA/ooB/qB = u/s) accepts u or s in the annotation.
A read word containing a 'U' is counted 'read' only if no other u/s choice gives a different word of
the lexicon (all read words of ann14 + LEX_EXTRA); otherwise 'poly-ambiguous' (not read).
Column 'poly-dep' = read words that contain at least one u/s sign (subset of read)."""
import sys,json,re,collections,itertools
from dec14 import units,lines,dec,ntok,val,SETS,MAJ
key=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'key14.json'))
LEX_EXTRA={'fui','fuit','fit','fac','fas','fere','fide','fides','fuisse','sic','hic','hoc','hac','has','his','hec','haec','hunc','hinc','fac','fuga','suum','sunt','sumus','suis','sui','suis','sum','sua','suo','usu','uis','ius','is','us','ut','uos','sis','suus','uisus','ussi','sus'}
L=list(lines()); D={h:dec(key,units(t)) for h,t in L}; UN={h:units(t) for h,t in L}
ANN=[l.rstrip('\n').split(' ',1) for l in open('ann14.txt')]
lex=set(LEX_EXTRA)
for h,a in ANN:
    for w in a.split():
        if w.startswith('[') or w.endswith(']') or w.startswith('?') or '~' in w or '-' in w: continue
        lt,_,nm=w.partition('='); lex.add(lt.strip('-')); lex.add(nm.strip('-'))
def ok(a,b): return len(a)==len(b) and all(x==y or (y in SETS and x in SETS[y]) for x,y in zip(a,b))
cnt=collections.defaultdict(collections.Counter); tc=collections.defaultdict(collections.Counter)
bad=[]; notread=[]; lat=[]; opn=False; buf=''; bufh=None; last='read'; polylist=[]; minlist=[]; pend=None
def close_word(p):
    # p=[h,full letters,full pattern,kind,label]
    h,lt,pat,kind,lab=p
    if kind=='read' and any(c in SETS for c in pat):
        alts=set()
        idx=[i for i,c in enumerate(pat) if c in SETS]
        for ch in itertools.product(*[SETS[pat[i]] for i in idx]):
            s=list(lt)
            for i,c in zip(idx,ch): s[i]=c
            s=''.join(s)
            if s!=lt and s in lex: alts.add(s)
        if alts: kind='polyamb'; notread.append((h,lab,1,'polyphony ambiguous: other choice gives '+'/'.join(sorted(alts))))
        else:
            cnt[h[:2]]['poly']+=1; polylist.append((h,lab))
            mins=set()
            for i in idx:
                if lt[i]!=MAJ[pat[i]]: mins.add({'U':'oo-u/s=s','W':'qB=s' if lt[i]=='s' else 'qB=f','S':'s=f'}[pat[i]])
            if mins: cnt[h[:2]]['minor']+=1; minlist.append((h,lab,sorted(mins)))
            for m in mins: cnt[h[:2]]['m:'+m]+=1
    cnt[h[:2]][kind]+=1
    return kind
for h,a in ANN:
    d=D[h]; letters=''; spans=[]; la=[]
    for w in a.split():
        if opn or w.startswith('['):
            if w.startswith('['): opn=True; buf=''; bufh=h
            s=w.strip('[]'); spans.append((len(letters),len(letters)+len(s),'damage' if '_' in s else 'open')); letters+=s; buf+=s
            if w.endswith(']'):
                opn=False; n=max(1,round(len(buf.replace('_',''))/6)); k='damage' if '_' in buf else 'open'
                cnt[bufh[:2]][k]+=n
                why='damage: lost sign(s) inside' if k=='damage' else ('code group v-e-D/x (#) inside' if '#' in buf and 'hom' not in buf else 'no Latin sense under key14')
                notread.append((bufh,'['+buf+']',n,why)); la.append('[...]')
            continue
        doubt=w.startswith('?'); w=w.lstrip('?')
        lt,sep,norm=re.match(r'([^=~]+)([=~])?(.*)',w).groups()
        cont=lt.startswith('-'); L0=len(letters); letters+=lt.strip('-')
        pat=d[L0:len(letters)]
        kind='damage' if '_' in lt else 'doubt' if doubt else 'tol' if sep=='~' else 'read'
        form=(norm or lt).strip('-')
        if cont and pend:
            pend[1]+=lt.strip('-'); pend[2]+=pat; pend[4]+=lt.strip('-')+((sep+norm) if norm else '')
            spans.append((L0,len(letters),pend[3])); la.append('-'+form+('' if pend[3]=='read' else '[?]')); continue
        if pend: k2=close_word(pend); 
        pend=[h,lt.strip('-'),pat,kind,lt+(sep or '')+(norm or '')] if not cont else None
        if kind in('tol','doubt','damage'):
            why={'damage':'damage: lost sign','doubt':'[?]: value attested in <2 words / unresolved sign','tol':'letter mismatch: sign value not in key14'}[kind]
            notread.append((h,lt+(sep or '')+(norm or ''),1,why))
        spans.append((L0,len(letters),kind)); la.append(form+('' if kind=='read' else '[?]'))
    if not ok(letters,d): bad.append((h,letters,d))
    lat.append((h,la,spans))
if pend: close_word(pend)
# token shares (poly-ambiguous words: recompute kind from notread is complex; tokens of read words that became polyamb counted via word list)
amb={(r[0],r[1]) for r in notread if r[3].startswith('u/s')}
for (h,la,spans),(hh,tk) in zip(lat,L):
    pos=0
    for x in UN[h]:
        for a0,b0,kd in spans:
            if a0<=pos<b0 or (a0==b0==pos): tc[h[:2]][kd]+=ntok(x); break
        else: tc[h[:2]]['open']+=ntok(x)
        pos+=len(val(key,x))
for b in bad: print('MISMATCH',*b)
res=[]; tot=collections.Counter(); T=collections.Counter()
f=lambda a,n:f'{a} ({100*a/max(n,1):.1f}%)'
for p in ['P1','P2','P3','P4','TOTAL']:
    c=tot if p=='TOTAL' else cnt[p]
    if p!='TOTAL': tot+=c
    n=sum(v for k,v in c.items() if k not in('poly','minor') and not k.startswith('m:')); nd=n-c['damage']
    res.append(f"{p}: words {n}  read-strict {f(c['read'],n)}  of which contain a polyphonic sign {c['poly']}  depend on a minority value {c['minor']} [oo-u/s=s {c['m:oo-u/s=s']}, qB=s {c['m:qB=s']}, qB=f {c['m:qB=f']}, s=f {c['m:s=f']}]  read-without-any-minority-value {f(c['read']-c['minor'],n)}  poly-ambiguous {c['polyamb']}  letter-mismatch(~) {c['tol']}  [?] {c['doubt']}  unread(est.) {c['open']}  blocked by damage {c['damage']}  | read of undamaged {f(c['read'],nd)}")
for p in ['P1','P2','P3','P4','TOTAL']:
    c=T if p=='TOTAL' else tc[p]
    if p!='TOTAL': T+=c
    m=sum(c.values())
    res.append(f"{p} tokens {m}: read-strict {100*(c['read'])/m:.1f}%  ~ {100*c['tol']/m:.1f}%  [?] {100*c['doubt']/m:.1f}%  unread {100*c['open']/m:.1f}%  damage {100*c['damage']/m:.1f}%")
res.append("(token shares count u/s-ambiguous words' tokens as read; word figures do not)")
print('\n'.join(res)); print()
print('Read words that depend on a minority polyphonic value:')
for r in minlist: print(' ',r[0],r[1],','.join(r[2]))
print()
CAUSE={
('P1L01','[ciciusqubm]'):'key: tp/x stretch after the salutation, no Latin candidate',
('P1L02','presenis~presentis'):'writer omission or key gap (image: no missed sign)',
('P1L02','[ho]'):'[?] "v e" alone = hoc (code-group parallel), 1 word',
('P1L02','[sui]'):'key: no sense in context',
('P1L04','dominatiunem~dominationem'):'qB = o needed (1 word)',
('P1L05','csrca~circa'):'[?] qA = i (1 word)',
('P1L05','afinitasem~affinitatem'):'[?] qA = t (1 word)',
('P1L05','[cupidinser]'):'key: no Latin candidate',
('P1L06','[preuatum#ediomo]'):'code group v-e-D (#) + priuatum needs o = i (1 word)',
('P1L08','[uuibudametabea]'):'[?] quibusdam needs qB = q (qC, 1 token); rest unresolved',
('P1L08','prefatu~prefatum'):'ff here would need = m (ff = null elsewhere, 3 words)',
('P1L10','[spsam]'):'image: qA x~1490 may be H crossbar (ipsam); ambiguous',
('P1L10','[hr]'):'key: no candidate',
('P1L11','co#iserat=commiserat'):'[?] Ob = m (new label, 1 word)',
('P1L11','[rmeletoansmo]'):'key/image (qA x~3195); no candidate',
('P1L12','[ehcrsentda]'):'key: no candidate',
('P1L17','[renis]'):'image: 3 between 3 and 3G (regis), ambiguous',
('P1L18','[tam_n]'):'damage (blot x~2280)',
('P1L19','[reeatur]'):'image: B? (ring with dot) ambiguous',
('P1L19','amictssi-~amicissi-'):'image: Q/4 ambiguous at x~3190',
('P1L20','afects~affectus'):'key: missing u (no sign)',
('P1L20','[iemher]'):'[?] semper needs 4 = s and f = p (1 word each)',
('P1L21','oitendit~ostendit'):'[?] 4 = s (1 clean word)',
('P1L23','[ani]'):'key: no candidate (nam/enim need 2 changes)',
('P1L24','[us]'):'[?] "ut" would need qB = t; open',
('P1L29','tantto~tanto'):'writer dittography (both signs real)',
('P2L02','[ubeiimumursotum]'):'key: no hypothesis',
('P2L02','senuiet~sentiet'):'key: 1 sign',
('P2L04','[#eo]'):'code group v-e-D (#)',
('P2L06','sio=sit'):'[?] 1 sign',
('P2L07','proter=propter'):'writer spelling (image-confirmed twice); kept [?]',
('P2L08','proter=propter'):'writer spelling (image-confirmed twice); kept [?]',
('P2L10','cotraxerat=contraxerat'):'[?] missing n',
('P2L11','[re#]'):'[?] Bd = x (rex), new label, 1 token',
('P2L12','nersuadebit~persuadebit'):'key: 1 sign',
('P2L13','cepoa~cepta'):'key: 1 sign',
('P2L14','[ssenouamin#sseuerumeut]'):'key: 8C has no value; no Latin',
('P2L15','[perpetite]'):'key/image (Tx inside; perpetite?)',
('P2L15','[amthumuiuaest]'):'image: f? is a distinct c-with-loop shape; no value',
('P2L16','[#euminacio_m]'):'code group v-e-D + damage',
('P2L17','[malunit]'):'image: P? at t15 under blot (maluit?)',
('P2L17','[eiuisumeut]'):'key: u/s choices and qA; no candidate',
('P2L20','[ec]'):'[?] Rx b = null pair (1 case)',
('P2L22','[a#epit]'):'[?] sl = c (accepit), new label, 1 token',
('P2L22','[uieata]'):'key: no hypothesis',
('P2L24','[_tetuosal#]'):'damage + 8C no value',
('P2L24','michi'):'[?] 6B/8A reading of michi unconfirmed',
('P2L25','[#ei]'):'code group v-e-D (#)',
('P2L26','[alitsone]'):'key: no candidate',
('P2L27','ragi~regi'):'key: 1 sign',
('P2L27','promiuirat~promiserat'):'key: 1 sign',
('P2L28','[ostendareue]'):'[?] F = e (ostendere se), 1 token',
('P3L01','[sicstipriuudeucenderat]'):'[?] qA = u (sicuti prius descenderat), 1 clean word',
('P3L02','[#]'):'fo (f with raised o, new label) no value; numeral/abbreviation?',
('P3L03','[eausga]'):'[?] qA = u + O=m after qA (summam), rule extension',
('P3L03','iocaluum~iocalium'):'[?] qB = i (2 words, not adopted: 4th value)',
('P3L06','e#cepto=excepto'):'[?] 8C = x (1 word)',
('P3L08','[uhb]'):'image: arch + rho (s tp) maybe one compound sign',
('P3L09','exponendb~exponenda'):'key: 1 sign',
('P3L10','seco-~secun-'):'[?] gA = u or writer spelling',
('P3L13','[d]'):'image: d? ambiguous (dx null?)',
('P3L17','reuerendissume~reuerendissime'):'[?] qB = i (2 words, not adopted: 4th value)',
('P3L17','[h]'):'[?] f at line end null (1 case)',
('P3L19','[heucetditadtam]'):'key: no candidate',
('P3L24','quemhadmodum~quemadmodum'):'s here would need null',
('P3L24','[uanninem]'):'image: second 3 half-fits 3G (sanguinem)',
('P3L27','admiendas~admittendas'):'y = t? conflicts with y = null (3 words)',
('P3L29','responu~responso'):'key: 1 sign',
('P3L29','[tetauth]'):'key: unresolved',
('P4L01','[isaincoratores]'):'key/image (F blotted)',
('P4L02','[mi#antur]'):'[?] wL = t (mittantur), 1 token',
('P4L04','[h]'):'[?] s here null (1 case)',
('P4L05','[ehx]'):'[?] Rx y + compound "s p"; no value',
('P3L16','ius=eius'):'[?] first e of eius lost at the end of L15 (damage)',
('P3L16','retraere=retrahere'):'[?] missing h',
}

def cz(a,b,w):
    c=CAUSE.get((a,b))
    if c is None: return w
    return ('damage + '+c) if w.startswith('damage') and 'damage' not in c else c
notread=[(a,b,n,cz(a,b,w)) for a,b,n,w in notread]
json.dump({'res':res,'notread':notread,'latin':[(h,la) for h,la,_ in lat],'poly':polylist,'minority':minlist},open('measure14.json','w'))
for r in notread: print(*r)

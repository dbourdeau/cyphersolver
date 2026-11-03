# f73_apply.py : cc. 73v-74r (2 Feb 1636). Start from the key-free read, apply only corrections settled on the enlarged strips, log them, decrypt with key.tsv unchanged.
import re,json
ID=json.load(open('scans/work/blind_ids_private.json'))
K={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('# ') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); K[p[0]]=p[2]
K['+']='u'
rows={}
for l in open('scans/blind/read_f73.txt',encoding='utf8'):
    m=re.match(r'(c\d+[rv]) (\d+)\.(\d+):\s*(.*)',l)
    if not m or '{none}' in m[4]: continue
    o=[]
    for t in re.findall(r'\[[^\]]*\]|\{[^}]*\}|\S+',m[4]):
        if t.startswith('{'): o.append('{clear}'); continue
        h='^' if t.endswith('^') else ''; t=t.rstrip('^'); b=re.match(r'\[blot:(.*)\]',t)
        o.append(('['+ID.get(b[1],'?')+']'+h) if b else (ID.get(t,'?')+h))
    rows.setdefault((m[1],int(m[2])),[]).append(' '.join(o))
E=[(('c73v',2),'A D V 2 D 2 V A 3','A D v 2 D 2 v A 3','short V, h; read as n by the reader'),
(('c73v',3),'c 2 N T V c T 9 T o N','c 2 r T V c T 9 T o N','hook with ball, f; reader N'),
(('c73v',4),'v T ? A + T 9 T o ?','v T [v] A + T 9 T o N','blot over h; last sign whole on the paper, past the end of the old strip'),
(('c73v',5),'c A r ? N V','c A r [9] N V','heavy blot over r'),
(('c73v',6),'[N] 2 V ? 2','[N] 2 V [r] 2','blot over f, tail visible'),
(('c73v',6),'D v + x 2 A o','D v T x 2 A o','inverted T; reader +'),
(('c73v',10),'+ A r A o A c T c 2 x','4 A r A o A c T c 2 x','long-legged 4; reader +'),
(('c73v',10),'A c^ 2 2 V 3 N + T 9 A','A [g]^ 2 2 V 3 N 4 T 9 A','open curve under the caret, g by sense; 4 with long leg'),
(('c73v',8),'V c A 3 T ?','V c A 3 T A','last sign whole on the paper, past the end of the old strip'),
(('c73v',10),'v T x V r 9 2 + A N','v T x V r 9 2 + A V N','n and o both legible past the end of the old strip; the sign after x stays V, a slip for o'),
(('c74r',0),'# 9 N D T 3^','# 9 N o T 3^','fourth sign has vertical sides, unlike the clean triangle six signs on; box'),
(('c74r',5),'[N] o x 2 9 2','[x] . o . x 2 9 2','blot over s; dots mark the abbreviation S. M.'),
(('c74r',10),'x N r N','x N V N','tick with long stroke; reader r'),
(('c74r',11),'/ N 4 N ?','/ N 4 N [g]','blot over g'),
(('c74r',13),'r 9 ? # N','r 9 [A] # N','blot over a'),
(('c74r',14),'A +^ 2 x N ? c A 9','A +^ 2 x N [deleted signs] c A 9','oval blot; the sentence runs through it'),
(('c74r',14),'A x o T 3','A x . o . T 3','dots mark the abbreviation S. M.'),
]
L=[('c73v',n) for n in range(1,12)]+[('c74r',n) for n in [0,5,6,7,8,9,10,11,12,13,14,15]]
log=['line\tkey-free read\tsigns now\treason']; used=0; T=[]; D=[]
def dec(b):
    def tr(m):
        t=m.group(0)
        if t.startswith('{') or t=='[deleted signs]': return ' '+t+' '
        if t=='.': return '.'
        h='^' if t.endswith('^') else ''; t=t.rstrip('^')
        if t=='?': return '?'
        return ('['+K[t[1:-1]]+']' if t.startswith('[') else K[t])+h
    d=re.sub(r'\{[^}]*\}|\[deleted signs\]|\[[^\] ]\]\^?|\S',lambda m:tr(m) if not (m.group(0)=='^') else '^',b)
    p=re.split(r'(\{[^}]*\}|\[deleted signs\])',d)
    return ' '.join(x for x in (q if q.startswith(('{','[deleted')) else q.replace(' ','') for q in p) if x)
for k in L:
    b=' '.join(rows[k])
    for e in E:
        if e[0]==k:
            assert e[1] in b,(k,e[1]); b=b.replace(e[1],e[2]); log.append(f'{k[0]} {k[1]}\t{e[1]}\t{e[2]}\t{e[3]}'); used+=1
    b=b.replace('{clear}','{rincontri:}') if k==('c73v',1) else b
    if k==('c74r',0): b+=' {Con la conf. diamo parte}'
    pl=f'c. {k[0][1:3]}{k[0][3]} cipher row {k[1]}'
    T.append(f'{pl}: {b}'); D.append(f'{pl}: {dec(b)}')
fn='cc73-74_1636-02-02.txt'
open('transcription_'+fn,'w',encoding='utf8').write("# Sign codes per key.tsv. Rows counted through the cipher on each page; c. 74r rows 0, then 5-9, then 10-15 as numbered on the strips.\n# Base text: one key-free reader who had no key and no language. Corrections made on enlarged strips, recut to the true paper edge, are in retranscription_log_1636.tsv. Only those were changed.\n# x^ a caret above the sign, the letter doubled; [x] blotted; . dots of an abbreviation; {..} clear words on the row.\n"+'\n'.join(T)+'\n')
open('decryption_'+fn,'w',encoding='utf8').write("# Letter-for-letter decryption with key.tsv unchanged. x^ means the letter doubled. Departures for sense are in the reading file.\n"+'\n'.join(D)+'\n')
open('retranscription_log_1636.tsv','w',encoding='utf8').write('\n'.join(log)+'\n')
n=sum(len(re.findall(r'\S+',re.sub(r'\{[^}]*\}|\[deleted signs\]|(?<= )\.(?= )','',t.split(':',1)[1]))) for t in T)
q=sum(t.count(' ?') for t in T); print('rows',len(T),'signs',n,'corrections',used,'of',len(E),'? left',q)
print('\n'.join(D))

"""decode_A.py [train-only] : decode the frozen code A transcription with the frozen KEY_A.tsv by RULES_A.txt.
Writes codeA/DECODE_A.txt (all letters, held-out tagged) and judge/decode_A.txt (clear text as '/').
With 'train-only' it prints the A1 lines only and writes nothing (format check before the one held-out decode)."""
import sys,re
R='/home/claude/keyless/rosenkrantz1629/pass2'
sys.path.insert(0,R+'/tools'); from numlib import load
key={}
for l in open(R+'/codeA/KEY_A.tsv').read().splitlines()[1:]:
    f=l.split('\t'); key[int(f[0])]=f[2]
lows={}
for v,L in key.items():
    if v<200: lows.setdefault(v%9,[]).append(v)
def letter(v,flag):
    if isinstance(v,str): return '?'
    if v in key: return '['+str(v)+']' if key[v]=='WORD' else key[v]
    if v>=200: return '['+str(v)+']'
    row=sorted(lows.get(v%9,[])); lo=[u for u in row if u<v]; hi=[u for u in row if u>v]
    if lo and hi and key[lo[-1]]==key[hi[0]]: return key[lo[-1]]
    return '?'
HELD={'A1P','A2'}
trainonly=len(sys.argv)>1 and sys.argv[1]=='train-only'
out=[]; jd=[]
for let,img,ln,items in load(R+'/tx/CODE_A_FROZEN.tsv'):
    if trainonly and let!='A1': continue
    o=''; j=''
    for it in items:
        if it[0]=='c': o+=' {'+it[1]+'} '; j+=' / '
        elif it[0]=='d': o+=' ['+it[1]+'] '; j+=' '
        else:
            x=letter(it[1],it[2])
            if x.startswith('['): o+=' '+x+' '; j+=' '+x+' '
            else: o+=x; j+=x
    tag='HELD-OUT' if let in HELD else 'train'
    out.append(f"{let}\t{img}\t{ln}\t{tag}\t"+re.sub(' +',' ',o).strip())
    jd.append(f"{let} {img} l{ln} {'[HELD-OUT] ' if let in HELD else ''}"+re.sub(' +',' ',j).strip())
if trainonly: print('\n'.join(out))
else:
    open(R+'/codeA/DECODE_A.txt','w').write('\n'.join(out)+'\n'); open(R+'/judge/decode_A.txt','w').write('\n'.join(jd)+'\n'); print('written')

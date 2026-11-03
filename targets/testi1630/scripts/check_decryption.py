# check_decryption.py : rerun key.tsv over every transcription and compare with the decryption files. Standard library, relative paths.
# Run from the folder that holds key.tsv: python scripts/check_decryption.py . Consistency only: it says nothing about the signs.
import glob,re
K={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('# ') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); K[p[0]]=p[2]
K['+']='u'
def dec(body):
    out=''
    for t in re.findall(r'\{[^}]*\}|\[deleted signs\]|\[[^\] ]+\]\^?|\S+',body):
        if t.startswith('{') or t=='[deleted signs]': out+=' '+t+' '; continue
        h='^' if t.endswith('^') else ''; t=t.rstrip('^')
        if t in ('?','.','|'): out+=t+h; continue
        if t[0]=='(': out+='('+K[t[1:-1]]+')'; continue
        out+=('['+''.join(K[c] for c in t[1:-1])+']' if t.startswith('[') else K[t])+h
    return ' '.join(out.split())
tot=bad=0
for f in sorted(glob.glob('transcription_*.txt')):
    g=f.replace('transcription_','decryption_')
    T=[l for l in open(f,encoding='utf8').read().split('\n') if l.strip() and not l.startswith('#')]
    D=[l for l in open(g,encoding='utf8').read().split('\n') if l.strip() and not l.startswith('#')]
    n=0
    for a,b in zip(T,D):
        x=dec(a.split(':',1)[1]); y=' '.join(b.split(':',1)[1].split()); n+=1
        if x!=y: bad+=1; print('DIFF',f,a.split(':',1)[0],'\n  ',x,'\n  ',y)
    tot+=n; print(f,len(T),len(D),'lines')
print('lines compared',tot,'differences',bad)

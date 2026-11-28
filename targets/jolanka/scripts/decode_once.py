# One decode of the frozen transcription with the frozen key. python3 -I decode_once.py
import sys, hashlib
B='/home/claude/keyless/postcards/jolanka'; sys.path.insert(0,B+'/tools')
from decode_lib import dec_line
for f,line in (('KEY.tsv',2),):
    want=open(B+'/FREEZE_KEY.txt').read().split('\n')[1].split()[0]
    assert hashlib.sha256(open(B+'/'+f,'rb').read()).hexdigest()==want, 'key changed after freeze'
fr=open(B+'/FREEZE_TX.txt').read().split('\n')
assert hashlib.sha256(open(B+'/TRANSCRIPTION.tsv','rb').read()).hexdigest()==fr[1].split()[0], 'transcription changed after freeze'
key={l.split('\t')[0]:l.split('\t')[1] for l in open(B+'/KEY.tsv',encoding='utf-8').read().split('\n')[1:] if l}
out=[]; jd=[]
for l in open(B+'/TRANSCRIPTION.tsv',encoding='utf-8').read().split('\n')[1:]:
    if not l: continue
    p=l.split('\t'); d=dec_line(p[6],key)
    out.append('%s\tjolanka-%s\tR%s\tline %s\t%s'%('HELD-OUT' if p[5]=='1' else 'training',p[1],p[0],p[4],d))
    jd.append('%s j%s l%s: %s'%('H' if p[5]=='1' else 'T',p[1],p[4],d))
open(B+'/DECODE.txt','w',encoding='utf-8').write('\n'.join(out)+'\n'); open(B+'/judge/decode.txt','w',encoding='utf-8').write('\n'.join(jd)+'\n')
print('\n'.join(o for o in out if o.startswith('HELD')))

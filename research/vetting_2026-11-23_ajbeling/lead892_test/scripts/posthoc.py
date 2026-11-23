# POST HOC, not part of the hashed plan: relabel three signs the sign sheet linked to the wrong key description
# (U = KEY_BRIEF's Sh-like g; ^ = turned-y h of k367; ?? looped sign = q, not in the key), and rescore transcription 2.
import json
from common import *
import decode as D
V=dict(D.VAL); V['U']='g'; V['^']='h'; V['??']='q'
orig=D.value
def value(code,VV):
    if code=='??': return [{'q'}]
    return orig(code,VV)
D.value=value
T=load(O+'transcription_T2.txt'); words=D.reftext()
seq,_=D.decode(T,V); sc,match,got,ref=D.score(D.prep(seq),words)
pos=0; wr=0; nw=0
for w in words:
    if w=='sultanum': continue
    nw+=1; mm=match[pos:pos+len(w)]; pos+=len(w); wr+=all(mm)
print('post hoc T2 letters',round(sc,4),'words',wr,'/',nw)

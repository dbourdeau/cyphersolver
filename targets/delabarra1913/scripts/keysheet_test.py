"""Test the fondo's key sheet X-1.5.466.1 ("Abecedario y su clave") on the three telegrams, both directions."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
P = 'ABCDEFGHIJKLMNOPQRSTUVXYZW'
C = 'efaigbzchwdoptrmuxvsqjnlyk'
dec = dict(zip(C, P.lower()))   # cipher row -> plain
enc = dict(zip(P.lower(), C))   # the other direction
T = {'207': 'xcrxneb hfmnfdxm hfkhfmxh fvyxpxeoh uormbw zbwmoefhx',
     '239': 'lxzrx hxzob wfmyn fwxov chfmo bwmon',
     '310': 'bizp muhheiz omaznim borezi ojugehozim'}
for d, t in T.items():
    print(d, 'clave->plain:', ' '.join(''.join(dec.get(c, '?') for c in w) for w in t.split()))
    print(d, 'plain->clave:', ' '.join(''.join(enc.get(c, '?') for c in w) for w in t.split()))

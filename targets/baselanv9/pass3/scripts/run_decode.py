import sys,hashlib,re
R='/home/claude/fable25/basel_p2/'
sys.path.insert(0,R+'scripts')
import decode_p3 as d
frz=open(R+'FREEZE_P3.txt').read()
for f in ['KEY_V3.tsv','scripts/decode_p3.py','tx/f015r_p3.txt','tx/f025r_H4.txt','tx/PENT_S2.txt']:
    assert hashlib.sha256(open(R+f,'rb').read()).hexdigest() in frz, f
K=d.load_key(R+'KEY_V3.tsv'); out=['# PASS 3: ONE decode, KEY_V3.tsv + scripts/decode_p3.py (RULES_V3.md). "=" word broken at line end; [?] no value; ~ bar, not expanded. No emendation.']
for tag,f in [('H1r','tx/f015r_p3.txt'),('H4','tx/f025r_H4.txt'),('S2','tx/PENT_S2.txt')]:
    n=u=0
    for lid,dec in d.decode_file(R+f,K):
        t=' '.join(dec); out.append('%s %s\t%s'%(tag,lid,t)); n+=len(re.sub('[^a-z]','',t.replace('[?]',''))); u+=t.count('[?]')
    out.append('# %s: decoded letters %d, signs with no value %d'%(tag,n,u))
open(R+'DECODE_P3.txt','w').write('\n'.join(out)+'\n'); print('\n'.join(out))

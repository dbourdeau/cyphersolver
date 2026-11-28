"""Variant decode of the frozen pass 3 transcriptions with decoder rules C4 and/or C5 switched off. Own code, python3 -I.
usage: run_variant.py <basel_p2 folder> <variant folder>"""
import sys,re,hashlib,importlib.util
R,V=sys.argv[1].rstrip('/')+'/',sys.argv[2].rstrip('/')+'/'
frz=open(R+'FREEZE_P3.txt').read()
for f in ['KEY_V3.tsv','scripts/decode_p3.py','tx/f015r_p3.txt','tx/f025r_H4.txt','tx/PENT_S2.txt']:
    assert hashlib.sha256(open(R+f,'rb').read()).hexdigest() in frz, f
def load(p,name):
    s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
base=open(R+'DECODE_P3.txt').read().split('\n')
for mode in ['noC4','noC5','noC4C5']:
    d=load(V+'decode_p3_%s.py'%mode,'dv_'+mode); K=d.load_key(R+'KEY_V3.tsv')
    out=['# PASS 3 VARIANT %s: frozen KEY_V3.tsv and frozen transcriptions, decoder = scripts/decode_p3.py with %s switched off. Run AFTER the pass 3 decode and its judging; not a first pass.'%(mode,mode[2:])]
    for tag,f in [('H1r','tx/f015r_p3.txt'),('H4','tx/f025r_H4.txt'),('S2','tx/PENT_S2.txt')]:
        n=u=0
        for lid,dec in d.decode_file(R+f,K):
            t=' '.join(dec); out.append('%s %s\t%s'%(tag,lid,t)); n+=len(re.sub('[^a-z]','',t.replace('[?]',''))); u+=t.count('[?]')
        out.append('# %s: decoded letters %d, signs with no value %d'%(tag,n,u))
    open(V+'DECODE_P3_%s.txt'%mode,'w').write('\n'.join(out)+'\n')
    print('==',mode)
    for x,y in zip(base[1:],out[1:]):
        if x!=y: print('  was:',x); print('  now:',y)

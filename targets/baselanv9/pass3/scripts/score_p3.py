"""Solver's own strict count (NOT a separate judge), pass-2 judge's rules: word tag S (all letters S), E (one slip: 1 letter E, rest S), N (all letters N).
Only the words listed in TAGS are not S. Checks every tagged word exists in the decode; sums letters; prints full arithmetic."""
import re,sys,difflib
R='/home/claude/fable25/basel_p2/'
TAGS={ # (unit, word): tag, reason
('H1r L02','sactorum'):('E','n missing (sanctorum)'),('H1r L05','pmer'):('E','m added (per)'),('H1r L08','dimones'):('E','i for ae (daemones)'),
('H1r L09','situs'):('E','u for i (sitis)'),('H1r L11','baptisum'):('E','m missing (baptismum)'),('H1r L12','atundi='):('N','t for r and the word runs off the passage (arundinem)'),
('H4 L01','sugit'):('E','r missing (surgit)'),('H4 L03','nooen'):('E','o for m (nomen)'),('H4 L03','iestius'):('N','not understood'),
('H4 L04','ne[?]'):('N','hole'),('H4 L04','oni'):('E','m missing (omni)'),('H4 L06','emloo'):('N','two slips (eloe)'),
('H4 L07','ineffabale'):('E','a for i'),('H4 L08','uidelichet'):('E','ch for c'),('H4 L09','exel[?]us'):('N','hole and c missing'),
('H4 L09','ueus'):('E','r missing (uerus), or not understood'),('H4 L09','imsrael'):('E','m added'),('H4 L09','t[?]='):('N','hole'),
('H4 L10','rar'):('N','not understood'),('H4 L10','gerum'):('N','not understood'),
('S2 S2-02','mesteriosum'):('E','e for y'),('S2 S2-03','erus'):('E','u for i (eris)'),('S2 S2-04','trasiens'):('E','n missing'),
('S2 S2-05','caraton'):('N','name, not understood'),('S2 S2-05','mathoi'):('N','name, not understood'),
('S2 S2-08','ineffabale'):('E','a for i'),('S2 S2-08','periculus'):('E','u for i'),('S2 S2-09','ingribe'):('N','two slips (inscribe)'),
('S2 S2-09','commedendum'):('E','m doubled'),('S2 S2-10','mirabala'):('N','two slips (mirabili)'),('S2 S2-11','gribe'):('N','two slips (scribe)'),
('S2 S2-11','iouus'):('E','u for i'),('S2 S2-11','aurgento'):('E','u added'),('S2 S2-12','liberabiutur'):('N','two slips (liberabuntur)')}
used=set(); rows=[]; tot={}
for ln in open(R+'DECODE_P3.txt'):
    if ln.startswith('#') or '\t' not in ln: continue
    unit,txt=ln.rstrip('\n').split('\t'); sec=unit.split()[0]; s=e=n=0
    for w in txt.split():
        L=len(re.sub('[^a-z]','',w.replace('[?]','')))
        t=TAGS.get((unit,w),('S',''))[0]
        if (unit,w) in TAGS: used.add((unit,w))
        if t=='S': s+=L
        elif t=='E': e+=1; s+=L-1
        else: n+=L
    rows.append((unit,s,e,n,txt)); a=tot.setdefault(sec,[0,0,0]); a[0]+=s;a[1]+=e;a[2]+=n
assert used==set(TAGS), set(TAGS)-used
o=['unit\tS\tE\tN\tarithmetic\tshare\tdecode']
for u,s,e,n,t in rows: o.append('%s\t%d\t%d\t%d\t%d/(%d+%d+%d)=%d/%d\t%.1f%%\t%s'%(u,s,e,n,s,s,e,n,s,s+e+n,100*s/(s+e+n),t))
for k,(s,e,n) in tot.items(): o.append('TOTAL %s\t%d\t%d\t%d\t%d/(%d+%d+%d)=%d/%d\t%.2f%%\t'%(k,s,e,n,s,s,e,n,s,s+e+n,100*s/(s+e+n)))
o.append('# tags other than S:'); o+=['# %s | %s | %s | %s'%(k[0],k[1],v[0],v[1]) for k,v in TAGS.items()]
# sensitivity: H1r without C5 (christiana N 10; five ch~ri -> i~ri scored E each) and without C4 (parte -> pa[?]te, N 4 of 4 letters)
s,e,n=tot['H1r']; s2=s-10-5; o.append('# H1r without C5: S %d-10-5=%d, E %d+5=%d, N %d+10=%d -> %d/%d = %.2f%%'%(s,s2,e,e+5,n,n+10,s2,s+e+n,100*s2/(s+e+n)))
s3=s2-5; o.append('# H1r without C5 and C4 (parte 5 letters -> pate 4 letters, N): S %d, total %d -> %.2f%%'%(s3,s+e+n-1,100*s3/(s+e+n-1)))
# clear-copy match for H1r
clear=''.join(l for l in open('/home/claude/wt-basel/targets/baselanv9/score/CLEAR_H1_f109v.txt') if not l.startswith('#')).lower()
clear=re.sub(r'[\[\]]','',clear); clear=re.sub('[^a-z]','',clear.replace('v','u').replace('j','i'))
dec=''.join(t for u,s,e,n,t in rows if u.startswith('H1r')); dec=re.sub('[^a-z]','',dec.replace('[?]',''))
m=sum(b.size for b in difflib.SequenceMatcher(None,dec,clear,autojunk=False).get_matching_blocks())
o.append('# H1r against the clear copy f. 109v (letters only, u=v, i=j, abbreviations of the clear copy expanded as in its file): matched %d of %d clear letters = %.1f%%; decode letters %d'%(m,len(clear),100*m/len(clear),len(dec)))
open(R+'SCORE_P3.tsv','w').write('\n'.join(o)+'\n'); print('\n'.join(o))

"""Measure R5029: share of cipher groups read as sense.
A letter group counts when its run decodes to German words (checked word by word below and LM-scored with de-1740s);
a code group counts only in tier A (Mirka's list or a sibling gloss). Tier B bracket proposals are reported, not counted."""
import os,re,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
sys.stdout.reconfigure(encoding='utf-8')
from dec import k,A,B
from lang import lm
# letter runs -> word split as read (writer's slips noted)
SENSE={'MIR':'mir','NICHT':'nicht','EXCVSATIONZVMACHEN':'excusation zu machen','HALTET':'haltet','LIEBE':'liebe',
 'VERLIEHRET':'verliehret','DES':'des','ZV':'zu','ZVSEHE':'zusehe','VNSERAN':'unser an','VERLIEHRE':'verliehre',
 'SVCCESSION':'succession','NIEHEMAHLENANZVNEHMEN':'niemahlen anzunehmen','DIENSTEZV':'dienste zu','GETHAN':'gethan'}
runs=[];tot=let=a=b=op=0;openc={}
for line in open('ct.txt',encoding='utf8'):
  if line.startswith('#') or '|' not in line: continue
  body=re.sub(r'\[[^\]]*\]',' | ',line.split('|',1)[1])
  for seg in body.split('|'):
    w='';n_in=0
    for n in map(int,seg.split()):
      tot+=1
      if n<=48: w+=k[n]; n_in+=1; continue
      if w: runs.append((w,n_in)); w='';n_in=0
      if n in A: a+=1
      elif n in B: b+=1; openc[n]=openc.get(n,0)+1
      else: op+=1; openc[n]=openc.get(n,0)+1
    if w: runs.append((w,n_in))
sense_letters=sum(c for w,c in runs if w in SENSE); let=sum(c for w,c in runs)
bad=[w for w,c in runs if w not in SENSE]
m=lm.load('de-1740s')
txt=' '.join(SENSE[w] for w,c in runs if w in SENSE)
print('letter runs:',len(runs),'groups',let,'as sense',sense_letters,'not sense:',bad)
print('LM de-1740s per char of the letter-run readings: %.2f (gibberish ~ -6)'%m.per_char(lm.norm(txt,'modern')))
print('code groups: tier A %d, tier B (proposed, not counted) %d, open %d'%(a,b,op))
print('open/proposed codes:',dict(sorted(openc.items())))
r=(sense_letters+a)/tot
print('total groups %d; read as sense %d = %.3f; with tier B %.3f'%(tot,sense_letters+a,r,(sense_letters+a+b)/tot))

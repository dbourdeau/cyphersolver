# Alignment of the frozen blind transcription with the proposed plaintext (after PREREG decision).
import sys, json; sys.path.insert(0, __file__.rsplit('/',1)[0])
from prereg_measure import load, dec
import os, pathlib
_h = pathlib.Path(__file__).resolve().parent
_c = [a for a in sys.argv[1:] if a.endswith('.txt')] + [str(_h/'blind_transcription_frozen.txt'), str(_h.parent/'TRANSCRIPTION-AVEUGLE.txt')]
T = load(next(c for c in _c if os.path.isfile(c)))
# (telegram, key, [(plaintext per cipher word, offset shift applied from this word on)])
PLAN = {
 "T1": ("COMERETRIBUTION", [
  ("OF",0),("ATTACKING",0),("MOBILE",0),("DOING",0),("AT",0),("PENSACOLA",0),
  ("FORCED",1),("RECONNAISANCE",1),("MADE",1),("AT",1),("ONCE",1),("DIRECTION",1),("OF",1),("PENSACOLA",1),
  ("CAVALRY",1),("YOU",1),("NOW",1),("HAVE",1),("ON",1),("EASTERN",1),("SHORE",1),("SELMA",1),("AND",1),
  ("MONTG",1),("OMERY",1),("LINE",1),("AGAINST",1),("CENTRAL",1),("ALABAMA",1)]),
 "T2": ("COMPLETEVICTORY", [
  ("IN",0),("NORTH",0),("ALA",0),("LIKELY",0),("TO",0),("FALL",0),("INTO",0),("ENEMYS",0),("HAN",0),("DS",0),
  ("IN",0),("CASE",0),("OF",0),("MOVEMENT",0),("FROM",0),("TENNE",0),("RIVER",0),
  ("IN",0),("FORTIF",0),("IED",0),("PLACES",0),("OR",0),("SOUTH",0),("OF",0),("ALA",0),("RIVER",0),
  ("CAHABA",0),("PRIS",0),("ONERS",0),("TO",0),("ANDERSONVILLE",0),
  ("ENEMYS",0),("ADVANCE",0),("TOWARDS",0),("CEN",0),("TRAL",0),("ALA",0),("IF",0),("GOVMT",0),("EMPLOYEES",0),
  ("AT",0),("DEMOPOLIS",0),("DEPRIVING",0),("WORKSHOPS",0)]),
}
def enc(p,key,off): return ''.join(chr((ord(c)-65+ord(key[(i+off)%len(key)])-65)%26+65) for i,c in enumerate(p))
out={}
for t,(key,plan) in (PLAN.items() if __name__=='__main__' else []):
    words=T[t]; assert len(words)==len(plan),(t,len(words),len(plan))
    pos=0; tot=agree=0; rows=[]
    for w,(p,sh) in zip(words,plan):
        if len(w)!=len(p): rows.append((w,p,'LEN %d/%d'%(len(w),len(p)))); pos+=len(w); continue
        exp=enc(p,key,pos+sh); diff=[(i,w[i],exp[i]) for i in range(len(w)) if w[i]!=exp[i]]
        tot+=len(w); agree+=len(w)-len(diff)
        rows.append((w,p,' '.join(f'{a}->{b}' for _,a,b in diff) or 'ok'))
        pos+=len(w)
    out[t]={"key":key,"letters_compared":tot,"letters_agree":agree,"rows":rows}
    print(f"== {t} key {key}: {agree}/{tot} letters as read")
    for r in rows: print('  %-15s %-14s %s'%r)

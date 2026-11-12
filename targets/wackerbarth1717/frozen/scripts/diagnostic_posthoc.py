# DIAGNOSTIC POST-HOC, NON DÉCISIF (après MESURE.json ; A et P grillés). Explique la cause de l'ÉCHEC, ne change aucun verdict.
import sys, os, json, random, difflib
sys.argv=['x']; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
src=open(os.path.join(os.path.dirname(__file__),'mesure.py')).read().split('K = load_key()')[0]
exec(src)
K=load_key(); R=json.load(open(os.path.join(D,'MESURE.json')))
F=R['A']['F']; DA=R['A']['decodage']; nA=nums_of(os.path.join(REL,'A-CHIFFRE-0040.txt'))
def carD(F,Dd):
    sm=difflib.SequenceMatcher(None,F,Dd,autojunk=False); return sum(b.size for b in sm.get_matching_blocks() if b.size>=3)/len(Dd)
t=controls(K,lambda k: carD(F,dec(k,nA)),random.Random(1717))
print('A /|D| :',round(carD(F,DA),4),'max témoins',round(max(t),4))
LEX={w for w in json.load(open(LEXF)) if len(w)>=4}
cover=make_cover(LEX); import re
nB=[]
for line in open(os.path.join(REL,'B-REL22.txt'),encoding='utf-8'):
    m=re.match(r'[LMN]\d+ C: ?(.*)',line)
    if m: nB+=[v for k,v in tokens(m.group(1)) if k=='n']
nB=nB[:360]
s=cover(dec(K,nB))[0]; t=controls(K,lambda k: cover(dec(k,nB))[0],random.Random(1717))
print('B mots>=4 (lexique cyphersolver seul) :',round(s,4),'max témoins',round(max(t),4),'moy',round(sum(t)/200,4))

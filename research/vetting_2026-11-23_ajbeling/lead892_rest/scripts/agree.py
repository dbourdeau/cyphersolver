# Sign-by-sign agreement of T1 and T2 per item (aligned per line), after the same code-name normalisation as score.py.
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from score import load, fix, ITEMS
sys.path.insert(0,os.path.join(HERE,'..','..','lead892_test','scripts'))
from common import norm, align
T1=load(['transcription_T1_latin.txt','transcription_T1_italian.txt']); T2=load(['transcription_T2.txt'])
for item,(labels,_,_,_) in ITEMS.items():
    tot=same=0
    for k in labels:
        a=[norm(fix(t)) for t in T1[k]]; b=[norm(fix(t)) for t in T2[k]]
        for x,y in align(a,b): tot+=1; same+=(x==y)
    print(item,'aligned',tot,'agree',same,round(same/tot,3),'signs T1',sum(len(T1[k]) for k in labels),'T2',sum(len(T2[k]) for k in labels))

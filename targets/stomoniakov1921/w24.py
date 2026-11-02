"""Width-focused runs with independent restarts: python w24.py <w> <seed0> <seed1> <its>. Prints each run's score, order and start of text; writes jsonl."""
import sys,json
from joint import *
w,s0,s1,its=map(int,sys.argv[1:5])
M=load('msgA.txt')
for r in range(s0,s1):
    b=solve([M],w,its,r)
    print(json.dumps({'w':w,'seed':r,'score':round(b[0],3),'order':b[1],'text':show(M,b[1])}),flush=True)

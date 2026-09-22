import sys, bl, beam
from lang import lm
beam.M = lm.load('fr-1600-letters', order=5, spaces=False)
W = {'m':'nio','h':'inoq','C':'lrfs','l':'asl','j':'acpg','6':'ermd','n':'e','k':'iqa','x':'n','X':'t','%':'sy','M':'gn','U':'abcdefghilmnopqrstuv','K':'abcdefghilmnopqrstuv','Q':'abcdefghilmnopqrstuv','T':'l','8':'nbmt','1':'caor','y':'fcq','Z':'upr','z':'ilr','3':'dcl','q':'dqc',')':'sd','#':'uv','p':'cp','E':'uvr','w':'mh','r':'x','Y':'s'}
W.update({'y':'dfc','8':'mnb','k':'aiq','U':'xrabcdefghilmnopqstuv','6':'ermdn','%':'sygp','K':'i','j':'acpg'})
beam.CAND.update(W)
L = bl.lines(); out=[]
for i,(num,t) in enumerate(L):
    s,x,d = beam.beam((L[i-1][1]+['|'] if i else [])+t, width=1500)
    print(num, d.split('\n')[-1], round(s/len(x),2), flush=True)

# Scorer and decoder for the 1623 test. Run with python3 -I. Stated and frozen before the decode.
import re, sys, json, random, collections, os
BASE='/home/claude/hunts40/G3/M4/trackB'
CORPUS=['1068','1120','1132','1151','1156']
def norm(s):
    s=s.lower().replace('y','ij').replace('j','i').replace('v','u').replace('w','u')
    return re.sub(r'[^a-z]','',s)
def wordlist():
    c=collections.Counter()
    for n in CORPUS:
        for line in open(f'/home/claude/hunts40/G3/M4/dl_txt/{n}.txt',encoding='utf-8',errors='ignore'):
            if line.startswith('#'): continue
            for w in re.findall(r"[A-Za-zÀ-ÿ]+",line):
                w=norm(w)
                if w: c[w]+=1
    return {w for w,k in c.items() if k>=2}, c
def load_key(path=BASE+'/frozen/K1634_key.tsv'):
    k={}
    for l in open(path).read().splitlines()[1:]:
        n,v,_=l.split('\t'); k[int(n)]=v.split('/')[0]
    return k
def load_tokens(path=BASE+'/frozen/T1623_transcription.txt'):
    toks=[]
    for l in open(path):
        if l.startswith('#') or '|' not in l: continue
        blk,c=[x.strip() for x in l.split('|',1)]
        c=re.sub(r'\[[^\]]*\]','/',c).replace('{','').replace('}','')
        for w in c.split('/'):
            g=[int(x) for x in w.split()]
            if g: toks.append((blk,g))
    return toks
def decode(g,key): return ''.join(key.get(x,'?') for x in g)
def score(toks,key,W):
    read=0
    for _,g in toks:
        d=decode(g,key)
        if '?' not in d and norm(d) in W: read+=1
    return read
if __name__=='__main__':
    W,C=wordlist(); key=load_key(); toks=load_tokens()
    print('corpus types (freq>=2):',len(W),' corpus tokens:',sum(C.values()))

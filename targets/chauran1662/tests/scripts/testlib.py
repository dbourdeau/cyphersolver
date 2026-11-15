#!/usr/bin/env python3
import re, sys, csv, random, hashlib, unicodedata
sys.path.insert(0,'scripts')
from parse import parse
SHA='9619f6ef0896b5efd0b0b2a6b14dddd305df983b6b022249ac8b176c8e9cd029'
def load_table(path='key/table_v1.tsv',check=True):
    if check: assert hashlib.sha256(open(path,'rb').read()).hexdigest()==SHA,'table changed'
    T={};tier={}
    for r in csv.DictReader(open(path),delimiter='\t'):
        if r['tier']=='unsettled': continue
        T[r['group']]=r['value']; tier[r['group']]=r['tier']
    return T,tier
def gid(g):
    m=g['mark']
    if m in('D1','D2'): m='D3'
    return '%s%s'%(g['num'],(':'+m) if m else '')
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); s=''.join(c for c in s if unicodedata.category(c)!='Mn')
    s=s.replace('ç','c')
    s=re.sub(r'[^a-z0-9]','',s)
    s=s.replace('v','u').replace('y','i').replace('j','i')
    s=re.sub(r'z(?=[ei])','c',s)
    s=s.replace('h','')
    s=re.sub(r'(.)\1+',r'\1',s)
    return s
def gloss_clean(t):
    t=re.sub(r'\[[^\]]*\]|\([^)]*\)',' ',t or '')
    return norm(t)
def sections(path):
    """ordered dict sec -> list of records"""
    out={}
    for r in parse(path): out.setdefault(r['sec'],[]).append(r)
    return out
def shuffled(T,seed):
    ks=sorted(T); vs=[T[k] for k in ks]; random.Random(seed).shuffle(vs); return dict(zip(ks,vs))

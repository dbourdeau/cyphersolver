#!/usr/bin/env python3
"""Align pass 1 and pass 2 line by line; decode with frozen table_v1 (+ extension tsv if given).
usage: recdec.py pass1 pass2 [section-prefix-filter] [ext.tsv] ; prints decode and agreement stats to stderr"""
import sys,csv,difflib
sys.path.insert(0,'scripts')
from parse import parse
from testlib import load_table,gid
T,tier=load_table()
EXT={}
if len(sys.argv)>4 and sys.argv[4]:
    for r in csv.DictReader(open(sys.argv[4]),delimiter='\t'): EXT[r['group']]=r['value']
flt=sys.argv[3] if len(sys.argv)>3 else ''
def recs(p):
    d={}
    for r in parse(p):
        if r['groups'] and r['sec'].startswith(flt): d[(r['sec'].split(' (')[0],r['line'])]=r
    return d
A=recs(sys.argv[1]);B=recs(sys.argv[2])
def val(k):
    if k in T: return T[k]
    if k in EXT: return '{'+EXT[k]+'}'
    return '<'+k+'>'
def ids(r): return [gid(g) if g['num'] is not None else '?' for g in r['groups'] if not g['struck']]
tot=agree=0;cursec=None
for key in A:
    if key not in B: continue
    if key[0]!=cursec: cursec=key[0]; print('##',cursec)
    a=ids(A[key]);b=ids(B[key])
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False);out=[]
    for t,i1,i2,j1,j2 in sm.get_opcodes():
        if t=='equal':
            for k in a[i1:i2]: out.append(val(k).replace(' ','_'))
            agree+=i2-i1; tot+=i2-i1
        else:
            tot+=max(i2-i1,j2-j1)
            out.append('['+' '.join(val(k) for k in a[i1:i2])+' / '+' '.join(val(k) for k in b[j1:j2])+' |'+','.join(a[i1:i2])+'/'+','.join(b[j1:j2])+']')
    print('L'+key[1],' '.join(out))
print('agreement %d/%d = %.1f%%'%(agree,tot,100*agree/max(tot,1)),file=sys.stderr)

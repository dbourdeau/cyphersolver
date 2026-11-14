"""Recheck package measurements and frozen test totals; no network or writes.
Run from the repository root, with the same Python as the repository checkers (it needs NumPy):
  PYTHONUTF8=1 python targets/haldimand1783/verify.py
Do not use -I: isolated mode drops user site-packages, where NumPy often lives.
"""
from pathlib import Path
import csv,json,sys,importlib.util,collections,ast,re
T=Path(__file__).resolve().parent; ROOT=T.parents[1]
sys.path.insert(0,str(ROOT/'docs'))
import _check_profile as cp
s=importlib.util.spec_from_file_location('reading_score',ROOT/'research/reading_audit/v2_score.py')
v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
p=json.loads((T/'profile.json').read_text());rows=list(csv.DictReader((T/'lookup_occurrences.tsv').open(),delimiter='\t'))
for d,t in zip(p['documents'],p['outcome']['texts']):
 m=cp.measure(T/d['length']['file']); assert all(m[k]==d['length'][k] for k in ['tokens','distinct'])
 score=v.score(v.holes(v.body_of((T/t['reading']).read_text())),'en',True)
 assert abs(1-score['hole_rate']-t['read_share'])<1e-9
 assert all((T/t[k]).is_file() for k in ['transcription','decryption','reading','contemporary'])
 n=d['id'][-1]; rr=[x for x in rows if x['msg']=='No'+n]
 marks=collections.Counter(x['mark'] for x in rr)
 print(d['id'],m['tokens'],'code groups;',dict(marks),'dictionary-evidence items;',t['read_share'],'strict reading share;',t['state'])
 assert t['state']!='read'
raw=(T/'evidence/prereg_no4_result.txt').read_text();pages=ast.literal_eval(raw.splitlines()[0].split(': ',1)[1]);lemmas=ast.literal_eval(raw.splitlines()[1].split(': ',1)[1])
counts={k:sum(a+k in pages for a in lemmas.values()) for k in [0,-20,-10,-5,5,10,20]};assert counts=={0:8,-20:1,-10:1,-5:0,5:3,10:1,20:2};print('Frozen No.4 test inputs:',counts)
r=list(csv.DictReader((T/'evidence/edition_row_scores.tsv').open(),delimiter='\t'))
enc=sum(x['set'] in 'AB' and x['result'] in ['exact','exact-stem'] for x in r);gloss=sum(x['set']=='C' and x['result']=='exact' for x in r);assert(enc,gloss)==(96,3);print('Edition encoder exact/stem:',enc,'/107; gloss exact:',gloss,'/9')
a=[x for x in rows if x['msg']=='No3' and x['pair']=='218-11'];assert len(a)==1 and a[0]['reading']=='magnanimous'
assert not any(x['pair']=='216-11' for x in rows)
assert any(x['pair']=='[?sign]' for x in rows)
print('result: package checks passed (not an independent image or full-reading review)')

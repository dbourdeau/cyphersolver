# Score a decoder output for f135r against the aligned truth: per-token letter from the full alignment path.
__file__=__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__import__('sys').argv[0])),'align.py')
import sys,re,json,collections
src=open('align.py',encoding='utf8').read().split("pairs=[a.split(':')")[0]; exec(src)
k=json.load(open('key1573.json')); P=model({t:collections.Counter(c) for t,c in k['counts'].items()},collections.Counter(k['nulls']))
toks=read_ct('ct/f135r.txt'); pt=read_pt('pt/f139r_a.txt'); sc,path=align(toks,pt,P)
truth=[ (ch if mv=='emit' else None) for mv,tk,ch in path if tk is not None]
out=''.join(l.split('  ',1)[1].strip() for l in open(sys.argv[1],encoding='utf8') if l.strip())
out=re.sub(r'\[[^\]]*\]','',out).replace(' ','')
assert len(out)==len(truth),(len(out),len(truth))
ok=sum(1 for o,t in zip(out,truth) if t and o==t); n=sum(1 for t in truth if t)
print('letters correct %d/%d = %.3f'%(ok,n,ok/n))

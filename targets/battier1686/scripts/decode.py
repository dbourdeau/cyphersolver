"""usage: decode.py tok/<file>.txt   -> prints decoded lines; writes reading/<file>.tsv (prefilled; grade column blank)
Token grammar (space separated, one manuscript line per 'Lnn:' line):
  b:n        codebook group, block b (1=unmarked >=99; 2 ~,3 \\,4 ^,5 /,6 e,7 l,8 r,9 -,10 ..,11 1st digit struck,
             12 2nd digit struck,13 3rd digit struck,14 c/,15 reversed-c/,16 names-series)
  n          bare 2..98 = cipher letter
  v:x        vowel-substitute letter
  suffix ?   uncertain reading;  a|b alternatives (first = adopted)
  {text}     clear text / comment (not counted)
dict/*.tsv : token<TAB>value<TAB>source   (source 'key sNNX#' = read in key image; 'ctx' = context only)"""
import sys, glob, re, os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key'))
from letters import NUM, VOWEL_LETTER
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_dict():
    d={}
    for f in sorted(glob.glob(f'{D}/key/dict/*.tsv')):
        for line in open(f):
            if not line.strip() or line.startswith('#'): continue
            p=line.rstrip('\n').split('\t')
            if len(p)<2: continue
            tok,val=p[0].strip(),p[1].strip(); src=p[2].strip() if len(p)>2 else ''
            # later files override earlier ones (sorted: core < fA.. < hB.. < names < orch < zz_corrections)
            d[tok]=(val,'key' if src.startswith('key') else src)
    return d
def parse(fn):
    lines=[]
    for raw in open(fn):
        m=re.match(r'\s*(L\w+)\s*:\s*(.*)',raw)
        if not m: continue
        body=re.sub(r'\{[^}]*\}',' ',m.group(2))
        lines.append((m.group(1),body.split()))
    return lines
def val(tok,d):
    t=tok.split('|')[0].rstrip('?')
    if t.startswith('v:'): return VOWEL_LETTER.get(t[2:],'?'),'letter'
    if ':' not in t:
        try: n=int(t)
        except: return '??','bad'
        if 2<=n<=98: return NUM[n],'letter'
        t=f'1:{n}'
    if t in d: return d[t][0],d[t][1]
    return '[%s]'%t,'missing'
if __name__=='__main__':
    d=load_dict(); fn=sys.argv[1]
    base=os.path.basename(fn).replace('.txt','')
    out=open(f'{D}/readings/{base}.tsv','w') if '--write' in sys.argv else None
    i=0; miss=0; tot=0
    for ln,toks in parse(fn):
        words=[]; 
        for t in toks:
            i+=1; tot+=1; v,s=val(t,d)
            if s=='missing': miss+=1
            words.append(v if s!='letter' else v.upper())
            if out: out.write(f'{i}\t{ln}\t{t}\t{v}\t{s}\t\t\n')
        # join runs of single letters
        txt=''; prev_letter=False
        for w in words:
            isl=len(w)==1 and w.isupper()
            txt+= (w.lower() if isl and prev_letter else (' '+(w.lower() if isl else w)))
            prev_letter=isl
        print(f'{ln}: {txt.strip()}')
    print(f'# tokens {tot}, missing dict {miss}',file=sys.stderr)

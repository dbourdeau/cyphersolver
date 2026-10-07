"""decode.py : apply key (key_letters.tsv, key_words.tsv, key_codes.tsv) to june1676_tx.txt; print reading + stats"""
import re,sys,csv
from pathlib import Path
B = Path(__file__).resolve().parents[1]
def load(fn):
    d={}
    for l in open(B / 'key' / fn):
        if l.startswith('#') or not l.strip(): continue
        p=l.rstrip('\n').split('\t')
        d[p[0]]=(p[1],p[2] if len(p)>2 else '?',p[3] if len(p)>3 else '')
    return d
L=load('key_letters.tsv'); W=load('key_words.tsv'); C=load('key_codes.tsv')
# Reviewed values; the original tables retain their historical evidence bands.
for row in csv.DictReader(open(B / 'key' / 'corrections.tsv'), delimiter='\t'):
    code = row['code']
    table = W if code.endswith(':') else C
    table[code.rstrip(':')] = (row['reading'], row['legacy_band'], row['evidence'])
args = [a for a in sys.argv[1:] if not a.startswith('--')]
src = args[0] if args else 'june1676_tx.txt'
if '--selve' in sys.argv:
    C['g121'] = ('selve', 'M', '250 104L; uncertain gloss')
if '--exclude-later' in sys.argv:
    C['n155'] = ('genomen', 'I', 'Later-hand witness excluded')
    C['r157'] = ('recompense', 'M', 'Later-hand witness excluded')
out=[];stats={'H':0,'C':0,'M':0,'I':0,'?':0}
def grade(g): stats[g if g in stats else '?']+=1
for line in open(B / 'transcription' / src):
    if line.startswith('#') or not line.strip(): continue
    lid,rest=line.split(' ',1)
    rest=re.sub(r'~([^~]*)~',lambda m:'~'+m.group(1).replace(' ','_')+'~',rest)
    toks=re.findall(r'\[ins|\]|~[^~]*~|\{[^}]*\}(?:\^\w+)?|\d+:-?(?:\^\w+)?|[a-zA-Z]\d+(?:\^\w+)?',rest)
    res=[]
    for t in toks:
        if t in('[ins',']'): res.append(t); continue
        if t.startswith('~'): res.append(t[1:-1].replace('_',' ')); continue
        if t.startswith('{'):
            m=re.match(r'\{([^}]*)\}(?:\^(\w+))?',t); nums=m.group(1).split(','); sfx=m.group(2) or ''
            s='';gs=[]
            for n in nums:
                v=L.get(n.strip(),('?','?'))
                s+=v[0]; gs.append(v[1])
            g='H' if all(x=='H' for x in gs) else ('?' if '?' in gs else max(gs,key='HCMI'.index))
            grade(g); res.append(f'<{s}{sfx}>' + ('' if g=='H' else f'[{g}]'))
            continue
        m=re.match(r'(\d+):(-?)(?:\^(\w+))?$',t)
        if m:
            v=W.get(m.group(1),('?'+m.group(1)+':','?'))
            grade(v[1]); res.append(f'{v[0]}{m.group(2)}{m.group(3) or ""}'+('' if v[1]=='H' else f'[{v[1]}]')); continue
        m=re.match(r'([a-zA-Z])(\d+)(?:\^(\w+))?$',t)
        k=m.group(1).lower()+m.group(2)
        v=C.get(k,('?'+k,'?'))
        grade(v[1]); res.append(f'{v[0].upper() if False else v[0]}{("+"+m.group(3)) if m.group(3) else ""}'+('' if v[1]=='H' else f'[{v[1]}]'))
    out.append(f'{lid} '+' '.join(res))
print('\n'.join(out))
tot=sum(stats.values()); print('\nTOKENS',tot,stats, 'legacy-band H+C+M=%.2f%%'%(100*(stats['H']+stats['C']+stats['M'])/tot), 'H+C=%.1f%%'%(100*(stats['H']+stats['C'])/tot))

print('Bands follow the historical tables; see NOTES.md for the reviewed fractions and sense limits.')

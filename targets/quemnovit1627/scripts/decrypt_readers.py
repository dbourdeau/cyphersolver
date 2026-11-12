# decrypt_readers.py: line-by-line decryption of each reader's transcription with key_B.txt (unit=decode).
# Reader 2 and 3 signs mapped to KEY_B labels by their own frozen MAPPING files. '?' = sign with no key value; '#' = code sign.
import os,re,json
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(R,*a)
key={}
for l in open(P('key_B.txt')):
    if l.startswith('#'): continue
    for x in l.split(): a,b=x.split('='); key[a]=b
def d(u,m={}): return ''.join(key.get(m.get(c,c),'?') for c in u if c!='-')
with open(P('decryptions','reader1.txt'),'w',encoding='utf-8') as f:
    f.write('# Reader 1 (b97) frozen transcription decrypted with key_B.txt; clear German in <..>; codes as numbers\n')
    for l in open(P('transcriptions','reader1_frozen.txt'),encoding='utf-8'):
        m=re.match(r'^(\d\d) (.*)',l)
        if not m: continue
        parts=re.split(r'(<[^>]*>)',m.group(2).rstrip('\n'))
        o=[]
        for p in parts:
            if p.startswith('<'): o.append(p); continue
            o+=[w if w.strip('-').isdigit() else '%s=%s'%(w,d(w)) for w in p.split()]
        f.write(m.group(1)+' '+' '.join(o)+'\n')
M2={'N':'P','0':'H','z':'S','g':'q','y':'q','x':'k','u':'?'}
with open(P('decryptions','reader2_blind.txt'),'w',encoding='utf-8') as f:
    f.write('# Reader 2 (b129, blind) decrypted with key_B.txt after mapping (reader2_mapping.md); #H #E #W code tokens\n')
    for l in open(P('transcriptions','reader2_blind.txt'),encoding='utf-8'):
        if l.startswith('L'): f.write(l[:3]+' '+' '.join(w if w.startswith('#') else '%s=%s'%(w,d(w,M2)) for w in l.split()[1:])+'\n')
MAP3={'P':'P','O':'H','S':'s','Z':'Z','g':'g','q':'q','c':'c','e':'e','d':'d','L':'L','l':'l','a':'a','b':'b','f':'f','h':'h','i':'i','k':'k','m':'m','o':'o','p':'p','r':'r','t':'t'}
U3=json.load(open(P('decryptions','reader3_blind.json'),encoding='utf-8')); k=0
with open(P('decryptions','reader3_blind.txt'),'w',encoding='utf-8') as f:
    f.write('# Reader 3 (b137, blind) decrypted with key_B.txt after mapping (reader3_mapping.md); _ = sign without a mapped value; # = code sign H\n')
    for l in open(P('transcriptions','reader3_blind.txt'),encoding='utf-8'):
        if not l.startswith('L'): continue
        n,b=l.split(':',1); o=[]
        for w in re.sub(r'\[[^\]]*\]',' ',b).split():
            w=w.rstrip('.')
            if not w: continue
            pl=''.join('#' if c=='H' else (key[MAP3[c]] if c in MAP3 else '_') for c in w if c!='?')
            assert pl==U3[k]['plain'],(w,pl,U3[k]); k+=1
            o.append('%s=%s'%(w,pl))
        f.write(n+' '+' '.join(o)+'\n')
assert k==len(U3)
print('written; reader 3 decode equals decode_r3.json on all %d units'%k)

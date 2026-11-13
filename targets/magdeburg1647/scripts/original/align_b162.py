# align.py mine.txt b160.txt : word alignment (difflib) + letter confusions on same-length paired words
import sys,re,difflib,collections
def W(f): return [re.sub('[^a-z]','',w.lower()) for l in open(f) if not l.startswith('#') for w in l.replace('|',' ').split() if re.sub('[^a-z]','',w.lower())]
a,b=W(sys.argv[1]),W(sys.argv[2]); sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
eq=0; pairs=[]; conf=collections.Counter(); lm=lt=0; un=[]
for op,i1,i2,j1,j2 in sm.get_opcodes():
    if op=='equal': eq+=i2-i1
    elif op=='replace' and i2-i1==j2-j1:
        for x,y in zip(a[i1:i2],b[j1:j2]): pairs.append((x,y))
    else: un.append((op,a[i1:i2],b[j1:j2]))
for x,y in pairs:
    if len(x)==len(y):
        for p,q in zip(x,y):
            lt+=1; lm+=p==q
            if p!=q: conf[(p,q)]+=1
print(f'mine {len(a)} words, b160 {len(b)} words; exact-equal aligned words {eq}; agreement {eq}/{len(a)} = {eq/len(a):.2%} (of mine), {eq}/{len(b)} = {eq/len(b):.2%} (of b160)')
print(f'paired differing words {len(pairs)}; same-length pairs letters agree {lm}/{lt}')
print('top confusions mine->b160:',conf.most_common(12))
for x,y in pairs: print('  DIFF',x,'|',y)
for u in un: print('  UNALIGNED',u)

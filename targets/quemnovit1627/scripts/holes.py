# holes.py: lists every unit of the adjudicated (majority) decode that is not S, with the cause, from decryptions/adjudicated.txt
# and reader 1's units. Prints a markdown table and the tally by cause.  python3 -I scripts/holes.py
import os,collections
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); P=lambda *a: os.path.join(R,*a)
ad=[l.rstrip('\n').split('\t') for l in open(P('decryptions','adjudicated.txt'),encoding='utf-8') if not l.startswith('#')]
segs=[l.rstrip('\n').split('|') for l in open(P('transcriptions','reader1_units.seg'),encoding='utf-8') if not l.startswith('#')]
assert len(ad)==len(segs)==103
rows=[];tally=collections.Counter()
for a,s in zip(ad,segs):
    if a[4]=='S': continue
    r1=s[1].replace('-',''); m=a[2]
    if r1.isdigit(): cause='code number (no value)'
    elif s[3]=='E': cause="reader 1's own emendation (one sign)"
    else:
        diffs=[(x,y) for x,y in zip(r1.replace('L','l').replace('h','S'),m) if x!=y]
        kinds=set()
        for x,y in diffs:
            if x=='g': kinds.add('g/q class')
            elif x=='e' and y in 'c?': kinds.add('c/e class')
            elif x=='Z': kinds.add('pi/Z/n class')
            else: kinds.add('other sign (%s/%s)'%(x,y))
        cause=' + '.join(sorted(kinds))
    key='g/q class' if 'g/q class' in cause else cause.split(' + ')[0]
    tally[key]+=1
    rows.append((a[0],s[1],s[2],s[3],m,a[3],a[4],cause))
print('| Line | Reader-1 unit | Reader-1 decode (label) | Majority signs | Majority decode | Label | Cause |')
print('|---|---|---|---|---|---|---|')
for r in rows: print('| %s | `%s` | %s (%s) | `%s` | %s | %s | %s |'%r)
print('\nTally by cause (a unit with g/q and another cause is counted under g/q):')
for k,v in sorted(tally.items(),key=lambda x:-x[1]): print('- %s: %d'%(k,v))
print('- total not S: %d; S: %d; check %d + %d = %d'%(len(rows),103-len(rows),len(rows),103-len(rows),103))

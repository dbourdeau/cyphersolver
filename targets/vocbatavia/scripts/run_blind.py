# Blind decode of the 1640 letter with KEY_v2, scored with trackB score.py unchanged. Run once: python3 -I run_blind.py
import sys, random, difflib, re, glob
sys.path.insert(0,'/home/claude/hunts40/G3/M4/trackB/scripts')
import score as S
B='/home/claude/hunts40/G3/M4/blindtest'
W,C=S.wordlist(); key=S.load_key('/home/claude/hunts40/G3/M4/trackB/keyv2/KEY_v2.tsv')
toks=S.load_tokens(B+'/frozen/T1640_transcription.txt')
print('wordlist types',len(W),'| key numbers',len(key))
groups=[x for _,g in toks for x in g]
cov=sum(1 for x in groups if x in key)
print(f'tokens {len(toks)}; groups {len(groups)}; groups keyed {cov}; coverage {cov}/{len(groups)} = {100*cov/len(groups):.2f}%')
unk=sorted({x for x in groups if x not in key}); print('numbers not in key:',unk, '| occurrences:',sum(1 for x in groups if x not in key))
rows=[]
for b,g in toks:
    d=S.decode(g,key); ok=('?' not in d and S.norm(d) in W); rows.append((b,' '.join(map(str,g)),d,ok))
for blk in sorted({r[0] for r in rows}):
    t=[r for r in rows if r[0]==blk]
    print(blk,' '.join(r[2] for r in t)); print('   block score',sum(r[3] for r in t),'/',len(t))
real=sum(r[3] for r in rows)
print(f'REAL score (figure of record): {real}/{len(toks)} = {100*real/len(toks):.2f}%')
with open(B+'/decode_1640_firstpass.tsv','w') as f:
    f.write('block\tgroups\tdecode\treads_as_sense(corpus)\n')
    for r in rows: f.write('\t'.join(map(str,r))+'\n')
nums=sorted(key); vals=[key[n] for n in nums]
for seed in (20261112,7):
    rng=random.Random(seed); ge=0; best=0; tot=0
    for i in range(5000):
        v=vals[:]; rng.shuffle(v); k=dict(zip(nums,v)); s=S.score(toks,k,W); tot+=s; best=max(best,s)
        if s>=real: ge+=1
    print(f'seed {seed}: shuffles >= real: {ge}/5000; max shuffle {best}; mean {tot/5000:.2f}')
for f in sorted(glob.glob(B+'/frozen/BLIND2_*.txt')):
    bt=S.load_tokens(f); bl=[x for _,g in bt for x in g]
    sm=difflib.SequenceMatcher(a=groups,b=bl,autojunk=False); m=sum(x.size for x in sm.get_matching_blocks())
    print(f'second transcription {f.split("/")[-1]}: {m} matching; frozen {len(groups)}, second {len(bl)}; {m}/{max(len(groups),len(bl))} = {100*m/max(len(groups),len(bl)):.1f}%')

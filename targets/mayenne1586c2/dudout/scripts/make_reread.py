"""Build the re-read transcription of f. 120r-v from Harumi-Matsuba's, applying the sign-by-sign corrections made on
Gallica views 246-247 (12 Nov 2026). Lines not in the re-read set are copied unchanged."""
import re, sys
src_r, src_v, out = sys.argv[1:4]
CHG = {  # (page, line): {token_index_1based: (old, new)}
 ('r',15): {21: ('r','vbar')},
 ('r',16): {9: ('g','g8'), 11: ('f','g')},
 ('r',27): {1: ('r','vbar')},
 ('r',28): {7: ('w','w2')},
 ('r',30): {1: ('B','6b')},
 ('r',31): {2: ('9','q+')},
 ('v',5):  {2: ('ls','S')},
}
REREAD = {('r',k) for k in list(range(15,20))+list(range(24,32))} | {('v',k) for k in (3,4,5)}
lines=[]
for page,p in (('r',src_r),('v',src_v)):
    for raw in open(p,encoding='utf-8'):
        m=re.match(r'^c(\d+):\s*(.*)$',raw.rstrip('\n'))
        if not m: continue
        k=int(m.group(1)); toks=m.group(2).split()
        # token indices count only cipher tokens (not ^(...) superscripts, not {struck})
        idx=[i for i,t in enumerate(toks)]
        ch=CHG.get((page,k),{})
        if ch:
            # recompute indices ignoring superscript groups
            plain=[]; i=0
            while i<len(toks):
                t=toks[i]
                if t.startswith('^('):
                    j=i
                    while not toks[j].endswith(')'): j+=1
                    i=j+1; continue
                if t.startswith('{'): i+=1; continue
                plain.append(i); i+=1
            for n,(old,new) in ch.items():
                pos=plain[n-1]
                assert toks[pos]==old,(page,k,n,toks[pos],old)
                toks[pos]=new
        tag='R' if (page,k) in REREAD else '-'
        lines.append(f"{page}{k:02d} {tag}: {' '.join(toks)}")
open(out,'w',encoding='utf-8').write(
"# fr. 15573 f. 120r-v, re-read transcription (12 Nov 2026, Claude Opus 5.5 for Brice Dudout).\n"
"# Base: Harumi-Matsuba transcription_f120r/v.txt (CC BY 4.0), sign names unchanged; R = line re-read sign by sign on\n"
"# Gallica btv1b90618780 views 246-247 (openapi IIIF, full resolution); - = copied unchanged. New names: vbar (v with\n"
"# a bar below), g8 (8-shaped g with a dot). Doubtful signs: DOUTES.md. Frozen by SHA-256 before decoding.\n"
+'\n'.join(lines)+'\n')
print(len(lines))

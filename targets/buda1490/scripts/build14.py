"""build14: reading.md, latin.md, measure.txt from measure14.json (round 6)."""
import json,re,collections
from dec14 import units,lines,dec
k=json.load(open('key14.json')); M=json.load(open('measure14.json'))
T={h:t for h,t in lines()}; NR=collections.defaultdict(list)
for h,w,n,why in M['notread']: NR[h].append(f'{w} ({why})')
LA=dict((h,la) for h,la in M['latin'])
with open('reading.md','w') as f:
    f.write('# Line-by-line reading, DL 46150 (round 6: p1r-p4r.txt after R6 image repairs, key14.json = key_final.json, dec14.py)\n')
    f.write('Decrypt: `U` = oo/ooA/ooB (u or s), `W` = qB (u, s or f), `S` = s (h or f), `#` = code group v-e-D/x or sign without value (8C, wL, Ob, Bd, sl, fo), `_` = lost sign. `[?]` not read strictly; `[...]` unread. Figures: measure.txt.\n')
    for h,t in lines():
        if h.endswith('L01'): f.write(f'\n## Page {h[1]}\n')
        f.write(f"\n**{h}**\n- signs: `{' '.join(t)}`\n- decrypt: `{dec(k,units(t))}`\n- Latin: {' '.join(LA[h])}\n")
        if NR[h]: f.write('- not read: '+'; '.join(NR[h])+'\n')
def cont(p):
    w=[x for h,_ in lines() if h[:2]==p for x in LA[h]]
    w=[x.lstrip('-') for i,x in enumerate(w) if not (i+1<len(w) and w[i+1].startswith('-'))]
    s=' '.join(w)
    s=re.sub(r'(\[\.\.\.\]\s*)+','[...] ',s); s=re.sub(r'(\S+?)-\s+-(\S+)',lambda m:m.group(2) if True else '',s)
    return s
with open('latin.md','w') as f:
    f.write('# Continuous Latin (round 6)\n\n[In christo pater et domine pater honorande.]\n\n`[?]` = word not read strictly (see reading.md); `[...]` = unread. A word split over a line end is given once, in its full form.\n')
    for p in ['P1','P2','P3','P4']: f.write(f'\n## Page {p[1]}\n\n'+cont(p)+'\n')
with open('measure.txt','w') as f:
    f.write('Round 6 measure (measure14.py on ann14.txt, dec14.py, key14.json = key_final.json). Strict: ~, [?], poly-ambiguous and damage words are NOT read.\n')
    f.write('Polyphonic signs: oo/ooA/ooB = u/s (majority u), qB = u/s/f (majority u), s = h/f (majority h). A read word with such a sign counts only if no other choice gives another lexicon word (poly-ambiguous = 0).\n"depend on a minority value" = read words where at least one polyphonic sign takes its minority value; "read-without-any-minority-value" is the floor if all minority values were wrong.\nRound 5 (key13): words 544, read-strict 411 (75.6%); tokens 74.9%. Word total fell 544 -> 539 because aN and K became nulls (unread brackets [e], [i] x2 disappear) and some brackets merged.\n\n')
    f.write('\n'.join(M['res'])+'\n\nRead words that depend on a minority polyphonic value:\n'+'\n'.join(f'{a} {b} {",".join(c)}' for a,b,c in M['minority'])+'\n')
    f.write('\n'.join(M['res'])+'\n\nNot read (line, word, est. words, cause):\n')
    for r in M['notread']: f.write(' '.join(map(str,r))+'\n')

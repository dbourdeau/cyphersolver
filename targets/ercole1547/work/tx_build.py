import sys,re
M={'L':'S01','n':'S02','g':'S03','9':'S04','d':'S05','TH':'S06','7':'S07','DL':'S08','b':'S09','r':'S10','y':'S11','h':'S12','m':'S13','p':'S14','GA':'S15','4':'S16','2':'S17','PI':'S18','c':'S19','BE':'S20','s':'S21','UP':'S22','8':'S23','0':'S24','e':'S25'}
out=['# ercole1547: Ercole II d\'Este to secretary Claudio, Ferrara 8 Jan 1547. Estense, Autografoteca Campori, Ercole II, sfasc. I, c. 16v.','# Blind transcription (no key exists), one reader (Claude Fable 5.2) on native-resolution IIIF crops, 24 Nov 2026.','# page<TAB>line<TAB>tokens. Sxx = drawn sign (SIGNS.md). ^m = raised mark on that sign. "." = dot on the line. ? = doubtful. {..} = punctuation.','page\tline\ttokens']
for l in open(sys.argv[1]):
    if l.startswith('#') or not l.strip(): continue
    pg,ln,t=l.rstrip('\n').split('\t')
    toks=[]
    for tok in t.split():
        if tok.startswith('{') or tok in ('.','.?'): toks.append(tok); continue
        m=re.match(r'^([A-Za-z0-9]+?)(\?)?(\^[^?]+)?(\?)?$',tok)
        b,q1,s,q2=m.groups()
        toks.append(M[b]+(q1 or '')+(s or '')+(q2 or ''))
    out.append('%s\t%s\t%s'%(pg,ln,' '.join(toks)))
open(sys.argv[2],'w').write('\n'.join(out)+'\n')

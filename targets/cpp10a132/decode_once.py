"""One decode of the frozen transcription with the frozen key. No emendation."""
import re, hashlib
D='/home/claude/keyless/cpp10a132/'
key={}
for ln in open(D+'KEY.tsv').read().splitlines()[1:]:
    c,p,_=ln.split('\t'); key[c]=p
HELD={'p76v'}
tok=re.compile(r'\{[^}]*\}|<S\d\d>|\[\.+\]|\?|[A-Za-z]|[./ ]')
out=[]; jud=[]; stats={}
for ln in open(D+'TRANSCRIPTION.tsv').read().splitlines()[1:]:
    page,line,t=ln.split('\t'); s=''; n=0; und=0; lost=0; doubt=0
    for m in tok.findall(t):
        if m.startswith('{'): s+=m
        elif m.startswith('<'): s+='#'; und+=1            # drawn sign, no key value
        elif m.startswith('['): s+='_' if m=='[.]' else '~'; lost+=1
        elif m=='?': doubt+=1                               # doubt flag on previous letter: letter kept as transcribed
        elif m.isalpha(): s+=key[m.lower()]; n+=1
        else: s+=m
    st=stats.setdefault(page,[0,0,0,0,0]); st[0]+=1; st[1]+=n; st[2]+=und; st[3]+=lost; st[4]+=doubt
    out.append(f"{page}\t{line}\t{'HELD-OUT' if page in HELD else 'train'}\t{s}")
    jud.append(f"{page} l.{line}{' [held-out]' if page in HELD else ''}: {s}")
h=lambda f: hashlib.sha256(open(D+f,'rb').read()).hexdigest()
hdr=[f"# DECODE cpp10a132: one pass, frozen key sha256 {h('KEY.tsv')[:16]}.., frozen transcription sha256 {h('TRANSCRIPTION.tsv')[:16]}..",
     "# marks: {..} clear numeral as written; # drawn sign with no key value; _ one illegible letter; ~ lost (blot or gutter); . / scribe's points",
     "# page\tline\tsplit\tdecoded"]
open(D+'DECODE.txt','w').write('\n'.join(hdr+out)+'\n')
open(D+'judge/decode.txt','w').write('\n'.join(jud)+'\n')
tot=[0]*5
print('page   lines letters undecoded-signs lost-marks doubt-flags')
for p,st in stats.items():
    print(p,*st); tot=[a+b for a,b in zip(tot,st)]
print('TOTAL',*tot)

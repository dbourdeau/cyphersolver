# decode the frozen transcription once with the frozen key -> DECODE.txt, judge/decode.txt
import re,os
W='/home/claude/keyless/ostermann1737/'
key={}
for l in open(W+'KEY.tsv').read().split('\n')[1:]:
    if l: f=l.split('\t'); key[f[0]]=f[2]
HELD={17,18,19,20}
out=[];j=[]
for l in open(W+'TRANSCRIPTION.tsv').read().split('\n')[1:]:
    if not l: continue
    p,ln,t=l.split('\t'); ln=int(ln); words=[]
    t=re.sub(r'\{[^}]*\}',lambda m:'{'+m.group(0)[1:-1].replace(' ','_')+'}',t)
    for g in t.split('|'):
        w=''
        for k in g.split():
            if k.startswith('{'): w+=k.replace('_',' ')+' '
            elif k=='[...]': w+='[...]'
            else:
                v=key[k.rstrip('?')]
                w+=(' '+v+' ' if v in ('/','//') else v)
        words.append(re.sub(r'\s+',' ',w).strip())
    s=' '.join(words)
    out.append('%2d%s\t%s'%(ln,' H' if ln in HELD else '  ',s)); j.append('%d\t%s'%(ln,re.sub(r'\{[^}]*\}\s*','',s)))
open(W+'DECODE.txt','w').write('# line (H = held-out), decode with frozen KEY.tsv; gaps as transcribed; / = divider sign, // = flourish; {} = clear text on the leaf\n'+'\n'.join(out)+'\n')
os.makedirs(W+'judge',exist_ok=True); open(W+'judge/decode.txt','w').write('\n'.join(j)+'\n')
print('\n'.join(out))

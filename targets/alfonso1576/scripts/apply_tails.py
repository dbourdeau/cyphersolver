# Pass 3 of cc. 76-77. Splits the q-form into q (straight tail with foot) and g (looped tail) from
# work/tails/tails_final.tsv, applies the corrections of c. 76r l. 2, adds the two insertions above the line,
# and rewrites transcription and decryption. No value is chosen by sense here.
import re
T={int(l.split()[0]):l.split()[2] for l in open('work/tails/tails_final.tsv').read().splitlines()[1:]}
K={'a':'e','z':'a','o':'i','m':'o','p':'n','n':'l','B':'t','f':'r','t':'c','s':'d','v':'u','l':'p','c':'g','d':'h','e':'q','u':'b','b':'f','7':'7','i':'z','q':'m','g':'s'}
NUL=set('xyk&3')
src=[l for l in open('work/transcription_cc76-77_pass2.txt',encoding='utf8') if not l.startswith('#')]
k=0;out=[]
for l in src:
    n,s=l.split(None,1);s=s.strip();r=''
    for c in s:
        if c=='q':
            r+='g' if T[k]=='L' else 'q';k+=1
        else: r+=c
    s=r
    if n=='f76r.02':
        assert s[24]=='l' and s[41:43]=='ao',s[38:46]
        s=s[:24]+'f'+s[25:42]+'B'+s[42:]
    if n=='f77r.09':
        assert s.endswith('mpafz'); s=s[:-2]+'{vmo}fz'
    if n=='f77r.P2':
        i=s.index('Bzpiatda')+len('Bzpia'); s=s[:i]+'{lczbnozfsa}'+s[i:]
    out.append((n,s))
assert k==339
H=["# Catalogue 1566: Alfonso II d'Este, 14 Apr 1576, Autografoteca Campori, Lettera E, cc. 76-77",
"# Signs as read, no word division. Line labels: page, line. P1-P4 = postscript on c. 77r.",
"# Letter labels are the Latin letters the clerks wrote, except: B = the tall 5-shaped secretary h.",
"# q = q with a straight tail ending in a short foot. g = q-form whose tail sweeps left and back up in a large loop.",
"# x y k & 3 = nulls. # = sign lost under a blot. 7 = the digit 7, written as a digit inside the cipher.",
"# Text in {} was written above the line, at a caret, and belongs at that place.",
"# c. 76r l. 2: the B after 'ma' is a tall sign squeezed in between a and o."]
open('transcription_cc76-77_1576-04-14.txt','w',encoding='utf8').write('\n'.join(H+[f'{n}  {s}' for n,s in out])+'\n')
D=["# Letter-for-letter decryption of cc. 76-77 with key_1576.tsv. Top line signs, lower line letters.",
"# . = null. ? = blot. Every letter follows the key with no choice made; q and g are separate signs. No letter here has been repaired."]
tot=nul=0
for n,s in out:
    L=''
    for c in s:
        if c in '{}': L+=c;continue
        tot+=1
        if c in NUL: L+='.';nul+=1
        elif c=='#': L+='?'
        else: L+=K[c]
    D+= [f'{n}  {s}',' '*len(n)+'  '+L]
open('decryption_cc76-77_1576-04-14.txt','w',encoding='utf8').write('\n'.join(D)+'\n')
print('signs',tot,'nulls',nul,'g',sum(s.count('g') for _,s in out),'q',sum(s.count('q') for _,s in out))

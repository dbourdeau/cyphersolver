# builds TRANSCRIPTION.tsv and SIGNS.md from the working reading (mnemonic -> neutral S-label)
import collections
W='/home/claude/keyless/ostermann1737/'
signs=[
('V','cursive Cyrillic В with closed loops (same shape as the В of the clear "Въ цѣлости")'),
('b','б / open 6 with a top flag, no lower inner loop'),
('W','ш: three minims on a base bar'),
('U','two minims on a base bar, no tail (и/u-like)'),
('C','ц: two minims on a base bar with a hooked tail below'),
('w','wavy w (two rounded humps, entry hook at left)'),
('+','plus / small cross'),
('y','small 8 with an open, forked top (ꙋ-like), x-height'),
('8','closed digit 8, full height'),
('4','digit 4'),
('2','digit 2'),
('3','3 with a hooked top (ӡ)'),
('5','digit 5, often with a flag like an apostrophe'),
('9','9 / g with a descender'),
('v','small ѵ / ч-like tick (short stem, hook to the right), mostly before T or W'),
('T','т in the three-minim cursive form with a top bar'),
('a','а'),
('p','п with a flat top bar'),
('n','rounded n (no top bar)'),
('r','р with a long descender'),
('F','bold circled sign, Ф / Ѳ-like with a tail'),
('D','tall closed oval on a stem (ϑ-like)'),
('A','angular Д / A-shape with a descending left foot'),
('G','tall Г with a top flag (J-like foot)'),
('e','є (open e)'),
('l','long slanted stroke descending below the line (ſ-like); possibly a divider'),
('q','ψ: three-pronged fork with tail'),
('Y','large У: two-pronged fork with tail'),
('o','small o'),
('x','small plain x'),
('X','x with a top bar / serifed (larger than x)'),
('L','tall Л/M-like sign with a looped ascender'),
('Z','line-end flourish like "ээ" with a long dash; probably a stop or filler'),
]
lab={m:'S%02d'%(i+1) for i,(m,_) in enumerate(signs)}
lines={
1:"{Въ цѣлости} l w + V W y W C F U | y U 3 U | p C U 5 W a D G 8 D | w 8 9 U r W Z",
2:"8 w W r W | w U w + | e W 4 8 y G + | y W a V W | b W 4 y p W C X 4 + D y G + | b C U X w 8 U",
3:"n V + 5 F l + 9 y W | b W 2 a U | y W r W | 5 4 U 2 x | 2 b W C 2 8 G V 8 v T | b W 2 a W v T",
4:"b C W 8 2 | e W 4 8 a W | p V W w o U C U w? G 8 q e T | W y U e T | b C 8 a + r + D y G + Z",
5:"b C 8 2 U v T | b C W y W V W a F | b W 2 W 4 U C X + w 8 D | V W y W C F | e T T? l",
6:"y F | p b? W y C U 3 w W v T | 2 a n 9 + W | b W 2 y n b + y x | 8 v W U A T l w W | b W w U l",
7:"X U | b W C 2 8 G V W 8 | b W 2 W a T | w U W 4 w W | V C + y w W | 4 W v W r + a 2 q",
8:"n w + A U r W | p 8 G U | V + w G a U C + | 9 y W 3 T | W w T Y 2 U 3 q | V A + e n | b 8? 2 + {sup. flourish}",
9:"8 e W y q | p y W v T | w 8 V + V W 8 | w n X 4 F | w U n 2 v W y C q a W 2 x | W 4 w + l",
10:"V W X T | p W n 4 W p W a 2 y p 8 U | b W 2 a n | W w T | p 8 G U | V + w G a U C T {flourish}",
11:"b W n V + 5 n | w + A U v n | y W | n 9 8 w 8 a T l | 2 V W y W C W r W | b C 8 2 U v T | y U 3 U l",
12:"V W b 8 q | 2 W W 3 | L + U y 2 q | r 4 U | n 2 v W y C 8 A T | 9 y W | p W p 2 U v T Z",
13:"2 W 2 a + w W 2 x | w + w U r W | b W 2 a + | 8 w + y U 3 q Z | y F | 8 v W U A T Z l",
14:"W w W U? | b 8 2 v W | b C 8 2 y W 8 w F v T | W 3 C + 5 W v T | V A + e n | Y b C + p 8 y x",
15:"+ p b C W y 9 U v T | 3 4 U w w W | 2 v W y C U y x | 8 b C 8 a U X w W | C + 5 p U 4 F T + {sup. y}",
16:"9 y W | v U X 4 n | A + e + | 8 y n C W V T | b C W 8 2 e W 4 8 [...] T | 8 V + V T | 8 2 9 U v T",
17:"p W 5 p C + y 8 a 2 q | 8 5 V? W w 2 y q w y 8 w W | b W a q | b W 2 W a T | U r W",
18:"+ 3 4 n a T | 3 + V F | e + w T | 2 V W y W C F v T | V + V T | 5 4 U 2 x | p U 4 W l",
19:"v W | 9 y W | 8 y n C U G V W 8 | b W 2 W a T | V A + e n | b W U e + a T | l w + W l",
20:"3 C + L U | w 8 q X U | y W r W | y n C U G V W r W | b W 2 a + | y U 3 U | p 2 q 9 U 2 V? 8",
}
out=['page\tline\ttokens']
cnt=collections.Counter(); tot=0
for n in sorted(lines):
    toks=[]
    for t in lines[n].split(' '):
        if t.startswith('{') or t.endswith('}') or t in ('|','[...]') or '{' in t: toks.append(t); continue
        q=t.endswith('?'); m=t.rstrip('?')
        if m not in lab: toks.append(t); continue
        toks.append(lab[m]+('?' if q else '')); cnt[m]+=1; tot+=1
    # rejoin clear-text braces untouched
    out.append('l.21\t%d\t%s'%(n,' '.join(toks)))
open(W+'TRANSCRIPTION.tsv','w').write('\n'.join(out)+'\n')
s=['# SIGNS (ostermann1737): neutral label, working mnemonic, shape, count','',
'Read from the 713x1020 thumbnail (5x crops in lines/). `|` = visible gap between groups, `?` = doubtful sign, `[...]` = illegible (blot), `{}` = clear text or non-cipher mark.','',
'| label | mnemonic | shape | count |','|---|---|---|---|']
for m,d in signs: s.append('| %s | `%s` | %s | %d |'%(lab[m],m,d,cnt[m]))
s+=['','Total sign tokens: %d (sum of the count column).'%tot,'',
'Doubtful distinctions at this resolution: W/U (three vs two minims), V/b (closed vs open), 8/y (size), x/X, D/A, p/n, q/Y.']
open(W+'SIGNS.md','w').write('\n'.join(s)+'\n')
print(tot, len(signs)); print(cnt.most_common())

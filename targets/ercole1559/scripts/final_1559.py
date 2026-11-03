# Pass 3 of c. 50r. Rows below are the copy made with the gloss masked (scripts/row_copy.py, row_zoom.py), checked
# against one dot per sign. Writes work/e50r_p3.txt, the change log, transcription and decryption.
import difflib

P3 = """01 U ] 2 T 2 + # I W V 2 d T W V A T ] A n T U ] O V O V 4 V W V A 4 U I 2 Z V V ] ] U
02 V 7 y V 8 8 V n T W U 4 I d T n I 8 n U 8 U G 2 T W U V 2 4 V n U V ] ] U O U I 4 U 4 U 8 A V
03 8 V 2 n U n V O I W U 7 O I n W V W I P V A T W I 4 V ] I U I n ] V W U 8 O T 8 n V P V n n
04 ] U 4 V ] 8 U G 2 T W G U T V 2 V 2 n T 2 U T 4 U G W V A U 2 V U ] d + I 8 U I W V V 2 d + I U 2 n
05 I 8 T 4 V W T 7 V 2 I 8 T 2 T W I 8 n V n T n A n n T 8 T 8 O I 8 T d T 2 8 U 4 I W V 2 4 T d + I
06 8 A V y I V n U n A 4 U 2 I ] V Q A V ] + V 7 V G U T W P T W Z I L V A n n T W U n V 4 U 7 I 2 T 2
07 A T ] I V n n I 2 4 W A U 2 I U 2 n W U 2 d V W 8 U 2 I ] I d T 8 I ] T W T n V 2 n T O ? A y U 8 T
08 G 2 V d + U T G A V W 4 U y I 2 I 4 U 2 T 2 U 2 d U V 7 O V W I L 7 V 8 U 7 I + V A I 2 4 T U 2 n
09 I 8 T d + I ] V d V O U n A ] V n U T 2 I n W V ] U 4 A T W I 8 n V U 2 7 V 2 I W V d + I 8 V 2 I 8
10 U 2 T 2 8 # O ? 8 T 2 T 4 W I V d + U ] T W T A T G ] U T 2 T d + I 8 W U V A 2 G W V 2 O V 8 8
11 T 8 P T 8 8 I A I W T U ] d + I 8 O I W T 4 U O T n I W 8 V O I W P W V 4 T U T n W I 4 U
12 2 I ] Q A V ] n I 7 O T 4 T A I W V O V W U 7 I 2 n U A I 2 U W 7 U 4 V A T 8 n W V 8 U G 2 T
13 W U V ] V W U 8 O T 8 n V 4 I ? ] I A ] n U 7 I 7 U I ] U n n I W I d + I ] I + T 8 d W U n n T
14 I 8 I 2 4 T y I 2 8 U d A W T d + I 8 I O W I P V n V A T 8 n W V 8 U G 2 T W U V + V A W V
15 U 2 n I 8 T d T 8 V V ] d A 2 V 4 I ] O W I P V n T V A U 8 T 2 T 2 7 V 2 d V W V 4 I V A U 8
16 V W 7 I ] T U 2 8 U I 7 I d T 2 4 U W 7 ] V 8 A V T O U 2 U T 2 I U 2 n A n n T Q A I ] T
17 4 U O U A d + I ? ] V G U A 4 U d V W V y I 2 I d + I 4 V 7 I 8 U V d T 2 8 U 4 I W V n T ? 2
18 Q A I 8 n V 7 V n I W U V L 8 A I 4 I O 2 4 I 2 n I O I W n A n n U Q A I U W U 8 O n n U
19 d + I A U d T 2 d T W I 2 T"""

key = {l.split('\t')[0]: l.split('\t')[2].replace('u/v', 'u') for l in open('key_1559.tsv', encoding='utf8').read().splitlines()[1:]}
old = {}
for l in open('work/e50r_p2.txt'):
    a, b = l.split(None, 1)
    old[a] = b.split()
new = {}
for l in P3.splitlines():
    a, b = l.split(None, 1)
    new[a] = b.split()
open('work/e50r_p3.txt', 'w').write(P3 + '\n')


def plain(s):
    return ''.join(key.get(x, '?') for x in s)


G = {'00': 'circa'}
for l in open('work/e50r_gloss_firstread.txt'):
    a, b = l.strip().split(' ', 1)
    G[a] = b
T = ["# Catalogue 1566: Ercole II d'Este to Cornelio Bentivoglio, Ferrara, 28 May 1559, cc. 50-51, cipher of c. 50r",
     "# Row 00 is the five signs at the end of clear line 2. Rows 01-19 follow it. Labels are in key_1559.tsv.",
     "# Every sign has a dot above it. Dots are not recorded; they carry no value that we found.",
     "# Pass 3: re-copied row by row with the gloss masked, one dot to one sign.",
     "# # = sign under a blot. ? = heavy sign, not settled."]
D = ["# Letter-for-letter decryption with key_1559.tsv. No letter here has been repaired. ? = blot or unsettled sign.",
     "# plain = the signs through the key. gloss = the interlinear decipherment on the leaf, as first read, kept for comparison.",
     "# Rows 04, 10, 13 and 14 of the gloss are incomplete in this first reading."]
rows = [('00', 'd U W d V'.split())] + list(new.items())
for a, s in rows:
    T.append(f"{a}  {' '.join(s)}")
    D += [f"{a}  {' '.join(s)}", f"    plain: {plain(s)}", f"    gloss: {G[a]}"]
open('transcription_cc50r_1559-05-28.txt', 'w', encoding='utf8').write('\n'.join(T) + '\n')
open('decryption_cc50r_1559-05-28.txt', 'w', encoding='utf8').write('\n'.join(D) + '\n')

log = ['row\tpass2_signs\tpass3_signs\tpass2_letters\tpass3_letters']
nch = 0
for a in new:
    if a not in old:
        continue
    sm = difflib.SequenceMatcher(None, old[a], new[a], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        nch += max(i2 - i1, j2 - j1)
        log.append(f"{a}\t{' '.join(old[a][i1:i2])}\t{' '.join(new[a][j1:j2])}\t{plain(old[a][max(i1 - 3, 0):i2 + 3])}\t{plain(new[a][max(j1 - 3, 0):j2 + 3])}")
open('work/e50r_p2_to_p3.tsv', 'w', encoding='utf8').write('\n'.join(log) + '\n')


def lcs(a, b):
    p = [0] * (len(b) + 1)
    for x in a:
        q = [0]
        for j, y in enumerate(b):
            q.append(p[j] + 1 if x == y else max(p[j + 1], q[j]))
        p = q
    return p[-1]


for name, src in (('pass 2', old), ('pass 3', new)):
    sg = sum(lcs(plain(src[a]), G[a].replace(' ', '').replace('v', 'u')) for a in src if a >= '10')
    tot = sum(len(G[a].replace(' ', '')) for a in src if a >= '10')
    print(name, 'rows 10-19 against gloss', sg, 'of', tot)
print('signs', sum(len(s) for _, s in rows), 'changed places', nch, 'log rows', len(log) - 1)
print({a: len(s) for a, s in rows})
for a, s in rows:
    print(a, plain(s))

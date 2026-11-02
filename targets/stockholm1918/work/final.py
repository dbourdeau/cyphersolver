"""Write the final transcriptions for both targets from the first pass plus the corrections made at full resolution,
and print the measured counts used in NOTES. A trailing ? marks a group whose figures stay doubtful."""
import re, sys, collections, json
sys.stdout.reconfigure(encoding='utf-8')
FIX = {
 'w752': {'435': '425', '30850': '20850', '13068': '12068', '29851': '29351?'},
 'w746': {'18456': '18458?', '9825': '9824', '14675': '14?75', '16760': '16760'},
 'w765': {'39520892': '3952 0892', '32385': '323??', '365882': '36582?', '58761': '58761?', '2127': '2127?', '07544': '07544?', '39261': '39?61', '12603': '12?03', '0100': '0100?', '5582': '5582?'},
 'w763': {'5582': '5582?'},
 'w513': {'2113': '2113?', '10819': '10819?'},
 'w791': {'76612': '76612?', '803388': '80338?'},
 'w769': {'34652': '34652?', '18302': '18302?', '82442': '82442?', '36990': '36990?', '48133': '48133?'},
 'w611': {'24330': '24330?'},
 'w643': {'1': '1?'},
}
T = {}; meta = {}; cur = None
for l in open('transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        p = l.split(None, 1); cur = p[0][1:]; meta[cur] = p[1].strip(); T[cur] = []; continue
    for g in l.split():
        if re.fullmatch(r'\d+', g):
            for x in FIX.get(cur, {}).get(g, g).split():
                T[cur].append(x)
i = T['w791'].index('22121'); del T['w791'][i + 1]  # typed twice, the second overstruck; part 2 then has its declared 30
FRAME = {
 'w763': ('Berlin c5428, 194/4/190, 27/7 1:07 m, deutsche gesandtschaft sthlm, signed hintze', 'M367 roll 141 f. 1256; cable roll 108 ff. 0691-0695'),
 'w752': ('Berlin 1742, 124/4/120, 26 10:43 s, deutsche gesandtschaft sthlm, no signature; only 73 of the 120 groups survive in both copies', 'roll 141 f. 1259; cable roll 108 ff. 0700-0701'),
 'w749': ('Berlin c1243, 45/4/41, 26 10:43 n, deutsche gesandtschaft stockholm, signed auswaertig', 'roll 141 f. 1261; cable roll 108 ff. 0723-0724'),
 'w735': ('Berlin c5398, 28/4/24, 26 9:07 d, deutsche gesandtschaft stockholm, signed bussche', 'roll 141 f. 1262; cable roll 108 f. 0725'),
 'w746': ('Berlin c1746, 74/4/70, 26 10:43 n, deutsche gesandtschaft stockholm, signed auswaertig; the copy repeats two typed lines, dropped here (70 groups as the header says)', 'roll 141 f. 1263; cable roll 108 ff. 0726-0727'),
 'w765': ('Berlin c5427, 288/4/284, 27 7 1:07 m, deutsche gesandtschaft stockholm, signed hintze', 'roll 141 ff. 1265-1266; cable roll 108 ff. 0747-0753'),
 'w2635': ('Berlin c2635, 50/4/46, 2 6:30 s, deutsche gesandtschaft stockholm, signed stumm', 'roll 114 f. 0416; cable roll 108 ff. 0512-0513'),
 'w512': ('w512/2, Berlin 286, 32, 2 1:30 m, deutsche gesandtschaft stockholm, signed auswaertig', 'roll 114 f. 0417; cable roll 108 ff. 0513-0514'),
 'w513': ('w513/2, Berlin c295, 44, 2 2 m, deutsche gesandtschaft stockholm, signed auswaertig', 'roll 114 f. 0418; cable roll 108 ff. 0514-0515'),
 'w643': ('Berlin c3516, 153-4-149, w 22 11:45 s, deutsche gesandtschaft sthlm, signed auswaertig; 142 legible, 4 struck, so 3 to 7 groups short of the header', 'roll 122 f. 0155; no cable copy found'),
 'w791': ('w791 SSD GRHQU S M POL ABT BEFSTOHL 26/7, Sehr dringend, DEUTSCHER MIL ATT STOCKHOLM; 5 Teile, each headed teil / urachi / n gruppen / 26 7; ends nr 34298 p roem 4 Ludendorff', 'roll 141 f. 1264; cable roll 108 ff. 0705-0709'),
 'w769': ('w769 s s s b berlin 217 50 26 11:40 s, legation allemande sthlm; opens funfacht vanadopote', 'roll 141 f. 1257; cable roll 108 ff. 0698-0699'),
 'w716': ('w716 s s s b berlin 215 28w 26 7:10 s, legation allemande sthlm; opens funfneun cavesaltri', 'roll 141 f. 1258; cable roll 108 ff. 0699-0700'),
 'w592': ('w592/26 b Berlin 73350 31 26 10:30 m, Deutsches Generalkonsulat Stockholm; opens 2507 18, one mixed group 5710v oh110, ends bidenus 177/2', 'roll 141 f. 1260; cable roll 108 ff. 0722-0723'),
 'w628': ('W628 B S Berlin 178 52 W 22 8:25 s, Legation Allmande Stockholm; opens Fuefsecho Ifesuijuni', 'roll 122 f. 0156; no cable copy found'),
 'w611': ('w611/22 b b berlin 67352 33 w 22 5:55 s, Kaiserl deutsche gesandtscha stockholm; opens hansa 22 juli; clear words vera lilly vera vera hanna LOLO between the groups', 'roll 122 f. 0157; no cable copy found'),
}
A = ['w765', 'w763', 'w735', 'w2635']; B = ['w749', 'w746', 'w512', 'w513']; C = ['w752']; D = ['w643']; E = ['w791']; F = ['w628', 'w611', 'w716', 'w769', 'w592']
def write(path, groups):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# NARA RG 59, M367. Struck or blotted groups are left out. A trailing ? marks a doubtful group.\n'
                '# Read from the frames at full resolution, checked against NARA OCR of the frame and of the Christiania cable copy.\n')
        for name, ids in groups:
            f.write(f'\n## {name}\n')
            for t in ids:
                f.write(f'\n@{t} | {FRAME[t][0]} | {FRAME[t][1]}\n')
                g = T[t]
                for i in range(0, len(g), 10):
                    f.write(' '.join(g[i:i + 10]) + '\n')
write('transcription.txt', [('System A: four-figure groups with a prefix figure, code mark 1219', A), ('System B: groups to about 24000, code marks 4407, 4416, 4435', B), ('System C: groups to about 48000', C), ('System D: groups to about 18200, page 181 dense', D)])
write('../ludendorff1918/transcription.txt', [('Military attache telegram', E), ('Legation and Consulate-General telegrams', F)])
import os
for folder, ids in (('.', A + B + C + D), ('../ludendorff1918', E + F)):
    os.makedirs(f'{folder}/groups', exist_ok=True)
    for t in ids:
        with open(f'{folder}/groups/{t}.txt', 'w', encoding='utf-8', newline='\n') as f:
            f.write(' '.join(x.rstrip('?') for x in T[t]) + '\n')
def stat(ids):
    g = [x.rstrip('?') for t in ids for x in T[t]]
    return len(g), len(set(g)), collections.Counter(g).most_common(6)
for n, ids in [('A', A), ('B', B), ('C', C), ('D', D), ('E', E), ('F', F)]:
    print(n, stat(ids))
for t in T: print(t, len(T[t]))
print('w791 parts'); g = T['w791']
for a, b, d in [(0, 39, 39), (39, 69, 30), (69, 106, 38), (106, 137, 31), (137, 170, 33)]:
    print('  ', g[a], '...', g[b - 1], b - a, 'declared', d)

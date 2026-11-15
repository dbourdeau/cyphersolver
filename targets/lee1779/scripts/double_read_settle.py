import csv
S = {  # id: (settled figure, outcome, new grade, note)
 8: ('?4,b,9', 'agree (partial)', 'doubtful', 'all three read 4,b,9 with the page cut at the gutter; 64b9 supplied, not read'),
 18: ('unsettled: 82,b,37 (O) / 12,b,37 (A, B)', 'unsettled', 'doubtful', 'image: first figure at the gutter, only a thin stroke before the 2; 12,b,37 has no entry (no arabic page 12 in the 1776 dictionary); 82b37 Charge rests on O alone'),
 44: ('63,a,32', "O's alternative", 'firm', 'A and B 32 = O alternative'),
 56: ('132,b,29', 'agree (partial)', 'firm', 'letter book 2,b,29 by O, A, B; page in full only on the received copy (one reading), interlined "distress"'),
 59: ('unsettled: 102,b,9 (A) / 152,b,9 (received copy) / ?2,b,9 (O, B)', 'unsettled', 'doubtful', 'image: page figures under a blot; 102b9 = Continuous (no fit); 152b9 Exertion rests on the received copy alone'),
 102: ('314,b,37', 'agree', 'firm', 'A listed 166bVII before 314bXXXVII (order slip); content agrees'),
 103: ('166,b,7', 'agree', 'firm', 'see 102'),
 106: ('284,a,9', 'agree (partial)', 'firm', 'letter book 28?,a,9 by O, A, B (third figure blotted); 284 only on the received copy (one reading)'),
 113: ('unsettled: 100,b,36 (O, A, B) / 101,b,36 (received copy)', 'unsettled', 'doubtful', '100b36 = Conspicuously (counted on the 1776 page image; no fit); 101b36 Contempt rests on the received copy alone; the two copies differ'),
 120: ('454,b,14', 'agree', 'firm', 'A and B both read 454,b,14 here (alignment listed it as extra)'),
 128: ('455,d,27', 'O wrong', 'firm', 'A, B and received copy d; O wrote "455?a27"'),
 144: ('250,?,12', 'agree (partial)', 'unread', 'column letter under a blot for all'),
 158: ('unsettled: 455,a,14 (O, A) / 445,a,14 (B); earlier check read column e', 'unsettled', 'doubtful', 'image: middle figures overwritten under a blot; 455a14 Gerard judged not to fit, 455e14 Thomas rests on one earlier check; both printed'),
 161: ('416,b,10?', 'agree (partial)', 'doubtful', 'right edge; strokes after X may be lost'),
 163: ('322,a,7', 'agree O+A', 'firm', 'B 822 (no such page; the dictionary ends near p. 456); image: first figure closed, 3 or 8'),
 109: ('454,b,14', 'agree', 'firm', 'B read 454,b,14 here (alignment listed it as extra)'),
 80: ('314,a,20', 'agree', 'firm', 'B read it (alignment listed it as extra)'),
}
rows = list(csv.DictReader(open('threeway.tsv'), delimiter='\t'))
out = open('double_read_settled.tsv', 'w')
cols = ['id','letter','O_written','O','A','A_conf','B','B_conf','received','settled','outcome','old_grade','new_grade','note']
out.write('\t'.join(cols) + '\n')
from collections import Counter
c = Counter(); per = {}
for r in rows:
    i = int(r['id'])
    if i in S: st, oc, ng, note = S[i]
    else: st, oc, ng, note = r['O'], 'all three agree' if r['all3']=='Y' else 'agree', r['grade'], ''
    c[ng] += 1
    per.setdefault(r['letter'], Counter())[oc] += 1
    out.write('\t'.join([r['id'], r['letter'], r['O_written'], r['O'], r['A'], r['A_conf'], r['B'], r['B_conf'], r['received'], st, oc, r['grade'], ng, note]) + '\n')
print(c); [print(k, dict(v)) for k, v in sorted(per.items())]

"""Pinckney to Jefferson, 28 Aug 1793 (frame 0140): each group of ../reading_pinckney_17930828.tsv against key v4 and
the other witnesses of the code. Checks that this repository's reading still says what the proposal assumes
(it stops if a row has changed), then writes corrections/pinckney_17930828_points.tsv.

Run from targets/legation1788/beling:   python3 corrections/pinckney_17930828_points.py
"""
import csv, sys
from pathlib import Path

B = Path(__file__).resolve().parents[1]
v4 = {r['group']: r for r in csv.DictReader(open(B / 'key' / 'code16_key_v4.tsv'), delimiter='\t')}
rows = [l.rstrip('\n').split('\t') for l in open(B.parent / 'reading_pinckney_17930828.tsv', encoding='utf-8') if not l.startswith('#')]
head, rows = rows[0], rows[1:]

# (line, pos): (group, reading and grade now in the repository, proposed reading, proposed grade, evidence)
P = {
 ('2', '6'): ('234', '[time?]', 'C', 'time', 'H', 'Lear to Madison [Jan 1813], Graham\'s interlinear "time" over 234 twice (981-L4, 982-L2); Eaton\'s Tunis enclosure 1802, "time" = 234 against the 1802 printed translation'),
 ('2', '9'): ('501', '[secret?]', 'C', 'secret', 'H', 'Lear [Jan 1813], Graham\'s interlinear "secret" over 501 (981-L25, placement clear); one occurrence'),
 ('1', '5'): ('923', 'are', 'E', 'are', 'H', '"are" over 923: Eaton 25 May 1801 (Wagner\'s interlinear, L10); Pinckney 1795 (Taylor, M31 roll 7 frame 0019 left, L01)'),
 ('2', '13'): ('923', 'are', 'E', 'are', 'H', 'as above'),
 ('3', '4'): ('1328', 'Sir', 'E', 'Si-', 'H', '1328 = si: Lear 1813 re-si-dent (1107 1328 1047) and expo-si-(tion) (1159? 1133 1328); Pinckney 28 Oct 1795 (M31/7/0111) si-tu-ation (1328 1404 1181); Tunis 1802 salutation "Sir" written 1328-1374 twice'),
 ('3', '5'): ('1374', 'Char-', 'E', '-r', 'H', '1374 = r: Tunis 1802 "Mr" written 1018-1374 twice (M with 1374 raised), "Sir" 1328-1374 twice; fits re-qui-[1374]-ing (requiring) on frame 0196 l. 7. key.tsv has 1374 = emerge (0148, one gloss). Not in key v4 (Tunis rows flagged, and 817 = r there, S1)'),
 ('3', '6'): ('672', '-les', 'E', 'Charles', 'E', 'with Sir = 1328 1374, Charles is 672 alone; 672 occurs nowhere else in the witnesses'),
 ('4', '1'): ('?55', '[Dun-]', 'C', '[?]', 'O', 'gutter; with 668 = at the editors\' [Dunda]s cannot be spelled ?55-668-800; the name stays open'),
 ('4', '2'): ('668', '[-da-]', 'C', '-at-', 'H', '668 = at: Eaton 25 May 1801 "at" three times (L18, L26, L28); Pinckney 1795 frame 0018 L03 "at" (clear); Tunis 1802 body "at"'),
 ('4', '9'): ('1010', '-tina-', 'E', '-tin-', 'H', '1010 = tin: Eaton 1801 dis-tin-guishable (957 1010 1151); Tunis 1802 dis-tin-c-tion (957-1010-1112-1432), dis-tin-guished (957-1010-1151-886-1515)'),
 ('4', '10'): ('1181', '-tion', 'H', '-ation', 'H', 'des-tin-ation; 1181 = ation also in si-tu-ation (M31/7/0111; key v4 S1)'),
 ('4', '13'): ('675', '-ly', 'E', '-ly', 'H', '675 = ly: Tunis 1802 equal-ly, infinite-ly, direct-ly, ho-ly, successive-ly; Lear 1813 general-ly (523 675), particular-ly (121 675); key.tsv has 675 = information (0180 "(lately)")'),
}
FLAG = {
 ('3', '13'): 'not changed: key v4 has 1064 = ou (S1, from Tunis w-ou-nd 507-1064-727), which would make 1565 1064 942 St-ou-rt rather than St-ua-rt; one word only, so flagged, not proposed',
 ('1', '1'): 'not changed: 447 is not in key v4 and occurs in no witness',
 ('2', '1'): 'not changed', ('3', '1'): 'not changed', ('5', '1'): 'not changed',
}
out = []
for r in rows:
    line, pos, g, reading, grade = r[:5]
    k = v4.get(g.rstrip('+'))
    kv = f"{k['value']} ({k['grade']}, n={k['n']}{', ' + k['sources'] if k['sources'] else ''})" if k else '-'
    if (line, pos) in P:
        pg, pr, pgr, nr, ngr, ev = P[(line, pos)]
        if (g, reading, grade) != (pg, pr, pgr):
            sys.exit(f'row {line}.{pos} has changed in the repository: {g} {reading} {grade}; expected {pg} {pr} {pgr}')
        out.append((line, pos, g, reading, grade, kv, nr, ngr, ev))
    else:
        out.append((line, pos, g, reading, grade, kv, reading, grade, FLAG.get((line, pos), '')))
with open(B / 'corrections' / 'pinckney_17930828_points.tsv', 'w') as f:
    f.write('# Pinckney 28 Aug 1793 (M30 roll 2 frame 0140): repository reading and grade, key v4 value, proposed reading and grade, evidence.\n')
    f.write('# Grades as in ../make_reading.py: H = value attested by a decoding in another letter of the same code; E = editors only; C = conjecture; O = open.\n')
    f.write('line\tpos\tgroup\treading_now\tgrade_now\tkey_v4\treading_proposed\tgrade_proposed\tevidence\n')
    for o in out: f.write('\t'.join(o) + '\n')
from collections import Counter
a = Counter(o[4] for o in out); b = Counter(o[7] for o in out)
print('now', dict(a), 'proposed', dict(b), 'changed rows', sum(1 for o in out if (o[3], o[4]) != (o[6], o[7])))

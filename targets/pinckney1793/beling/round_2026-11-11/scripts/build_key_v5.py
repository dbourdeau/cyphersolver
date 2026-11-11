"""Code 16 key v5 = key v4 (output/code16_merged_2026-11-10/code16_key_v4.tsv, 537 groups, sha256 e18775d8...) plus the
hand-checked changes below, from the 28 Jan 1794 (M30-002-0196), 26 Feb 1794 (0208) and 1 Oct 1795 (M31-007-0020/21)
alignments (alignment_*.tsv, interlinear_vs_v4.tsv). Nothing from frame 0178 or its print is used.
Writes code16_key_v5.tsv and key_v5_changes.tsv; prints sha256. Does not touch v4."""
from pathlib import Path
import csv, hashlib

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/code16_pinckney_2026-11-11'
V4 = ROOT / 'output/code16_merged_2026-11-10/code16_key_v4.tsv'

# (group, value, grade, n, sources, evidence)
ADD = [
    (1160, ',', 'D', 16, 'lear tick x14; m30-0196 x2',
     "Lear 1813: the clerk's comma stroke over 1160 fourteen times; 0196: at both printed commas (merchants, | Toulon,). v4 had removed 1160 = ry."),
    (1501, 'di', 'A', 2, 'm30-0196; m31-0111',
     '0196 ad-di-tion, pinned by 1521 ad and 1432 tion; 0111 Taylor "prejudices" = 941 640 1501 1369+. Note 1496 = di (B) also claims di.'),
    (1435, 'ent', 'A', 3, 'm30-0196; m31-0111; lear',
     '0196 differ-ent; 0111 "equivalent" ends 972 1435 (al-ent); Lear "insurgents" = 1465 1589 1366 1435 800 (in-sur-g-ent-s). Note 1438 = ent (S1, Tunis "convenient"): a 5/8 misreading in one of them is likely.'),
    (941, 'pre', 'A', 2, 'm30-0196; m31-0111', '0196 pre-ci-se; 0111 Taylor "prejudices" begins 941.'),
    (481, 'fine', 'A', 1, 'm30-0196', '0196 con-fine(d), 481++ pinned by 1206 con and 270 my (aligner accepted).'),
    (679, 'mine', 'A', 1, 'm30-0196 clerk', '0196 de-ter-mine(d): clerk wrote "mined" over 679++ alone; print "determined".'),
    (1235, 'past', 'A', 1, 'm30-0196', '0196 "what is past because": two-group gap between 885 is and 298 if; past|because is the only split into unowned list elements.'),
    (69, 'because', 'A', 1, 'm30-0196', 'as 1235.'),
    (1336, 'pres', 'A', 1, 'm30-0196', '0196 "I presume he": gap between 753 I and 648 he; pres|ume is the only split into unowned list elements.'),
    (415, 'ume', 'A', 1, 'm30-0196', 'as 1336.'),
    (586, 'move', 'A', 1, 'm30-0208 clerk', '0208 re-move(d): clerk "moved" over 586++; pinned by 1107 re and 1490 to (aligner accepted).'),
    (490, 'cure', 'A', 1, 'm30-0208 clerk', '0208 pro-cure: clerk "cu[..]" over 490 alone, after 1425 pro.'),
    (950, 'ia', 'A', 2, 'm30-0208', '0208 confident-ia-l (728 l) and Si-les-ia (1328? 1426 950); clerk "ial" over 950.'),
]
CHANGE = [
    (1366, 'g', 'A', 2, 'm30-0208; lear', 'was ge (S1). Lear "insurgents" in-sur-g-ent-s with 1435 = ent; 0208 sen-din-g (clerk "sen", "di[..]", dash over 1366).'),
    (631, 'sixth', 'A', 1, 'm30-0196', 'was th (B, Bourdeau). 0196 "the sixth of november": 631 alone under the clerk\'s "6th"; cf. 1156 = tenth.'),
    (598, 'es', 'A', 3, 'p1795; tunis; m31-0021',
     'was fourth (D, one occurrence, 0111, doubtful digit, alt 508). 0019L "acquiesce" = 936 1259 598 1369 (ac-qui-es-ce, pinned both sides); Tunis ti-es; 0021 con..-ur-es.'),
]
DROP = [
    (640, 'was es (S2). Three words want "iv": Tunis suc-cess-640-e-ly (if 1063^ = ces doubled), "equivalent" 265/255 640 972 1435 at 0019L and 0111. "iv" is not on the element list, so no value entered.'),
]
UPGRADE = {1494: 'no', 779: 'plan', 144: 'place', 885: 'is', 1252: 'try'}   # B -> D: one unmarked group under the clerk's whole word, clear placement


def main():
    rows = {int(r['group']): r for r in csv.DictReader(V4.open(), delimiter='\t')}
    log = []
    for g, v, gr, n, src, ev in ADD:
        assert g not in rows, g
        rows[g] = dict(group=str(g), value=v, grade=gr, n=str(n), sources=src, on_element_list='y'); log.append(('add', g, '', v, gr, ev))
    for g, v, gr, n, src, ev in CHANGE:
        old = rows[g]['value'] + ' (' + rows[g]['grade'] + ')'
        rows[g] = dict(group=str(g), value=v, grade=gr, n=str(n), sources=src, on_element_list='y'); log.append(('change', g, old, v, gr, ev))
    for g, ev in DROP:
        old = rows.pop(g); log.append(('drop', g, old['value'] + ' (' + old['grade'] + ')', '', '', ev))
    for g, v in UPGRADE.items():
        assert rows[g]['value'] == v and rows[g]['grade'] == 'B', g
        rows[g]['grade'] = 'D'; rows[g]['sources'] = 'm30-0196/0208 clerk; ' + rows[g]['sources']
        log.append(('B->D', g, v + ' (B)', v, 'D', "clerk's whole word over the single unmarked group (0196 or 0208)"))
    p = OUT / 'code16_key_v5.tsv'
    with p.open('w') as f:
        f.write('group\tvalue\tgrade\tn\tsources\ton_element_list\n')
        for g in sorted(rows):
            r = rows[g]; f.write('\t'.join([r['group'], r['value'], r['grade'], r['n'], r['sources'], r['on_element_list']]) + '\n')
    with (OUT / 'key_v5_changes.tsv').open('w') as f:
        f.write('action\tgroup\tv4\tv5\tgrade\tevidence\n')
        for x in log: f.write('\t'.join(map(str, x)) + '\n')
    print(len(rows), 'groups', hashlib.sha256(p.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()

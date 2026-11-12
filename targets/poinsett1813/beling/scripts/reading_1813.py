"""Line-by-line reading of Poinsett -> Monroe, 20 Feb 1813 with WE025, and coverage counts.
Status per group:
  D = frozen first reading, WE025 element used as is
  A = the other of two frozen readings {a|b} chosen
  R = reread on the image this run (after seeing the decode; the note column says which)
  I = inferred misreading, not confirmed on the image (blot, page edge, or digit form ambiguous); number shown
  H = hole: no element that makes sense
Post-freeze table correction 668 fect applied (key/we025_postfreeze_corrections.tsv).
Writes ../groups_1813-02-20.tsv; prints the counts and a compact line view (../tests/reading_1813_lines.txt).
Run from anywhere: python3 scripts/reading_1813.py > tests/reading_1813_lines.txt"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import texts
OUT = texts.BEL
we = texts.load_key()   # key/we025_poinsett.tsv with key/we025_postfreeze_corrections.tsv applied (668 fect)
# (label, token index in line incl. [X]) -> (status, number or None, note)
OV = {
 ('P1.1',0): ('A',1486,'image 1486; mas(s)'),
 ('P1.4',4): ('R',697,'frozen 657 (ice); image 6?7, middle digit 9 or 5; 697 number'),
 ('P2.2',8): ('A',1589,'no'),
 ('P2.2',9): ('R',739,'frozen 789 (pire); at 3x the middle digit is open like 3, not the closed 8 of 1589 beside it; 739 mean + diamond = means'),
 ('P2.3',6): ('H',None,'55 diamond: spect; a faint stroke before it; [?instructions] by context only'),
 ('P2.4',9): ('A',1547,'si (situation)'),
 ('P2.4',13): ('I',1348,'134 at the page edge, last digit lost; 1348 in'),
 ('P2.5',0): ('I',324,'first digit blotted (934|924 frozen); 324 which'),
 ('P4.1',6): ('A',1299,'act + diamond = acts'),
 ('P4.2',2): ('R',1355,'1356 (sm) frozen with doubt; final 5/6 with flourish; the'),
 ('P4.2',11): ('A',1399,'nt (want)'),
 ('P4.3',12): ('I',461,'416 (ful) at page edge, blotted; 461 mit (admit)'),
 ('P4.4',10): ('I',1244,'124? last digit under a blot; 1244 tre (treasury)'),
 ('P4.5',3): ('I',1554,'155 then a gap; 1554 to'),
 ('P4.5',8): ('A',1225,'cu'),
 ('P4.5',9): ('A',1111,'tin + cross (doubled letter): cutting'),
 ('P4.5',11): ('I',1397,'1387 (what) at page edge; 1397 of + cross = off'),
 ('P4.6',10): ('A',148,'mar'),
 ('P4.6',11): ('I',431,'?31, first digit under the folio number 41; 431 ke'),
 ('P4.6',12): ('H',None,'12 quire; expected t (market)'),
 ('P4.7',13): ('H',None,'502 forty; general dis[...]'),
 ('P4.8',0): ('H',None,'774 force; part of the same word?'),
 ('P4.8',8): ('H',None,'487 phy; expected must/ought'),
 ('P4.9',5): ('A',805,'deem'),
 ('P4.9',13): ('A',1589,'no'),
 ('P4.10',7): ('R',1331,'frozen 78?1; first figure is the hooked 1 seen in 1133 on the line above; 1331 sea + diamond = seas'),
 ('P5.1',3): ('A',854,'object'),
 ('P5.2',9): ('A',711,'lea (leave)'),
 ('P5.3',7): ('I',1228,'1221 (pot); last digit unclear; 1228 re (return)'),
 ('P5.3',8): ('A',1288,'turn'),
 ('P5.4',0): ('A',1548,'de; image clear 1548'),
 ('P5.4',3): ('I',1300,'1800 is above the code range; second digit blotted; 1300 thro (throughout)'),
 ('P5.4',4): ('A',1584,'out; image 1584'),
 ('P6.2',14): ('H',None,'122 (course) at page edge; [?con]'),
 ('P6.3',0): ('H',None,'1261 (nat); [?fu] would need 1201'),
 ('P7.1',0): ('A',1385,'pre; first digits retouched'),
 ('P7.2',13): ('I',425,'428 (yo); 425 court'),
 ('P7.3',0): ('I',1458,'1450|1459 blotted; 1458 bra (Brasil)'),
 ('P7.3',1): ('D',1547,'si (Bra-si-l)'),
 ('P7.3',2): ('A',120,'l'),
 ('P7.3',4): ('I',891,'851 (rian); 891 this'),
 ('P7.3',7): ('A',168,'ra (paralises)'),
 ('P7.4',0): ('I',1397,'17, blotted; 1397 of'),
 ('P7.4',2): ('I',1517,'1317|1327 frozen; 1517 ay (Ayres)'),
 ('P8.1',7): ('I',1355,'1?? faint at page edge; 1355 the'),
 ('P8.2',5): ('I',1586,'1386 (ail); first digits doubtful; 1586 had'),
 ('P8.2',10): ('I',1355,'13?? blotted; 1355 the'),
 ('P9.1',10): ('I',1400,'140 cut at the page edge; 1400 doc (docile)'),
 ('P9.2',12): ('A',14,'america'),
 ('P9.3',6): ('A',1178,'me'),
 ('P9.3',12): ('I',638,'658 (bor); 638 cal (political)'),
 ('P9.3',15): ('I',1166,'1106 (oa) at page edge; 1166 ne (engine)'),
 ('P9.4',2): ('A',1320,'my'),
}
L = texts.load_1813()
rows = []; cnt = {}
for l in L:
    for i, t in enumerate(l['toks']):
        if t['raw'] == '[X]':
            rows.append((l['label'], i, '[X]', '', '', 'X', 'cancelled group')); continue
        st, num, note = OV.get((l['label'], i), ('D', None, ''))
        if num is None and st == 'D': num = int(t['alts'][0])
        el = we.get(num, '') if num else ''
        if st == 'H': el = ''
        cnt[st] = cnt.get(st, 0) + 1
        rows.append((l['label'], i, t['raw'], str(num or ''), el + (t['mark'] if el else ''), st, note))
with open(OUT / 'groups_1813-02-20.tsv', 'w', encoding='utf-8') as f:
    f.write('line\tidx\tfrozen\tused\telement\tstatus\tnote\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
n = sum(cnt.values())
print(n, cnt)
for k in 'DARIH': print(k, cnt.get(k, 0), f'{cnt.get(k,0)/n:.1%}')
# compact line view
cur = None; buf = []
for r in rows:
    if r[0] != cur:
        if buf: print(cur, ' '.join(buf))
        cur = r[0]; buf = []
    buf.append(f"{r[4] or '['+r[2]+']'}" + ('' if r[5] in 'DX' else '/' + r[5]))
print(cur, ' '.join(buf))

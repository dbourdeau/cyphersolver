"""Tunis 1802 coded enclosure: word-level alignment to the printed 1802 translation.

Source cipher: NARA T303 roll 2, frames 0299-0301 (copy A), Eaton's "Triplicate copy by
translation" of Hammuda Bey's letter to Jefferson, 8 September 1802.
Printed English text used as crib: American State Papers, Claims, p. 331, as reprinted in
Naval Documents ... Barbary Powers II:269.  The printed text is NOT letter-identical to the
cipher (e.g. cipher "Sir" where print has "Mr. President"; cipher "ship" where print has
"vessel"); each such place is flagged.

Manuscript conventions read from the images on 10 Nov 2026:
  period  = end of word;  dash = groups joined in one word
  ^       = caret written beneath a group: double its final letter (al->all, ful->full,
            se->see, wel->well, ad->add, shal->shall, ke->kee, ces->cess)
  +       = inflection mark (plural s, -ed, -n, possessive)
A word of one group is "direct" evidence for that group.  Pieces of multi-group words are
hypotheses, kept only when the same piece value serves two or more different words.

Postscript (Eaton's own, 9 Oct 1802; editors' decipherment in PJM-SS 4) re-read with the same
conventions on 10 Nov: see PS below.  'large' is 1241 alone and 'vessels' is 1367-1110+ (the 6 Nov
alignment had split them wrongly); 'address' is 1521^-146^ (ad+d, res+s); 'add' in the body is 1521^
(first read 1524^: the caret's tail made the final 1 look like 4).

Nothing here is a blind test: the alignment was made by hand with the crib in view.
The independent check is the comparison with keys built by others from other documents.
"""
from pathlib import Path
import csv, json, collections

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/tunis_known_plaintext_2026-11-10'
OUT.mkdir(parents=True, exist_ok=True)

# (plaintext word, groups joined by '-', flag)   flag: '' ok, 'u' uncertain numeral or word,
# 'x' printed text differs / unresolved, 'd' date heading (low confidence)
RAW = """
# date heading, frame 0299
Tunis 1404-933-800
eight? 1351 d
September? 26 d
[1802] 1058?-63-1351-171-977 d
# address, frame 0301, marked for insertion
the 663
Bashaw 1506-886-658
Bey 1517-1258
of 1518
Tunis 1404-933-800
to 1490
the 663
President 649 x
of 1518
the 663
republic 1107-708-1112
of 1518
the 663
United_States 71
of 1518
America 54
# salutation
Sir 1328-1374 x
# body, frame 0299
with 709
equal 145
pleasure 994-1488-940
and 856
satisfaction 1378-154
I 753
have 673
seen 1104-1166
arrive 982-729
and 856
have 673
received 99+
successively 1573-1063^-640-940-675
all 972^
the 663
military 1423-1362-232
and 856
naval 1333-456
stores 1579-146
as 913
well 737
as 913
the 663
superb 1588-1301
jewels 489-737^
which 515
your 561
government 829-1546
has 1076
sent 622
forward 1226-1382
for 1226
my 270
regency 735-1186
and 856
myself 270-1008
in 1465
execution 891-997
of 1518
our 604
conditions 229+
for 1226
the 663
confirming 381-134
and 856
consolidation 1206-1099-435-1282-1432 x
of 1518
the 663
good_harmony 1123-976-113-1500 x
and 856
alliance 972-435-634
which 515
thank 1361-1210
God 918-1475
have 673
been 1457
established 189+
and 856
[actually] 945-1063^-955 x
subsist 1580-1196
between 59
us 983
while 246
I 753
am 928
happy 762-1407
to 1490
give 688
you 367
this 194
assurance 913-1589-634
indeed 1273
sincere 1297-951-940
of 1518
my 270
full 523^
contentment 1206-1340-924-1546
I 753
ought 337
not 967
to 1490
dissemble 957-224-899
that 1058
I 753
do 689
not 967
at 668
the 663
same 1468
time 234
see 1104^
myself 270-1008
treated 290+
with 709
the 663
same 1468
distinction 957-1010-1112-1432
and 856
the 663
same 1468
regard 1107-455-1475
that 1058
you 367
have 673
had 1271
for 1226
your 561
other 1472
friends 700-1399+
and 856
since 187
that 1058 x
I 753
am 928
equally 145-675
one 1506 x
I 753
avow 1513-1022-1466
to 1490
you 367
with 709
frankness 981-642
as 913
I 753
have 673
already 972-213
declared 1190-1007-533
to 1490
Mr 1018-1374 x
Eaton 545-924-616
your 561
consul 160
that 1058
it 1362
would 90
have 673
been 1457
infinitely 1465-158-933-1005-675
agreeable 29
to 1490
me 212
if 298
you 367
had 1271
also 1219
made 320
me 212
a 1513
present 649
of 1518
a 1513
ship 218 x
of 1518
war 770
Mr 1018-1374 x
Eaton 545-924-616
not 967
finding 390-1475-134
it 1362
convenient 1206-1367-933-1438
to 1490
charge 155
himself 525-1008
with 709
the 663
communication 8-1432
of 1518
this 194
demand 471
to 1490
you 367
on 616
my 270
part 743
I 753
am 928
determined 1190-1481-856+ u
to 1490
testify 248-753-987
to 1490
you 367
directly 1501-1067-924-675
by 1527
the 663
present 649
that 1058
it 1362
would 90
be 1517
# frame 0300
very 353
agreeable 29
to 1409 x
me 212
that 1058
you 367
should 614
send 312-1475
me 212
a 1513
good 1123
frigate 700-1171-1005
of 1518
thirty 1462
six 1491
guns 930-1523+
which 515
would 90
add 1521^
to 1490
the 663
high 1441
esteem 93
I 753
have 673
for 1226
your 561
nation 126
and 856
would 90
more 1509
and 856
more 1509
cement 1369-1546
the 663
ties 1350?-598 u
of 1518
our 604
friendship 700-1399-218
which 515
on 616
my 270
part 743
I 753
shall 986^
maintain 454
firm 477-1018
and 856
inviolable 1465-1479-943-819-899
convinced 1206-1019-1467
as 913
I 753
am 928
beforehand 1167-667
Sir 1328-1374 x
this 194
demand 471
taken 620+
into 1216
consideration 371?-1184? u
will 1408
obtain 557
the 663
full 523^
effect 1432?-180 u
which 515
I 753
expect 1159-1090-1355
from 612
it 1362
I 753
renew 1107-548
to 1490
you 367
the 663
assurance 913-1589-634
of 1518
my 270
most 335
distinguished 957-1010-1151-886-1515
esteem 93
and 856
I 753
pray 610-564? u
Almighty 972-1302-1258
God 918-1475
to 1490
have 673
you 367
in 1465
his 1034
holy 1120-675
keeping 1412^-1402-134
# signature
Hamuda 965-1497-1282
Bashaw 1506-886-658
Bey 1517-1258
Prince 285
of 1518
the 663
Princes 285+
of 1518
Tunis 1404-933-800
the 663
city 613
well 737^
guarded 930-474+
the 663
abode 1513-1463-1190
of 1518
happiness 762-705-642
Bey's 1517-1258+
seal 1306-728
"""

PS = """
if 298
the 663
Bey's 1517-1258+
letter 538
should 614
provoke 1425-1022-1012
resentment 1107-622-1546
Porto 460-943
Farina 1444-1348-1333
may 512
be 1517
taken 620+
by 1527
surprise 1589-1100-1104
or 1127
stratagem 1570-1513-1116-1448-1048? u
with 709
eight_hundred 1371?-171 u
men 788
and 856
the 663
Bey's 1517-1258+
whole 1254
naval 1333-456
arsenal 982-1104-1225
together 51
with 709
his 1034
large 1241
vessels 1367-1110+
of 1518
war 770
destroyed 1228-924-1299-1258+
but 810
it 1362
would 90
require 1107-350
secrecy 1104-1305-1176
and 856
address 1521^-146^
it 1362
would 90
be 1517
a 1513
vital 1479-1554
wound 507-1064-727
to 1490
cruising 1112-1392-855?-134 u
but 810
it 1362
should 614
be 1517
done 611
in 1465
the 663
winter 307
or 1127
spring 1563-134
season 1306-1547
"""

# piece hypotheses: (group, piece, words that share it).  Kept only if >=2 distinct words.
PIECES = """
1404 tu Tunis
933 ni Tunis infinitely convenient
800 s Tunis
1517 be Bey be
1258 y Bey Almighty
1107 re republic regard renew
1112 c republic distinction
1104 se seen see
982 ar arrive
940 e pleasure successively sincere
675 ly successively equally infinitely directly holy
972 al all alliance already Almighty
1362 it military it
1546 ment government contentment cement
1226 for forward for
1008 self myself himself
270 my myself my
134 ing confirming finding keeping
1206 con consolidation contentment convenient convinced
435 li consolidation alliance
1282 da consolidation Hamuda
1432 tion consolidation distinction communication
634 ance alliance assurance
1475 d God regard finding send
913 as assurance as
1589 sur assurance
924 t contentment Eaton directly
957 dis dissemble distinction distinguished
899 ble dissemble inviolable
1010 tin distinction distinguished
700 fri friends friendship frigate
1399 end friends friendship
218 ship friendship ship
1513 a avow abode a
1022 vo avow
642 ness frankness happiness
1190 de declared determined abode
1465 in infinitely inviolable in
1005 te infinitely frigate
616 on Eaton on
762 hap happy happiness
930 gu guns guarded
737 wel well jewels
1018 m firm Mr
1374 r Sir Mr
753 i testify I
886 sh Bashaw distinguished
145 equal equal equally
1063 ces successively [actually]
918 go God
"""

def parse():
    rows = []; section = ''
    for line in RAW.strip().splitlines():
        if line.startswith('#'):
            section = line[1:].strip(); continue
        parts = line.split()
        word, groups = parts[0], parts[1]
        flag = parts[2] if len(parts) > 2 else ''
        toks = groups.split('-')
        rows.append(dict(n=len(rows) + 1, section=section, word=word.replace('_', ' '),
                         tokens=toks, flag=flag))
    return rows

def num(tok):
    return int(tok.rstrip('+^?'))

def load_ext():
    base = ROOT / 'sources/raw/reconstruction_2026-11-06/repo/targets/legation1788/key.tsv'
    code16 = {}
    for r in csv.DictReader(base.open(), delimiter='\t'):
        if r['code'] == '16' and r['group'].isdigit():   # marked groups such as 22+ are kept out of the plain comparison
            code16[int(r['group'])] = (r['value'], r['other_readings'])
    lear = {}
    for r in csv.DictReader((ROOT / 'output/adjudication_2026-11-06/lear_direct_key.tsv').open(), delimiter='\t'):
        lear[int(r['group'])] = r['value']
    return code16, lear

def norm(s):
    return ''.join(ch for ch in s.lower() if ch.isalpha())

def main():
    rows = parse()
    n_groups = sum(len(r['tokens']) for r in rows)
    # direct single-group words
    direct = collections.defaultdict(lambda: collections.Counter())
    for r in rows:
        if len(r['tokens']) == 1 and r['flag'] in ('',):
            t = r['tokens'][0]
            if '?' in t: continue
            mark = '+' if '+' in t else ('^' if '^' in t else '')
            direct[(num(t), mark)][r['word'].lower()] += 1
    pieces = {}
    for line in PIECES.strip().splitlines():
        g, p, *ws = line.split()
        if len(set(ws)) >= 2:
            pieces[int(g)] = (p, ws)
    code16, lear = load_ext()

    # plain (unmarked) direct values
    plain = {g: c.most_common(1)[0][0] for (g, m), c in direct.items() if m == ''}
    multi_valued = {g: dict(c) for (g, m), c in direct.items() if m == '' and len(c) > 1}
    comp = []
    for g in sorted(set(plain) | set(pieces)):
        tv = plain.get(g) or pieces[g][0]
        kind = 'direct' if g in plain else 'piece'
        for name, ext in (('code16', code16), ('lear', lear)):
            if g in ext:
                ev = ext[g][0] if name == 'code16' else ext[g]
                a, b = norm(tv), norm(ev)
                if a == b: verdict = 'agree'
                elif a and b and (a.startswith(b) or b.startswith(a) or a in b or b in a): verdict = 'compatible'
                else: verdict = 'differ'
                comp.append(dict(group=g, tunis=tv, kind=kind, source=name, external=ev, verdict=verdict))
    with (OUT / 'tunis_word_spans.tsv').open('w') as f:
        f.write('n\tsection\tword\tgroups\tflag\n')
        for r in rows:
            f.write(f"{r['n']}\t{r['section']}\t{r['word']}\t{'-'.join(r['tokens'])}\t{r['flag']}\n")
    with (OUT / 'tunis_postscript_spans_v2.tsv').open('w') as f:
        f.write('n\tword\tgroups\tflag\n')
        for i, line in enumerate(PS.strip().splitlines(), 1):
            parts = line.split()
            f.write(f"{i}\t{parts[0].replace('_', ' ')}\t{parts[1]}\t{parts[2] if len(parts) > 2 else ''}\n")
    with (OUT / 'tunis_direct_values.tsv').open('w') as f:
        f.write('group\tmark\tvalue\tobservations\tin_code16\tin_lear\n')
        for (g, m), c in sorted(direct.items()):
            v, k = c.most_common(1)[0]
            f.write(f"{g}\t{m}\t{v}\t{sum(c.values())}\t{code16.get(g, ('',))[0]}\t{lear.get(g, '')}\n")
    with (OUT / 'tunis_piece_hypotheses.tsv').open('w') as f:
        f.write('group\tpiece\twords\tin_code16\tin_lear\n')
        for g, (p, ws) in sorted(pieces.items()):
            f.write(f"{g}\t{p}\t{' '.join(ws)}\t{code16.get(g, ('',))[0]}\t{lear.get(g, '')}\n")
    with (OUT / 'tunis_external_comparison.tsv').open('w') as f:
        f.write('group\ttunis\tkind\tsource\texternal\tverdict\n')
        for c in comp:
            f.write('\t'.join(str(c[k]) for k in ('group', 'tunis', 'kind', 'source', 'external', 'verdict')) + '\n')
    tally = collections.Counter((c['source'], c['kind'], c['verdict']) for c in comp)
    new_direct = sorted(g for g in plain if g not in code16 and g not in lear)
    new_piece = sorted(g for g in pieces if g not in plain and g not in code16 and g not in lear)
    summary = dict(words=len(rows), groups=n_groups,
                   single_group_words=sum(1 for r in rows if len(r['tokens']) == 1),
                   distinct_direct_plain=len(plain),
                   distinct_direct_marked=len([1 for (g, m) in direct if m]),
                   piece_hypotheses=len(pieces),
                   tally={' / '.join(k): v for k, v in sorted(tally.items())},
                   direct_new_to_code16_and_lear=len(new_direct),
                   piece_new_to_code16_and_lear=len(new_piece),
                   direct_multi_valued=multi_valued,
                   flagged=[dict(word=r['word'], groups='-'.join(r['tokens']), flag=r['flag']) for r in rows if r['flag']])
    (OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps({k: v for k, v in summary.items() if k != 'flagged'}, indent=1))
    print('DIFFER/COMPATIBLE rows:')
    for c in comp:
        if c['verdict'] != 'agree': print('  ', c)
    return rows, plain, pieces, code16, lear



def heldout_lear(seed=20261110, trials=2000):
    """Held-out check: Tunis values (direct + piece) tested on Lear's 1813 interlined spans.

    A Tunis value 'fits' a Lear span when it occurs as a substring of the interlinear word
    (order within the word is not checked).  Groups already in Lear's own direct key are excluded, so
    nothing is counted that Lear's single-group interlines had already settled.  Baseline: the
    same Tunis values dealt at random to the same groups.
    """
    import random, io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        rows, plain, pieces, code16, lear = main()
    tun = dict(plain)
    for g, (p, ws) in pieces.items():
        tun.setdefault(g, p)
    spans = list(csv.DictReader((ROOT / 'output/adjudication_2026-11-06/lear_span_ledger.tsv').open(), delimiter='\t'))
    # the edition's corrected readings for two spans (prior scholarship, noted 6 Nov)
    fix = {'generally': 'fully', 'report': 'reply'}
    tests = []
    for s in spans:
        gs = [g.rstrip('?+^') for g in s['groups'].split()]
        if len(gs) < 2 or not all(g.isdigit() for g in gs):
            continue
        word = norm(fix.get(s['interlinear'].strip().lower(), s['interlinear']))
        for g in map(int, gs):
            if g in tun and g not in lear:
                tests.append((s['line'], word, g))
    def score(assign):
        return sum(1 for _, w, g in tests if norm(assign[g]) in w)
    real = score(tun)
    rng = random.Random(seed)
    gl = sorted({g for _, _, g in tests}); vals = [tun[g] for g in gl]
    base = []
    for _ in range(trials):
        sh = vals[:]; rng.shuffle(sh)
        base.append(score(dict(zip(gl, sh))))
    res = dict(tests=len(tests), distinct_groups=len(gl), fits=real, share=round(real / len(tests), 3),
               shuffled_mean=round(sum(base) / trials / len(tests), 3), shuffled_max=round(max(base) / len(tests), 3),
               misfits=[(l, w, g, tun[g]) for l, w, g in tests if norm(tun[g]) not in w])
    (OUT / 'heldout_lear.json').write_text(json.dumps(res, indent=2) + '\n')
    print(json.dumps(res, indent=1))

if __name__ == '__main__':
    main()
    heldout_lear()

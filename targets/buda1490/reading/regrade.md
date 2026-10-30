# Regrade of the read words (scripts/regrade.py, 30 Oct 2026)

Every word measure.py counts as read, decoded again sign by sign with every value a key allows, and graded by what the reading rests on. B = key.json and the blind key14 (ciphertext only, before the minute was found) both give it; K = key.json gives it, key14 does not; X = only the extended key (retry pass) gives it; C = a code sign, whose meaning rests on the minute alone; D = no key gives the form as read (abbreviation or emendation). Stretches where the alignment crossed the minute's word order are tested as one group in the cipher's order.

Read words 561: B 466, K 16, X 7, C 72, D 0. Independent of the minute (B): 466 (74.7% of the 624 words).

| kind | B | K | X | C | D |
|---|---|---|---|---|---|
| exact | 430 | 15 | 5 | 69 | 0 |
| spelling | 19 | 1 | 1 | 0 | 0 |
| wording | 8 | 0 | 1 | 0 | 0 |
| group | 6 | 0 | 0 | 0 | 0 |
| added | 3 | 0 | 0 | 3 | 0 |

Every read word that is not an exact word graded B:

| line | minute | read | kind | signs | grade | why |
|---|---|---|---|---|---|---|
| P1L01 | non | {non} | exact | Gp | C | code sign Gp = non |
| P1L01 | quam | quam | exact | nq qB tp x | K | key14 differs on tp = a (key14 b) |
| P1L01 | uigesimamquartam | uigesimam | wording | M m O o ooA 4 D F x | B | key.json and the blind key14 give it |
| P1L02 | illustrissimum | {illustrissimumprincipemmeum} | exact | ve | C | code sign ve = illustrissimumprincipemmeum |
| P1L02 | principem | {illustrissimumprincipemmeum} | exact | ve | C | code sign ve = illustrissimumprincipemmeum |
| P1L02 | meum | {illustrissimumprincipemmeum} | exact | ve | C | code sign ve = illustrissimumprincipemmeum |
| P1L02 | cui | cui | exact | 6 M m | K | key14 differs on 6 = c (key14 s) |
| P1L03 | opportunitate | oportunitate | spelling | U 7 N a Q ooA P 4 gB L Q E | B | key.json and the blind key14 give it |
| P1L05 | circa | circa | exact | mH qA Y b L | X | extended key: qA = i/t |
| P1L05 | affinitatem | afinitatem | spelling | F hB m P 4 gB F qA w D | X | extended key: qA = i/t |
| P1L06 | inter | inter | exact | 4 P qA E Y | X | extended key: qA = i/t |
| P1L06 | serenissimum | {serenissimumdominumregemhungarie} | exact | ff | C | code sign ff = serenissimumdominumregemhungarie |
| P1L06 | dominum | {serenissimumdominumregemhungarie} | exact | ff | C | code sign ff = serenissimumdominumregemhungarie |
| P1L06 | regem | {serenissimumdominumregemhungarie} | exact | ff | C | code sign ff = serenissimumdominumregemhungarie |
| P1L06 | hungarie | {serenissimumdominumregemhungarie} | exact | ff | C | code sign ff = serenissimumdominumregemhungarie |
| P1L06 | illustrissimum | {illustrissimumdominummeum} | exact | ve | C | code sign ve = illustrissimumdominummeum |
| P1L06 | dominum | {illustrissimumdominummeum} | exact | ve | C | code sign ve = illustrissimumdominummeum |
| P1L06 | meum | {illustrissimumdominummeum} | exact | ve | C | code sign ve = illustrissimumdominummeum |
| P1L08 | prefatum | prefatu | spelling | 7 Y w s to Q M | B | key.json and the blind key14 give it |
| P1L08 | serenissimum | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L08 | dominum | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L08 | regem | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L10 | ipsam | ipsam | exact | qA Ho qA L D | X | extended key: qA = i/t |
| P1L10 | serenissimus | {serenissimusdominusrex} | exact | ff | C | code sign ff = serenissimusdominusrex |
| P1L10 | dominus | {serenissimusdominusrex} | exact | ff | C | code sign ff = serenissimusdominusrex |
| P1L10 | rex | {serenissimusdominusrex} | exact | ff | C | code sign ff = serenissimusdominusrex |
| P1L11 | commiserat | commiserat | exact | mH gA Ob m ooB E Y to Q | K | key14 differs on Ob = mm (key14 none) |
| P1L11 | animo | animo | exact | to P qA x U | X | extended key: qA = i/t |
| P1L12 | audiuitque | audiitque | wording | to M 5 m 2 Q nq ooA w | B | key.json and the blind key14 give it |
| P1L12 | serenissimum | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L12 | dominum | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L12 | regem | {serenissimumdominumregem} | exact | ff | C | code sign ff = serenissimumdominumregem |
| P1L14 | affinitatem | afinitatem | spelling | L hB 4 3 2 gB F Q w x | B | key.json and the blind key14 give it |
| P1L20 | affectu | afectu | spelling | F hB o mH gB qB | B | key.json and the blind key14 give it |
| P1L23 | affinitate | afinitate | spelling | F hB 2 P m gB L Q o | B | key.json and the blind key14 give it |
| P1L23 | agi | agi | exact | to 3 m | K | key14 differs on 3 = g (key14 n) |
| P1L23 | ceptum | ceptum | exact | mH B H gB qB D | K | key14 differs on H = p (key14 r) |
| P1L27 | efficacius | eficacius | spelling | o hB 2 mH to b 4 qB ooB | B | key.json and the blind key14 give it |
| P1L28 | affectus | afectus | spelling | F hB o mH gB qB ooB | B | key.json and the blind key14 give it |
| P2L03 | affinitas | {affinitasserenissimidominiregis} | exact | Ga | C | code sign Ga = affinitasserenissimidominiregis |
| P2L03 | serenissimi | {affinitasserenissimidominiregis} | exact | Ga | C | code sign Ga = affinitasserenissimidominiregis |
| P2L03 | domini | {affinitasserenissimidominiregis} | exact | Ga | C | code sign Ga = affinitasserenissimidominiregis |
| P2L03 | regis | {affinitasserenissimidominiregis} | exact | Ga | C | code sign Ga = affinitasserenissimidominiregis |
| P2L04 | illustrissimo | {illustrissimoprincipi} | exact | ve | C | code sign ve = illustrissimoprincipi |
| P2L04 | principi | {illustrissimoprincipi} | exact | ve | C | code sign ve = illustrissimoprincipi |
| P2L04 | quoniam | {quoniam} | exact | K | C | code sign K = quoniam |
| P2L04 | quod | {quodab} | exact | dt | C | code sign dt = quodab |
| P2L04 | ab | {quodab} | exact | dt | C | code sign dt = quodab |
| P2L05 | summo | sumo | spelling | qA ooA Om N | B | key.json and the blind key14 give it |
| P2L06 | maiestatem | {maiestatemsuam} | exact | Tx | C | code sign Tx = maiestatemsuam |
| P2L06 | suam | {maiestatemsuam} | exact | Tx | C | code sign Tx = maiestatemsuam |
| P2L06 | sit | sit | exact | ooB 2 gA | K | key14 differs on gA = t (key14 o) |
| P2L07 | regnum | regnum | exact | a o 3 P qB x | K | key14 differs on 3 = g (key14 n) |
| P2L07 | dignitatem | dignitatem | exact | 5 2 3 P 4 Q to gB o x | K | key14 differs on 3 = g (key14 n) |
| P2L09 | affinitatem | {affinitatem} | exact | Ga | C | code sign Ga = affinitatem |
| P2L10 | contraxerat | cotraxerat | spelling | b N gB a to p o Y F Q | B | key.json and the blind key14 give it |
| P2L10 | regno | regno | exact | a o 3 P N | K | key14 differs on 3 = g (key14 n) |
| P2L11 | quod | {quod} | exact | dt | C | code sign dt = quod |
| P2L11 | rex | rex | exact | a o Bd | K | key14 differs on Bd = x (key14 none) |
| P2L13 | affinitas | {affinitas} | exact | Ga | C | code sign Ga = affinitas |
| P2L13 | cepta | cepta | exact | mH o 7 gA L | K | key14 differs on gA = t (key14 o) |
| P2L14 | non | {non} | exact | Gp | C | code sign Gp = non |
| P2L14 | quod | {quod} | exact | dt | C | code sign dt = quod |
| P2L15 | summa | suma | spelling | qA qB Om to | B | key.json and the blind key14 give it |
| P2L15 | maiestatem | {maiestatemsuam} | exact | Tx | C | code sign Tx = maiestatemsuam |
| P2L15 | suam | {maiestatemsuam} | exact | Tx | C | code sign Tx = maiestatemsuam |
| P2L16 | illustrissimum | {illustrissimumprincipem} | exact | ve | C | code sign ve = illustrissimumprincipem |
| P2L16 | principem | {illustrissimumprincipem} | exact | ve | C | code sign ve = illustrissimumprincipem |
| P2L19 | commemoraui | comemoraui | spelling | mH N D o x gA a to M 4 | B | key.json and the blind key14 give it |
| P2L19 | quod | {quod} | exact | dt | C | code sign dt = quod |
| P2L19 | summa | suma | spelling | qA qB Om F | B | key.json and the blind key14 give it |
| P2L20 | deberet | debeat | wording | 5 o tp w to qA | X | extended key: qA = i/t |
| P2L22 | accepit | accepit | exact | to sl w 7 2 gB | K | key14 differs on sl = cc (key14 none) |
| P2L22 | imo quod ambobus | nequeuieataquibus | group | P o oH qB w ooA 2 o to gB F oH qB 4 tp ooA qA | B | key.json and the blind key14 give it |
| P2L23 | prefata | {prefatamaiestasregia} | exact | Tx | C | code sign Tx = prefatamaiestasregia |
| P2L23 | maiestas | {prefatamaiestasregia} | exact | Tx | C | code sign Tx = prefatamaiestasregia |
| P2L23 | regia | {prefatamaiestasregia} | exact | Tx | C | code sign Tx = prefatamaiestasregia |
| P2L23 | affinitatem | {affinitatem} | exact | Ga | C | code sign Ga = affinitatem |
| P2L25 | affirmastis | afirmastis | spelling | to hB 2 a x F qA Q 2 ooB | B | key.json and the blind key14 give it |
| P2L25 | principis | {principis} | exact | ve | C | code sign ve = principis |
| P2L26 | additione | additione | exact | to Od 4 Q qA N P o | X | extended key: qA = i/t |
| P2L27 | quod | {quod} | exact | dt | C | code sign dt = quod |
| P3L02 | centum | {centumquinquagintamilia} | exact | fo | C | code sign fo = centumquinquagintamilia |
| P3L02 | quinquaginta | {centumquinquagintamilia} | exact | fo | C | code sign fo = centumquinquagintamilia |
| P3L02 | milia | {centumquinquagintamilia} | exact | fo | C | code sign fo = centumquinquagintamilia |
| P3L02 | ducenta | {ducentamilia} | exact | y | C | code sign y = ducentamilia |
| P3L02 | milia | {ducentamilia} | exact | y | C | code sign y = ducentamilia |
| P3L02 | extendit | extendet | wording | w 8B Q o 3 5 w gB | B | key.json and the blind key14 give it |
| P3L04 | tantum habere | habereuelittantum | group | s F tp o a w qB o hA 2 Q Q to 3 gB qB x | B | key.json and the blind key14 give it |
| P3L05 | quod | {quod} | exact | dx | C | code sign dx = quod |
| P3L06 | quod | {quod} | exact | dx | C | code sign dx = quod |
| P3L08 | uestitum | uestitu | wording | qB o qB Q 4 gB ooA | B | key.json and the blind key14 give it |
| P3L08 | necessaria | necessarie | wording | P w b o X to a 2 w | B | key.json and the blind key14 give it |
| P3L09 | exponenda | exponenda | exact | o p 7 N 3 w P 5 tp | K | key14 differs on tp = a (key14 b) |
| P3L11 | dignitatem | dignitatem | exact | 5 4 3 P 2 Q to gB o x | K | key14 differs on 3 = g (key14 n) |
| P3L12 | summa | suma | spelling | qA ooA Om to | B | key.json and the blind key14 give it |
| P3L12 | ducentorum | {ducentorummilium} | exact | y | C | code sign y = ducentorummilium |
| P3L12 | milium | {ducentorummilium} | exact | y | C | code sign y = ducentorummilium |
| P3L16 | quod | {quod} | exact | dx | C | code sign dx = quod |
| P3L16 | illustrissimo | {illustrissimoprincipe} | exact | ve | C | code sign ve = illustrissimoprincipe |
| P3L16 | principe | {illustrissimoprincipe} | exact | ve | C | code sign ve = illustrissimoprincipe |
| P3L16 | retrahere | retraere | spelling | Y o Q a F o Y w | B | key.json and the blind key14 give it |
| P3L20 | conditiones | condiciones | wording | b N P 5 2 mH 4 gA 3 w qA | B | key.json and the blind key14 give it |
| P3L20 | serenissimo | {serenissimodominorege} | exact | ff | C | code sign ff = serenissimodominorege |
| P3L20 | domino | {serenissimodominorege} | exact | ff | C | code sign ff = serenissimodominorege |
| P3L20 | rege | {serenissimodominorege} | exact | ff | C | code sign ff = serenissimodominorege |
| P3L22 | quoniam | {quoniam} | exact | K | C | code sign K = quoniam |
| P3L23 | summa | suma | spelling | ooB qB Om to | B | key.json and the blind key14 give it |
| P3L24 | sanguine | sangine | spelling | qB L 3 3 2 P o | K | key14 differs on 3 = g (key14 n) |
| P3L25 | affinibus | afinibus | spelling | to hB 2 3 4 tp ooA qA | B | key.json and the blind key14 give it |
| P3L25 | communem | comunem | spelling | mH N x qB P o D | B | key.json and the blind key14 give it |
| P3L26 | maiestas | {maiestassua} | exact | Tx | C | code sign Tx = maiestassua |
| P3L26 | sua | {maiestassua} | exact | Tx | C | code sign Tx = maiestassua |
| P3L28 | remittet | remitet | spelling | Y o x 4 Q o gB | B | key.json and the blind key14 give it |
| P4L02 | mittantur | mittantur | exact | D 2 wL to P Q qB a | K | key14 differs on wL = tt (key14 none) |
| P4L03 | quod | {quod} | exact | dt | C | code sign dt = quod |
| P4L05 | euenerit | euenit | wording | o qB w 3 2 Q | B | key.json and the blind key14 give it |
| P4L05 | debebitis | debebit | wording | 5 o tp w T 2 Q | B | key.json and the blind key14 give it |
| P4L06 | serenissimi | {serenissimidominiregis} | exact | ff | C | code sign ff = serenissimidominiregis |
| P4L06 | domini | {serenissimidominiregis} | exact | ff | C | code sign ff = serenissimidominiregis |
| P4L06 | regis | {serenissimidominiregis} | exact | ff | C | code sign ff = serenissimidominiregis |
| P1L25 | (added) | non | added | Gp | C | code sign Gp = non |
| P3L02 | (added) | et | added | & | B | & = et in both keys |
| P3L12 | (added) | et | added | & | B | & = et in both keys |
| P3L24 | (added) | quoniam | added | K | C | code sign K = quoniam |
| P4L01 | (added) | quod | added | dt | C | code sign dt = quod |
| P4L04 | (added) | et | added | & | B | & = et in both keys |

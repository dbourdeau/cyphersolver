# K3 version log (Riva-Vienna table). 12 Nov 2026 AEST
K2 = b57 KEY_K2.tsv, md5 24bcb9be... (copied unchanged to work/KEY_K2.tsv). K3 = KEY_K3.tsv. Rule: a value changes only with >= 2 independent contexts. Line ids: pass C unless marked A (WAINUT pass A, 8 Aug letter) or S26 (Starhemberg 20 Mar 1726, b57 pass A).

| # | token | K2 | K3 | contexts (literal K2 decode around the token) | tag |
|---|---|---|---|---|---|
| 1 | 8_ | E | PER | 23r.L13-14 "PER non svegliare li cani che dormono"; 23v.L04 "PER-CHE, PER dirla schietta"; 25r.L13 "che sarà PER dare"; 21r.L09-10 "PER portare ed assistere la causa"; 21r.L13 "tengono PER sicura"; 25v.L09 "è portata PER"; S26 21v.L01 "onorari PER la spesa". "E" fails in each. | [measured] 7 contexts |
| 2 | 10_ | b | MENT (-mente/-mento) | 25r.L10 breve-MENTe; 25v.L05-06 presente-MENTe; 23v.L04 {schietta}-MENTe; 25r.L15 senti-MENTo; A 35v.L16 probabil-MENTe; b57 gloss "positivamente 94 63 73_ 81_ 10_" | [measured] 6 |
| 3 | 70_ | m | TUTTO | 25r.L12 "che TUTTO dipende dal congresso"; A 35r.L13 "con TUTTO lo sforzo"; A 36r.L13 "con TUTTO il calore"; S26 21r.L06 "mandarmi TUTTO quel che può" | [measured] 4 |
| 4 | 53 | ri | gi | 25v.L08 "ma-GI'-o-re" (maggiore); A 36r.L17 "ma-GI-o-re"; A 35v.L13 "p-re-GI-u-d-zi-o"; A 36r.L07 "a?-GI-ta-zi-o-ni"; S26 21r.L04 "havevamo GI[à]" | [measured] 5 |
| 5 | 54 | ro | go | 21r.L13 "te-n-GO-no"; A 35r.L19 "lu-n-GO te[m]po" | [measured] 2 |
| 6 | 55 | ru | gu | 23r.L10 "con-se-GU-e-n-za"; A 35v.L08 "se-GU-e-n-ti"; S26 21r.L14 "con-se-GU-e-n-za" | [measured] 3 |
| 7 | 60_ | l | si | 25r.L13 "a-SI'-s-te-n-za"; 25r.L14 "che lei SI procuri"; A 36v.L09 "fidar-SI punto"; A 36v.L02 "è da temer-SI molto". May be a carelessly closed 63_ (same value). | [derived] 4 |
| 8 | 226 | code | QUEST(o/a; ^3 = questi) | 23r.L08 "QUESTo colpo sarebbe fatale"; 23r.L12 "per QUESTo motivo"; 25r.L11 "a QUESTo punto"; 25v.L07 "QUESTi^3 ... sono di differente opinione"; 25r.L10, 23v.L05 "QUESTa 128" | [measured] 6 |
| 9 | 128 | code | CORTE | 21r.L04 "a cotesta CORTE"; 25r.L10 "in questa CORTE"; 23v.L05 "fidarsi di questa CORTE" | [derived] 3, by sense |
| 10 | 2_, 5_, 20_, 30_, 40_, 50_, 80_, 90_ | e, r, c, d, f, g, n, p | removed (unkeyed -> E) | K2 filled these by table regularity with no gloss. 10_, 70_ and 8_ proved to be word-signs, so the pattern is not safe. 5_ in 25r.L17 "s'è di-[5_]-a-ra-to" cannot be r. | [derived] |

Not changed (fewer than 2 clean contexts): 51 (K2 ra; S26 "onorari", "apertura" support ra, so the g-row rule may not cover 51), 52 (ge? S26 "in-GE-ni-arsi" only), 5_ = CHI (dichiarato, 1), 9_ = SE (1), 40_ = STATO? (2 by sense only, weak), 0_ unknown.
Reading rules added (PARSER.md section 6): ' = doubled consonant or accent (ssi-, -lla, -nno, -ffa-, -bbe, rè, tà, è, sarà: over 40 instances in pass C); ^3 = -i plural on a code.
Codes proposed as annotations only, NOT key values and never counted S: 181 Imperatore (l'181 s'è dichiarato; l'181 non vuole), 147 Mirandola (restituire la 147 al Pico), 196 ministr-, 287 the Duke of Modena / S.A.S. (causa di 287 nel congresso; "di lui speranze"), 254 Spagna?, 259 261 unknown.

## K3.1 (after the 8 Aug letter, pass C2). K3.0 kept as work/KEY_K3.0.tsv (md5 1f4d586d...)
| # | token | K3.0 | K3.1 | contexts | tag |
|---|---|---|---|---|---|
| 11 | 01 (crossed 0 + 1) | none | qua | always before 60 6_: 36r.L04 "QUA-l-che cosa della Mirandola"; 36r.L11 and 36v.L08 "QUA-l-che altra potenza"; 36v.L15 "v'è stato QUA-l-che {faux allarmes}" | [measured] 4. Digit identity of the sign is doubtful, so every instance stays E |
| 12 | 40_ | removed | STATO (^3 = stati) | 25r.L09 "lo STATO dell'affari"; 35r.L11 "danni sofferti dalli STATi di 143 nella guerra"; 36r.L06 "tanto denaro allo STATO di 143"; 36v.L15 "v'è STATO qualche" | [measured] 4 |
| 13 | 162 | code | FAVOR(e) | 35v.L01 "in nostro FAVORe"; 35v.L02 "FAVORe-voli"; 21r.L09 "s'interessi in FAVORe della 261 133" | [derived] 3 |
| 14 | 227 | code | QUEL(lo) | 36r.L02 "più danno di QUELLO che"; 25r.L13 "sarà per dare in QUELLO"; b57 1726 glosses "tutto quello", "quel che" | [sourced] gloss + 2 |
| 15 | 142, 261 | codes | PADRONE, SERENISSIMO | clear text 35r "gl'affari del Ser.mo nostro Padrone" against 35v.L13-14 "al 261 nostro 142"; 142 alone 5 times as subject ("se il 142 farà promuovere") ; 261 133 against clear "Ser.ma Casa" (23v) | [derived] |
Not added: 30_ = ESSER (36r.L14 "non vuole ESSERne principale", 1 clean context), 50_ = ORA (35r.L15 "fino ad ORA", 1), 0_ (3 contexts, no single word fits all: "debito, 0_ che giusto"), 9 (35v.L14), ^2 = -e ("queste potenze", 1).
All code values are E in the strict count whatever K3 says (PARSER.md section 5).

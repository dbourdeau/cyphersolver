# Notes on the code table from the 4 Aug clear text and two re-zooms (11 Nov 2026)

None of these groups is in the report; they concern the table and the sibling transcriptions. [V] = checked on the
image or the clear text; [I] = inference. Source: `check_4aug_output.txt` (misses listed per unit) and the crops
named in `../images.txt`.

| group | table now | proposed | evidence |
|---|---|---|---|
| 701 | mo (M) | mo, firm | 60907 L13 "26 701 594" = "j'aimois" in the clear copy, 60903 [V] |
| 594 | is | is | same place; the 4 Aug gloss "oit" is a slip for "ois" [V clear text] |
| 191 | c'est | c'est (60907 L19, digit no longer doubtful as to sense) | clear copy "[c'est Jalouse humeur qui]" [V]; 791 would give "sois" |
| 791 | sois | ois | 60907 L06-L07 "474 fais 791" = "faisois" in the clear copy [V]; 792 oit, 793 oient follow [V table] |
| 869 | e (M; 4 Aug glosses perdu) | perdu | clear copy "il ne sera point perdu" (60908 L06) [V]; order 867 pense < perdu < 870 perte [V table]. The two 188 readings 869 = e (60917 L02 "Sa-in-te Ma-ri-e", L17 "certain-e") are then most likely 369 = e [I]; on the image the first figure is ambiguous between this hand's 3 and 8 [V] |
| 880 | plus (M) | plustot | clear copy "au plustot" (60908 L07) [V]; 830 is plus; order 874 personne < plustot < 888 pouvoir |
| 829 | pl (187 has a doubtful "pas") | pl | clear copy "plaisoit" (60907 L18) [V]; 824 is pas |
| 169 | cl / com (M) | com | clear copy "compter" (60908 L04) [V] |
| 900 | écrit / pris (M) | pris | clear copy "repris", "surpris", "pris garde" (60907 L06, L16) [V]; the other value comes from 187/188 |
| 974 | répondez (M) | répondu where it stands alone | 60907 L05 "ai 974 que non" = "ai repondu que non" [V]; on 60920 it is followed by 1019 (réponse) |
| 12 | a | a (stands) | 60917 L14 "668 12" glossed "l-a" (la paix); the second figure is a 2, not 8 [V image] |

Also seen [V transcription]: 60909 L13-L14 reads "trois no-ve-m-br-e ... mille sept cent vingt neuf" (3 November
1729), which cannot belong to a letter of 4 Aug 1729; 60909 has no parallel in the clear copy 60903-60904 [V]. It may be
a separate piece filed with the 4 Aug letter [I]; not checked further.

## Round 2 (11 Nov 2026, evening): full-resolution re-reads and the full transcription of mssBLA 194

Sources: `../transcription/sib194_60893.txt`, `sib194_60894.txt`; `check_194_output.txt`; `full_table.tsv` (one row
per group, with every gloss and clear-copy attestation and a conflict flag); crops in `../images.txt` (round 2).

| group | table now | proposed | evidence |
|---|---|---|---|
| 869 / 369 | 869 e (M) | 60917 L02 and L17 read **369** (e); 869 = perdu | full-resolution crops of 60917 [V]: the first figure of both groups has the flat top stroke this hand gives its 3 (as in 387 at the end of L17), not the two closed loops of its 8 (870 on L17, 1268 on L02). The gloss under both is "e" (369 = e in 11 places). 869 is glossed "perdu" in 194 (60894 L01) [V] as well as in the 4 Aug clear copy, so 869 = perdu has two independent attestations |
| 830 / 880 | 880 plus (M) | 60917 L16 reads **830** (plus) | [V] the middle figure has the flat-topped 3 of 438 on the same line; the sense is "plus-ie-u-r-s" (plusieurs), and 830 = plus (60918 L16). 880 = plustot then rests on the 4 Aug clear copy. 60887 L15 is a clear 880 [V crop] glossed "plus" ("écrire plus justement"): check it against the clear 14 July text 60886 |
| 1118 | - (open) | glossed **tain** | 194 L14 "974 163 1118" glossed "reponse cer-tain" [V]; "tain" is written in darker ink over an earlier gloss and the first figure of 1118 is retouched in the same ink. Only glossed occurrence of any open group. See README section 7 |
| 386 | est | est (confirmed) | 194 60894 L01, gloss "dom" struck, "est" written below [V]; supports the report's L01 386 |
| 1049 | sentiment (M) | semble / sentiment, both fit the slot | 194 L03 "semble" (as Brackx) [V]; 60919 L06 "sentiment" |
| 948 | re (M) | ro (194, twice) | 194 L04 "en d-ro-i-tu-re" [V] |
| 974 | répondez (M) | répon- family | 194 L14 "reponse" [V] |
| 475 | falloit | conflict | 194 L02 glossed "favorable" [V]; last figure overwritten (477/479 possible) |
| 491 | force | conflict | 194 L10 glossed "faite", 60894 L01 "force" (sense wants "fais"); 60909 L03 "491 = r" is probably a slip for 941 |
| 433 / 438 | 433 espere (185), 438 été | 433 in 194 L09 by this reading | Brackx lists 194's group as 438 = espere; this hand's 7 and 3 are close, so 433/437/438 all need a re-zoom |
| 835 | pour | pour (once "par") | 194 60894 L03 "par-oit" (paroît) [V] |
| 1135 | travaille (M) | travaille (confirmed) | 194 60894 L01 [V] |

New groups from 194 (not in `codetable.tsv`): 840 pro, 939 quoique, 1159 veu, 1260 (end mark, no gloss); 1118 tain.
`check_194.py`: the table without any 194 gloss matches 89 of 93 firm 194 glosses (0.957; 200 shuffled tables best
0.065; margin 0.893; pass). The four misses are 1049, 948, 974 and 869, all listed above.

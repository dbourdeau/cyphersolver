# DECODE R5318 "Nicodemus": a key sheet for Nicodemo Tranchedini's cipher (ASMi, Archivio Sforzesco cart. 1597)

Brice Dudout, with Claude Opus 5.5 (14 Nov 2026). Image: DECODE R5318 (one leaf, no. 176), seen with DECODE level-2 access.
**No image or crop is included or derived here**; cite it as DECODE R5318.

## The sheet
Heading "Nicodemus"; pencil note at the foot "Chiave della cifra di Nicodemo del gennaio ... 1451" (archivist's date). A later, neat
copy: alphabet a-z with 2-5 homophones per letter (some struck), a syllabary (b c d f l m n p r s t g x five vowels), signs for non, et,
che, ss, per, nn, vv, bb, cc, pp, con, tt, como, 18 nulls ("insignificanti"), and a nomenclator of about 44 entries: denaro, Cosmo,
Duca, Camerlengo, Sig. de Faenza, Sig. Federico, March. de Ferrara, Fiorentini, Gente d'arme, Sig. Malatesta, March. de Mantua,
provisione, **Stantie**, Sig. Sigismondo, la S.V., Toscana, Venetiani, victoria, Io, Venetia, cavalli, fanti, Papa, Romagna,
Collegati, Signore, Milano, Sua Sig.ia, Campo, dice, facto, Ambassadore, Fiorini, Re de Ragona, Italia, pace, dicto, Repubblica,
Fiorenza (four more entries struck out). Two foot lines are almost all struck through.

Transcribed twice: pass A (`R5318_passA.tsv`) and a blind pass B by a subagent (`R5318_passB_blind.tsv`); about 95% agree, the rest
settled on the image at 4x. The settled key is given against the shape labels of `targets/tranchedini1448/dudout/texts/sign_legend.md`
(`key_R5318_by_1448_label.tsv`) so that it applies directly to the labelled texts of both targets.

## It is the 1446 key, nomenclator included (f. 134 glosses)
Every word sign glossed on f. 134 (R7905) is on R5318 with the glossed value:

| f. 134 run | sign | gloss | R5318 |
|---|---|---|---|
| 2 | bent F with a foot | stantie | **Stantie** |
| 3 | bar-o-bar-o | duca | **Duca** |
| 4 | M, then o-dot-o | le gente d'arme in Toscana | **Gente d'arme** = M, **Toscana** = o-dot-o |
| 4 | double comb | non | non |
| 7 | V with a small circle on each top corner | fiorentini | **Fiorentini** |
| 6 | loop-cross, dotted b, m, four circles, bar-o-bar | le compagnie | le, co, m, pa, g |

So the reading of the bar-o-bar-o sign as *duca* in 1446 (NOTES, 5 Nov) is confirmed by a key sheet; on R5318 Venetiani has another
sign (o-bar-θ-bar).

## Against the 1448 table (tranchedini1448, learnt on BnF ital. 1585 f. 28) — `compare.py` → `results_R5318.json`
| | value |
|---|---|
| 1448 labels with an R5318 sign of the same shape | 58 |
| same value (settled crosswalk) | **54 / 58** |
| same value (labels of the blind pass B) | **42 / 49** |
| f. 28 valued tokens decoded right by R5318 | **194 / 222 = 0.874** |
| 200 within-class shuffles of the R5318 values | mean 0.028, best 0.126, z 31.7 |
| coverage of f. 28 / f. 139 tokens through the same crosswalk | 94.6% / 62.1% (same as the 1448 table) |

Differences: bar-o-bar-o = Duca on R5318 but li Venetiani in Feb 1448 (seven times on ff. 28 and 30, where the copies have Venetiani);
6-with-bar-and-dots = na on R5318 (bo in the 1448 table; R5318's bo is the 6 with a bar and no dots, so f. 28 probably has the bo
shape); ħ = bi (ri in 1448); dotted cross = sa (cc in 1448). The gamma sign is *la* on R5318, which explains the a/l tie in the f. 28
votes. Caveat: the settled crosswalk was made knowing the 1448 table; the blind pass B gives the same picture.

So one family, one key with small changes: R5318 is the 1446 state (Duca, stantie); by Feb 1448 the bar-o-bar-o sign stands for the
Venetians (the Duke Filippo Maria died in Aug 1447).

## No held-out measurement
The key was frozen by SHA-256 before any measurement (sha of the settled key 04c8ae96...). No intact held-out portion of at least
300 signs is available today: f. 30 is burnt (measured with the 1448 table), f. 139 has been scored several times and has no clear
text, f. 28 and the f. 134 glosses are training material under 300 signs; the other letters of lead 1317 are not transcribed; ital.
1583 ff. 126/132/133/162 have no image. So no reading is claimed; the sheet gives values and the nomenclator, to be measured on a new
letter.

## Prior art
Not in this repository; the cart. 1597 headings had not been searched for Nicodemo. Not checked: Cerioni 1970 (the Sforza cipher
keys) may print this key.

# Avenel III: the other pieces printed with figures in the same cipher (May 1629 and March 1630)

Checked 20 Nov 2026 (Brice Dudout, with Claude Opus 5.5) with the key of this PR **as frozen at fbc611f8** (letter values
10–38, word codes 39 et, 40 de, 41 que, 42 la; no new value used). PREREG (French) and hashes:
`../avenel3_others_check/PREREG2_fr.md` (sha256 `2060a85e…`), frozen before any figure was decoded.

## Status: existing (Avenel 1858), verified with the key; not measurable

Every run in these pieces carries Avenel's decipherment (a footnote gloss, or, for CCCXVII, the piece printed in clear
and the letter value of each figure of its one unread run). The part with no printed decipherment is 14 signs
(CCCXVII n. 4), under the 300-sign floor: **no test was run**; the numbers below are descriptive.

Figures transcribed from the archive.org page images (`lettresinstructi03richuoft`, leaves given in
`avenel3_others_figures.txt`), every figure read on an enlarged crop; the OCR was used only to find the pages.

| Avenel | Source he cites (checked on the image) | Date | Runs | Signs | Agreement with his glosses |
|---|---|---|---|---|---|
| CLVI | Béthune 9331 fol. 44, original | [1 May 1629], to Bouthillier (doublet of CLV) | 19 | 160 | 0.960 |
| CLXXIV | Béthune 9331 fol. 46, original | [May 1629], to Bouthillier? | 3 | 25 | 0.923 |
| CCCXII | AE Turin XI fol. 136 (Richelieu's draft; Charpentier's partly ciphered fair copy fol. 282) | 5 Mar 1630 | 4 | 37 | 0.950 |
| CCCXIV | AE Turin XI fols. 187, 298 (+ XII fol. 122); Bouthillier's interlinear decipherment | 8 Mar 1630 | 18 | 180 | 0.935 |
| CCCXVI | AE Turin XI fols. 300, 317 (deciphered by Bouthillier) | 9–10 Mar 1630 | 1 (in a note) | 9 | 1.000 |
| CCCXVII | AE Turin XI fol. 323 (not deciphered by the secretary; Avenel deciphered it) | 10 Mar 1630 | 2 (in notes) | 7 + 14 | 1.000 on the 7 |
| CCCXXXII | AE Turin XI fol. 359 | 31 Mar 1630 | 7 | 63 | 0.925 |
| **all glossed runs** | | | 54 | **481** | **0.945** (best of 200 shuffled tables 0.417, mean 0.304; for orientation only) |

What this adds to the nine 1629 letters: the fr. 3829 letter table, unchanged, still reproduces the printed
decipherments of four pieces of **March 1630** from the Turin volume of the Affaires étrangères. Richelieu and
Bouthillier were using the same cipher during the Piedmont campaign.

The single run of `describe.py` counted the bracketed date in the headers of CLVI and CLXXIV ("[1er mai 1629]") as a
one-sign run (decoded "?"); `description.json` therefore reads 161 / 26 / 483 signs and 0.9543 / 0.8889 / 0.9412
(controls 0.4156 / 0.3029). The table removes exactly those two pseudo-signs (each costs 1 for the key and for every
control). Nothing else was corrected and the script was not run again.

## Differences between key and glosses (all visible on the page images)

- **42** is also the article *le / les* in 1630 (*les sis mil*, *les Genevois*, *dans le Milanois*, *les Génois*,
  *les ataquer*, *les Vénitiens*, *le Montf.*); Avenel says so himself: "42 (le ou la)" (CCCXVII n. 4). Already
  *la dégast* in CLIII.
- Misprints or cipher clerk's slips (figure clear on the page, other letter expected): CLVI 23 for s (*Chahteauneuf*),
  19 for 39 (*a* for *et*), r missing (*conteechange*); CLXXIV 17 for 13 (*fres* for *près*, noted by Avenel);
  CCCXIV 12 for 22 twice (*cardigal*, *Mogtf*), 61 for 16 (*marie?*); CCCXXXII 10 for 20 (*cis huit*).
- 20 used as the number in *au 20 mai* (CLVI n. 15), as in CLIII–CLV.

## Code values (from Avenel's glosses at the place; declared, not sure under the 19 Nov rule)

These values are declared here only: they are **not** added to `key.md` or to `final.py` (NOMEN), since under the
owner's rule of 19 Nov 2026 a value fixed from the printed decipherment of the same letters does not make a word sure.
Where they are read below they count as holes.

| Code | Value | Source |
|---|---|---|
| 53 | la reine régnante (Anne of Austria) | CLXXIV n. 4 |
| 89 | la Champagne | CCCXXXII n. 1 p. 604 and n. 1 p. 605 |
| 59 | "duc de Mantoue" (CCCXIV n. 6: *la fille de 59* = Marie de Gonzague, the duke's daughter) | supports the CLVIII reading and Daniel's remark on #813 that 59 means Mantua more broadly; table not changed |
| 63 | unread (Avenel: Marillac or La Force?) | CCCXII n. 6 |
| 41 | *que*, confirmed outside 1629: *ata-que-r* three times (CCCXIV, CCCXXXII) | extension of this PR |

## The one unread run (CCCXVII n. 4)

`42 20 21 12 26 21 30 16 27 13 30 16 21 22` = l· d i g u i e r e p e r i n (Avenel prints these letter values and
leaves "le reste à la sagacité du lecteur"). One possible split: *le Diguière, Perin* ("faite par Lesdiguières; Perin en
est le conducteur"). A hypothesis only: not counted as read.

## Word count (#728, cipher words only, strict rule of 19 Nov)

| Piece | sure / words | share | class |
|---|---|---|---|
| CLVI | 46/50 | 0.920 | read in part |
| CLXXIV | 12/14 | 0.857 | read (floor, 2 holes) |
| CCCXII | 8/10 | 0.800 | read (floor, 2 holes) |
| CCCXIV | 33/44 | 0.750 | read in part |
| CCCXVI | 2/2 | 1.000 | read |
| CCCXVII | 2/5 | 0.400 | read in part |
| CCCXXXII | 16/19 | 0.842 | read in part |
| **total** | **119/144** | **0.826** | |

Holes (25): codes valued from the local gloss (4: 53, 89 ×2, 59 as "duc de Mantoue"), 63 (1), 42 read *le/les* (7),
a corrected figure or a missing letter (9), 20 as a number (1), the unread run (3). With 42 = *le/la/les* admitted on Avenel's statement: 126/144 = 0.875.
41 = *que* (in *ata-que-r*, 3 words in CCCXIV and CCCXXXII) is counted sure here: it was in the key frozen at fbc611f8
before these pieces were decoded, and it was fixed from another letter (CLXVII). Counting it as a hole as well gives
116/144 = 0.806 (no change of class).

Method in Lasry's categories: read from existing decipherment (Avenel; Bouthillier for CCCXIV and CCCXVI).

## Not in this cipher

CCXLV (9 Oct 1629; codes 60, 61, 64) and CCLIII (8 Nov 1629; "10 25 12 11" = *Scot* from the draft) belong to
Châteauneuf's London embassy cipher: another table (60 is not Mme de Longueville there). Not decoded, not counted.

## Limits

Avenel's printed figures only; the manuscripts (Béthune 9331, AE Turin XI) were not seen, so a printer's error cannot be
told from a clerk's. Avenel's glosses were read during the transcription.

# Scan check of the token streams and a held-out test of the frozen v2 dictionary (17 Nov 2026)

By Jozef Krajčovič (kjfriedo), with an AI model (Claude). Licence: CC BY 4.0 for the text, tables and script. Pages cited: Archives nationales, 400AP/144 img 181 (frame `DAFANCH97_MIC032003596`, viewable in the AN viewer and not stored here); Gallica (BnF), NAF 11355. This answers the two conditions in `PROJECT_CHECK.md` §3.

## 1. Token streams compared with the Gallica scan
Source: Gallica `btv1b52517729k`, full-size IIIF images (`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b52517729k/f<n>/full/max/0/default.jpg`).
Note the offset: IIIF `f<n>` = Gallica PDF page n+2. The PDF pages used in `prince_family_tokens_f7_f10_f11_f12.tsv` are therefore:

| folio | PDF page | IIIF | groups | result |
|---|---|---|---|---|
| f7r | 21 | f19 | 13 | all 13 as transcribed |
| f10r | 27 | f25 | 9 | all 9 as transcribed |
| f11r | 29 | f27 | 31 + 27 | all 58 as transcribed; also identical to the Florence copy (400AP/144 img 181) |
| f12r | 31 | f29 | 135 | all 135 as transcribed, line by line (22 lines) |

**Uncertain readings resolved.** The clerk writes 5 as a long ſ. With that:
- f12 line 5 "11ſ0" = **1150** (not 1140); this applies to f12:24 and f12:89.
- f12 line 7 "12ſſ" = **1255**.
- f12 line 13 reads **1216** (the last digit is a 6 with a cross-stroke; 1214 is less likely).
- f11 ancien 1749 stands (the 7 is clear on the f11r scan).

**The count, 133 vs 135.** The scan has 135 groups. The Sardinian clerk's header ("55 parole 133 gro.") is a miscount. No group is doubtful or doubled on the scan, and the alignment needs all 135.

**f11r** has one header ("N° 785 / 10 mots / 58 groupes / 11h45 m.") and no separate header for the nouveau block. This agrees with the Florence copy: one telegram, 4 June, enciphered twice.

**Not compared with a scan:** the clear-text parts of the folios. They were not needed for the groups.

## 2. Held-out test: frozen v2 dictionary against f11r nouveau
- **Frozen dictionary:** `prince_key_dictionary_v2.tsv` as merged in PR #285, SHA-256 `a23bdb32…18c3`. It was built from f7, f10, f11F, r11 and the f12 alignment. Its author had **not** seen the decipherment of f11r (400AP/144 img 181), which was first read on 17 Nov 2026.
- **Held-out text:** the 27 groups of f11r nouveau, with the values written under them on 400AP/144 img 181 (frame `DAFANCH97_MIC032003596`).
- **Overlap:** 11 of the 27 codes are in v2. **10 of the 11 are correct.** The one error is 1344, which v2 had as "ville" (tier C); its value is "pas".
  - By tier: A 8/8, B 1/1, C 1/2.
  - Codes whose v2 value came **only from the f12 alignment** (no external decipherment): 1040, 1344, 1682, 1299, 2041, 512. Of these, **5 of 6** are correct.
- **Control:** v2 meanings shuffled among the 149 v2 codes, 10,000 times (seed 1859). On average 0.21 of the 11 overlaps match; the maximum is 3; never 10. p < 0.0001.
- Script: `heldout_f11N.py`. Its matching is lenient: a value counts as correct if one string starts the other.
- **What the test shows.** Eight of the ten correct codes are tier A, with values taken from other telegrams' decipherments (f7, f10, f11F, r11). They show that f11r nouveau uses this code. The f12 alignment itself is tested only by the six codes 1040, 1344, 1682, 1299, 2041 and 512, and five of them are right. The 1344 correction was made after the answer was seen.

## 3. What follows
- The f12 alignment predicts, in part, an independent decipherment it was not built on: five of the six alignment-only codes are right. This is the held-out stretch `PROJECT_CHECK.md` asked for, with the dictionary frozen in the repository before the test. Six codes is a small test.
- f12:109 = 1344 = **pas**. The sent text at f12:106–112 differs from the minute ("Parme, cette ville a fait son mouvement"). 108 and 110 stay open.
- Still open in f12: groups 87–97, 78, 108 and 110; the 799 conflict; and the tier B and C values that no second text has tested.

# Three blind sign sheets on vol. 196 fr. 0018, 0065, 0071, 0064 and 0056 (24 Nov 2026, Brice Dudout, with Claude)

Each target is a glyph where the letter read in the aided alignment (nov1 / nov9, Payne and the readings integrated
here) differs from the letter the known key (COME RETRIBUTION) predicts. The key and the alignments are unchanged.

Brice Dudout saw each target as a cropped sign next to real examples of the candidate letters from the same clerk.
The forms were unlabelled. Every rule was written and hashed before any thumbnail was cut (in French, byte for byte
as hashed). The keys were opened only after the answers were exported.

| sheet | frames | rule (SHA-256) | targets | controls |
|---|---|---|---|---|
| A | 0018 | `sheet-A-rule.md` (9e914605...) | 14 | T, C, R: 3/3 |
| B | 0065, 0071 | `sheet-B-rule.md` (9602d769...) | 15 | K, B, Z: 3/3 |
| C | 0064, 0056 | `sheet-C-rule.md` (a51d2e22...) + `sheet-C-rule-amendment-1.md` | 10 | G, U, B: 3/3 |

Sheet C's amendment 1 withdrew target 0064 g6p1, because of a pencil mark on the sign. Results are in
`sheet-*-results.tsv`. Their columns are in French: lieu = glyph, lu = letter read, cle = letter of the key,
reponse = answer, statut / verdict = effect.

## Results
- **Re-read as the key predicts (29).**
  - 0018: F at g1p2, g5p4, g10p3, g12p2, g18p2, g24p4, g25p3; L g11p4; M g9p1, g15p2; E g14p1.
  - 0065: g2p3 I, g5p5 F, g13p5 M, g17p4 M.
  - 0071: g5p2, g5p3, g8p5, g8p6, g9p7, g9p9 F; g9p8 M.
  - 0064: g8p5 K, g9p2 L, g14p8 L.
  - 0056: g9p4 F, g9p5 L, g17p5 V, g18p2 I.
- **Divergences confirmed as the clerk's own (8).**
  - 0018: g16p2 E, g7p2 V, g12p1 V.
  - 0065: g14p1 T, g19p1 T.
  - 0071: g13p4 N.
  - 0064: g9p3 T, g10p1 T.
- **Unresolved (2).** These are not integrated.
  - 0065 g15p2: the form chosen was T, which is neither the read I nor the key F.
  - 0056 g6p1: the form chosen was P, a distractor option with the shape of a sure P on the page.
- **Alphabet note (sheet A).** The F option showed two examples, and Brice noted that only the first is right. The
  second (g4p1, the F of FIM) has no lower bar and a shorter stem. It is labelled F2 (no value), and g4p1 takes its
  value from sense only ({probable}). The seven F answers match the first form. Brice confirmed q07 and q16 (F).

## Effect (words no longer marked [?] in `*_read_measure.txt` and `*_reading.md`)

| frame | before | after | now unmarked |
|---|---|---|---|
| 0018 (to Beauregard) | 22/44 | **28/44** | BRANTLEYS, EXPIRE, THESE, TOTAL, OVER, TWO |
| 0065 (to Maury) | 11/18 | **15/18** | FOR, EIGHT, THOMAS, RELIEVING |
| 0071 (Surget) | 9/14 | **12/14** | MOBILE, COMPEL, EVACUATION |
| 0064 (personnel) | 8/13 | **9/13** | RESERVES (last word) |
| 0056 (to D. W. Adams) | 19/27 | **22/27** | MONTGOMERY, ENGINES, SUPT |

The words still marked keep their meaning-based reading ({probable}). Groups g26-g49 of 0018 were not segmented, so a
further sheet could cover them (E/F, N/M and I/L recur there).

No image or crop is committed (NARA, public domain).

## Credit
- Reading and alignment: Bryan Payne (PRs #186, #205) and the nov1 / nov9 readings integrated here.
- Blind reader of the signs: Brice Dudout.
- Sheets built, scored and integrated by Claude (AI agent).

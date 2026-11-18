# 90R-93L: strict recount with key_c02 after its passed test, image re-reads, conjectured missing values (17 Nov 2026, later)

No new measure; key_c02 (SHA-256 `1813621c87e8...`) is unchanged; no portion was used for a test. Reading only.

| file | what it is |
|---|---|
| `sense_values_vs_period_clears.tsv` | the 48 key_c02 values read by sense in this letter (+ the withdrawn 558), checked against the six system A letters that have a period clear, by the monotone alignment of `../../keyc02/scripts/align_learn.py` run with key_c02 unchanged (the May and August clears are burnt for tests; they are used here for reading only): 35 are met at least once where the clear agrees; **13 are never met in a clear** (167, 174, 217, 248, 274, 275, 416, 417, 443, 492, 607, 617, 661) |
| `conjectures_key_c02.json` | 30 values for groups absent from key_c02, each with its source (what the clears emit, the alphabetical place in this one-part code, the sense). Not part of the key |
| `decode_90R-93L_key_c02_reread.txt` | decode with key_c02 after the image re-reads (92 groups of 1,585 unknown) |
| `decode_90R-93L_key_c02_plus_conjectures.txt` | the same with the conjectures in braces (54 groups still unknown) |
| `reading_90R-93L_key_c02_strict.txt` | the strict tagged reading |
| `count_words.py` | the word counter used for both letters |

## Image re-reads (full-size image, two looks)
- 90R02 g8: 393 -> **323** (the scribe's open 3); with 93L01 it gives "chagrin(s)" twice.
- 91R13 g10: 930 -> **233** (first digit 2, middle open 3): "rendre mes devoirs" (233 = 'dre' in key_c02).
- 90R02 g7 (192/193/194) and g13 (590/650) stay ambiguous by form.

## Strict count (Daniel's rule, answering the review point on the sense values)
Words resting on one of the 13 sense-only values are now **probable**, not sure; words resting on a conjectured value are probable. Words with 109 "ac" are also kept probable: it is met once in a clear, but 92L03 needs "at" ("attribuer").
`python3 -I count_words.py reading_90R-93L_key_c02_strict.txt`: **651 sure + 81 probable of about 860 words: sure 0.757, sure + probable 0.851.**
The same counter on the earlier tagged file gives 679 sure + 23 probable of about 876 (0.775 / 0.801; the "698 / 0.78" of the earlier note
counted elided forms differently). The letter stays **read in part**. The 95 % of sure words is not reachable with key_c02 alone: 92 groups are
absent from it, and the unresolved spans (about 128 words) sit mostly on them.

## The date
The letter opens 96.70 (nulls) 171.732.727.710 and 90R02 has "votre lettre du 732.727.703". Groups above 700 are numbers and months in this code
(720 premier, 721 deux, 726 sept, 729 dix, 709 février, 713 juin, from the clears), so the letter is dated in cipher; the values of 727, 732,
703 and 710 are not known, so the date stays unread.

## 18 Nov 2026: blind digit-form check (Brice Dudout, sheet of 17 Nov evening)
Nineteen groups doubtful by the form of one digit were shown framed alone, with reference digits of the same hand and four control digits of
sure groups (**4 of 4 controls right**). Nine of the nineteen answers go against the sense: the scribe may have slipped or the key_c02 value
may be wrong; this is not settled (no new measure, key unchanged). A word contradicted by the form is not made sure; it stays probable if it was.
Applied in `reading_90R-93L_key_c02_strict_plate1711.txt` (the file above is kept): 90R09 357 "inutiles", 90R17 396 "l'", 92L02 374 "doit",
92L15 538 "jusqu'ici" become sure; 92L12 606 (0, absent from key_c02) makes "peu" probable and 92R17 574 (4, absent) makes "sans" probable
(each had been counted sure plus one unresolved word); 90R02 193 ("chagrin") and 91L03 616 ("forte") go against the sense and stay probable;
91R13 218 ("devoirs") is confirmed. **Count: 654 sure + 80 probable of about 858 words: sure 0.762, sure + probable 0.855: read in part.**

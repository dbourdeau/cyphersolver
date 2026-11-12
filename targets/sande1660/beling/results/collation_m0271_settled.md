# m0271: the two readings collated, and each disagreement looked at on the image

A = the first reading (`transcription/m0271.txt`, made by a reader who knew the key table).
B = the blind second reading (`transcription/m0271_r2.txt`, 12 Nov 2026, an AI agent in a separate context that was
given only the scan and the glyph notes; it did not see A, the reading, key.txt or any decryption).
The token-by-token list is `collation_m0271.txt` (from `scripts/collate_m0271.py`).

[V] = seen on the image (DigitArq JPEG, crops at 3x-7x by the collator); [I] = settled by context (the word the
decrypt must make), not by the image.

## Agreement [V, output]
Both readings have 1,225 tokens. 1,202 tokens are identical and aligned (0.981 of A). 21 places differ (23 tokens).
B scores 0.765 under the round-1 rule (A: 0.782); see `test_round2_result.json`, `secondary_m0271_r2`.

## The 21 disagreements

| Id (line.n) | A | B | On the image [V] | Settled |
|---|---|---|---|---|
| 01.1 (pos 16) | 3 | 5* | an S-like sign with a heavy left stroke; 3 or 5 on the image | [I] 3 ("escreuo a uos") |
| 01.2 (pos 20) | 3 | 31* | a 3 with a short upright joined on its right, no dot, then a blotted 1 before 22 | [I] 3 ("vosa exelensia" needs a); the upright is not a separate sign |
| 02.1 (pos 1) | 9 | 19* | a short tick high before the 9, not a full 1 like the 19 four signs later | 9 [V]; [I] "sobre tudo" across the line end |
| 02.2 (pos 27) | 27 | 22* | the shape is the same as the 27 at the end of the same crop | 27 [V, I "empenho"] |
| 03.1 (pos 14) | 7* | 17 | a dark 1 stands right before the 7 hook, no dot; a reddish show-through blob before it | A is wrong to read 7 alone: 17 or 1.7. Open |
| 03.2 (pos 27) | 27 | 22 | second stroke closed with a short foot, between this hand's 22 and 27 | [I] 27 ("de grande") |
| 04.1 (pos 15) | ?.3 | 23* | a z-shaped stroke joined to a 3; it matches the 5 of 13.5.3 at the start of the crop | [I] 5.3 ("seria que"); neither ? nor 23 |
| 07.1 (pos 10) | 3* | 32* | a 3 with a tail or a small x after it | open (3 or 32) |
| 08.1 (pos 11) | ? | 2* | a light 2 between 20 and 19 | 2 [V]; [I] "a frota do [102]" |
| 10.1 (pos 10) | 62 | 6.2 | no dot visible between 6 and 2; the 6.3 just before has one | 62 [V], 6.2 not excluded |
| 10.2 (pos 18) | 2 | 12 | a faint upright before the 2, lighter than the ink: show-through | 2 [V]; [I] "como geral" |
| 10.3 (pos 28) | 27 | 29* | the hook is closed into a loop like a 9 | [I] 27 ("-mente") |
| 10.4 (pos 31) | 61 | 6.1 | a dot on the line between 6 and 1 | **6.1** [V]; [I] "se de-pende" across the line end. A was wrong |
| 12.1 (pos 22) | 27 | 22 | second stroke rounded with a base: looks like 22 | [I] 27 ("depende"); variant 27 |
| 16.1 (pos 27) | ? | 16* | a faint 4 with a heavy 6 written over or after it (a correction) | open |
| 18.1 (pos 6) | 27 | 25* | the same S-tailed 2-sign as at pos 8 (which both read 25) | [I] e both places ("deferirão"); see unkeyed_numbers.md |
| 20.1 (pos 27) | 27* | 22 | rounded second stroke with a base, like 22 | [I] 27 ("que pode"); variant 27 |
| 21.1 (pos 7) | ? | 6* | a heavy blot with the outline of a 6 | open (6 likely; word unclear) |
| 21.2 (pos 21) | 27 | 22* | blotted, with heavy show-through | [I] 27 ("ninguém") |
| 24.1 (pos 29) | 20 | 26* | a 2 and an o with an entry stroke: reads as 26 or 20 | [I] 20 ("faltar") |
| 36.1 (pos 8) | 6.5 | 65 | no dot; the 5 tucked under the 6's flourish | **6.5** [I] ("diferenças"); A right |

Summary: of 21, the image alone settles 6 (02.1, 02.2, 08.1, 10.1, 10.2, 10.4); context settles 11 more
(01.1, 01.2, 03.2, 04.1, 10.3, 12.1, 18.1, 20.1, 21.2, 24.1, 36.1), and 4 stay open (03.1, 07.1, 16.1, 21.1;
21.1 looks like 6 but the word is not clear). One clear error in A (10.4: 61 for 6.1) and one probable
(03.1: 7 for 17 or 1.7); A's reading stands in the other places, or a third reading (04.1: 5.3) replaces both.
B's "22" in five places (02.2, 03.2, 12.1, 20.1, 21.2) is a real shape: a 27 whose second stroke is
closed with a foot. Every one of the five stands where the word needs e. It is treated as a variant of 27, not as x.
The scored file `m0271.txt` is not changed (frozen); these corrections are for the reading only.

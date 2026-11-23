# Independent check of the second Whitworth 1708 test

Checker: an AI model, Claude Opus 5.5 (Anthropic), acting as an independent checker at the orchestrator's request.
Started Sun 22 Nov 2026 21:23 EST (from `date`). No person has checked this report.
Brief: try to break the reported PASS. Nothing was edited, deleted, posted or uploaded. Images were only viewed with the Read tool.

## a. Hashes
All 17 files listed in plans/HASHES_2.txt match their sha256 (`shasum -a 256 -c`). test2/table2_frozen.tsv hashes to
4f39e3e8...422f, the value in table2_frozen.sha256 and run2_stdout.txt.

## b. Reproduction
Scratch copy at test2/verify_scratch/ (scripts/, transcriptions/, empty test2/), `python3 -I scripts/run_test2.py`,
3 min 28 s. Output is identical to test2/run2_stdout.txt apart from the freeze timestamp: table sha256 4f39e3e8...422f,
2,579 bytes, 246 entries (S 139, A 62, B 45), byte-identical to the original; held-out groups 112, covered 78, hits 69,
H 0.885; control 1 median 0.10, p95 0.15, p99 0.17, max 0.22; control 2 max 0.14; verdict PASS. Reproduced.

## c. Code review: leakage and inflation
- Leakage: none found. The table is built only from spo_f090/f110_deciphered.txt, merged_f112/f114.tsv and
  adjudication.tsv (all last changed 21 Nov, before the f049 transcriptions of 22 Nov 21:13). wlib.py and wlib2.py never
  name an f049 file; run_test2.py opens runs_f049.json only after writing and hashing the table. The print file
  sbornik50_no22 is not read by the script at all (the print words come in via runs_f049.json).
- One soft point, not a leak: wlib2.py and run_test2.py were written (21:15-21:17) after the f049 transcriptions existed
  (21:13), so the rule could in principle have been tuned with them in view. The plan says the method check used building
  letters only; I found nothing in the code that touches f049 before the freeze.
- Scoring: score_run is permissive for groups not in the table (any 1-16 letters), and a short table value can fall
  into place easily. Control 1 deals the same values (short ones included) to other numbers and gets only 0.10-0.22,
  so short values do not by themselves produce the score.
- Hit breakdown by table-value length (from heldout_reading.tsv, 78 covered groups):
  one letter 15 hits of 17 covered; two letters 23 of 25; three or more 31 of 36.
- H counting only hits and covered groups with values of three or more letters: 31/36 = 0.861.
  Re-scoring with the table cut to values of 3+ letters (143 entries): covered 36, hits 31, H 0.861, control 1 (300
  shuffles) p99 0.11, max 0.14. With values of 2+ letters: covered 61, hits 54, H 0.885, p99 0.11. The pass survives
  both cuts, though at 36 covered groups the 3+ subset alone would be under the plan's 40-group floor.
- By tier: S 48/51, A 16/18, B 5/9.

## d. Hand settings (overrides_f049.tsv)
All five look fair and none hands the test a hit:
- "if" (MS) for "as" (print): only fixes where run 2 ends; no code value involved.
- "allways" merge: the MS line reads "own 630 116 607 907 121 366 allways 154 461 265 1415"; merging the two stretches
  costs the test, if anything (see 907 below).
- "awake"/"awaken", "concernd"/"concerned", and ignoring the MS's clear "the": simple boundary matches from clear words.

## e. Held-out letter images (f049 page 2 strips 1-3, page 3 strips 3-5)
Seen on the images: all nine missed groups read as transcribed: 51, 859, 219 (partly under the stamp, still 219),
1470, 36, 907, 363, 505, 236. Ten (in fact more) others also agree: 689, 141, 1237, 496, 650, 645, 365, 91, 697, 439,
241, 1194, 31, 563, 750, 153, 123, 354, 56, 630, 116, 607, 121, 366, 154, 461, 265, 1415, 499, 1235, 479, 580, 177,
81, 200, 134, 474, 679, 421, 297, 205, 49, 204, 323, 239, 935, 589, 380. No disagreement found.
(587 after "awake" on p3 L22 has a looped 7 that could be taken for 4 at a glance; the other 587s settle it as 587.)

Inferred, not seen: several misses look like differences between the manuscript and the 1886 print rather than table
errors:
- 1470 "muscovi": the office spells "Muscovites" (f090 p4: "Muscovites" above 1470.239); the print has "moscovites".
- 36 "a" with 153 "ba" (153 stands under "bargain" in f110): "to 36 153 123 354 56" reads "to a ba t t le": the cipher
  likely has "to a battle", the print "to battle".
- 363 "ur": "ill hu mo ur ed": MS likely "humoured", print "humored".
- 51 "d", 859 "engag": spellings "warnd"/"engag(e)" style.
- 907 "person": table reads "[630 116] and person s will allways be safe": the cipher likely has "effects and persons",
  the print "persons and effects".
- 236 and 505: see f.

## f. Building-letter images (crops_spo)
- 219 = po (tier A): f110 p3 L14, "Archangel post" written above "1415. 219. 236."; 219 also stands in expose, positive,
  points, potent. Supported (as part of "post").
- 236 = post (tier S): CONTRADICTED as a whole word. Seen: "post" is written above 1415.219.236 with the word sitting
  mostly over 236. Inferred: 219 = po and 236 = st, because 236 stands in brimstone, distroyed, masters, stipulate,
  "Mr Stiles" (seen: "from Mr Stiles" above 637.320.236.74, f110 p3) and assistance. The tier S rule took the helper's
  attachment of "post" to 236 alone. Right value: st. In the held-out letter "they do not 935 236 496 they are" fits
  "...under-st-and"; with 236 = st the test gets 70/78 (H 0.897), so this error cost the test a hit, it did not give one.
- 505 = court (tier S): SUPPORTED. Seen: f090 p4 L12 "the Court" above "469. 505."; f110 p3 L16 "this Court" above
  473.505. In the held-out letter 505 sits where the print has "seeming" ("se 399 505 to o much"); the image reads 505
  clearly. The building letters cannot settle why; either the despatch's text differs from the print there or the clerk
  used 505 differently. Counted as a miss, which is the conservative way.
- 36 = a (tier B): f110 p2 L11, "gratitude" above "296. 36. 240." (seen). Consistent with gr-a-ti(tude) but cannot
  settle the split by itself; the held-out "to a battle" reading above supports it.
Ten further entries:
- Tier S, all supported by the image (word written over the number): 637 from, 320 mr (f110 p3 L13); 1415 archangel
  (f110 p3 L14 and f090 p4 L11 "at Archangel" over 265.1415); 481 well, 304 if (f090 p4 L11).
- Tier A/B, all consistent, none contradicted: 1470 muscovi (B; "Muscovites" over 1470.239, split cannot be settled);
  155 bi (A; "binding" over 155.94.51, also supports 94 n, 51 d); 231 se (A) and 55 e (B) ("they see" over 589.231.55,
  f090 p4 L16); 225 re (A; "the remaining" over 357.225.201.417, f110 p2 L14).

## Verdict
The PASS stands. Numbers reproduce exactly; no route for the held-out letter into the table; hand settings fair; my
reading of the f049 images agrees with the transcription at every group checked. Hits are not carried by one-letter
values (3+ letter values alone: 31/36, H 0.861, control p99 0.11). One table entry is wrong (236 should be st, not
post), from the tier S rule trusting a single attachment; it lowered the score. The sample is small (78 covered
groups) and the test confirms the office's decipherment, as the plan says, not an independent solution.

Scratch: test2/verify_scratch/ (reproduction; extra/restricted.py for the length cuts).

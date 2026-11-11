# Batch 4: interlined code pages, King despatches (NARA M30), rolls 5-6

Output: `batch4_spans.tsv` (tab-separated: frame, page L/R, line, span_no, groups, interlinear, placement, note).
Made from the local images only, by cutting full-resolution strips with `sips`; no key or word list was consulted or applied while reading digits.

## Conventions

- `line` counts only lines that carry code groups (plus a few rows of clear text in braces that begin or end a code line, and catch-words/catch-groups at the page foot, which get their own line number).
- A row holds the group or groups a word physically stands over. A group with nothing above it has an empty interlinear and empty placement.
- `placement = ambiguous` means the word does not sit squarely over the group(s) of its row: it straddles two groups, sits over a gap, or the whole line is visibly shifted against its words. The note says where the word actually stands. On these pages the clerk wrote the words loosely, often half a group left or right of their figures, so the ambiguous rows should not be used as equations without checking the neighbours.
- A word followed by `——` has a rule drawn on over further groups; hooked rules drawn UNDER a group (frame 0140) are noted, not treated as spans.
- `?` after a group = at least one digit doubtful (alternatives in the note). `_` = digit hidden in the binding/gutter (leading or trailing, as the note says). `{...}` = words written in clear on the code line. `[379]` = group the pen itself enclosed in brackets.
- Marks: `^` caret-like mark after a group.

## Hands

- Frames 005-0139, 005-0140: King's own hand; image heavily thresholded, 4s fill in and look like L, several groups blotted by show-through.
- Frames 005-0212, 005-0213, 005-0218 (No. 4, Triplicate): a clerk's copy hand. His 9 is a q, his 5 is a small bowl with a detached flag or cap, and he writes 8 two ways: a plain figure-eight, and a single open loop with a tail rising to the right. The capped-oval 5 and the one-stroke 8 can be confused; the groups under "Mr Pitt" are written 128. 55. 28 plainly at 0213 R line 8 and 0218 R line 1, and less plainly (flagged `?`) at 0212 lines 2 and 8 and 0213 R line 1.

## Per frame

### M30-005-0139
- Visible: right page headed "London Aug. 16. 1798", "Dear Sir" (to Murray; addressee line in code at foot: 562 738 301 &c.); left page is the end of another letter, signed Rufus King.
- Left page 4 code lines, right page 24 code lines plus a catch-group; 302 groups.
- Doubtful: L 378? 532? 147? 528?; R 334? 1513? 529? 564? 1106? 231? 394? 1100? 1383? 1253?; leading digits hidden in the binding at R lines 20-23 (_56, _5, _7, _24), first digits half hidden at R lines 17-19 (964, 554, 571).
- Spot check (R line 2-3 left half, R line 6 right half, R line 2 right half re-cut and re-read): two slips fixed, 334 -> 334? (first digit 3 or 5) and 1513 -> 1513? on line 2.

### M30-005-0140
- Visible: no date (continuation of the 16 Aug 1798 letter; catch-group 644 begins the page); signed Rufus King.
- Left page 15 code lines; 152 groups. Right page blank.
- Doubtful: 554? (three times, blotted), 1097?, 520?, 375?, 561?, 147?, 339?, 499?, 273?, 1046? (second digit written like 6), 1150?; line ends lost in the gutter: 98_ (twice), 7__ (twice), 76_, 41_, 36_, 72_?.
- Spot check (gutter strip of all 15 line ends, and lines 10-11 right half re-cut): no wrong digits found; gutter groups refined.

### M30-005-0212
- Visible: "No. 4. (Triplicate)", "London Octo. 10. 1798.", "Dear Sir", foot "Secretary of State &c &c &c".
- Right page 13 code lines (mixed with clear text); 107 groups. Left page is a printed/ruled abstract form, no code.
- Doubtful: 128? 55? 28? (line 2), 128? 55? (line 8), 1205?, 437?, 881?, and the blotted pair 650? 123? on line 7 (overwritten; cf. 0218).
- Spot check (lines 2, 4, 7, 8 re-cut at higher enlargement): no slips in digits; the 5/8 glyph question written up above.

### M30-005-0213
- Visible: continuation of No. 4 (Triplicate); no date on the opening.
- Left page 17 code lines plus cut catch-group, right page 19 code lines; 243 groups.
- Doubtful: L 125? (Grenville), _86 (first glyph malformed), line ends in gutter 118_, 1__, 2__, 107_, 125_, 54_, 4__, 64_; R 128? (line 1), 125? (blot, line 3), 1? (line 7, may be a stray stroke).
- Spot check (gutter strip of the left page and lines 3 and 9 re-cut): no slips found.

### M30-005-0218
- Visible: continuation of No. 4 (Triplicate); mostly clear text.
- Left page 5 code lines, right page 1; 25 groups (incl. one bracketed repetition [379]).
- Doubtful: 548? (overwritten).
- Whole frame read twice (overview and strips); no slips.

### M30-005-0234
- Visible: no date or number on the opening (left page top in clear about French Directoire despatches concealed in tubs; survey gives Oct-Nov 1798). Clerk's copy hand (9 written as q), interlineations in a darker pen, heavy show-through.
- Left page 17 code lines, right page 20; 190 groups, much clear text between them (given in braces).
- Doubtful: L 1416?, 506?, 710? (line 7), 342?; R line 1 almost wholly blotted (1410? ??? 532? 944?: the group under "Portugal" is illegible and entered as `???`), 833? (twice), 321?, 88?, 728?, 1430?, 1375? 818? (under "fearful").
- Spot check (L lines 7-8 and R lines 15-16 re-cut): no slips; one row split (817 "three" / 951 "months").

### M30-005-0239
- Visible: no date or number on the opening (survey: Nov 1798); left page mostly clear (Union with Ireland, Levant trade), code begins four lines from its foot.
- Left page 4 code lines, right page 18 code lines plus catch-group 868; 170 groups.
- Doubtful: L 1__ and 12_ at the gutter; R 10? (line 13), 1086? (line 14), `???` under "afford" (line 16, blotted, about three digits), 410? (410/418, line 17), 609?.
- Spot check (R lines 1-3 right half and R line 10 re-cut): no slips.

### M30-005-0240
- Visible: no date (end of the same despatch as 0239: begins on its catch-group 868); signed Rufus King; P.S. in clear on the right page, signed R.K.
- Left page 15 code lines (several of one to four groups among clear text); 83 groups.
- Doubtful: 1416? (line 9, 6 or 0), 1589? (twice, third digit overwritten or crossed), 834?.
- Spot check (lines 3 and 7 re-cut): no slips.

### M30-005-0246
- Visible: no date or number on the opening (survey: c. 7 Dec 1798); left page mostly clear (Malta, Minorca, Elgin, Grenville's mission), code begins four lines from its foot (St Domingo, Maitland, Toussaint).
- Left page 4 code lines plus catch-group 1233, right page 20 lines carrying code; 141 groups.
- The right page is badly blotted by show-through from line 14 down. Doubtful: L 1051?; R 1233? (line 1), 28?, 345?, 794?, 786? 691? (under "Rigaud"), 1128? (line 12, where 1288 would be expected from the parallel passages), 1423?, 1021? (twice), 1259? 1031?, 1051? 321? 969? (line 16), 709? (twice), 1056?, 10? 784? (line 19), 368? 769? 1572? (line 20). Two stretches entered as `???` (line 17 after "as", line 18 after "with") are cancelled or blotted beyond reading: one or two groups each, not counted reliably.
- Spot check (R line 2 and R lines 7-8 re-cut): no slips.

## Counts (from the TSV)

```
M30-005-0139 lines 29 groups 302 single 166 multi 35 doubt 18 amb 40
M30-005-0140 lines 15 groups 152 single 88 multi 17 doubt 21 amb 21
M30-005-0212 lines 13 groups 107 single 65 multi 10 doubt 10 amb 15
M30-005-0213 lines 36 groups 243 single 149 multi 26 doubt 13 amb 13
M30-005-0218 lines 6 groups 25 single 10 multi 5 doubt 1 amb 1
M30-005-0234 lines 37 groups 190 single 97 multi 28 doubt 16 amb 2
M30-005-0239 lines 23 groups 170 single 74 multi 29 doubt 7 amb 2
M30-005-0240 lines 15 groups 83 single 49 multi 12 doubt 4 amb 2
M30-005-0246 lines 25 groups 141 single 55 multi 23 doubt 26 amb 8
TOTAL {'groups': 1413, 'single': 753, 'multi': 185, 'doubt': 116, 'amb': 104, 'lines': 199} rows 1398
```

## Not done

Frames not transcribed in this batch: M30-005-0247, M30-006-0009.

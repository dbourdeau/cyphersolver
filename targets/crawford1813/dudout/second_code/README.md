# Crawford 1813: the second code (the = 285) is the JQA code with its blocks reversed, not WE025

Brice Dudout (with Claude Opus 5.5), 16 Nov 2026. A test of a lead from Andrew Beling's peer review: his
`../../../crawford1814` reads Crawford's private letter of 5 Nov 1814 in WE025 (Weber 1979; Poinsett's code). Could
Crawford's other 1813 code be WE025 too?

## The material

Besides the JQA code (the = 1385) of the 15 Aug 1813 letter, Crawford's despatches of 1813 on NARA M34 roll 17 use a
second numbering: the = 285, of = 76, to = 1069, Emperor = 1516. It is on frames 0035 (Paris, 8 Sept 1813), 0056 (right
page) and 0070 (both pages; a clerk's copy, "Signed Wm H Crawford", which mentions the Senate's grant of 300,000 men).
All three carry a contemporary interlinear decipherment, word by word over the groups. The images are NARA, public domain
(e.g. https://catalog.archives.gov/medialz/dc-metro/rg-059/603720/M34/M34-017/M34-017-0035.jpg).

`interlinear_pairs.tsv`: 152 word units (one or more groups under one interlinear word), taken where the alignment of
word and groups is clear; 0035 in full, 0056R and 0070 in part. One transcription pass, frozen by sha256
(7aec7785...) before any key was applied to these numbers. No key was fitted on it.

## Test 1: WE025 (fails)

Written down before the run (sha256 of the protocol caf27d9d...): key = the WE025 rows public here (the union of
`poinsett1813/beling/key/we025_poinsett.tsv` and `crawford1814/key/we025_crawford1814.tsv`, 419 numbers; the full table
is not in the repository), measure = agreement with the interlinear on covered units, 200 within-class shuffles, bar
M >= 0.85 and >= best shuffle + 0.30. Seen before the protocol: WE025 has 285 = be, 1355 = the, 65 = emperor.

`python score.py we025` -> 65 of 152 units covered, **3 agree (M = 0.046)**; shuffles best 0.092. **WE025 is not the
second code.** (The three agreements are 284 = that, which the two codes share by chance of arrangement.) An exploratory
scan of constant offsets n -> n+k gave 26/38 at k = 1070 (285 + 1070 = 1355), but this is the repeated "the" alone; the
offsets of the other words scatter (of +1321, to +485, which +1548...).

## Test 2: the JQA table under morris1813's block reversal (passes)

The three anchors fit `../../../morris1813` (WAINUT, PR #114; Beling): Morris's copy of the State Department code is the
JQA table with its sixteen blocks of 100 in reverse order, Morris 100*i + r = JQA 100*(15-i) + r; JQA 1385 the -> 285,
1576 of -> 76, 16 emperor -> 1516. Protocol written before the run (sha256 03ed336b...): key = `../../../jqa/code_table.tsv`
under that formula, nothing fitted; units containing the anchors 285, 76, 1516 left out (106 units remain).

`python score.py reversed` -> 100 of 106 units covered, **89 agree (M = 0.890; strict 89/106 = 0.840)**; shuffles mean
0.006, best 0.090: **pass**. The measure was frozen with the jqa table of commit 4b76b5705 (sha256 49fb967e...); today's
table gives the same counts. Of the 11 differences, at least four are our alignment of a word over two groups
(pas-sport, probab-le, nex-t, Bass-sa-no spelt "bass sa no"); 416 pe / if, 288 then / before, 488 Wil / winter,
1150 ink / veteran may be digit slips in our single pass; 1258 1185 is glossed "north" with "(vol)" over it.

So in 1813 Crawford used both numberings of the same code: the JQA order (15 Aug 1813, from the legation's papers) and the
reversed-block copy (8 Sept 1813 and after), the copy that Morris used at Cadiz and Madrid in 1814-15 and that is in the
Claiborne letters (`../../../morris1813/claiborne`). Tomokiyo (Cryptiana) names Crawford's 1813 use of WE028, which fits.

## The 15 Aug 1813 letter's 41 unread groups

Tried with WE025 (rows public here) and with the reversed numbering: no group gives a word that fits its context
(e.g. 499 1443 "represent_s": WE025 sen + -, reversed would mod; 1480 "the Emperor was _ in Dresden": WE025 tal, reversed
high; 58 "_ of the Rhine": WE025 character). Nothing in the reading is changed.

## Not done

- No new reading: the three frames here already have their period decipherment. Crawford's other coded runs of 1813-14 on
  roll 17 (0032-0034, 0044-0049, 0055-0057, 0065-0067, 0070-0073, 0079-0082, 0086-0091, 0095, 0199-0201, 0213-0214) were
  not sorted here by numbering or by interlinear; any run without an interlinear can now be tried with the right block order.
- A second transcription pass of `interlinear_pairs.tsv`.

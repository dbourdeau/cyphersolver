# Round 2 plan: catalogue 2857 (Juan Manuel, Genoa, 14 April 1497), written before any helper starts

Written Tue 17 Nov 2026 01:39-01:45 EST (from `date`) by an AI agent (Claude Opus 5.5). No person has checked it.
Hashed in `PLAN_round2.sha256` before any helper is started and before any script below is run.

## What is already known to the writer of this plan (so the reader can judge the bias)

- The writer knows Lasry's no. 95 key and has looked, non-blind, at five lines of the 1496 Genoa letter (BNE
  MSS/20212/61/1, spread image `img03`, right-hand page lines at y = 215, 251, 289-324, 398, 909, 943), and read in them,
  by eye: "ya sabe [dal] que el [dif] esta mal contento del casamiento de ynglat..."; "que sera contento de";
  "el [bnh?] a dicho que [dal] no ..."; "la yda de [dal] de girona". In those readings the barred u/v sign (N03 of the
  package) stands for o five times (contento twice, casamiento, girona; plus 2857's procuran and inconviniente).
  These readings are hypotheses, not tests. They are NOT used as test data below.
- The writer has NOT decoded any line of the left-hand page of that spread (lines at y = 187 ... 409 used in part B),
  beyond seeing the page at low zoom.

## Inputs (sha256)

- 2857 page image `sources/raw/claver1497_2026-11-16/pages_0039/p001_0_Im0.jpg` 4090aae4...a36c
- 1496 letter, BNE MSS/20212/61/1 (CC BY 4.0), PDF `sources/raw/juanmanuel1497_round2_2026-11-17/bne_MSS20212-61-1_carta1.pdf`
  0af6521a...48b8; its spread image `bne_carta1_jpg/img03_2029x1475.jpg` 9d415a20...fbdc (extracted unchanged from the PDF)
- value-free sign sheet `signsheet_K.png` ed229f36...3ea56 (the same sheet round 2 used: 58 tiles K01-K58, no values)
- extra tile `K59_tile.png` b808e556...f977: the barred u/v sign cut from 2857 line 1 (no value given to readers)
- id map `output/juanmanuel1497_verify_2026-11-16/my_map_from_key_image.json` bd647c13...5f3b (round 2's map, located in
  Lasry's key image by template matching)
- Lasry's key `.../esp318no95/lasry2021/ctts/key.txt` 5ee40781...fb06
- round 2 readers A and B: `output/juanmanuel1497_verify_2026-11-16/helper/transcription_A.txt` bdc3c441...9f38,
  `transcription_B.txt` d5c61a56...d7bd
- language model text (Pulgar 1780, Internet Archive OCR) b265e4c7...ec29, normalised exactly as round 2's T2.

## Part A: third blind reading of the 2857 cipher (helpers C and D)

- Two fresh helpers (Opus, medium effort), separately, each given ONLY `signsheet_K.png` and the same 51 windows round 2
  used (`output/juanmanuel1497_verify_2026-11-16/crops/lines/*.png`), with round 2's instructions (sheet ids, `?` for a
  sign not on the sheet with a short description, `#` damaged, `/` only for a clear space; each sign once, inside the
  green lines). Not given: the key, any decode, any earlier transcription, K59. Output files hashed on arrival.
- Reconciliation, mechanical (`scripts/reconcile_round3.py`), run once after both arrive:
  1. C and D are reconciled with round 2's own `reconcile.py` rule (difflib alignment per line; equal tokens stand,
     everything else is a hole), giving the C/D text.
  2. The A/B reconciled text (round 2, 47 holes) and the C/D text are aligned per line by difflib on tokens, where a hole
     never equals anything.
  3. An A/B hole CLOSES only when the C/D text has an agreed sign at the aligned place AND that sign equals A's or B's
     reading there (three of four blind readers agree). If one of A/B had no sign there (a one-sided insertion) and C/D
     agree on no sign there (nothing aligned), the position is DROPPED (three of four readers see no sign). Every other
     case stays a hole: C/D disagree, C/D agree on a third sign, or alignment is not one-to-one.
  4. No image check by the writer (who knows the key) decides any position. Damaged line ends stay holes unless rule 3
     closes them.
- Report: holes closed, dropped, left; the per-position table (`holes_table.tsv`).

## Part B: test of the barred u/v sign = o, on held-out text (helper E)

- Held-out text: the first eight cipher lines of the LEFT page of the 1496 spread (window sets `helperE_windows/M1-M8`,
  150 source px windows, 30 px overlap, 5x). One fresh helper (Opus, medium effort) transcribes them blind with
  `signsheet_K.png` plus `K59_tile.png` as K59 (described only as "a sign seen in another letter"), same conventions.
- Decode (`scripts/test_n03.py`): each sheet id -> its letter column in Lasry's key (my_map: "E1" -> e, etc.); D_null
  dropped; code groups, `nine_dot`, `aunque`, `?`, `#` and Latin-letter groups break the letter stream; K59 is the sign
  under test.
- For each K59 occurrence: context = up to 6 decoded letters on each side, stopping at a break or at another K59. For
  each of the 21 letters v (abcdefghilmnopqrstuyz) the window left+v+right is scored with round 2's T2 model
  (Pulgar trigram, interpolation 0.7/0.2/0.1, add-0.5). Rank of o among the 21.
- Statistic S = number of occurrences where o ranks first. Control: 1,000 tables with Lasry's letter values permuted among
  his 44 letter signs (seed 1497); for each, the same S computed on the permuted decode (K59 still free).
- **Pass mark (all three):** at least 3 K59 occurrences; o ranks first by the summed score over all occurrences; and
  S > n/2 and S at or above the 99th percentile of the 1,000 permuted-table values of S. **Anything else is a MISS**; fewer
  than 3 occurrences is "no result", reported as such and not as a pass.
- Descriptive (not part of the mark): the same ranking at every held-out position of a sign Lasry reads o (his O column),
  as a measure of what the procedure can do; and the decoded words around each K59 with o in place.
- Run once. If it passes, the working text of 2857 gets N03 = o, marked as a value added from outside Lasry's table.

## Part C: blind check of the writer's non-blind readings of the 1496 letter (helper F) - descriptive, not a test

- One fresh helper transcribes blind five right-page lines (`helperF_windows/N1-N5` = y 215, 251, 398, 909, 943) with
  the same sheet plus K59. Decoded as in part B with K59 = o only if part B passed (otherwise K59 = hole).
- Reported: the decode next to the writer's earlier eye readings; the share of letters that agree. These lines were seen
  by the writer, so this is a check of the writer's reading, not evidence for any value.

## Code groups

- `dal` and `bnm`: no test is planned. Candidates are reported with their contexts (2857, no. 95, the 1496 letter) and
  outside support (Zurita); a group counts as read only if the planned rule above makes it so - it cannot, so both stay
  unread in every count, and any identification is marked "proposed".

## Read share (after parts A-C)

Repository rule, as in the package: cipher words only; a word counts only when every sign has a value (Lasry's table,
plus N03 = o only if part B passed, marked) and no letter is supplied or changed by sense; each code group one word, unread
without a value; 56 words with the package's division. Counted on (1) the strict text = round 2's blind text with part A's
closures and drops, and (2) the working text.

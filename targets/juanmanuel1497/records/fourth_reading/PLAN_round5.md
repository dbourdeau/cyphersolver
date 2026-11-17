# Round 5 plan: Juan Manuel letters 2 and 1 (BNE MSS/20212/61/2 and /1) and 14 April 1497: closing holes honestly

Written Tue 17 Nov 2026, finished at about 03:48 EST, by an AI agent (Claude Opus 5.5, the round-5 worker). No person has
checked it. Its sha256 goes in `PLAN_round5.sha256` (with the time from `date`), together with the hidden mapping of
sign sheet version 2, before any transcription helper starts and before any new decode. Andrew's decision of 17 Nov 2026
stands: nothing is posted, pushed, commented or reserved; the package worktree is only read.

## 0. What this round is, and what it is not

- **Not a test of the key.** Lasry's no. 95 key passed both planned tests on letter 2 in round 4 (letter trigrams -1.043,
  above all 1,000 permuted tables and the Zurita 5th percentile; word share 0.338 against a mark of 0.255). Those tests
  are NOT re-run as tests. On the new letter-2 text the worker will report the same two measures (`tests4.py`
  unchanged, run with `--descriptive`) as a **consistency check only**; a fall in either below its round-4 mark (trigram
  per letter below the Zurita 5th percentile, or word share below the mark recalibrated at the new hole share) is
  reported as a **warning**, not as a failure or a pass.
- **The new sheet rows are not blind to round 4's decode of f. 7r.** The worker has read round 4's notes (which quote
  decoded sentences of f. 7r and the `def`/`dal` contexts) and has seen round 4's helpers' transcriptions, including where
  they wrote `?(alpha-like loop)`, `?(x with a dot each side)` and `?(upright with crossbar ... small o)`. The mapping of
  the new rows was decided by shape against Lasry's own glyphs (cut from his f122c photograph with his positions file,
  `work/lasry_ref/lasry_missing_candidates.png`), not by trying values in decodes, and no decode with the new rows has been
  run; but the worker cannot be called blind to what the letters say. That is why nothing in this round counts as a test.

## 1. Sign sheet, version 2 (fixed now)

- Rows W01-W38 and their mapping are unchanged from round 4 (`hidden/sheet_mapping.tsv` there, sha256 40cc28a6...a17a67).
- New rows W39-W49, `signsheet/signsheet_W_part3.png`, examples cut from round 4's line crops of letters 1 and 2
  (`scripts/make_signsheet_part3.py`, boxes in `hidden/sheet_v2_new_rows.tsv`). Full mapping `hidden/sheet_mapping_v2.tsv`:

| Row | Shape (as on the sheet) | Lasry sign | His value | Basis on his leaf |
|---|---|---|---|---|
| W39 | upright, short arm to the right at the top, then small o | `I-o` | H | his 5 examples: same build |
| W40 | x with a dot on each side | `.X.` | P | his 2 examples: same |
| W41 | alpha joined to a c, bar across the top | `a_` | R | his 2 examples have the bar |
| W42 | alpha joined to a c, no bar | `ee` | L | his 2 examples have no bar |
| W43 | small o standing alone | `o` | Z | his 3 examples: a lone small o |
| W44 | p with cross-stroke(s) on the descender | `p++` | R | his 1 example |
| W45 | plain p | `p` | r (lower case in his key) | his 1 example |
| W46 | S-shaped stroke | none | no value | his `S` is not on the leaf image I can cut by his positions |
| W47 | figure 9 with a long tail | none | no value | his `9` likewise; his value "[y?]" is itself uncertain |
| W48 | figure 6 / G shape | none | no value | no counterpart |
| W49 | # shape (two bars crossed by two strokes) | none | no value | not his `b++` (one stem) |

  Less certain, stated now: W41 against W42 rests on one bar that is faint in places; W43 has only two clean examples;
  W44 and W45 one each. Recurring unknowns not given a row: the "d-shape" (one round-4 reader, nine times; no clean
  example found) and loose "small o" reports that the worker found on inspection to be parts of W20, W03 or W42.
- Helper instructions `helper_instructions_v2.md` (round 4's, with the new rows and neutral notes on the new pairs).

## 2. Show-through on ff. 6r and 6v (done before this plan; result fixed now)

- `scripts/st_register.py`: the other side of the leaf (f. 6v for f. 6r and vice versa), mirrored left-right, registered
  onto the page (rotation and scale search at quarter size with FFT translation, then a smooth quadratic displacement
  field fitted to 160-pixel tile shifts). `scripts/st_clean.py`: three treatments of the darkness map: **sub** (page ink
  minus k times the registered other-side ink, k = least-squares slope, 0.60 for f. 6r and 0.65 for f. 6v), **chan**
  (the same after a Fisher colour projection), **subloc** (sub plus local contrast). Originals untouched; new files in
  `showthrough/`.
- Blind choice: two fresh helpers (CL1, CL2) ranked four versions (original, sub, chan, subloc; labels shuffled, key in
  `hidden/clarity_labels.tsv`) of five sample lines (A05, A22, B05, B20, B30). Result: sub 35 points, chan 35, subloc 20,
  original 10 (4 = best ... 1 = worst, ten rankings); sub and chan each first five times; both helpers call them near
  identical. Tie broken by the worker for **sub** (one fitted step fewer). The original was ranked last in all ten.
- Readers of ff. 6r-6v get the sub version of every line (`crops/letter2_6r_clean`, `_6v_clean`, made with round 4's own
  line tracks and cutting method, `scripts/make_line_crops5.py`) AND the unprocessed round-4 line image of the same line
  for checking faint strokes (the treatment can weaken a stroke of the page's own ink where it crosses show-through).

## 3. Readers and reconciliation (all helpers Opus, medium effort, fresh, separate folders, outputs hashed on arrival)

They see only crops, the value-free sheet (three parts) and instructions; never the key, a mapping or a decode; no file
named REPORT.md; at most six at a time.

**3a. Letter 2, ff. 6r (A01-A34) and 6v (B01-B36), full lines.** Readers R1 and R2, one agent per reader per page (four
agents). Reconciled per line with round 4's rule (`scripts/reconcile4.py` unchanged: difflib alignment; equal tokens agree
except `?` and `#`; everything else a hole). Open stretches (maximal runs of non-agreed positions in a line) go to a
third fresh reader T (one agent per page), who sees the line images and, for each stretch, up to three agreed sheet ids
on each side as anchors (no readings of R1 or R2 at the stretch), and writes the signs between the anchors.

**3b. Letter 2 f. 7r (57 stretches, 62 positions) and letter 1 (113 stretches, 135 positions).** The open stretches
of round 4's reconciliation (`hidden/stretches_f7r.tsv`, `hidden/stretches_l1.tsv`: all non-agreed positions,
including those both round-4 readers marked `?(...)` or `#`), with round 4's agreed anchors. Two fresh readers S1 and S2
(one agent each, both letters) read every stretch on round 4's line images (these pages have little show-through); a
third fresh reader S3 reads the stretches where S1 and S2 differ. Round 4's agreed positions stand as they are.

**3c. Vote (mechanical, `scripts/vote5.py`):** per stretch, the readings are sequences of sheet ids (possibly empty).
(1) If two readers (S1 and S2, or R1 and R2 on their aligned stretch) are identical, the stretch closes with that
sequence (for 3a this is already the agreed text). (2) Otherwise, with the third reader: if two of the three sequences
are identical, the stretch closes with it. (3) Otherwise, if all three sequences have the same length, each position
closes where at least two of the three agree. (4) Everything else stays a hole. `?(...)`, `?` and `#` never close a
position; a closed position whose sheet id has no value (W26, W27, W46-W49) is closed but unread. `{...}` groups close
only if identical letter by letter. Round-4 readers P and Q are not counted in 3b (their disagreement is why the stretch
is open).

## 4. Decode and readings

- Decode: closed W id -> Lasry sign name through `hidden/sheet_mapping_v2.tsv` -> his letter (key.txt, unchanged);
  W25 his null dropped; W26, W27, W46-W49 and holes -> `?`. Scripts `tests4.py` and `diplomatic4.py` from round 4
  (copied unchanged except paths).
- Readings for letters 2 and 1: diplomatic text with every hole and every departure from the mechanical decode marked;
  normalised text; English translation marked as an AI agent's. Read share the repository's way (as round 4's
  `words4.py`: cipher words only; a word counts only if every sign is a closed position with a value and the decode is
  the word itself, no letter supplied or changed by sense; a code group is one word and unread, since no group value has
  passed a test), by page, beside round 4's figures (letter 2: 342 of 848; letter 1: 219 of 388). Word division and
  reading by the worker after the decode, as in round 4.
- Code groups written in Latin letters (`dal`, `def`, `dif`, `dcf`, `del`, `bac`, `bcd`, `bon`, any others): every
  closed occurrence with its context, as evidence; no value assigned.
- Consistency check on the new letter-2 text: B1 and B2 as in section 0 (descriptive).

## 5. The barred u/v sign (W26), descriptive only

The 11 places where round 4's value o "broke" a word (`tests/tests_output_letter2.txt`, part C1) are located on the
image and compared in shape (bar position, u or v form, extra strokes) with the 22 places where o made a word. Reported
as what the shapes show; no value proposed as read.

## 6. 14 April 1497 (catalogue 2857)

- Two fresh blind readers N1 and N2 transcribe all 51 windows of the letter (round 2's windows, `helper_inputs/C/windows`
  of round 2) with sheet version 2 (the W sheet of the 1496 hand; the readers are not told the letters differ).
- For each of round 2's 29 still-doubtful positions (`holes_table.tsv`, result "left"), grouped into stretches (runs of
  consecutive left positions in a line), every reader's reading of the stretch is taken in Lasry sign names: readers A and
  B (round 1), C and D (round 2's third reading) through round 2's K map (`my_map_from_key_image.json`, cell labels
  converted to Lasry names in key.txt order), N1 and N2 through the v2 mapping; each reader's stretch is found by
  aligning his whole line (in Lasry names) to the strict line's agreed anchors (difflib).
- **Rule (majority over all readers so far):** a stretch closes when at least four of the six readers give the identical
  sequence of Lasry sign names; otherwise, if those six sequences include at least four of equal length, a position closes
  where at least four of the six agree. `?`, `#`, `-` and no-value signs never count as a reading.
- Recount strict and working shares with round 2/3's rule (`words_round3.py` logic); were 35 and 45 of 56.

## 7. Verdict

Read shares now, by letter and page, beside round 4; what is still unread and why; whether another transcription round
would gain anything; what an independent verifier should check before any package.

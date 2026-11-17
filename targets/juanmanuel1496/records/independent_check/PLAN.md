# Verifier 2 plan: does George Lasry's no. 95 key, unchanged, read Juan Manuel's letters of 1496?

Written 17 Nov 2026 by an AI agent (independent verifier 2) BEFORE opening any note, plan, sheet, mapping,
transcription, decode or word table of the earlier rounds (juanmanuel1497_verify_2026-11-16,
juanmanuel1497_round2, round3, round4, round5, repo_items_2026-11-16 transcriptions). Nothing of theirs has been
opened. Opened so far: the page images, Lasry's upstream files (key, CTTS transcription and positions, f122r scan,
NOTES of esp318no95), the shared Spanish corpora (lang/corpora es-quijote, es-vasto-memorias). No web requests.

Material:
- Letter 2 (BNE MSS/20212/61/2, Genoa 18 Dec 1496): `sources/raw/juanmanuel_round4_2026-11-17/carta2_jpg/`,
  f. 6r = img03 right half, f. 6v = img04 left half, f. 7r = img04 right half (unprocessed JPEGs as extracted from the BNE PDF).
- Letter 1 (BNE MSS/20212/61/1, Genoa 10 Nov 1496): `sources/raw/juanmanuel1497_round2_2026-11-17/bne_carta1_jpg/img03`,
  the two cipher pages: left half (page "pL", 25 lines) and right half (page "pR", headed 1496, 21 lines).
- Lasry: key `lasry2021/ctts/key.txt`, transcriptions and positions f122a/b/c (copy in
  `output/push_2026-11-14/wt-montcalm1757w-followup/targets/esp318no95/`, identical key to `repo_items_2026-11-16/upstream_files`),
  scan `f122r.jpg`. The esp318no95 folder named in the brief (`repo_shortlist_2026-11-16b/upstream/targets/esp318no95/`)
  holds only NOTES.md, so the key, positions and scan are taken from the copies above (same upstream files).

## (a) The draw

Lines are numbered from the top of each cipher page, one per line of cipher, as found by `scripts/lines.py`
(horizontal ink profile, central 60 % of the width) and checked by eye on `work/lines_<page>.jpg`:
f. 6r 35 lines, f. 6v 36, f. 7r 25 (letter 2, 96 lines); letter 1 pL 25, pR 21 (46 lines).

Seed 20261117, Python `random.Random(20261117)`, one generator used in this order:
`sample(range(1,36),8)` for f. 6r, `sample(range(1,37),8)` for f. 6v, `sample(range(1,26),8)` for f. 7r,
`sample(range(1,26),6)` for letter 1 pL, `sample(range(1,22),6)` for pR. 24 lines of letter 2, 12 of letter 1.
A drawn line is kept whatever it holds (short lines, clear words, corrections included).

## (b) The sign sheet (value-free)

- For each sign name in Lasry's CTTS transcription (57 names: his 43 invented signs, his special signs and the
  code groups he wrote in letters), up to five examples are cut from the BnF scan f122r.jpg at his own boxes:
  his f122a/b/c position frames were placed on the scan by `scripts/register_ab.py` (scale and offset that maximise
  ink contrast inside his boxes; c gives scale 0.998, a 1.894, b 0.998; checked by eye on overlays) and cut by
  `scripts/sheet_lasry.py`. The verso sign `pi` (one occurrence, f122v only) has no frame on a scan here and is left off.
- Each sign gets a random id S01-S57 (`random.Random(1117)` shuffle of the sorted names). The id-to-name table is
  kept in `private/sheet_mapping_HIDDEN.json` and is never given to a helper.
- Code groups written in ordinary letters (bac, bnh, dal ...) are not sheet rows: helpers write such groups as
  the letters they see, in brackets.
- After the draw, I add to each row up to three examples of the same shape from the letters, taken only from lines
  NOT drawn (so no helper sees a drawn position resolved); rows where I find no clear example say so.
- The sheet images carry ids only: no values, no Lasry names.

## (c) Two blind helpers

- Two fresh agents (Opus, medium effort), started separately and at the same time, each told nothing about the key,
  the values, the earlier rounds or the other helper. They read only `helper_pack/` (sheet, instructions, crops)
  and write only their own folder `helper_A/` or `helper_B/` (file `transcription.txt`; never REPORT.md).
- Crops: each drawn line cut from the UNPROCESSED page JPEG as a band of about two line heights around the line,
  split at a low-ink column near the middle into parts a and b, enlarged 3x (Lanczos), with a white margin on each
  side holding a red arrow at the target line (`scripts/crops.py`). No cleaning, no contrast change.
- Token rules (in `helper_pack/INSTRUCTIONS.md`): sheet id; `?` for a sign they cannot assign; `[letters]` for a group
  in ordinary letters; `X:desc` for a sign not on the sheet; `{clear}` for ordinary handwriting; `/` for a word gap.
- Agreement: `scripts/align.py`, Needleman-Wunsch per line (match +2, mismatch -1, gap -1). A position counts only
  when both helpers give the same sheet id (or the same bracketed group with no `?`). Every other alignment column
  is a hole. Agreement rate = agreed / alignment columns, reported per page.

## (d) Tests of Lasry's key UNCHANGED on letter 2's agreed positions (`scripts/tests.py`, one run)

Decoding: agreed sheet id -> Lasry sign name (hidden table) -> Lasry value from key.txt as he wrote it. Nulls are
dropped; code groups, `[y?]`, `[aunque?]`, holes and bracketed letter groups break the letter stream and count as
holes. No value changed, added or guessed.

1. Trigram measure, no word division: mean log2 probability per letter under a letter trigram model (add-0.5)
   trained on Don Quijote + the first half of Villa, *Memorias* (Spanish documents 1500-1530); context restarts after
   each hole. Normalisation: lower case, accents off, j->i, v->u, n-tilde->n, c-cedilla->z.
   - Control 1: 1,000 permuted tables (the multiset of letter values shuffled over Lasry's letter signs, seed 20261118).
     **Mark T1: the real score must exceed the maximum of the 1,000 permuted tables.** Control limit reported: mean + 3 SD.
   - Control 2: 1,000 samples of period Spanish from the held-out second half of the *Memorias*, same total letters
     and the same run lengths (seed 20261119). **Mark T2: the real score must be at or above the 1st percentile of
     the Spanish samples.** Control limits reported: 1st and 99th percentiles.
2. Word-share measure: each run of decoded letters is covered by words of the same training text (length >= 2, seen
   >= 3 times) by dynamic programming; word share = covered letters / all positions (holes included).
   **Mark W, set by rule on Lasry's own letter:** 200 random contiguous windows of his decoded no. 95 (his
   transcription and key) with as many signs as the tested text, holes punched at random up to the same hole share
   (seed 20261120); the mark is the 5th percentile of those 200 word shares. Control reported: word share of 100 of
   the permuted tables.
3. A miss on any mark is reported as a miss for that measure; "key verified on unseen text" needs T1, T2 and W all
   passed. By construction W misses about 1 time in 20 on text as good as Lasry's own.
4. The same three tests are run on letter 1's agreed positions as a secondary result, same marks.
5. One run. A dry run of the code on Lasry's own letter with 25 % random holes was made before this plan to check the
   code (`dryrun/`); it passed T1 and T2 and W after W's windows were made the same size as the tested text. No
   letter data had been transcribed then.

## (e) Comparison with the earlier rounds (only after step 2 is finished)

For each drawn line, the earlier rounds' transcription of the same page line (found by content: the best alignment
among their lines within +-2 of my line number) is mapped through THEIR sign-to-Lasry table and aligned to my
agreed sequence (Needleman-Wunsch as above). Measured on my agreed positions: share where their Lasry sign equals mine,
and share where the Lasry value (letter) equals mine. **Threshold: value agreement below 85 % = their transcription
is unreliable at these positions; 85-95 % = usable with errors; 95 % or more = reliable.**

## Later samples (step 3), seeds fixed now

- (d) show-through cleaning: 20 closed positions on ff. 6r and 6v drawn with seed 20261121.
- (e) third-reader closures that sided with one reader: 30 drawn with seed 20261122.
- (f) words counted as read: 60 drawn with seed 20261123; each judged sure period Spanish as written / read only by
  sense / wrong; my read share = sure words / all cipher words, beside theirs.

# Round 4 plan: letter 2 of BNE MSS/20212/61 (Genoa, 18 Dec 1496) read blind and tested; letter 1 re-read; back to 14 Apr 1497

Written Tue 17 Nov 2026, finished at about 03:04 EST, by an AI agent (Claude Opus 5.5, the round-4 worker). No person has checked it.
Its sha256 goes in `PLAN_round4.sha256` (with the time from `date`) before any helper is started and before any script of
parts B-C is run. One run of everything below. Misses are reported as misses; "no result" as no result, never as a pass.
Andrew's decision of 17 Nov 2026 stands: nothing of this is posted.

## 0. What the writer knows and has seen (to judge the bias)

- Letter 1 (Genoa, 10 Nov 1496, MSS/20212/61/1, ff. 2v-3r): read in rounds 2 and 3 (round 3's agreed decode, its
  reading and its descriptive variant). **Letter 1 is not held-out material for any test of this round.**
- Letter 2 (Genoa, 18 Dec 1496, MSS/20212/61/2): downloaded today (`sources/raw/juanmanuel_round4_2026-11-17/`, the
  library's own "PDF de este volumen" link in the viewer). Cipher on three pages: image 3 right (f. 6r, headed "1496",
  34 lines, here A01-A34), image 4 left (f. 6v, 36 lines, B01-B36), image 4 right (f. 7r, 25 lines, C01-C25; image 5
  left is a second photograph of the same page and is not used). The writer has looked at letter 2's pages to cut sign
  examples and to check line tracking (overlays of A01-A05, B01-B04, C01-C04, left halves, with component boxes; the
  straightened-line check images of all 95 lines). **Nothing of letter 2 has been decoded by anyone.** Seen in passing,
  stated now: letter 2 opens with the two signs that open Lasry's no. 95 (large C, large D-shape); Latin-letter groups
  that look like `dal`, `bae`, `bon`, `dif`/`def` and an `8cf`-like group occur; C25 ends in clear handwriting.
- Lasry's key, his sign names and his own glyphs (cut from his f122c photograph with his positions file:
  `work/lasry_ref/`).

## 1. Inputs (sha256)

- Letter 1 spread `sources/raw/juanmanuel1497_round2_2026-11-17/bne_carta1_jpg/img03_2029x1475.jpg` 9d415a20...fbdc.
- Letter 2 `sources/raw/juanmanuel_round4_2026-11-17/carta2_jpg/img03_2048x1488.jpg` ef201b7b...daec and
  `img04_2048x1488.jpg` e13eb20c...737a (extracted unchanged from the library's PDF).
- 141 line images `crops/letter1/L01-L25, R01-R21` and `crops/letter2/A01-A34, B01-B36, C01-C25` and the two sheet
  images: manifest `crops_SHA256SUMS.txt` 4bc35027...6dbb. Lines tracked per eighth of the page by ink peaks linked
  with an order-preserving one-to-one alignment (`scripts/find_lines2.py`), straightened column by column and cut
  +-27 px, three overlapping segments at 3x (`scripts/make_line_crops4.py`). Every line was checked in the stacked
  straightened views (`work/dw_*.png`): one spurious track on f. 3r (a second copy of R07/R08) was dropped; letter 1's
  sloping foot (L21-L25) is now caught whole.
- Value-free sign sheet `signsheet/signsheet_W_part1.png`, `_part2.png`: 38 rows W01-W38, each with 1-7 examples cut
  from letters 1 and 2 themselves (`scripts/make_signsheet.py`), grouped by shape. Helper instructions
  `helper_instructions.md` 8c780896...7725 (with neutral notes on which shapes are easily confused).
- **Hidden mapping** (never shown to helpers) `hidden/sheet_mapping.tsv` 40cc28a6...a17a67: W id -> Lasry CTTS sign
  name, fixed now, before any decode. W25 -> Lasry's null `D`; **W26 (barred u/v) and W27 (8) -> NONE** (no counterpart in
  Lasry's key: no value). Mapping by shape against Lasry's own glyphs; the less certain choices, stated now: W24 (large
  reversed hook) -> `D-` (T); W34 -> `_I_o` (M); W21 -> `i...` (l); W31 (n + z-tail) -> `n+` (L) like W30; W32 -> `yt`
  (M); W33 -> `gt` (M). Lasry signs with no row on the sheet (not found in the 1496 hand while cutting): `ee`, `-o-`,
  `p++`, `a_`, `.X.`, `o`, `9`, `oN`, `p`, `S`, `pi` (dotted-bar form); a helper meets them only as `?(...)` = hole.
- Lasry's key `.../esp318no95/lasry2021/ctts/key.txt` 5ee40781...fb06 (applied UNCHANGED) and his transcription
  `.../ctts/transcription/all.txt` 81ec4406...0411 (B2 calibration); word list and measure
  `output/juanmanuel1497_verify_2026-11-16/scripts/wl2857_copy.py` 2e7c269c...e6fb (`build_claver_pulgar_long(.., 4, 5)`,
  `sandwich_measure(.., 3)`) over `output/claver1497_2026-11-16/wordlist_claver_es.tsv` 9b4e5b16...091b and Pulgar 1780
  (`output/claver1497_verify_2026-11-16/raw/pulgar1780_...djvu.txt` b265e4c7...ec29); Zurita 1580 OCR 75979b15...16db.
  All as in round 3.

## 2. Part A: two blind transcriptions of every line

- Reader P and reader Q, each made of four fresh helper agents (Opus, medium effort), one per batch: letter 1 (46
  lines), f. 6r (A, 34), f. 6v (B, 36), f. 7r (C, 25). Eight agents, started separately; each sees only its own folder
  (the two sheet images, `helper_instructions.md`, its batch of line images). They are told nothing about values, the
  key, the language, earlier readings or other helpers; no file named REPORT.md. Outputs hashed on arrival in
  `HASHES_helpers.txt`.
- Reconciliation (`scripts/reconcile4.py`, mechanical, run once per letter): `?(...)` -> `?`; per line, difflib
  alignment of P and Q; equal tokens agree, except `?` and `#`, holes even when both write them; every other position is
  a hole. **A position counts only where both agree.** `{...}` groups agree only if identical letter by letter.
  Agreement = agreed / aligned positions, per line and per letter.

## 3. Part B: Lasry's key unchanged, on LETTER 2 ONLY (agreed positions)

Decode (`scripts/tests4.py`): agreed W id -> Lasry sign name (hidden mapping) -> his letter (key.txt). W25 (his null)
dropped. W26, W27 and holes -> `?` (holes). `{groups}`, `?(...)`-turned-holes stay holes; `{groups}` and `<clear>` break
the letter stream into segments.

**B1, letter trigrams, no word division** (round 3's B1 unchanged): runs of letters between breaks and holes; mean
log10 probability per letter under the Pulgar letter-trigram model. Control: 1,000 tables permuting Lasry's letter values
among his 44 letter signs (seed 1496; the W values follow the permuted table through the mapping). Reference: 1,000
samples of the Zurita letter stream with the same run lengths (seed 1496). **Pass: the real table beats all 1,000
permuted tables AND scores at or above the 5th percentile of the Zurita samples.** Anything else is a miss.

**B2, share of letters in words** (round 3's B2 unchanged). Calibration rule, fixed now: h = holes / (letters + holes)
of letter 2's agreed decode (holes = disagreements, `?`, `#`, W26, W27); Lasry's own no. 95 decoded with his key (code
groups break segments); holes punched at random into its letter positions at share h, 200 draws (seed 95); **mark M =
the 5th percentile of those 200 values. Pass: real >= M AND real above the 99th percentile of the 1,000 permuted
tables.** Anything else is a miss.

## 4. Part C: the additions, each tested on letter 2 only

**C1, barred u/v sign (W26) = o.** Occurrences n = agreed W26 positions in letter 2; n < 3: NO RESULT. Context of each:
the agreed decoded letters on each side up to 8, stopping at a break, a hole or another W26. An occurrence is evaluable
if its context has at least 3 letters (both sides together). For a candidate letter v in the slot, segment the context
with the round-3 word list (Seg of `wl2857_copy`); v **makes a word** there if the token holding the slot is a list
word that `sandwich_measure` would count (length >= 3, or a shorter list word standing between such words or a segment
edge); v **breaks** an evaluable occurrence if it does not. **Pass (the brief's rule, made mechanical): o makes words
at >= 3 occurrences AND breaks none AND no other of the 21 letters scores higher on (makes - breaks).** Control,
reported: the same counts for every other letter. Anything else: MISS (or NO RESULT if n < 3).

**C2, `dal` = King Ferdinand.** Candidates fixed now: King Ferdinand; King of France (Charles VIII); King of the
Romans (Maximilian); the Pope (Alexander VI); the Duke of Milan (Ludovico Sforza); the Señoría / Commune of Genoa; the
Queen. Every agreed `{dal}` in letter 2 is listed with its context (agreed decode, 40 letters each side). Datable facts
that decide, fixed now: in Nov-Dec 1496 Ferdinand had been on the Roussillon front (Girona, Perpignan; truce with France
in Roussillon, autumn 1496) and the Catholic Monarchs held court together; the writer's master (`Vuestras Altezas`).
**Pass:** >= 1 agreed `{dal}` in letter 2; every one read with "el Rey" (Ferdinand) gives sense; at least one context
excludes every other candidate by a datable fact or by its wording (e.g. Ferdinand's own army, his Roussillon truce,
"the Queen and [dal]", the writer's own lord); none excludes Ferdinand. **MISS:** a context excludes Ferdinand. **NO
RESULT:** no `{dal}`, or contexts compatible but nothing excludes the others. The judgment is the worker's and is
reported as such, with the contexts verbatim.

**C3, `dif` = King of France and `dcf` = King of the Romans** (round 3's proposal; `def` recorded as written and treated
as its own group). Each group is tested separately on letter 2. Datable events, fixed now (Sanuto, *Diarii* vol. I, Nov
1496-Jan 1497; Zurita III for the Spanish side; local OCR only): (1) Charles VIII's preparations against Genoa: the
Cardinal of San Pietro in Vincoli (Giuliano della Rovere) and Battistino Fregoso, French men and money, by sea from
Marseille/Provence and by land from Asti, Savona; (2) Maximilian's withdrawal: he raised the siege of Livorno (Nov 1496)
and left Italy for Germany in December 1496 (no. 95, 8 Jan 1497: "está en Alemanna"); (3) the Duke of Savoy's position
between the French and the League; (4) della Rovere's movements (towards Savona); (5) Battistino Fregoso.
**Pass for a value V of a group:** >= 2 agreed occurrences in letter 2; every occurrence compatible with V; at least one
occurrence decided for V by one of events (1)-(5) (the context gives the group an act or place that in Nov-Dec 1496
belongs only to V: e.g. sending della Rovere / Battistino / French ships against Genoa -> King of France; leaving Italy,
returning to Germany, the siege of Livorno, the imperial camp -> Maximilian); no occurrence decided against V. **MISS:**
an occurrence decided against V. **NO RESULT:** fewer than 2 occurrences, or none decided by an event. The judgment is
the worker's, reported with contexts and the Sanuto/Zurita passages quoted.

**C4, `bnm`:** every agreed `{bnm}` in letter 2 listed with context; a value counts by C2's rule (candidates: Señoría of
Genoa, Duke of Milan, King of France, Maximilian, the Pope). None found: NO RESULT.

Every other code group in letter 2 is listed with context (descriptive only).

## 5. Part D: reading and read share

- Letter 2: diplomatic text (agreed decode; every hole marked; every departure from the mechanical decode marked);
  normalised text; English translation marked as an AI agent's. Read share the repository's way: cipher words only; a
  word counts only if every sign is an agreed position with a value (Lasry's table through the fixed mapping, plus any
  addition that passed part C), no letter supplied or changed by sense; a code group is one word, read only with a value
  that passed here.
- Letter 1: the same from the two fresh transcriptions, stated as a re-reading, not a test (B1/B2 run on it are
  descriptive only).
- Content of both checked against Sanuto and Zurita for the weeks concerned; matches quoted.
- 14 Apr 1497 (catalogue 2857): apply only what PASSED in part C to round 2's strict (35 of 56) and working (45 of 56)
  texts; recount with round 2's rule; list each unread word with its blocker.

**What counts as a miss:** a test that does not reach its mark. **No result:** too few occurrences, or nothing decides.
Neither changes any text. A passed addition is marked "added in round 4, outside Lasry's table" wherever used.

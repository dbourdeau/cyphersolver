# Verification plan: cyphersolver entry 2857, Juan Manuel to the Catholic Monarchs, Genoa, 14 April 1497

Written Mon 16 Nov 2026 23:38 EST (from `date`), before any helper transcription, before reading the solver's notes,
transcriptions, adjudications, decode or scripts (other than the first 15 lines of `linecrops2857.py`, read only to find
the Python image library path), and before any decode by me. Verifier: an AI agent (Claude Opus 5.5). No person has checked.

Inputs, with sha256:
- page image `sources/raw/claver1497_2026-11-16/pages_0039/p001_0_Im0.jpg` 4090aae4bd486db2063a402f002a54d7795b0300cf327d092d6fee3ac677a36c
- neutral sign sheet (copied from the solver's `i2857/private/signsheet_K_blind.png`, ids K01-K58, no values) `crops/signsheet_K.png` ed229f36bf8cafdf9c88ba3eb492b9fecfe807f6c94955eb4dcb385a6d853a56
- Lasry's key file `output/push_2026-11-16/wt-taylor1865-print/targets/esp318no95/lasry2021/ctts/key.txt` 5ee40781ca8a562dcfd1a760b88806a24f458140007c3ea376cb638c4f08fb06
- solver's test plan `output/repo_items_2026-11-16/TEST_PLAN_2857.md` 6eb293fb15e5c488dfdfffec351fbf5e27406abb1c08beaac926e8027865e52d (not yet read)
- language-model text: Pulgar, Cronica de los Reyes Catolicos (1780 print, Internet Archive OCR) `output/claver1497_verify_2026-11-16/raw/pulgar1780_bub_gb_RB9nAr9N5AkC_djvu.txt` b265e4c7d071a0d83cb903565948a954dd0603cc1ab2d875c150fda6cf22ec29
- second, unrelated text for real-Spanish passages: Zurita, Anales (1580 print, Internet Archive OCR) `output/claver1497_verify_2026-11-16/raw/zurita1580_bub_gb_XgWt5lHz3_MC_djvu.txt` 75979b157bcd7d9c1158c202149127773ab3d5dc37b63d3b4deddcf1f68416db

## Step 1: blind re-transcription

- Crops: `scripts/cut_lines.py` cuts the cipher block of the recto (cipher lines 1-7, the cipher start of line 8 before
  the clear words, and the cipher end of line 8 after them) into 51 windows of 260 source pixels, overlapping 40 px,
  enlarged 3.5x, following the measured slope of each line. Red arrows mark the target line; dashed green lines mark
  where the window's share of the line starts and ends (the overlap midpoint). Boundaries were checked on the full page
  (`crops/check_windows.png`). Reading order: L1 ... L7, L8a (left of the clear words), L8b (right of the clear words).
  The order L8a/L8b versus a possible continuation of L7 is not settled by the image; this order is fixed now.
- Two fresh helpers (Opus, medium effort), separately, each given only the sign sheet and the 51 crops. Each writes
  every window as a sequence of sheet ids, `?` for a sign not on the sheet, `#` for a damaged place, `/` for a space only
  where the manuscript clearly has one. Each sign once (inside the green lines). I do not transcribe.
- Both outputs are hashed (sha256, `HASHES.txt`) before step 2.
- Reconciliation, mechanical (`scripts/reconcile.py`): per line (windows concatenated), the two id sequences
  (spaces removed) are aligned with a minimum-edit alignment (Python difflib opcodes on token lists). Equal tokens stand.
  A substitution, an insertion by one helper only, a `?` or a `#` on either side is DOUBTFUL and stays doubtful: no third
  look. A space stands only if both helpers mark it at the same agreed position.
- Report: agreement n of m (n = agreed positions; m = all aligned positions, counting each substitution, one-sided
  insertion and `?`/`#` as one position). Comparison with the solver's final transcription (read only after the hashes):
  aligned the same way, counts of equal, different, and positions only one side has; and at each of the solver's eight
  adjudicated places, whether my two helpers agreed with each other and with his choice.

## Step 2: tests (decided now, run once each)

Mapping of sheet ids to Lasry's signs: each sheet cell was cut from Lasry's key image
(`.../esp318no95/lasry2021/cryptiana/images/esp318_1497_key.png`), so I locate each cell in that image by template
matching (`scripts/locate_cells.py`) and take its value from the column (letter) or the label beside it (code group,
special sign). The resulting table is compared with Lasry's key.txt (counts of signs per letter must match) and with
the solver's private id map; any difference is reported, and T1/T2 use MY mapping from the key image.

- T1, replication. Lasry's values applied by `scripts/decode.py` to my reconciled transcription; doubtful positions,
  `?` and `#` are holes (no letter, and a word containing a hole cannot count as read). The solver's measure, word list,
  segmentation rule and pass mark (70%) are then taken unchanged from his `TEST_PLAN_2857.md` and scripts (read after
  my hashes) and applied by my own script; if his measure needs his transcription format, I convert my text to it and
  say how. Control: 1,000 tables made by randomly permuting the letter values among the letter signs (code groups and
  special signs unchanged), seed 2857, same measure. Mark: score >= 70% and above the maximum of the 1,000. A score below
  70% is a MISS (the claim does not survive an independent transcription), whatever the control.
- T2, measure independent of segmentation. Alphabet: Lasry's 21 letters (a b c d e f g h i l m n o p q r s t u y z).
  Normalisation of model and reference texts: lowercase, accents stripped, j->i, v->u, w->u, k->c, c-cedilla->c,
  n-tilde->n, x->s, every other character removed, so the text becomes one letter stream (word spaces dropped).
  Model: letter trigram, trained on the Pulgar text, interpolated with bigram and unigram (weights 0.7/0.2/0.1),
  add-0.5 smoothing at each order. Score: mean log10 probability per letter of the decoded letter stream, where holes,
  code groups and special signs break the stream (each run scored separately; the first two letters of a run use the
  lower orders). Control: the same 1,000 permuted tables as T1 (seed 2857). Reference: 1,000 samples from the Zurita
  text; each sample reproduces the run lengths of the real decode, each run a contiguous chunk from a random start
  (seed 1497) in the Zurita letter stream. Mark: the real table beats all 1,000 permuted tables AND its score is at or
  above the 5th percentile of the 1,000 Zurita samples. Failing either is a MISS.
- T3, calibration. Recompute the solver's 72.7% for Lasry's key on 225 signs of Lasry's own letter, from Lasry's files
  (`lasry2021/ctts/transcription`, `decryption`) and the solver's calibration script, unchanged. Reproduced = within
  1 point of 72.7% on the same 225 signs. Not reproduced: the 70% mark is unsupported, and I say so.
- T4, reported differences from no. 95: (a) a barred u/v sign not in Lasry's table that the solver says needs o in
  both places; (b) the plain 7 (Lasry's D) standing for s four times and d twice. Check each place on the page image
  (my own crops), check Lasry's letter (his transcription and decryption: does the plain 7 stand for s there, do his
  edits show the same variation?) and his key table (a homophone the sheet missed?). Verdict per item: a real difference
  of this letter, a misreading, or a sign of a different key. Descriptive, no pass mark.

## Step 3 (after the tests): sense and outside facts

My own count of read cipher words under the repository rule (every sign has a value from Lasry's table, no letter
supplied or changed by sense), with my word division stated; the solver's 44 read words classed sure / not sure; the
12 unread words: which could be settled only by sense. Outside facts from files on disk first (Claver 2025 book text,
Sanuto and Zurita extracts), at most 8 web requests (Internet Archive, 2 s apart; no Chrome, no PARES, no Gallica).
Prior print: the 2025 book note 166, Suarez Fernandez, Lasry's paper on Espagnol 318.

## What counts as a miss

T1 below 70% or not above every permuted table; T2 failing either condition; T3 not reproduced (mark unsupported).
A miss is reported as a miss, not softened.

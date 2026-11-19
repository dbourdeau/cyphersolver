# Transcription accuracy benchmark: solo plan

Goal: measure how accurately the AI transcribes cipher pages, beyond the single Pillon pilot (one telegram, 271 of 283
groups exactly right, 95.8%; every miss one digit; 8 of 12 flagged). Uses only material in this repository or fetchable
from public archives. Nobody else is asked for anything.

Status: Phase 0 script written (`inventory.py`); nothing else run. The 97% figure quoted in conversation is NOT in the
repository; do not quote it publicly until Phase 3 produces it.

## What is on hand (counts from profile.json, 17 Nov 2026 session)
- 761 profiles; 1,177 documents marked transcribed by an LLM from images.
- 123 targets list a human reference for at least one document: DECODE (154 documents), published (113), project (11).
- Phase 0 result (inventory.py, recursive search): 278 documents in 123 targets have a human reference; 221 have the
  reference text file locally, 126 sit in a target folder that holds images, 113 have both. (A first top-level-only
  check found only 12 targets with images; images are git-ignored and often in subfolders.) The rest need re-fetching
  from public archives. Skews to note: 159 digit-only documents, 115 Italian, 154 DECODE.
- `transcription.corrections` counts are self-correction against the images, not independent ground truth.

## Phases
0. **Inventory.** `inventory.py` lists every document with a human reference, its symbol kind, size, image availability
   and stratum; writes `frame.json` and `frame_summary.md`.
1. **Fix the sample before any run.** 40-60 pages stratified by symbol kind (digits, letters, invented glyphs),
   legibility and period. Pillon's telegram is the anchor. Commit `sample.json` and the scoring script first.
   Draft (17 Nov 2026): `sample.py` (seed 20261117) drew 36 of a 48 target from the 111 documents that have reference
   text and images on hand: 20 digit, 13 symbol, 3 letter documents. Letters fall 11 short, because few letter-cipher
   documents have both. Closing that gap means fetching public images for letter-cipher targets (Phase 1b) or
   accepting a thinner letter stratum and saying so. The draft is not frozen; commit `sample.json` only once settled.
   Update (same day): fetched 38 DECODE page images (13 records: carpio1677 R1002-R1011, ferdinand3 R1889-R1890,
   r1873 R1873; 198 MB, git-ignored, DECODE route with the stored cookie, 2 s between requests). Pool grew from 111 to
   124; the redraw gives 41 documents: 20 digit, 13 symbol, 8 letter. Letters are still 6 short, because the cap of
   2 documents per target stops carpio1677 (10 documents, one hand, one archive series) from supplying the rest.
   Raising the cap would fill the quota but lean on one hand; the other 34 letter documents come from other archives
   and would each need their own image route.
   FROZEN at 41 documents (user's decision, 17 Nov 2026; seed 20261117, cap 2 per target). The letter stratum is small
   (8 against a quota of 14) and results for it must be reported as such. sample.json is not to be redrawn after any
   transcription run; a new draw is a new, separately named sample.
2. **Blind AI transcription.** 3-5 independent passes per page. The human reference is never in the model's context.
   Fix the prompt; record the model name and date.
3. **Score.** Align at group level. Report exact-group rate and per-symbol error rate separately, a confusion matrix of
   mixed-up symbols, and flag calibration (flagged groups that are real errors; real errors that were not flagged).
4. **Repeat-attempt curve.** Accuracy for one pass, best of N and a majority vote per group; does disagreement between
   passes predict errors?
5. **Downstream test.** On targets with a known key, run the existing solver on the AI transcription and on the human
   one; compare key recovery and share of text read.
6. **Contamination control.** Mark each page "published online" or not; prefer references never online (DECODE behind
   a login); report both groups separately.
7. **Optional solo controls.** The user's own hand transcription of 10-15 pages (label: not independent of the
   project); synthetic pages with known text at controlled noise (supplementary, not real handwriting).
8. **Record and report.** Add a solution step to each affected profile.json; publish the scoring script and paired
   transcriptions; report by stratum, not one number.

## Limits to state up front
- No second independent human transcriber, so the human ceiling is unknown; DECODE texts carry their own errors.
- The user's own transcriptions are not independent of the project.
- Results from DECODE-sourced references depend on the DECODE transcription being reachable for scoring.

## Effort
About 3-5 working sessions: inventory and sample (1), blind runs (1-2), scoring and repeat-attempt curve (1), solver
test (1).

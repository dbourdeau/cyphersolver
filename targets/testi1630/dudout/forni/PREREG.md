# PREREG - Forni cipher (Lettera F c. 53), written 17/11/2026 ~15:20 (agent Opus 5.5, fil 🔓) BEFORE any transcription or decoding of c. 53

## State of knowledge
- c. 54r (Forni's reply, Florence 25/7/1634) carries on the same page a clear paragraph that is the plain text of its cipher block
  (lines 1-4) and plain words around the later cipher (lines 5-12). Key KEY_c54.tsv was built ONLY from c. 54r by aligning the cipher
  (transcription c54r_pass2.txt) with that clear (c54r_align.txt). Homophonic substitution, ~37 signs, diaeresis = doubled letter.
- KEY_c54.tsv frozen: SHA-256 844b6343893db14505d86aa90027862dab75416d7fbd523199cd181ea12491fc (KEY_c54.sha256, 15:13).
- c. 53 (the duke's cipher letter of 22/7/1634 to Forni, ~17 lines) has NOT been transcribed or decoded by me. I have only seen it
  at 25 % in the overview. WAINUT's rough copy (failed annealing) is not used. c. 72 is not used either (it is decoded only after the measure).

## Held-out portion
All cipher signs of c. 53r, lines 1 to the end of the cipher block, read top to bottom (expected >= 300 signs; if fewer than 300,
c. 53v cipher is added; if still fewer, the measure is declared undersized and reported as such). Clear words, dates, address and
endorsements are excluded ({...}).
- Two transcription passes on full-resolution IIIF crops, labels of SIGNES (KEY_c54 labels; a shape not in KEY_c54 gets a new label N1, N2..
  which decodes to '?'), second pass without looking at the first, arbitration on the image. ':' after a label = two dots over the sign.
- Frozen: c53r_final.txt + SHA-256 in MESURE.txt BEFORE running measure.py on it.

## Measure (one)
measure.py (SHA in MESURE.txt), MINLEN = 3, seed 1634:
- decode with KEY_c54 (unknown labels -> '?'); normalisation: lower case, v->u, j->i, z->f (the sign U is shared by f and z), doubles collapsed.
- lexicon = forms of length >= 3 seen >= 5 times in the OCR of Doglio 1967, Testi, Lettere vols. 1-3 (archive.org djvu.txt, same normalisation).
- car = characters covered by a best segmentation into lexicon words (DP, length 3-16) / all decoded positions ('?' included).
- 200 witnesses: random permutations of the KEY_c54 values among the labels present in the held-out text; same score.
- Calibration (training text c. 54r only, in-sample): real 0.859, witnesses max 0.410.
- Thresholds (usual): car >= 0.85 AND car >= max(witness) + 0.30 -> VALIDATED; margin >= 0.30 only -> PARTIAL; otherwise FAIL.
- One run. The portion is burnt after the run. No key change before the run.

## After the measure
Strict reading count (Daniel's rule): words read by sense (sure + probable) / all words of the decoded c. 53 text; >= 95 % = read.

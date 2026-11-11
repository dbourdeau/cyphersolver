# King's code (the = 769): test declared 2026-11-10T19:43:27-0500, before any batch transcription came back

**Held-out text:** despatch No. 59, 23 Dec 1797 (NARA M30 roll 4, frames 0272-0273), bare code, 297 groups, already transcribed
without a key (`output/king_code16_2026-11-10/bare_passage.tsv`). Truth: the Department's clear text on frame 0273
(`bare_passage_answer_key.txt`). No. 59 is not in any transcription batch.

**Key:** built only from the interlined frames in `output/king_code16_2026-11-10/batches.json` plus frame 004-0249: single unmarked
groups under single words (majority value), then the frame solver over Weber's element list. The key file is hashed before scoring.

**Measure:** as for Eaton 22 Oct 1802 (`scripts/eaton_heldout_score_2026_11_10.py`): key values of covered groups laid on the clear
text in order under the 12 x (k+1) gap rule; score = matched / covered; coverage reported; baseline 200 shuffles of the key's values.
Groups with a hidden leading digit (marked ?) are left out. One run. Pass if score >= 0.85 and score minus shuffled maximum >= 0.30.

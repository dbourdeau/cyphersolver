# Follow-up of 14 November 2026 (after the test; nothing here changes the frozen files)

The three gaps Daniel Bourdeau listed when merging PR #579, worked by our AI agent (Andrew Beling, with AI agents).

- `duplicate_fo125/`: gap 1. B.148 pp. 126-128 are a transcript of a second signed cipher original (BL fo. 125,
  endorsed received 26 Oct 1782); full transcription, mechanical collation with fo. 124 (pp. 123-125), `DUPLICATE.md`.
- `other_copies/`: gap 2. B.45 (reel H-1434), Carleton's clear duplicate of 6 Sep (B.148 p. 89), Q series vol. 20
  pp. 384-385 (reel C-11892); CO 5/107 seen in part afterwards (one despatch of 15 Nov 1782, clear copies only; by AI
  agents from a copy saved at the Library of Congress, no person has checked it, licensed images not included);
  `OTHER_COPIES.md`.
- `structure_test/`: gap 3. What the two numbers are (`STRUCTURE.md`, `structure.py`), the pre-written held-out test
  (`TEST_PLAN.md`, not run for want of material). The list of books tried is `../key/books_tried.tsv`.

Run from the repository root:

    python targets/carleton1782/followup_2026-11-14/duplicate_fo125/collate.py
    python targets/carleton1782/followup_2026-11-14/structure_test/structure.py

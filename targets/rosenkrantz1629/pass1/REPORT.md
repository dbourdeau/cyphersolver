# rosenkrantz1629: Palle Rosenkrantz's London relations, Feb-Apr 1629 (24 Nov 2026)

## Bottom line
**No key. No reading. A failure write-up.** None of the period keys in the "Chiffer" packet fits. The sign cipher
(408 tokens in 7 letters to the king) was transcribed in full, frozen and attacked from ciphertext alone; no run
produced Danish, and the frozen candidate key does no better than shuffled keys on the held-out letters.
One prior-art risk is open: Temler's manuscript key to Christian IV's own sign cipher of 1625-27 (see PRIOR_ART.md
item 3). Check tool: none exists for a keyless target outside the repo; `_check_writeup.py` and `_check_profile.py`
were not run (no target folder was made in the repo).

## Target
Rigsarkivet, TKUA England A II 13, unit 261258, images 263-293, folder "Relation(er) fra Palle Rosenkrantz 1628-1629".
All 31 images fetched at full size (img/, FETCH_LOG.txt) and surveyed (WORKLOG.md). [measured]

## Letters (15)
| # | Date | To | Images | System | Size |
|---|---|---|---|---|---|
| 1 | 23 May 1628, Helsingor | (no. 138) | 264-265 | clear | - |
| 2 | 2 Feb 1629 | Statholder | 266R-270L | number code A (3 to about 1700, most under 200) | about 8 pages, heavy; not counted |
| 3 | 2 Feb 1629, No. 12 | king | 270R-271 | sign cipher | 43 tokens, 3 lines |
| 4 | 15 Feb 1629, No. 13 | king | 272R-273 | sign cipher | 75 tokens, 6 lines |
| 5 | 15 Feb 1629 | Statholder | 274R-276L | number code A | about 7 lines; not counted |
| 6 | 20 Feb 1629, No. 14 | king | 277R-278 | sign cipher | 153 tokens, 16 lines |
| 7 | 7 Mar 1629 | Chancellor | 279 | clear | - |
| 8 | 13 Mar 1629 | Statholder | 280R-281L | number code B (to 2431) | about 11 lines; not counted |
| 9 | 13 Mar 1629, No. 20 | king | 282R-283L | sign cipher | 51 tokens, 6 lines |
| 10 | 13 Mar 1629 | Chancellor | 283R-284L | number code B, same ciphered sentences as letter 8 | about 9 lines; not counted |
| 11 | 20 Mar 1629 | Chancellor | 284R-285 | number code B | about 25 lines; not counted |
| 12 | 24 Mar 1629, No. 21 | king | 286R-288L | sign cipher | 22 tokens, 3 lines |
| 13 | 24 Mar 1629 | Statholder | 288R-290 | number code B | about 8 lines; not counted |
| 14 | 25 Mar 1629, No. 22 | king | 291R-292L | sign cipher | 18 tokens, 4 lines |
| 15 | 9 Apr 1629, No. 23 | king | 292R-293L | sign cipher | 46 tokens, 5 lines |
Sign cipher total: 43+75+153+51+22+18+46 = 408 tokens, 63 types, 43 lines [measured from TRANSCRIPTION.tsv].
No May 1629 letter: the "23 Maij" seen at triage is letter 1, of 1628. Nos. 15-19 are not in the folder.
Corrections to the lead: the number code is two codes (A before 10 March, B after: 289L margin "effter dj sidste
Zifre som jeg sende med Christen Clemetsen"); the number-code letters go to the Statholder and the Chancellor, the
sign cipher only to the king. [measured; clear Kurrent read at 2000 px, not collated]

## Period keys compared (unit 260610), before transcription
None fits. 127-128 (France 1629, homophones 44-98, words 200-240): numbers only; the sign cipher has just five
two-digit numbers (33, 68, 79, 84, 98) standing alone as words, and code A runs mostly under 44 and 100-200.
133-134 "DSM": the king's 1627 two-row letter alphabet and word list (carried by Rosenkrantz to Friis, edition II
nos. 70, 74), no drawn-sign alphabet. 137 "DSM": one sign per letter, closest in look, fails by eye on the recurring
word. 135, 123, 124-126, 139, 145-147, 149-150, 305, 308 and the bound register 151-200: wrong design, wrong sign
set or later date. The register was compared at sheet scale, not value by value, against code B. Detail: WORKLOG.md.

## Method and figures
- Transcription: TRANSCRIPTION.tsv, SIGNS.md (49 sign labels), frozen in FREEZE_TX.txt before solving. One reader,
  no second pass. Weak sign distinctions are listed in SIGNS.md.
- Split: training N12, N13, N14, N20 (322 tokens, 78.9%); held-out N21, N22, N23 (86 tokens, 21.1%).
- Language model: lm/da1620 (5-gram, 3-gram for short runs), 576,754 letters of Christian IV's own Danish letters
  1589-1635 from the Bricka/Fridericia OCR (German and Latin blocks filtered out by marker words).
- 24 solver runs, all logged in SOLVE_LOG.md, plus a control. Control: the solver recovers a planted key in full at
  21 and 28 sign classes on text of this size and fails at 36. The real text has 53 types raw, 22-37 after merges.
- Two merge schemes converged from two seeds each (M3, M5). Both decodes are not Danish and contradict each other.
- Pattern guess H1: a seven-sign word, pattern A B C A D E F, occurs six times, once after "och med de": ENGELSK(E)?
  Pinned, it scores worse than the free optimum and nothing else reads. Unsupported.
- Frozen candidate (M5): KEY.tsv, FREEZE_KEY.txt; decode_once.py -> DECODE.txt (the script was run three times with
  the same key: twice more to fix output formatting only).
- Shuffle (shuffle_out.txt), held-out, 72 letters: real -133.0; shuffles at or above real 1360/5000 (seed 20261112)
  and 1407/5000 (seed 7). The key has no predictive value. On training text 0/5000, which only shows it was fitted.
- Judge: judge/BRIEF.txt, judge/decode.txt prepared; held-out and full figures pending the judge. Solver's
  expectation: 0% sense.

## Gist
None. Unchecked context from the clear text only: Parliament, a levy with Colonel Mackay, money due to the king,
Danzig; the cipher hides names, sums and what "33", "79", "84", "98", the crescent and the long cross stand for.

## Why it failed, and what is open
- 340 letter signs in runs of 2 to 18 between clear words, 53 sign types, one unchecked transcription: too little
  for a blind homophonic search with this solver.
- Not tried: a second transcription pass to settle the sign classes; treating the raised ring and the digits as
  vowel marks or numerals by rule; word-pattern attack with a period word list; the clear context as cribs line by
  line; number codes A and B (large codebooks, not attempted: unlikely to break from ciphertext alone, though
  letters 8 and 10 give the same sentences twice, which helps transcription only).
- First thing to do before more work: settle item 3 of PRIOR_ART.md (Temler's key, KB Kallske Saml. 4to 436).

## Files
/home/claude/keyless/rosenkrantz1629/: REPORT.md, PRIOR_ART.md, WORKLOG.md, SOLVE_LOG.md, TRANSCRIPTION.tsv, SIGNS.md,
FREEZE_TX.txt, KEY.tsv, FREEZE_KEY.txt, decode_once.py, DECODE.txt, judge/, shuffle.py, shuffle_out.txt,
FETCH_LOG.txt, tools/, lm/, img/ (33 pages), keys/ (83 key images), dl/ (edition texts). 131 MB. tmp/ deleted.

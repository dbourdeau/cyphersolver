# PREREG — Morier 1808 (cyphersolver catalogue 2649) — frozen 16/11/2026 before any key search

Training (T): IOR/L/PS/9/67/18 (9 images on disk) + IOR/L/PS/9/67/20 (8 images on disk), which is a second
copy of the SAME letter (seen on 20_0001: "44,60,8. 98,90,80,93,69,97,74,96..." = 18_0002 line 1).
Held-out (H): IOR/L/PS/9/67/21 image 0001 (f.1r), a different, short letter (316 groups, 72 words),
transcription file H_21_0001.txt, SHA-256 3e3909169b0584431db25aee058ae30eadbdf7b61a06c3d753f17a3629bd6da3.
H will not be decoded, partially or wholly, before the key file is frozen by SHA-256.

System hypothesis: homophonic substitution of letters by numbers 2-99, word division by full stops, plus a
few 4-digit code groups (8674, 4040) taken as nomenclator words (excluded from the measure).

Key: a map number -> letter (or -> '?' unknown), fixed on T only (n-gram LM solve + cribs), frozen
as key.json with its SHA-256 recorded in HANDOFF.md BEFORE the measurement.

ONE measurement on H (lexical):
- Decode each H word with the key. Words containing a 4-digit group are excluded from numerator and
  denominator. Any number not in the key decodes to '?' and the word fails.
- A word counts as read if its decoded lowercase string is in the vocabulary V = all alphabetic tokens of
  bunch-1862/dl/lyons_newton.txt (Project Gutenberg, Lord Lyons vol. 1, English 19th-c. diplomacy),
  lowercased, count >= 1, with one-letter words restricted to 'a' and 'i'.
- Score S = read words / counted words.
- Controls: 200 within-class shuffles = random permutations of the letter values over the set of numbers
  of the key (same letter multiset, same numbers), RNG seed 1808 (python random), same scoring.
- PASS iff S >= 0.85 AND S >= max(control) + 0.30.
- H is burned after this measurement.

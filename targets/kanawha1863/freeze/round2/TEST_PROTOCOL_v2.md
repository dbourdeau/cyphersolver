# Round 2 test, written before scoring (13 Nov 2026)

Why the round 1 test failed: the share of adjacent word pairs found in a reference corpus is nearly route-independent for short
telegrams. Any route keeps the same bag of words, and with code words, names and dropped articles most pairs are unattested
whatever the order. The calibration run on the known crib (.341) scored below several random routes.

New test: held-out pair. key_v2.json is fixed from three pairs (.341/.114, .229/.137, .344/.138) and the corrections in .110,
and frozen (sha256 in key_v2.sha256) before the held-out telegram is scored. The held-out telegram is GLC02414.185: a cipher text
and its period decipherment grid on one sheet (Toland). Prediction: take the cipher words, drop the commencement words
(Wilderness, Turkey), fill each section's grid by the frozen route with rows = words/6, replace code words by key_v2 values, and
compare cell by cell with the period grid (case-insensitive; the struck "that" in the period grid is ignored).
Statistic: number of cells where our predicted word equals the period decipherer's word.
Control: 200 random six-column routes (random column order and directions, seed 1863) with the same code values and grid sizes.
Pass: predicted agreement above every control and at least 50 % of cells.
Also reported (not pass/fail): the heading-row statistic for .229, .339 and .344 under key_v2.

Disclosure: I glanced at the .185 sheet while triaging the downloads (I saw that it holds a cipher and a grid, and read its
opening words) before writing this protocol. No value in key_v2 comes from it.

# PREREG C05 — Dorffler (catalogue 1773), new held-out pages, language measure — frozen before the run
Date: 12/11/2026, ~20:25 CET. Executor: Claude Opus 5.5 via the API (claude-opus-5-5, code execution container), one run.
History: C03 (img. 476) and C04 (img. 474) FAILED against the period gloss (0.735 and 0.660 vs threshold 0.75);
diagnosis: the gloss is not word-for-word and spans line ends, so a gloss-alignment metric cannot reach the bar.
C05 therefore changes the METRIC (declared here, before seeing any decode of the new pages) and uses NEW pages.

Portion (never used for the key, never sent before): Riksarkivet SE/RA/2115/I/19/100 (1680-83), images 277 and 304
(IIIF R0003594_00277 and _00304), all cipher passages on both pages. Declared risk: 1682 may predate the 1686 key.
Key: TABLE.json = TABLE-C04.json (SHA in SHA256SUMS), FROZEN, applied unchanged. No value may be added or changed.
Order inside the run: (1) transcribe the cipher groups blind (do not read the pale gloss, do not decode), write
T-C05.txt and print its SHA-256; (2) decode with TABLE.json mechanically; (3) run the measure ONCE; (4) only then read.
Metric W: tokenise the decode into words (word = run of letters between group/word boundaries as the system marks
them; code words count as one word). W = share of decoded words of length >= 3 that are in LEXICON.txt (built only
from training glosses 467-476 + common German function words; SHA in SHA256SUMS).
Controls: 200 tables made by permuting the table's values at random among its groups (same value multiset),
seeds 0..199, same tokenisation. PASS if W >= 0.55 AND W >= max(controls) + 0.25 AND >= 150 groups transcribed.
Otherwise FAIL; no second measure on these pages. Count with Daniel's 95 % rule only if PASS.

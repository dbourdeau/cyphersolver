# SOLVE_LOG: ostermann1737 (24 Nov 2026, times UTC from the sandbox clock)

Language model: own 5-gram character model with spaces (`scripts/rulm.py`), no Russian model exists in `lang/`. Corpus: 160 ru.wikisource pages of 1700-1749 documents in pre-reform spelling (mostly Полное собрание законов, ДО), about 0.6 M characters; hash of the concatenated pages in `lmsrc/CORPUS_SHA256.txt`, page list in `lmsrc/FETCH_LOG_lm.txt`. Normalised to 31 letters (й, і -> и; э, ё -> е; ѳ -> ф). Genre is decrees, not diplomatic rescripts.

| # | attempt | settings | result |
|---|---|---|---|
| 0 | statistics, lines 1-16 | 637 signs, 33 labels | IC 0.0552; top sign S03 14.4%, S04 7.2%. Fits a one-to-one substitution on Russian. |
| 1 | hand guess | S03 S06 S16 as "отъ" or "онъ" (a free-standing 3-sign group, twice) | not pursued; left to the solver. S06 turned out to be н. |
| 2 | simulated annealing, lines 1-16, gaps as spaces, S26 and S33 as dividers | 5-gram, 30,000 steps, T 6.0 -> 0.05, swap 70% / unused letter 30%, 8 seeds, corpus at 143 pages (crawl still running) | 8 of 8 seeds: same key, score -1762.8. Reads as Russian. |
| 3 | same, corpus fixed at 160 pages | 6 seeds | 6 of 6: same key, score -1764.3 |
| 4 | same without spaces | 4-gram, 4 seeds | same key |
| 5 | key edit from training lines only | S28 (2 training occurrences): solver gave ѣ; set to ligature ѿ = "от" from "онъ _ себя" and "_править" | recorded in KEY.tsv note |

Not tried, not needed: homophonic or nomenclator models, syllable tokenisation (the first look suggested pairs with S03; the count ruled it out).
Failures: none in the solving. Fetch failures are in FETCH_LOG.txt.
Key frozen (FREEZE_KEY.txt) before `decode_once.py` ran on lines 17-20. The held-out lines had been seen as images during transcription (unavoidable on one leaf); no decode of them existed before the freeze.

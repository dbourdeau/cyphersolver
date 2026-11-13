# Hashes and how to re-run the 05r measure (catalogue 1555)

| file | SHA-256 |
|---|---|
| KEY-1555.json (frozen 12 Nov 2026, 20:56 CET, before the measure) | 76ab7684449a3cae197600fdbbfd44a05e118752cc31b560b8e7048ba9c2955e |
| lexicon_1555.txt (derived word list, committed) | 328049d33983471e857beabee5dfe36d97b4f3fe7e9e555f599358d6ac1ed533 |
| it_nunz_clean.txt (source corpus, not committed) | e59da4f993c12533dc6f3888ed36f3295f95b63efd19087b05531146c9fde4eb |

The preregistered run used the source corpus. `lexicon_1555.txt` holds the words that `measure_1555.py` keeps from that corpus: words of length 3 or more, with frequency 3 or more, after j->i and v->u. There are 6,463 of them. Each word is written three times, so the script builds the same lexicon from this file.

Re-run, from this folder:

    python3 -I measure_1555.py KEY-1555.json transcription_05r.txt lexicon_1555.txt

Output, re-run on 13 Nov 2026: `M 0.7962`, `controls max 0.175 mean 0.0181`, `PASS`. This is identical to `MESURE-1555-H.txt`.

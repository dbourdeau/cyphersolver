# sinclair1923 - code book screening (14 Nov 2026)

Criterion fixed in the protocol (SHA-256 below): a book is kept for a telegram only if (a) at least 90% of its code words are in the book (the aim is all of them; 10% allows for OCR) and (b) the word-by-word decoding, put into the clear words around it, gives connected, grammatical text. (b) is tried only on a book that passes (a). Declared deviation: the coverage count (a) was run once before the protocol was written; no code word was decoded before it, except the values of the six Western Union 1901 words read to rule that book out (below).

Method: exact match of each code word (as transcribed, then with the obvious corrections PAVILION, ARBITRATE, SUZERAIN, STONING) against the full OCR text of each book on archive.org (`_djvu.txt`, downloaded with curl). Code words counted: 67 distinct in the 1923-24 telegrams, 12 in 1922, 2 in 1916.

| archive.org id | Book | 1923-24 (67) | 1922 (12, corrected forms) | 1916 (2) |
|---|---|---|---|---|
| WesternUnionTelegraphicCode | Western Union Telegraphic Code (1901) | 6 | 6 (BLAMEFUL, GLADSOMELY, RECOMMIT, ARBITRATE, RESEMBLE, SUZERAIN) | 0 |
| abcuniversalcom00clau | ABC Universal Commercial Electric Telegraphic Code, 5th ed. (1901) | 6 | 4 | 0 |
| in.ernet.dli.2015.38270 | ABC Electric Telegraphic Code, ed. 5 (1901, second scan) | 2 | 4 | 0 |
| ocodigoelectrico00clau | ABC, Portuguese ed., O codigo electrico telegraphico (1915) | 5 | 2 | 0 |
| mcneillscode00mcneuoft | Bedford McNeill's Mining and General Code (1908) | 5 | 6, all on the meaning side (e.g. CONQUER = the sense of code word BROMOFORME), none as a code word | 0 |
| mcneillscodearra00mcnerich | McNeill's Code (1895) | 2 | 2 | 0 |
| generalminingnew00morerich | Moreing & Neal, New General and Mining Telegraph Code (1905) | 1 | 5 | 0 |
| liebersstandard00liebgoog, standardtelegrap00liebuoft | Lieber's Standard Telegraphic Code (1896) | 5 | 2 / 1 | 0 |
| liebrsfivelett00lieb | Lieber's Five Letter American Telegraphic Code (1915) | 5 | 1 | 0 |
| bentleyscomplete00bentuoft | Bentley's Complete Phrase Code (1906 text, 1909 issue) | 0 | 2 | 0 |
| acmecommodityphr00acme | Acme Commodity and Phrase Code (1923) | 0 | 2 | 0 |
| universaltradeco00code | Universal Trade Code (1921) | 1 | 2 | 0 |
| imperialcombinat00broo | Broomhall, Imperial Combination Code (1913) | 0 | 2 | 0 |
| UnicodeUniversalTelegraphicPhraseBook | Unicode (1896) | 0 | 0 | 0 |
| americanbankersb00amer | American Bankers and Brokers Telegraphic Code (1920) | 0 | 0 | 0 |
| moderneconomyte00peycgoog | Modern Economy Telegraphic Code (1908) | 0 | 0 | 0 |
| telegraphiccode00amer | Telegraphic Code (1911) | 1 | 0 | 0 |
| everybodyspocke00saun | Everybody's Pocket Code (1911) | 0 | 0 | 0 |
| privateconfident00will | Private and Confidential Cipher Code (1916) | 0 | 1 | 0 |
| privatecode00nati | Private Code (1924) | 0 | 0 | 0 |
| cinemacodepracti00poil | Cinema Code (1923) | 0 | 3 | 0 |
| heathtelegraphic00heat | Heath Telegraphic Cipher (1900) | 2 | 1 | 0 |

No book passes (a), so nothing was decoded. The five-letter halves of the ten-letter words (TUBOL/DNUMD, KANYX/YAMUL, XORUS/OMTUL) are in none of these books either, Bentley's five-letter list included.

Western Union 1901 as the control for the 1922 telegram: the six words it holds mean "if it is appropriated" (BLAMEFUL), "by next post" (GLADSOMELY) and the like, which does not fit "PAVILLION MONDAY ARROGANCE BLAMEFUL GLADSOMELY FOUR OCLOCK THURSDAY ARROGANCE"; ARROGANCE, HYGIENIC, DEMAGOGUE and CONQUER are not in it (only neighbours: HYGIENICO, DEMAGOGIC, CONQUERED). Ruled out.

The 1923-24 words (ASEGURABAN, COLLIGAREM, VERLANDEN, ONTPLANKEN, REGBARKEIT, TORVISCO...) are words of eight languages, as in the Berne official vocabulary of 1901; every code built on it shares a handful, which is the 5-6 word overlap seen above. The book behind them is none of those screened. The ten-letter words with X, Y and consonant clusters (TUBOLDNUMD, KANYXYAMUL, XORUSOMTUL, GJPLYJWD, YDMLOXO, XINPARX) are not vocabulary words: either artificial words of the book or telegraph garbles.

Not reachable without a browser: HathiTrust full-text search (anti-robot page answers curl, 14 Nov 2026), Google Books (anonymous API quota exhausted). Not on archive.org: ABC 6th ed. (1920), Western Union Universal Codeword, Bentley's Second Phrase Code (1929, too late), Peterson, Lombard, Scott's, Marconi International Code (1919), the Berne vocabulary itself, Wright's Codigo brasileiro universal (1902; the only code book besides the Berne vocabulary that the vetting found holding COLLIGAREM and ASEGURABAN).

Frozen files (sha256): PREREG.md 305566346288c387252f91e2e0deb58df833ebb5e85bea961a2ddf5d639f7c72; transcription.txt 39461ebae190ce09876a4eeef918ffa1741de4f698564b7e86a860df5c51cf3e; codecheck.py 77c76fb8fee0b26eeea33844d4e3450b8915302b129b310f845df3a6fd880ed8; screening_results.txt 8fe094213f55587ca8d0aba11fd8b7490fb8c378ece986962f4c43c01f4d6ce2.

## HathiTrust full-text search (14 Nov 2026, in the contributor's own browser)
- TUBOLDNUMD, and CATCHFLYS + SOOTHSAYER + YELLOWFISH together: no hits.
- ANZUNDET alone: only German texts (anzündet), so it is not a useful search term.
- ANOMALIDAD + ASEGURABAN + COLLIGAREM together: one hit, the International Telegraph Bureau's *New official vocabulary for telegrams in preconcerted language* (Bern, 1901; search-only on HathiTrust). This confirms that the 1923-24 code words come from the 1901 Berne vocabulary. The code book that gives them meanings is still not identified.
- ASEGURABAN + TEOBROMA, and ARROGANCE + BLAMEFUL + GLADSOMELY + HYGIENIC (the 1922 telegram): only unrelated books (a Spanish-language history, an English-Portuguese dictionary). No code book in the hits.

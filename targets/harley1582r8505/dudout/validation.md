# Held-out check of key.json (29 Oct 2026, session C03), registered before transcription

Portion: the last two cipher lines of f. 264v (after the clear "pour revenir aux deux points proposez"), absent from b28, so never decoded by anyone. Transcribed sign by sign from DECODE R8010 P4 by shape only, frozen (sha256 f7431011add31bd9817201222c5a4cc546418ca2b0cf01feac24a5f3b6846ba9) before decryption; key.json applied unchanged; one measurement.

Criterion fixed in advance (protocol hash 25be34d0...): share of characters falling in French words (Viterbi segmentation with word.py's lexicon, seed 20261029) >= 0.85, and strictly above each of 200 control keys (letters permuted, homophone structure kept).

Result: coverage 0.886; controls max 0.737, mean 0.483; 0/200 >= real -> rank 1/201 -> passed.

Reading of the two lines (not used in the measurement): "a {sauoir} les moiens que <lelent> tenir e <alonrs> se renforcer daliances / et pour {diuertir} les {efforts} de ses ennemis sans {beaucoup} {simcomoder}".

Caveat: the later re-transcription of 3.10-3.12, 3.35 and 3.38-3.46 (session C04) was not blind (the b28 decoding was known); doubtful shapes are marked a/b? and every word that depends on one is counted probable.

Targeted blind re-reading (session C05/C06, 29 Oct 2026): 12 doubtful signs of 264v shown to Brice Dudout as shapes only (no letter or value), each to be matched against certain shapes taken elsewhere in the letter; the effect of every answer was fixed and hashed (sha256 f784d23d...) before the answers and applied mechanically. Result: 6 words probable -> certain (qu'ele, tant, esté, ofrir, seruice, denier); laisses/traites -> {laissee}/{traitee} (final sign = e), still probable; recherchee, font, despende unchanged (no clear choice); first sign of <cissuada> confirmed c. Unresolved: 31, unchanged.

# Check of the contributor's keys and decryption (9 Nov 2026, repository commit a181cd7)

What an AI model (Claude) checked of the submission by Harumi-Matsuba (issue #364). The NARA frame images are not reachable from the project's environment, so **no transcription was compared with an image by the project**. No human has repeated the check, and the contributor's transcriptions were made by an AI.

## 1. The decryption

An own implementation of the double columnar transposition (written from the description, not by running the contributor's code) undid the second transposition with the 28-column key and then the first with the 24-column key on the six parts of the contributor's transcriptions (indicator groups removed; part 3 with lines 2 and 3 put back in order and letter 113 read T, as he describes). The six results (174, 173, 162, 125, 200 and 189 letters, 1,023 in all) are identical, letter for letter, with the rows of `plaintext.txt`. They read as German: "GKDOS X ERSTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X GIBT AN FLUGABWEHRKOMMANDO X SCHWARZWALD ..." and "GEHEIME KOMMANDOSAQE X AM X EINSSEQS ...".

## 2. Control against random keys

Counting the positions where one of 30 frequent German trigrams starts, the six decryptions give 66 hits in all. For 300 random pairs of keys of the same lengths (24 and 28 columns), the sum over the same six parts has a mean of 8.9 and a best of 19. The contributor reports 66, 8.7 and 19 for 1,000 random keys. This is the same measure as his, so it shows that the keys make German and not how many letters are right.

## 3. What the project could not check

- The transcriptions against the NARA images (the typed frame 0993 and the hand-written frames 1025-1027).
- The recipient's fair copy and the teleprinter original, which the contributor used for the plaintext and as a calibration (98.8% and 91.1% agreement, his figures).
- The second reader's agreement (99.2% for frame 0993, 93.8% to 95.4% for frames 1025-1027, his figures) and the image-based judgements.
- The known-plaintext tools (`src/kpa.c`, `src/kpb.c`), whose results are the keys above.
- Statistical validation by the project's n-gram test: it is made for substitutions and does not apply to a transposition.

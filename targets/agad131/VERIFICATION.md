# Check of the contributor's key application and decryption (10 Nov 2026, repository commit af80f5e)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #331). The AGAD scans are not reachable from the project's environment, so **no transcription was compared with a scan by the project**. No human has repeated the check.

## 1. The decryption

The cipher lines of `transcription.txt` (the lines that are not clear Polish in << >>) were decrypted again with the 24-letter reciprocal key of `key.tsv` by an own script, number groups kept as groups: 64 lines. Compared line by line with `decryption.txt` (clear Polish and bracketed numbers removed), 62 of the 64 lines are identical and the letter agreement over all lines is 99.9%. The two other lines differ by struck-out or bracketed marks in the contributor's file.

## 2. Control against shuffled keys

A word list of about 80 common French words (articles, prepositions, auxiliaries, and words of the letter such as protection, subside, comte) was matched by longest match in the decryption of the 64 lines. With the key 46.3% of the cipher letters fall in listed words; shuffling the key values 200 times gives a mean of 4.5% and a best of 19.1%. This shows that the key makes French, not how many words are right; the word list shares vocabulary with the reading.

## 3. What was not checked

- The transcription against the scans, and the contributor's two passes (88% agreement on 2,514 tokens, about 300 differences not settled on the scan).
- The contributor's count-matching fit (97.7% of tokens), the language-model scores and the blind reader (about 75% of the clauses translated).
- The identification of the writer (Matuszewicz), the addressee (Branicki), and the names and events of the Strutyński affair, which are the contributor's reading and are not checked in print here.
- The 446 key itself, which is the target `branicki1757`.

## 4. Second check and recount (14 Nov 2026, Brice Dudout with Claude)

- **Decoder.** A second decoder, written from `key.tsv` alone (24 pairs, digit groups kept as groups, `[struck ...]` dropped), was run on the 91 lines of `transcription.txt`. Against `decryption.txt` (clear Polish and bracketed numbers removed) 2,447 of 2,449 letters agree (99.9%); the two differences are the transcription's capital X in `Xeyni...` (p4.14) and `Xowno` (p4.17), outside the key, which `decryption.txt` gives as K (Keynixbergue, Kowno). The result of section 1 is reproduced; no key value is in question.
- **Recount by the README rule.** `research/reading_audit/v10_relabel.share` on `reading.md`: 895 words, 27 holes, read share 0.971. The Polish passages in clear (the opening, the paragraph on the secretary, the close and the date) are not cipher; with them left out the French cipher passages give 576 words, 22 holes (the `[?word]` and `[?name: code]` places), read share **0.963**. This replaces the contributor's estimate of 0.946 (about 25 of some 460 cipher words), which the project had not recounted.
- **What this does not change.** The scans were not seen (szukajwarchiwach is not reached by script), and the about 300 differences between the contributor's two transcription passes are still not settled on the scan. The measure counts the reading as written; it cannot see a word misread from a look-alike sign.

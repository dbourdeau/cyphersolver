# Check of the contributor's key and decryption (10 Nov 2026, repository commit af80f5e)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #332). The archive's images are not reachable from the project's environment, so **no transcription was compared with an image by the project**. No human has repeated the check.

## 1. The decryption

The cipher words of `transcription.txt` (the runs between bracketed clear text, with every token a letter sign of the key) were decrypted again with `key.tsv` by an own script: 108 cipher words. Compared word by word with the literal decodes in `decryption.txt` they are identical in all 108 cases. The contributor counts 113 cipher words; the difference is words that his decryption splits or that carry a numeral inside, which the script leaves out.

## 2. Control against shuffled keys

A word list of about 90 common Italian words and forms (articles, prepositions, auxiliaries, and words of the letter's own vocabulary) was matched by longest match in the decryption of those 108 words. With the contributor's key 55.1% of the letters fall in listed words. Shuffling the 20 key values 200 times gives a mean of 9.4% and a best of 27.7%. The contributor reports 65.3% against a mean of 1.9% and a best of 11.4% with a larger 15th-century word list. This shows that the key makes Italian, not how many words are right; the word list shares vocabulary with the reading.

## 3. How much of the cipher reads

By the contributor's count 88 of 113 cipher words are read in full (77.9%), 21 hold a doubtful letter and 4 are open; counting the 60 code items for persons that stay unread as cipher items, 88 of 173 = 51%. Either way it is far below the 95% read bar, so this is a partial reading.

## 4. What was not checked

- The transcription against the archive's images, and the contributor's AI re-reads of doubtful signs.
- The independent review by a second AI model, the blind first-stage check (30 of 31 words) and the method check on test texts (98.5% to 99.8%).
- The reading of the clear Italian between the cipher runs (partly provisional) and the historical context (Alcáçovas, the Pazzi war), which is the contributor's inference.
- Rubinstein's edition and any other print of the letter.

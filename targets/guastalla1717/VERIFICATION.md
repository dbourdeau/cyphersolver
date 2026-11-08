# Check of the contributor's key and reading (8 Nov 2026, repository commit af80f5e)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #329). The Estense scans are not reachable from the
project's environment, so **no transcription was compared with a scan by the project**. No human has repeated the check.

## 1. The key

`key.tsv` has 32 two-digit values that stand for letters, 9 single digits for a word's last vowel (5 a, 6 e, 7 i, 8 o, 9 u) and
11 other entries (code groups and the exception b = 25 among them). Several letters have more than one number (for e, 37, 77 and 38;
for a, 30, 70 and 54), the 3x and 7x twins being the contributor's convention for a hard-to-tell first digit.

## 2. The decryption

The cipher groups of `transcription.txt` (clear parts left out, bracketed notes left out) were decrypted again with `key.tsv`
by an own script, taking two-digit pairs from the left and a final single digit as a last vowel: 1,668 letters. Compared with the
letters of the contributor's `decryption.txt` (1,600 letters, bracketed notes removed) by a sequence match, 95.2% agree. The
difference is mostly groups the contributor read by sense and left out or normalised, and unread code groups.

## 3. Control against shuffled keys

A word list of about 130 common Italian function words and words of the letter's own vocabulary was matched in the decryption
of the 1,668 letters. With the contributor's key 35.2% of the letters fall in listed words; shuffling the letters of the 32
two-digit values 300 times gives a mean of 17.7% and a best of 34.5%. The test separates the key from the average shuffled key but not
clearly from the best one, so it is weak: it does not measure the key, and the project relies on the reading as Italian sentences
(for example "in sostanza vedo ... era ritornato da' suoi beni ... aspettavano le mie risposte sul tenore delle antecedenti
lettere") and on the contributor's own held-out figure (98.3% agreement of a half-text key with the full key, not repeated here).

## 4. How much of the cipher reads

Counting the cipher part of `reading.md` as 356 units (words, with a code group in brackets counted as one unit), 34 carry an unread
code group or a [?] mark: 322 of 356 = 90.4%, so this is a partial reading by the project's bar of 95%.

## 5. What was not checked

- The transcription against the scans, and the contributor's two-pass agreement (92.0% of 3,064 digits).
- The contributor's blind reader, the held-out half and the Italian-model score.
- The identification of Trautson and Starhemberg with ministers of the imperial court in 1717, and Affò's history.
- The date: the dateline's "7bre" as September is the contributor's reading; the Estense record says July.

# Test plan: known keys on the blind transcriptions (written 15 Nov 2026, before any decryption)

Written after the four blind transcriptions and the seed check were complete and before any key was applied to
them. The sha256 of this file and of the four `transcription.tsv` files is recorded in `test/FROZEN.sha256` before
the run. One run. Every telegram is reported, including those that do not pass.

## Units
Every telegram with cipher groups on the open frames, as found by the readers (telegrams paired by their order on the
frame):

| id | frame | telegram |
|---|---|---|
| T01 | vol. 196 fr. 0053 | 8 Mar 1865, to D. W. Adams |
| T02 | vol. 196 fr. 0056 | 9 Mar 1865, to D. W. Adams (first) |
| T03 | vol. 196 fr. 0056 | 9 Mar 1865, to Lt Col W. M. Levy, Montgomery (second) |
| T04 | vol. 196 fr. 0064 | 13 Mar 1865, to the Secretary of War |
| T05 | vol. 196 fr. 0065 | 13 (or 14) Mar 1865, to Maury |
| T06 | vol. 196 fr. 0071 | 17 Mar 1865, to Taylor at Selma |
| T07 | vol. 11 fr. 0044 | 10 Apr 1865, to Taylor (first) |
| T08 | vol. 11 fr. 0044 | 10 Apr 1865, to Maury (second) - already read and printed (OR I/49/2 p. 1223): positive control |
| T09 | vol. 11 fr. 0045 | 10 Apr 1865, to Maury |
| T10 | vol. 11 fr. 0046 | 11 Apr 1865, to Maury (first, flowing capitals) |
| T11 | vol. 11 fr. 0046 | 11 Apr 1865, to Maury (second) |
| T12 | vol. 10 fr. 0056 | 18 Jan 1865, Tupelo, to President Davis |
| S1, S2 | vol. 196 fr. 0061; vol. 11 fr. 0039 | the seed telegrams (read, key COME RETRIBUTION): positive controls |

## Ciphertext
For each telegram and each reader separately: the reader's preferred letters (first form of each `[X/Y]`), cipher
groups joined in order, letters A-Z only; `?` dropped. So every telegram is tested twice, once per reader.

## Keys and offsets
Standard Vigenere, plaintext = cipher - key (mod 26), key running over cipher letters only.
Keys: COMPLETEVICTORY, COMERETRIBUTION, MANCHESTERBLUFF, THENAVYOURPRIDE. Offsets: every phase 0-14 for the first
cipher letter.

## Score
Mean log10 quadgram probability per quadgram, model from the OCR text of the Official Records Ser. I vol. 49 pt. 2
(Internet Archive `warofrebellion014902rootrich_djvu.txt`, letters only, sha256 in
`sources/raw/taylor1865_open_2026-11-15/or_text/SHA256SUMS`), floor log10(0.01/N).

- One-phase model (M1): best score over 4 keys x 15 offsets.
- Two-phase model (M2), allowing one slip (a letter dropped or added by the clerk or the reader): the stream is split
  at one cipher-group boundary, each part at least 15 letters, each part with its own phase of the same key; the three
  quadgrams across the split are not scored. Best over keys, phase pairs and splits.

## Controls (same maximisation as the real text)
- Shuffled: 200 random permutations of the telegram's own cipher letters (group lengths kept), each scored with the
  same model (M1 or M2) maximised over the 4 keys and 15 offsets.
- Wrong keys: 200 random 15-letter keys (uniform letters), each maximised over the 15 offsets (and phase pairs and
  splits for M2), on the real ciphertext.
- Random seed fixed at 1865.

## Pass mark (fixed now)
A telegram passes under a model for a reader when its best score is above the maximum of all 400 control scores
for that telegram, reader and model. A telegram **yields** if it passes under M1 or M2 for both readers with the
same key. M2 alone counts only with the split point stated and is reported as "one slip".
The positive controls (S1, S2, T08) must pass under M1; if one fails, the test is reported as not working and no
other result is claimed.

Key identification: the winning key is reported with the margin over the best other key. COMPLETE VICTORY and COME
RETRIBUTION share letters (C, O, M, E, T in six places), so a margin below the spread of the wrong-key controls
(their 95th minus 5th percentile) is reported as "key not separated".

## Reading step (after the test)
For each telegram that yields: decrypt both readers' transcriptions with the winning key and phase(s); list per
group the plaintext of each reading; where the readers disagree or a letter is marked doubtful and the choice
decides a word, show both readings; settle on the image where possible (crops in `work/settle/`). Words that need
a letter other than either reader's reading are marked as corrected, not read. Telegrams that do not yield are
reported as not yielding; no reading is forced on them.

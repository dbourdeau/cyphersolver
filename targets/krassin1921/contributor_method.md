# Method

## 1. Transcription
- First transcription: the five-digit groups were taken from the OCR served by the NARA catalogue (M316 roll 43). The typewriter has no digit one and uses a capital I, which was turned into 1.
- The "/21545/" at the head of frame 0428 repeats the last group of frame 0427 (a catchword) and was left out. Nr 451 then has 1,600 digits.
- One digit was changed after looking at the image: the first digit of the 2nd group on the 12th line of frame 0427, which has an "I" typed above it (0 → 1).
- Second, independent transcription: the text of the frames was cut into eight strips of seven lines (long side 2,000 px) and given to OpenAI Codex one at a time, from an empty directory. It received the image and the prompt (`second/PROMPT.md`) only: not the first transcription, the table or the plaintext. The run logs show one answer per run and no command execution. Output: `second/codex/`.
- Comparison: digit groups only, {a/b} taken as its first choice, digit streams aligned. Nr 451: 1,598 of 1,600 digits agree (99.88%). Nr 523: all 575 agree.
  - Difference 1: second digit of the 2nd group on the 5th line of frame 0427. The digit is overstruck on the sheet; the OCR reads 5, Codex 0 (or 9). The plaintext wants 7 (the а of выслать). The data keep 5 and the pair is counted as not read.
  - Difference 2: the group 00668 on frame 0427. The image has 00668; Codex dropped a digit.
- **No human compared the images with the transcription.**

## 1a. Spot check of agreed digits (two-way choice on the image)
- From the digits on which the two transcriptions agree, 90 were drawn at random per message (in Nr 451 without the two differing digits and the one changed from the image). Ten of them were marked beforehand as control items, to see that the judges look at the image.
- For each digit the judge saw a crop of its group and chose between the transcribed digit and a digit often confused with it (0 with 6 or 9, 1 with 7 or 4, 3 with 8 or 5 ...). The order was random and the transcribed digit was not marked. Judges: OpenAI Codex (gpt-6-astra, reasoning effort high; 18 sheets of ten questions, one sheet per run) and Claude Sonnet (the same 18 sheets). Example prompt: `second/PROMPT_judge.md`; questions and answers: `second/judgements.tsv`.
- Result: in both messages both judges chose the transcribed digit in all 90 questions (80/80 and 10/10). No digit was changed.
- In a two-way choice a planted error can only be a wrong digit among the options, so the ten control items have the same form as the other 80.

## 2. Finding the system
- A Russian number word stands before the groups (SOROK = 40, DWADZAT TCHETYRE = 24). The digit counts are 1,600 = 40 x 40 and 575 ≈ 24 x 24.
- Cut into runs of that length, the digits fall into columns of high digits (6-9) alternating with columns of low digits (1-5). Leaving out 0, the digits that fit this pattern are 1,169 of 1,232 in Nr 451 (94.9%) and 445 of 468 in Nr 523 (95.1%). The rest are the pairs outside the table (10, 33, 28 ...) and errors.
- Pairing two neighbouring columns row by row gives about 30 kinds of pair (37 in Nr 451, 34 in Nr 523) with an index of coincidence of 0.0551 and 0.0490, which fits a substitution of one pair per letter.
- Direction: in the square of Nr 451 only the four rightmost pairs of row 39 carry text; everything to their left and all of row 40 is 00. The text ends at the right edge, so the rows are read right to left. Nr 523 has both the column order (second digit first) and the row direction reversed.
- That the columns are not permuted follows from long repeats (the 14 pairs of "представите..." and others) that recur at different positions inside the rows.

## 3. Recovering the table
- Only the 764 pairs of Nr 451 were used. Simulated annealing assigned 32 Russian letters one-to-one to the 32 commonest pairs, scored with Russian letter 4-grams; three runs ended at the same score and the text was readable. No crib was used.
- Three values were then changed on reading the text: 10 (ф → full stop), 33 (й → comma), 71 (ъ → ф, in атмосферы). The annealer had given ц to 28; since 28 only occurs in "ревизионая [28]ия" (three times) it was taken out of the table and moved to the open points.
- The table was then applied to Nr 523 unchanged. Nr 523 was not used to build it.

## 4. Control
- `src/control.py`: the 30 letter values of the table are shuffled 1,000 times, the same ciphertext is decrypted with each, and the mean Russian 4-gram score per letter is compared (4-gram table from the 50,000 most frequent words of wordfreq). No shuffled table reaches the real one in either message (real -11.127 and -12.329; best shuffled -14.686 and -14.796).
- With the real table and the rows read the other way the scores are -13.889 and -14.282, close to the shuffled tables.
- Nr 523 took no part in building the table, so its reading with the same table is an independent check of the table.

## 5. Counting "pairs that read as sense"
- Each pair in reading order (without the trailing 00) is classed as read or open (`status` in `data/reading_*.tsv`): read means it has a table value and that value is part of a word.
- Counted as open: pairs outside the table (also those given a value from context), the wrong letter of a word with one wrong letter, a pair containing the overstruck digit, and the last pair, which lacks a digit.
- Nr 451: 14 open of 764, 750 read (98.2%). Nr 523: 9 open of 288, 279 read (96.9%).
- Word breaks and the reading of the punctuation are the reader's. The text is telegraphic and drops prepositions, so some case relations can be read more than one way.

## 6. Calibration
No contemporary decipherment and no printed text of these messages was found (`docs/PRIOR_CHECK.en.md`), so there is no blind calibration.

## 7. Limits
- The transcription is by OCR and AI; no human has checked it.
- The values of the pairs outside the table (комисс, раб, ц) are inferred from context, and the number pairs are not read.
- The identification of the persons (Кулябко, Бродовский, Штелер) and the dating and context rest on these two texts alone and have not been compared with other sources.

# Method

## 1. Sources and first transcription
- The images are the public NARA frame images (`SOURCES.en.md`). The transcription was made from the images by an AI (Claude Fable 5.1). No human has checked it.
- Frame 0993 (typed): first read from an image reduced to 2,400 pixels on the long side, then every line was re-read from the original image (3,552 x 6,112) enlarged line by line. The re-reading changed three letters of part 4 (letters 17, 62 and 130, Q to O). Pen marks made by the recipient under the letters had looked like the tail of a Q; in this typeface the Q has its tail inside the bowl.
- Frame 0993, part 3, letter 113 (third letter of EDIMN) is a vertical bar with short bars at top and bottom. It was first read as I with the note "may be T". The second reader (section 6) read T, and decryption gives a word only with T (STELLUNGEN). It was corrected to T. `data/ciphertext_0993.txt` keeps the first reading; `src/decrypt.py` applies the correction.
- Frames 1025-1027 (hand-written): read from the original images. After decryption the images were looked at again and seven letters were corrected (six times a g with a cross-stroke on the descender to q, once o to c). The reading before these corrections is `data/ciphertext_1025_1027_before_decryption.txt`. All seven (one of them is in an indicator group) were read the same way by the second reader, who did not know the decryption.

## 2. System
Frames 0349 and 0350 of the same reel hold an exercise message of 25 February 1939 and the key card of that day. The card gives two number sequences (a = 21 numbers, b = 19 numbers) and four three-letter Kenngruppen. That message can be read as a double columnar transposition (write the plaintext in rows under key a and read the columns in the order of the key numbers; write the result under key b and read it the same way), as reproduced by the Cyphersolver ledger. The same system was assumed for the 1940 messages. The difference is the position of the key indicator group (the seventh group in 1939, the first group of each part in 1940).

## 3. Fixing the plaintext first
Frame 0993 has a fair copy by the recipient (frames 0994-0995). The fair copy is in ordinary writing; it is not the text as it was enciphered (with numbers and signs spelled out and X as separator).

A transposition does not change the letter counts. So the letters of each part were counted, and candidate spellings of the words of the fair copy (are brackets spelled KLAMMER, how is "Ia" spelled, and so on) were fitted until the counts agreed.
- Part 3 (162 letters): `SETZT DREI ZUG FLA M G RES KOMP DREINULLVIER KLAMMER SIGMARINGEN KLAMMER BEIMSQUTZOBJEKTHERBERTINGENEIN TRANSPORT… DIENEUENSTELLUNGEN`. The 147 letters other than X agreed with the cipher text except for one letter (letter 113 above).
- Part 4 (125 letters): `UNDFEUERBEREITSQAFTZUMELDEN LUFTGAUKOMMANDO ROEM SIEBEN STRIQ ROEM EINS ANTON OP ZWO NR ZWOAQTFUENFEINS STRIQ VIERNULL GKDOS`. All 110 letters other than X agreed. That "Ia" is spelled ROEM EINS ANTON and "/" is spelled STRIQ was found at this step.
- The positions of the X cannot be found from the counts (both parts have 15).

The plaintext assumed at this stage differed slightly from what decryption later showed (part 3 has DURQ and FRIEDRICHSHAFEN where DURCH and FRIEDRIQSHAFEN had been assumed; part 4 ends G X KDOS).

## 4. Recovering the keys (known plaintext)
Neither the key lengths nor the keys were known. Two tools were written; each uses a property that does not depend on one of the two keys.
- `src/kpb.c` (second-key side): after undoing the second transposition, adjacent letters of the intermediate text are plaintext letters "length of the first key" apart, whatever the order of the first key. From the plaintext the set of letter pairs and triples La apart is built, and the second key is varied by simulated annealing to maximise the number of adjacent pairs and triples of the intermediate text that lie in the set. If an X of the plaintext is misplaced, only the pairs spanning it are lost.
- `src/kpa.c` (first-key side): letters of the intermediate text "length of the second key" apart stand in the same column of the second grid, so they must occur as adjacent letters of the cipher text, whatever the order of the second key. This needs every plaintext letter in its exact position.

Test: on the 1939 exercise message (216 letters) both tools single out the correct pair of key lengths (21, 19): kpa reaches the full score and returns the first key of the key card, the 24 neighbouring pairs score 0.33-0.41; kpb scores 0.81 against 0.33-0.35.

Applied to part 4: kpa was first run on all pairs of key lengths from 2 to 26 for each candidate placement of the X. No pair reached the full score, but for several candidates a first key of length 24 came out on top. kpb was then run on first-key lengths 20-28 and second-key lengths 2-40: (first key 24, second key 28) scored 0.72-0.76, all others 0.57 or less. In the intermediate text so obtained, 15 of the 24 five-letter strings formed by taking every 24th plaintext letter occurred verbatim. kpa then fixed the first key, and the second key was read off by locating the columns of the intermediate text in the cipher text. Because the plaintext had been assumed to begin with an X, the first key found at first had its columns rotated by one; the rotated key is the key in `data/key.txt`.

## 5. Checks on the keys
- The keys were recovered from part 4 of frame 0993 (the final rotation of the columns was confirmed by parts 1, 2 and 4 becoming readable). **Parts 1 and 2, which were not used for the key recovery, decrypt with the same keys as they stand.**
- Part 3 did not decrypt. Encrypting the plaintext of section 3 with the keys and aligning it with the page showed that **lines 2 and 3 of part 3 (50 letters each) are interchanged on the page** (longest common subsequence of expected and actual cipher text 99 letters; 59 for a shuffled control). With the lines put back, part 3 decrypts.
- **Another message of the same day** (frames 1025-1027, found by searching the OCR of the catalogue for frames dated "17. Mai 1940") decrypts with the same keys. Its plaintext had not been looked at before decryption (afterwards it was found to have the same content as the teleprinter message on frame 1024).
- Control: the six parts were decrypted with 1,000 random keys of the same lengths and compared for German. None was as good as the real keys.
  - Count of 30 frequent trigrams of ordinary German (`src/decrypt.py control`): real 66, best random 19, mean 8.7.
  - Mean log score per letter from a table of German four-letter statistics (a local table, not included here): real -4.704, best random -7.243.
- Calibration (`src/calib.py`): the decryption was turned back into ordinary writing and compared, as a sequence of letters and digits, with the contemporary texts in the same file. Frame 0993, parts 1-2 (the fair copy was not used for these in the key recovery): 254 of 257 characters (98.8%). Frames 1025-1027: 215 of 236 (91.1%; most differences come from the radio version writing Flgabw.Kdo and Centimeter where the teleprinter message has Flugabwehrkommando and cm). Parts 3-4 of frame 0993 give 98.9% but do not count as calibration, because their plaintext was fixed with the fair copy in view.

## 6. Second transcription by another reader
OpenAI Codex (codex-cli 0.163.0-alpha.10.2, model gpt-6-astra, reasoning effort high) was given the line images and a prompt only and read them blind (no key, no first reading, no plaintext; the run logs show no command execution and no file access). Prompts are in `second/`, the returned readings in `second/codex/`. The prompt for the handwriting had been written for a message of another day before this message was decrypted; only the description of the number of images was changed. One run each.

| Message | Version of the first transcription | Agreement (text without indicator groups) |
|---|---|---|
| 0993 (634 letters) | revised (O/Q corrected) | 629 (99.2%) |
| 0993 | first version | 628 (99.1%) |
| 1025-1027 (389 letters) | after correcting 7 letters following decryption | 371 (95.4%) |
| 1025-1027 | before decryption | 365 (93.8%) |

Decrypting the letters on which the two readers differ (5 in 0993, 18 in 1025-1027): for 22 of them the first reading gives a word and the second does not; the reverse holds for one letter only (0993, part 3, letter 113).

## 7. Image-based judgements (two models)
Letters on which both readers agree can still be wrong, so a sample of agreed letters and all disputed letters were judged from images. The judges were OpenAI Codex (gpt-6-astra, high) and Claude Sonnet. Each received the image of one five-letter group and the question "is the letter at position n X or Y?" (which of the two is the first reading was not disclosed, the order was random, and no key or plaintext was given). Questions and answers: `second/judgements.tsv`; examples of the prompts: `second/PROMPT_judge_*_example.md`.

- Per message: (a) 80 agreed letters chosen at random (the alternative is a similar-looking letter); (b) 10 planted items (to measure whether the judge can tell similar letters apart; same form as (a)); (c) all disputed letters (the alternatives are the first and the second reading). 203 questions in all.
- **Repeat**: in the first round some group images were cut wrongly (in message 1, the six groups of line 3 of part 4 were shifted by one group; in message 2, part 2, the crops sat too high and cut off the descenders). This was noticed from a judge's report; the images were corrected and the 57 affected questions were put to both judges again. The figures below are after the repeat.

| | Message 1 (typed) | Message 2 (hand-written) |
|---|---|---|
| Sample of 80 agreed letters: first reading chosen | Codex 80, Sonnet 80 | Codex 80, Sonnet 76 |
| 10 planted items: correct letter chosen (the check was to be void below 6) | Codex 10, Sonnet 10 | Codex 8, Sonnet 8 |
| Disputed letters: first reading chosen | of 5: Codex 3, Sonnet 3 | of 18: Codex 13, Sonnet 11 |
| Letters for which both judges chose against the first reading | 1 (part 3, letter 113, I to T) | 4 disputed letters and 2 planted items |

Only letter 113 of part 3 of message 1 was corrected (both judges and the second reader read T; decryption wants T).

The six letters of message 2 for which both judges chose against the first reading (r/k three times, n/u, g/q and l/b once each) were not changed. Decrypted with the keys, the first reading gives words for all six (ROEM, NULL, TUELLINGEN, ZUGETEILT and others) and agrees with the contemporary teleprinter message; the judges' letters do not. In this hand r and k, and n and u, are evidently easy for an AI to confuse from the image of a single group.

## 8. Use of AI
- Transcription, fitting of the plaintext, writing of the key-recovery tools, decryption, documents: Claude Fable 5.1 (Anthropic).
- Second transcription and image-based judgements: OpenAI Codex (gpt-6-astra, high). The other judge, and the second reader in the search for earlier work: Claude Sonnet.
- Human: direction of the work and the decision to publish. **No human compared the images with the transcriptions or the reading.** Agreement between AIs does not replace a human check.

## 9. Limits
- The plaintexts survived as the contemporary fair copy and teleprinter message. What was recovered is the key and the correspondence, not a previously unknown text.
- The plaintext of parts 3-4 of frame 0993 was fixed with the fair copy in view. The checks on the keys are that parts 1-2 and frames 1025-1027 decrypt.
- The second transcription was run once per part.
- The cause of the seven wrong letters (`docs/READING.en.md`) cannot be established.
- Only the two messages of 17 May 1940 were read.

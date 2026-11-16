# Francia 346: a full decode with the published key

The letters that this folder decodes are cipher letters of 1632 to 1634 from Rome to Francesco Adriano Ceva, extraordinary nuncio in France. Their clear endorsements name Cardinal Barberini. This folder decodes the digit pages of the DECODE records of Francia 346 with the published key: "read with the known key".

The transcription is a machine transcription of the DECODE images, made in my pipeline. Nobody verified it. Every number here is real.

## The whole file at a glance

DECODE holds 73 records of Francia 346 (260 scans).

| Records | How many | State | Where |
| --- | ---: | --- | --- |
| R5626, R5635 to R5637, R5640, R5642, R5643, R5645 to R5659: the first 22 digit records | 22 | read with the known key; a summary and a reading for each | the sections below; `r5626.md` to `r5659.md` |
| R5627 to R5633, R5641, R5644 | 9 | read with the known key (R5641 is too small to judge); each carries a decipherment of the time | [our repository](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full) |
| R74 to R78, the earlier leaves | 5 | read with the known key from my pilot transcription; R74 to R76 in fragments | [our repository](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full) |
| R5660 to R5666, R5669 to R5671 | 10 | do not read with the known key: another cipher; content from the clerk's decipherment or a clear copy; no decode | [our repository](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full) |
| R5634, R5638, R5639 | 3 | do not read with the known key: another cipher; each carries a decipherment of the time; a blind read is in progress | [our repository](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full) |
| R5667, R5668, R5672 to R5686 | 17 | other signs; a blind fit is in progress | [The other records](#the-other-records-of-the-file) |
| R79 to R84 | 6 | my pipeline has no transcription yet | the same section |
| R5625 | 1 | a letter in clear | the same section |

Ten pages that read badly were read again. [`rereads.md`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-346-full/rereads.md) in our repository gives their decode.

## What came first

The order of events is part of the result.

1. **A key from the ciphertext alone.** My algorithm found a key from 13 records of this file, without the published key. I fixed it at 01:27 on 12 November 2026 (UTC−3). [`francia-346-leaves/`](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-leaves) in our repository has that read and its check.
   - Those 13 records include an earlier transcription of 8 records here: R5626, R5635, R5636, R5637, R5640, R5643, R5647 and R5648.
   - The other 14 records here were not in that fit.
2. **A read of the new pages, frozen.** I applied that key to the 22 records here, with no new fit. I fixed that read at 17:00 the same day.
3. **The published key, then.** After that, I opened the published key. I graded the frozen read against it and made the full decode.

## The numbers

**The frozen read** (`check.md`): of the true letters that it shows, 98.8% are right (6,930 of 7,017). All 87 wrong letters are code 07, which is h. But only 62.0% of its graded shown tokens are letter codes (7,017 of 11,324). The rest are syllables, nulls or false pairs of my cut.

On the 8 records inside the key's fit, 99.0% of the shown true letters are right (3,091 of 3,122). On the 14 records outside it, 98.6% are right (3,839 of 3,895).

**The full decode, first pass:** 10,919 code tokens, of which 92.3% had a value (10,081). Three-digit codes: 351 tokens had a value from the ledger, and 803 had none. **Second pass (graded):** the pages now give 515 three-digit tokens a value: 142 certain, 131 probable, 242 conjecture. 639 stay open. So 10,245 code tokens (93.8%) show a value. The table of the first pass below keeps its first-pass figures.

| Record | Key-free check | Code tokens | With a value | Three-digit, ledger value | Three-digit, no value | Bits per letter |
| --- | --- | ---: | --- | ---: | ---: | ---: |
| [R5626](r5626.md) | fits | 682 | 93.7% (639) | 15 | 43 | 4.90 |
| [R5635](r5635.md) | fits | 410 | 94.6% (388) | 16 | 21 | 4.58 |
| [R5636](r5636.md) | fits | 1,104 | 94.6% (1,044) | 45 | 57 | 4.25 |
| [R5637](r5637.md) | fits | 832 | 92.7% (771) | 24 | 59 | 4.43 |
| [R5640](r5640.md) | fits | 652 | 93.6% (610) | 21 | 42 | 4.74 |
| [R5642](r5642.md) | differs | 586 | 82.9% (486) | 15 | 91 | 5.77 |
| [R5643](r5643.md) | fits | 38 | 84.2% (32) | 2 | 6 | 5.54 |
| [R5645](r5645.md) | differs | 198 | 93.9% (186) | 3 | 12 | 4.62 |
| [R5646](r5646.md) | fits | 818 | 92.1% (753) | 26 | 65 | 4.52 |
| [R5647](r5647.md) | fits | 60 | 90.0% (54) | 3 | 6 | 4.58 |
| [R5648](r5648.md) | fits | 855 | 92.6% (792) | 33 | 60 | 4.63 |
| [R5649](r5649.md) | differs | 376 | 91.8% (345) | 11 | 27 | 4.59 |
| [R5650](r5650.md) | fits | 739 | 94.0% (695) | 30 | 44 | 4.48 |
| [R5651](r5651.md) | differs | 1,042 | 91.9% (958) | 36 | 84 | 4.49 |
| [R5652](r5652.md) | differs | 586 | 91.3% (535) | 7 | 51 | 4.54 |
| [R5653](r5653.md) | fits | 162 | 95.7% (155) | 2 | 7 | 4.51 |
| [R5654](r5654.md) | differs | 205 | 93.2% (191) | 6 | 13 | 4.46 |
| [R5655](r5655.md) | fits | 573 | 93.9% (538) | 24 | 31 | 4.24 |
| [R5656](r5656.md) | too small | 325 | 89.8% (292) | 10 | 33 | 5.29 |
| [R5657](r5657.md) | too small | 546 | 91.4% (499) | 18 | 44 | 5.57 |
| [R5658](r5658.md) | too small | 107 | 90.7% (97) | 3 | 5 | 4.76 |
| [R5659](r5659.md) | too small | 23 | 91.3% (21) | 1 | 2 | 5.64 |

- **Code tokens** are the two- and three-digit codes, without word spaces and nulls. **With a value** counts letters, syllables and the three-digit codes that have a ledger value.
- **Bits per letter** measure how Italian the decoded letters look, under a letter model of 17th- and 18th-century Italian prose. Lower is more Italian. The same letters in a shuffled order give 9.4 on average.
- **The key-free check** compared the code counts of each record with those of the earlier letters, before I opened the key. "Too small" means that no page of the record passed its page test with read digits.
- **A check against the decipherment leaves** of three records: 58% to 79% of the decoded letters align with equal letters of the leaf. Other leaves give 32% to 49%. `check.md`, section 7, gives the method and its limits.

## The grades of the code values (second pass)

A second pass graded every value of a three-digit code. It took no new value from outside the ledger: the test below gave no other source a measured accuracy. All numbers are real.

| Grade | Codes | Tokens | Source |
| --- | ---: | ---: | --- |
| certain | 14 | 142 | values that the ledger adopted, with no whole-word doubt in these letters: 498 tanto, 854 guerra, 149 piazza, 315 S.E., 988 negotio, 338 stato, 441 bene, 857 Germania, 334 Sueco, 454 grandi, 488 quale, 541 armi, 473 mentre, 491 quell- |
| probable | 7 | 131 | values that the ledger adopted, with a doubt at whole-word places in one record: 411 V.S., 439 ancora, 481 però, 493 questa, 495 quanto, 830 Francia, 938 Monsieur |
| conjecture | 25 | 242 | 6 values that the ledger adopted but that these letters put in doubt in two or more records (470 hor, 127 Imperiali, 104 Olandesi, 171 regno, 474 mente, 497 tutt-), and 19 values that the ledger read off the decipherments of 1632 (ff. 82r and 136r) but did not adopt |
| open | — | 639 | no value |

- **A doubt** is a place where the earlier reading of a record marks the ledger's word as not fitting.
- **The ledger's unadopted values** come from its readings of R75 and R84: 153 pace, 451 fatto, 471 molto, 485 perché, 110 Principe, 998 nella, 357 Schomberg, 581 Card. Richelieu, 197 Religione Cattolica, 844 Gostavo, 309 and 107 S.M.tà, 930 Mons.r, 957 Nuntio, 380 trattato, 831 Francesi, 397 Valtellina, 170 Re, 445 tanto.
- **The test.** Each ledger value was hidden in turn, and three sources tried to find it again:
  - the decipherments of the time in seven records, aligned with the decode under strict rules: no place passed the rules, so they gave no value;
  - a word-level score in context: it found 0 of 21 values;
  - two readers who saw only the contexts: they found 5 and 1 of 21.
- So no new value reaches "probable". The pages show no value from those three sources.
- **Shown and not shown:** a further 69 conjectures (252 tokens) from the word-level score and the readers stay in the internal table, because the test gave those sources no measured accuracy. The counts on these pages count the shown values only.
- **Unchanged:** the cut and the letters of the decode.

## The six records that differ

The key-free check found that six records differ a little in their code counts: R5642, R5645, R5649, R5651, R5652 and R5654.

- **Five of them read as Italian under the published key.** Their bits per letter lie between 4.46 and 4.62. The twelve that fit give 4.52 (the mean weighted by letters).
- **R5642 does not read** (5.77). Its main page, f. 246r, carries a tentative reading in the source. The page has a high share of 6 and a low share of 8, so I suspect that the transcription reads some 8s as 6. Its last four rows read in part.
- So the published key reads five of the six. For R5642, this test cannot show whether another key was used.

## What the letters say

The readings are partial. Each record page gives the Italian, the English and the place of each name.

- **The peace talks of 1633.** Rome urges the nuncio to keep the talks going and not to "break the thread" (R5648, R5651). It names plenipotentiaries (R5635, R5636) and a universal [?peace] (R5640, R5650). R5655 names something "in luogo terzo" (in a third place) and a suspension of arms.
- **Benavides.** The name recurs in nine records, often with a writing and Rome's view of how to answer it (R5637, R5640, R5645, R5646, R5650, R5651, R5652, R5653, R5654).
- **Lorraine.** Rome names the fortresses of Lorraine (R5636) and "the invasion of Lorraine" (R5653). It hears of the events in Lorraine "con disgusto", with displeasure (R5654, R5655).
- **Germany and the Swedes.** A rumour of a fortress on this side of the [?Rhine] held by the "Svezesi", probably the Swedes (R5636); aid to a people (code 104) under old alliances (R5651); a violated neutrality and the Imperial court (R5655).
- **Church affairs.** A priory, offers of pensions (R5636, R5637), and the bull "de non infeudandis": the letter says that it also covers exchanges, and it names censures (R5649).
- **A woman who is ill.** Rome hopes that she will be reconciled with a "f…uolo", perhaps her son, and return (R5646, R5648). The decode does not name her.

## The other records in our repository

Our repository also decodes nine records that carry a decipherment of the time (R5627 to R5633, R5641 and R5644) and the earlier leaves R74 to R78. It also describes thirteen records in another cipher. This folder does not hold those pages. See [`francia-346-full/`](https://github.com/prabal-rje/branicki-1757/tree/main/francia-346-full).

## The key

- **The published key** gives 61 pair codes: 40 letter codes for 19 letters, and 21 syllable codes such as che, per and di. George Lasry reconstructed it, and it stands on DECODE with a key note of 24 October 2020.
- **The form of the cipher,** as the ledger rebuilt it from Lasry's own readings: a lone 6 is a word space, and the ten pairs 2x are nulls.
- **The published key gives no three-digit code a value.**
- **The cipher ledger** at https://github.com/dbourdeau/cyphersolver gives values to three-digit codes.
  - Its file `targets/ceva1632/cipher.py` gives 23 values.
  - Its notes on a re-read of 22 to 23 October 2026 (`targets/ceva1632/NOTES.md`) add five values and change one: 104 is Olandesi, not Svedesi.
  - The same notes change two pairs: 88 is del, not quel, and 33 is gli.
  - The first pass used these 28 three-digit values and the two pairs. The second pass grades 27 of them (129 regno is withdrawn by the ledger) and adds 19 values that the ledger read but did not adopt, as conjectures (see "The grades of the code values").
- **Some ledger values do not fit these letters.** For example, code 470 ("hor") stands where no "hor" can stand. Each record page lists such places, and the reading marks them `[?word]`.

## How to read the decode

Each record page ends with the decode, row by row, as the key gives it.

| Mark | Meaning |
| --- | --- |
| a space | the word space, a lone 6 |
| `abc` | letters and syllables of the key; the code for u and v is written u |
| `{word}` | a three-digit code with a **certain** value: a value that the ledger adopted, with no whole-word doubt in these letters |
| `{~word}` | a three-digit code with a **probable** value: a value that the ledger adopted, with a doubt at one place in one record |
| `[123 ?word]` | a three-digit code with a **conjecture**: a value that the ledger questioned or read off one decipherment of 1632 but did not adopt |
| `[123]` | a three-digit code with no value |
| `⟨a⟩` | a code that holds a doubtful digit of the transcription |
| `{word?}`, `{~word?}`, `[123?]` | a three-digit code that holds a doubtful digit; the value or the code as before |
| `·` | a code that holds an unread sign, or a lone digit that fits no code |
| `[…]` | an unread span of the transcription |
| `‖` | clear text stood here; this page does not copy it |

The cipher writes no double letters, so "sarebe" stands for "sarebbe". The readings mostly keep this spelling. In the readings, `[abc]` is supplied or changed by me, `[?word]` is a doubtful word, and `[…]` does not read. Where a silent repair remains, the decode line is the reference.

## Who read these letters before

- **Decipherment leaves.** Some records hold a decipherment in Italian on another leaf: R5626 (f. 155r), R5637 (f. 212v) and R5646 (f. 269r). Brice Dudout's notes in the ledger (29 October 2026) call such leaves contemporary. They add R5655 (f. 324) and find none in R5640. So some of these letters were read before.
- **Copies in clear** may also exist in other volumes. This folder does not copy the decipherment leaves, and it takes no code value from the decipherment leaves of these 22 records. The conjectures that it shows come from the ledger's readings of two 1632 decipherments in other records (ff. 82r and 136r).
- **DECODE.** On 12 November 2026, the public record pages of R5625 to R5659 all give the status "N/A" and the cipher type "Unknown". The word "Decryption" stands on each page, but its documents need a login, so I could not check them.
- **The cipher ledger.** Its entry 880 lists R5625 to R5686 as "N/A" with no decipherment filed, and says that none of them is in the repository. Its notes of 29 October 2026 name R5626, R5640 and R5655 in a sample, and say which leaves hold decipherments. They decode R5630 (now in our repository), and none of the first 22 records. I checked the live catalogue and notes on 12 November 2026.
- **Print.** I found no edition of these letters. A. Iommelli's study of Ceva (Fondazione 1563, 2022) cites his own deciphered despatches, "Francia, 78", and Bichi's letters from Paris. In the first pass I found no citation of Francia 346 in it; the second pass did not check this again.

**No modern decipherment of these 22 records shows on DECODE's public record pages or is on file at the ledger.** This does not mean that nobody read them: the decipherment leaves show that some were read long ago.

**A book of 1920.** A. Leman (1920) used the Barberini library's minutes of the cipher despatches to Ceva. So clear drafts of letters of this series were in use in print in 1920. I did not check which letters those minutes hold.

## Limits

- **The transcription** is a machine transcription. Nobody verified it against the images. A misread digit gives a wrong letter or a broken cut.
- **The cut** of the decode into two- and three-digit codes comes from a search with an Italian letter model. Where it picks a three-digit code, the letters around it can be wrong.
- **The readings** are mine. They supply words where the context allows, and they mark each supply. Many rows do not read.
- **639 three-digit tokens** stay open after the second pass (803 after the first). They hide names and words that the published key does not give.
- **Three records give almost nothing:** R5643, R5658 and R5659. Most of their cipher rows are unread in the source.
- **Four pages in three records do not read:** R5642 f. 246r, R5656 f. 337r and R5657 ff. 342r–v. On all four, 8 is rare and 6 is common, so the transcription may read some 8s as 6. A declared correction of misread digits failed its own check on a page that reads. My pipeline read these pages and those of R5643, R5658 and R5659 again; [`rereads.md`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-346-full/rereads.md) in our repository decodes the newer transcription.

## The other records of the file

- **R5625** is a letter in clear. It holds no cipher. DECODE catalogues 9 pages but shows 2 scans.
- **17 records use other signs:** R5667, R5668 and R5672 to R5686. A test before the key found another system. Their pages name Madrid and Vienna. They stay open.
- **R79 to R84** have no transcription of my pipeline yet. DECODE holds its own transcription of them, and marks them "Decrypted" or "Partially decrypted". R83 uses another system.
- **Francia 32** is another file (1590 to 1592) in another cipher. See [`francia-32/README.md`](https://github.com/prabal-rje/branicki-1757/blob/main/francia-32/README.md) in our repository.

## Credits

- **DECODE**, the database of historical ciphers of the DECRYPT project: records R5626, R5635 to R5637, R5640, R5642, R5643 and R5645 to R5659. https://de-crypt.org/decrypt-web/RecordsList
- **The archive:** Archivio Apostolico Vaticano, Segreteria di Stato, Francia 346.
- **The key:** George Lasry, Beáta Megyesi and Nils Kopal (2020). The ledger's values for three-digit codes and two pairs: the cipher ledger at https://github.com/dbourdeau/cyphersolver.

DECODE's images are for research use only. They may not be redistributed or published without permission from the archive. No DECODE image is in this folder. The digit rows of my own transcription are in `transcription/`, one file for each cipher page. Each decode line gives its record, folio and row.

## Files

- `NOTES.md` and `profile.json`: the notes and the profile of this target
- `check.md`: the grade of the frozen read against the published key, and the checks of 13 November
- `r5626.md` to `r5659.md`: one page for each of the first 22 records, with the reading, the translation, the names and the decode row by row
- `key-and-key-free-read/`: the key table of the decode, and the frozen key-free read with its key
- `TRANSCRIPTION.md`: what the transcription is, its known challenges, its marks and its counts
- `transcription/`: the digit rows, one file for each of the 35 cipher pages

# The open frames of catalogue 681, transcribed twice blind and tested with the known keys (15 Nov 2026)

Andrew Beling, with AI agents (Claude, Opus). Every image reading here is by AI readers; no person has checked it.
No reading review grade is recorded in this folder or for the new documents: that grade is the reviewers'.

## What was done

Fifteen NARA frames (vol. 196 fr. 0053, 0056, 0061, 0064, 0065, 0071; vol. 11 fr. 0039, 0044, 0045, 0046, 0078-0081;
vol. 10 fr. 0056) were fetched from the National Archives catalog on 15 Nov 2026 (public; the frame 0045 file has the
sha256 in `../source_audit_2026-11-12/SOURCES.json`). Four readers transcribed the cipher groups from the images, each
alone, with no earlier transcription, key or decryption in sight and told not to decrypt
(`TRANSCRIPTION_PROTOCOL.md`): A1 and A2 for vol. 196, B1 and B2 for vols. 11 and 10. Each began with a seed telegram
whose transcription is established (`seed_check_result.json`, pass mark 90% of letters): A1 176/180, A2 166/180,
B1 60/61, B2 57/61; all passed.

Then a test plan was written and frozen before any key was applied (`TEST_PLAN.md`; sha256 1f5eaadc...8c97, and the
four transcriptions' hashes below): every telegram, each reader's preferred letters separately, the four known keys
(COMPLETE VICTORY, COME RETRIBUTION, MANCHESTER BLUFF, THE NAVY OUR PRIDE) at all 15 starting positions, scored by
quadgrams from the Official Records OCR (OR I/49/2); a second model allows one slip (two phases of the same key, split
at a group boundary). Controls under the same maximisation: 200 shuffles of the telegram's own letters (maximised over
all four keys and 15 positions, so the search over four keys is allowed for) and 200 random 15-letter keys. Pass = above
the highest of all 400 controls; a telegram yields when both readers pass with the same key.

## Agreement of the blind readers (`transcriptions/blind_agreement.txt`)

| telegram | frame | groups A/B | letters agreeing |
|---|---|---|---|
| T01 8 Mar, to D. W. Adams | v196 0053 | 33/32 | 151/165 (0.915) |
| T02 9 Mar, to D. W. Adams | v196 0056 upper | 32/32 | 133/140 (0.950) |
| T03 9 Mar, to Lt Col W. M. Levy | v196 0056 lower | 23/23 | 101/109 (0.927) |
| T04 13 Mar, to the Secretary of War | v196 0064 | 14/14 | 71/72 (0.986) |
| T05 13 or 14 Mar, to Maury | v196 0065 | 19/19 | 87/87 (1.000) |
| T06 17 Mar, to Taylor at Selma | v196 0071 | 15/15 | 74/79 (0.937) |
| T07 10 Apr, to Taylor | v11 0044 first | 16/16 | 69/71 (0.972) |
| T08 10 Apr, to Maury (read and printed) | v11 0044 second | 20/20 | 72/78 (0.923) |
| T09 10 Apr, to Maury | v11 0045 lower | 15/15 | 56/57 (0.982) |
| T10 11 Apr, to Maury, flowing capitals | v11 0046 upper | 21/22 | 60/94 (0.638) |
| T11 11 Apr, to Maury, second | v11 0046 lower | 25/25 | 102/107 (0.953) |
| T12 18 Jan, to President Davis | v10 0056 | 51/51 | 254/258 (0.984) |

All twelve: 1230/1317 letters (0.934). T03 counts XS|UMGM and ELWDA|VBBX as four groups; they are two words.

**Independent check of T03 and T10 (verifier, `verifier/`).** A verifier who had not opened this work transcribed both
telegrams from the images, and a second helper who had seen nothing did the same; both froze their files (sha256
066a900c... and 71631780...) before either was compared or decrypted. T03: 107 of 109 letters agree (the two differ
only on the clerk's L/Z), 19 of 21 words identical. T10: 67 of 91 letters, 8 of 21 groups identical, so this hand
stays the weak point. The verifier decrypted his own transcription with every known key at every position and got the
same plain text of T03 word for word, and the same words of T10.

## Results (`test_results_table.md`, `test_results.json`)

- Positive controls S1 (12 Mar), S2 (8 Apr) and T08 pass with COME RETRIBUTION for both readers.
- **Yield (both readers, same key):** T01 COMPLETE VICTORY; T02 COME RETRIBUTION; T03 COMPLETE VICTORY; T04, T05, T06
  COME RETRIBUTION; T07 COME RETRIBUTION from position 3; T09 COME RETRIBUTION; T10 COME RETRIBUTION (narrow for B2:
  -7.046 against a control maximum of -7.120); T12 COMPLETE VICTORY from position 1.
- **Miss: T11**, the second telegram of 11 April on fr. 0046. No known key passes at any position under either model,
  for both readers (best -7.56 and -7.47 against control maxima -7.19 and -7.35), although the two readers agree on
  0.953 of its letters. bdpayne's tests of November had failed on it as well. Its letters have an index of
  coincidence of 0.043-0.045 (a polyalphabetic cipher, not a transposition of English), and the columns at period 15
  are the most uneven of periods 1-20 for both readers (with about seven letters a column, a weak sign only): a
  15-letter key not among the four, or one of them under another convention, is the likeliest; not worked further.
- Re-run on 15 Nov by the verifier with `run_test.py` (paths made relative, nothing else changed): every score,
  control maximum and pass is identical.
- With twelve telegrams and two models, a pass at 1 in 200 per reader could happen by chance about once in eight
  tests of this size for one reader; the yield needs both readers and, for the readings, the words themselves. The
  margins are wide everywhere except T10, whose reading rests on its eight decrypted words at the end.

Run: `python run_test.py <OR I/49/2 OCR text> [out.json]` (the OCR file is fetched from the Internet Archive; its URL and
sha256 are in the script).

## Readings (`reading_tables.md`, `word_counts.md`)

New, written up as documents in the target folder:

- **T03, 9 March 1865, to Levy** (`../v196-0056-levy_*`): read with COMPLETE VICTORY from position 0. 155 cars on the
  Mobile and Montgomery road to be "transferred on trucks to wide guage at Columbus, Ga.", "under pretense of assisting
  roads in Georgia". 21 cipher words, 20 read; GUAGE needs I for J twice (the image shows the clerk's J form twice:
  a correction against the image, counted as a hole).
- **T10, 11 April 1865, to Maury** (`../v11-0046a-maury_*`): read in part with COME RETRIBUTION. "One [?of] the
  [?trains] from Mobile last night brought [... 9] and quite a number of bales of cotton for the rail road company."
  21 cipher words: 10 read, 2 need one letter no reader saw (OF, TRAINS), 9 unread. RAIL needs two letters that are
  readers' marked alternatives (image-supported), not corrections.

Confirmations and proposed improvements of earlier provisional readings (not applied to the earlier reading files;
the word-by-word tables are in `reading_tables.md`; the verifier checked T03 and T10 only on the image):

- T01 and T02 (8 and 9 Mar, to D. W. Adams; bdpayne, PR #388): confirmed with the same keys and phases; in T01 the
  STEAMBOATS group has one letter too many as bdpayne found, and TLGAIIOKGS still does not read; in T02 the blotted
  first letter of the tenth group stays outside the key stream, as bdpayne's cancelled-R hypothesis has it.
- T04, T05, T06 (13, 13/14, 17 Mar; bdpayne, #388): confirmed; T04 has five words that need one letter each, T06's
  last group is still one letter short.
- T07 (10 Apr, fr. 0044 first passage; bdpayne): SENDING at position 0, the rest at position 3 (three key places
  missing after the first group).
- T09 (10 Apr, fr. 0045; bdpayne, #577, #660): both blind readers read EIEX (SENT) and MF (TO); the ending would give
  STORES ALSO with three one-letter changes, so it stays unread here.
- T12 (18 Jan, to Davis; bdpayne, source audit of #577): most of its 15 bracketed words read on both blind
  transcriptions; FMNA gives MISS; seven words need a one-letter change.

Bryan Payne's provisional readings of #388 (and earlier) are confirmed in substance by two blind transcriptions for
T01, T02, T04, T05, T06, T07, T09 and T12; the readings are his.

## The catalogue's open list (entry 681), as of 15 Nov 2026

- Read now in a document of this folder: vol. 196 fr. 0053, 0056 (both telegrams), 0064, 0065, 0071 (provisional
  readings of #388, confirmed above); vol. 11 fr. 0044 (both), 0045 (lower telegram read except its last three
  groups); vol. 10 fr. 0056.
- Frames 0078-0081 of vol. 11 hold no cipher: 0078-0080 are clear telegrams of 20-22 April 1865 and 0081 is the back
  cover (seen on the images by two AI readers).
- Still open: fr. 0046 lower telegram (T11, fails every known key); fr. 0046 upper telegram, nine middle words (T10);
  fr. 0045 ending (EX FVWJ JMNH); fr. 0053 group TLGAIIOKGS; fr. 0071 last group.

## Files

- `TRANSCRIPTION_PROTOCOL.md`, `TEST_PLAN.md`, `seed_check_result.json`
- `transcriptions/`: the four readers' transcriptions (one group a row, `[X/Y]` doubtful), their lists of confusable
  letters, `blind_agreement.txt`
- `test_results_table.md`, `test_results.json`, `run_test.py`; `agreement_with_earlier_transcriptions.txt` (made after
  the test: the blind readings against the earlier `<doc>_cipher.txt` files, 0.84 to 0.95)
- `reading_tables.md`, `word_counts.md`: group by group, each reader's letters and plain text, and word status
- `verifier/`: the verifier's and the helper's blind transcriptions of T03 and T10

Frozen before the test (sha256): `TEST_PLAN.md` 1f5eaadc0fc160e8a609cc306e628e8b4942facfd95f7df356a3e590b0b38c97;
`transcriptions/readerA1_transcription.tsv` 7b64b054a51b76fd5285f0f17430a05fdc36ecfe1116fdc327722b4cdf39960e;
`readerA2` e6f1d6d492d93ef3b7cac11b4ac222fb08050a05d175d76626251eae590eb9b9;
`readerB1` 48909b6aa8f1b17fb359782021a43dd7d7a73dd49066305303dc1a0e5e17e164;
`readerB2` 25187d1a46d60650a8e2a573732b17b841a513b58769292966e243098a5594f9.

Status: read (Brice Dudout, 12 Nov 2026; vol. 196 fr. 0030, 21 Feb 1865 to Maury, 29 of 29 cipher words, and fr. 0031-0032, 21 Feb 1865 to D. W. Adams, 44 of 44 cipher words, read in their sense; Daniel Bourdeau's 95% rule).

# Catalogue 681: two telegrams of 21 February 1865 from the open list, read (vol. 196 fr. 0030 and 0031-0032)

The catalogue's folio_note lists vol. 196 fr. 0030 and 0032 among the open telegrams, and no file in this folder treats
them. Both are read here with the known keys, under the conventions WAINUT and Bryan Payne established in this folder
(Vigenere over the cipher letters only, key from position 0 at each telegram's first cipher letter).

| doc | frame, MS page | date | to | key | cipher words / letters | letters direct | prior print |
|---|---|---|---|---|---|---|---|
| v196-0030-maury | vol. 196 fr. 0030, p. 55 | 21 Feb 1865 | Maj. Gen. D. H. Maury, Mobile | COME RETRIBUTION | 29 / 156 | 141 | none found |
| v196-0032-dw | vol. 196 fr. 0031 p. 57 (clear) and fr. 0032 p. 58 | 21 Feb 1865 | Brig. Gen. D. W. Adams, Selma or Montevallo | COMPLETE VICTORY | 44 / 206 | 195 | OR I/49/1 p. 1003, cipher passage omitted ("* * *") |

Images: NARA naId 45485022, `chapter-2-volume-196-0030.jpg`, `-0031.jpg`, `-0032.jpg` under
https://catalog.archives.gov/medialive/22/4850/45485022/content/dc-metro/rg-109/596501-confederate-record-books/chapter-02-volume-196/
(public domain; not copied here). SHA-256 of the files as downloaded 12 Nov 2026: 0030 ff808d51…6d81, 0031 d9d361c6…8729, 0032 6fb233a2…cf.

## Readings

- **To Maury, 21 Feb.** Latest information indicates that the enemy has gone down the river from Vicksburg without avowed
  intention OF ATTACKING MOBILE. It is now of the highest importance to develop what the enemy is DOING AT PENSACOLA. If
  you can't otherwise ascertain with certainty, you must have [a] FORCED RECONNAISANCE MADE AT ONCE ... If there no longer
  exists probability of the enemy attacking from DIRECTION OF PENSACOLA, most of the CAVALRY YOU NOW HAVE ON EASTERN SHORE
  should be placed on SELMA AND MONTGOMERY LINE to repel anticipated movement AGAINST CENTRAL ALABAMA.
  (`v196-0030-maury_reading.md`)
- **To D. W. Adams, 21 Feb.** All public stores and property IN NORTH ALA LIKELY TO FALL INTO ENEMY'S HANDS IN CASE OF
  MOVEMENT FROM TENNE[SSEE] RIVER should either be placed IN FORTIFIED PLACES OR SOUTH OF ALA RIVER. You must without
  awaiting further orders send CAHABA PRISONERS TO ANDERSONVILLE immediately on first receipt of accurate information of
  ENEMY'S ADVANCE TOWARDS CENTRAL ALA. IF GOVT EMPLOYEES AT DEMOPOLIS have not already been organized and drilled for local
  defense, send competent officers ... This can be done without DEPRIVING WORKSHOPS of any great part of their labor.
  (`v196-0032-dw_reading.md`)

Line by line: `<doc>_decryption.txt`; every word with its key letters, the expected cipher and the glyph corrections:
`alignment.tsv` (`python3 align.py` rebuilds and checks it).

## Method and order of work (frozen by SHA-256)

1. Blind transcription of the cipher words from the images, before any key was tried:
   `blind_transcription_frozen.txt` (sha256 `10984ebe1ae35be8f67185555b3a02d195881a4c65df1fb6a0b770e2cd330efb`; French
   comment lines; ambiguous glyphs written [X|Y], first option used).
2. Pre-registration, before any key was tried on these telegrams: `prereg_fr.md` (sha256 `0edd646d…c501`) and its
   measure script `prereg_measure.py` (sha256 `ce88b0cc…2002`). Closed key list: COME RETRIBUTION, COMPLETE VICTORY,
   MANCHESTER BLUFF, THE NAVY OUR PRIDE, OUR NAVY OUR PRIDE. Single measure: mean log10 English letter probability of the
   decryption, offset 0 per telegram, letters as read with no correction, against 200 random 15-letter keys (seed 681).
   A key fits if it beats all 200. The keys are fixed phrases, not fitted, so all 362 letters are held out.
3. Results (`measure_results.json`):

| | letters | COME RETRIBUTION | COMPLETE VICTORY | MANCHESTER BLUFF | THE NAVY OUR PRIDE | OUR NAVY OUR PRIDE | 200 controls max / median |
|---|---|---|---|---|---|---|---|
| fr. 0032, to D. W. Adams | 206 | -1.540 (rank 1) | **-1.296 (rank 1)** | -1.594 (4) | -1.713 (145) | -1.711 (145) | -1.558 / -1.685 |
| fr. 0030, to Maury | 156 | -1.572 (10) | -1.622 (34) | -1.768 (183) | -1.722 (150) | -1.677 (89) | -1.517 / -1.684 |
| both | 362 | -1.554 (1) | -1.436 (1) | -1.669 (77) | -1.717 (160) | -1.696 (122) | -1.589 / -1.682 |

   COMPLETE VICTORY is the pre-registered winner for the D. W. Adams telegram (English text is about -1.25; COME
   RETRIBUTION also passes there only through the key letters it shares with COMPLETE VICTORY, as noted in NOTES.md).
   **The Maury telegram fails the pre-registered test at offset 0.** Read word by word, COME RETRIBUTION at offset 0 gives
   its first six words (OF ATTACKING MOBILE DOING AT PENSACOLA), and from the seventh word to the end the key runs one
   place ahead: one key letter was skipped, or a one-letter cipher word (the "a" of "a forced reconnaissance") was not
   copied. This break was found after the test, so its check is post hoc (`posthoc_T1_break.py`): with one break and free
   offsets allowed to every key, COME RETRIBUTION scores -1.271 against 200 random keys at most -1.463 (COMPLETE VICTORY
   -1.4625, through shared letters). We report the Maury reading as read, with this caveat stated.
4. Count by the 95% rule: each cipher word read gives an English word that makes sense in the sentence; the corrections
   are one glyph per place, of the kinds already listed in NOTES.md for this clerk (barred E for F, W for U, Y for V, J
   for I, ...): 26 places in 362 letters.

## Prior work and print

- This folder: WAINUT (27 Oct), and Bryan Payne with OpenAI Codex (PRs #186, #205, #388) established the keys, the
  per-telegram convention, the glyph confusions and the key chronology (orders of 9 March to change to COME RETRIBUTION;
  COMPLETE VICTORY to Wirt Adams on 21 Feb, fr. 0031 p. 56). Neither frame read here appears in their files.
- Official Records, Ser. I vol. 49 pt. 1 (archive.org `warofrebellion014901rootrich`, OCR searched 12 Nov 2026): prints the
  D. W. Adams telegram on p. 1003 without its cipher part; no 21 Feb telegram to Maury, and none of "doing at Pensacola",
  "real condition of affairs", "repel anticipated", "Cahaba prisoners", "depriving workshops". Pt. 2 and vol. 45 pt. 2
  searched for the same phrases: none. OR Ser. II vol. 8 (prisoners) could not be fetched (archive.org error); not checked.
- Web search (12 Nov 2026) on "Cahaba prisoners to Andersonville" and on the Maury phrases: no earlier decipherment found.
- No issue, PR or fork branch on catalogue 681 other than those above (checked 12 Nov 2026).

## Historical note

On the same day Taylor's headquarters used COME RETRIBUTION to Maury and COMPLETE VICTORY to D. W. Adams, which fits
Payne's recipient-specific chronology: the Mobile channel already on the new key (as Davis on 4 Feb and Beauregard on 10 Feb),
the Adams channels on the old one until the orders of 9 March. The Adams telegram orders the Union prisoners at Cahaba
sent to Andersonville at the first sign of an advance on Central Alabama, five weeks before Wilson's raid.

Work by Brice Dudout with Claude (Anthropic) agents: transcription from the images, pre-registration, measure and reading.

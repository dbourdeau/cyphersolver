# Biermann to Lindenow in Sweden, 1675: the Lindenow cipher of the Biermann copybook (Unsolved Catalogue no. 465)

Status: read in part. Key rebuilt on one letter from the clear letter beside it (no key sheet, no decipherment). Contributed by Tomáš Pavuk, working with OpenAI GPT-6 (Codex) and Claude (Anthropic); issue #679. Folder prepared 16 Nov 2026.

## What this folder is, and what it is not

`targets/biermann1675` holds the survey of Conrad Biermann's copybook of 1675 and the letters read with the image-55 key sheet (K55). Its notes list the French letters to Christopher Lindenow in Sweden as "key unknown, not attempted", and they record that the Lindenow letter of 22 February (image 71) runs nearly word for word with the clear letter to Meyercron of 20 February (images 67-70). That find is the project's, and the key here starts from it. Nothing here uses K55.

This folder is the separate entry for the Lindenow key (one key, one entry). It holds the four letters to Lindenow that the project's survey lists with cipher:

| Letter | Images | Groups | State |
| --- | --- | --- | --- |
| 11 January 1675 | 14 right, 15 left | 57 | decoded, not read |
| 18 January 1675 | 22 left | 14 | decoded, not read |
| 22 February 1675 | 71 left and right; ends in clear on 72 left | 196 | read in part |
| 12 April 1675 | 130 right, 131 left | 123 | decoded, not read |

Images: Rigsarkivet, Tyske Kancelli, Udenrigske Afdeling, Conrad Biermanns kopibog 1675 (Daisy heid 2130515, unit S-1418), `https://api.rigsarkivet.dk/ao/v1/images/<48573951+n>` for image n.

Only the letter of 22 February is claimed as a reading. The key was built on it. The other three are decoded here with that key as it stands, to show what it does and does not carry; they are not read.

## The system

A homophonic nomenclator in three layers, used together inside one word, with clear French around the cipher runs:

1. Letter signs, written as drawn shapes (named G01-G27 here; shapes described in `key.tsv`), and letter numbers below 30 (3 t, 4 m, 7 u, 8 q, 9 i, 10 l, 15 r, 19 s, 20 n, 22 z, 24 a, 26 y). Most letters have two or three forms.
2. Syllables in rows of five by vowel: 559-563 d, 717-720 l, 737-741 m, 891-895 r, 931-935 s, 960-964 t are the rows seen (717 la, 718 le, 719 li; 891 ra, 892 re, 894 ro; 961 te, 962 ti).
3. Words and stems by first letter: A 442-444, C 509-524, D 560-576, E 578, F 629, H 670, L 717-719, M 737-775, N 782, O 817, P 833-856, Q 870-880, R 891-894, S 931-950, T 961-979, V 985; names lower (277 Suede). Inside a letter the order is not strictly alphabetical (748 mesme before 749 ment).

The survey table in `targets/biermann1675/NOTES.md` gives 700-986 as the numbers of these letters. Over the four letters the numbers run wider: 437-986 for syllables and words, 185, 277, 291, 378 for names, and 3-96 for letters and a few other groups, beside the drawn signs.

`key.tsv` holds the 85 groups of the February letter: 83 with a value and two unread (607, G18). The column `evidence` says what each value rests on: `repeated` (48 groups, 159 of the 196 occurrences), `single, clear parallel` (7), `single, April fit` (4), `single, context` (23), `single, provisional` (880), `unread` (2). It is a part of a larger book: the other three letters hold 56 further groups with no value here.

## How the key was obtained

From plaintext beside the ciphertext. The clear letter to Meyercron of 20 February has, between *a presenté est* and *portant en substance*, the sentence *tout entier a l'avantage du Roy son Maistre sans qu'il y ayt la moindre realité pour sa Majesté*. The Lindenow letter has 32 groups between the same clear words. They read *tout e n ti e r a l avantage de la Suede sans qui l y a y t la mo i n d re re a li te pour sa Majeste*: the same sentence with *de la Suede* for *du Roy son Maistre*. An exact word-for-word alignment was tried first and failed; the two 892 groups in a row are both on the scan (moind-re re-alité). The values from this sentence were then carried through the other three runs of the letter, and the remaining values were fitted there from context.

This is not a ciphertext-only result, and the near-parallel was not found here.

## The count of record

By words, on `texts/1675-02-22_lindenow_reading.md`: the four cipher runs hold 84 words; one is unread and 29 are marked `[?word]`; 54 are plain: **0.643**, read in part. This is the project's own count on the first submission (issue #679: 54 of 84 with whole-word codes and single values read from context counted as holes; 72 of 84 by the contributor's twelve marks alone), reproduced word by word in `texts/1675-02-22_lindenow_marks.md`. The 29 are the 23 words with a value seen once and read from context, four whose single value is supported only by the fitted April reading (*que*, *avec*, *faire*, *malheur*), *les* in the provisional clause, and *mettent* for a disputed scan reading. The seven words whose single value rests on the clear parallel stay plain; with them the figure would be 47 of 84.

By groups: 194 of 196 have a value. This is assignment, not a reading rate.

## Checks made, and their limits

- **Transcription.** The 196 groups were read from the scan by an OpenAI GPT helper that did not have the key, and frozen; 14 corrections were then made against the scan and recorded (the main ones: 961 against 561 in two places, R01 group 10 = 20, R04 group 8 = 817, L07 group 1 = 894 partly hidden by a descender, the signs G26 and G27 kept apart from G14 and G03). Claude Fable 5.2 then read all 196 groups on the scan and found no difference; it had seen the transcription first, so this is a check, not a blind reading. No person has checked the scan.
- **G20 against G13.** *craindre* (L10 group 1), *peine d'y* (R04 group 4) and *plaindre* (R06 group 3) need d where a theta-like sign stands. The two signs stand side by side twice, at L09 group 12 / L10 group 1 and at R06 groups 2-3, and are drawn differently both times: G13 has a bar running through and beyond the oval, G20 is a closed oval with a short inner mark. Crops: `evidence/G20_vs_G13_L09-L10.jpg`, `evidence/G20_vs_G13_R06.jpg`.
- **Review.** Claude Fable 5.2 reviewed the contributor's solution on 15 Nov 2026 with the verdict "revise", accepting a partial reading only. Its nine findings are answered in the contributor's repository (linked under Files). The two that changed the edition: 30 single values had been labelled "supported", and the clause *les quartiers qu'ils ont presentement* rests on two single values (880 and 942).
- **Statistical validation** (`validation.tsv`, the repository's `docs/_validate.py`, model fr-1600-letters, 16 Nov 2026). On the 22 February letter, 194 read groups of 83 types: the reading scores -1.760; random keys of the same structure -3.191 (z 10.1); keys annealed onto the shuffled ciphertext -2.061 at best -2.048 (22 sd below the reading); the annealer on the real text from a random start reaches -1.978. Verdict: pass. It shows the text is not what fitting a key gives on shuffled groups; it does not confirm any single value, and the key was built on this letter.
- **April, first pass.** Before the April transcription was read, a candidate key was frozen and applied once: 61 of 93 groups had a value, with the runs *cette*, *conne*, *il ne les*, *mesler en se*, *issance*. That candidate had 24 = n; the key here has 24 = a (*qu'il y auroit*, *avoir*). So the first pass does not test this key. The frozen files are in the contributor's repository; their commit date does not prove when they were frozen.
- **January and April with the key as it stands** (`decode.py`, the `_decryption.txt` files). 11 January: 33 of 57 groups have a value; runs *de la mesme [743] que les*, *avec la Suede*. 18 January: 12 of 14; *la li s qui y e s [963] i t [693] i n te*. 12 April: 85 of 123; *cette*, *il ne les*, *mesler en se m u le*, *la mo u r*, *sa [781] i s sa n ce*, *la re c he r [5] he que*. These letters were transcribed and looked at during the work on the key (a search for recurring groups, some tentative readings), so they are not unseen material. No value in `key.tsv` is recorded as coming from them, but the record cannot certify that. They are a cross-letter check with that exposure, not a held-out test.

## Values the other letters suggest, not adopted

Listed so that the next reader does not have to find them again; none is in `key.tsv` and none is counted.

- The syllable rows predict 895 = ru and 964 = tu (11 January: *e n [895] p [964] re*, rupture), 963 = to (18 January *e s [963] i t*, 12 April *ne s [963] i t*: estoit) and 893 = ri.
- 12 April, fitted from context by the contributor: 442 avec (also February), 464 affaire (twice), 621 fa, 720 lo, 437 avoit, 862 point, 440 autre, 863 pas, 644 ga, 781 na, 96 on, 563 du, 784 no, 724 luy, 840 Princesse.
- 12 April line 8 gives *e n se m u le* where *ensemble* is wanted; 7 = u is firm in February (*l'augmenter*, *malheur*). Left as written.
- 12 April line 13 has 10 where *ses* wants s; 10 = l in February (*qu'il y auroit*). Left as written.
- 11 January line 4: 858 on the scan, where the first transcription had 856 (pour). *et le [858] de [185]* suits a title and a name.

## Errors of ours, found in review or in preparing this folder

- The first handover counted 189 occurrences as "supported"; 30 of them were single values. Corrected to the evidence classes in `key.tsv`.
- The key file first listed stems in D (deloge, detourne) for 607, which lies between 578 = et and 629 = faire. Corrected: E or F is likelier; the group stays unread.
- The candidate key frozen before the April letter had 24 = n. Corrected to a from the February letter itself.
- 11 January: 856 and 859 in the first transcription are 858 and 559 on the scan. 12 April: 13 is 15.
- The first translation rendered some single-value words without a mark. All 29 are now marked in the reading and the translation.

## Remaining gaps

- 607 and the sign G18, the verb of *les moyens qu'il y auroit de les en [607]* (22 February) - blocker: open-codes; one occurrence each, and neither recurs in the other three letters. A fifth letter in this key, or the draft, would fix them.
- The clause *et les quartiers qu'ils ont presentement* (22 February) - blocker: open-codes; 880 and 942 occur once each in the letter and were read together from context; 942 recurs on 12 April inside a run that is not read.
- The 25 other words marked `[?word]` in the reading - blocker: open-codes; each holds one value seen once in this letter, or (*mettent*) rests on a disputed sign. The other letters are too little read to confirm them.
- 11 January, 18 January and 12 April, decoded with the key as it stands and not read: 56 distinct groups with no value (64 occurrences) - blocker: open-codes; the key was built on one letter of 196 groups.
- The short quotation in clear after *ses propres mots* (22 February) - blocker: illegible; a few words, perhaps German, not read on the scan.
- The draft of the 22 February letter (TKUA Almindelig del 1 nr. 130, "Koncepter til Conrad Biermanns kopibog", Daisy unit 2951037) and Lindenow's own reports of 1675 (TKUA Speciel del Sverige, units 12924151 and 12928820) - blocker: needs-physical-access; listed as paper only, not seen. A draft in clear would settle every gap above.
- No original key for this family - blocker: no-key-material; the project's sweep of the key volume found none, and the sheet at images 307-309 was looked at again without a match.

## Escalation

- [x] siblings: the four letters to Lindenow that the copybook survey lists with cipher are all here; three are decoded with the key and not read. The neighbouring clear letters of 15 February and 1 March were read and carry no cipher.
- [x] clear-pages: the clear letter to Meyercron of 20 February (images 67-70) is the source of the key; the rest of it was read and gives no parallel for the military paragraph. No decipherment in the copybook.
- [x] known-keys: K55 does not read these letters. The project's sweep of TKUA Chiffer 1670-1709 found no sheet for this family (`targets/biermann1675/keyhunt.md`); images 307-309 were looked at again, 309 mirrored and contrast-raised, with no match (307 has 277 = Sielland, where the letters want Suede).
- [x] print: Vaupell, Rigskansler Grev Griffenfeld (1880-82), and Aarsberetninger fra det Kongelige Geheimearchiv VI searched; they print reports of Brahe of 22 February 1675 and a Lindenow report of October 1674, not this letter. Web and repository searches found no decipherment. Priority is not established.
- [x] key-rebuild: the key in `key.tsv` was rebuilt from the clear parallel and carried through the letter; its evidence classes are in the file.
- [x] retry: the key was applied again to the three other letters after the scan check of 16 Nov 2026 (`decode.py`); the counts are above.

## Files

- `key.tsv`: the 85 groups of the February letter with value, evidence class, count and places; two further signs seen only in the other letters.
- `decode.py`: applies `key.tsv` to every transcription in `texts/` and writes the decryptions; `--check` compares them with the files on disk.
- `texts/<date>_lindenow_transcription.txt`, `texts/<date>_lindenow_decryption.txt`: the four letters.
- `texts/1675-02-22_lindenow_reading.md`, `texts/1675-02-22_lindenow_translation.md`: the French reading with its marks, and the English translation.
- `texts/1675-02-22_lindenow_marks.md`: the count by words and, for each `[?word]`, the group it rests on and what the groups give.
- `evidence/`: the two crops for G20 against G13.
- The contributor's working files (the frozen first transcriptions, the correction ledger, the frozen April files, the review and the answer to it, a longer report): <https://github.com/JOPPA5/hcsolve/tree/5f070275e113cd32b675a3c5891b9d95e5aa819d/ciphers/lindenow-1675>.

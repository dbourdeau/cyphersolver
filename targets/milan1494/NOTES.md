# milan1494: Ridolfi (Milan, October 1494) and Alamanni (Vigevano, April 1494) to Piero de' Medici, in the key sheet MAP LXXII 183

Status: in progress. The key did not pass its pre-registered held-out test on doc. 114 (0.838 against a bar of 0.85): the connected text below is a proposal. Read in part with the key sheet ASF Mediceo avanti il Principato LXXII doc. 183, matched and applied by Andrew Aymeloglu (issue #589, 14 Nov 2026; repository `aaymeloglu/unsolved-ciphers`, folder `milan-1494`, CC0, commits 579c487 and 26378c7). Words with no ambiguous sign, after the contributor's revision of 14 Nov 2026 (the n/c and d/l signs told apart by shape): 193 of 283 (68.2%) in Ridolfi's three letters, 51 of 91 (56.0%) in Alamanni's; before it 104 (36.7%) and 37 (40.7%). His own held-out test on Ridolfi's doc. 114 failed its bar (0.838 against 0.85). No page yet: the open pieces below can still be worked.

Catalogue 2382 (Ridolfi) and 2381 (Alamanni). One key, one entry: all four letters are in the same key sheet, so they are one target.

## The documents

Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP), filza LXXIV:

- doc. 112, c. 256r: Giovan Battista Ridolfi, Florentine envoy, Milan, 16 October 1494, to Piero di Lorenzo de' Medici; three cipher blocks on the recto (the verso carries show-through only).
- doc. 113, c. 257r-v: the same, 21 October 1494; nine cipher lines in two blocks on the recto, two on the verso.
- doc. 115, c. 263r: the same, 30 October 1494; four short cipher runs within lines 5-12.
- doc. 96, cc. 220-221: Piero Alamanni, Vigevano, 26 April 1494, to Piero de' Medici; cipher from c. 220v line 6 to c. 221v.

The key sheet is MAP LXXII doc. 183 (image 79536; the verso, image 79537, is endorsed "Cifra con Paulantonio Soderini", by the contributor's reading): an alphabet with up to three signs a letter, signs for et, che, per, io, tu, voi, noi, quando, come and titles, nulls, and numbers from 10 for names (Papa 10, Re di Napoli 11 ...). The images are on the ASF MAP server at 1272 px at most; every image used is listed with its id and SHA-256 in `aaymeloglu/images.tsv`. None is copied here.

## The cipher and the key

A homophonic sign alphabet with a small set of word signs, nulls and name numbers. The contributor found the sheet by comparing the glossed word pairs of Ridolfi's letters LXXIV 107 and 110 (havendo, una volta, questo, stato, salvo, per venire) with the key sheets in filza LXXII: 183 reproduces them letter for letter (44 of 44, his figure; not held out, since the match was found on those pairs). Not on the sheet and added by him, each with its ground in `aaymeloglu/key.json`: six signs for doubled consonants (ss and tt from Ridolfi's interlinear glosses in 107 and 110; rr, nn, bb, cc fitted from the words they make) and the arch-with-dot sign read *non* from the gloss in 110 c. 250r, where the sheet's label reads *noi*.

Two things limited every reading in this key as first filed: the sheet was read as giving the sign ÷ for both n and c, and Ridolfi's d and l were taken as one form. At 1272 px several other signs cannot be told apart. The transcriptions therefore carry, for each ambiguous sign, the value chosen and the alternatives. On 14 Nov 2026 the contributor separated both pairs by shape (section "The contributor's held-out test" below); signs he could not sort with confidence keep their two values.

Name number 22: the sheet gives 22 = S. di Pesaro and 15 = S. Lodovico, but Ridolfi 107 c. 241r has the contemporary gloss "S. Lco" over 22, and the three passages with 22 in Alamanni's letter fit Lodovico. The contributor renders it "[22: probably S. Lodovico]" and grades it inferred. Open.

## What the letters say (the contributor's reading)

Ridolfi, 16 October: Charles VIII's arrival in the castle of Pavia, met by the Duchess Bona; a person written with a sign not on the sheet (now read the Duke, by inference) ill in bed; the citizens of Pavia protest against the milling duty. 21 October, the day the death of Gian Galeazzo was announced: the King spent about two hours at night with Bona; the Duchess Isabella would not appear, pleading illness; fra Lauro met on the road dressed as a courier; Lorenzo and Giovanni di Pierfrancesco at Modena. 30 October: opinion in Milan that Florence cannot resist the French and that they count on dissension in the city; the accord of Forlì and the promise of Faenza.

Alamanni, 26 April: he urges Piero privately that the King of Naples's plan to turn Genoa is the one remedy, must not be delayed and must be entered only with preparation enough to win; that name 22 will never trust the King; and that Piero must tell no one. On c. 221v, Lodovico's three threats: Genoa, France (unread), and closing the road of the Florentine merchants in the West.

Full Italian (clear and cipher) and English: `aaymeloglu/ridolfi-reading.md`, `aaymeloglu/alamanni-reading.md`. The contributor says of the connected text that it is a proposal whose secure parts are the words graded H or C in `aaymeloglu/reading.txt`.

## Counts

The contributor grades every cipher word by how its reading was chosen: strict (no ambiguous sign), forced (ambiguous signs, but only one choice gives a word), lenient (chosen by sense or a language model), doubtful, unread.

| Letters | Cipher words | Strict | Forced | Lenient | Doubtful | Unread |
|---|---|---|---|---|---|---|
| Ridolfi 112, 113, 115, as filed (commit 579c487) | 283 | 104 (36.7%) | 90 (31.8%) | 85 (30.0%) | 2 | 2 |
| Alamanni 96, as filed | 91 | 37 (40.7%) | 24 (26.4%) | 19 (20.9%) | 0 | 11 |
| Ridolfi, revised 14 Nov 2026 (commit 26378c7) | 283 | 193 (68.2%) | 54 (19.1%) | 32 (11.3%) | 2 | 2 |
| Alamanni, revised 14 Nov 2026 | 91 | 51 (56.0%) | 12 (13.2%) | 17 (18.7%) | 2 | 9 |

Read share by the README rule (sure words only; words chosen by sense are holes): the strict tier, now 68.2% and 56.0% (244 of 374 words together, 65.2%), under the 95% bar: read in part. As filed it was 36.7% and 40.7%. The rise comes from relabelling signs by their shape, not from new values: a word is strict when none of its signs is two-valued, and the shape sorts that made signs one-valued were one pass each by agents that had the existing labels (the contributor calls their agreement with the forced words a consistency check, not a blind confirmation). With the forced words, which rest on a dictionary and not on the sense, 87.3% and 69.2% (as filed 68.6% and 67.0%). The contributor's widest figure, every word with a proposed reading, is 98.6% and 87.9%; in his words it is how much has a proposed reading, not how much is right. His own calibration: with the gloss of Ridolfi 107 c. 241v masked, the reader got 28 of 38 glossed words right (74%) and 4 confidently wrong.

Reading review (14 Nov 2026, the project as reviewer, not the author of the reading; `profile.json` `outcome.texts`): both reading files read as Italian against their English, sentence by sentence. Ridolfi 112, 113, 115: grade B, the cipher passages build sentences with the clear text and the English follows them; weak at 'lo edicto ha fatto', 'le poste siano legate', the sign read [il Duca] and the two unread groups of doc. 113. Alamanni 96: decoded, not read, no grade; about half of its cipher clauses break (the passage after [22], 'tu qui tu havessi a schoprire', the three threats of c. 221v), the clear text around them has open gaps, and the English is part summary. `fraction_read` (244 of 374, both letters) was left as recorded.

## Integration check (14 Nov 2026)

- An own decoder (`aaymeloglu/own_decode.py`), written from `key.json` and the two transcriptions, gives the key output column of `reading.txt` for all 283 and all 91 cipher words (1,092 and 371 signs), and the tier counts of the table above. The contributor's `verify.py` was read and not run (it needs his `cipherkit` package).
- Images: the ASF server answered from this session. The key sheet (image 79536) and Ridolfi 112 c. 256r (image 81807) were fetched; their SHA-256 are the ones in `images.tsv`. The sheet shows the alphabet as `key.json` gives it (a: +, two strokes, c; n and c both with ÷; names from Papa 10). Line 4 of c. 256r (13 units, about 45 signs: intendo che arrivando in Pava quando ... fu entrato in castelo) agrees with his transcription sign for sign. The other leaves were not compared.
- The Italian and the English were read as sentences: they hold together and fit the days (the King at Pavia, the Duke's death on 21 October, the march on Florence). The secure part is small, as the contributor says.
- Not repeated here: his key-shuffle control (z = 18.5 Ridolfi, 13.5 Alamanni), the second model's 70 spot checks (`aaymeloglu/audit/codex-review.md`), the blind second transcription.
- Catalogue corrections taken into entries 2382 and 2381 (cipher extent per leaf; the key is LXXII 183, not Alamanni's Naples sheet LXXII 178).

## A test by Brice Dudout on a held-out letter (comment on issue #589, 14 Nov 2026; his report, no files sent)

Brice Dudout applied the published `key.json` (commit 46dec7b) unchanged to Ridolfi's glossed letter MAP LXXIV doc. 114 (22 October 1494; 27 cipher lines, 865 signs, his own transcription frozen before he fetched the key), against the text printed by Desjardins, *Négociations diplomatiques de la France avec la Toscane*, I (1859), pp. 585-586. One measurement: character agreement 0.774 against 0.397 for the best of 200 shuffled keys. His bar was 0.85, so the test failed by his own rule; he puts the loss on the image resolution and on one shape choice of his own (the d/l class). 101 of 175 words exact. The key reads running Italian on a letter it was not built on; the test does not reach his bar. His own key, built from Niccolini's glosses of 1492-93 without the sheet, agrees on most values, also has ÷ for n and c, and reads 22 as Lodovico (his report).

He also points to P. D. Gabbrielli's copy book of the keys of the Dieci di Balìa (Ilardi microfilm reel 58, Yale Dataverse doi:10.60600/YU/XKVOWE; inventory in issue #610): no. 25 (Piero Alamanni, 1492) and no. 34 ("de Rydolfis", 1495) are the nearest to these letters. Not tested on them.

## The contributor's held-out test on doc. 114 (issue #589, comment of 14 Nov 2026, 21:44 UTC): failed, by 0.012

Asked on 14 Nov whether doc. 114 could serve as his own held-out test, Andrew Aymeloglu ran it the same day and filed it in his repository (commit 26378c7, folder `held-out-114/`, copied here unchanged as `aaymeloglu/held-out-114/`).

- **Declared beforehand** (`PREREGISTRATION.md`): key `key.json` at commit 46dec7b unchanged; a transcription of the gloss-masked cipher lines of doc. 114 by an agent that saw neither gloss, key values nor print; reference Desjardins I (1859), pp. 585-586; one measurement, character agreement after alignment, any listed value of a two-valued sign counting; 1,000 shuffled keys; bar 0.85.
- **Result: 0.838, under the bar. The test failed.** Best of 1,000 shuffled keys 0.379, mean 0.286. With every two-valued sign forced to its first value 0.775 (Brice Dudout's 0.774). The contributor asks that it be recorded as below the bar; it is.
- **Not done, though promised in the protocol:** the count of exact words.
- **After the result, not pre-registered:** dropping two wrongly delimited ends of block 5 would give 0.844 (his diagnostic, still under the bar; the frozen score stands). Against the gloss as he read it from the leaf the same transcription scores 0.886; about a dozen gloss spellings were settled with the help of the cipher, so by his own account that is not an independent figure.
- **Order of events and blinding: by the contributor's record.** One commit of 14 Nov 2026 (21:43 UTC) holds the protocol, the transcription and the result. He lists the limits himself: a few label names are mnemonic (BB, CC, NN, ET, TH), the exemplar label sequences carry the earlier sign divisions, the masking agent saw the gloss and set the block boundaries, and the scoring session had seen c. 258r and the two fragments quoted in the issue.

Checked here on 14 Nov 2026 (an AI agent, not a person):

- The SHA-256 of `transcription-frozen.tsv` (98f1ec21...), `score.py` (439bd0ea...) and `key-46dec7b.json` (91472a7f..., equal to `key.json` at his commit 46dec7b) are the ones in `PREREGISTRATION.md`.
- `score.py` was read and run with `python3 -I`: 865 signs, 988 reference letters, 0.8382, first value only 0.7745, shuffles best 0.3790, mean 0.2859, as filed.
- An own scorer written from the protocol (not importing his): 0.8382 and 0.7745 against Desjardins; 0.8855 against his gloss reading; best of 300 own shuffles 0.362, mean 0.286.
- `own_decode.py`, unchanged, run on the revised `key.json` and transcriptions: the key output of `reading.txt` for all 283 and 91 cipher words (1,092 and 371 signs) and the revised tier counts of the table above.
- Not checked: the reference against a copy of Desjardins (the file is his transcription of the print); the transcription of doc. 114, the shape sorts and the gloss reading against the images. The ASF server, which answered this session in the morning, reset every connection in the evening of 14 Nov (three tries; no bot check page). The second model's review (`audit/codex-review-2.md`) was not repeated.

What the gloss of doc. 114 gave, by his report (from here on 114 is no longer held out):

1. ÷ is two signs: a dot or tick above the dash (with or without one below) is n, a dot below only is c; he reads the key sheet's own cells that way when enlarged. In Ridolfi's three letters 73 of 73 and 34 of 34 sorted signs agree with the word; in Alamanni's, 12 of 12 and 6 of 6 where the word decides.
2. Ridolfi's d and l separate: l has an arm to the right at the baseline, d has none (32 of 32 and 57 of 57 in the three letters).
3. A sign for ll, a d-shape with a barred ascender: under *quella*, *alla*, *quello*, *fanciullo*, *Isabella*, *quelli* in 114; it gives *castello*, *alla camera*, *nel letto*, *non volle*, *cavallaro* in 112, 113, 115, and *mantello* in Alamanni's letter where a sign was unplaced.
4. bb is glossed four times. The long-tailed 2 with a raised c is glossed *Re* five times, which settles [il Re]; the same base with another raised letter is glossed *Duca* twice, so the open person sign of 112 is now read [il Duca], by inference (the raised letter is not clear at 1272 px; Lodovico is not excluded).
5. Alamanni's second threat: the letters now give "ce la calerà" (doubtful); the word before it is unread.

The new labels are `Na`/`Nb`, `/a`/`/b`, `Zh`/`Za` and `LL` in `key.json`.

Gabbrielli's copy book (Brice Dudout's pointer), by his report from frames 58-29 and 58-38: no. 25 (Alamanni, 1492) is the alphabet of sheet 183 as far as Gabbrielli recovered it, with doppie ll, nn, rr, tt, which supports the nn and rr that had only been fitted (a nineteenth-century reconstruction from deciphered letters, so corroboration, not a second sheet); no. 34 ("de Rydolphis", 1495) is a different alphabet and not that of the October 1494 letters. No. 25 was not scored separately on doc. 96; nos. 13, 26 and 30 were not looked at. Not seen here.

He also reports that the ASF server answered a United States address directly on 14 Nov.

## Relation to rucellai1482 (pull request 617)

Bernardo Rucellai's letters of 1482 in the same fonds (MAP LXXII 196-211) are in another table: in Brice Dudout's key for them 6 is a, 7 is e and = is n, where the sheet LXXII 183 has 6 and 7 for i and ÷ for n and c. The two keys do not relate beyond the family of system (a sign alphabet with homophones, nulls and separate signs for doubled consonants, which both workers found independently for rr and tt).

## 14 Nov 2026: reading review (audit section J)

Both reading files were read as sentences and a `reading_review` recorded for each entry in `profile.json`.

- Ridolfi (docs 112, 113, 115): grade A. Every sentence with cipher in it holds and translates; the holes are two unread
  groups in doc. 113 and a few words marked (?), most of them in the clear hand.
- Alamanni (doc. 96): grade A. The cipher passages are short runs inside clear sentences and fit them; the unread cipher
  is in three runs (11 of 91 words). The clear hand has more gaps than the cipher. The contributor's English abridges
  the clear text of c. 220r and parts of the rest, so the whole Italian letter was translated here, sentence for
  sentence, with the same holes: `alamanni_en.md`.
- The grade says the sentences are coherent. It does not make the words secure: the state stays read in part and the
  read shares stay the strict tier (0.367 and 0.407). No image was looked at in this pass.

## Niccolini's bare passages, catalogue 2380 (19 Nov 2026, Malcolm McBratney with Claude): attempted, not read

As agreed on issue #589, the four bare cipher passages of Angelo Niccolini in MAP LXXIV (docs 42 c. 90r, 49 c. 104r, 81 c. 177r, 90 c. 200r; Aug 1492 - Jan 1493) were transcribed blind with neutral labels, frozen and decoded once with `aaymeloglu/key.json` unchanged. Files and method in `niccolini/README.md`. No person has checked the transcriptions. This blind pass supersedes our sighted working decode of 10 Nov 2026 (earlier record: Zenodo doi:10.5281/zenodo.24267269, unfiled), described on #589 as read: docs 42, 81 and 90 now score 61.5%, 50.0% and 33.3%, so those readings are withdrawn.

- Strict judge (word units): doc 42 16/26 = 61.5%, doc 49 0/5, doc 81 4/8 = 50.0%, doc 90 2/6 = 33.3%. All below our 65% line: attempted, not read.
- Shuffle control (5,000 at seeds 20261112 and 7): doc 42 0 and 0, doc 81 0 and 1; docs 49 and 90 fail (14/10, 158/139).
- Doc 42 decodes in part ("el re di Francia ... dal governo [22] ... e apto ad governare lui per non"), which suggests the 1494 sheet is close to the 1492-93 key but differs in some signs. A key from Niccolini's glossed letters was not built.

## Gabbrielli key no. 25 on Niccolini's glossed letters (14-20 Nov 2026, Brice Dudout with Claude): attempted, not read

Brice Dudout tested key no. 25 of Gabbrielli's *Chiavi delle cifre ... Dieci di Balìa*, vol. 1 ("an. 1492, Alamannis (de) Petrus", filza 39; Ilardi microfilm reel 58, Yale Dataverse doi:10.60600/YU/XKVOWE). The key was transcribed twice, the second pass blind, and frozen as K_G25. It was then tested against the contemporary interlinear glosses of Niccolini's letters in MAP LXXIV, in four pre-registered stages. Files, hashes and scripts are in `niccolini/gabbrielli25/README.md`. All transcriptions are blind passes by AI agents with neutral labels F01-F39, and no person has checked them.

- P02 (doc. 78, pos. 329-331), P03 (pos. 158, 159, 161, 167, 351, 254, 300, 299) and P04 (doc. 97, pos. 443-444): not measurable. Too few signs sit under a complete gloss (15, 86 and 0 F signs, against a floor of 300). Nothing was decoded.
- P05 (plan B: partial glosses, local alignment, 39 runs, 778 gloss letters): 0.4987 against a bar of 0.85. Best key control 0.3123, best gloss control 0.3201 (200 each). Failed. K_G25 beats every control, so it is probably related to Niccolini's cipher, but it is not his key as it stands, or the 1272 px transcriptions are too noisy (19% T2/T3 disagreement), or both.
- K_G25 was not applied to the bare passages, and no decoding of catalogue 2380 is presented. Malcolm McBratney's blind transcriptions in `niccolini/blind/` were not used.

## Remaining gaps

- 32 + 17 words chosen by sense and 54 + 12 forced words still rest on ambiguous signs (signs not sorted with confidence; b, 6 and others at 1272 px) - blocker: none yet; the shape sorts of ÷ and d/l were one pass each by agents that had the labels, and nobody has re-sorted them blind; doc. 114 is used up as a test (failed, 0.838 against 0.85) and Ridolfi's glossed letters 101-110 have not been used
- Two unread groups and two doubtful words in Ridolfi 113; 9 unread and 2 doubtful words in Alamanni (the second threat on c. 221v, where "ce la calerà" is doubtful and the word before it unread; a run after name 22 on c. 220v; a few signs) - blocker: none yet; Gabbrielli's no. 25 is this alphabet by the contributor's report and was not scored separately on doc. 96, no. 34 is another alphabet, nos. 13, 26 and 30 were not looked at
- Name number 22 (sheet: S. di Pesaro; gloss in Ridolfi 107: S. Lodovico) and 15 - blocker: none yet; doc. 114 has neither; the other letters in this key have not been searched for 22 and 15
- The second person sign of doc. 112, now read [il Duca] by inference from two glosses in doc. 114 ([il Re] is settled by five glosses there) - blocker: none yet; the raised letter is not clear at 1272 px
- The fitted rr, nn and cc have Gabbrielli's support (by the contributor's report) but no gloss - blocker: none yet; Ridolfi 101-110 and Niccolini's glossed letters are the place to look
- The transcription of doc. 114, the shape sorts and the contributor's gloss reading were not compared with the images here - blocker: none yet; the ASF server reset the connection on the evening of 14 Nov 2026 (it answered in the morning)
- The clear text of the four letters was read from the same images and not collated - blocker: none yet
- Higher-resolution images - blocker: needs-physical-access; the ASF server serves 1272 px at most
- Niccolini 2380 (docs 42, 49, 81, 90) attempted, not read with the 1494 key (`niccolini/README.md`) - blocker: not-attempted: a key from Niccolini's own glossed letters of 1492-93 in this filza (docs 6, 21, 32, 35-37, 59, 62, 72, 78, 81 c. 176r, 97), then a declared second pass on docs 42 and 81; docs 49 and 90 are too short for the shuffle control.
- Gabbrielli key no. 25 (K_G25, Alamanni 1492) on Niccolini's glossed letters: failed (P05 0.4987 against 0.85; `niccolini/gabbrielli25/README.md`); doc. 97 pos. 443-444 and pos. 158, 159, 161, 167, 254, 299, 300, 351 are used up - blocker: not-attempted: Dieci di Balìa, Responsive, filza 39 (not online) and higher-resolution images; K_G25 not compared sign by sign with `aaymeloglu/key.json`

## Escalation

- [x] siblings: Ridolfi 107 and 110 (glossed) used to find the key; 114 used by Brice Dudout as a test, then by the contributor as his held-out test (failed, 0.838) and as an exemplar set; 101-106, 108-109 not used
- [x] clear-pages: the clear passages of the four letters are transcribed in the reading files
- [x] known-keys: MAP LXXII 183 is the key; LXXII 178 (Alamanni's Naples sheet) saved by the contributor and not formally tested
- [ ] print: Desjardins I (1859) prints doc. 114; whether he or others print 112, 113, 115 or doc. 96 was searched by the contributor without result, and not re-searched here
- [x] key-rebuild: the signs for doubled consonants and *non* were added; on 14 Nov 2026 ÷ was split into n and c and Ridolfi's d and l were separated by shape, and a sign for ll added, from the gloss of doc. 114
- [x] retry: the four letters relabelled and re-read by the contributor after the separation (strict 68.2% and 56.0%); a blind second sort is not made

## Files

| File | Content |
|---|---|
| `aaymeloglu/key.json` | the key: every sign with its values, what the sheet gives, the grade and the ground |
| `aaymeloglu/ridolfi-transcription.tsv`, `aaymeloglu/alamanni-transcription.tsv` | one row per unit, with the chosen value and the alternatives of each ambiguous sign |
| `aaymeloglu/reading.txt` | key output against the editorial reading, word by word, with tier and grade |
| `aaymeloglu/ridolfi-reading.md`, `aaymeloglu/alamanni-reading.md` | Italian and English |
| `aaymeloglu/images.tsv` | the ASF images used, with their SHA-256 |
| `aaymeloglu/held-out-114/` | the contributor's held-out test on doc. 114 (protocol, frozen transcription, scorer, result: failed), his gloss reading, the shape sorts and `apply_shapes.py` (commit 26378c7, 14 Nov 2026) |
| `aaymeloglu/README_aaymeloglu.md`, `aaymeloglu/AUDIT.md`, `aaymeloglu/audit/` | the contributor's account, the history of the work and the second model's review |
| `aaymeloglu/own_decode.py` | the project's decoder and count |
| `alamanni_en.md` | the project's full English of Alamanni's letter (14 Nov 2026) |
| `niccolini/gabbrielli25/` | Gabbrielli key no. 25 frozen as K_G25, the blind transcriptions of the glossed letters, PREREGs P02-P05 with hashes and scripts, and the results (failed) |

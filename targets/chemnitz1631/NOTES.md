# chemnitz1631: notes

Status: in progress (re-reading of 17 Nov 2026: read in part, 72 of 89 cipher words sure = 80.9% by the README rule, was 68 = 76.4%; 80/89 = 89.9% with probable words. Next step: test the restored values 46, 51 and 43 on their occurrences in the glossed page 58 as a key rebuild; the other gaps are clear figures that disagree with the key or two doubtful figures. Catalogue lead 2570 stays open.)

**Contributor's status: partial reading** (the outcome class in profile.json says the same). 89 cipher words in the two bare passages of images 55
and 56: 68 sure, 11 probable, 10 on values restored from the sense. Sure + probable = 79/89 = 88.8 %, under the
95 % bar, so the entry is not marked "read". Image 55: 37/40 (92.5 %); image 56: 42/49 (85.7 %).

## Key and its test
- The key (key.tsv, 79 values) comes only from the **contemporary interlinear decipherment** written at the time over
  the letter of image 57 (same writer, same file): 124 glossed words, 598 letter-group pairs (gloss57_pairs.txt).
  Credit: `contemporary`, role "key or decipherment used".
- Protocol and key frozen by SHA-256 (PREREG-3) before the held-out page was transcribed; one run (validation.txt).
- Held-out portion: image 58 left (another Chemnitz letter, 5 Nov 1631), the only Chemnitz page left in the
  volume. Images 55 and 56 were not used for testing: an earlier 23-value table had been tried on them and failed
  (coverage 59 %).
- **Measure A (frequency): indicative only.** S = 0.969 vs 0.869 for the best of 200 permuted keys, coverage 97 %,
  but on **144 groups, fewer than the 150 asked**. It is reported, not counted as a pass.
- **Measure B (glosses of 58): pass.** Agreement 95.6 % on 91 letters vs 34.1 % for the best control (threshold
  fixed in advance: at least 0.30 above the best control).
- The restored values (46=w, 29=b, 51=r, ligatures Sd=w and Sf=t, 10=c) are not in the 57 glosses; they are marked
  in key.tsv and in reading.md. 51=r also fits the near-cycle of 24 in the numbering (3, 27 = r).

## Prior work checked
- *Arkiv till upplysning om svenska krigens historia* I and II (1854-1861, archive.org OCR): no Chemnitz letter of
  1631. A web search found no edition. Not on DECODE.
- Riksarkivet "Agenten Chemnitz brev till Kungl. Maj:t" (Diplomatica Germanica, SE/RA/2106/F/XI/1392, 1631-1632)
  is not digitised and was not seen: it may hold more letters in the same system, or a key.

## Limits
- Transcription by an AI model from the full-resolution IIIF images; no human palaeographer checked it.
  Doubtful figures: 4/7, 24/27, 14, 58, 21 (listed in reading.md).
- reading_review grade B by the model; `_check_reading` scores 73 % of sentences clean (unspaced text), and
  the weak sentences were the ones read again for the review.
- The date of image 55 is not established.
- Images are not reproduced (Riksarkivet IIIF, Public Domain Mark; cited by image number).

## Integration check (13 Nov 2026)

Verified for the maintainer before merging PR #539 (Brice Dudout). The PR carries no scripts; the checks were made with
a decoder written for the check.

- **Key from the glosses.** Rebuilding the key from gloss57_pairs.txt (majority letter per group) gives 598 pairs and
  79 values, as stated. key.tsv agrees with it except where it should: 45 (the glosses give ß 2, s 1; key.tsv s),
  47 (v/u) and the five values marked restored (46 w, 29 b, 51 r, Sd w, Sf t), which the glosses do not give. Twelve
  groups carry more than one letter in the glosses (9: u 15, v 6, s 4, ü 1; 68: s 4, l 1; 49: f 2, n 1; and others).
- **Decryption.** Decoding transcription.txt with the rebuilt key reproduces decryption.txt (up to ß/s and u/v). The
  raw decode shows where the probable words come from: gewaltib, unterseilen, deusewohn·, anspag, wibd, fe·nd,
  hifweck, begierung, dtm: in each, one group gives a letter the sense rejects.
- **Held-out page 58.** 144 groups, 140 with a value (97%), as stated. The decode reads in part as German (das ... die
  stat auch nur durch ... animiren ... referiren das ich nicht von hinnen verreise ... grossen nachtheil). Measure A
  did not meet its own declared condition (150 groups); it is reported, not counted. Measure B (95.6% of 91 letters
  against 34.1%) could not be re-run: the alignment of page 58's glosses is not in the PR, and the PREREG-3 hashes
  are not in the files either, so Measure B and the order of events are by the contributor's record.
- **Earlier attempt.** An earlier 23-value table tried on images 55 and 56 failed (coverage 59%), by the
  contributor's record; this is why 55-56 were not used as the test.
- **Images.** Riksarkivet IIIF (lbiiif.riksarkivet.se/arkis!R0000624_000NN/full/max/0/default.jpg) answered 200 with
  curl for images 55 and 57. Image 55, lines 3-6 of the cipher passage: 68 groups compared, 67 agree with
  transcription.txt; the group transcribed S2 in line 6 (in "deusewohn·") looks on the image like the ligature
  transcribed Sf elsewhere (restored t), which would give ...gewohnt if 9 is also misread. Image 57: the glosses
  over the first two lines (auf, anhalten, eines, weil, allem, einkommenem) agree with gloss57_pairs.txt.
- **Count, strict rule.** Probable words (a group read against the key, or a doubtful figure) and restored words
  (values not in the glosses, supplied from the sense) are holes. Image 55: 34/40; image 56: 34/49; together 68/89 =
  76.4%. The contributor's figure, counting probable words, is 79/89 = 88.8%.
- **Why in progress.** The gaps are workable with what is in hand: the restored values (46, 29, 51, Sd, Sf) can be
  tested on their other occurrences in images 55-58; the probable words rest on figures that can be re-read on the
  images (4/7, 24/27, 14, 58, 21, and the S2/Sf group above); the volume may hold more Chemnitz leaves (only a top-64
  window sheet screened it). Only the Riksarkivet volume "Agenten Chemnitz brev" (SE/RA/2106/F/XI/1392, not
  digitised) needs an outside step.
- **Prior art.** Not on DECODE; no edition found by the contributor (Arkiv till upplysning om svenska krigens
  historia I-II); not re-searched here. Images 55 and 56 were used in the contributor's earlier failed attempt.
- **Writer.** "Martin Chemnitz (1596-1645)" is the contributor's identification from the signature and the
  literature; not checked here.

## Remaining gaps
- images 55-56: 9 words on restored values (46, 51, 43=l, ligatures Sd and Sf, 10=c) - blocker: not-attempted; key rebuild: test the values on their occurrences in the glossed page 58 (not done in the 17 Nov re-reading, which kept the key frozen)
- images 55-56: 6 probable words with clear figures that the key values otherwise than the sense needs (unterweilen 21, gewohnt S2, Anspach 7, feind t, zweifel 58, dem 4) - blocker: no-key-material; likely encipherment slips, re-read on 17 Nov 2026; no other gloss of these words in the volume
- image 56: 'sein' and 'aber', one doubtful figure each - blocker: illegible; re-read on 17 Nov 2026 at full resolution (a flourish crosses the 'aber' figure)
- further Chemnitz letters in SE/RA/2106/F/XI/1392 - blocker: needs-physical-access; not digitised

## Escalation
- [ ] siblings: the rest of R0000624 not paged beyond images 54-59 at full size
- [x] clear-pages: image 57's gloss is the key source; image 58's glosses used as the test
- [ ] known-keys: no other Swedish agents' keys of 1631 tried
- [x] print: Arkiv till upplysning om svenska krigens historia I-II (contributor): nothing
- [ ] key-rebuild: restored values not yet tested on their other occurrences
- [x] retry: doubtful figures re-read on the images, 17 Nov 2026 (four groups corrected, see below)

## Re-reading (17 Nov 2026, Brice Dudout with a Claude Opus 5.5 agent)

Reading only, no new measurement (no fresh held-out portion exists) and **no change to key.tsv**.
- The doubtful figures of images 55 and 56 were re-read on the full-resolution Riksarkivet IIIF images in two passes
  (line crops, then the target groups set beside reference figures of the same hand). The hand writes 4 closed with a
  cross-bar (4, 14, 40, 48 in 'vorkombt', 24 in 'aber' on 55) and 7 open like a y (17 = a throughout, 27 in 'vorath',
  78 in 'aufschlagen').
- Four groups first transcribed with a 4 carry the open 7: 55 line 2 **78** (not 48), 56 line 3 **27** (not 24) and
  **79** (not 49), 56 line 6 **27** (not 24). The key then gives 'gewaltig', 'wird', 'hinweck' and 'regierung' letter
  for letter: four probable words become sure. transcription.txt and decryption.txt are corrected; reading.md lists the
  figures looked at and left unchanged.
- 'aber' (56 line 4): the figure looks more like a closed 4 (24 = b) than 29, but a ligature flourish crosses it, so
  the word goes from restored to probable, not to sure.
- Count: 72/89 sure = 80.9% (image 55 35/40, image 56 37/49); sure + probable 80/89 = 89.9%.
- Ceiling: the 9 words on restored values (46, 51, 43=l, Sd, Sf, 10=c) have clear figures that the glosses of 57 do not
  value. The numbering supports 46 = w, 51 = r and 43 = l (rows of about 24: 22, 46, 69, 93 = w; 3, 27, 51, 74 = r;
  19, 43, 66, 90 = l; key.tsv has 43 = m from the glosses), but that is a conjecture about the key and is not counted.
  With the key as it stands, at most 80 of 89 words (89.9%) can be sure.
- Prior work re-checked on 17 Nov 2026: no other pull request or target touches this letter.


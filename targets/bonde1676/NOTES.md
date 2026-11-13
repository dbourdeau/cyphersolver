# Bonde and Lillieroot to Louis XIV (6/16 Oct 1676) and Bonde to Charles XI (24 Nov/4 Dec 1677): one number table (Riksarkivet, Diplomatica Gallica; catalogue 2317)

Status: read in part, contributed. No claim of a first reading (see Prior art).

**Two documents, one key (decided at integration, 12 Nov 2026).** The contributor filed two folders (PR #486 `bonde1676`, the
French memorial, read with key v3; PR #485 `bonde1677`, a Swedish despatch, read with key v9). v9 is the same number table as
v3, corrected (66, 89, 21, 103, 131, 176, 335) and extended by 36 rows (none dropped), so under one key, one entry they are one
target. The memorial is the main text (this file, top level); the 1677 despatch sits in `despatch1677/` with its own key state,
decoder, controls and the contributor's original notes (`despatch1677/CONTRIBUTOR_NOTES.md`). Both are counted by the same strict
rule: memorial 546 of 764 units (71.47%), despatch 24 of 30 (80.00%), together 570 of 794 (71.79%). Neither reaches the 95% bar.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic). Issue #453 and its two comments. This folder
answers the request on that issue for the transcription, the frozen key, the decoder, the decryption, the reading and
translation with holes marked, and the shuffled-key control.

## What the document is

Stockholm, Riksarkivet, Diplomatica Gallica, SE/RA/2105/I/A/24/54, "Envoyén Carl Bonde, Brev till Kungl. Maj:t 1674-1678"
(image series R0003797; IIIF manifest `https://lbiiif.riksarkivet.se/arkis!R0003797/manifest`; viewer
`https://sok.riksarkivet.se/bildvisning/R0003797_00321` and following). A memorial in French from the Swedish envoys in
Paris, Carl Bonde and Nils Lillieroot, to Louis XIV, headed "6 Oct: 1676" (Old Style) on f.306r and signed "C.B. N.L." on
f.311r. It follows the envoys' despatch of 6/16 Oct 1676 (image 321L) and is its enclosure. Long passages are in cipher;
the rest is clear French. No gloss on these leaves.

| page | image | cipher numbers | word units | read (strict, after corrections) | decoded |
|---|---|---|---|---|---|
| f.306r | 321R | 205 | 47 | 33 = 70.21% | once, v3 frozen (b104) |
| f.306v | 322L | 546 | 120 | 73 = 60.83% | once, v3 frozen (b104) |
| f.307r | 322R | 493 | 111 | 94 = 84.68% | once, v3 frozen (b104) |
| f.307v | 323L | 500 | 100 | 71 = 71.00% | once, v3 frozen (b101) |
| f.308r | 323R | 496 | 104 | 83 = 79.81% | once, v3 frozen (b101) |
| f.308v, lines 1-14 | 324L | 202 | - | training lines of the key | - |
| f.308v-309r, rest | 324 | 501 | 103 under v2 | 44 = 42.72% under key v2 (first test); in-sample for v3 | once, v2 (b99) |
| f.309v | 325L | 399 | 82 | 50 = 60.98% | once, v3 frozen (b101) |
| f.310r | 325R | 382 | 83 | 62 = 74.70% | once, v3 frozen (b101) |
| f.310v | 326L | 364 | 72 | 47 = 65.28% | once, v3 frozen (b101) |
| f.311r | 326R | 214 | 45 | 33 = 73.33% | once, v3 frozen (b101) |

Nine held-out pages: 33 + 73 + 94 + 71 + 83 + 50 + 62 + 47 + 33 = 546 of 47 + 120 + 111 + 100 + 104 + 82 + 83 + 72 + 45
= 764 word units, strict 71.47%. Under the 95% bar: read in part. Per-page sums, the filed figures and the corrected ones:
`counts.txt`. Cipher numbers counted by script over the transcription files (4,302 in all, 96 cut at the gutter).

## The system

Homophonic substitution on numbers, one number a letter: seven numbers each for e, f and n in key v3, six for l and o; a few numbers
stand for ss, st, ff, ll. Word codes from about 240 (314 = Danmarck in the 1675 gloss). The signs 173-178 and the single
digits 3, 4, 8 stand alone between words and look like nulls; nothing proves it. The same table serves Bonde's Swedish
despatches of 1675-1678 in the volume: 66 is å in Swedish and is written for y in this French text; 89 is n in the 1675
gloss and l here. Numbers are separated by dots; no word division.

## The key and how it was obtained

All on 12 Nov 2026 (UTC), one session each (b99, b101, b104), every step logged and stamped (`timestamps/`).

1. Key v1 (`gloss/KEY_v1.tsv`): the chancery's interlinear decipherment of Bonde's despatch of 11/21 Nov 1675 (image 102R,
   f.96r) aligned letter by letter with the cipher numbers beneath it by EM (`scripts/original/em4.py`; 488 numbers
   against 566 gloss letters; output `gloss/em4_out.txt`). The gloss lines and number lines as read are
   `gloss/gloss_102R_f96r_lines1-16.txt` (provisional reading of the hand; not frozen, not checked).
2. Control: rows 1-10 of image 107L (bare) transcribed and frozen, decoded once with v1 (`gloss/control_107L_*`), then
   found word for word in the gloss on image 105L. So 107-109 are the cipher tail of the 1675 despatch, already deciphered
   at the time (catalogue correction below).
3. Key v2 (`gloss/KEY_v2.tsv`, frozen 02:49:24): v1 with values corrected from 107L/105L (tier B) and values 100-176 fixed
   on 14 training lines of image 324L (tier F, `transcriptions/f308v_324L_lines1-14_training.txt`).
4. First test: the other 30 lines of image 324 frozen (02:50:10) and decoded once with v2: strict 44/103 = 42.72%, under
   the 65% bar we set ourselves. Shuffled keys 0 of 5,000 (two seeds).
5. Key v3 (`key.tsv`, md5 8e1d93d1188e698ad6dd14826e8ba168, frozen 02:55:22): v2 plus 23 values read off the image-324
   test lines after that test (tier P), and 88 corrected from a to m (a misread numeral on 102R). So image 324 is in-sample
   for v3 and is not counted under it. 128 rows: A 57 (gloss of 102R), B 6 (107L/105L), F 29 (324 training lines),
   P 23 (324 test lines, after the test), C 4 (weak guesses, shown in capitals and never counted), W 8 and U 1 (word codes).
6. Nine pages transcribed after v3 was frozen, each frozen before a single decode with v3 unchanged (b101 for f.307v-311r,
   b104 for f.306r-307r). No value was changed after those decodes; values that the decodes suggest are listed in
   `holes.md` 2 and never counted.

Method class: key recovered from the decipherment of a glossed sibling despatch in the same file, finished on context in
the memorial's own image 324, then applied to nine pages held out from it. Not a ciphertext-only break. About two fifths of
the key's letter rows (F 29 + P 23 = 52 of 119 letter rows) come from context in image 324, not from the gloss.

Key lineage: `despatch1677/` reads a Swedish despatch of Nov/Dec 1677 with key v9 (md5 af29e81f). v9 is a later state of
this same key: v3, then v4-v7 (values from context in the 1676 despatches and the post-hoc values of this memorial),
v8-v9 (values from chancery glosses of 1676-1677), with 131 changed from q to r. v9 was made for Swedish text; this French
memorial is read with v3 only, and no v4-v10 value is used here. Keys v4-v10 and the despatches read with them: next section and `despatches/`.

## The 1677 despatch (folded in from PR #485)

Carl Bonde (Paris) to Charles XI, "Paris d. 24 Novemb./4 Decemb. 1677" (image 490L), Swedish; the only cipher is on image 489R
(hand folio 474): 17 runs, 169 numbers inside clear sentences, no gloss. Key v9 (`despatch1677/key.tsv`, md5
af29e81f99e96f03663d94dea392e672, 164 rows), by the contributor's record frozen at 06:08:58 UTC, before 489R was transcribed;
first transcription frozen 06:24:26 and decoded once: **24 of 30 word units = 80.00%** strict; the blind second transcription
(b127, 168 of 169 numbers the same, 61 against 67 in "alarme") 23 of 30 = 76.67%. Not read: ila (illa) and instäla
(inställa) spelt short by the key, paeE (46 weak), <418>en twice, <435>. Of the 149 numbers inside the 24 read units 90 have a
value from the 1675 gloss, 1 from a 1676-77 gloss and 58 from context (F 36, P 16, Q 5, T 1); 22 of the 24 read units use at
least one context value. The contributor's issue text said the key was "built only from the chancery's glosses": it is not.
A 30-unit test is too short to say much about the key (blocker too-short): shuffled keys 0 of 5,000 (true -3.1451, best
-4.0151 and -3.9637), but the test is weak. The clear Swedish between the runs agrees with the decode, which is the stronger
evidence: "man här wid Hofwet mycket [illa tilfredt]", "kommandes till Lijfland och förnimmandes [Paez' opposition] skulle
willia [dröya och inställa]". Reading: `despatch1677/readings/`, translation: `despatch1677/translations/`; the contributor's
own notes: `despatch1677/CONTRIBUTOR_NOTES.md`. The despatch of 17/27 Nov 1677 (images 479R-481R), decoded in the same
session with v9 at 62/100 = 62.00%, is under the contributor's threshold and was not filed with #476; it is now in `despatches/` (13 Nov 2026).

## Key states v4 to v10 and the despatches read with them (added 13 Nov 2026)

After the memorial, the same number table was carried through Bonde's other bare (unglossed) despatches in the volume, with a key
state frozen before each new stretch of text. These are filed here at Dan Bourdeau's request on #453/#476 for one entry, **below our
own 65% line except one, and that one is not first**. Everything is in `despatches/`: frozen page transcriptions, the decodes, the
reader's word division, the doubt notes, readings and English (AI-made) with holes, `manifest.tsv` (one row per page decode, with the
md5 and time of each freeze), `counts.txt`, `units.tsv`, the controls and `PRIOR_ART.md`. The key states are described, with gloss
values and context values counted apart, in `despatches/keys/LINEAGE.md`; v4-v8 are in `despatch1677/gloss/key_history/`, v9 is
`despatch1677/key.tsv`, v10 is new (`despatches/keys/KEY_v10.tsv`, md5 f780c0f3).

First pass = each page frozen, then decoded once with the key frozen before it. It is the figure of record. Figures are per despatch,
never pooled across despatches.

| despatch (R0003797 images) | key | first pass, strict | flags |
|---|---|---|---|
| Bonde, 12/22 Feb 1676 (159R-165L) | v10 | 41 + 48 + 68 + 44 + 82 + 35 + 64 + 2 = 384 of 603 = 63.68% | under 65%. Gutter: a decode-blind second transcription of the left pages (b125) gives the despatch 385 of 593 = 64.92%; the gutter digits are physically lost |
| Bonde and Lillieroot, 12/22 Aug 1676 (278R-283R) | v10 | 26 + 61 + 64 + 57 + 69 + 50 + 92 + 56 + 19 = 494 of 705 = 70.07% | **NOT FIRST**: Wimarson II (1903) p.176 n.3 and p.305 n.1 paraphrase its substance, except the Feuquières passage (279R) |
| Bonde and Lillieroot, 6/16 Oct 1676 (317R-321L) | v7; v8 | 317R, 318L/R, 319L: 108 of 262 = 41.22% (318L/R alone 63 of 145; 317R + 319L 45 of 117); 319R, 320L, 320R top: 78 of 185 = 42.16% | under 65%; a second transcription of 318 (blind, then adjudicated against the first: decode not blind) 71 of 147 = 48.30% |
| Bonde and Lillieroot, 13/23 Oct 1676 (327R-330R) | v4; v5; v6 | 327R lines 4-10: 10 of 23; 328L lines 1-13: 11 of 26; the rest: 161 of 315 = 51.11% | under 65%; 327R lines 1-3 were training for v4 |
| Bonde, 3/13 Nov 1677 (471R-473R) | v9 | 75 of 131 = 57.25% | under 65%; short |
| Bonde, 17/27 Nov 1677 (479R-482L) | v9 | 62 of 100 = 62.00% | under 65%; short |
| Bonde, French copy, 24 Nov/4 Dec 1677 (490R-491L) | v3 | 34 of 70 = 48.57% | under 65%; short |
| Bonde, 1/11 Dec 1677 (491R-493R) | v9 | 66 of 104 = 63.46% | under 65%; short; 493L failed its shuffle test |
| Bonde, 29 Dec 1677/8 Jan 1678 (506R-511R) | v9 | 214 of 377 = 56.76% | under 65% |
| Bonde, 5/15 Jan 1678 (512R-516L) | v9 | 112 of 194 = 57.73% | under 65%; 515L failed its shuffle test |

Per-page sums for every row: `despatches/counts.txt`. Short = under 150 word units.

**Re-scores, NOT held-out** (a later key over pages already seen; never a figure of record): 6/16 Oct 1676 v7 pages with v8, 127 of
264 = 48.11% (318 on the adjudicated second transcription); 13/23 Oct 1676 v6 pages with v8, 183 of 315 = 58.10%; with v10, 1/11 Dec
1677 73 of 104 = 70.19%, 29 Dec 1677 262 of 377 = 69.50%, 5/15 Jan 1678 130 of 194 = 67.01%. v10's new values came from glosses of
other despatches, not from these pages, but the pages had been decoded and read before v10 was made.

**Gloss values and context values.** In every despatch most read units use at least one context value (tiers F, P, Q, T, not from a
gloss): Feb 1676 322 of 384; Aug 1676 362 of 494; 6 Oct 1676 159 of 186; 13 Oct 1676 141 of 182; 3 Nov 1677 69 of 75; 17 Nov 1677 57
of 62; French copy 27 of 34; 1 Dec 1677 60 of 66; 29 Dec 1677 190 of 214; 5 Jan 1678 103 of 112. Of the cipher numbers inside the
read units, between a third and a half carry context values (Aug 1676: gloss 1,515, context 739; Feb 1676: 869 against 870). No figure
here is a gloss-only reading.

**Word layer.** The shuffle test scores letter values only. Units read through a gloss word code (tier H) are not tested by it; with
them counted not read: Aug 1676 439 of 705 = 62.27% (55 units), Feb 1676 369 of 603 = 61.19% (15); the other despatches lose 0 to 12
units (`counts.txt`). No statistical word-layer control was made.

**Controls** (`despatches/controls/shuffle.txt`, 5,000 shuffled keys, seeds 20261112 and 7, Swedish or French 4-gram model): 0 of
5,000 for every despatch's first pass and both second transcriptions. Three page tests **failed**: 165L (6 numbers; 4,843 of 5,000),
493L (40 numbers; 116 of 5,000) and 515L (49 numbers; 1 of 5,000). Short pages carry little weight either way.

**Second transcriptions** (`despatches/controls/alignment.txt`). Feb 1676 left pages, b125, decode-blind (frozen before b124's files
were opened; one exposure to b124's 162L word division after the freeze, logged): full numerals the same 428 of 440, 452 of 473,
439 of 449, 7 of 7, and 17 numerals cut in the first are full in the second. 318 (6 Oct 1676), b112, blind of b111's files by its
record: 363 of 379 and 310 of 323 the same; adjudicated against b111 before its decode, so that decode is not blind. Every other
despatch: one reader, not blind.

**Exposures logged before a freeze.** 3/13 Nov 1677: 472L lines 1-2 decoded in the head with v8 during b118's gloss check; 17/27 Nov
1677: about 12 cipher lines of 480L seen at 3000 px, not decoded; 13/23 Oct 1676: 327R lines 1-3 used as a structure test (training,
not counted); 12/22 Aug 1676: b123 had read b122's decode of 280L/R (already scored) before transcribing the rest. No key value was
taken from any of them (session logs).

**Dan's '?' rule.** Only b125's second transcription marks numerals with '?' (6 numerals); no read unit holds one, so the figure is the
same by both rules (130 of 258). The first transcriptions put doubts in the doubt notes (`doubts.md`), not inline; those are not
counted as holes.

**Stamps.** Two stamps already in this folder cover part of the addition (`despatches/STAMPS.md`): 03:53:21 GMT holds the six v6
pages of 13/23 Oct 1676 and keys v5 and v6; 06:25:27 GMT holds the five pages of 17/27 Nov 1677 and key v9. Both came after those
decodes: they fix the files, not the order. Nothing else here is stamped; freeze times and md5s are the session logs'
(`manifest.tsv`), the contributor's record only.

**Volume exhausted.** A survey of R0003797 (b118, b124, b128) found no further bare cipher in this table: the other cipher passages of
Sep-Dec 1676 and Aug-Oct 1677 carry chancery glosses; 21/31 Mar 1676 (201R-203R) uses a different code. The sister volumes are not
digitised (b130).

## Corrections to our issue figures

1. **The 358/486 = 73.66% of #453 counted 12 units as read that the frozen key does not spell.** In those units 66 decodes
   as å (its Swedish value in v3) where the French word needs y: roå, moåen, aåant, nå (three times), luå (three times),
   så, då, amploåee. The S rule (every sign gives its frozen value and the word is spelt) excludes them, and the same filing
   counted the four units where 89 gives n for French l as not read. They are downgraded to N in `overrides.tsv`; the
   transcriptions and segmentations are unchanged. Corrected: the six pages of #453 346/486 = 71.19%; the three opening
   pages unchanged at 200/278 = 71.94%; all nine 546/764 = 71.47%. The figure is 71.47%. The blind decode figure of the
   second comment (122/182) and the v2 test (44/103) are given as filed; their tallies may hold the same kind of unit.
2. **"Key from the 1675 chancery gloss" is too short.** v3 has 52 letter rows from context in image 324 (point 5 above).
   The method field of #453 said so; the title and key line did not.
3. **The memorial does not start on image 322 or 323.** It opens on f.306r (image 321R), headed "6 Oct: 1676", the enclosure
   to the despatch of 6/16 Oct 1676 (our second comment). "Autumn 1676" in the title of #453 can be 6/16 Oct 1676.
4. **S+E is not a share read.** The 98.15% of #453 counts every unit with a code, a cut numeral or a weak value as if
   placed; it shows that the decode is French throughout, nothing more. Only the strict figure is used here.
5. **The second transcription of image 324 in #453 (486 of 501 the same) was not blind.** The blind one is that of f.307v
   and f.309v in our first comment (860 of 863 full numerals the same; `second_transcription/`).
6. Code 314 (Danmarck, from the 1675 gloss) is counted not read, as filed, although its value comes from a gloss. Counting
   it read would add 2 units; not done.
7. The reading of image 324 is the b99 reading (key v2 plus context) and does not bracket its supplied letters.

Catalogue correction (row 2317), as in #453: images 107-109 are the cipher tail of the despatch of 11/21 Nov 1675, already
deciphered in the 1675 gloss on images 102-106 (control in step 2). Image 109 and 112L assumed by analogy, not tested.

## What the memorial says

The envoys thank Louis XIV for his declaration of war on Denmark under the guarantee of the Northern treaties and for
Pomponne's assurance that France will not abandon Charles XI, and report the victory near Halmstad and the raising of the
siege of Bohus. In cipher and clear together they press him: the allies, having lost hope of retaking what France has won,
will throw their weight on Sweden; let him turn his arms on Denmark and send troops and ships as the treaty provides. As
Pomponne has said that is impossible, let him ready a squadron for the start of spring 1677 to reach Gothenburg and join the
ten ships there, and keep it secret. The allies will make no peace until France returns its conquests, count on taking
Pomerania, and court Bavaria, Hanover, Denmark and Holland. If France makes peace, it should be on a condition that puts
Charles XI back in possession of his places. Charles XI cannot meet the cost from his ruined provinces and the ordinary
subsidy: let France grant an extraordinary sum, part to buy provisions and munitions in England and Holland for Stralsund
and Gothenburg, part for Pomerania, and win Hamburg to the cause with freedom of trade.

French with holes: `readings/memorial_1676-10-06.md`. English: `translations/memorial_1676-10-06.md`.

## Checks

All re-run for this folder with `python3 -I` (standard library):

- `scripts/build.py`: decodes every transcription with `key.tsv` (checks its md5), checks that each segmentation rebuilds
  the decode letter for letter, classes each unit and writes `decryptions/`, `units.tsv`, `counts.txt`, `holes.md`. The nine
  decryptions are byte-identical to the decode files of the sessions (b101, b104), and the image-324 v2 decode to b99's.
  Every filed count reproduces (358/486, 200/278, 44/103, blind 122/182 against 123/182).
- `scripts/compare_blind.py`: blind against first transcription of f.307v and f.309v: 860 of 863 full numerals the same
  (478/480, 382/383); the three differences are those of our first comment (two blind errors, one unsettled).
- `scripts/run_controls.py <French corpus>`: 5,000 shuffled keys per test, seeds 20261112 and 7, French character 4-gram
  model from four Project Gutenberg texts (`controls/CORPUS.txt`), each asserted to carry "Language: French". Every filed
  line reproduces to four decimals. Results (`controls/shuffle.txt`): 0 of 5,000 on every page; the six #453 pages
  pooled, true -2.1459, best shuffle -4.6356 (seed 20261112), -4.6830 (seed 7); the three opening pages -2.1681 against
  -4.5716 and -4.5828; all nine -2.1534 against -4.6480 and -4.5698; the v2 test on image 324 -2.2969 against -4.3049
  and -4.2634; the blind transcription -2.1213 against -4.5915.
- The repository's checker scripts were not run by us (we treat downloaded repositories as data). The checks they make
  were verified by hand against the schema and CONTRIBUTING; see the pull request text.

## Remaining gaps

- Word codes 240, 245, 267, 324, 463 (one unit each) and 314 (two units) - blocker: open-codes; senses from context only (267 alliance, 324 discours, 463 reputation?)
- Seventeen numbers with no value in v3, values proposed after the decodes (99 st, 44 x, 109 ff, 120 q, 129 y ...; `holes.md` 2) - blocker: no-key-material; testing them needs fresh text in this table, and the volume's bare French cipher is used up
- Numerals cut at the gutter: 68 units hold one - blocker: illegible; lost in the binding
- Probable nulls 173-178, 3, 4, 8 - blocker: no-key-material
- Trolle-Bonde D.1 (1910), Höjer 1875, Grauers 1926 and the French side (AAE) not seen - blocker: needs-physical-access
- Despatch of 1677: word codes 418 (twice, "<418>en") and 435 (once); v10, made later from glosses, gives 418 = march and 435 = Preussen, not used - blocker: open-codes
- Despatch of 1677: "illa", "inställa" (spelt short by the key), "Paez" (46 a weak value), counted not read - blocker: open-codes
- Despatch of 1677: 30 word units only - blocker: too-short
- Despatches 1676-1678 (`despatches/`): word codes with no value in the key state used (331, 348, 358, 418, 435, 441 under v9; 174, 175, 179, 355, 400, 470 and others under v10) - blocker: open-codes
- Despatch of 12/22 Feb 1676: line ends of the left pages lost in the gutter - blocker: illegible; a decode-blind second transcription recovered 17 numerals, the rest are lost in the binding
- Despatches of 3/13 Nov, 17/27 Nov and 1/11 Dec 1677 and the French copy of 24 Nov/4 Dec 1677: 131, 100, 104 and 70 word units - blocker: too-short; shuffle tests failed on pages 165L, 493L and 515L
- Despatches of 6/16 and 13/23 Oct 1676: holes in most sentences under keys v4-v8 - blocker: no-key-material; every bare page of the volume has been decoded once and the sister volumes are not digitised (integration note, 13 Nov 2026: the volume's chancery glosses of Sep 1676-Jan 1678 were harvested only in part for v8-v10, about twenty glossed images; more gloss values could be taken, but any new decode of these pages would be a re-score, not a held-out test, so the frozen first pass stays the figure)
- Höjer 1875, Trolle-Bonde D.1, Grauers 1926 and AAE Correspondance politique Suède 1676-78 for the despatches - blocker: needs-physical-access; the 12/22 Aug 1676 despatch is NOT FIRST (Wimarson II)

Not gaps in the unread cipher, but limits of the evidence: no person has compared any transcription with the images (the
contributor's second transcriptions and the integration sample are by AI agents); image 324 is in-sample for v3 and its
reading is the first-test reading under v2; the clear text of 488R-490L is transcribed only next to the cipher runs.

## Prior art (checked 12 Nov 2026): priority not established

- Not found in: LIBRIS; archive.org metadata and full text (32 phrase queries, clear and decoded); Google Books feed;
  Runeberg; Litteraturbanken; Recueil des instructions II, Suède (Geffroy 1885), full text; Varenius' review of
  Trolle-Bonde D.2 (Historisk tidskrift 1901); Wimarson, "En ifrågasatt diversion mot Danmark 1676-1677" (Historisk
  tidskrift 1903), who used this volume and paraphrases a different Bonde memorial (1/11 Jan 1677); Wimarson, Sveriges
  krig i Tyskland II, complete OCR (432 pages): he cites Bonde's despatches of July-August 1676 and none of 6/16 Oct 1676.
- NOT seen: Carl Trolle-Bonde, Anteckningar om Bondesläkten: Kongliga rådet och ambassadören grefve Carl Bonde, D.1 (Lund
  1910, 150 copies), reported in library notes to print Bonde letters of 1676; no online copy (HathiTrust bot check not bypassed). Archives des
  Affaires étrangères, Correspondance politique, Suède 1676, where the memorial as handed to the French court may be in
  clear. Either could hold the text.
- Wimarson (Sveriges krig II, p. 6 n.) notes that some of Horn's ciphered letters of autumn 1675 were left wholly
  undeciphered. Our inference: historians used this volume from its clear text and glosses.

## Integration check (12 Nov 2026)

By an AI agent for the maintainer, not a person. Reproduced with `python3 -I` from the folders: `scripts/build.py` in both
(546/764, 24/30, every filed figure), `compare_blind.py` (860 of 863 and 168 of 169), shuffle outputs. An own decoder written
from `key.tsv` alone decodes all 284 cipher lines of the nine held-out memorial pages and of 489R identically to the
contributor's decryptions. On the Riksarkivet images (IIIF `full/max` via curl; region requests return 501, so crops are made
locally) about 400 groups were compared: all 17 runs of 489R, f.307r lines 1-6 and 18-22, f.309v lines 4-12: 0 disagreements.
Not sampled: the other seven memorial pages and image 324. On the nine held-out pages 94.7% of cipher numbers (3,407 of
3,599) carry a letter value, of which 56.5% come from the gloss (tiers A, B) and 43.5% from context (F, P).

The one external time fact: an RFC 3161 stamp of 02:54:07 GMT 12 Nov 2026 covers a file byte-identical to key v3 (md5 8e1d93d1),
before any stamp that holds a held-out page (03:10:20, 03:53:21). Everything else about the order of events (that pages were
transcribed after the key, decoded once; key v9 and the 489R transcription before the decode, the stamp of 06:25:27 being after
it; the blind transcriptions) is by the contributor's record.

The first test of the memorial (key v2 on 30 lines of image 324) **failed** the contributor's own bar: 44 of 103 = 42.72%
strict against the 65% set beforehand. Key v3 was then made with 23 more values read off those very lines, so image 324 is
in-sample for v3 and carries no count. The result of v3 is the nine held-out pages, 546 of 764 = 71.47%.

Catalogue 2317 narrowed (not removed): images 327-330 (the Swedish letter with Lillieroot), 114 left (a different code) and
other bare leaves remain unread.

## Integration check of PR #525 (13 Nov 2026): the ten despatches

By an AI agent for the maintainer, not a person. PR #525 adds `despatches/` (134 files), `timestamps/pr_folder/` and the section
"Key states v4 to v10" above; nothing outside this folder.

- Reproduced: `despatches/scripts/build.py` and `compare_second.py`, run with `python3 -I` from this folder, pass every md5,
  decode and tally assertion and rewrite `counts.txt`, `units.tsv`, `decryptions/`, `readings/` and `controls/alignment.txt`
  byte-identically (no change in git). Every per-despatch figure in the table above is the script's. `run_controls.py` was
  read, not re-run (it needs the contributor's Gutenberg corpus folders, not in the PR).
- Own decoder: written here from `despatches/keys/KEY_v10.tsv` alone (not importing theirs), on the first-pass transcriptions of
  12/22 Feb 1676 (8 pages) and 12/22 Aug 1676 (9 pages): all 17 pages decode letter for letter as the contributor's decryptions.
- Images: Riksarkivet IIIF `full/max` (curl; crops made locally). Image 279R lines 1-13, 20 and 28: 222 of 222 groups as
  transcribed. Image 163L lines 1-9 (a gutter page): 153 groups, 151 as transcribed; R2 group 12 is 89 on the image (first
  transcription 59), R7 group 15 is 136 (first transcription 130, flagged in `doubts.md`); the decode-blind second transcription
  b125 has both as read here. The numerals marked `~` run into the binding on the image, as stated. 375 groups in all, 373 agree.
  Not sampled: the other 17 pages of these two despatches and all pages of the other eight.
- Strict rule: the class S of `build.py` is the README read bar (any unvalued number, cut numeral, weak value or flagged
  emendation makes a hole); the contributor counted strictly, so the figures stand. The reading of 12/22 Aug 1676 was read here as
  Swedish sentences against the translation (subsidy talks with Pomponne, the Feuquières orders, peace terms): it reads, with holes
  in place. 494 of 705 = 70.07%: read in part. The other nine are under the contributor's 65% line: decoded, not read.
- Key timing: by the manifest, v10 (07:22:14 UTC) precedes every first-pass transcription freeze of Feb and Aug 1676 (07:27:55 on);
  v7 and v8 precede their 6 Oct pages; v9 precedes the Nov 1677-Jan 1678 freezes. The freeze times of 327R and 328L lines 1-13 equal
  the freeze times of v4 and v5 to the second (the session logged one time for both). All by the contributor's record; the two
  stamps in `despatches/STAMPS.md` and the PR-folder stamp (13 Nov 2026 10:28:57 GMT) came after the decodes.
- Selective filing: every page of each of the ten despatches is filed, including the nine under 65%; the earlier unfiled despatches
  (17/27 Nov and 3/13 Nov 1677) are now in. That no other bare passage of this table remains in R0003797 is the contributor's survey
  (b118, b124, b128), not re-checked here; image 112L is the 1675 tail (glossed context), 114L another code.
- Prior art: Wimarson, Sveriges krig i Tyskland, is not on archive.org; HathiTrust answered 403 (bot check, not bypassed) and
  Google Books returned nothing. The NOT FIRST verdict for 12/22 Aug 1676 and the negative result for the other nine are the
  contributor's (KB OCR), not re-checked here.
- Weight: in every despatch most read units use at least one context value (counts above); for 12/22 Feb and 12/22 Aug 1676 key
  v10's word codes were read off glosses of January 1678 and applied eighteen months earlier, and 144 = b (1678 gloss) fits Aug 1676
  badly ("ansenbig"). Three page tests failed (165L, 493L, 515L), published as failed.
- No change to the memorial's figure or to `fraction_read` (0.718); the despatches are not pooled with it.

## Escalation
- [x] siblings: the neighbouring leaves of R0003797 opened; 107-109 are the cipher tail of the 1675 despatch (glossed on 105-106); the 1677 despatch of 17/27 Nov (479R-481R) decoded at 62%, and 327-330 (the Swedish letter with Lillieroot, 13/23 Oct 1676) decoded under keys v4-v6: both now in `despatches/` (13 Nov 2026), below our 65% line
- [x] clear-pages: the clear Swedish and French between the cipher runs read and used as context
- [x] known-keys: no other Swedish 1670s table is known to this repository; the glosses of the volume are the key source
- [x] print: LIBRIS, archive.org full text, Runeberg, Wimarson I-III, Varenius, Recueil des instructions: nothing on these two texts; Trolle-Bonde D.1, Hojer 1875, Grauers 1926 not seen
- [x] key-rebuild: key v3 from the 1675 gloss, v4-v10 from glosses and context (v10 for the 1676 and 1677-78 despatches in `despatches/`); further values proposed after the decodes are not counted
- [n/a] retry: a rerun of the memorial with v9 was not made; v3 is the frozen test, and values proposed after it are listed in holes.md

## Files

- `despatches/` (added 13 Nov 2026): ten despatches of 1676-1678 read with key states v3-v10, one folder per despatch
  (`transcriptions/` frozen page files; `segmentation.txt` and `doubts.md` as md5-checked blocks), `manifest.tsv`, `keys/`
  (KEY_v10 and LINEAGE.md), `decryptions/`, `readings/`, `translations/` (AI-made), `units.tsv`, `counts.txt`, `controls/`
  (shuffle, alignment, corpus list), `PRIOR_ART.md`, `scripts/` (`build.py`, `run_controls.py`, `compare_second.py`; standard
  library, `python3 -I`, run from the target folder).

- `transcriptions/`: eleven files, the frozen transcriptions unchanged (byte-identical to the stamped files). Numbers as
  written; "..." = clear words; `~` = numeral cut at the gutter.
- `segmentation/`: the reader's word division of each decode (`decoded=reading`, `!E`/`!N` flags), frozen with the decode;
  the hand-classed units of the v2 test.
- `key.tsv` (v3, byte-identical to the frozen file); `overrides.tsv` (12 downgrades); `gloss/` (102R gloss lines, EM
  output, the 107L control, keys v1 and v2).
- `decryptions/`, `units.tsv`, `counts.txt`, `holes.md`: written by `scripts/build.py`.
- `readings/`, `translations/`.
- `second_transcription/`: b103 blind transcription of f.307v and f.309v (as written and in R-format), its segmentation
  and freeze record; b101 second transcription of the image-324 test lines and its comparison.
- `controls/`: shuffle output, blind comparison, the corpus list.
- `scripts/`: `build.py`, `shuffle_control.py`, `run_controls.py`, `compare_blind.py`; `original/` the session scripts
  they reproduce.
- `timestamps/`: three stamps of 12 Nov 2026 with a selection of the stamped files (`timestamps/README.md`).

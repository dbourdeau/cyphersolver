# Bonde and Lillieroot to Louis XIV, 6/16 Oct 1676: the ciphered French memorial (Riksarkivet, Diplomatica Gallica; catalogue 2317)

Status: read in part, contributed. No claim of a first reading (see Prior art).

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

Key lineage: `targets/bonde1677` reads a Swedish despatch of Nov/Dec 1677 with key v9 (md5 af29e81f). v9 is a later state of
this same key: v3, then v4-v7 (values from context in the 1676 despatches and the post-hoc values of this memorial),
v8-v9 (values from chancery glosses of 1676-1677), with 131 changed from q to r. v9 was made for Swedish text; this French
memorial is read with v3 only, and no v4-v10 value is used here.

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

- Word codes 240, 245, 267, 324, 463 (one unit each) and 314 (two units) - blocker: open-codes; senses from context only
  (267 alliance, 324 discours, 463 reputation?)
- Seventeen numbers with no value in v3, values proposed after the decodes (99 st, 44 x, 109 ff, 120 q, 129 y ...;
  `holes.md` 2) - blocker: no-key-material; testing them needs fresh text in this table, and the volume's bare French
  cipher is used up
- Numerals cut at the gutter: 68 units hold one - blocker: illegible; lost in the binding
- Probable nulls 173-178, 3, 4, 8 - blocker: no-key-material
- Image 324: in-sample for v3; reading is b99's under v2 - blocker: not-attempted
- No person has compared any transcription with the images; all checks are by model sessions - blocker: not-attempted
- Trolle-Bonde D.1 (1910) and the French side (AAE) not seen - blocker: needs-physical-access

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

## Files

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

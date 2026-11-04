# Catalogue 1771: Höpken and Carlson, Constantinople, to the King of Sweden, 1739-41

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/21 (R0003582, 568 images). Work of 3 Nov 2026, contributed by
WAINUT. Scope was deliberately narrow: four images with interlinear French (255, 256, 257, 260) and one bare cipher
postscript (263), out of a volume with well over a hundred pages of numbers.

## Outcome

| Document | Images | Cipher words | Status |
|---|---|---|---|
| Enclosure to the despatch of 2/13 Dec. 1739: a conversation, speakers A [1440] and B [1529] | 255-257 (left) | 234 | **Read in part**, through the contemporary gloss. Confirmed key values give 143 words (61%), single/mixed values 41 (18%); 50 (21%) rest on the gloss alone |
| Second enclosure, same date ("N 2") | 257 (right, top) | 14 | Read in part; 4 runs only. Confirmed 5 (36%), single/mixed 2 (14%), gloss alone 7 (50%) |
| Conversation report, 1740 (the **held-out** passage) | 260 (left) | 68 | Read in part. Held-out result (frozen key): 111 of 164 groups match the gloss; shuffled maximum 36. Word counts with the final key, which was trained on this page too (so NOT held-out): confirmed 38 (56%), single/mixed 6 (9%), gloss alone 24 (35%) |
| Cipher postscript "P.S. 4 Dec." to a Swedish despatch received 20 Feb. 1740 | 263 | 55 groups | **Decoded, not read** (15 groups not in the key) |

All glossed runs together: 316 words; 186 (58.9%) from confirmed key values, 49 (15.5%) on single or mixed values, 81
(25.6%) on the gloss alone (counts after the clean-up of 3 Nov, see the last section). Volume status: **read in part**. Nothing here is a break of a bare despatch: the readable text is what the chancery
decipherer wrote over the numbers. The value of this work is the rebuilt code list (184 groups), the held-out test that shows
it is real, and the transcriptions. The 95% bar is met for the glossed runs only because the gloss covers them; it is not met
from the key alone.

## The system

A two-part numerical code of four-digit groups, all seen between 1000 and 1749. It is mainly a syllabary (letters and
syllables: 1020 de, 1267 la, 1501 s, 1062 r, 1152 ne, 1232 tion, 1512 go, 1368 ti, 1673 et, 1652 en, 1712 re, ...) with code
words for names (1217 Russie, 1532 Suède, 1104 Grand Vizir, 1280 l'Empereur, 1584 traité, 1684 alliance). u and v are one
element (1618 = av / au). The code is written with commas between groups, and in the glossed copies the decipherer struck the
groups through and wrote the French above. The margin tags "A 1440" and "B 1529" mark the speakers of a written-out
dialogue; they are code groups that were never glossed. From what B says on 257 ("Vous avez tort d'appeller la paix avec la
Russie mon ouvrage ... La paix avec l'Empereur étoit déjà conclue sans qu'il fût stipulé de la Russie"), B is very probably
the French ambassador Villeneuve, mediator of the Belgrade peace of 1739; A is the Swedish side. That identification is ours,
from content only.

## Transcription

Sign first, two passes: pass 1 by the solver from crops of the full-size images (pairs_pass1.tsv); pass 2 by a second AI
language-model agent instructed to read only the digits and ignore the French (pass2_digits.txt, pass2_heldout.txt).
Honest caveat: in pass 1 the French was in view, because it is written directly over the numbers. That is why pass 2 was
kept blind. Disagreements were settled on full-size crops (scripts/montage.py): 9 in the key pages; on image 260, 4 digit disagreements
(pass 2 also left out 4 groups it judged unstruck; they are kept), none on 263. One pass-1 reading on 260 was wrong in the direction of a value seen earlier (1504 for 1604); pass 2 was right. In
260 h11 pass 1 had 1501 and pass 2 had 1601; the independent verifier could not settle it on 4x crops, and neither could
we (the second digit has a bowl and a rising stem; the 5s of the next group, 1551, look much the same). It is kept as
"1601?"; both values = s, so the decryption does not change. Seven groups stay doubtful and carry "?" in the
transcriptions (1416?, 1725?, 1624? on 256; 1223? on 257; 1000?, 1222? and 1601? on 260). No digit was changed toward the gloss.

## Key: how it was obtained, and the held-out test

1. Pairs: each maximal run of groups between clear words, paired with the French over it (pairs.tsv; use K = key
   building, X = left out because the gloss was corrected, blotted or incomplete).
2. scripts/build_key.py: hard-EM segmentation. Each group must account for a contiguous piece of the French (accents and
   apostrophes dropped). It alternates best segmentation and recounting. A flat start collapses, so it starts from 74 seed
   values read by eye (seeds.tsv; 4 more, 1199 1551 1177 1601, were added after the held-out test for the final key). Seeds count as one pseudo-count and the pairs can overrule them.
3. The key from images 255-257 was **frozen** (key_frozen_heldout_test.tsv; sha256 in FROZEN.sha256) before image 260
   was transcribed.
4. Held-out test (scripts/heldout_test.py on heldout.tsv, image 260, 14 runs, 164 groups): 138 groups (84%) were in the
   frozen key, and **111 (68% of all, 80% of those known) decoded to exactly the letters of the gloss at their place**.
   With the same key's values shuffled among its groups, the score was a mean of 25.5 and a maximum of 36 over 500
   shuffles. The code list is real.
5. Final key.tsv: the EM run on all pairs (key building + held-out), plus 9 code words set by hand (key_overrides.tsv).
   Ten EM values that cross a word or syllable boundary were demoted on 3 Nov (key_demoted.tsv: 1481 suedeest, 1573
   itombra, 1474 damit, 1507 xpu, 1097 ppor, 1621 iho, 1106 epe, 1240 ommo, 1467 tba, 1415 eu/xmemes/entame). They stay
   in key.tsv as "unresolved" with value [?], and decode.py treats them as not in the key.
   Status now: 85 confirmed (two or more places, at least 2/3 agreeing), 18 mixed, 62 single, 9 code words, 10 unresolved. Only the
   "confirmed" values are firm. Single values are fixed by one gloss; mixed ones show real conflicts (e.g. 1474 is "mi" in
   "amitié" twice but cannot be in "fait" or "ombrage"). Either the decipherer's glosses are loose there, or the code has
   homophones we cannot yet separate.
6. The word counts for 260 come from the final key, which was trained on 260 as well; they are not held-out figures. Run
   against the final key, the held-out script scores 140/164 on 260, which is circular. The only held-out figure is the
   frozen-key one in point 4. (The frozen key also had 1199 = "rain", an EM artefact; the seed 1199 = "in" was added
   only after the test.)

## Reading and the mark check

reading_<doc>.md gives, per run, the contemporary French with every place where the key does not give that text marked in
place: `[1234 ?text]` (the text rests on the gloss) or `[1234 -]` (a key value with no counterpart in the gloss). Each reading
opens with the passage in context (clear text plus cipher) in French and English. scripts/check_marks.py rebuilds the
decryption from transcription and key, walks every reading letter by letter against the key values, and fails on any
unmarked departure. It passes ("OK: no unmarked departure") and prints the word counts above. The marks are placed by make_reading.py, not
by hand. Limitation: the text inside a mark is never checked against anything; a mark only moves its words to the
"gloss" count. Rebuild, from this folder:

    python scripts/make_key.py
    python scripts/decode.py
    python scripts/make_reading.py
    python scripts/check_marks.py
    python scripts/heldout_test.py key_frozen_heldout_test.tsv heldout.tsv

(heldout_test.py needs both arguments; with them it prints 138/164 in the frozen key, 111 matching the gloss, shuffled
mean 25.5, maximum 36.)

## Remaining gaps

- Only 4 glossed images were used. The glossed despatches at 258, 259 and 261 (and around 322-327) would confirm most of
  the 66 single values and settle the mixed ones. They were not transcribed (tool budget).
- The bare cipher pages (for example 264-266, 115-196, 389-470) are untouched. With 85 confirmed values and a syllabary of
  probably about 750 elements, expect partial readings at best until more glossed pages are added.
- Postscript 263: decoded (with the final key.tsv), not read. 15 of 55 groups are unknown; the language is unsettled
  (the clear Swedish word "angående" stands in the postscript). A small superscript "o" over the second digit of 1363
  (p02) is recorded in bare_263.tsv; its meaning is unknown.
- 255 r05: the gloss leaves a blank after "une" ("une [ ] à la fois"). 256 r13 and r16: the gloss has blots. 256 r22,
  257 r37, r39, r41, r47, r49: the gloss was corrected or the article is implicit. These runs were kept out of the key
  building (X).
- The 257 left-page dialogue breaks off ("Celle-ci fait ..."); its continuation was not located.
- The speaker tags 1440 and 1529 are not decoded; B = Villeneuve is a proposal from the content.

## Catalogue 1772/1773 (Dorffler, Poland)

Not worked. Their catalogue descriptions give 2-3 digit numbers up to about 320, which is not this 4-digit code. They do not
share this key.

## Collision check and prior art (3 Nov 2026)

- Dan's repo (origin/main, head d803a1d8d) has no target or notes claiming Höpken, Carlson or R0003582 beyond the
  catalogue entry and the Riksarkivet volume-sweep README. Open PRs #201, #216 and #227 are unrelated. Issue #208 (Brice
  Dudout) concerns Celsing keys and the Turcica volumes I/11/43-45 of 1763-66, not this volume.
- One web search (Höpken, Carlson, Villeneuve, Constantinople 1739, cipher) found background only: Höpken was envoy in
  Constantinople from 1738, where the Swedish-Ottoman defensive alliance was concluded, and Villeneuve was the mediator at
  Belgrade in 1739. It found no edition or decipherment of these despatches. A 2021 paper by C. Görür on the
  Ottoman-Swedish alliance (1718-1740) was seen only as a citation. The scout round's search ("Höpken-Carlson 1739
  cipher") also found nothing.

## Image sources

IIIF manifest https://lbiiif.riksarkivet.se/arkis!R0003582/manifest ; images via
https://lbiiif.riksarkivet.se/v3/arkis!R0003582_00NNN/full/max/0/default.jpg (NNN = 255-261, 263; thumbnails 255-266 and
320-328). Viewer: https://sok.riksarkivet.se/bildvisning/R0003582_00255 (and _00256, _00257, _00260, _00263). Fetched one at a
time, 1.2 s apart, User-Agent "WAINUT-research" (scripts/fetch.py); no 429 and no bot check. Scans are kept in scans/, which is
not for git.

## Files

transcription_*.txt, decryption_*.txt, reading_*.md (four documents); key.tsv (final), key_frozen_heldout_test.tsv (the
frozen key used for the test), key_em.tsv, key_overrides.tsv, key_demoted.tsv (EM fillers taken out of the key), seeds.tsv; pairs.tsv, heldout.tsv, bare_263.tsv (settled
digits), pairs_pass1.tsv, pass2_*.txt (the two passes); translations.tsv; contexts/; scripts/ (fetch, crop, sheet, montage,
compare_passes, build_key, make_key, heldout_test, decode, make_reading, check_marks). The key, decode, reading,
check and held-out scripts use the Python standard library only; crop, sheet and montage need Pillow and local scans,
which are not part of the folder. VERIFY.md is the independent verification; profile.json the fixed-field record.

## Changes after the independent verification (3 Nov 2026)

The verifier (VERIFY.md; the report is unchanged except that one phrase in its section 6, listing internal search
terms, was shortened before submission) returned "fix". All seven points were applied; we disagree with none.

1. The ten word-crossing EM values were demoted (key_demoted.tsv, make_key.py, decode.py). The readings were regenerated.
2. 260 h04: 1532 = Suède now aligns as `[1532 ?la Suede]` (the gloss adds the article; the code word itself matches),
   not `[1532 -]`. To get this, make_reading.py now breaks ties between equal-cost alignments in favour of a mark whose
   span still contains the group's own value. 1481 is marked `[1481 ?st]`.
3. The 260 word counts are stated as non-held-out (Key, point 6); the held-out result is the frozen-key one only.
4. 260 h11 group 13 is "1601?" (checked on a 3x crop: the image does not decide; both values = s). The old line that
   called 1501 a pass-1 error was corrected.
5. reading_ps_img263.md now says "final key.tsv"; the superscript "o" over 1363 was confirmed on a crop and recorded.
6. The rebuild instructions now include make_key.py and the held-out command with its two arguments.
7. The PR text describes the readings as transcriptions of the contemporary decipherment.

Word counting. check_marks.py used to count a mark that spans several gloss words (e.g. `[1415 ?eux mêmes]` in 256 r21) as one
word. It now counts each gloss word in a mark. With the old key and the new counter the totals are 316 words: 185 confirmed,
56 single/mixed, 75 gloss. With the cleaned key: 186 confirmed (58.9%), 49 single/mixed (15.5%), 81 gloss (25.6%). The
verifier's 305 words / 61% / 19% / 20% were measured with the old counter and the old key; the share from confirmed values
moved from 61% to 59% only because the word total is now counted correctly.

Candidate for later: on the 260 right page (not transcribed as runs) "entamé nos" stands over 1652 1115 1415 1121 1089,
which suggests 1415 = me. Not used.

# Catalogue 2244 (Höpken-Carlson volume, Constantinople, 1742): the Khan of Crimea's letter to the King of Sweden, in the second Höpken code

Work of 12 Nov 2026 by AI language-model agents (no human palaeographer), contributed by WAINUT. Proposed state: **read**
(contemporary French gloss, checked group by group against the frozen hopken1740 key). The key alone reads 205 of the
256 cipher words verbatim (80.1%), or 228 (89.1%) with marked repairs. If the read bar is counted on the key alone, the
state is **read in part**. Proposed folder name `hopken1742`. It applies `targets/hopken1740/key_1741.tsv` byte for byte,
so it could instead be folded into `targets/hopken1740` (one key, one entry), as was done with hopken1741a and
hopken1741b. Like Lit. A of 1741 there, it is a contemporary decipherment checked against the key; the bare cipher runs
of the volume are not touched, so catalogue 2244 is not closed by it.

Status: in progress (not yet written up). This document is read; the rest of catalogue 2244 (bare runs, other glossed
passages, image 482 in another code) is not part of this target and was not worked (see "Not part of this target").

## Document

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/9/28, "Brev till kanslipresidenten, 1742" (image series R0003637,
567 images). Images 227, 228 (an opened leaf, two pages on one image) and 229 hold one document. It is headed "Lit: A.
Extrait de la Traduction de la Lettre du Chan de Crimée à Sa Majesté le Roy de Suede" and endorsed "Bil. till Carlsons
desp. till Kanslipr. d. 10/21 Maj 1742". It has 614 code groups (161 distinct) in 60 cipher rows, with clear French
phrases between them; 602 of the groups stand under the gloss (row B07, 12 groups, has none). A contemporary hand
struck the groups through and wrote the French over them. The extract ends "au commencement du mois de mai 1742".

The letter: the Khan writes to the King of Sweden after his own arrival at the Porte. He explains that the
Swedish-Ottoman defensive alliance has not been carried out only because the Porte has to fortify its frontier with
Persia. Aid promised to friends depends on circumstances, so aid to Sweden is difficult. But the Ottoman Empire values
Sweden's friendship and will give "tout le secours qui peut dépendre d'elle dans les circonstances présentes". This is
probably the Ottoman answer to the Swedish hope of Ottoman help in the war with Russia of 1741-43 (inferred from the
date and the sense; the letter names no war).

Images: https://sok.riksarkivet.se/bildvisning/R0003637_00227 , `_00228` , `_00229` (IIIF
`https://lbiiif.riksarkivet.se/v3/arkis!R0003637_00227/full/max/0/default.jpg`). No scans are in the files for git.

## System and key source

The second Höpken-Carlson code of `targets/hopken1740`: four-digit groups 1006-1915, a syllabary with word codes
(1516 ottporten = Porte, 1360 tractat = traité, 1450 alliance, 1265 swerige = Suède, 1430 minister). The key used is
`key_frozen.tsv` = `targets/hopken1740/key_1741.tsv` on origin/main, byte for byte (sha256 865cbb5e...2d7e, in
FROZEN.sha256; rechecked against origin/main 65cdcd9d5 on 13 Nov 2026). It has 352 entries (353 lines with the header:
235 confirmed, 76 single, 24 gloss_1741a, 15 mixed, 2 changed_1741a). It was frozen before any group of these pages was
decrypted. Two groups above 1900 occur here: 1903 (Perse) and 1913 (Chan). They are word codes, like 1902 Tessin and
1915 Reis Effendi in the 1740 key. Of the document's 161 distinct groups, 135 are in the frozen key (584 of the 614
occurrences).

## Transcription

- SIGN_CONVENTIONS.md was written first. Pass 1 used bands at 0.72-0.8x of the full-size image. Pass 2 used fresh
  half-width crops at 1.4-1.5x, with 3x zooms on doubtful groups. Both passes are digits only. The gloss was in view (it
  is written between the rows), but it was read afterwards into gloss_khan1742.tsv, before any decryption. One agent made
  both passes, so they are not fully independent.
- Images 227 and 229: the digit disagreements and doubts between the passes were settled on the image
  (transcription_khan1742_blind.txt).
- **Pass 3 (after the first decryption).** On 227 and 229 the decryption broke at one recurring shape. In this hand 8 is
  often written with an open, z-like top and a looped foot, so it looks like a looped 2. Every group whose value broke
  the sense was looked at again on 1.6x row crops. 23 groups were re-read as 8 (22 as 2 -> 8, one as 7 -> 8); the list
  is in the header of transcription_khan1742.txt. 22 of the 256 cipher words rest on one of these re-reads. The rule was
  then added to SIGN_CONVENTIONS.md before image 228 was transcribed, and both passes of 228 applied it from the start.
- Doubtful digits are kept with `?` (14 cipher words contain one).

## Held-out test (scripts/heldout.py)

The frozen key is tested against the contemporary gloss. Each run (the cipher between two clear phrases) is aligned to
its gloss by dynamic programming. The test uses the **key-blind** transcription (transcription_khan1742_blind.txt):

- All three images: **487 of the 602 glossed groups (81%) give exactly the letters of the gloss at their place. 554 of
  those groups are in the key, so 88% of those known.** With the key's values shuffled (300 shuffles): mean 63.2,
  maximum 103.
- Images 227 and 229 only (transcribed before the 8 rule): 214 of 282 (76%; 86% of those in the key); shuffled mean 29.0,
  maximum 50. A first run with one gloss run per row gave 156 of 274 (57%). The gloss lines do not break where the cipher
  rows break, so that run split words; the span runs replaced it.
- On the pass-3 transcription the same test gives 507 of 602 (84%). That figure is not held out.

This is the second held-out test of this key outside volume I/9/21, in another year and volume. The first was Lit. A of
1741 (222 of 282).

Statistical validation (docs/_validate.py, 13 Nov 2026) of the mechanical text with the frozen key
(scripts/validation_pairs_1742.py writes validation.tsv; the 30 occurrences of groups not in the frozen key are left
out): 584 tokens, 135 types, fr-1600-letters order 4, reading -2.075 per letter; random keys -3.633 (z 13.0); key
annealed onto shuffled ciphertext best -2.453; verdict pass.

## Reading

- decryption_khan1742.txt: mechanical decryption (scripts/decrypt.py).
- marked_khan1742.txt: every departure is marked. scripts/check_marks.py passes, and it fails on a tampered file (tested).
- reading_khan1742.md (French), translation_khan1742.md (English), about_reading_khan1742.txt (notes where the cipher and
  the gloss differ).

Counts (scripts/check_marks.py, strict, re-run 13 Nov 2026): **256 cipher words. 205 are read verbatim from the key
(80.1%), 23 carry a marked repair, 28 come from the gloss only (groups not in the frozen key), 0 are holes.** Verbatim
plus repaired is 228 (89.1%). Clear words between the groups are not counted. One cipher row has no gloss (image 229,
B07, "dans les circonstances présentes"), nor do a few stretches where the glossing hand drew only a line; these are
read from the key alone.

Dan's reading checker (docs/_check_reading.py, origin/main 65cdcd9d5): reading_khan1742.md has a **clean share of
0.900** (27 of 30 sentences). The other three fail only on period spellings ("délays", "provenoit", "conditionel") and
on the `{+t}` marks. translation_khan1742.md scores 0.912. decryption_khan1742.txt scores 0.091, as expected for
syllable pieces.

The working key `key.tsv` has 373 entries (374 lines with the header): the 352 of the frozen key plus 21 values from
this gloss (status gloss_1742: 1913 Chan, 1903 Perse, 1121 cri, 1428 mée, 1628 roy, 1126 quo, 1286 Sa, 1336 sçau,
1239 vra, 1029 gu, 1564 ance, 1638 ns, 1727 ap, 1605 où, 1816 vent, 1522 t, 1407 faire, 1762 pa, 1174 mo, 1261 de,
1281 de) and one correction (1324 pp -> et, at four places; it was a single value).

## Independent review (12 Nov 2026)

An AI language-model agent that took no part in the solve reviewed the folder blind. Before opening the transcription
it cropped 8 cipher rows from the full-size scans at 1.3-2x and copied the digits itself: A05, A06, A09, A13 (image
227), C13, D11 (image 228), B06, B12 (image 229), 96 groups in all. Every group agrees with transcription_khan1742.txt.
The one ambiguity it met is the one documented above: the looped 8 (for example 1870 and 1158 in A05, 1678 in A06,
1826 in D11), which on its own shape it could not always tell from a looped 2; it judged the pass-3 re-reads plausible
but key-assisted. It confirmed FROZEN.sha256 against origin/main, re-ran decrypt.py (identical output), check_marks.py
(same counts, no unmarked departure) and heldout.py on the key-blind file (487 of 602; 100 shuffles, mean 62.8,
maximum 103), and found no reference to R0003637, the Khan or Crimea in targets/hopken1740. It read
reading_khan1742.md as French sentences against the translation: all five paragraphs hold, with no holes. Grade
**A**, state read (recorded as `reading_review` in profile.json). It raised no digit correction, so the transcription,
decryption and reading are unchanged; its caveats are under Remaining gaps.

## Remaining gaps

- 14 repairs against confirmed key values are not settled - blocker: open-codes. Some are probably misread digits:
  1270 el for "fâ" (1870 = fa), 1233 i for "pe" and "pi", 1248 m for "té", 1732 gli for "f", 1759 ga for "nt", and the
  five groups of "frontières". Others may be the encipherer's slips: 1526 negociation for "sion", 1156 re for "im", and
  1500 1500 1757 for "avons".
- Group 1226 (2 occurrences) is read with two values - blocker: open-codes. The "V" of "V. M." from the gloss, and
  "comm" in the last lines. One of the two is probably 1286 (Sa) or 1886 (com) misread. 1224 (2 occurrences) is "is"
  in one place and "x" in another. Neither group is in the key.
- 22 verbatim words rest on pass-3 re-reads of the looped 8 - blocker: illegible. The reviewer could not always tell
  this 8 from a looped 2 on shape alone; the plain 8 of 1248 (A05) and 1585 (B12) has the same foot. The re-reads are
  plausible but key-assisted.
- One agent made both transcription passes, and every reader so far was an AI agent - blocker: needs-physical-access.
  A blind second transcription of the doubtful groups would settle most of the above; the blind review spot-checked
  96 groups in 8 rows.
## Not part of this target (not worked)

The following are other documents of the volume, not unread pieces of the document above.

- The rest of catalogue 2244. The catalogue entry treats the glossed passages, image 227 among them, as cribs and "not
  part of the open text", so this document does not close 2244. The bare runs at images 198, 246 and 342 (and 378, 438,
  450, 474, 486, 510, 522 in the catalogue's sample) and the glossed passages at 29, 86, 114, 397 and 539 were not
  opened in this round, so it is not known which code each uses. In targets/hopken1740 the analogous Lit. A of 1741 is
  recorded as a contemporary decipherment, not counted in the headline share.
- Image 482 (Carlson's despatch of 22 Sept 1742, with three Swedish-glossed blocks and a "Lit. A" on Lanmary's letter to
  Castellane) is **in another code**. Its groups run to 2959, and "Castellane" is 1531 1733 1442 1034 1182, which the
  hopken1740 key does not give.

## Extent

Counted on the key alone, 205 of 256 cipher words (80.1%) are verbatim, so the extent would be read in part. With the
contemporary gloss over the 26 distinct groups the frozen key lacks, all 256 words read as sense, with 0 holes
(`fraction_coherent` 1.0 in profile.json); the reviewer graded the document read on that basis, as with Lit. A of 1741 in
targets/hopken1740. If the maintainer prefers the key-alone count, `outcome.class` should be read in part.

## Escalation

- [x] siblings: image 482 of the same volume looked at (another code); the sibling volumes' key (targets/hopken1740) applied frozen
- [x] clear-pages: the gloss over the groups is the contemporary decipherment, used as held-out test and for 21 values
- [x] known-keys: the hopken1740 key (key_1741.tsv) applied frozen and unchanged; it does not fit image 482
- [x] print: web search of 12 Nov 2026, no edition or decipherment of this extract; a 2002 study of Crimean Tatar letters to Sweden noted and not opened
- [ ] key-rebuild: the 14 unsettled repairs and 1226/1224 not rebuilt; a blind second transcription would test them
- [ ] retry: the 14 repairs and the 14 words with a doubtful digit not retried beyond the pass-3 crops; the other documents of the volume are outside this target (above)

## Collision check (12 Nov 2026, at the start and again before finishing; again 13 Nov 2026)

The clone's origin/main was 65445e3f8 on 12 Nov; live main through the GitHub API was 7dcbe3f68 (17:56 UTC). On 13 Nov
origin/main and live main were both 65cdcd9d5 (12 Nov 21:56 UTC). targets/ has only hopken1739 and hopken1740 for Höpken
(hopken1741a and hopken1741b were folded into hopken1740), and no hopken1742. Nothing in targets/ or research/ names
R0003637 except the sweep-D rows, the Turcica sweep's units.json and the vetting files. Open PRs (13 Nov: #391, #494-#498,
#500) and PR searches for hopken1742, Höpken, Hopken, Crimea, Khan, Carlson, R0003637 and 2244 show only our merged #236,
#300, #458 and #459 and Dan's merged #379. No collision.

## Prior art (checked 12 Nov 2026)

On 4 Nov the catalogue entry recorded known.py, DECODE (Nordic dump), Tomokiyo and web searches, with nothing found. One
web search on 12 Nov 2026 (the Khan of Crimea's letter to the King of Sweden, 1742, Porte, secours, défensive) found no
edition or decipherment of this extract. It did find a 2002 study of Crimean Tatar letters to Sweden (Pis'mennye pamyatniki
Vostoka 8, orientalstudies.ru), which was not opened. **The Khan's original letter (in Turkish or Tatar) may survive among
the Turcica in Riksarkivet and may be described there. That would be a possible crib for the sense; not checked.**

## Files

- SIGN_CONVENTIONS.md; transcription_khan1742_pass1.txt, _pass2.txt, _blind.txt (key-blind reconciled) and
  transcription_khan1742.txt (pass 3); gloss_khan1742.tsv.
- key_frozen.tsv (352 entries, = targets/hopken1740/key_1741.tsv), FROZEN.sha256, key.tsv (373 entries).
- decryption_khan1742.txt, marked_khan1742.txt, reading_khan1742.md, translation_khan1742.md, about_reading_khan1742.txt.
- validation.tsv (scripts/validation_pairs_1742.py).
- scripts/: fetch.py, crop.py (need the scans, not included), decrypt.py, check_marks.py, heldout.py,
  validation_pairs_1742.py.

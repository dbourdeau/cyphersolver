# Poinsett → Monroe, Santiago de Chile, 20 Feb 1813 (Unsolved Catalogue no. 639), with the Buenos Aires letter of 14 June 1814 (no. 651)

Outcome (12 Nov 2026): the 20 Feb 1813 letter is read in part with the printed code table WE025 (Andrew Beling, pull
request 414; integration check at the end of this file); the 14 June 1814 letter is read from the clerk's decipherment.
Sections 1-5 are the earlier work and are kept as written, with dated corrections.

Catalogue 639. Joel Roberts Poinsett, US special agent for Buenos Aires, Chile and Peru, to James Monroe, Secretary
of State. Manning, *Diplomatic Correspondence ... concerning the Independence of the Latin-American Nations* vol. 2
(1925), doc. 442, pp. 896-898, prints the clear text with "(undeciphered cipher)" at ten places.

## 1. The document

- NARA RG 59, Despatches from Special Agents, vol. 3 = microfilm **M37 roll 2** (catalogue naId 213803757),
  **frames 0092-0094** (folios 37, 37v-38, 38v; old foliation 41 on 0093). Images are the catalogue JPEGs
  `https://catalog.archives.gov/medialz/dc-metro/rg-059/876974/M37-02/M37-02-NNNN.jpg` (not committed).
- Frame 0092 (f. 37r, the opening) is filmed almost black with heavy show-through; even after background
  flattening only the clear words can be made out, not the code groups of passage P0 ("You will have seen a series
  of ..."). Frames 0093-0094 are good.
- Passages P1-P9 (`transcription.tsv`, one row per written line, with the clear context from Manning): **437 code
  groups, 256 distinct** (`ciphertext_1813.txt`, measured with `docs/_check_profile.py --measure --digits`).
  Manning's ten "(undeciphered cipher)" places = P0 + P1-P9 (Manning splits P2/P3 around "and dictated by the first").

## 2. The system

A numbered code of about 1,600 groups (highest group read 1589; one doubtful 1800), comma-separated. Common words
are single groups (1355 the, 1397 of, 522 and, 1348 in, 1215 / 1315 a, 1554 to), longer words are spelled from
syllable groups (409 1175 1179 765 pro-te-ti-on; 1314 413 1166 per-ma-nent). Values are not in alphabetical order
(1348 in, 1355 the, 1385 pre, 1397 of, 1399 foot, 1407 po, 1413 at): a two-part code. A small circle over a group
adds -s (971 country, 971° countries; 1116° in "sloops"); a cross under a group and a caret also occur (1115+,
694+, 264^, 961^), meaning not yet established.

(Corrected 12 Nov 2026: with WE025 the examples above change. 1314 413 1166 1399 is per-ma-ne-nt; 593 is foot, 1399 nt,
1407 pose; 1215 is a, and 1315 is "hu" in WE025, written where "a" is wanted and not explained; 409 1175 1179 765 is
pro-te-ct-ion. Besides the circle a diamond adds -s; the cross doubles a letter and the caret adds -ed, both read from use.)

It is **WE025**, which Weber, *United States Diplomatic Codes and Ciphers* (1979), prints in full (1,592 elements; the
contributor cites pp. 470-480, see the integration check for the page numbers); no copy of that table was in the repo
(corrected 11 Nov 2026: see "WE025 (Beling, 11 Nov 2026)" below).
It is not any of the US code tables that were in the repo: the Department code of 1803-40 (`targets/jqa`, the = 1385), Armstrong's
THE=972, Pinckney's legation code, the 1788 legation code, Jefferson 1787, Mountflorence 1801, nor Sumter's Rio code
of 1813 (M121 vol. 1A frames 0035-0039: the = 798, of = 1399, and = 1242). `shift_test.py` also tried every constant
shift (and mod 1600/1700) of the first five against the 1813 groups: best z = 4.3 among ~9,000 settings for the JQA
table, decodes are junk; no signal. Gallatin to Madison, 15 Aug 1810 (Founders, Madison 03-02-02-0600), says
Sumter "ought to have Mr Poinsett's cypher", so a Sumter-Poinsett copy may have existed, but Sumter's despatches to
Washington are in his own code.

## 3. The 14 June 1814 sibling (Unsolved Catalogue no. 651): already deciphered, and the key source

Poinsett → Monroe, Buenos Aires 14 June 1814. Original (RC): M37 roll 2 **frames 0097-0098** (f. 39r clear, f. 39v
with both code passages and a **clerk's decode written over the groups**). **Duplicate**: frames 0099-0100 (f. 40r
headed "Duplicate", f. 40v the same code passages, no decode, line ends intact). Same code as 1813 (the = 1355, of = 1397,
"of this country" = 1397 891 971 in both letters).

**Prior art.** Manning, *Diplomatic Correspondence ... Latin-American Nations* **vol. 1 (1925), doc. 201, pp. 335-336**,
prints the whole letter with the code passages in clear, from "MS. Consular Letters, Buenos Aires, I". His text is the
clerk's decode word for word ("the utmost ship should draw", "than single Frigate"). So catalogue 651 was read in
1814 and in print since 1925; the catalogue's "OCR only, no decipherment" was wrong (found 27 Oct 2026, archive.org
djvu text of `diplomaticcorres01mann`). Method for this letter: **existing decipherment**.

**What was done here** (`transcription_1814.tsv`, `ciphertext_1814.txt`, `decode_1814.py` → `reading_1814.txt`):
both copies transcribed line by line and checked against the clerk's words and Manning. Merged text (RC, gutter
ends from the Duplicate): **123 groups, 90 distinct; 122 have a value = 0.992**. The one open group is **39** in "a ship
[39] should draw", left blank by the clerk and by Manning.

- A (after "a mission which has originated from the"): the prevailing opinion of a rupture between Great Britain and
  Spain [:] the present government of this country will endeavour to obtain the protection of the latter at any
  price; such is however the disposition of the people that the English never can gain a permanent footing in these
  countries.
- B (after "sent a prize to Rio de Janeiro"): their trade is exposed to a just retaliation of this principle, with
  seldom more than a single frigate to protect it; two sloops of war [are] better than a frigate, eighteen feet being
  the utmost a ship [39] should draw.

Corrections to the key aligned earlier (`key_1814.tsv`, now 95 values): 964 = *principle*, not "prince" (the clerk's
word runs into the gutter, Manning prints "principle"); the group for "it" is **1236** (Duplicate clear, faint 1 on the
RC; 1236 occurs three times in 1813), not 236; "two" is **1087** on both copies, not 1037; "between" reads **737** on
both copies (middle digit not certain), not 727; "protect(ion)" splits pro-te-**ct**-**ion** (409 1175 1179 765),
since "protect" is 409 1175 1179 and "frigate" ends in 1175 = te; "feet" = 108 **480** (480 from the Duplicate).
Copy differences: the Duplicate drops 337 *never* and 1506 *sloo-*, and writes 127? for the RC's 137 *war*.

## 4. The 1813 letter with that key

`decode.py` → `decode_1813.txt`: **161 of 437 groups (0.368) have a value** (158 before the 1814 corrections of 27 Oct). The decode is fragments, not yet
sentences, e.g. P1 "No dependance can be placed on the [1436] of the people the [486][1095] and li[218][1095] of
this country ..."; P4 "... of this govern-ment [901] the ..."; P6 "... re-[12]-pro-te-ti-on ..."; P7 "... in the
[428] of ... the govern-ment". No sentence reads yet, so nothing is claimed as read.
(Superseded 11 Nov 2026: with Weber's WE025 the letter reads in part; see the section "WE025 (Beling, 11 Nov 2026)".)

### Claims review by a second reader (12 Nov 2026)

- The committed key file has 341 lines, 339 of them rows of the table (1800 and 1885 are out of range).
- 293 word places: "B. Ayres" is one place, and the "the" of "[?to the]" has no group and is not a place.
- The separate decoder used the contributor's table rows on the project's earlier transcription: it shows the reading
  does not depend on his transcription, not that the table is confirmed apart from him.
- The Full-texts decryption of the 1814 letter is the earlier alignment file (462 = should, group 39 blank); the
  WE025 decode (39 = should, 462 1495 = dra-w) is `beling/tests/heldout_1814_result.txt`.
- The contributor's reading header and the profile step of 11 Nov keep "pp. 470-480" and 0.916: his text, see above.

## Remaining gaps
- P0, f. 37r (frame 0092), about three lines of groups - blocker: illegible; the microfilm frame is nearly black;
  needs a new scan of the original (NARA RG 59) or the 1813 duplicate if one survives
- 20 Feb 1813, 7 groups whose WE025 value gives no sense where they stand - blocker: open-codes; the groups are 55,
  12, 502, 774, 487, 122, 1261 (five of the numbers, 55, 502, 487, 122, 1261, occur nowhere else in the letter); a
  misread digit, a slip of the encoder or a wrong row of our copy of the table cannot be told apart from these frames
- 20 Feb 1813, 20 groups read only by assuming a digit misread - blocker: illegible; listed in
  `beling/groups_1813-02-20.tsv` (status I); the film is high-contrast, the doubtful digits are filled blots or lie
  at the gutter and the page edge; eleven were looked at again on frame 0093 on 12 Nov 2026 (integration check) and
  none can be settled digit for digit there; needs a new scan of the original
- 20 Feb 1813, 25 groups whose number was fixed after the decode was seen - blocker: illegible; 21 choices between
  two readings frozen beforehand and 4 rereads; same film; one transcriber, no second reader of the numerals
- 1315, three times in the 14 June 1814 letter where "a" is wanted - blocker: open-codes; WE025 has "hu" and
  1215 = a; 1315 is clear on frame 0100 all three times, so it is not a misreading of 1215; not explained
- 210 in Brice Dudout's 1811 line ("in-form-ed") - blocker: needs-physical-access; WE025 has "cur" at 210 and "form"
  at 216; his photograph of the HSP leaf is not published, so the digit cannot be checked here
- that the table used is the one Weber prints as WE025, row for row - blocker: needs-physical-access; neither the book
  nor the contributor's full transcription is in the repository (341 of 1,592 rows are, 10 marked as checked on the page
  image); the page numbers given for the table conflict (see the integration check)
- the marks over and under groups (circle, diamond, cross, caret) - blocker: no-key-material; their meaning is read
  from use only, no instruction sheet for this code is in hand

Closed on 11 Nov 2026: the 276 of 437 groups without a value (WE025 gives every group a value), and group 39 of the
14 June 1814 letter ("should" in WE025; beling/README.md).

## Escalation
- [x] siblings: M37 roll 2 frames 0091-0102 opened; 14 June 1814 (0098, duplicate 0100) is in the same code with a
  clerk's decode, used for the key; 0462 (Jacob Lewis) is another code; Sumter's Rio code (M121) is not this one.
  28 Oct: M37 roll 1 (all 753 frames), M37 roll 2 frames 0025-1057, M70 roll 1 (Buenos Aires consular despatches
  1811-17, 292 frames) and M77 vol. 7 (instructions 1808-15, sampled) surveyed by contact sheet: no further frame in
  this code and no key table. Lowry, La Guaira 1810-12 (M84 roll 1 frames 0014-0090): all clear. Not surveyed: M78
  consular instructions 1801-17 (naId 220862827)
- [x] clear-pages: Manning prints the clear text only; no clear copy of the cipher passages found
- [x] known-keys: JQA/Department 1803-40, Armstrong THE=972, Pinckney, 1788 legation, Jefferson 1787,
  Mountflorence 1801, Sumter 1813 tried directly and under shifts; none fits. 11 Nov 2026: the printed table WE025
  (Weber 1979) is this code (Beling; beling/README.md)
- [x] print: Manning vol. 1 doc. 201 (1925) prints the 14 June 1814 letter decoded (the clerk's text); vol. 2 prints
  the 1813 letter undecoded; Weber 1979 consulted by the contributor on 11 Nov 2026 (table only, no decode of 1813).
  The HSP calendar of the Poinsett papers (1941, HathiTrust mdp.39015034759822) is behind a bot check and was not
  searched; it is a calendar of his own papers, where no decode of the Department's copy is expected
- [x] key-rebuild: context pass of 27 Oct gave only 'Lima'; superseded by WE025, which gives every group a value.
  The seven holes cannot be bracketed: the code is not in alphabetical order
- [x] retry: 11 Nov 2026, every group decoded again with WE025 from the frozen numerals, four rereads on the image
  (Beling); 12 Nov 2026, eleven of the twenty assumed misreads looked at again on frame 0093 (integration check)

## 5. Next steps

1. Context pass: fill recurring groups only where two or more occurrences agree; grade them I.
(12 Nov 2026: steps 1-2 are overtaken by WE025; step 3 stands; for step 4, group 39 is "should" in WE025.)
2. Find more decoded material in this code: Weber, *United States Diplomatic Codes and Ciphers* (1979); HSP Poinsett
   Papers vol. 4 (1811-14 reports "parts in cipher", per the HSP list filmed at M37 roll 2 frames 20-22); the
   Department's Buenos Aires consular file (M70) for any of his letters that were not returned in 1818.
3. A better image of f. 37r (frame 0092).
4. Manning took the 1814 text from "MS. Consular Letters, Buenos Aires, I" (NARA M70 roll 1): check whether that is a
   third copy of the 14 June 1814 letter, or a copy of the 1813 one, with its own decode (it might fill group 39).

Prior art (27 Oct 2026): Manning 1925 has no decode; web search found none; not in the repo before this folder.

## Contribution (Brice Dudout, 3 Nov 2026)

Poinsett's despatch of 29 June 1811 (HSP, Poinsett Papers vol. 1, folder 10) has 19 groups in this code with the plain
text written over them: four values of `key_1814.tsv` are confirmed and 13 are new (`dudout/key_1811_additions.tsv`).
With them, 170 of the 437 groups of the 1813 letter have a value (was 161); no sentence reads yet. The despatches of
20 March and 11 April 1811 are in a second code, with a "decyphered" sheet for 11 April. Details in `dudout/README.md`.

## WE025 (Beling, 11 Nov 2026)

Contribution by Andrew Beling, with AI agents; details, files and scripts in `beling/README.md`. Daniel's files and
`dudout/` are unchanged.

- **The code is WE025** (Weber 1979, pp. 470-480). Our transcription of Weber's table was frozen by sha256 at
  2026-11-11T10:37:23Z, before any decoding with it (`beling/key/we025_SHA256.txt`); one correction after the freeze,
  668 = fect. Only the 341 rows for numbers that occur in these letters are in the repo (`beling/key/we025_poinsett.tsv`).
- **14 June 1814** (not a blind test: the agent had seen the clerk's values): WE025 alone matches 0.935 of the clerk's
  letters (376 of 401); 200 shuffled keys mean 0.184, best 0.306. With two image rereads (337 = 338 never, 435 = 485
  dom) 0.954. Of the 27 values where WE025 and `key_1814.tsv` differ, 21 are syllable splits of the clerk's words; group
  39 is "should" (462 1495 = dra-w). 1315, written three times where "a" is wanted, is "hu" in Weber: not explained.
- **20 Feb 1813, read in part**: from our own frozen transcription of the numerals (1 Nov 2026), 406 of 437 groups read
  as frozen (92.9%), 4 more after an image reread, 20 rest on an assumed digit misread, 7 are holes. All nine coded
  passages P1-P9 join Manning's clear text (`beling/reading_1813-02-20.md`; line by line against `transcription.tsv`
  in `beling/decryption_1813-02-20.txt`). Poinsett admits taking "a part in the revolution of this country" beyond his
  instructions; "a small naval force with five thousand stand of arms would insure the fall of Lima"; the journey to
  Arauco is to leave the militia "in the hands of patriots", and independence is to be declared.
- **Open points**: 1215 = a in WE025 (1413 = at), so the "at" of 1811 is the decoder's word; 708 = i, the letter, so
  "disposition" is dispose-i-tion and 708 is the pronoun "I" in 1813 ("I have"). Of Dudout's 13 values 12 are WE025's;
  210 (form) is "cur" in WE025, which has form at 216: left to him.
- **Still open**: P0 (frame 0092); the 7 holes; the 20 assumed misreads; 1315; the marks (meaning inferred from use);
  no second reader. Reading review pending.

## Integration check (12 Nov 2026)

Pull request 414 was verified by a separate read-only pass before integration; this section records what that pass
and the integration found, and what was changed. The contributor's files in `beling/` are unchanged.

**What reproduces.** The file hashes; the status counts (D 385, A 21, R 4, I 20, H 7 of 437); the 1814 score with the
committed rows, 0.935 of the clerk's letters (376 of 401), 0.954 with the two rereads; the comparison of the two
transcriptions (420 first readings, 5 second, 5 differ, 7 with an unread digit); Dudout's values (12 of 13 are
WE025's). A decoder written separately, applied to Daniel Bourdeau's transcription of 27 Oct (`transcription.tsv`,
not the contributor's numerals), gives a value to 432 of 437 groups and the same English without any override. On
frame 0093, 73 groups (P1.1-P1.3, P5.1-P5.4) were compared with the frozen numerals: all agree, including the 1800
that the reading takes as 1300. On frame 0100, 485 is clear (the reread of 435) and 1315 is clear all three times.

**What does not.** The control with 200 shuffled keys (mean 0.184, best 0.306) needs the contributor's full table,
which is not in the repository; a shuffle of the 339 committed elements gives mean 0.194, best 0.307. The hash of the
full table (26dad03e...) cannot be checked for the same reason. The freeze of the numerals on 1 Nov and of the table
on 11 Nov before decoding is by the contributor's record (hashes and timestamps of his own files, one commit).

**Is the table Weber's WE025?** Not checkable here. The book is not in the repository and only 341 of the 1,592 rows
are, 10 of them marked as checked on the page image. What confirms the numbering without Weber: the clerk's
decipherment of 14 June 1814 (63 of 89 values identical, the rest syllable splits of his words), Dudout's 1811
values from the HSP leaf (12 of 13), and the 1813 text itself, which reads as English. The sheet of another code of
the same family in the repository (`targets/morris1813/beling/key/codebook_M97_13_transcription.csv`, Weber's WE028)
has 334 of the 339 elements in its vocabulary and none of the 341 numbers the same: the same printed 1,600-element
form with another numbering. `targets/king1797/NOTES.md` section 9 quotes Weber p. 143 for WE025 having 1,592 elements.
**Page numbers:** the contributor's text, profile entries and reading cite "pp. 470-480"; his
`beling/key/we025_corrections.tsv` cites "page 443" to "page 453" for rows of the same table. Both spans are eleven
pages, 27 apart, so one is probably the numbering of a PDF; nothing in the repository says which is the printed one.
The table's page numbers are therefore not checked, and the write-up cites the table as WE025 without them. That
Weber's own list of users of WE025 does not name Poinsett is the contributor's search, not confirmed here.

**The test on the 1814 letter is not blind**, as the contributor says: the clerk's values had been seen before the
table was identified, and no threshold was set. It shows that the table reproduces the clerk's decipherment.

**Counting, by the read bar as written** (a word is read only if it is not a hole, a guessed `[?word]`, a supplied
word, or a value fixed by the sense). The coded passages of the reading have 293 word places (292 words and the
supplied "[be]"; Manning's clear words are not counted). Words whose every group is a first frozen reading, used as
the table gives it: **248 of 293 = 0.846**. The other 45: 16 words holding one of the 21 choice groups (mass, no
twice, situation, acts, want, cutting, deemed, object, leave, declared, preponderance, paralises, America, me, my),
4 holding a reread group (number, means, the, seas), 19 holding an assumed misread, 5 with a hole (in-struct[55],
mar-ke-[12], dis[502][774], [487], [122][1261]-sion), and "[be]". Counting the choice words as read gives 264
(0.901; the verification pass counted 264 of 295, 0.895). The contributor's 0.916 is `share()` on his reading file
and also counts the clear words from Manning that open each passage. By groups: 385 of 437 = 0.881 are first frozen
readings; 406 (0.929) with the choices; 410 with the rereads. `read_share` in the profile is 0.846 and
`fraction_read` 0.881; both are under the 95% bar, so the letter is read in part.

**A look at the frames (12 Nov 2026, NARA catalogue JPEGs of frames 0093-0094, one pass).** The film is
high-contrast: closed digits fill in and the left page loses its line ends in the gutter. P7.4 third group: the last
three digits read 517, which supports 1517 (ay) against the frozen 1317|1327. P7.3 "851": the middle digit could be
9 (891 this). P7.2 "428": the last digit is a filled blot (425 court is possible). P4.6 "?31": the first digit is
under the folio number, 4 is possible; the group before it could be 140 or 148. P5.3 "1221": the last digit is a
blot. P2.5 first group: the first digit is blotted, 3 is possible. P4.4 "124?": blot over the last digit. P4.5: after
"155" the film has a blank about one group wide before 1002, room for the rest of 1554 and one more group ("to the").
P7.3 first group and P7.4 first group ("17"): blotted, not legible. P5.4: 1800 is what is written. That is eleven of
the twenty assumed misreads. Also seen: P4.2 "1356" (a reread), the last digit is 5 or 6 with a flourish. None of
these is settled; the statuses in `beling/groups_1813-02-20.tsv` stand.

**Corrections made in the folder.**
- `profile.json`: `outcome.key` was "recovered"; it is now "partial" (a printed table was matched, nothing was
  recovered by cryptanalysis, and seven groups have no usable value). `contribution` no longer lists "key extended or
  corrected". `read_share` 0.916 becomes 0.846 and `fraction_read` 0.929 becomes 0.881 (above). `codes_open.total`
  is 245, the distinct numbers of the contributor's transcription; the 256 of section 1 is the distinct count of
  Daniel Bourdeau's transcription (`ciphertext_1813.txt`). Gaps, a text entry for the 1814 letter, the reading
  reviews and the integration step added.
- 668: `beling/key/we025_poinsett.tsv` still carries "feet" in its element column, with "fect" in the `post_freeze`
  column; the decode applies "fect" (P4.8 "into ef-fect"). The file is left as the contributor froze it.
- The 1814 letter with WE025: group 39 is "should" and 462 1495 is dra-w, so the passage ends "the utmost [1315] ship
  should draw" (`reading_1814.md`); 337 is 338 (never) and 435 is 485 (dom), both on the images. `reading_1814.txt`
  and `key_1814.tsv` are the earlier alignment to the clerk's words and are kept as they were.
- The figures in `beling/README.md` section 6 for Shaler, Monroe, Crawford, Clay and the other Poinsett letters have
  no inputs in the repository. They are the contributor's pointers, not results of this target, and are not published
  as results.


# Verification of the Arthur Lee to Richard Henry Lee readings, 1779-80

Verifier: Claude (Opus 5.5 subagent), 14 November 2026. Part A done blind: the reader's
NOTES_arthur_lee_1779.md, decoding.tsv and PASSAGES.md were not opened before BLIND_FREEZE.txt was written.

## Part A, step 1: sample rule (written before any lookup)

Sample = the 24 groups the transcription marks doubtful, plus 30 further groups chosen thus:
number all 166 groups 1-166 in the order of the transcription's "Normalised group lists"
(letter 1 to letter 6). Take positions 5, 10, 15, ... (every fifth). If the group at a
position is one of the 24 doubtful ones, take the next non-doubtful group after it. Stop at 30.

Resulting sample (position in the 166-group list: group as transcribed):
- Doubtful 24: 6 51a10, 8 4b9, 11 68a30, 14 390a15, 18 82b37-s, 20 392b28, 39 108a37, 44 63a31,
  52 115b38(second), 56 2b29, 59 ?2b9-s, 62 134a6, 72 284a7, 91 236b18, 102 314b37-d, 106 28?a9-s,
  111 238b30-es, 113 100b36, 120 454b?14, 128 455?a27, 144 250?b?12, 151 119b5, 158 455?a14, 161 416b10.
- Rule sample 30: 5 224b22, 10 243a17, 15 170b15, 21 170a25 (20 doubtful), 25 252a28, 30 243a17,
  35 311a27, 40 56b31, 45 455a14, 50 101a35, 55 108a9, 60 246b25, 65 216a8-s, 70 354a36, 75 145a34,
  80 314a20, 85 108a9, 90 314a28, 95 43a23, 100 107b30, 105 150b33, 110 332b28, 115 80b1,
  121 115b38 (120 doubtful), 125 455b11, 130 196a28, 135 134a6-s, 140 93b15-s, 145 455a14, 150 179b18.

## Part A, step 2: edition and counting rule (decided blind, from Tomokiyo's groups only)

Tomokiyo's page used: https://cryptiana.web.fc2.com/code/bookcode.htm (fetched 14 Nov 2026, saved in `tmp/bookcode.html`).
His Lee groups: 243a17 minister, 196a28 I, 059a08 base?, 426b29 and 330b13 (uncertain), and from Lee's
translated 27 Aug 1778 letter 082b05 channels, 099a17 Congress, 229a37 loan. From Jay's unoffset letters:
108a10 court, 166b32 force, 223a34 latter, 378a07 told.

Checked by eye on the page images (1776 copy in `sources/raw/entick_dictionary/bim_..._1776/pages/`, and
three 1773 pages fetched into `tmp/e73/`):
- 1772 and 1781: different pagination (Congress, minister, loan nowhere near). Ruled out.
- 1773 and 1776: same page breaks on pp. 166, 196, 229. They differ elsewhere: p.101 begins with
  Conspicuously in 1773 but with Conspiracy in 1776; p.108 col. a has Court as the 10th entry in 1773 but
  the 9th in 1776. Lee writes court as 108a9 five times, so the **1776** setting fits Lee and the 1773 does not.
- Counting rule: **entries** from the top of the column, not physical lines. Loan 229a37 is right only if
  the run-over line under "Lively" is skipped; I 196a28 only if the section heading "I." is skipped;
  Friend 170b15 only if the run-overs under "Fret" and "Friarlike" are skipped. Minister 243a17, Congress
  99a17, channels 82b5 and force 166b32 fit either way. Jay's court 108a10 does not fit (Lee's own 108a9
  does): Jay counted differently or had another printing.
- Pages 454-455 ("Most usual Christian Names of Men"): five columns a-e; letter headings not counted.
  Lee's "455,d,XXVII" (column letter clearly d on image 0041) gives Samuel, which supports this.

Frozen in BLIND_FREEZE.txt (sha256 of blind_lookup.tsv) before any reader file was opened.

## Part B: comparison with the reader (files opened after the freeze)

### Agreement on the 54 groups

| Result | Count | Groups (position in the 166 list) |
|---|---|---|
| Same word | 43 | all 30 rule-sample groups except 21; doubtful 6, 18, 20, 44, 52, 62, 72, 91, 102, 111, 113, 120, 128, 151 |
| One line off | 1 | 21 (170a25) |
| Different column | 1 | 158 (455?a14 vs reader's 455e14) |
| Other (different digit, or I left it unsettled) | 9 | 8, 11, 14, 39, 56, 59, 106, 144, 161 |

Rule sample alone: 29 of 30 the same word. Doubtful 24: 14 the same, 1 column, 9 other.

### Each disagreement, looked at again on both images

- **21, 170a25 (reader: 170a24 French).** The letter-book reads XXV clearly (image 0019, line "same &
  nothing material"); entry 25 on p.170 col. a is *Frenchified*, 24 is *French*. The reader changed the
  group to fit. Not settled: Lee may have slipped, or meant "Frenchified". "French faith" is an emendation.
- **158, 455?a14 in letter 5 (reader: 455e14 Thomas).** Re-examined at 6x: page digits blotted, and the
  column letter is a small looped letter that looks more like *e* than Lee's usual *a*. Col. e entry 14 =
  Thomas (p.455). Context (he is to marry and go into trade) excludes Gerard. **Reader right**, image consistent.
- **14, 390a15 (reader: 390a25 Venerable).** Image: "390,a," ends the line, next line starts "XV," at the
  same margin as the lines above, no sign of a lost X. As written = *Vendible* (nonsense). XXV = Venerable,
  IX = Venal. Not settled; "venerable" is a guess.
- **39, 108a37 (reader: 100a37 Considerableness).** Third digit looks like 8 to me; 108a37 = Cowl (nonsense);
  100a37 = Considerableness (checked). Reader's reading is plausible but rests on a changed digit.
- **161, 416b10 (reader: 416b19 War).** Image shows X plus a faint stroke at the right edge; War = entry 19.
  Reader probably right (peace or a long war); the IX is inferred.
- **8, 11, 56, 59 (reader: 64b9 Bishop, 168a30 Former, 132b29 Distress, 152b9 Exertions).** On the images the
  left edge of the scan cuts the first letters of lines (e.g. "[thi]ng that is", "[ve]ry good authority"),
  and p.2 and p.4 are front matter (dictionary words begin p.33), so the printed page numbers are certainly
  incomplete. I checked the reader's four supplied pages on the 1776 images: Bishop (64b9), Former (168a30,
  counted from the foot), Distress (132b29), Exertion (152b9) are right for those coordinates. The missing
  digits are inferred from sense, not read. Bishop agrees with history (La Luzerne's brother was Bishop of
  Langres).
- **106, 28?a9-s (reader: 287a10-s Powers).** Image: third digit under a blot; "IX" is clear. The reader
  changed both the digit and the line. Keeping IX, 284a9 = *Politician* gives "European politicians are much
  at ease on that head", which needs only the blotted digit. I prefer *politicians*; neither is settled.
- **144, 250?12 (reader: 250b12 Murder, left unread).** Column hidden by the blot (250a12 = Multipede).
  Agree it is unread.

### Reader errors found that do not change words
- 392b28 is Villanous as transcribed; the reader's `lookup_used` says 392b27 (a miscount; same word).
- 166b7: the reader says Footing is in col. a in 1776 and changed the group to 166a7. On the 1776 image
  (p166_n165.jpg) col. a begins Foison and col. b begins Foot; **Footing is 166b7 and Force is 166b32
  exactly**. So the claim "p.166 shows the 1777 edition differs" is wrong, and Tomokiyo's anchors fit the
  1776 copy 10 of 12, not 9.
- 455?a27: the column letter on image 0041 is a clear *d*; Samuel should be firm, not a guess.
- 314b37-d: I first leaned to XXXVI on the image; the dictionary decides for 37 (Restrained). Agree with reader.

### Was the reader's test sound?
Partly. The real-versus-control comparison (27/30 against 0-1 of about 22 per control arm) does show that
the 1776 edition with the entry rule turns Lee's groups into sense and that shifted pages do not. But the
same agent extracted the words and judged them, and the judge sheet shows decoded neighbours in the context
(e.g. "jobbing the state ___ , to job the state"; "that French, faith, & ___"), which makes a right word
easier to accept. The control arms are random dictionary words, which almost never fit, so the test cannot
fail by much and does not test the guessed or emended groups at all. My independent re-derivation (same
edition, same rule, 43 of 54 the same word, 29 of 30 in the rule sample) is stronger evidence for the key
than the test; the test adds little beyond it. It does not support the 17 "guess" readings.

### Claims in the passage summaries not carried by firm groups
1. "The *venerable* friend [Franklin] ... to promote Deane's charges ... equally wicked" (letter 1):
   *venerable* rests on 390a15 read as XXV; "friend = Franklin" is the reader's identification.
2. "*French* faith & friendship" (letter 1, and the Historical note "says French 'faith and friendship' are
   mere interest"): the group reads XXV = Frenchified; "French" is an emendation. (The sense is close.)
3. "I am afraid the *former* [Gérard] will have done all the mischief": page digit supplied; Gérard is inferred.
4. "brother to the *Bishop*": page digit supplied (historically right).
5. "the French consul [John Holker]": consul is firm, Holker is identification only.
6. "Lafayette's 2,000 French *troops*" (letter 4 and Historical note): 384b26 is Trot; Troop is 384b16.
   *Troops* is a guess (twice).
7. "*European powers* are much at ease": changed digit and line; *politicians* fits better.
8. "In one word he [Franklin] is the servant of this court, not of his country": the groups are firm, but
   the referent is inferred; the sentence before ("He must win the cause") is about the new man to be sent.
   "They have him" favours Franklin; still an inference.
9. "the wickedness which *Benjamin*, Deane & [their] junto" (second Benjamin): the column letter is under a
   blot (454a14 would be Ambrose). Firm enough by sense, but not read.
10. "*Thomas* [Lee] will come": column letter read as e from context; image consistent.
11. Inflections supplied by the reader: "ministry"/"minister[s]" (243a17 has no ending), "enemies"
    (145a34 no -s), "John Adams's" (should be "John Adams"; the -s is on Adam). None changes an accusation.
12. The Historical note says Lee "does not want Lafayette's 2,000 French troops on American soil" and that
    they "wish for a footing": *footing* is firm (166b7), *troops* is guessed, Lafayette is identified from
    "Marquis ... your Brigadeer" (reasonable).

Firm: Gérard suspected of being "concerned with Deane in merchandise, contracts" and "imposed upon the
minister"; "the Doctor, the French consul, Gérard, Deane, Chaumont & Beaumarchais are all interested
together"; Gérard's "connexion in jobs with Deane"; "never will our affairs go well while Benjamin is here"
(first Benjamin firm); "the wicked manoeuvre of M. Gérard"; the "old Doctor's unfitness to be minister".

## Part C: gaps

### Letter-book page 39 (image 0052, 1000-pixel copy only; read on the image by me)
Page 39 holds letters of 28 May 1779 (R. H. Lee, S. Adams, Joseph Reed, F. L. Lee, introducing La Luzerne).
At its foot: "R. H. Lee continued from p. 28. he being now in England" — this completes "hurt him he be-"
on p.28. Page 40 (image 0053) begins a new letter ("R. H. Lee & F. L. Lee, Dear Brothers, Paris May 28th
1779"). **No further code.** The May letter's date is still only "before 9 May"; no date line on p.39.

### Earlier readings and received copies
| Source | Result |
|---|---|
| Potts, *Arthur Lee* (1981) | Internet Archive lending copy only (`arthurleevirtuou0000pott`); search-inside returned **403** "Item not available", 14 Nov; stopped using archive.org after that. Not read. |
| Weber (1979) | Lending copy only (`unitedstatesdipl0000webe`); not attempted after the 403. Not read. |
| Smith, *Letters of Delegates* (Library of Congress) | Old memory.loc.gov query URL gives 404; loc.gov collection search for "Entick" returns 0 hits; item/resource JSON for the series and vol. 12 returned **520** twice. Not read. |
| Burnett, *Letters of Members* III-IV | Not re-checked by me (archive.org stopped after the 403). The reader's report of what Burnett says stands unverified. |
| American Philosophical Society | A printed *Calendar of the Correspondence of Richard Henry Lee and Arthur Lee in the Library of the American Philosophical Society* (Hays, 1900) exists (BioStor 203621, Biodiversity Heritage Library pages 7124125-42). BHL OCR request returned **403**; stopped. This calendar is the quickest way to learn whether the received copies of these six letters are at the APS. The reader did not mention it. |
| Houghton, MS Am 811 | Web search finds the collection and some items on FromThePage ("Colonial North America"), no sign that letters to R. H. Lee of these dates are digitized. Not confirmed. |
| Hoffman guide (UVA Lee Family Papers microfilm, 1966) | Not found online in this pass. |
| 1777 Entick | Internet Archive search: editions 1766, 1772, 1773, 1776, 1781, 1782 and later; **no 1777**. HathiTrust catalogue search: Cloudflare challenge, **403**, stopped. Web search: no 1777 copy surfaced. Google Books not checked by ordinary viewing. No login anywhere. |

Downloads this pass: 4 Internet Archive page images of the 1773 edition (about 4.4 MB, `tmp/e73/`), Cryptiana
and blog HTML pages; under 10 MB in all.

## Corrected wording (only where the code does not carry the reader's)
- Letter 1: "The [Vendible as written; venerable? venal?] friend is doing all he can here with his assistants
  to promote Deane's charges." / "I would hint to you that Frenchified [French?] faith & friendship are the same."
- Letter 4: "The Marquis your Brigadier is to return with 2000 French [troops? 384b26 = trot]." /
  "European [politicians? 28?a9: blotted] are much at ease on that head." / "the part taken by John Adams".
- Letter 1: "rising to great [considerableness? group reads 108, = cowl]".
- Mark "former", "Bishop", "distress", "exertions", "war" (letter 5) as readings with a supplied digit.
- Promote "Samuel" (455d27) to firm.

## Verdict
Sound, with these corrections. The key (1776 London Entick setting, entry count, names pages with five
columns) was reached independently and reproduces the reader's words for 43 of 54 groups and 29 of 30
in the rule sample. The accusations against Gérard and Deane rest on firm groups; those against Franklin
mostly do, except "venerable friend", "French faith" and the referent of "he is the servant of this court".

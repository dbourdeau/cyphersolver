# Bernstorff to the Auswärtiges Amt, Washington, 10 Jan 1917: the code telegram sent by the State Department (catalogue 657)

Status: contributed by WAINUT (27 Oct 2026). Read in part. The first 147 groups are Bernstorff's telegram No. 205
of 10 Jan 1917, whose German text he printed in 1920; aligning the two gives 82 code groups. The other 430 groups
are a second text in the same code and stay unread. The site page and the ledger rows are left to the maintainer.
Second pass 2 Nov 2026 (section 10): the code is identified as Code 7500 from Friedman and Mendelsohn (1938), the
sibling route is closed online, and the second text remains unread for want of a crib.

Catalogue 657. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcription was made with a vision-capable language model and checked against the NARA scans. A second agent
re-read about 117 groups on the full-resolution scans and redid the alignment with its own code.

## 1. The document

- **Source.** NARA RG 59, State Department decimal file **763.72111/4443**, microfilm M367 roll 166
  (763.72111/4226-4500), catalogue [naId 27179174](https://catalog.archives.gov/id/27179174).
  - Frame 0785, sheet "1." ([scan](https://catalog.archives.gov/medialive/74/1791/27179174/content/dc-metro/rg-059/M367/M367_Box_4_122-175/M367_Roll166/M367_Roll166-0785.jpg))
  - Frame 0786, sheet "2." ([scan](https://catalog.archives.gov/medialive/74/1791/27179174/content/dc-metro/rg-059/M367/M367_Box_4_122-175/M367_Roll166/M367_Roll166-0786.jpg)),
    ending "DEPARTMENT OF STATE JAN 11 1917 APPROVED Robert Lansing".
  - Frames 0787-0789: Lansing's note of 10 Jan and the "TELEGRAM SENT ... Please deliver following cipher to Foreign
    Office, from German Ambassador here" of 11 Jan 1917.
  - Frames 0769-0775 and 0778-0784: the German memorandum on armed merchant ships in clear, and its translation.
- **Frame 0786 is not a reversed image.** It is sheet 2. The reversed-looking figures in the left margin of
  0786-0789 show through from sheet 1 in the bound volume.
- **Context.** On 10 Jan 1917 Bernstorff handed Lansing a German memorandum on the armed merchant ships of the
  Entente, and asked the State Department to cable a cipher message to Berlin. Lansing's
  letter of the same day (FRUS 1917, Supplement 1, [doc. 75](https://history.state.gov/historicaldocuments/frus1917Supp01v01/d75),
  file 763.72111/4443) first refused. It names two subjects: "the new offensive armament of the merchant vessels of
  the Entente powers, and also my note of December 18 relative to peace terms". A footnote says: "This message,
  however, was sent the following day." This is the same State Department channel the Zimmermann telegram used five
  days later.

## 2. Transcription

`transcription.txt` gives the groups row by row as typed, with struck groups in braces and notes in parentheses.
`decode.py` numbers them from 0.

- **577 groups**: 505 of four figures, 67 of five, 4 of three (the head) and 1 of six (group 377, 108609 [?]).
  The catalogue's "about 150 groups" was too low.
- The typeface confuses 5, 6 and 8: 6 has an open hooked top, 8 is closed and S-like. On the full-resolution scans:
  - group 20 reads **8918** (a closed 8, as in 8559 next to it), not 6918; group 12 (6918) has an open 6;
  - group 40 reads **88789** (the fourth figure is the same closed 8 as in 8789 at group 27), not 88769;
  - group 447 (sheet 2, row 12, second group) has its second figure typed over another: 28648 or 26648 [?].
- An independent re-reading of about 117 groups (sheet 1 rows 1-4 and 9-12, sheet 2 rows 1-4, 12 and 13) agreed
  on 116; the open case is group 447. Readings such as 06887, 4118 and 0089 fit the glyph forms but are not certain.
  Repeated groups were read the same way every time, so the repeat analysis below does not depend on them.
- The clerk underlined the four-figure tail of several five-figure groups (54873, 88789, 71621, 11374, 61166, 98462,
  80129). Pencil tallies in the margin are a count for charging, not part of the message.

## 3. The two parts

- **Groups 0-146 are telegram No. 205.** Bernstorff printed its German text in *Deutschland und Amerika* (Berlin
  1920), pp. 325-326: "2. Ziffertelegramm, Washington, den 10. Januar 1917. Antwort auf Telegramm 148". The English
  is in *Official German Documents relating to the World War* (Carnegie Endowment 1923), vol. II, p. 1017, no. 56:
  "Telegram No. 205 ... Rec. Berlin, January 14, 1917". Neither source mentions the ciphertext or gives a code group.
  `printed_tel205_de.txt` is the German body (two OCR slips corrected: Einigimg, nauß).
- **Groups 147-576 are a second text** in the same code. It does not fit No. 205 (section 6). It is probably the part
  on the note of 18 Dec 1916 on peace terms, the second subject in Lansing's letter. That is not confirmed.
- The catalogue's suggested crib, the memorandum in clear on frames 0769-0775, is not the plaintext. It is what
  No. 205 reports on ("Memorandum Lansing überreicht").

## 4. The code

- **Two-part (randomised) code.** The recovered groups are in no alphabetical order: aber 8335, alles 4349,
  Amerikaner 7294, auf 8693, bis 7424, Bruch 4879, Da 9793, daß 8172.
- **Four-figure groups 0000-9999**, leading zeros kept.
- **A five-figure group is a prefix figure plus a four-figure base group.** In 21 of the 67 five-figure groups the
  last four figures also occur as a four-figure group; chance gives about 2.2, and the first four figures do so in
  only 2. Cases: 86699 vorgegangen (6699 Vorgehen), 88789 herbeigeführt (8789 herbeiführen), 11374 hiesigen
  Regierung (1374 hiesiger Regierung), 61166 des Memorandums (1166 Memorandum), 54873 Vereinigten Staaten (plain
  4873 for the same phrase at 134), 71621 zu nehmen.
  - Prefix 8 for a past participle rests on **two secure cases** (86699, 88789). A third, 85380 = geantwortet in
    part 2, is a guess.
  - Prefix 5 in 54873 has no known meaning.
  - 71621 is placed by position only: 1621 never occurs alone.
- **Several groups for the full stop.** The eight sentence ends of No. 205 carry 1515, 3377, 0404, 1515, 3377,
  0404, 1724, 1515 (groups 8, 42, 64, 73, 88, 98, 107, 122).
- **Not code 13040.** The 13040 text of the Zimmermann telegram (19 Jan 1917) is mostly five-figure groups in the
  range 10000-24000. This fits the published description of code **0075** (a two-part code of 10,000 groups, held
  at the Washington embassy in January 1917), as quoted second-hand from Kahn. No 0075 indicator is visible, and
  the head 958 677 728 229 0705 is unresolved. So "0075 family" is probable, not proven [?]. **Updated 2 Nov 2026:**
  Friedman and Mendelsohn (1938) call the code of the Bernstorff messages on this State Department route **7500**;
  see section 10. This cable is not in their list, so the attribution stays an inference, now a strong one.
- The 82 base groups fixed so far are in `codebook.tsv` (the key file), each with its evidence and a grade: C for
  the known plaintext, consistent at every occurrence; M for uncertain.

## 5. The reading of telegram No. 205

The line-by-line decryption is in `decryption_tel205.txt` (output of `python decode.py`), with the alignment in
`align_205.tsv`. The sentences are in `reading_tel205.md` and the English in `translation_tel205.md`. Holes:
`[958]` is a group without a value; `[?words]` are words of the print that sit on a run of groups whose split is not
fixed, so they are not read from the groups.

> [958] [677] [728] [229] [0705] Memorandum Lansing überreicht. Meines Erachtens wird Vorgehen im Sinne dieses
> Memorandums Friedensvermittlung Wilsons [?zum Scheitern bringen und statt dessen] Bruch mit Vereinigten Staaten
> herbeiführen, [?wenn nicht mindestens so lange] mit Vorgehen gewartet wird, bis Einigung mit hiesiger Regierung
> herbeigeführt ist. Es wird sich vielleicht erreichen lassen, daß Amerikaner davor gewarnt werden, auf Schiffen
> Dienst zu nehmen, [?welche zu Angriffszwecken bewaffnet sind]. Hierzu muß aber jedenfalls [der] hiesigen Regierung
> Zeit gelassen werden. Da alles [7918] von Wilson entschieden wird, ist Besprechung mit Lansing reine Formsache. Er
> antwortet niemals, bis er Instruktionen von Wilson hat. Im vorliegenden Fall muß letzterer erst Denkschrift lesen.
> Wieviel Wert Euere Exzellenz auf Wilsons Friedensvermittlung legen, kann ich von hier [?aus nicht ermessen]. Davon
> abgesehen, [?muß ich pflichtgemäß bestimmt erklären, daß ich] Bruch mit Vereinigten Staaten für [?unvermeidlich]
> halte, wenn ohne weiteres im Sinne des Memorandums vorgegangen wird. [0278]

> [958] [677] [728] [229] [0705] Memorandum handed to Lansing. In my opinion, action along the lines of this
> memorandum will [?wreck] Wilson's peace mediation [?and instead] bring about a break with the United States,
> [?unless, at least for as long as it takes,] action is held back until agreement with the government here has been
> reached. It may perhaps be possible to have Americans warned against taking service on ships [?that are armed for
> purposes of attack]. For this, however, [the] government here must in any case be given time. Since everything
> [7918] is decided by Wilson, a discussion with Lansing is a mere formality. He never answers until he has
> instructions from Wilson. In the present case the latter must first read the memorandum. How much weight Your
> Excellency places on Wilson's peace mediation I [?cannot judge] from here. Apart from that, [?duty compels me to
> state positively that I] consider a break with the United States [?unavoidable] if action is taken along the lines
> of the memorandum without further ado. [0278]

- 120 of the 147 groups have a value of their own. read_share 0.793 (hole rate 0.207 on
  `research/reading_audit/v2_score.py`), so the document is **read in part**. On the same scorer 7 of 13 sentences
  are clean when the marked words count as holes (the printed German alone scores 12 of 12 that way), which is
  near the lower edge for "read in part".
- **Weak spots.**
  - Groups 19-23 (5 groups for 6 words) and 28-30 (3 groups for 5 words and a comma): their content comes from the
    print, not from the groups.
  - Groups 59-63 (", welche zu Angriffszwecken bewaffnet sind"): the split is not fixed.
  - Groups 120-121 (1354 0321, "aus nicht ermessen"): the split is doubtful.
  - Groups 125-131 (", muß ich pflichtgemäß bestimmt erklären, daß ich") contain none of the known groups for muß
    (5810), ich (2880) or daß (8172). Either the cipher words this differently from the print, or it uses other
    forms. This is a hole, not a confirmed reading.
  - 7918 at 76 has no word in the print. 8096 "unvermeidlich" is a doubtful reading of its figures.
  - The head 958 677 728 229 0705 (probably the heading "Antwort auf Telegramm 148") and the end group 0278
    (perhaps the signature) are unresolved.
- Context: Bernstorff warns Berlin that acting on the memorandum will end Wilson's peace mediation and lead to a
  break with the United States. Germany announced unrestricted U-boat warfare on 31 Jan 1917; the United States
  broke off relations on 3 Feb.

## 6. Why the alignment is not chance (`python decode.py --controls`)

Every code group that recurs in groups 0-146 recurs where the printed text repeats the word: 0352 Lansing (6, 84);
2373 Wilson (18, 78, 96, 112); 7937 mit (25, 31, 38, 83, 133); 9699 wird (10, 35, 44, 80, 145); 0197 von (77, 95,
118); 7424 bis (36, 92); 2765 er (89, 93); 5810 muß (66, 102); 8693 auf (55, 111); 6356 werden (54, 72); 2012 ist
(41, 81); 3091 ge- (gewartet 33, gewarnt 52); 6918 7437 im Sinne (12, 141); 2396 2772 Friedensvermittlung (16,
113); 4879 7937 (5)4873 Bruch mit Vereinigten Staaten (24, 132). None is contradicted.

A blind test that does not use the alignment maps cipher position p of groups 5-145 to word position p·160/141 of
the printed German (160 tokens). A repeated group scores when all its occurrences fall within ±w of one shared word.
On the corrected transcription:

| window | tel 205 vs groups 5-145 | control: tel 212 text vs groups 5-145 | control: tel 205 vs part-2 blocks (3 × 141) | 2000 shuffles (mean / max) |
|---|---|---|---|---|
| ±6 | 23/25 | 8/25 | 7/19, 7/16, 8/16 | 0.43 / 0.76 |
| ±3 | 20/25 | 4/25 | 3/19, 2/16, 5/16 | 0.17 / 0.44 |
| ±2 | 16/25 | 2/25 | 0/19, 0/16, 3/16 | 0.10 / 0.32 |

No shuffle reached the observed score at any window (p < 0.0005). The tel 212 control is the opening of Bernstorff's
Ziffertelegramm Nr. 212 of 16 Jan 1917 (same book, pp. 352-353; `control_tel212_de.txt`). The test counts any
shared word, so a few hits fall on a neighbouring word (8789 at 27 and 40 meets "mit"). The independent check ran
the same test on the transcription before the two corrections and got 21/24, 18/24 and 15/24, with the same
controls pattern.

`python decode.py --check` confirms that every span in `align_205.tsv` matches the transcription and that the spans
cover groups 0-146 without gaps.

## 7. Part 2 (groups 147-576)

`decryption_part2.txt` fills in the groups already fixed by No. 205: 69 of 430 (16.0%), from the 82 base groups.
Nearly all are function words (ich, daß, hat, auf, für, Wilson, Friedens-). No sentence can be built, and no
plaintext is claimed. Part 2 opens 6497 8511; the same pair recurs at 277-278 (and 96497, 98511 elsewhere), perhaps a
heading or a repeated formula. A run 8769 3865 2452 occurs twice (507-509, 512-514).

## 8. Earlier work

- The plaintext of No. 205 is in print (Bernstorff 1920; Official German Documents 1923), as above. We credit
  Bernstorff's 1920 print as the source of the crib (role "key or decipherment used").
- No decipherment of this ciphertext and no code groups of this code were found in print. The link between the
  ciphertext in 763.72111/4443 and telegram No. 205 is not made in FRUS, Bernstorff or the Official German
  Documents. The web search was light, and Boghardt, *The Zimmermann Telegram* (2012), which covers the State
  Department route and Room 40's handling of Bernstorff's January 1917 traffic, was not consulted. Since the British
  read the State Department cables and code 0075 was partly broken, a Room 40 decrypt may exist. "Not found in
  print" and "first link made here" are therefore qualified claims until Boghardt is checked.
- A British (Room 40) intercept of this message, if one exists, would be in TNA HW 7 or ADM 137; not checked
  (offline), nor is the PA AA file copy. The Official German Documents (vol. II, p. 881, minutes of 18 Nov 1919) list it as "a telegram of Ambassador Count Bernstorff
  of January 10, 1917, which was communicated from the Foreign Office on January 14 and 15, 1917".

## 9. Proposed catalogue corrections (entry 657)

- folio_note: 577 groups (505 four-figure, 67 five-figure, 4 three-figure, 1 six-figure), not "about 150";
  frame 0786 is sheet 2, not a reversed or offset image.
- status: groups 0-146 are Bernstorff's telegram No. 205 of 10 Jan 1917 (printed in Bernstorff 1920 pp. 325-326 and
  Official German Documents II p. 1017); the memorandum on 0769-0775 is not the plaintext. 82 code groups recovered;
  groups 147-576 are a second text in the same code, unread.
- code: a two-part four-figure code with prefix figures; not 13040; probably 0075 [?].
- Suggested status: read in part (telegram No. 205 aligned; the second text open).

## 10. Second pass, 2 Nov 2026: the second text, not read

The aim was to read groups 147-576. They were not read. No plaintext and no sibling ciphertext could be reached.

**What the second text is about.** Bernstorff's own cover letter (FRUS 1917 Supp. 1, doc. 74) says the cipher message
"refers to the above-mentioned question" (the armed ships) "and to your note of December 18 last concerning peace
terms". So the subject guess in section 3 now rests on the sender's words. It is still not proved that the division
falls at group 147, or that groups 147-576 are all on that subject.

**The code.** Friedman and Mendelsohn, *The Zimmermann Telegram of January 16, 1917 and its Cryptographic Background*
(War Department 1938; archive.org 41766889080599), p. 16 and n. 40:

- The Bernstorff messages sent through the State Department are "all in a code which is known as 7500", established by
  comparing them with the plain texts in the German Hearings.
- It is a two-part code of 10,000 phrases numbered 0000-9999, which is what section 4 found from the groups.
- It came to America by the submarine *Deutschland*; their earliest message is dated 16 Nov 1916. They count "about a
  dozen" 7500 messages in the American files.
- Note 40 names Nos. 151 and 156 of 21 Nov, 164 of 1 Dec, 169 of 4 Dec 1916, 212 of 16 Jan, 222 of 21 Jan, 228 and 229
  of 23 Jan and 239 of 27 Jan 1917, as "some of" them (one OCR layer reads 154 and 166 for 151 and 156; 154 fits
  No. 164's text in Official German Documents).
- This cable is not named, so 7500 is inferred from the route, date and structure. They cite a further paper,
  Mendelsohn, *An Encipherment of the German Diplomatic Code 7500* (1938). It is not in the NSA Friedman index pages
  (Publications, Reports, Correspondence) or on archive.org.

**Why those siblings are the way in, and why they failed.** Several of those telegrams have a printed plaintext
(Nos. 164, 169, 212, 228, 239 in Official German Documents II; 212 and others in Bernstorff 1920), so each ciphertext
would be a new crib for the code. No ciphertext was found online:

| Searched (OCR text; frame filter that does catch both sheets of this cable) | Result |
|---|---|
| M367: 763.72/2991-3100, 3101-3300, 3301-3515; 763.72111/3951-4225, 4501-4810; 763.72119/--150, 151-325, 326-470, 471-625; 763.72115/2201-2325, 2326-2500 | no German code sheet; roll 166 is the only hit |
| M580: 841.857/203-495, 496-820 | one numeric frame, 2 of 45 groups shared, no sibling |
| Bulk OCR of all RG 59 frames (`rg_59.jsonl`, first 400 characters of each flagged frame), ranked on shared groups | M367 roll 166 frame 0785 only (40 of 50); the next frames share 5 at most and are not code |
| M973 purport lists: 701.38-701.6239, 763.72/1-763.72111/5692, 763.72119; name index card for Bernstorff | show 701.6211/399 (24 Nov 1916, code telegram asking leave for Hatzfeldt to testify) and this cable's 4443; 701.6211 is listed only in purport lists and the name index, not as a digitised file |

Also searched, because the Zimmermann inquiry and the Bell-Harrison exchanges passed German cipher telegrams through
them (purport list 87662081): 862.20212/0-350 and 862.20211/0-200, 601-1000, 1001-1175. They hold German cipher
telegrams, mostly five-figure, but the best frames share 9% of their groups with this cable, which is near the chance
level for 384 four-figure bases plus five-figure tails. None is in this code.

**Catalogue 635 is not a crib.** The file copy, 841.857/244 (M580 roll 191 frame 0111, seen), is Grew's telegram 4691.
It gives only "(Quote German cipher)", with the note "delivered to Ambassador by direction of the Secy 12/7/16". The
groups went to the embassy and were not kept with the telegram. This explains the pattern: incoming ciphers left the
Department, so only Bernstorff's outgoing messages can survive. It also corrects the next step named in the first pass.

**Print.** `align_part2.py` aligns the known groups of part 2 with a text. On all of Bernstorff 1920 the best place is
No. 205 itself (score 14.1, shared vocabulary) and no other place gives a long run; the same book's Nos. 192 and 212 do
not fit. Official German Documents II has Bernstorff's Nos. 164, 169, 182, 188, 192 ... and only No. 205 for 10 Jan; a
word-anchor scan of its English found nothing beyond No. 205 and the other telegrams on the same subjects. So the second
text seems never to have been printed in those series. A State Department index card (name index, 763.72119/8814, from Berlin, 25 Jan 1920) records a published pamphlet with
"all Bernstorff correspondence" on the peace action; it was not found, and it may be the same material. Not read in
full: Birnbaum 1958, Doerries 1989 and Link vol. 5 (loan copies on archive.org; phrase searches gave no hit on this
telegram, and search-inside returned 403 on Doerries and Ritter). Scherer and Grunewald vol. 1 was not reached.

**What a reader could do with it.** The 82 values remain valid for 16% of the groups, and no value was added. German
function words alone do not support a code recovery: on a two-part code one group gives no clue to another, as Friedman
says of this very code, and a stretch of five or six unknown groups "may be filled" in endless ways. Guessing the 361
others from context would produce a text of the model's making, so none is offered.

## Remaining gaps

- Groups 147-576, the second text (430 groups) - blocker: needs-physical-access. The crib is outside this session:
  the Politisches Archiv draft of the telegram, a Room 40 decrypt (TNA HW 7, ADM 137), or the sibling ciphertexts
  Friedman saw in State Department files (not on the digitised reels searched, section 10). Mendelsohn's 1938 paper
  on Code 7500 may also help and was not found.
- The head groups 958 677 728 229 0705 and the end group 0278 of No. 205 - blocker: needs-physical-access. Same
  sources; a sibling with its head and signature would fix them.
- The runs 19-23, 28-30, 59-63, 120-121 and 125-131, group 7918, and the doubtful 8096 - blocker: needs-physical-access.
  They occur once each; a second text in this code with a known plaintext would fix them.

## Escalation

- [x] siblings: Friedman's nine named 7500 telegrams looked for on 14 reels, the RG 59 bulk OCR, purport lists and the
  name index (section 10); no ciphertext online. Catalogue 635 holds no ciphertext (841.857/244, frame seen).
  No. 212 stays a control only.
- [x] clear-pages: the memorandum in clear (frames 0769-0775) is what No. 205 reports on, not its text.
- [x] known-keys: no copy of Code 7500 (0075) or 13040 was available; 13040 ruled out by its group range. Mendelsohn
  1937 (archive.org 41784749082377) has 13040 and 18470 material, nothing for 7500.
- [x] print: Bernstorff 1920 aligned by script and Official German Documents 1923 scanned; they give No. 205 but not the
  second text. Friedman and Mendelsohn 1938 read: no groups of this code printed.
- [x] key-rebuild: 82 groups fixed from No. 205; not enough for part 2, and no value added by guessing.
- [x] retry: the prefix-figure rule is applied to part 2 by `decode.py` (a five-figure group takes the value of its
  four-figure base): of the 58 five-figure groups in part 2, 5 get a value this way (included in the 69); no
  sentence follows. The German Foreign Office file copy of the second message (PA AA, Weltkrieg /
  Friedensvermittlung series) or a Room 40 decrypt (TNA HW 7, ADM 137) would be the crib for part 2.
- Statistical validation: `validation.tsv` holds the 147 groups of No. 205 with their values (27 unread);
  `python docs/_validate.py bernstorff1917` gives "underdetermined" (reading -2.062 per letter, random keys -2.008,
  key fitted to shuffled text -1.816). This is expected for a whole-word code with 1.38 tokens per type: swapping
  word values of equal length still yields German words. The test that fits this code is the blind alignment test
  in section 6.

## Files

- `transcription.txt`: the 577 groups as typed, with marks.
- `ciphertext_tel205.txt`, `ciphertext_part2.txt`: the groups of each part without marks (written by `decode.py`).
- `codebook.tsv`: the 82 recovered code groups (key file).
- `align_205.tsv`: the alignment of groups 0-146 with the print.
- `validation.tsv`: groups 0-146 with their values, for `docs/_validate.py`.
- `decryption_tel205.txt`, `decryption_part2.txt`: the line-by-line decryptions (written by `decode.py`).
- `reading_tel205.md`, `translation_tel205.md`: telegram No. 205 as German sentences and in English.
- `printed_tel205_de.txt`: the German text of No. 205 as printed in 1920 (the crib).
- `control_tel212_de.txt`: the opening of telegram No. 212 as printed in 1920 (control only).
- `decode.py`: decryption, span check and controls (standard library only).
- `align_part2.py`: aligns the known groups of part 2 with a printed text (section 10).
- No images are kept here; the scans are linked above.

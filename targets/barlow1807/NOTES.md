# Catalogue 1245: Sir George Barlow to Thomas Grenville, 1807, "in a curious cipher"

Status: in progress. Not yet written up: no site page or README row. Read in part, with escalation steps still open (see Remaining gaps and Escalation). The status below is the contributor's.

Status: read in part (3 Nov 2026). 1192 of 1379 words of the letter to Grenville read with no letter changed (86.4%).
The letter to Tierney is in clear.

Work by WAINUT with AI language-model agents viewing the images. No human palaeographer has checked any sign.

## Status per document (3 Nov 2026)

| Document | Images (reading order) | Words | Read as sense | Status |
|---|---|---|---|---|
| 1. Barlow to Thomas Grenville, Fort William, 12 Feb 1807, "(Private and Confidential)", "Quadruplicate"; cipher | 15, 16, 17, 18, 1-14, 19, 20; 21 blank; 22 docket | 1379 on images 1-19 (713 clear, 666 cipher), plus 12 clear words of the subscription | 1192 (86.4%) with no letter changed | **read in part** |
| 2. Barlow to George Tierney, Fort William, 15 June 1807; clear | 23-25; 26 docket | 440, all clear | 440 | transcribed; no cipher |

Letter 2 is a separate letter, not a cover for letter 1. It reports on the political state of India and on finance:
dispatches sent by the extra ship Indus; Hyderabad, Poona and Delhi; a surplus expected in 1808/9. Its docket reads
"Recd 26th Novr 1807". The docket of letter 1 (image 22) reads "Duplicate Fort William 12 Febry 1807 Sir Geo. Barlow to
Mr Grenville R. 23 Septr 1807", though the letter itself is headed "Quadruplicate".

**Counts for letter 1.** These are the counts of `python scripts/check_marks.py 01 ... 19` over images 1-19: 1379
words, of which 713 are clear and count as read. The subscription on image 20 has 12 more clear words and is outside
these counts. The 1379 count words only: four-digit code groups and nulls (28 places, among them the groups read as
India and British) are left out of it. Image 3 is in the count but is in effect not read (see Remaining gaps).

| Measure | Words read of 1379 | Share |
|---|---|---|
| Read with no letter changed (dropped nulls and supplied omitted letters allowed): **the headline figure** | 1192 | **86.4%** |
| Alternative: the same, if the three key errors below were corrected (80=c, 99=b, 58=m) | about 1241 | about 90.0% |
| Alternative: read as sense, counting the 119 words with a letter changed from context | 1311 | 95.1% |
| Read with no repair at all (only omitted letters supplied) | 1028 | 74.5% |

Letter 1 is **read in part**. The headline is 86.4%. It reaches 95% only if the 119 words with a letter changed from context are counted as
read. A value from context alone is doubtful, so they are not.

Of the 666 cipher words:
- 315 read with no repair;
- 164 read with signs dropped only;
- 119 read with at least one letter changed;
- 68 are doubtful.

There are 447 repairs in all: 314 dropped signs and 133 changed letters. `check_marks.py` passes with no unmarked
departure (exit 0).

## Source and images

- **Catalogue entry.** Cleveland Public Library (John G. White collection), Zamboni note no. 159: "1807. Sir George
  Barlow to Lord Grenville and others. Official, private and confidential reports written in a curious cipher with
  covering letters." Via DPLA / Ohio Digital Network, item e4082bb91cf5f55ec10516bc367df12d.
- **Images.** 26 images on Wikimedia Commons, titled "Two letters to Thomas Grenville (in cipher) and to George Tierney
  on affairs in India - DPLA - e4082bb91cf5f55ec10516bc367df12d (page N).jpg". They are about 1100 x 1380 px and public
  domain. Scans are kept locally and are not in git.
- **Fetching.** `scripts/fetch.py` (UA `WAINUT-research`). The first runs stopped on HTTP 429 after page 13. One later
  run at one request per 30 s fetched pages 14-26 with no 429.
- **The Commons image order is not the letter's order.** The letter runs:
  - Image 15 has the heading, address and date, and begins "Having observed a paragraph".
  - Images 15 -> 16 -> 17 -> 18 run on by sense ("estab | lishment").
  - Image 18 ends with the catchword 98. Image 1 begins "98,90,12. ... have generally been supposed to be so" ("in the
    degree in which they have generally been supposed to be so").
  - Images 1-14 run on (catchwords on images 2, 6 and 10).
  - Image 14 ends with the catchword 55. Image 19 begins 55,43,39 ("presidencies") and ends "I have the honor to be".
  - Image 20 has the subscription "with high respect Sir Your most faithful & obedient Servant G H Barlow".
- **Pencil numbers.** Image 1 = 3, image 13 = 15, image 19 = 17, image 21 = 19, image 23 = 21. The number on image 17
  looks like 16 and does not fit, so the pencil numbers do not settle images 15-18. Text and catchwords do.

## Collision and prior art (3 Nov 2026)

There is no target folder or open PR for Barlow or Grenville in dbourdeau/cyphersolver (checked on origin/main). One web
search (Barlow, Grenville, 1807, cipher, Dropmore) found no printed decipherment. The HMC Dropmore volumes and the India
Office records were not searched. We do not claim the content is unknown: a clear copy may exist in London.

## The system

- **Mixed text.** Clear English is used for function words and many phrases. Sensitive words are runs of numbers
  separated by commas, each run closed by a stop. A stray stop sometimes splits a word ("ques. tions.", "persuas. ion.").
- **Letter table.** One number = one letter, with homophones, and one table for the whole letter. The three-digit
  forms 401, 402, 140 and 190 are e's; 151 is u.
- **Omitted letters.** The clerk leaves out letters, mostly e, i and o, and sometimes a syllable (`rligious`,
  `sntmnt`, `gout` = govt). u/v and i/j are one letter each.
- **Probable nulls.** The frozen key gives signs 10, 11, 12, 20, 21 and 22 letters (t, h, s, r, d, o). But they mostly
  stand where no letter belongs, inside words as well as at the ends: `a{d>}nd`, `o{d>}f{t>}`, `i{o>}{t>}n`,
  `t{h>}he{o>}y`.
  - On pages 1-19, counted before the readings, sign 11 stands at a word edge 26 times and inside 50 times; 21 at an
    edge 31 times and inside 34; 22 at an edge 37 times and inside 58.
  - **One rule.** In a read word these six signs are dropped (`{x>}`), unless the word needs that very letter at that
    place and no other sign in the word gives it. Then the sign is kept as its key letter. That happens at 11 places:
    `conclusion` (22), `this` (10 and 11), `those` (22 and 12), `excited` (21), `has` (11), `most` (22), `it` (10),
    `tenets` (10), `with` (11, its final h). Dropping the sign and supplying the same letter as an omitted one would give the same reading. Where
    a null and a real sign give the same letter (`s{o>}o`, `t{t>}h`), the null is the one dropped. At 3 places sign 20
    stands where the word needs d (`regard`, `solicitude`, `discharged`), and at 1 place sign 11 stands where the
    word needs w (`with`, image 14); these are counted as changed letters.
  - With this rule the readings drop 273 of these signs in read words, keep 11 and change 4.
  - That they are nulls throughout is not proved, but the independent check (`VERIFY.md`) found that every place it
    could test reads as English with them dropped, and that reading them as omitted vowels fails.
- **Four-digit nulls.** Groups 1100 and 2200 are nulls at all 9 places, and inside two runs. 1000 occurs once and
  behaves the same way.

## Code groups

Each group was tested at every occurrence on images 1-19. A value is given only where it fits every place.

| Group | Places | Value | Note |
|---|---|---|---|
| 4990 | 7 (images 7, 9, 10 x2, 11, 14, 15) | **India** | "natives of [4990]" x3, "establishment in [4990]" x2, "[5650] empire in [4990]" x2. "India" is also spelled out in letters 3 times. |
| 5650 | 4 (images 10, 14, 16, 17) | **British** | "the [5650] dominions", "authority of [5650] government", "[5650] empire" x2. "British India" is also spelled out once. |
| 3355, 4340 | 1 | not a code | On image 10 the commas are faint. The digits split as pairs 33,55,43,40 = "mpre" (empire), the same phrase as image 14 "5650. 33,55,43.". Patched. |
| 4845 | 1 (image 12) | open | "religious topics in the college of [4845]". Fort William fits, but one place proves nothing. |
| 4600 | 1 (image 14) | open | "the moral and religious interests of the [4600] community". |
| 4087, 5089 | 1 each (image 15) | open | "one of the [4087] newspapers lately received in [5089]". |

Earlier notes called 4990 a sentence-end marker. That was wrong.

## Transcription

- **Two passes.** Each page was transcribed twice, independently and sign first, from full-size images, with no key in
  the prompt. Pass A and pass B were made by two different AI language-model agents. Pass A on image 17
  stopped after five lines and was run again; the cut-off run is kept as `trans_raw/p17_A_truncated.txt`.
- **Settling.** Every A/B difference was settled by eye on 1.5x crops, sign first: 269 on images 1-13 and 189 on
  images 14-26. Each is logged in `disagreements.tsv` (page, line, position, pass A, pass B, final, reason).
- **Patches.** `patches.tsv` (80 entries) holds every change to pass A: B readings taken, catchwords, interlined and
  struck figures, run splits and doubt notes. `scripts/apply_patches.py` asserts that each old text is present.
- **Run splits.** These are decided on the digit pairs, never on the expected word: image 18 "5,140" -> 51,40; image
  10 "3355,4340" -> 33,55,43,40.
- **Image 16, line 14.** There are dots under the second `46,40,10`, which looks like the clerk deleting a repeated
  "the". Both are kept in the transcription.

## Key and held-out test

- **Frozen key.** `key_final.txt` (91 signs) was frozen after pages 1-13 and is not changed. `key.tsv` lists each sign
  with its frozen value, its count and what the readings found.
- **Held-out result, images 14-19.** These pages were never seen when the key was frozen. Of their 221 cipher words:
  - **100 (45.2%) read with no repair;**
  - 52 (23.5%) read with only dropped signs;
  - 48 (21.7%) read with a changed letter;
  - 21 (9.5%) are doubtful.

  Of the 1160 decoded letters in read words, 86.0% are kept as decoded, 9.1% dropped and 4.9% changed.
  **These figures are graded against our own reading.** They count only the words we chose to read, and the reader who
  settled the transcription of these pages already knew the key. The independent check found 3 wrong signs on image 19
  (lines 6 and 9: 79 -> 70, 98 -> 95, 96 -> 36). Each was checked again on a 2x crop and corrected; the figures above are
  after that correction. The checker's blind file reads `64,70` at the first of the three, so the checker also read 70 there; the crop shows
  70, which gives "assigning". On the training
  pages the figures are 87.7%, 9.0% and 3.3%. The heading and first paragraph of image 15 read at once under the frozen
  key ("paragraph", "newspapers", "proposed", "plan suggested by the Revd C. Buchanan", "England").
- **What the held-out pages showed was wrong in the key.**
  - Sign 58 does not occur on pages 1-13, so it is missing from the key. It is m: `{?>m}[e]moir`,
    `[i]{?>m}p[o]rt[a]nt`, 7 places.
  - Sign 80 reads c, not n, wherever the word is clear: `{n>c}[o]nv[e]rsion`, `{n>c}lergymen`, and on image 7
    `c[o]nv[i]{n>c}tion` (read as `convention` before the second check).
  - Sign 99 reads b, not i, wherever the word is clear: `{i>b}u{p>c}hanan`, `glo{i>b}[e]`, `{i>b}l[e]ss[i]ngs`.

  The marks `{n>c}`, `{i>b}` and `{?>m}` make up 23 of the 57 changed letters on images 14-19 and 37 of the 76 on
  images 1-13 (a few of them come from other signs with the same letters). A corrected key
  would read them without repair. We have not made one, because no unseen cipher text is left to test it on.
- **Round 2 test.** A key annealed on pages 1-5 matched the final key on 125 of 144 signs of page 6 (87%).

## Remaining gaps

One line per unread piece (mirrors `outcome.gaps` in profile.json); details in the next section.

- Image 3 - blocker: illegible; holes marked, the page does not parse.
- Image 8, four-word hole - blocker: not-attempted.
- Image 18, four-word hole - blocker: not-attempted.
- Code groups 4845, 4600, 4087, 5089 - blocker: open-codes; one place each.
- Key errors at signs 80, 99, 58 - blocker: too-short; no unseen cipher text left to test a corrected key.
- Nulls 10, 11, 12, 20, 21, 22 - blocker: not-attempted; one stated rule, not proved everywhere.
- Blind reading beyond images 8, 16 and 19 - blocker: not-attempted.
- Prior art - blocker: not-attempted; Dropmore and India Office papers not searched.

## Gap details

- **Image 3 is in effect not read.** Its holes are marked, but the page does not parse: `[?ato310] to contemplate
  without [?emotion] the operatyon of [?that] [?restricted] ... [?diffusing]`, and "this adverse to these conclusions"
  has no verb. The second check graded it C.
- **Doubtful words.** 68 cipher words in letter 1 are doubtful, all marked `[?..]` in the reading. The longest open
  runs are:
  - image 8: `[?dotr] [?snrt] [?sntmies] of the [?shtratrpsdimployd]`, the subject of "to excite it";
  - image 18: `[?mfap] [?iit] [?oott] [?accomplishing]`.
- **Single code groups.** 4845, 4600, 4087 and 5089 occur once each and are left as codes.
- **Three-digit signs not in the key.** Lone signs 100, 101, 102, 104, 106, 130, 152, 173, 200, 201, 202, 210, 221,
  301, 310, 501, 601, 661, 831, 901 and 902 are dropped or read from context, each marked.
- **Nulls.** Whether 10, 11, 12, 20, 21 and 22 are nulls everywhere is not proved (see the rule above).
- **Blind check covers three pages only.** An independent AI language-model agent transcribed images 8, 16 and 19 blind (697 signs).
  The solver was wrong at 3 signs, all now corrected. The checker left 7 signs ambiguous; each was looked at again on
  a 2x crop. `402,30` on image 19 is 30, the same shape as the 30 on its first line. The other six stay unresolved, and
  their words are now marked doubtful: image 19 `70`/`73` (`[?yiets]`, already doubtful), `69`/`89` (`[?ought]`),
  `98`/`96` (`[?maintains]`), `86`/`36` (`[?of]`); image 8 `89`/`39` (`[?produce]`); image 16 `35`/`85`
  (`[?delicacy]`). The other
  pages have no blind second reading, and the settling was done by one reader who knew the key for pages 7-19.
- **Prior art.** The Dropmore and India Office papers were not searched.

## Escalation

- [x] siblings: the other letter in the same item (to Tierney, 15 June 1807) transcribed; it is in clear and is not a decipherment of the letter to Grenville. Other Barlow cipher letters were not looked for
- [x] clear-pages: the docket (image 22) and the Tierney letter checked; neither gives a decipherment
- [ ] known-keys: no other key of Barlow's or the Bengal government's correspondence was tried; we know of none
- [ ] print: one web search only; the HMC Dropmore volumes and the India Office records were not searched
- [ ] key-rebuild: a corrected key (80 = c, 99 = b, 58 = m) was not made, because no unseen cipher text is left to test it
- [x] retry: the four readings named by the second check were redone and all 33 places of sign 80 rechecked; the doubtful words were not retried with a corrected key

## Changes after the second check (3 Nov 2026)

The second independent check (end of `VERIFY.md`) asked for four reading changes. All four are made:

- **Image 7, `convention` -> `conviction`.** The signs are 65,70,53,80,44,75,36,83,11. With 80 = c, as everywhere else in
  the letter, the word is `conviction`, now `c[o]nv[i]{n>c}tion{h>}`, a changed letter. The next word (80,83,84,32,77,
  98,70,21), which was doubtful, reads `conuiction` in the same way: `{n>c}[o]nui[c]ti[o]n{d>}`, also a changed letter.
  The passage now runs "even by a conviction (if indeed such a conviction could be established) that persuasion
  alone ...". All 33 places of sign 80 in images 1-19 were checked again: every other read place already carried `{n>c}`
  or is doubtful.
- **Image 10, `purposes or` -> `of`.** On a 4x crop the third sign of 36,21,85,21 is plainly 85 (r), not 86 (f). The
  word is now `o{d>}{r>f}{d>}`, a changed letter, so it no longer counts in the headline.
- **Image 14, `than [?st] it solicitude` -> `with`.** The signs are 11,87,10,11. The word is now `{h>w}ith`, a
  changed letter.
- **Counts.** The headline falls from 1195 to 1192 of 1379 (86.4%). The second check expected about 86.5-86.6%; the
  difference is that all three words counted in the old headline now count as changed. `check_marks.py` exits 0.

The check also asked to name the target and its files consistently. The files are now named by the date of each letter
(`*_12feb1807.*`, `*_15jun1807.*`), as in the other targets.

## A second reading of the letter to Grenville, by Harumi-Matsuba (issue #253; recorded 8 Nov 2026)

A separate transcription, key and reading of the cipher letter of 12 Feb 1807 (the same 19 pages in the same order) made by Harumi-Matsuba with Claude, without sight of WAINUT's, is in `matsuba/` (his repository `Harumi-Matsuba/barlow1807-public`, commit 9ee34ba; text and data CC BY 4.0, code MIT; `matsuba/README.en.md` and `matsuba/LICENSE`). It is kept **beside** this reading, not in place of it: neither has been judged against the images, which the project cannot reach, and **no human has checked either transcription**.

What it says of itself (`matsuba/docs/COMPARISON.en.md`, `matsuba/docs/METHOD.en.md`): per cipher token 3,727 of 3,869 (96.3%), per word 3,575 of 3,869 (92.4%, under the read bar); the counts were added after the per-word result was seen and the word test has relaxations added after the reading; no held-out test; the key was set seeing the whole text, with 19 as a or e, 56 as y or w, and 10 and 12 sometimes skipped. A control of 1,000 shuffled keys: none reached the real key (516 of 703 against a best of 369). Second readings from the images alone: Claude Sonnet 93.3% and OpenAI Codex 91.0% before and 91.3% after corrections, against 93.4% and 91.2% for this folder's transcription: they do not separate the two. At the 49 one-to-one transcription differences the second readers side with this folder's more often (Sonnet 27 to 16, Codex 21 to 19). The transcriptions agree at 97.9% in values (of 3,934), with 75 differences (`matsuba/docs/comparison_transcription.tsv`).

What it adds: a reading of p03 (this folder's "in effect not read"; uncertain words remain), readings of the words left as holes on p08 and p18 (or secret enemies, state [?might] be employed, facility of accomplishing), and a key set with the whole text in view (80 = c and 99 = b, which this folder lists as errors in its frozen key, and 58 = m). What this folder has and it lacks: the letter to Tierney in clear, the held-out test of a frozen key, and the blind reading of three pages.

Where they disagree: 101 places in the reading (`matsuba/docs/comparison_reading.tsv`: 52 marked uncertain only here, 8 only there, 41 mixed; different words include elements / limits, privileges / prejudices, consecrated / inscribed, concerns / interests, purity / piety). They are recorded as disagreements and **not judged**. The project recounted the shared key signs from the two key files, letters only: of 79 signs carrying a letter in both, 58 agree and 21 differ (his count is 59 and 20; the signs where one key has a null or a code are left out). The project did not check the reading, the controls or the agreement figures.

## Files

- **Letter 1:** `transcription_12feb1807.txt`, `decryption_12feb1807.txt` and `reading_12feb1807.md`, with
  pages in reading order. The reading gives the marked words per page, a plain running text per page, and the whole
  letter.
- **Letter 2:** `transcription_15jun1807.txt` and `reading_15jun1807.md`. `decryption_15jun1807.txt` states that
  there is no cipher.
- **Key:** `key_final.txt` (frozen key, `num=letter`, read by the scripts), `key_frozen.tsv` (the same table as a TSV)
  and `key.tsv` (sign, frozen value, count, finding).
- **Working files:** `trans_raw/` (two passes per image), `trans_final/` (pass A plus patches), `patches.tsv`,
  `disagreements.tsv`, and `reading/rNN.txt` (one marked token per cipher word, in image order).
- **Scripts:**
  - `scripts/check_marks.py` checks the marks and exits 1 on any unmarked departure;
  - `scripts/heldout_stats.py`, `scripts/build_docs.py`, `scripts/apply_patches.py`, `scripts/abdiff2.py`,
    `scripts/parse.py`, `scripts/solve_sa2.py` and the rest. `solve_sa.py`, `solve_sa2.py` and `vfit.py` score
    against an English corpus in `corpus/federalist.txt` (the Federalist Papers, public domain), which is not included.
- **Checks:** `VERIFY.md`, the two independent checks.

To rebuild: `python scripts/apply_patches.py; python scripts/check_marks.py 01 02 ... 19; python scripts/build_docs.py`.

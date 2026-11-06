# Clas Rålamb and Gotthard Vellingk, Constantinople 1657: the number code and two bare passages (catalogue 2258)

WAINUT, 6 November 2026. Work done with AI language-model agents viewing the images; no human palaeographer has checked
the signs. An independent AI language-model agent that took no part in the solve checked the folder (`VERIFY.md`); the
fixes it asked for are listed under "Independent verification and what changed".

Status (contributor's, after the maintainer's review of 6 Nov 2026): image 104 **not prose**, one deciphered phrase
(4 of 4 words verbatim); image 114 **not prose**, a list of 30 runs (31 of 40 words verbatim from the signs, 77.5%).
Images 22-23 and 75 carry a contemporary decipherment and are used only as the key source and the held-out test; they
are not claimed as read.

## Documents

Riksarkivet, Diplomatica Turcica, SE/RA/2119/2119.1/I/2/2, "E.o. ablegaterna Clas Rålamb och Gotthard Vellingk" (1657),
132 images, IIIF manifest https://lbiiif.riksarkivet.se/arkis!40008933/manifest (scripts need the header
`Referer: https://sok.riksarkivet.se/`). Despatches in Swedish to Charles X Gustav, with words and phrases in a number code.

| Image | What | Use here |
|---|---|---|
| 22-23 | letter of Clas Rålamb, Constantinople 27 May 1657 (end on 24); code with a decipherment written over the numbers | key source (`pairs_022_023.txt`) |
| 75 | copy of a letter of 22 May 1657, signed Clas Rålamb; code with decipherment above | held-out test (`transcription_heldout_075.txt`) |
| 114 | letter of June 1657 (continues on 115); 30 bare runs, no decipherment | **not prose**, list of runs (`reading_114.md`) |
| 104 | letter after 14 June 1657; one bare run of 33 groups, no decipherment | **not prose**, one deciphered phrase (`reading_104.md`) |

Links: https://sok.riksarkivet.se/bildvisning/40008933_00022, _00023, _00075, _00104, _00114.

The volume holds far more cipher than these pages. On 600-px contact sheets of the whole volume, number runs show on images
11, 12, 18-23, 25-29, 43, 46-47, 73-78, 104, 109, 112-116 (sheets of images 49-72, 85-103 and 121-132 were made but not
inspected in this round). Which of these carry a decipherment was checked only for 22, 23, 75, 104 and 114. Image 109 ends a
letter also dated Constantinople 27 May 1657 and may be a cipher duplicate of 22-23; not compared.

## System

A homophonic letter cipher (not a word code): each number stands for one letter, each letter has two to four numbers.
Seen values run 2-108. u/v/w and i/j/y are each treated as one letter in places (33 u/v, 17 i/y); 38 serves å and o;
77 serves y and ö. Numbers in the 800s noted in the catalogue entry were not met in the passages read here.
Sign conventions are in `SIGN_CONVENTIONS.md` (written before any key was applied).

## Key

Built from the 15 glossed runs of images 22-23 (about 330 groups). The decipherment is interlinear, so cipher and gloss
are aligned word by word. `key_frozen.tsv` is the key as it stood before the test: 54 numbers with a sure value,
1 doubtful (78 f), 2 open (72, 108). `key.tsv` keeps those 57 rows unchanged and adds what came after: 72 g, 86 d,
105 ö (confirmed by the image-75 gloss), 50 k (backed by the image-75 gloss "skatt", and holding in 114 and 104),
67 p and 7 z (context values from the bare runs alone, "passa silistrie" and "uiziren", each occurring once in a read
word), and lists 15, 93, 97 as open.

Exceptions in the key material (also noted at the foot of `key.tsv`):

- **79**: t in "totaliter" (image 22, the one place) but m twice in the held-out gloss of 75 (medel, månge). The image-22
  group stands at the line end next to the fold. It reads 79 on a 1.5x crop, but 74 (t) cannot be fully ruled out; if it
  is 74, the conflict goes away and 79 = m everywhere. 79 does not occur in the bare runs read here.
- **9**: l in many pairs, m once in 75 (förmögen), probably a slip. Every 9 in the bare runs reads l (til, aflifuas,
  silistrie, tilkommen, keiserlige).
- **77**: y in 23 (dyren), ö in 75 (förmögen) and in 114 L20 (marked as a change there).
- **31**: in pairs L10 ("trängsmål", `74 47 7? 36 35 31 5 75 46`) 31 stands where the gloss has s. A one-off; the other
  13 places of 31 in the pairs give h.
- **7**: in the same word the group cut at the crop edge, read `7?`, sits at the ä position, while `key.tsv` makes 7 = z
  from 114 "uiziren". The group is cut, so this is not a contradiction, but 7 = z rests on one bare-run word.

## Held-out test (image 75, not used for the key)

`python scripts/heldout.py` decrypts the image-75 cipher with `key_frozen.tsv` and grades it against the contemporary
interlinear decipherment of image 75 (not against our own reading). It prints two scores:

| Scoring | Groups | Right | Wrong | Not in the frozen key | Words exact |
|---|---|---|---|---|---|
| A. signs as written (L03 `45 8 . 4 31`) | 65 | 54 (83%) | 6 | 5 | 3 of 10 |
| B. gloss-guided variant (L03 `8 . 4` read as `84`) | 64 | 55 (86%) | 4 | 5 | 4 of 10 |

In L03 the clerk wrote a point between 8 and 4 (`45, 8. 4, 31`), at the height of the other separators, where the gloss
"underhåldet" needs one group 84 (r). That is most likely the clerk's slip, but the signs as written give two groups, so
the transcription now keeps them (`L03`) and gives the gloss-guided variant on its own line (`V03`). An earlier version
of this folder wrote `84?` in L03 and quoted only score B. The five codes missing from the frozen key are 50, 86, 105
and 72 twice; all four values were later confirmed by this same gloss (they are in `key.tsv`, not in `key_frozen.tsv`).
The wrong groups are 79 twice (m, see above), 9 once (m), 77 once (ö), and in score A the 8 and 4 of L03.

Limits of this test, stated plainly:

- **It is small**: 64 groups, 10 words. It supports the key but is not a strong figure on its own. The stronger evidence
  is that the frozen key alone turns the bare runs of 114 into Swedish sense ("skrifuit ... skrifuit", "togo uiziren
  fat", "aflifuas", "passa silistrie", "tilkommen").
- **The freeze is recorded by file times only.** There was no commit or hash at the time. `key_frozen.tsv` was last
  written at 13:37:43 on 6 Nov 2026; the first full-size crop of image 75 was made at 13:37:54 and the held-out
  transcription at 13:43. The SHA-256 of `key_frozen.tsv`, recorded afterwards, is
  `0bb9b0f8d63cc284f4e8d2497e96ea4ec0d9a4748a4759c68a3ed68d2b54e20d` (`FROZEN.sha256`); it is the file in this folder.
- **Image 75 was seen before the freeze**, but only at contact-sheet size: a 600-px tile on the sheet of images 73-84,
  made at 13:33 when the volume was surveyed for number runs. No value in the frozen key was taken from it, and the
  verifier found no frozen value that needs image 75 (the frozen key keeps 79 = t, which 75 contradicts, and lacks the
  four values 75 supplies).
- **`pairs_022_023.txt` was edited after the freeze** (last written 13:45). What changed was not recorded. The verifier
  ran `key_frozen.tsv` over all 15 pair lines of the final file: every word decrypts to its gloss word except two groups
  cut at the crop edge (L08 `3?`, L10 `7?`) and the 31 = s one-off above, so the frozen key and the final pairs agree.

## Reading of the bare passages

`python scripts/check_marks.py` rebuilds both decryptions from transcription + key and checks every mark (passes, exit 0).

- **Image 114**: 30 runs, 40 words. Verbatim from the signs 31 (77.5%), 1 with a marked change (förb{ö/y}n), 8 with a hole:
  5 where groups are lost in the binding of the volume (L02, L03, L06, L09, L14), 3 with a code not yet identified
  (15, 93, 97). The 93 in L15 is written over another figure and is transcribed `93?`; it may be 97 (both are open codes,
  so the hole stays a hole). Without the two bare-run context values 67 p and 7 z, 29 of 40 words would be verbatim.
  Status: **not prose** (a list of runs; the cipher forms no sentences of its own). Content: the Porte's assurance and
  how firmly "what they have once written stays written"; a mutiny in the camp in which the troops seized the Vizier, brought him to the Sultan and wanted him put to
  death, and the Sultan barely got him off by great intercession; the new Mufti, said to plan with the Tatar Khan and
  the Pasha of Silistra to join forces in support of the Russian. The clear frame given in the reading is an approximate
  working transcription; the cipher words in it copy the marked reading.
- **Image 104**: one short run (one phrase, 33 groups), 4 words, all verbatim: "romerske keiserlige residentens tålk",
  the interpreter of the Imperial (Habsburg) Resident, whom the Vizier uses. Every value used comes from a contemporary
  gloss (the frozen key, plus 50 k from the image-75 gloss). Status: **not prose** (one deciphered phrase, no ciphered
  sentence to score).

These two are bare letters, so this is a break with a key rebuilt from the sibling decipherments, not a transcription of a
decipherment. The glossed letters 22-23 and 75 are only the key source and the test; they are not claimed as read.
English versions: `translation_114.md`, `translation_104.md`.

## Transcription

Image 114 and image 104 were each transcribed in two passes from crops of the full-size scans (`transcription_*_pass1.txt`,
`_pass2.txt`); the passes agree group for group, and the reconciled files are `transcription_114.txt` and
`transcription_104.txt`. For the key pairs (`pairs_022_023.txt`) the numbers were copied with the interlinear gloss covered, as
`SIGN_CONVENTIONS.md` says, and the gloss was read onto separate `G` lines; the gloss ink is faint.

## Independent verification and what changed

`VERIFY.md` is the report of an AI language-model agent that did not take part in the solve. It wrote a blind
transcription of 10 sample lines of 114, the 104 run and the 75 numbers before opening any solver file: 297 groups
compared, 4 raw disagreements (1.7% of groups); after settling on 2x-3x crops, 1 place where the solver had normalised
to the gloss (75 L03) and 1 unresolved (114 L15), 2 of 297 groups (0.7%). It checked the pairs on the scan, reran the
key over all pair lines, reran the held-out test and the mark check, and tampered with copies to see the check fail.
Verdict: confirm, with minor fixes, none changing a status. Fixes made on 6 Nov 2026:

1. `transcription_heldout_075.txt` L03 now gives the signs as written (`45 8 . 4 31`); the gloss-guided reading is the
   separate `V03` line; `heldout.py` scores both and the word score is given (table above).
2. All scripts set standard output to UTF-8, so they run on a Windows cp1252 console (`heldout.py` crashed on "≠").
3. `transcription_114.txt` L15: `93` is now `93?`.
4. Key notes: the 31 = s one-off and the cut `7?` in "trängsmål", and the fold position of the image-22 79, are listed
   above and in `key.tsv`.
5. `reading_114.md`: the bold cipher words in the clear-frame table now copy the marked reading, marks and holes
   included (it had normalised forms such as "assistence", "förbön", "skrifwit", "aflifwas", "Viziren").
6. The freeze is now recorded (file times and hash above), with the post-freeze edit of the pairs file disclosed.

None of these changes the decryptions or the word counts (`check_marks.py` gives the same figures before and after).

**6 Nov 2026, after the maintainer's review.** The reading check asked for a `reading_review` on both entries. Both bare
images are short cipher runs set into letters in clear Swedish: the cipher does not build sentences of its own, and the
only sentences are in the clear text around it, which is an approximate working transcription and not our decipherment.
Following the precedent of other targets (runs set into a clear letter, a single cipher word in a clear holograph), both
entries are now marked **not prose**: 114 as a list of 30 runs with glosses, 104 as one deciphered phrase. The `read_share`
fields were removed and a `reading_review` was added to each (114 grade B, 104 grade A). No count changed: 31 of 40 words
verbatim for 114, 4 of 4 for 104.

## Remaining gaps

- The five gutter holes in 114 need the original or a better scan; the groups run into the fold.
- Codes 15, 93 (or 97), 97 (once each), 108 (once, after Ragocy) and 2 (gutter) are unidentified.
- 79 (t or m) to be settled on more glossed pages, or on a better view of the image-22 group at the fold.
- 67 p and 7 z rest on one bare-run word each.
- The rest of the volume has many more bare runs (see the table above); the frozen key should read most of them.
- Image 115 (the end of the 114 letter) was not read.
- Not compared with the Rákóczi cipher of 2119.5/4 (lead 2243), Cantersten 1648, or DECODE R4201 (Chifferklaver låda II 82,
  1657), which may be this key.
- Only one blind second reader, on a sample; no human has checked any sign.

## Prior art (checked 6 Nov 2026)

Two web searches (Rålamb Vellingk 1657 chiffer/dechiffrering; Rålamb 1657 embassy letters cipher edition) found only
general work on the embassy: Rålamb's diary (ed. C. Callmer, Historiska handlingar 37:3, 1963), Forss 2021 in Legatio,
The Sultan's Procession (2006/2007). No edition or decipherment of these despatches was found. The vetting of 5 Nov 2026
found nothing in DECODE, Tomokiyo or Lasry. Callmer's edition of the diary was not opened, so a printed clear copy of
these despatches in an appendix is not ruled out.

## Files

`SIGN_CONVENTIONS.md`; `pairs_022_023.txt` (key pairs); `key_frozen.tsv`, `FROZEN.sha256`, `key.tsv`; `transcription_heldout_075.txt`;
`transcription_114_pass1.txt`, `_pass2.txt`, `transcription_114.txt`, `decryption_114.txt`, `reading_114.md`,
`translation_114.md`; the same for 104; `VERIFY.md` (the independent report); `profile.json`; `scripts/`:

- `decrypt.py`, `reading.py`, `check_marks.py`, `heldout.py`: standard library only. `python scripts/check_marks.py` and
  `python scripts/heldout.py` run from this folder.
- `fetch.py` (one image at a time, 1.6 s apart, User-Agent `WAINUT-research`), `crop.py`, `sheet.py` (these two need Pillow).

Scans and crops are not in git (`.gitignore`); fetch them with `python scripts/fetch.py scans/max max 22 23 75 104 114`.

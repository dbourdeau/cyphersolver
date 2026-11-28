# guaras1577: Antonio de Guaras to Don John of Austria, London, 15 February 1577 (TNA SP 70/143 f. 93)

**Status:** no write-up (the text is in print, with gaps; this folder adds the key, a held-out test and two of the gaps)

AI agents (Claude Opus 5.5) did all of this work on 27-28 Nov 2026; no person has checked the transcription, the key or
the readings against the images. Times are EST. The order of plan and runs before the held-out test rests on local
file times only; the held-out test itself was frozen and stamped by FreeTSA (RFC 3161) before it was measured.

Pointer: Brice Dudout's printed-editions sweep, pull request #1007, row 3 (Guaras 1577). Announced on #542 on
28 Nov 2026 (04:07 UTC).

## Source

- The National Archives, Kew, SP 70/143 f. 93 (Calendar of State Papers Foreign 1575-77 no. 1264, "Letter in
  Spanish cipher intercepted"). Seen through Gale State Papers Online (subscription), document MC4311981270, images
  94-96 (f. 93r, f. 93v and the endorsement "1577 Feb 15"). A solver needs a State Papers Online login to see them;
  TNA Discovery has no images of SP 70/143. No images or crops are in this folder.
- f. 93r: 13 lines in clear Spanish, then 33 cipher lines. f. 93v: 14 cipher lines, then the clear closing and the
  signature "Antonio de guaras".
- Printed: Kervyn de Lettenhove, *Relations politiques des Pays-Bas et de l'Angleterre* IX (1886), no. 3359,
  pp. 200-201, from this Record Office copy (Marnix's decipherment of 1577). He leaves three gaps (rows of dots) and
  prints ten words in brackets. Internet Archive `relationspolitiq09nethuoft`. The print is used here as the
  plaintext for the key build and as the reference of the held-out test; it is not copied into this folder
  (`scripts/fetch_kervyn.py` downloads the OCR and checks its hash).

## Results, in the order they were registered

1. **Andrew Beling's 1574 Guaras key (catalogue 1001, #743, #892) does not read this letter.** Plan frozen by hash at
   27 Nov 23:27:57 (`plan/PLAN.md`, `plan/PLAN.sha256`, local file times only) before any decoding. Applied unchanged:
   40-44% of tokens are signs of the 1574 alphabet; letter-trigram score -3.36 (reader A), -3.48 (B), -3.59 (merged)
   against about -2.33 for the 5th percentile of Spanish; it does not beat all 200 shuffled-key controls (195, 187,
   181). Verdict by the frozen rule: does not read (`plan/step2_result.json`). The 1577 letter uses another cipher.
2. **No key sheet found.** Davison's letter of 5 Apr 1578 (SP 83/6 f. 9; CSP Foreign 1577-78 no. 768; the calendar
   wrongly suggested Wilson) says he sends "the cipher of Guaras's letters", but no such enclosure is listed in the
   State Papers Online contents of SP 83/6, and none is with the letter (images 10-12 checked). SP 70/144 (Wilson,
   10 Mar 1577, sending "two letters of Antony Guerras", CSP no. 1326) has no Guaras enclosure either. Checked 27 Nov
   about 23:30-23:40 (local times). **The Escobedo key in SP 106/1 f. 116 is a different cipher.**
   DECODE record 340 ("TNA_SP106/1_ElizabethI_f116", a Spanish key of 1577, receiver "Elegdedo"; found by the cold
   check's prior-art search) was fetched from State Papers Online on 28 Nov 2026 at 01:18 EST (SP 106/1, document
   MC4323480002, image 120; not in git). The sheet is headed "Cyphra Escovedi": Don John's secretary Juan de
   Escobedo's cipher, listed in the volume's index as "Escovedo, Flanders, 1577, 43A, 58" and "Juan, Don, & Escovedo,
   58"; "Elegdedo" is a misreading of Escovedo. The index lists no Guaras cipher. One blind AI helper (Claude Opus
   5.5) transcribed the sheet in our shape notation (`escovedo_sheet/`, 213 cells): a digit-based alphabet
   (B 3, D 2, E 0, F 1, M 7, N 8, O 9, R 10, S 11, Qu b, T thorn) with syllables made of a consonant sign and a
   vowel mark (a 1, e 6, i t, u e), doubled letters with a circumflex, and codes (50 = Senor don Juan). Compared
   with f. 93 (`scripts/escovedo_sheet_check.py`, 01:25 EST, after the held-out test, not frozen): applied unchanged
   to the held-out lines it scores 80 of 165 (0.485), at the mean of 200 shuffled keys (0.481; best 0.643); of 181
   held-out tokens valued by both keys, 12 have the same value (mostly `7` = m). f. 93 has none of the sheet's
   digits 0, 2, 3 or 10, 11 and no code 50, though Don John is its addressee. Checked and ruled out.
3. **The 1577 key, rebuilt from the print, passed a held-out test.** Key rebuilt by aligning the cipher with Kervyn's
   text (Viterbi training, `scripts/build_key.py`; values tuned on build lines, `scripts/tune_key.py`), never reading
   f. 93v lines 1-7, which were fixed as the held-out passage on 27 Nov 23:29:34, before any key work
   (`verification/PASSAGE_FIXED.sha256`). Protocol, key, transcription, passage, reference hash and scripts frozen in
   `verification/MANIFEST_v1.sha256`; its SHA-256 (bba82888...413348) stamped by FreeTSA at 28 Nov 2026 05:46:25 UTC
   (`verification/MANIFEST_v1.sha256.tsr`, verifies with openssl). Measured once at 00:46:36 EST:
   **268 of 318 scored signs right, 0.843, against a best control of 0.372 (mean 0.281, z 15.9): pass**
   (threshold 0.70, margin 0.20; `verification/RESULT_v1.json`). The metric merges c=e and l=t because the OCR of
   the print confuses them; this was set in the protocol before measuring. Without those two classes the same key
   scores 262 of 317 (0.826) against a best control of 0.343 (`scripts/heldout_rescore.py`, run after the test by the
   cold check of 28 Nov, about 01:00 EST; not a registered result). A pass shows that the key is far from random on
   that passage, not that every value is right.
4. **Strict word count (after the test).** Printed words the decode gives letter for letter, with nothing supplied
   (`scripts/word_count.py`): 251 of 509 (held-out lines 42 of 79; build lines 178 of 371 and 31 of 59). The c=e and
   l=t classes are not used here, except for 14 OCR slips of the print listed in the script where the decode gives the
   real word (OCR "lienen", decode "tienen"); with the classes the count would be 252, the extra word being "ello",
   which the decode gives wrongly as "elto". Kervyn's ten bracketed words or phrases (13 words) and his three gaps
   (counted as one word each) are holes: **251 of 525 cipher words read (0.478)**, read in part. The key is a working
   approximation: several signs carry two values in the alignment (below), so about half the words come out exact.
   The reading of the letter as a whole rests on the print.

## The cipher

A homophonic substitution of about 40 signs: letter-like shapes, digits, a u-like double or triple minim, tall
strokes with a crossbar or a loop, and a small cross. About 2,230 signs in 47 lines, with 19 code numbers written
between dots. Visible gaps between groups of signs are not word divisions. `8` stands for "qu". Values:
`verification/key_1577_v1.json`.

Signs whose aligned letters split, so their value is the more frequent one: `t` (a 71 / i 16) and `t2` (i 34 /
a 15), the crossed tall stroke `T` (a 33 / i 17), `y` (t 25 / l 16), `Z` (several), `P` (e, with many c that are
OCR slips of the print), `6` (o, h 12).

Code numbers (one occurrence unless said; "print" = the word Kervyn prints at that place):

| code | where | value | basis |
|---|---|---|---|
| 20 | P1L23, P1L25, P1L28 | estado(s) | three places, print plain |
| 31 | P1L26 | (Su) Magestad | print plain |
| 35 | P1L15 | Consejo | print plain |
| 49 | P1L30, P2L01 | Conde | two places; print in brackets both times |
| 66 | P1L23, P1L31 | libertad (probable) | see gaps below |
| 16 . 0 . 17 | P1L20 | print "alla y aca" | print plain; split not settled |
| 36, 39, 43, 34 | P1L18, P1L19, P1L21, P1L22 | print [gente], [soldados], [armas], [Reyna de Escocia] | bracketed words fall on these codes; one occurrence each, not confirmed |
| 21, 22 | P2L06 | print [frances], [espanol] | as above |
| 59 | P1L17 | unread | Kervyn omits the word (his "si no en publicas" reads "y no en publicas [59]s" here) |

**Open codes, strictly: 8 of 15.** Code 59 is unread; codes 21, 22, 34, 36, 39 and 43 rest on the print alone;
code 66 is probable only. The 16/0/17 split is also unsettled (counted with the print, not as open). Open tokens: 9
(59 once, the six once each, 66 twice). `profile.json` `outcome.codes_open` gives these figures.

## The three gaps and the ten bracketed words

- **Gap 3 and code 66: "libertad", not "carcel" (probable).** Kervyn leaves "le ha puesto en ...." blank (P1L31) and
  prints "[carcel]" where the same code 66 stands earlier (P1L23, "ni la osan poner en [66], ni la tienen sin ella").
  "Libertad" fits both places (Leicester set the man at liberty and showed him great favour; they dare not set the
  Queen of Scots at liberty, nor keep her without it, save with suspicion); "carcel" does not fit P1L31. Not
  confirmed by a third occurrence.
- **Gap 1 (P1L05), "de pocos dias aca que ...., pariente cercano de la Reyna".** The cipher has nine signs,
  `d 6 uy 9 4 9 9 o`; the key gives "nolsossy". A probable reading is a title and "Sussex" (Thomas Radcliffe, Earl of
  Sussex, a kinsman of the Queen), but two signs (`d 6`) do not fit and the reading is not sure.
- **Gap 2 (P1L30), "fue preso .... El Conde de Leicester".** The cipher between "preso" and "el" decodes "relo";
  unread.
- Bracketed words: Conde (twice, both on code 49) is consistent; carcel is contradicted (above); Vuestra Alteza
  (P2L04) stands on two signs `8 z`, not a code; gente, soldados, armas, Reyna de Escocia, frances and espanol each
  fall on a code that occurs only once, so the cipher cannot confirm them.

## Transcription

Two blind readers (AI helpers, Claude Opus 5.5, 27 Nov 23:12-23:26; `transcription/transcription_A.txt` in page order,
`transcription_B.txt` from the last line back) in a shape-only notation (`transcription/TRANSCRIPTION_NOTATION.md`).
After a fixed notation bridge they agreed on 1,910 of 2,263 aligned tokens (84.4%). A third AI helper (Claude Opus
5.5, 28 Nov) settled all 259 disagreement blocks on the image, blind to values (`adjudication_log.tsv`: 167 for A,
39 for B, 30 other, 22 notation only, 1 undecidable), giving `transcription_final.txt`.

Two sign splits were made after the first key build had shown that `uy` and the small cross `t` carried two values
each: a fourth AI helper (Claude Opus 5.5, 28 Nov) was given unlabelled groups from build lines only and asked
whether the shapes differ. `uy` splits by minim count (three minims `uy`, two `uy2`; 27 of 30 sample instances),
applied to all 207 occurrences by shape alone (`transcription_final_v2.txt`, `class_uy.tsv`). The cross `t` splits
by whether the bar crosses the upright (23 of 30; `class_t.tsv`, used as `t` / `t2`). Both splits were made before
the held-out test was frozen, and the helper did not see values for the held-out lines. `Z` (a possible two-way
split, 28 of 31) and `T` were not split.

Doubts: P2L14 one sign under a blot; the torn end of P1L33; P1L12 a struck cluster read `y P`.

## Transcription doubts

- one sign under an ink blot (P2L14, before `u y 6`) - read: ?; checked: image, decode; the blot hides the shape, left open.
- torn end of P1L33 (after `y t`) - read: ?; checked: image, decode; at least one damaged sign at the torn edge, left open.
- struck cluster (P1L12) - read: `y P`; checked: image, decode, transcription (two readers); head least certain of the P clusters.
- cross on `d 6 t 1 P` (P1L12 start) - read: as both readers; checked: image, transcription; cross not visible to the adjudicator, kept on the two readers' agreement.

## Remaining gaps

- Kervyn's gap 2 (P1L30, after "fue preso"): decodes "relo", unread - blocker: no-key-material; several signs carry two values, the key sheet Davison sent in 1578 is not in SP 83/6 or SP 70/144, and the 1577 key in SP 106/1 f. 116 is Escobedo's, a different cipher.
- Kervyn's gap 1 (P1L05): probable "[title] Sussex" only - blocker: no-key-material; as above (`d 6` do not fit).
- Code 59 unread (Kervyn omits the word) - blocker: open-codes; one occurrence.
- Codes 21, 22, 34, 36, 39, 43 rest on the print alone - blocker: open-codes; one occurrence each, so the cipher cannot confirm Kervyn's bracketed words.
- Signs `t`, `t2`, `T`, `y`, `Z` carry two values in the alignment - blocker: no-key-material; no key sheet of this cipher is known (SP 106/1 f. 116 is another cipher); a blind recheck of their shapes is the next step, and only another letter in this cipher could test a corrected key (the held-out passage is used).

## Escalation

- [x] siblings: SP 70/143 contents read for other Guaras items (only f. 93); SP 70/144 (Wilson's two Guaras letters of 10 Mar 1577: no enclosure filed); SP 83/3 f. 101 (Guaras to Don John, 14 Nov 1577, a clear draft); SP 83/6 (Davison, 5 Apr 1578, the key he sent: not filed).
- [x] clear-pages: the clear opening and closing of f. 93 and the endorsement (img02) checked; no decipherment on the leaves.
- [x] known-keys: Andrew Beling's 1574 Guaras key (catalogue 1001) tried under a frozen plan: does not read. The 1577 Escobedo key, SP 106/1 f. 116 (DECODE record 340), fetched, transcribed blind and compared: a different cipher (0.485 on the held-out lines, at the control mean).
- [x] prior art: DECODE public search (Guaras, Guerras, Juan de Austria, Don John, SP 70/143: no record of this letter;
  record 340 above found), Tomokiyo's cryptiana.web.fc2.com (spanish3.htm mentions Guaras's cipher, no key or
  decipherment of this letter), Lasry's published papers (nothing on Guaras); cold check, 28 Nov about 01:00 EST.
- [x] print: Kervyn IX no. 3359 (the decipherment, used) and X no. 3640 (French translation, not used); CSP Foreign 1575-77 no. 1264 and 1577-78 no. 768.
- [x] key-rebuild: key rebuilt by EM alignment with the print, signs split by blind shape rules, values tuned on build lines; held-out test passed.
- [x] retry: gaps, codes and bracketed words retried with the rebuilt key (above).

## Further steps

Tried: the 1574 Guaras key (no); the key sheet Davison sent in 1578 (not found in SP 83/6 or SP 70/144 on State
Papers Online); the printed decipherment as plaintext for a key rebuild (key passes a held-out test). The Escobedo key (SP 106/1 f. 116) is another cipher. Next, in order: a two-way shape split of `Z` and a recheck of `T`, `y` and `t2` on the images (blind to values), then a second held-out
test on a new passage only if another Guaras letter of 1577-78 in this cipher is found (Simancas, Estado, holds
Guaras's letters of these years); a better text of the print than the OCR for gaps 1 and 2.

## Files

- `plan/`: the 1574-key test (plan, hashes, scripts, result, the 1574 key as on main). `step2_key1574.py` read its
  language texts from local copies of Internet Archive `bub_gb_XgWt5lHz3_MC` (Zurita 1580) and `bub_gb_RB9nAr9N5AkC`
  (Pulgar 1780), hashes in `PLAN.md`.
- `transcription/`: both blind readings, the adjudication, the final transcription and the two shape sorts.
- `scripts/`: `fetch_kervyn.py` (download and hash check of the OCR), `build_key.py` (run with `TSPLIT=1`),
  `tune_key.py`, `measure_lib.py`, `measure_heldout.py`, `insample_check.py`, `word_count.py`, `decode.py`,
  `heldout_rescore.py` (the held-out score with and without the OCR classes, after the test). They read
  `kervyn9_djvu.txt` in this folder (not in git). `measure_heldout.py` is the frozen script as run once in the work
  folder; here it refuses (the result exists), and `verification/check_manifest.py` re-checks the freeze.
- `decryption_SP70-143-f93.txt`: the machine decode, line by line.
- `escovedo_sheet/`: the blind transcription of the Escobedo key sheet, SP 106/1 f. 116 (no image), and its notes;
  `scripts/escovedo_sheet_check.py` compares it with f. 93.
- `verification/`: the draft and final protocols, the manifest, the FreeTSA query, token and certificates, the
  result, the frozen key, the held-out passage and the frozen copies of the scripts; `check_manifest.py` re-checks
  every hash and the token.

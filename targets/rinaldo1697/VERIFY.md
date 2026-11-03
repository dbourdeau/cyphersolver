# Independent verification: rinaldo1697 (Rinaldo d'Este to "Marchese Taddeo", 6 Jun 1697, cc. 73r-73v)

> Packaging note (3 Nov 2026): four validation files named an AI vendor and were renamed (`pass1_R.txt`, `pass1_V.txt`,
> `pass2_R.txt`, `pass2_V.txt`); the file names below follow the new names. The report is otherwise unchanged. Its counts
> and findings predate the corrections listed in `NOTES.md`.

Verifier, 3 Nov 2026. Adversarial check before any contribution. No solver file was edited; only this file was added.

## Verdict

**fix**. Recommended status: **read in part** (as claimed). The letter key holds: a reversed Italian alphabet that
reads the cipher on 73r and on 73v. But the folder has one certain misreading that created a false key value (10 = i),
a false method claim (73r "pass 1 by eye"), a mistranslated phrase on 73v, unused gloss values, and vendor names and
local paths that must not leave WAINUT.

## 1. Blind transcription (done before opening transcription, key, decryption or readings)

I read NOTES.md only to locate images. I then cut my own full-resolution crops from `scans/c0_cipher_all.jpg` (73r) and
`scans/c1_cipher.jpg` (73v) and transcribed every cipher group on 73r L02-L11 and 73v V01-V17. That is 214 groups, about
420 digits, including all of the held-out page (73v).

Comparison with `transcription_c73.txt`:

| place | mine | solver | settled on a full-size crop | who was wrong |
|---|---|---|---|---|
| V15, *ministro*, 2nd group | 16 | 10 | **16**: tall 6 with a looped bowl and a hooked ascender, the same form as every 16 on the page. The 0 of this hand is a small o (as in 20). | solver |
| V15, *ministro*, 4th group | 16 (blotted) | 10 | Not fully settled: an ink blot. The visible form has a tall hooked stroke, which fits 6 and not the small 0. Probably 16. | solver, probably |
| V06, end of line, "Sʀ." | cipher? (5 + rho-2, i.e. 52) | [TXT] ("Sp.") | Not settled. The first sign has the long-s-like form of this hand's 5 (compare "15." on V09). The second is the rho-shaped 2 of the cipher hand, not a clear p. The gloss reader's own note (`validation/gloss_raw_V.txt`) puts "Caggio" just after it. | open; the solver should mark it doubtful, not silently treat it as text |
| L03, "22 12 7" | first read as 22 21 12 7?, then 22 12 7 | 22 12 7 | 22 12 7 | none |
| L07, 13 18? 12 | 13 ?8 12 | 13 18? 12 | doubtful on both sides | none |

Raw disagreement: 3 of 214 groups (1.4%). After settlement: 1 certain solver error and 1 probable solver error (both in
*ministro*), and 1 open case (V06). No error on my side survived. On 73r the two transcriptions agree group for group.

Gloss read by me over the sample (73r L03, L07-L10; 73v V08, V09, V11, V12, V14). It agrees with the letter key
everywhere I could read it, and it gives code values that the solver lists as unidentified:

- V09: "Sud.ti(?) di S.M.C. che" over **25 . 21 16 . 131 . 187**. So 131 = S.M.C. (Sua Maestà Cattolica) and
  187 = che. 25 is probably "sudditi", but the reading is not certain.
- V14: "che" over the second **187**. That confirms 187 = che twice.
- V12: "ordina[to] a p **le** n i p o t e" over **110 24 7 12 . 24 . 11 189 13 16 11 12 7 20**. So 189 = le, and the
  text is "a p[le]nipotenz. catolici" ("to the Catholic plenipotentiaries"), not "ni potenz. catolici" ("the Catholic
  powers").
- V08, V12: "ordini" over 110 and "ordinato" over 110 24 7 12. The gloss confirms 110 = ordin-, which the solver gives
  only as "proposed".
- V07: the gloss over 15 16 8 7 6 183 reads more like "s i s t u a zione" than "l i s t u". The decoded "listu[183]" is
  weak, and the translation "institu-" is a guess.

## 2. Rebuild

There is no separate decrypt script: `scripts/check_marks.py` rebuilds `decryption_c73.txt` and runs the checks. I ran
it in a scratch copy:

- `decryption_c73.txt`: byte-identical to the folder's copy (cmp).
- stdout: identical to `validation/check_marks_output.txt`. Exit 0.
- Tamper 1: changed "di costi" to "di costa" in the marked reading. Result: `FAIL V11: unmarked departure`, exit 1.
- Tamper 2: changed a transcription digit (V11 22 12 to 22 20). Result: FAIL, exit 1.
- Tamper 3: corrected *ministro* to 14 16 13 16 8. Result: exit 0. Held-out coverage rises from 81/88 to 83/88 (94.3%).

The check works. It does not check the translation or the word split (see section 5).

## 3. Held-out test

The key was frozen on 73r and applied to 73v. The test was scored only with a small Italian letter-bigram model:
frozen key -2.943; shuffled tables mean -3.658, max -2.940; 1/1000 shuffles score as high. That margin is effectively
nil, as NOTES admits. The test was **not** graded against the independent text, the 73v gloss, although the gloss
covers much of 73v (decoro, rinovati li ordini, defonto, costì, ordinato, plenipotenz., catolici, congresso di pace,
assistino, ministro). The real evidence is that the frozen key gives Italian words that match the gloss letter for letter
wherever I could read the gloss. The test should be rerun against the gloss letters. The "7 groups without a frozen
value" include the two misread 10s; corrected, 83/88 letter groups have a frozen value.

## 4. Counts and honest headline

Recount from `check_marks.py`: 79 words in the cipher reading: 42 verbatim, 4 with a marked repair, 7 code words with a
proposed value, 26 open codes. Read as sense: 46/79 = 58%. That is far below Dan's ~95% bar, so **read in part** is
correct, and is the most the folder can claim.

Using the gloss values above (187 ×2, 131, 189 ×4 if "le" holds elsewhere, 110 promoted) would close up to about
8 more holes. That is still well under 95%. The letter text itself is solid: 42+4 words follow mechanically from a
systematic key.

Honest headline: *"Read in part: 46 of 79 cipher words (58%) read from the groups (42 verbatim, 4 with marked
repairs); 7 code words carry a proposed value and 26 are open. Letter key (reversed alphabet) confirmed against the
contemporary gloss on both pages."*

## 5. Readings, sentence by sentence

- `reading_marked_c73.txt`: **B**. Faithful to the groups and holes are marked, but several weak places are not named:
  - "cot." (probably *cotesta*) is not glossed.
  - "sime" (L08) is not a word.
  - "listu[183]" disagrees with the gloss.
  - "mi{n}is" rests on the misread 10.
  - "a p [189 ?] ni pote-" is split wrongly.
  - V06 is treated as ending in text.
- `reading_c73.md`: **C**. As continuous sense, 73r is mostly holes ("[19P ?male] [189 ?] [190 ?] [188 ?] fede [130 ?]
  [191 ?]"). Its errors:
  - "Catholic powers" should be "Catholic plenipotentiaries" (the gloss reads "p le nipote").
  - "compendo" is translated "I understand" (= *comprendo*) with no mark that a letter is supplied. The cipher has
    c-o-m-p-e-n-d-o; *compiendo* ("fulfilling") is just as possible.
  - "institu[183]" is a guess against the gloss.
  - "of Sp." treats a possible code group as clear text.
  - "si in [94 ?Francia]" and "[19P ?male]" rest on one gloss reading each.
  - The context paragraph (Ryswick, Charles II) is plausible but labelled unverified, which is correct.

## 6. Vendor names and local paths (must be removed before anything leaves WAINUT)

- `validation/pass1_R.txt`, `validation/pass1_V.txt`, `validation/pass2_R.txt`,
  `validation/pass2_V.txt`: vendor names in the file names.
- `scripts/gloss.py` line 18: provider and model name strings.
- `scripts/gloss.py` lines 3-4 and `scripts/pass_blind.py` lines 4-5: hard-coded local user paths.
- Both scripts import `llm_direct`, which is not in the folder, so they cannot be rerun by anyone else.
- `scripts/__pycache__/` is present. Do not commit it.
- `scans/` holds images. Do not commit them.

Method claim: NOTES and the transcription header say 73r pass 1 was done "by eye". But `validation/pass1_R.txt`
is a model output (its errors include 198, 142, 620, 122) and `validation/p1r.log` logs token counts for it. Both 73r
passes were model runs. NOTES must say so. Only this verification included a pass by eye.

## 7. Prior art

One web search (Rinaldo d'Este 1697 lettera cifrata Rangoni Ryswick plenipotenziari Estense Campori) found no edition or
decipherment of this letter. It found only biographies and unrelated catalogue records (e.g. a Rinaldo letter of
1 Jan 1697 at the Morgan Library).

## Must fix before a PR

1. V15 *ministro*: transcribe 14 16 13 16 8 (4th group marked doubtful, blotted). Drop the key row "10 i later" and
   "(and 10)" from NOTES. Held-out coverage becomes 83/88.
2. Correct the method claim: 73r pass 1 was a model pass, not by eye.
3. V06 "Sʀ.": mark it as a doubtful sign (possibly code 52), not [TXT]. Take "of Sp." out of the translation.
4. Use the gloss values that are visible: 187 = che (V09, V14), 131 = S.M.C. (V09), 189 = le (V12), and 110 = ordin-
   (gloss). Fix V12-V13 to "a p[le]nipotenz. catolici" = "the Catholic plenipotentiaries". Recount.
5. Mark the emendation in "compendo" in the translation. Name "sime", "cot.", "listu[183]" as weak places.
6. Grade the held-out test against the 73v gloss letters, not only the bigram model.
7. Remove the vendor names (file names, gloss.py) and local paths (gloss.py, pass_blind.py) and the `llm_direct`
   dependency, or keep these scripts out of the PR. Exclude `__pycache__` and `scans/`.

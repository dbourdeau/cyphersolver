# Independent verification: gondi1649 (Gondi to Commendator Galilei, 11 May 1649, c. 1r)

Verifier, 3 Nov 2026. An adversarial check: the aim was to find faults, not to confirm the work. No solver file was edited.
All reruns were done in a scratch copy.

## Verdict

**fix**. The sign transcription and the key hold up. The reading is coherent and the scripts reproduce exactly. Before
anything leaves WAINUT, these must be fixed: a vendor/model name and a local path in `scripts/pass2_blind.py`, the
"vision model" wording, an inconsistent word count, a too-generous "read as sense" figure, and one mistranslation.
Recommended status: **read**, as a transcription job. A contemporary interlinear decipherment covers all of the cipher,
and the catalogue record itself says "decifrata in interlinea". The content was never secret. The new things are the key
and the check of the cipher against the clear.

## 1. Blind transcription

Before opening the transcription, decryption, reading or key files (NOTES.md was read only for the image locations and
the sign inventory), I cut my own full-resolution bands from `scans/c0_cipher_all.jpg` and copied the signs of
L04, L07, L08, L09, L11, L12 and L13. That is 280 signs (184 sign units). It covers the whole held-out passage
L07-L13 except the 3 signs of L10. I also read the interlinear gloss over these lines myself: "si manderà a V.S. la
replica di S.A. alla l[ette]ra di S.E."; "la prima di havere le sud.te risposte del Sig. Vincenzio"; "a Milano furono
sentiti malam.te et biasimati quelli concetti del S. Vic.Re de' quali S.A. con ragione si era risentita"; "aspettando le
risposte categoriche del Sig.r Vinc.o de' Medici". My decoding of the signs agrees with the gloss in the same places the
solver reports.

Comparison with `transcription_c1r.txt` (commas and dots not counted):

| place | mine | solver | settled on a 2x full-resolution crop |
|---|---|---|---|
| L09 *veduto* | 4 6**0** W | 4 6 W | solver right. The omega sign W follows the 6 directly; I had taken the left loop of W for a 0. |
| L09 start | 5 0? B | 5 8 3 | unresolved. I see a loop between the 5 and the B-shaped sign, which the solver's adjudication rejects. Neither side reads the pair, so the reading does not change. |
| L07 *replica* | 6? (blob) | 6? | agree, doubtful on both sides |
| L13 *ragione* | 2 | 2? | agree. On the zoom it looks like a clean 2, so the solver's doubt mark is conservative. |

Raw disagreement: 2 of 280 signs (0.7%). After settling: 0 solver errors found, 1 verifier error, 1 place that stays
unresolved (L09 `5 8`, unread either way). Both of my slips are the same ones as the solver's own pass 1 (see
`validation/adjudication.tsv`), so these two spots are hard to see, not careless. The solver's internal two-pass
figure (39 of 558 signs differing before adjudication, 25 adjudicated places) is documented consistently.

## 2. Rebuild

In a scratch copy, `scripts/decode.py` regenerated `decryption_c1r.txt` **byte for byte**. `scripts/check_marks.py`
(run with UTF-8 stdout) reproduced `validation/check_marks_output.txt` **byte for byte** and exits 0. Note that on a
cp1252 console, "Vicerè" prints as mojibake. That is cosmetic.

Tests of the checker:
- L03 *sta* changed to *sto*, unmarked: `FAIL L03: unmarked departure: reading o, signs 3=['a']`, exit 1.
- The `{?e}` mark removed in *replica*: `FAIL L07: letter e rests on doubtful sign 6 without {?}`, exit 1.
- The restored `{+a}` written as a plain *a*: three FAILs on L07, exit 1.

The checker works. It has one design limit that should be stated: `{+x}` can insert any amount of text with no sign
under it, and `{a/b}` can replace any value. Only the counts keep these honest.

## 3. Held-out test

Rerun: L07-L13, 148 units, 139 agree (93.9%). The 9 others are all values first seen after the freeze. None
contradicts a frozen value. This matches the claim. **The test is graded against the solver's own reading**
(`ASSIGNED` in `check_marks.py`), not against an independent transcription of the gloss. That reading was made with the
gloss in view, so in practice it is gloss-informed. Many frozen values are two-way (30 l|r, 40 n|s, 10 c|b, 9 p|q), which
makes agreement easy. The test shows the key is consistent. It is not an independent proof. NOTES should say so plainly.

## 4. Counts

`check_marks.py`: 102 words; 86 verbatim (code words included); 14 with a marked repair; 2 context-only (273 and the
unread `5 8`). **The solver's report says "84 of 102 verbatim"**, which does not match the script's 86. One figure must
be used throughout.

What the 14 marked words are:
- 9 double letters written once (*accenni, possa, occorra, aspettando, della, scrittura, sett., alla, concetti*). This
  is a convention of the cipher, so these count as read.
- 2 doubtful signs (*replica, ragione*), both settled by sense. Read.
- *che* (L01) and *et* (L12): the signs give an unbarred 5 (o) and an unbarred 4 (u/v). The reading takes the gloss
  value. Read with a repair.
- *a* (L07): a word with no sign at all, restored. This is not a read word.

NOTES says "100 of 102 (98.0%) read as sense". The honest form: **98 of 101 sign-bearing words are read from the signs
under the cipher's own conventions (97.0%)**. Two of those 98 (*che*, *et*) rest on a value repair. One unit is unread
(`5 8`), and one code (273) is supported only by its place under the gloss "Vic.Re". Even on the strictest count, which
drops *che*, *et*, 273 and *pesar*, the figure is 94/101 = 93%. That is close to Dan's 95% bar but just under it. On the
normal count it is clearly above. **Status "read" is defensible.** The headline should give the 97% count with its
definition, not 98%.

## 5. Reading files

| file | grade | weak places |
|---|---|---|
| reading_marked_c1r.txt | A | L01 *pesar* (p-e-n/s-a-l/r; *pensar* would need one more sign; the gloss has "pensiero di") is a forced literal reading; L01 *{che/o}*; L09 `5 8` unread; L12 *{et/u}*; L13 273 context-only. All are marked. |
| reading_c1r.md | B | Cipher parts as above. The clear connecting text is read loosely and not marked as rough: "Se già havessi detto già a V.S." (*già* twice, doubtful) and "portarla a S.A." (I read the clear as "portar all'A.S."). Both should be marked rough or put in `[...]`. |
| translation_c1r.md | B | **Mistranslation:** "da far **la prima di** aver veduto" is "to do **it before** having seen" (*farla* + *prima di*). It is not "to make the first one before". "weighing" for *pesar* is a stretch, though the note says so. Otherwise the sense is right. |

Read as sentences, the cipher text makes sense throughout. Galilei is to find out whether S.E. thinks nothing more is
needed, or does not like having him there. S.A. has not yet decided on his recall and is waiting for Vincenzio de'
Medici's answers. S.A.'s reply will be sent once those answers are in. The Viceroy's ideas were very badly received in
Milan, and S.A. had rightly taken offence.

## 6. Vendor names and local paths

Searched the folder, excluding images:
- `scripts/pass2_blind.py` line 42: [redacted for the PR: a model-provider name and a model name in the call]. **Must not ship.**
- `scripts/pass2_blind.py` line 6: [redacted for the PR: an absolute local path in `sys.path.insert`]. **Local path. Must not ship.**
- `scripts/pass2_blind.py` line 1 docstring ("a vision model") and NOTES.md line 42 ("a separate vision-model run").
  Reword to "a separate AI language-model agent".
- `scripts/__pycache__/decode.cpython-314.pyc` exists and must not be committed.
- `scans/` (about 60 MB of JPG/PNG) must not be committed. NOTES already says so.
- "WAINUT" appears in NOTES and in the fetch User-Agent. That is allowed.
- [redacted for the PR: one line naming an archive outside this target that is not mentioned.]

## 7. Prior art

One web search (Gondi, 1649, cipher, Galilei, commendatore, Vicerè) found no edition or decipherment of this letter. The
results were only Gondi papers at Penn (Kislak) and the Morgan, and a book on Gondi's 1634 mission. This agrees with the
solver. Again: the catalogue record states that the letter is deciphered between the lines, so the content is not new.

## Must fix before a PR

1. Remove the vendor/model name and the local path from `scripts/pass2_blind.py` (or leave the script out). Reword
   "vision model" in that script and in NOTES.md.
2. Leave out `scripts/__pycache__/` and `scans/`.
3. Use one consistent count (the script gives 86 verbatim; the report says 84). Restate the headline as 98 of 101
   sign-bearing words (97.0%), with *che*/*et* as value repairs, the restored *a* not counted as read, `5 8` unread
   and 273 context-only.
4. Fix the translation of "da far la prima di aver veduto" to "to do it before having seen".
5. Mark the loosely read clear text in `reading_c1r.md` as rough ("Se già ... già", "portarla a S.A.").
6. State in NOTES that the held-out test is graded against the gloss-informed reading, not against an independent text.

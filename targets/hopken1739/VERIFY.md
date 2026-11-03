# Independent verification, catalogue 1771 (planned target hopken1739), 3 Nov 2026

Verifier: an AI language-model agent, adversarial, working separately from the solver. No solver file was edited; the
rebuild and the failure tests ran in a scratch copy.

## Verdict

**fix**. The recommended status is honest: **read in part** for the glossed despatches, **decoded, not read** for postscript
263. The digits hold up, the rebuild is byte-identical, check_marks works, and the held-out test is real. Before this
goes out, the key needs cleaning: it carries EM artefacts that the readings count as "read on single values".

## 1. Blind transcription (image 260 left page, the held-out passage)

Before opening any transcription, decryption, reading or key file, I transcribed all 164 groups of the 260 left page from
full-size crops. I also read the gloss over the page myself.

- Raw disagreements with transcription_img260_1740.txt: **2 of 164 (1.2%)**.
  - h12, group 3: I read 1222; solver 1228. On a 3x crop the last digit is clearly an 8 with its loop. **I was wrong.**
  - h11, group 13: I read 1501; solver 1601 (solver pass 1 had 1501, blind pass 2 had 1601). On 3x and 4x crops the
    second digit is a bowl with a rising stem. In this hand the 5s of the next group (1551) have the same shape, and the
    strike-through runs across the top of the digit. **The image does not settle it.** NOTES calls 1501 a "pass-1 error",
    but that is not shown, and the group should carry "?". It does not change the decryption, because 1501 and 1601 both
    = s in the frozen key and in the final key.
- Settled: 0 confirmed solver errors, 1 unresolved (0.6%), 1 verifier error.
- Both readers flag the same two uncertain groups, 1000? (h04) and 1222? (h08).
- Gloss: my reading of the interlinear French matches the solver's gloss lines word for word, including the run
  boundaries ("stipulées" running onto 1591, "ce" over the lone 1471 of h07).
- Postscript 263, all 55 groups. This check was **not blind**, because the decryption had already been opened. Agreement
  is 55/55. One thing was not recorded: a small superscript "o" above the second digit of **1363** (p02). It may be a
  correction or a flag, and it should be noted in bare_263.tsv.

## 2. Rebuild

- FROZEN.sha256: both hashes (key_frozen_heldout_test.tsv, pairs.tsv) verify.
- `decode.py; make_reading.py; check_marks.py` in a scratch copy: all 12 decryption/transcription/reading files are
  **byte-identical** to the folder. check_marks prints OK and the word counts below.
- Injected departures. An unmarked letter change ("Empire" -> "Empere" in 260 h05) **FAILS** (exit 1), and so does an
  extra word past the last group (FAIL). This works.
- Limitation, by design: the text inside a mark `[1234 ?text]` is never checked. Writing `[1618 ?xyz]` over a confirmed
  value still passes; the word simply moves to the "gloss" count. The readings come out of make_reading.py, so the marks
  are machine-placed, not hand-placed. That is fine, but the PR should say so.

## 3. Held-out test

Rerun with `heldout_test.py key_frozen_heldout_test.tsv heldout.tsv`. The script needs these two arguments, and the
NOTES rebuild line leaves them out. The result is reproduced exactly: 138/164 groups in the frozen key, **111 (68% of all,
80% of known) match the gloss**; 500 shuffles give a mean of 25.5 and a maximum of 36. The test is graded against the
**independent contemporary gloss**, not against the solver's own reading, so it is a genuine test that the code list is
real. The alignment lets the gloss skip freely, which makes it lenient, but the shuffled control uses the same values and
lengths, so the comparison is fair.

Caveat: the **final** key.tsv was rebuilt with the 260 pairs included. The 260 reading's 57%/15%/28% split is therefore
**not** a held-out figure. Run against the final key, the "held-out" score rises to 140/164 (85%), which is circular. The
frozen key also had 1199 = "rain" (EM artefact), when 1199 is "in" 12/12 in the final key. The seed 1199 "in" was added
only after the test.

## 4. Counts (rerun of check_marks)

| Document | cipher words | confirmed key | single/mixed | gloss only |
|---|---|---|---|---|
| dialogue 255-257 | 226 | 142 (63%) | 45 (20%) | 39 (17%) |
| enc2 257 | 12 | 5 (42%) | 3 (25%) | 4 (33%) |
| 260 (final key, not held-out) | 67 | 38 (57%) | 10 (15%) | 19 (28%) |
| **all glossed** | **305** | **185 (61%)** | **58 (19%)** | **62 (20%)** |
| 263 postscript | 55 groups | - | - | 15 groups not in key; no text |

Honest headline: from the key alone, **61% of glossed cipher words** rest on confirmed values. Every word of the French
is known only because the 18th-century decipherer wrote it over the numbers. On Dan's rule this is **read in part**: the
95% bar is reached only with the gloss. Postscript 263 is **decoded, not read**. The 58 "single/mixed" words include
words carried by EM artefacts (below), so 19% overstates what single values really support.

## 5. Readings graded

- **reading_dialogue_dec1739.md: B.** It reads as coherent French because it is the contemporary gloss, and the English
  is faithful. Weak places: 256 r13 (5 marks), 256 r15 (8 marks: "aux instances", "du ... Sultan même"; 1221 du is
  marked "no counterpart" because the gloss leaves out "du"), 256 r16 (blot, "flegme" on the gloss alone), 257 r47 (the
  1260 que vs "stipulé" mismatch, "fait"), 255 r05 (blank in the gloss), 255 r07 ("Cour, ni"). The identification
  B = Villeneuve rests on content only, and the file says so.
- **reading_enc2_dec1739.md: B.** It is short and coherent. Weak places: "entamer" (1415, a mixed value whose other
  readings are "eu" and "xmemes"), "Le grand Vizir" (code word set by hand, marked), "proposoit", "vingt" (1222 mixed).
- **reading_img260_1740.md: B.** It is coherent, and the English is good. Weak places:
  - h04: "Suede est" is carried by **1481 = "suedeest"**, an EM artefact that crosses a word boundary. Meanwhile the
    hand-set code word **1532 = Suède** is marked "no counterpart" `[1532 -]`. The alignment is wrong there.
  - "fait" rests on the gloss.
  - h09 "amitié": 1474 = "damit", an artefact.
  - h11 "ombrage" is counted as a single-value word through **1573 = "itombra"**, an artefact.
  - h12 "mauvaises desseins" is mostly gloss.
  - h13 "intentions" is partly gloss.
- **reading_ps_img263.md: C as a reading** (correctly labelled "decoded, not read"). Two problems. The file says it was
  "Decoded with the frozen key", but decode.py uses the final key.tsv. The page has the clear Swedish word "angående", so
  a French syllabary decode may be meaningless.

Implausible key values that should not stand as "single" or "mixed": 1481 suedeest, 1573 itombra, 1474 damit, 1507 xpu,
1097 ppor, 1621 iho, 1106 epe, 1240 ommo, 1467 tba, 1415 eu/xmemes/entame. A syllabary does not have groups for "itombra"
or "suedeest". These are segmentation fillers.

## 6. Vendor names and paths

I grepped every md/txt/tsv/py/json/sha256 file in the folder (scans excluded) for vendor and model names and local
paths. **No hits.** scripts/__pycache__/ (two .pyc files) and scans/ (jpgs) must stay out of any
commit.

## 7. Prior art (one search)

There is no edition or decipherment of these Höpken-Carlson ciphered enclosures. Related: S. Kuneralp's edition *Les
rapports de Louis-Sauveur marquis de Villeneuve ... (1728-1741)*, vol. 4 (1736-1739), ISIS Press, which mentions
approaches by Höpken and Carlson. Villeneuve's own report of the same conversation could appear in vol. 4 or 5. That
would be an independent check on "B = Villeneuve", and possibly a French-side account of the same text. It is not a prior
decipherment.

## Must fix before a PR

1. Remove or demote the word-crossing EM artefacts from key.tsv (1481, 1573, 1474, 1507, 1097, 1621, 1106, 1240, 1467,
   1415), regenerate the readings, recount, and update the headline numbers.
2. 260 h04: align 1532 = Suède (code word) and do not mark it `[1532 -]`.
3. State plainly that the 260 word counts use a key trained on 260. Quote the frozen-key figure (111/164 = 68%, shuffled
   max 36) as the held-out result.
4. Mark 260 h11 group 13 as doubtful ("1601?"; the image allows 1501). Correct the NOTES line that calls 1501 a pass-1
   error.
5. reading_ps_img263.md: "frozen key" -> "final key"; note the superscript mark on 1363 in bare_263.tsv.
6. NOTES rebuild line: add `python scripts/heldout_test.py key_frozen_heldout_test.tsv heldout.tsv`.
7. PR text: describe the readings as transcriptions of the contemporary decipherment. The code list confirms them; it is
   not a break. Keep scans/ and __pycache__/ out of the commit.

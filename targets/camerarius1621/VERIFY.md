# VERIFY camerarius1621 (n.194), 3 Nov 2026: independent adversarial check

Verdict: **fix**. Recommended status: **read in part** (borderline; about 94-95%). It can go back to "read" only if
the fixes below are made and a re-count still clears 95%.

## 1. Blind sample (fol. 416r, scan 799, the whole page)

Method: I opened only NOTES.md (to find the images) and the raw scan `46_p799_full.jpg`. I cut my own bands at 1.8x
and detail crops at 3-5x, wrote my reading to scratch, and only then opened `code_groups_n194.tsv` and
`transcription_n194.txt`. The sample covers 12 code groups, 9 of them glossed, and about 190 clear-text words
(roughly 1,000 letters and digits). n.194 is itself the held-out letter, so the sample falls inside the held-out
passage.

### Code groups (digits)

| solver | blind | settled on full-size crop | wrong side |
|---|---|---|---|
| 1682 | 1683 | **1682** (flat z-shaped 2; the 3 in this hand is round) | verifier |
| 1393 | 1397 | **1394**: the last sign is the same form as the 4 in 1684/1344 and unlike the round 3 inside the same group | solver (both sides wrong) |
| 43 | [1]43 | unresolved: a small comma-like stroke stands before the 4; probably a pen mark, possibly a short 1 | open |
| 108, 2095, 2130, [?]858, 1344, 2117, 1684, 484, 410 | same | agree | - |

Raw: 3 of 12 groups disagree (25%); 3 of about 42 digits (7%). Settled: 1 solver digit error (1393 should be 1394;
the value Heilbronn does not change, but the key entry number is wrong), 1 verifier error, 1 open.

### Glosses

| group | solver gloss | blind gloss | settled |
|---|---|---|---|
| 1682 | "K. in D." -> König in Dennemarck | "K. i. B." | At 5x the last letter has two bows and a waist, so I read **B** (König in Böhmen). The solver is probably wrong. This gloss is the **only** source of key entry 1682. |
| 2130 | "Oberpf." | "Obrst." | "Oberp." The solver is right. |
| 1344 | "? (faint, not legible)"; value Großhofmeister taken from n.63 | "M. Lesse?" | The gloss reads **"Gr. hofm."**, which is legible and agrees with n.63. Both of us read it short; the value stands, and this adds one more held-out agreement. |
| 43 | "[?Freyh.] v. Dona" | "Fur..tch / Burggr.? v. Dona" | "v. Dona" is certain; the first word is open. |
| 108, 2095, 858, 1393(4), 2117 | agree | | |

Raw gloss disagreement: 4 of 9. Settled: solver wrong 1 (1682), under-read 1 (1344), right 1 (2130), open 1 (43).

### Clear text

My blind clear text was rougher than the solver's. About 35 of about 190 words were raw holes or disagreements
(~18%). Settled on crops in the solver's favour: violentiā (not "credentiā"), Landtrosten, mitt ziehen,
"ein hohes verlangen", "oder einen Extract". Still open, and **unmarked** in the solver's transcription: l.80
"verlang[en]" (I see "hinlang-"), l.92 "schicken" (I see "schreiben"/"schriben"), l.79 "motus" vs "modus",
l.71 "fürchte ich" vs "förchte dz", l.75 "den" vs "zum/dem durchzug". On the other side, l.73 can be partly read
("hett dz drei-"), where the solver has two [?...].

## 2. Rebuild

I copied key.tsv, n194/ and scripts/ to scratch and ran `python -I scripts/check_marks.py n194`. Result: "result: ok",
95.3%, and the `decryption_n194.txt` it wrote is **byte-identical** to the folder copy. Negative test: I changed the
reading of seq 14 (1372) to "Lübeck" without a mark, and the script returned `FAIL 14: unmarked departure` with
exit 1. The checker works as described.

Limits of the checker:
- pass1 and pass2 are both the solver's own reads, so they cannot catch 1393/1394.
- `order_check.py` skips groups below 100 (so 43 is never tested) and folds every "König in X" into "König", so it
  cannot see that 1682/1683 Dennemarck, 1684 Böhmen, 1686 Engelland and 1687 Dennemarck interleave.
- The ORDER printout in `heldout.py` shows 43 "v. Dona" between A and Audienz, and 858 between Dennemarck and
  Gesandte, but the script never flags anything (`bad` is unused).

## 3. Held-out test

Rerun gives agree 12, disagree 1 (553 "Chur S.", which is only an abbreviation match), and 5 untestable. It is
graded against the **contemporary interlinear glosses** of n.194 (an independent text), as transcribed by the solver.
That is a fair design. Weak points:
- The "frozen from n.63" dictionary is hard-coded, so the claim that it was fixed before n.194 was read cannot be
  checked.
- It tests only 11 distinct groups, and only key values, not the 784 clear-text words that make up 93% of the
  headline.
- 1344 should move from untestable to agree ("Gr. hofm.").

## 4. Counts and honest headline

Solver: 784 clear-text words (37 not read) + 60 groups (57 read) = 804/844 = 95.3%.

Corrections from this check:
- 1682 must be marked doubtful (disputed gloss, sole source).
- 43 must be marked doubtful. key.tsv's own letter table from n.63 gives **o = 43**, NOTES says numbers below about
  70 are single letters, and 43 sits out of alphabetical slot.

That gives 802/844 = **95.0%**, exactly on the bar. Marking the five open clear-text words above would take it to
about 797/844 = **94.4%**.

Honest headline: "n.194 read in part: about 94-95% of 844 words. 55-57 of 60 code groups have values, nearly all
from the contemporary decipherment written over them on the page; the remaining holes are a pasted slip and
microfilm-limited Kurrent." This is a transcription of an already-deciphered letter, not a break.

## 5. Reading files

- `reading_n194.md`: **B**. Mostly coherent sense. Weak places:
  - l.3-4 "[?de] [?Morz]";
  - l.22-23 "[?seiner] [?Bleib] ... [?resignat]" (the sentence does not parse);
  - l.28 1513 unread;
  - l.36 "mit [?...] in hoc p[unct]o";
  - l.72 "violentia zuerhalten", with 1682 disputed (Denmark or Bohemia changes who is to write);
  - l.78-81 under the slip, with "⟨Oberpfalz⟩ mit verlang[en]" unsure;
  - l.83-85: "Herr ⟨Großhofmeister⟩ wie auch ⟨von Dohna⟩ hinaus" has no verb, and 43 is doubtful.
- `translation_n194.md`: **B**. It follows the reading but fills holes by interpretation:
  - "to keep off violence" for "violentia zuerhalten";
  - "[i.e. Solms himself]", which is a plausible conjecture but should be marked as one;
  - "[go] out";
  - "[?Imperial governor]" (the German reads only "[?Kayserlichen] fürsten").
- `decryption_n194.txt`: mechanical output, consistent with the key. It carries the 1393 and 1682 issues.

## 6. Vendor and path grep (must be cleaned before anything leaves WAINUT)

- [Four lines redacted for publication by WAINUT: they named an AI vendor and model and local file paths in
  working files (NOTES.md l.43, a survey table, two survey scripts). NOTES.md was genericised; the survey files and
  scripts are not in this target.]

Fix: leave the two survey scripts and survey/ out of the PR, or genericise them to "an AI language-model agent" and drop
the sys.path line. The "WAINUT-research" User-Agent is allowed. Never commit scans/ (164 MB of jpg) or any image.

## 7. Prior art (one quick search)

The query "Ludwig Camerarius Solms 1622 Bremen Chiffre Clm 10397" found no edition or decipherment of these
letters. The solver's own check already flagged two unseen sources: Schubert, *Ludwig Camerarius* (1955; 2nd ed.
2013), which may quote the glossed passages; and the *Briefe und Akten zur Geschichte des Dreißigjährigen Krieges*
series, which draws on the Munich Camerariana. Check these before calling the content new. The contemporary glosses
are themselves prior art for every glossed group.

## Must fix

1. Genericise or exclude every vendor, model and path mention (section 6).
2. Change 1393 to 1394 in the transcription, code table and key.tsv (Heilbronn unchanged).
3. Re-examine the 1682 gloss ("K. i. B." vs "K. in D."). Mark it [?], and do not let it alone carry the key entry
   "1682 = König in Dennemarck".
4. Mark 43 = von Dohna doubtful. It conflicts with o = 43 in key.tsv and with the alphabetical order. Note the
   stroke before the 4.
5. Update the 1344 gloss to "Gr. hofm." (held-out: 13 agree).
6. Mark the open clear-text words, re-count, and publish the honest figure (about 94-95%, "read in part" unless
   ≥95% after marking).
7. Describe the held-out test accurately: 11 groups, graded against the glosses, key values only; the hard-coded
   "frozen" dictionary cannot be verified.
8. Check Schubert and the *Briefe und Akten* series for prior publication.

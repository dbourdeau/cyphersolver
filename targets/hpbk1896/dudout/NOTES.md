# hpbk1896 / dudout: system B transcriptions and a gloss table (15 Nov 2026), PARTIAL

Contribution to Daniel Bourdeau's target hpbk1896 (catalogue 2646 / 2575 / 2577), building on his first session and on
his 14 Nov Koc sweep (lead and image routes). Images: Koc University, HPBK, CC BY-NC-ND 3.0, not included; links only,
e.g. https://cdm21054.contentdm.oclc.org/digital/collection/HPBK/id/541 . Images were read at full size (2000 x 3500)
from https://cdm21054.contentdm.oclc.org/iiif/2/HPBK:<id>/full/full/0/default.jpg .

## What is here
* `transcription/passA`, `passB`: two independent blind transcriptions (separate agents, neither saw the other) of system B
  sheets 541, 585, 562, 575, 577, 587, 602, 644, 652, 675: every numeral and the clerk's gloss over it, with x,y page
  coordinates, confidence marks and notes (brief: `transcription/BRIEF-PASS.md`). `passA/1070.txt`, `1070_latin.txt`:
  tentative transcription of the clear sheet 1070 (pass A only).
* `transcription/merged_<id>.tsv`: A and B aligned by coordinates (`scripts/align.py`, radius 70 px).
  Numeral agreement A/B: 541 117/119, 585 172/201, 562 282/331, 575 176/183, 577 33/34, 587 132/205, 602 219/259,
  644 123/136, 652 150/209, 675 56/98. The 2/4/6 confusion Daniel describes is real: agreement drops on the pale or fast
  sheets (587, 652, 675).
* `key/`: v1 (24 numerals, glosses of 541+585, some arbitration) and v2 (27 numerals, mechanical rule over the glosses of
  541+585+562, `scripts/build_key2.py`, with `key_v2_evidence.tsv` listing every reading per numeral).
* `prereg/`, `prereg2/`: the two preregistrations, hashes, results and post-hoc miss lists.

## Results (honest)
Structure confirmed independently of Daniel's notes: two-digit numerals = letters (with homophones: alif 67/77; ayn 44/45/59/62;
he 17/25/27), three-digit numerals = words or suffixes (668 = -de/-nde; 745 olduğu; 626 mezkur ...), clear words in between.

Test of the gloss table = does a table built from the clerk's glosses on training sheets predict the clerk's glosses on
held-out sheets? (skeleton/dot-less comparison, 200 within-class shuffles, bar 0.85 and best control + 0.30):
* Test 1 (key v1, held-out 575 + 577, 174 tokens): 0.787, best control 0.420 -> partial.
* Test 2, last (key v2, held-out 644 + 652 + 675; 644 has no clerk glosses, so 0 tokens; 652: 125, 675: 35 = 160): 0.5625,
  best control 0.450 -> failed.
Reading of the misses (post hoc): on 652/675 numeral 49 is glossed ل (ص on 562), 44 ی/ك, 58 ع; numerals 16, 48, 65 do not
occur in training. So one numeral->letter table does NOT hold across all sheets of 1898-1900: either the table changed
(dates: training 541 Sep 1898, 562 Feb 1899, 585 undated; 652 Jul 1898 and 675 Jun 1898 fail), or the A/B transcription
of the pale sheets is too noisy. Splitting the sheets by date and building one table per period is the next step; we
make no claim of a key.

Reading: 541 (7 Sep 1898) is read in part only, with the clerk's glosses: « Hudeyde'de yaveran-ı hazret-i şehriyari'den
kaimmakam Rüşdi ... bir telgrafname'de ... mukarrer ... lazım ... mezkur ... idük », signed Mehmed Kâmil. Other sheets:
decoded, not read. 1070 is headed as the solution of the cipher of 25 Kânûn-ı sânî 1315 (= 6 Feb 1900, the date of 575),
but its key words (fesad, Hicaz, İslam, hilafet, tedbir) do not appear in our 575 decode: no match established.

Percent read: system B 0% by Daniel's rule (the clerk's own reading is not counted as ours).

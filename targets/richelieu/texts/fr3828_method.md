# The nine sibling letters (fr. 3828, 3825, 3835) read with the fr. 3829 key: method and measure

Brice Dudout, with Claude Opus 5.5, 19 Nov 2026. Leads 1577 and 2744; issue #206 (Daniel Bourdeau's request to open
Avenel t. III).

**Status: existing (Avenel 1858), verified with the key.** Avenel, *Lettres, instructions diplomatiques et papiers
d'État du cardinal de Richelieu* III (1858), prints these nine letters with the cipher figures left in place and his
decipherment of each run in a footnote; he says he "recomposed" the cipher from documents of the Affaires étrangères
(note to CXXXV). This work adds an independent check of his glosses with the key recovered from fr. 3829 ff. 87, 89,
the letter-exact text of the cipher, and a small extension of the key.

## Pieces

| Avenel | Pages | Date | BnF (Béthune) |
|---|---|---|---|
| CXIX | 233–235 | [15 (?) Feb 1629] | fr. 3835 no. 15 (9329 fol. 46) |
| CXXXV | 262–263 | 21 Mar [1629], Susa | fr. 3825 no. 28 (9319 fol. 77) |
| CXLVI | 275–276 | 14 Apr 1629 | fr. 3828 no. 8 (9322 fol. 24) |
| CXLVII | 277 | 20 Apr [1629], Susa | fr. 3828 no. 10 (9322 fol. 30) |
| CLIII | 291–294 | 29 Apr 1629, Susa, to the Queen Mother | fr. 3828 no. 17 (9322 fol. 48) |
| CLIV | 294–296 | 30 Apr 1629, Susa | fr. 3828 no. 18 (9322 fol. 51) |
| CLV | 296–297 | 1 May 1629, Susa | fr. 3828 no. 19 (9322 fol. 54) |
| CLVIII | 300–301 | 2 May 1629, Susa | fr. 3828 no. 21 (9322 fol. 59) |
| CLXVII | 321–322 | 25 May 1629 | fr. 3828 no. 26 (9322 fol. 73) |

Folios as printed by Avenel. The Toronto OCR reads 69 and 78 for fol. 59 and 73 (and lead 2744's vetting quotes those).

## Transcription

The figures were read from the page images of Internet Archive `lettresinstructi03richuoft` (University of Toronto
copy; Source archive.org), overlines kept, and compared number by number (difflib alignment) with two independent OCRs:
the Toronto scan's own and the Google scan `bub_gb_OIQItRIybmIC`. Every disagreement, and every figure that neither OCR
confirmed, was re-read on an enlarged crop of the image: all confirmed the visual reading, nothing was changed. The
disagreements were systematic OCR confusions (27→37, 22→33, 25→35 in one; 37→87, 25→26, 52→62, 39→89 in the other).
One figure is marked doubtful: CXIX before note 6, a blotted 30.

| Letter | Figures | Agree OCR A | Agree OCR B | A = B ≠ image | Image only |
|---|---|---|---|---|---|
| CXIX | 198 | 160 | 163 | 1 | 7 |
| CXXXV | 72 | 51 | 60 | 0 | 1 |
| CXLVI | 133 | 92 | 109 | 1 | 6 |
| CXLVII | 46 | 32 | 36 | 0 | 2 |
| CLIII | 167 | 132 | 152 | 0 | 2 |
| CLIV | 168 | 110 | 126 | 0 | 16 |
| CLV | 189 | 148 | 167 | 1 | 5 |
| CLVIII | 134 | 107 | 109 | 0 | 4 |
| CLXVII | 99 | 78 | 86 | 1 | 4 |

## Pre-registered measure (one run)

The protocol (`fr3828_measure/PREREG_fr.md`, in French, sha256 `d98e7dcc…9d44`) was frozen before any run of these
letters was passed through the key, together with the transcription (`4e13e311…d357`; the copy here differs only in
its comment lines, now in English), Daniel's `key.md` and `final.py` @ 9736c436, and the scoring tool
(`fr3828_measure/measure.py`, `eb549a91…8f33`, comments in French, kept as frozen).

- Key: `final.py` @ 9736c436 as it stands: letters 10–38, word codes 39 et, 40 de, 42 la, overline = doubled letter.
  Nomenclator figures are not scored (Daniel named some of them from Avenel's notes in this same volume).
- Held-out portion: CLIV and CLV (333 figures in runs), neither used by Daniel for the key (he cites CXXXV *ne piquer*
  for 33 = u and CXCIX/CCV for 39).
- Reference: Avenel's footnote gloss for each run. Score: edit distance of the decoded run to the best substring of
  the normalised gloss; agreement = 1 − Σ distances / Σ decoded characters.
- Controls: 200 tables with the values of figures 10–38 shuffled (seed 20261119), same score.
- Threshold, fixed in advance: ≥ 0.85 and ≥ best control + 0.30.

**Result: 0.940 against a best control of 0.456 (mean 0.285); thresholds 0.85 and 0.756: passed**
(`fr3828_measure/measure_result.json`; the run reproduces exactly on the transcription in this folder).

## Reading and count

After the measure, every run of the nine letters was decoded with the key (`fr3828_decryption.txt`, unedited) and made
into sentences (`fr3828_reading.md`, translation `fr3828_en.md`). The key was extended under rules written before the
measure: letter values and word codes unchanged; a nomenclator figure gets a value only where Avenel's note glosses it
at that place and the decoded runs beside it agree; nothing taken from CLIV or CLV (`key.md`, "Extension").

Read share over cipher words only (README Conventions, 16 and 19 Nov 2026; `fr3828_measure/count_words.py` on
`word_count.tsv`): a code is one word; a figure valued by Avenel's note at that very place is counted as read (his
printed decipherment), as pre-registered.

| Letter | Read / cipher words | Share | Holes | Class |
|---|---|---|---|---|
| CXIX | 51/51 | 1.000 | 0 | read |
| CXXXV | 24/24 | 1.000 | 0 | read |
| CXLVI | 45/45 | 1.000 | 0 | read |
| CXLVII | 14/15 | 0.933 | 1 | read by the floor for < 40 words (1 hole); recorded "read in part" in `profile.json` because `docs/_texts.py` does not apply the floor yet |
| CLIII | 54/55 | 0.982 | 1 | read |
| CLIV | 48/49 | 0.980 | 1 | read |
| CLV | 54/56 | 0.964 | 2 | read |
| CLVIII | 44/45 | 0.978 | 1 | read |
| CLXVII | 34/34 | 1.000 | 0 | read |
| **Total** | **368/374** | **0.984** | 6 | |

The six holes: CXLVII *septembre* (last figure 29 = a); CLIII, CLIV, CLV twice *le 20 mai* (20 = d in the key, read
as the number, as Avenel says); CLV *veuille* (figures *veule*); CLVIII *maistresse* (figures *mistrese*).

**Stricter count.** If only the figures of Daniel's table count as read (no value taken from Avenel's notes, i.e.
without the extension and the two context readings of 59 in CLVIII): CXIX 49/51 (0.961), CXLVI 44/45 (0.978),
CLIII 48/55 (0.873), CLVIII 42/45 (0.933), CLXVII 31/34 (0.912, 3 holes, over the floor); the others unchanged.
CLIII and CLXVII then fall to "read in part". Under the 19 Nov 2026 rule a reviewer may also count CLVIII's two 59s
(glossed "M. de Mantoue" against the table's "princesse Marie") as holes: 42/45, read in part.

## What the key adds to Avenel

- The figures' own spelling where Avenel modernises or cuts his note short ("…"): *un mauvais efet*, *bénéfice de sa
  colation*, *Vincenes*, *de Meaus*, *Bordeaus*, *coup aus huguenots*, *mal aus Anglois*, *courones*, *afaires*,
  *aler*, *alés*, *s'acommode*, *le Monferat*, *Marilac*, *rejoint*, *juin*, *incontinant*, *des Sevenes*.
- Four small differences with his glosses: CXXXV *mécontent* (Avenel "Mécontentement"); CLIII *la dégast* (42 = la;
  Avenel "Le dégast"); CLV *en veule* (Avenel "En veuille"); CXLVII *septembra* (Avenel "Septembre": a misprint or
  the clerk's slip).
- Three usages not in the fr. 3829 key: 40 used as the syllable *de/dé* inside words; 20 used as the number in
  "le 20 mai"; 59 glossed "M. de Mantoue" in CLVIII against "princesse Marie" elsewhere (left unsettled).
- Ten values: 41 que and nine names (`key.md`).

## Limits

- Everything rests on the figures as Avenel printed them. The BnF manuscripts (fr. 3828, 3825, 3835) are not
  digitised and were not seen; an editor's misprint cannot be excluded (Daniel found one on fr. 3829: 16 for 19).
- Avenel's footnotes were read during the transcription (they are printed on the same pages). The key itself comes
  from fr. 3829 without them, so the measure stays a test of the key against an independent decipherment.
- The clear text is transcribed only around the figures, abridged elsewhere.

## Credits

D.-L.-M. Avenel (1858) for the edition and its decipherment; Daniel Bourdeau for the fr. 3829 key; BnF (Archives et
manuscrits) for the shelfmarks; Internet Archive for the scans and OCR (Source archive.org).

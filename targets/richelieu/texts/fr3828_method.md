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
`word_count.tsv`): a code is one word. **Strict count** (owner's decision on #813, 19 Nov 2026): a code value fixed from
Avenel's printed decipherment of the same letters, or from context, is a hole at the place where it is counted; values
written in `key.md` after the fact do not make it sure. So the ten values of the Extension (41, 55, 61, 62, 67, 68, 69,
95, 96, 97), 59 read "M. de Mantoue" in CLVIII and 84 read "les Anglois" in CLIV are holes, written `{x}` in
`word_count.tsv`. So are the base codes 54 (Monsieur), 59 (princesse Marie) and 60 (Mme de Longueville) (20 Nov 2026,
owner's question on #813): they do not occur in ff. 87, 89, and their values are glossed in Avenel's notes to these
nine letters (59 and 60 only there, 54 also once in 1630); see `key.md`, "Where each base code comes from".

| Letter | Read / cipher words | Share | Holes | Class |
|---|---|---|---|---|
| CXIX | 49/51 | 0.961 | 2 | read |
| CXXXV | 19/24 | 0.792 | 5 | read in part |
| CXLVI | 42/45 | 0.933 | 3 | read in part |
| CXLVII | 13/15 | 0.867 | 2 | read by the floor for < 40 words (`floor_used`, 15 cipher words, 2 holes) |
| CLIII | 48/55 | 0.873 | 7 | read in part |
| CLIV | 45/49 | 0.918 | 4 | read in part |
| CLV | 53/56 | 0.946 | 3 | read in part |
| CLVIII | 41/45 | 0.911 | 4 | read in part |
| CLXVII | 27/35 | 0.771 | 8 | read in part |
| **Total** | **337/375** | **0.899** | 38 | |

The holes: CXLVII *septembre* (last figure 29 = a); CLIII, CLIV, CLV twice *le 20 mai* (20 = d in the key, read as
the number, as Avenel says); CLV *veuille* (figures *veule*); CLV *articles* (figures *articlesignes*, one s); CLVIII *maistresse* (figures *mistrese*); the Extension
values where they are read (CXIX 68, 69; CXLVI 69; CLIII 55, 61, 62, 95, 96, 97; CLXVII 41, 67, 68); CLVIII 59 twice
(*M. de Mantoue*, against *princesse Marie* in the table); CLIV 84 twice (*les Anglois*, *mal aus Anglois*, Avenel
nn. 10, 11); the base codes 54, 59, 60 wherever they occur (15 words: CXXXV 54, 59, 60 ×3; CXLVI 54 ×2;
CXLVII 54; CLIV 54; CLVIII 54; CLXVII 54 ×2, 59 ×2, 60).

Corrected 23 Nov 2026 (owner's review of #813, 20 Nov): CLXVII has five 52 in the figures and the table had four
(the one in "je suplie {52} de se faire monstrer mes lettres" was missing), so 27/35; CLV *articles* is a hole, the
figures giving *articlesignes* with one s (53/56, read in part). The filed 20 Nov total was 337/374 (0.901); the
earlier counts below were also on 374 words, without that 52.

The strict count filed on 20 Nov 2026 before the base codes were traced (352/374 = 0.941, five letters read) is
replaced by this one.

The count filed first (19 Nov 2026) took the values fixed from Avenel's note at the place as read, as pre-registered:
368/374 (0.984), all nine letters read. It is replaced by the strict count above; the measure itself (0.940) is not
affected, since it uses the letter values 10-38 only.

The plaintext of these nine letters is Avenel's printed decipherment, checked with the key: "read from existing
decipherment" in George Lasry's categories (`profile.json`, `outcome.parts`).

## What the key adds to Avenel

- The figures' own spelling where Avenel modernises or cuts his note short ("…"): *un mauvais efet*, *bénéfice de sa
  colation*, *Vincenes*, *de Meaus*, *Bordeaus*, *coup aus huguenots*, *mal aus Anglois*, *courones*, *afaires*,
  *aler*, *alés*, *s'acommode*, *le Monferat*, *Marilac*, *rejoint*, *juin*, *incontinant*, *des Sevenes*.
- Four small differences with his glosses: CXXXV *mécontent* (Avenel "Mécontentement"); CLIII *la dégast* (42 = la;
  Avenel "Le dégast"); CLV *en veule* (Avenel "En veuille"); CXLVII *septembra* (Avenel "Septembre": a misprint or
  the clerk's slip).
- Three usages not in the fr. 3829 key: 40 used as the syllable *de/dé* inside words; 20 used as the number in
  "le 20 mai"; 59 glossed "M. de Mantoue" in CLVIII against "princesse Marie" elsewhere (left unsettled).
- Ten values: 41 que and nine names (`key.md`), from Avenel's notes; holes in the strict count.

## Limits

- Everything rests on the figures as Avenel printed them. The BnF manuscripts (fr. 3828, 3825, 3835) are not
  digitised and were not seen; an editor's misprint cannot be excluded (Daniel found one on fr. 3829: 16 for 19).
- Avenel's footnotes were read during the transcription (they are printed on the same pages). The key itself comes
  from fr. 3829 without them, so the measure stays a test of the key against an independent decipherment.
- The clear text is transcribed only around the figures, abridged elsewhere.

## Credits

D.-L.-M. Avenel (1858) for the edition and its decipherment; Daniel Bourdeau for the fr. 3829 key; BnF (Archives et
manuscrits) for the shelfmarks; Internet Archive for the scans and OCR (Source archive.org).

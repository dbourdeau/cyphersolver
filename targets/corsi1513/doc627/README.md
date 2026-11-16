# Doc 627 (c. 635r): the source of the Corsi key

Added 16 Nov 2026 in answer to the review of PR #685 (Dan Bourdeau), which asked for the 627 cipher block, the
decipherment as written, the image id and the frozen key run against it.

## The image

- ASF, Mediceo avanti il Principato, filza CXXXVII, doc 627, c. 635r. IIIF id `A0001353`
  (viewer id 133869 = 1353 + 132516, the offset measured on 10 Nov from doc 620 = viewer 133843 = A0001327) [measured].
- URL: `https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?FIF=/data/iip-data/asfi/mediceo_avanti_principato/00100137/A0001353.ptif&WID=1600&CVT=jpeg`
- Fetched 16 Nov 2026 05:4x UTC from the contributor's Mac (the ASF server refuses cloud hosts), 1600 px wide,
  506,693 bytes, md5 `d54b593af4bf28749aed6947433988a8` [measured]. The image is not committed here.
- What the page holds [measured by eye on that image]:
  - a letter in Corsi's hand: six lines of clear text, then about four and a half lines of cipher (from "q x s3 z o7 ..."
    to "... w x g q7"), then clear text, dated "In Madrid a di xxviii[?] di dicembre 1513", signed "Ioannes Corsius or[ator] apud
    Cath[olicam] M[aies]tem";
  - **below the signature, five lines in a different, heavier hand and ink: a decipherment of the cipher block.**
- So the page is not bare. Catalogue 2391's vetting note of 6 Nov ("no interlinear or marginal decipherment on any leaf")
  missed it: the decipherment is neither interlinear nor marginal but at the foot of the page, after the signature.
  The 10 Nov contact sheet that found it is in the contributor's working files (`batch9_medici/2391_2392/LOG.md`, 18:07).

## Files

| File | What it is |
|---|---|
| `transcription_627.txt` | The cipher block as transcribed on 10 Nov 2026, copied unchanged. **Not blind**: it was made while the key was being built from this page, and doubtful shapes are marked `?`. 179 tokens. |
| `decipherment_627.txt` | The contemporary decipherment at the foot of the page, as written (abbreviations kept, expansions in brackets), transcribed 16 Nov from the image above. |
| `decode_627.py` | The 10 Nov decoder (key json + transcription, one line out per line in). |
| `decode_627_w17.txt` | The frozen key of record (`../key_corsi_w17_frozen.json`, sha256 5f56ad58...) run once on `transcription_627.txt`, 16 Nov. |
| `decode_627_w17.stats` | 179 tokens, 2 not in the key, 98.9% given a value [measured]. |

The output is identical, line for line, to the 10 Nov decode with the earlier key `key_corsi_10nov_frozen.json` [measured: diff],
as expected, since wave 17 changed no existing value.

## What this shows, and what it does not

- The key reproduces the decipherment on the page: the decode runs "el tempo ha digia mostro a [questo Re] e?..re falso
  qu..l.. gli ha scricto el cardinale romolino circa lo stato de [Firenze] ... ne fermo ne unito ... verso lo stato de
  [Firenze] et de [65] tanto malignamente quanto ha potuto ... mostrando la mala contenteza del popolo ... trovai nel mio
  arrivare qua ... poi non sento altro", which follows the five lines of `decipherment_627.txt` [derived].
- This is **not an independent control**. The key was built from this page, so agreement here is expected. It shows the
  key's source exists and says what the method claims; it does not test the key. The test of the key remains its
  unchanged use on 620, 623 and 633 (strict 74.7%, 55.4%, 74.2%, shuffles 0 of 5,000) [sourced: ../NOTES.md].
- A blind control on 627 (a fresh reader, name-only sheet, one decode, scored against the decipherment) has still not
  been run.

Method label stays "key recovered based on adjacent plaintext" (Lasry): the plaintext is the contemporary decipherment of
a sibling letter in the same filza, in another hand.

## Blind control on doc 627 (16 Nov 2026, after review of #685)

`blind_control/`: a fresh AI reader saw only a crop of the cipher block (no clear text, no decipherment) and a sheet with
neutral labels S01-S42 (`SHEET.md`, `PROMPT.txt`; label-to-key map `LABELS_TO_KEY.tsv` kept out of the packet). Its
`BLIND.tsv` was hashed (`FREEZE_blind.txt`, sha256 f9d31abe...) and decoded once with the frozen key (`decode_once.py`,
`decode_once.txt`: 188 tokens; 155 valued, 14 numbers, 15 holes, 4 nulls) [measured].

A separate strict judge aligned the decode to `../decipherment_627.txt` letter by letter (`judge.tsv`, `judge_count.py`,
`JUDGE_NOTES.md`) [measured]:

| Line | Match | Wrong | Hole | Omitted | Strict M/(M+X+H+O) | Accuracy M/(M+X) |
|---|---|---|---|---|---|---|
| 1 | 47 | 7 | 6 | 2 | 47/62 = 75.8% | 47/54 = 87.0% |
| 2 | 45 | 7 | 3 | 1 | 45/56 = 80.4% | 45/52 = 86.5% |
| 3 | 60 | 5 | 2 | 4 | 60/71 = 84.5% | 60/65 = 92.3% |
| 4 | 46 | 6 | 7 | 9 | 46/68 = 67.6% | 46/52 = 88.5% |
| 5 | 5 | 0 | 0 | 0 | 5/5 = 100% | 5/5 = 100% |
| Block | 203 | 25 | 18 | 16 | 203/262 = 77.5% | 203/228 = 89.0% |

- Codes: "questo Re" (#23) was read as a point (hole); Firenze (#70) was misread as two bare signs (wrong); 65 was read #63 (hole).
- Dictionary-cover shuffle (as `../../blind633/shuffle.py`): real 0.617; seed 20261112 0 of 5,000 as good (max 0.6082); seed 7 1 of 5,000 (max 0.625) (`shuffle_out.txt`). This passes our bar (under 5 of 5,000) by a thin margin on a short block; the letter-by-letter match against the page's decipherment is the stronger evidence.
- The decode reads "intendo" where our 16 Nov transcription of the decipherment has "Intado[?]"; our reading of the decipherment there may be wrong. Not emended.
- Still not independent: the key was built from this page. What it shows is that a blind reading of the cipher, through the frozen key, reproduces the decipherment written on the page.

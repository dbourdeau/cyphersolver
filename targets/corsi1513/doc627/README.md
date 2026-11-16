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

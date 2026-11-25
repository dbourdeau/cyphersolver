# Blind shape check of 17 Nov 2026 (view 13)

Brice Dudout answered a blind sheet of 15 boxed numbers on view 13. For each question he saw:
- a strip of the line with one number boxed in red;
- the same number enlarged;
- two or three "shapes", each shown as one or two crops of a sure number of the same hand.

No letters, words or readings were shown. The text options were "none / other shape", "cannot tell apart", "illegible" and
"not a sign", and every question had a remark field. The places of the reference shapes were balanced across questions, and the
controls were put at different places.

| file | content |
|---|---|
| `sheet_2026-11-17.json` | the 15 questions: line, word, which number, box in the crop, boxes of the example crops, the options as shown |
| `answer_key_2026-11-17.json` | which shape was which number; for each target, the value that would make the word sure; for the 3 controls, the expected shape |
| `answers_2026-11-17.json` | the answers exactly as exported by the sheet (17 Nov 2026 23:02 UTC), unchanged |

SHA-256 values:
- `answers_2026-11-17.json`: `b00b5e60f38599d39db180674fabb41106e40bf12420d4cbeb099d0633ff978a`
- the sheet as answered (HTML with the image crops embedded): `274e7f185cb12d87a4cbf4d5af5ccd7b05ea0a202ab8fea353d2d66736a41e4d`
- the private key file it was built with: `c2069aaa97499915358f7d791ff3b7bfd4ea63bbb2e113d7664311c64c9335d8`

The HTML sheet itself is not included. It embeds crops of the archive's images, which we keep for private study. With the boxes
in `sheet_2026-11-17.json`, it can be rebuilt from the public IIIF image of view 13: image
`c7eca322-4298-457d-a7d9-dc7b23f8283c`, turned 90 degrees clockwise and scaled to 1100 × 1500 px.

The remarks in the answers are in French. In English:
- q01: "with a trace or 2 dots above as well";
- q02: "shape 1 and 2: these are 3s";
- q10: "28 ?".

Controls: q06, q12 and q15 were all answered as expected (3 of 3).

## Why 19 numbers were prepared and 15 answered

The first sheet (17 Nov, 19 questions) was never answered. The same evening it was replaced by a second sheet in the format above:
the first sheet showed the options as digits typed out, without crops of the hand, and it had no controls. Of the 19 places:

- 10 were kept as targets: entsetzung ×2, die, tag, mittwoch, also, dapffer ×2, gesch… (6th number), gräfliche.
- 9 were dropped, because the answer could not change a word's status by its shape:
  - 3 numbers 38 (sollicitirt l. 6, alhero l. 11, noch l. 20): the shape is clear; what is deduced is the value 38 = o.
  - 2 numbers in keyserischen (l. 5): the first half of the word is faded, so it stays probable whatever the answer.
  - The end of l. 7 and the start of l. 8: crossing-out and blot, so this is not a choice between shapes.
  - A pale trace after alhero (l. 11): no word depends on it.
  - 398 on the slip: the question was how many numbers it holds, not which shape.
- 5 were added:
  - 3 controls on sure words (etliche l. 3, wesen l. 4, noch l. 20);
  - the last number of gesch… (l. 24);
  - the two-stroke 11 of Zabern (l. 3).

That gives 19 − 9 + 5 = 15. There was no other version: the 12 questions of an intermediate state of the second sheet are
q01–q12 here, in the same order and with the same option order.

# Blind shape check of 25 Nov 2026 (new scan of view 13)

On 25 Nov 2026 HStA Darmstadt sent a new colour scan of the sheet (TIFF, 5733 × 7721 px once flipped: it came as a mirror
image). It is kept for private study and is not included; unlike the microfilm, it is not public, so this sheet cannot be
rebuilt from a public image. Brice Dudout answered a second blind sheet on it, in the same format as above (crops of sure
numbers of the same hand as options, no letters or words shown, text options and a remark field, balanced places).

Before any crop was made, a selection rule was written and its SHA-256 recorded
(`90e1082caa70c724241b7808950a9d21d6dcbf59c0920e74b8ecde5f7bb1136c`). It names the 6 targets, the 3 controls, the shapes
offered and what each answer would change. An addendum written afterwards, before the sheet was sent, moved only the boxes,
which had been drawn on too coarse a grid (targets, controls, shapes and rule unchanged), and replaced two example crops.

| file | content |
|---|---|
| `sheet_2026-11-25.json` | the 9 questions: line, word, which number, box in the flipped scan, boxes and places of the example crops, the options as shown |
| `answer_key_2026-11-25.json` | which shape was which number; the value that would make the word sure and what each answer changes; for the 3 controls, the expected shape |
| `answers_2026-11-25.json` | the answers exactly as exported by the sheet (25 Nov 2026 18:58 UTC), unchanged |

SHA-256 values:
- `answers_2026-11-25.json`: `3d7772f98410f631335414d5ad65cf417c91e577264275a81506580a990d6fb8`
- the sheet as answered (HTML with the image crops embedded, not included): `e94f7f2b51f5b8ad5e1a835c7bbb6e6606c46620ed33d8cfb78ec8aabe9ef9fd`
- the private key file it was built with: `c2b08b5f1f599aafe0fe578773d29f001d388694b3fab03b5348b6d42ab9e93c`

The one remark, in French in the answers, is on q07: "with a dot above the 1, like an i". It describes the dot this hand
puts on every 1; the rule gives a value only to the shape chosen, so it changes nothing.

Results (controls q01, q02 and q04: 3 of 3 as expected):

| q | place | shape seen | effect under the rule |
|---|---|---|---|
| q09, q05 | l. 24 gesch…, 6th and last numbers | 24, 23 | geschossen sure on the new-scan reading |
| q08 | l. 12 mittwoch, 5th number | 31 | mittwoch sure |
| q07 | l. 29 (new scan) Hagenaw, last number | 31 | Hagenaw sure on the new-scan reading |
| q03 | l. 30 (new scan) decembris, middle number | 22, not 12 | written "decemmris"; stays probable |
| q06 | l. 30 (new scan) sign after decembris | none of 15, 18, 39 | stays unresolved; no year read |

The rule had estimated "+4 sure, 102 → 106 of 124" on the new-scan reading. Hagenaw is a word that only the new scan shows,
so it is not among those 124 words: the result there is 104 / 124. In this folder, which still holds the microfilm
transcription, only mittwoch is counted (98 / 124); see `reading.md`.

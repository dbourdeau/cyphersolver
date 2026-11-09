# Luftwaffe radio messages of Flugabwehrkommando Schwarzwald, 17 May 1940: the key of the day and a reading

Among the radio messages of the Flak units of Luftgau VII on NARA RG 242, T405 roll 9 (five-letter groups, double columnar transposition), this repository recovers the key of 17 May 1940 and decrypts the two messages of that day (six parts, 1,023 letters of text). The material is entry 704 of the unsolved catalogue of the Cyphersolver ledger.

**Relation to earlier work.** As of 10 November 2026 no recovery of this day's key and no decryption of these two messages was found in the places listed in `docs/PRIOR_CHECK.en.md`. Three things must be said:
- **The plaintexts survive in the same file in their contemporary form** (the first message as the recipient's fair copy, the second as the teleprinter message of the same day). The keys were recovered by a known-plaintext method, using a plaintext built from the fair copy of the first message. No previously unknown text was read.
- The ledger's page for catalogue entry 704 suggests this kind of attack (use the typed teleprinter messages on neighbouring frames as cribs, key lengths 15-25). The method used here is of that kind; the second key turned out to be 28 long.
- What was recovered: the two keys of 17 May, the letter-by-letter correspondence between cipher text and plaintext (the conventions for spelling numbers, signs and abbreviations), and the fact that two lines of part 3 of the first message are interchanged on the page.

**Status: full reading (both messages).** Of the 1,023 letters of text, 7 (0.7%) do not make sense as plaintext.

**No human has checked the transcriptions.** They were made from the images by an AI. Agreement with another AI's reading does not replace a human check.

## What the messages say

First message (frame 0993, Luftgaukommando VII to Flugabwehrkommando Schwarzwald, four parts):

> G.Kdos. 1.) Flakgruppe Friedrichshafen gibt an Flugabwehrkommando Schwarzwald ab: 1. und 3. Zug der 3. Batterie Res. Lei. Flakabteilung 932 (Herbertingen). Die beiden Züge werden durch Flugabwehrkommando Schwarzwald transportiert und gem. fernmündlicher Besprechung eingesetzt. 2.) Flakgruppe Friedrichshafen setzt 3. Zug Fla. M.G. Res. Komp. 304 (Sigmaringen) beim Schutzobjekt Herbertingen ein. Transport durch Flakgruppe Friedrichshafen. Die neuen Stellungen und Feuerbereitschaft zu melden. Luftgaukommando VII/Ia op 2 Nr. 2851/40 g.Kdos.

Second message (frames 1025-1027, sent by Flugabwehrkommando Schwarzwald Ic, two parts):

> Geheime Kommandosache. Am 16.5.40 wurde dem Flgabw.Kdo. Schwarzwald der I. Zug 2./932 (2 cm) von Flakgruppe Friedrichshafen zugeteilt. Der Zug ist seit 22.30 Uhr in Stellung 3031 westl. Tüllingen feuerbereit. Er ist Abt. 942 unterstellt. Flgabw.Kdo. Schwarzwald Ic Nr. F 161/40 g.Kdos.

The text as it was enciphered (`GKDOS X ERSTENS KLAMMER FLAKGRUPPE X FRIEDRICHSHAFEN X GIBT AN …`) and the spelling conventions are in `docs/READING.en.md`; the letter strings are in `data/plaintext.txt`.

## System and keys

Double columnar transposition. The plaintext is written in rows in a grid 24 wide and read off column by column in the order of the key numbers; the result is written in a grid 28 wide and read off the same way. The first five-letter group of each part is the key indicator group and is not part of the text.

```
first key (24)   15 12 20 8 17 4 22 9 19 2 16 11 5 21 10 3 14 24 7 13 1 6 18 23
second key (28)  24 17 10 21 6 18 27 1 22 16 7 25 11 2 20 23 4 8 13 19 28 14 5 9 15 3 26 12
```

Decrypt: `python3 src/decrypt.py`. Tests: `python3 -m unittest discover -s tests`.

## Figures

| Item | First message (0993, 634 letters) | Second message (1025-1027, 389 letters) |
|---|---|---|
| Letters that make sense | 629 (99.2%) | 387 (99.5%) |
| Control (1,000 random keys, all six parts together) | 0 as good as the real keys (trigram count: real 66, best random 19) | same |
| Not used for key recovery | parts 1-2 (347 letters) decrypted as they stand; part 3 after putting the two interchanged lines back | all of it (decrypted without sight of the plaintext) |
| Agreement with a second reader (OpenAI Codex) | 99.1% (first version), 99.2% (revised version) | 93.8% (version before decryption), 95.4% (after correcting 7 letters following decryption) |
| Calibration (characters agreeing with the contemporary text) | 98.8% (parts 1-2 against the fair copy) | 91.1% (against the teleprinter message) |
| Image-based judgements (sample of 80 agreed letters; number for which Codex / Sonnet chose the first reading) | 80 / 80 (10 planted items: 10 / 10) | 80 / 76 (10 planted items: 8 / 8) |

How these were counted, and the caveats, are in `docs/METHOD.en.md`.

## Use of AI

Transcription, fitting of the plaintext, key recovery, decryption and documents: Claude Fable 5.1 (Anthropic). Second transcription and image-based letter judgements: OpenAI Codex (gpt-6-astra) and Claude Sonnet. The human directed the work and decided on publication. No human compared the images with the transcriptions or the reading.

## Files

- `data/`: transcriptions (`ciphertext_0993.txt`, `ciphertext_1025_1027.txt`, and the version before decryption), keys, plaintext
- `src/`: decryption and control (`decrypt.py`), calibration (`calib.py`), key-recovery tools (`kpa.c`, `kpb.c`)
- `second/`: prompts and results of the second transcription; questions and answers of the image-based judgements
- `docs/`: method (METHOD), reading (READING), open points (OPEN), search for earlier work (PRIOR_CHECK)
- `SOURCES.en.md`: sources and frame numbers. No images are included

## Licence

Code: MIT. Own documents and data: CC BY 4.0 (`LICENSE`).

# H. Holbeck to Rowland Browne, 10 March 1550/51 (Hatfield House, Cecil Papers CP 150/143)

Status: attempted, 16 Nov 2026. Key proposed on pages 1-2; the one pre-registered measure on held-out page 3 failed
(0.684 against a bar of 0.85 and best shuffled key + 0.30, best shuffled key 0.501). Not read. Catalogue entry 1015.

A merchant's letter: a short opening in clear (three "garnish of vessels", six banqueting dishes and six saucers
to be delivered by Wm. Pawpers of Berwick), then three closely written pages in cipher. The cipher is a simple
letter substitution with words separated; many letters keep their own shape, so English shows through in places.

## The document

- **Shelfmark.** Hatfield House, Cecil Papers CP 150/143 (three pages; page 3 is f. 144). The reference was given by
  Sarah Whale (Hatfield House), see issue #712, which also covers CP 231/83 (catalogue 1017).
- **Images.** A free PDF copy supplied by Sarah Whale (Hatfield House) on 16 Nov 2026, for private study only.
  **No image, crop or derivative is in this repository, and none may be republished without Hatfield House's
  permission.** Only transcriptions and measures are here. To see the letter, ask the Hatfield House archives.
- **Printed calendar.** HMC, *Calendar of the Manuscripts of the Marquis of Salisbury at Hatfield House*, Part I
  (1883), p. 85, no. 349 (archive.org `calendarmanusc01grea`).

## Prior work: the HMC calendar

The calendar summarises the cipher part: it "relates to a previous consignment of 28 pipes of oil, respecting which
proceedings appear to have been instituted against Rowland Browne by certain merchants of Edinburgh, and to other
mercantile transactions." The editor therefore read at least the drift of the cipher, though he printed no
decipherment and no key. This is prior art and is credited as such: the HMC editor is the first known reader of the
gist. The summary was known before the work began (it is named in `frozen/HOLDOUT-DEF.md` as a published crib).
Nothing else was found: catalogue 1015 vetting (29 Oct 2026) searched DECODE, Tomokiyo and Lasry; no PR or issue on
this letter on origin/main as of 16 Nov 2026 (issue #712 is about another item).

## The system

Simple substitution, words separated by points (transcribed as spaces). Part of the alphabet keeps its usual
secretary-hand form (t, h, e, o, b and others); the rest is replaced by signs, several shaped like digits:
4 = a, p = n, z = r (and k, a similar form), ∂ = s/d, a barred loop = l/d, 8 = w, 9 = g, 7 = p, j = f/i,
a "10"-like sign = m, v = u, s = c, 2 = i/y/k, y = p. Sums are written in clear figures (`#16s8d#`).
Transcription codes (in `frozen/transcription/GLYPHES.md`, French): 4, D (the ∂ loop), Q (barred loop, often doubled),
8, 9, 7, 2, z, j, f, w (the "10"-like sign), p; other letters are their own shape; `#...#` clear figures, excluded
from every measure; `[?]` illegible.

## Transcriptions

Made by shape, from the PDF, by Claude Opus 5.5 agents. All in `frozen/transcription/`:

| file | portion | pass | words | signs |
|---|---|---|---|---|
| `p1-DEV-passe2.txt` | page 1 (cipher after the clear opening), development | blind pass 2 (sub-agent) | 354 | 1,530 |
| `p2-DEV-passe2.txt` | page 2, development | blind pass 2 (sub-agent) | 419 | 1,733 |
| `p3-TEST-passe1.txt` | page 3, held out | pass 1 | 257 | 1,081 |
| `p3-TEST-passe2.txt` | page 3, held out | blind pass 2 (sub-agent) | 261 | 1,093 |

Signs counted without the clear figures. Not done: pass 1 of pages 1-2, and the reconciliation of the two passes of
page 3 against the image. Hashes: `frozen/transcription/p3-TEST-passe1.sha256`, `frozen/transcription/passe2.sha256`.

## The test (pre-registered, one measure)

All frozen files are in `frozen/` with their SHA-256 (`shasum -a 256 -c PREREG.sha256` and the others from that folder).

1. **Held-out portion defined first** (`HOLDOUT-DEF.md`, frozen before any key work): the whole of page 3. At that
   point only the first four cipher lines of page 1 had been looked at closely; page 3 had been seen as a thumbnail.
2. **Key built on pages 1-2 only** and frozen (`cle/key-FROZEN.json`): each sign maps to a small set of letters
   that absorbs shape confusions of the transcription.
3. **Measure frozen** (`PREREG.md`, `cle/mesure.py`, `cle/lex-supp.txt`): the share of the test's signs that fall in
   words which, decoded by the key (any combination of the sets), and normalised (lower case, y→i, v→u, j→i,
   doubled letters reduced, final -e dropped), are in the lexicon: the system word list (`/usr/share/dict/words`,
   web2 on macOS) plus about 200 older spellings taken from pages 1-2 only. Null: 200 keys made by shuffling the key's
   values among the signs (seeds 0-199). Bar: score ≥ 0.85 **and** score ≥ best null + 0.30.
   Reference values on the development pages before the freeze: page 1 0.847 (best null 0.478), page 2 0.857 (0.444).
4. **Result** (`MESURE-p3-passe1.json`): **0.684**, best null 0.501, mean null 0.155. **Fail.** Secondary, not
   deciding, on the blind pass 2 of page 3 (`MESURE-p3-passe2-secondaire.json`): 0.676, best null 0.450.
   Words not recognised: 50 of 257 on page 3 (37 of 354 on page 1, 37 of 419 on page 2).

Re-run from `frozen/cle/`: `python3 mesure.py key-FROZEN.json ../transcription/p3-TEST-passe1.txt`
(re-run at integration, 16 Nov 2026: same figures; the result depends on the macOS web2 word list).

Page 3 is now spent as a held-out portion. No other text in this system is known, so a second test needs another
Holbeck-Browne cipher letter, or a new pre-registered measure (a lexicon of early modern English frozen in advance)
on a new portion.

**Matched control.** Not run, and the reason is stated here: the README rule is for a negative from a solver (a
solver that fails the target must be shown to succeed on a synthetic text of the same design). Here no solver failed:
a fixed key was scored by a fixed measure, against 200 shuffled keys of the same structure as the null. What the
failure leaves open is the measure's ceiling on 1551 spelling, not whether a solver can find the key. The control
that would answer that is the same measure on a clear English letter of about 1550, of the same length; it is listed
under the gaps.

## After the measure (does not change the verdict)

`decode_after_measure.txt` is the mechanical decode of the three pages with the first value of each set
(`decode_first.py`). It is not a reading. Page 3 decodes into continuous English that a reader can follow: ships
stayed in Zealand ("sellans"), the exchange "at 16s 8d usance", a ship freighted for Berwick, "I pray God send you a
short dispatch", the household in health. Pages 1-2 (not validated) speak of the 28 pipes of oil, the merchants'
declaration, witnesses ("master Jobson"), a notary, bills of lading, Edinburgh, fish to be sold through a partner
fishmonger, and the Bishop of Gloucester preaching before the King, which agrees with the HMC summary.

So the failure looks like a fault of the measure more than of the key: the lexicon misses names and 1551 spellings,
and the transcription is noisy where signs look alike (2/j/z, D/Q, the "10"-like sign absorbing an o). This is a
diagnosis made after the measure and it is not counted: by the frozen rule the key is partial and the text is not
read.

## Remaining gaps

- No second held-out test: page 3 is spent and no other letter in this system is known. Blocker: too-short.
  (Another Holbeck or Browne cipher letter at Hatfield would give a new portion.)
- Pass 1 of pages 1-2 and the reconciliation of the two passes of page 3 against the image. Blocker: not-attempted.
- A matched control for the measure's ceiling on 1550s English spelling. Blocker: not-attempted.
- A reading (sentences, holes marked, checked against the images by a reader). Blocker: not-attempted.

## Credits and tools

- Sarah Whale (Hatfield House) supplied the images and the shelfmarks (issue #712).
- HMC, Calendar of the Cecil Papers, Part I (1883), p. 85, no. 349: summary of the cipher part (prior art).
- Brice Dudout chose the target and set the rule (held-out page named before the key work, one measure);
  Claude Opus 5.5 agents transcribed, built the key, measured and wrote this up. No human has read the decode.

# Mondoucet → Charles IX, BnF fr. 16127 (Low Countries despatches 1571–74)

Outcome: **read in part** (21 Sept 2026). Two of the three documents worked are read, the third only in stretches:

- **9 Sept 1573** (Amsterdam, ff. 135–137): read. The Court's verbatim decipherment is on ff. 139–141; the
  cipher was transcribed and aligned against it end to end (`f1573/reading.md` §2).
- **4 Jan 1573** (Antwerp, ff. 126v–127v): read. No decipherment in the volume; decoded ciphertext-only to
  ~55–60 % of letters (held-out control 79.0 %), then found printed in clear by L. Didier, *Lettres et
  négociations de Claude de Mondoucet*, t. 1 (1891), pp. 141–142, which confirms the decode where it read
  (`f1573/reading.md` §3–5).
- **13 July 1572** (Brussels, ff. 60–61): not read beyond scattered words (~1–8 % of glyphs; `reading.md`, `hand/decode_retry.txt`). It has no contemporary
  decipherment and is not in Didier (the Reims register starts 6 Sept 1572; Didier's introduction lists it as
  "chiffrée et en grande partie sans déchiffrement").

Details: `reading.md` (1572) and `f1573/reading.md` (1573).

## Remaining gaps
- 13 July 1572, cipher lines J1-J22 (f. 60r), K1 (f. 60v), M1-M6 (f. 61r) - blocker: no-key-material; no
  decipherment in fr. 16127 or in Didier, and after the a/alpha retry the 1572 key still reads only ~1-8 % of the
  1,082 glyphs as sense (hand/decode_retry.txt). The 1572 key was fitted on one 863-letter crib (16 July) and scores
  only ~60 % on that same block, so the limit is the key, not the scan: the leaves are legible on the microfilm.
  Known transcription residue remains (f. 61 lines are partly out of step with the image), but a better f. 61
  transcription alone would not read without a better key. A Court decipherment or a copy of the letter would move it.

## Escalation
- [x] siblings: fr. 16127 swept entire; neighbouring leaves ff. 62–64 (16 July 1572, glossed) used as the crib
- [x] clear-pages: none for 13 July; f. 64 is the 16 July decipherment, not 13 July's
- [x] known-keys: the 1573 key (key1573_split2.json, same system) is the extended form of the 1572 key
- [x] print: Didier t. 1 (1891) found; it has 4 Jan 1573 but not 13 July 1572 (register begins 6 Sept 1572)
- [x] key-rebuild: seeded hard-EM on 9 Sept, a/α split (α = r), tryalt constrained pass on 4 Jan
- [x] retry: 13 July re-transcribed with open alpha marked on the strips (hand/ct_f60_split.txt, ct_f60v_split.txt,
  ct_f61_split.txt; 42 of 76 a-class signs are alpha) and re-decoded with key2 + alpha = r and with key1573_split2
  directly (hand/decode_retry.txt). Control on the 16 July block (not held out): 60.3 % -> 61.1 % with alpha = r,
  56.2 % with the 1573 key; chance 12-15 %. Share of 13 July glyphs in stretches that read as sense: ~8 % lenient,
  ~1 % strict. No gain: the passage stays read only in scattered words.

## Glyph-level XML (24 Sept 2026, pilot for George Lasry)

`python tools/transcription_xml.py mondoucet` writes `xml/1573-09-09.xml` and `xml/1572-07-13.xml` from the
sign-label files (`f1573/ct/f135r_split.txt`, `f1573/ct/blk2_split.txt`, `hand/ct_f6*_split.txt`). There is one `<g sign=..>`
per glyph, with the scribe's gaps as `<w gap="scribe">`.
- **9 Sept 1573** (4,734 glyphs and 70 dots): each glyph carries the Court's letter (`basis="court"`) from the hard-EM
  alignment. That alignment was regenerated as `f1573/key1573_split2_align.txt` by
  `OUT=key1573_split2 python align2.py ct/f135r_split.txt:pt/f139r_a.txt ct/blk2_split.txt:pt/blk2.txt`, and the
  re-run reproduces `key1573_split2.json` exactly. Each glyph also carries `key=`, the sign's spread over the whole
  alignment. Court letters left without a glyph are `<gap r=..>` (217). Of the 177 glyph→word matches, only the
  ones that recur (J = que) keep full certainty; the others are marked `cert="low"` as aligner slack.
- **13 July 1572** (1,082 glyphs): no reading exists. Each glyph gets the 1572 key's alternatives (`key=`, the "ext" key of
  `hand/decode_retry.py`) and the beam decoder's letter (`basis="decoder"`). The decoder letter is not a reading.
No coordinates: the transcription was made by eye from line strips, and no bounding boxes were kept.

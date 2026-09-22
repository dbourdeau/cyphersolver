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

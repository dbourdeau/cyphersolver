# Prince de Conti's mémoire for Laigue, Paris, 5 March 1649 (BnF fr. 3854 no. 43, ff. 117r–120r)

Status: read (18 Sept 2026; split into its own entry 14 Oct 2026).

Split on 14 Oct 2026 from `conti1649` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 26 grouped
the three ciphered mémoires of fr. 3854 nos. 41–43; no. 43 is a numeric letter-and-syllable code, a different
system from the poly-homophonic letter cipher of nos. 41–42 that Lasry solved (HistoCrypt 2023). Nos. 41–42 keep the
old entry: [`targets/conti1649/`](../conti1649/NOTES.md), page `conti1649.html` ("a different cipher, with its own
page"). `READING43.md` and `n43/` moved here from conti1649.

## The document

- Gallica ark `btv1b52520094g` (fr. 3854), canvases 245–251; IIIF manifest in `../conti1649/manifest.json` (shared).
  Images are git-ignored, in the main checkout's `targets/conti1649/` (`full/`, `n43/*.jpg`).
- Omont no. 43: "Mémoire, avec chiffre et déchiffrement, du prince de Conti, pour un de ses envoyés auprès de
  l'archiduc", undated in the catalogue. It is Conti's mémoire *pour Monsieur de Legue*: Geoffroy, marquis de Laigue,
  his envoy to Archduke Leopold Wilhelm. The last line of f. 120r is glossed *à Paris le 5me mars 1649*.
- A numerical code of letters and syllables, with clear words mixed in. A contemporary hand deciphered it between
  the lines from f. 117r l. 12 onward. The first twelve lines, 264 groups (the address and the purpose of the
  mémoire), were never glossed.

## The key (rebuilt here, 18 Sept 2026)

From the glossed groups (`n43/pairs_c246.txt` … `pairs_c248.txt`, 1,485 glossed groups; `n43/buildkey.py` →
`n43/key43.txt`) and the code's regular layout (details in `READING43.md`):
- four interleaved single-letter alphabets (3–25 a→z, 28–50 z→a, 51–73 a→z, about 80–98 z→a);
- syllables in consonant blocks of five in vowel order, with a second homophonic series in the gaps;
- an underlined number reverses its syllable (385 ra, 385̲ ar);
- nulls 99–250, never glossed; code words 451 la Reyne, 457 cardinal, 458 parlement, 472 l'archiduc, 482 France;
  the 500s are dates.

## The reading

- The opening (264 groups, `n43/decode_opening.py` → `n43/opening_decoded.txt`): 220 by the majority gloss of the
  same number, 24 by the alphabet structure or as nulls, 20 second-series syllables by context. Nine of the context
  and structural values were later found glossed on ff. 117r–120r, all as predicted (279 de, 364 la, 354 ne, 443
  te, 445 su, 37 o, 43 h, 86 n, 36 p); none contradicted (`n43/scan_119_120.md`).
- The body: the contemporary interlinear decipherment, transcribed group by group (`n43/pairs_c245.txt` …
  `pairs_c251.txt`, about 3,300 glossed groups) and joined by `n43/assemble.py` (`n43/body_assembled.txt`).
- Edition of the whole mémoire: `READING43.md`.

Measured 14 Oct 2026 (`mk_validation.py`): 3,367 code groups in all; 3,300 have a value or are nulls (98.0%), 89
nulls; 67 unread, all in the glossed body: groups with no legible gloss (faint, blotted or struck, or passed over by
the glosser outside the null range). The opening: 264 of 264.
Statistical validation on these pairs: `python docs/_validate.py laigue1649` (result in profile.json).

## Remaining gaps

- 67 groups without a legible gloss, chiefly four short places (f. 117v l. 18, f. 118v ll. 5–8, f. 119v l. 14,
  f. 120r l. 0) - blocker: illegible; the gloss is faint, blotted or struck through (f. 119v l. 14 apparently "duc de Lorraine",
  struck)
- ten context values in the opening (277, 314, 321, 358, 390, 398, 400, 407, 439, 442) - blocker: open-codes; they
  never occur in the glossed text, so they rest on sense alone; none changes a sentence

## Escalation

- [x] siblings: nos. 41–42 (different cipher, Lasry)
- [x] clear-pages: the interlinear decipherment is the clear text of the body; none for the opening
- [x] known-keys: Lasry's 1649 key (nos. 41–42) is a different system; no other Conti code known
- [x] print: no printed decipherment of no. 43 found (Omont lists it with its déchiffrement)
- [x] key-rebuild: key rebuilt from about 3,300 glossed groups and the layout
- [x] retry: ff. 119r–120r scanned again for the context values (nine confirmed, none contradicted)

## Files

- `READING43.md`: the reading and the edition. `n43/`: transcriptions, key tally, decoders, assembler.
- `mk_validation.py`: counts the groups and writes `validation.tsv` for `docs/_validate.py`.

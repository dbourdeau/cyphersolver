# LJS 51: a typology of the 207 ciphers, set against Qalqashandi and the Miftah

Analysis by Brice Dudout (AI agents, Claude Opus 5.5), 28 Nov 2026. It classifies every cipher of the volume by system,
using only Daniel Bourdeau's files at d8ac608093 (`chains_all.json`, `keys_eye/REPORT.md`, `keys_eye/*.json`,
`texts/stats.json`). No image was read and no key was rebuilt. Every key used is Daniel's by-eye key from the compiler's
plaintext, not independently confirmed, so the counts below inherit that limit. The facts are Daniel's; what is new
here is the classification of the whole volume and its comparison with the treatises.

`typology.tsv`: one row per document (Daniel's 207 documents: 211 chain records less the two merges and 48r.8 / 106v.6).
- **A columns** are computed mechanically from Daniel's files: length, number of shapes, letters with two or more shapes
  (homophones), shapes with two or more letters, red gloss, shape family and dividers (keywords in `style`), and the share
  of shapes described by an Arabic letter that take that letter.
- **B columns** are hand-coded from per-document fact sheets, following a coding grid frozen before any coding (hash
  posted on #1023): system, lam-alif, hamza, the difficulty the compiler declares, the encipherer, whether the compiler
  comments on the technique, and whether the cipher departs from the written plaintext.

## Reliability

Two independent blind coders coded 30 documents (seed 3030) on B1-B7. The criterion, frozen in advance, was Cohen's
kappa >= 0.80 per dimension. The freeze was verified first, and the manifest hash was posted on #1023 before the coders
started. This was the only measurement.

| dimension | kappa A-B | agreement A-B | my coding vs A / B |
|---|---|---|---|
| B1 system | 0.936 | 29/30 | 0.90 / 0.87 |
| B2 lam-alif | 1.000 | 30/30 | 1.00 / 1.00 |
| B3 hamza | 1.000 | 30/30 | 1.00 / 1.00 |
| B4 declared difficulty | 1.000 | 30/30 | 0.97 / 0.97 |
| B5 encipherer | 0.953 | 29/30 | 0.93 / 0.97 |
| B6 compiler comments on technique | 0.930 | 29/30 | 0.93 / 0.97 |
| B7 cipher differs from written plaintext | 0.911 | 29/30 | 0.90 / 0.87 |

All seven dimensions pass, with three caveats:
- The sample has no SKELETON, NO_KEY, tree or maqlub document. The B1 skeleton count (20) is therefore not validated.
- B2 and B3 are mostly ND in the sample, and their kappa rests on 4 and 5 coded cases.
- The 207-row B coding is mine. It was not done blind, and it agrees 87-100% with the blind coders.

## Findings (descriptive)

- 207 ciphers, 15,203 signs, median 73 signs and 20 shapes. Systems: simple substitution 109, substitution with flagged
  homophones 68, substitution that merges letters of one skeleton 20 (13r.11 ب/ي; 68v.13 12 shapes for 13 dotted letters;
  99r.10 one sign per rasm group throughout), tashifi 1 (14v.7), tree script 1 (63v), maqlub 1 (102v.11), no key 7.
  The tashifi of 14v.7 is the end of a range of partial skeleton ciphers, not a one-off.
- 107 keys have at least one letter with two shapes, mostly one letter (54). The compiler calls several such cases slips
  (50v.1, 57r.2, 64r.3, 69r.12): a stray homophone is often an accident, not a system.
- Of 492 shapes that the key files describe by an Arabic letter ("ط-like"), 69 (14%) take that letter: letter-shaped
  signs are mostly decoys, with a minority derived from the plain letter (as Daniel noted under "Shared alphabets?").
- Lam-alif as one sign is noted six times (10v.1, 22r.1, 22v.9, 42v.3, 103v.11, 105v.6). At 103v.11 the compiler adds
  that it is "not the rule". Hamza is noted as not written 17 times, and as written (usually with its seat) 10 times.
- Pieces the compiler calls hard are shorter (median 55.5 signs against 73) and have no more shapes or homophones. The
  difficulty is in the text, and the compiler hardens his own plaintexts against exactly the solving cues of the
  treatises: no definite article (55r.7, 55v.5, 65r.5, 70v.11), only dotted letters (68v.13), five two-letter words
  (41r.3), few distinct letters (53r.3), dropped letters or added ones (3r.7, 51r.10, 105v.6), optional groups (94v.5).
- Several pens: one per verse (12v.8, 12v.11), "seven pens" (80r.9), "fifteen kinds of writing" (80v.9), re-enciphered in
  another pen (77r.3), "I changed the letters" (81r.5), Coptic (86v.9), an old pen from a book (78r.12).
- Reused shape sets in exchange pairs (56r.13/56v.8, 65v.2/65v.13, 67v.9/68r.6, 69r.12/69v.11, 80r.9/80v.9/81r.5,
  100r.8/100v.6/101r.2), with the values changed where checked (65v.13, 81r.5). This is consistent with Daniel's finding
  that no two pieces share an alphabet: what is shared is the shapes, not the key.

## Against Qalqashandi, *Subh al-a'sha* 9:229-231 (after Ibn al-Durayhim)

Read in OpenITI `0821Qalqashandi.SubhAcsha.Shamela0009429-ara1`, PageV09P229-235.

| Qalqashandi's kind | LJS 51 |
|---|---|
| old or foreign scripts | named, rare: 86v.9 Coptic, 78r.12 old pen |
| qalam qummi (reciprocal pairs) | named once: 37v.12 |
| reversing a word; swapping its first two letters | not as such; 102v.11 is a more complex transposition (even positions, then odd reversed); 105v.6 is written left to right |
| abjad numbers; letters summing to the number | not attested; numeral-like shapes (60 pieces) are plain shapes |
| names, lunar mansions, countries, fruits, trees, birds | not attested as such (63v trees belong to the Miftah's mushajjar) |
| invented shapes in alphabet order, one per letter, with dividers | dominant; dotted-alif or dotted-stem dividers in 120, but "one shape per letter" is often broken |

Found in practice and not in his list: tashifi and partial skeleton ciphers, the tree script (Miftah only, per
`prior_art_2.md`), several pens in one piece, red glosses, hardening through the plaintext, reused shape sets.
In the treatises and not in practice: abjad numerals, name substitutions, regular letter swaps, the Miftah's "regulated"
shifts.

Miftah: only what `prior_art_2.md` cites (Mrayati et al., Arabic vol. 1, 1987). The English *Arabic Origins of
Cryptology* vol. 3 was not seen; that is a limit of this comparison.

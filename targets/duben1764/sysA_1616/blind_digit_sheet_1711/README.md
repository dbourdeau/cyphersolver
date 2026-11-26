# Blind digit-form sheet soir1711-f (17 Nov 2026)

Added on 26 Nov 2026 at Daniel's request (review of PR #759). This is the sheet behind the `*_plate1711.txt` readings of
90R-93L and 104R-105L. key_c02, the transcriptions and the measures did not change with it.

| file | what it is |
|---|---|
| `answers_soir1711-f.json` | Brice Dudout's answers, exported by the page on 17 Nov 2026 at 23:04 UTC. Byte for byte as exported (keys in French: `choix` = choice, `remarque` = remark) |
| `sheet_soir1711-f.json` | the 23 questions: place, Riksarkivet image, pixel box of the framed sign and of its group, the forms offered, the reference digits of the same hand shown for each form, the expected answer (controls) or the form the sense expects (targets), the answer and whether it agrees |
| `SHA256SUMS` | SHA-256 of the two files above |

**How it was shown.** The page framed one doubtful digit at a time. Next to it were reference digits of the same hand,
one row per candidate form. The page showed no value, no reading and no sense, and the expected forms were not in the
page. Question order and option order were shuffled with fixed seeds (17112026, 17641764). Four control questions on
sure groups were mixed in (ranks 6, 12, 16 and 18).

**Result.** All four controls were answered as expected (4/4). Of the 19 target questions, 10 agree with the sense and
9 go against it (the targets are 105L07 g9, 105L03 g11, 90R02 g7, 104R03 g9, 104R17 g14, 92L12 g8, 92R17 g8, 104R05 g12
and 91L03 g12). A form against the sense may be a slip of the encipherer or a wrong key_c02 value. This is not settled.
A word contradicted by the form is never made sure.

**Not included.** The page itself (`planche.html`) embeds image crops, and the archive's images are not republished here.
The answer key was kept in a separate file, away from the page; `sheet_soir1711-f.json` gives its content in English.
SHA-256 values of both, for the record:
- `planche.html`: `a3baf38be5a163ad48f6762a9027e450860eb862f314edce9a81a82dd2680606`
- answer key (`_correspondance.json`, from which `sheet_soir1711-f.json` is written in English): `993402e978c9df702a031892e02be80f76357158154ab5ae120283a1f292405a`

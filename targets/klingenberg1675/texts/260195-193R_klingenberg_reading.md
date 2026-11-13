# Biermann to Klingenberg, c. 9 Sept 1675 (docket 195L, day doubtful), unit 260195 images 193R-194L: German reading, holes in place

Built by rule from the frozen first transcription (`260195-193R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260195-193R_klingenberg_decryption.txt`) and the ledger (`260195-193R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 30/(30 + 10 + 0) = 30/40 = 75.00%. Of the 10 E units, 5 are printed with an emendation and 5 are left as decoded.

## Reading

> ... Nun gehet die menke

beiderseits auf des churfürst

> ganz

instandiges anhalten gerades wecs[?wegs] nach [293] unangesehen ihr dessein dahin keinesfweges[?keineswegs] sondern auf wismar gerichtet gewesen

> es ist aber

der churfürst von den andern was [112] auch allegieret [418] nicht abzu[41][?] gefwesen[?gewesen]

> Gott gebe nur dass

es an [139]em[?] untergult[?unterhalt] nicht mancel[?mangeln] moge

> Ihr Hochgräfl. Excellenz werden wegen ...

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> ... Nun gehet die menke

beiderseits auf des churfürst

> ganz

instandiges anhalten gerades wecs[?wegs] nach [293], unangesehen ihr dessein dahin, keinesfweges[?keineswegs], sondern auf wismar gerichtet gewesen.

> es ist aber

der churfürst von den andern, was [112] auch allegieret [418], nicht abzu[41][?] gefwesen[?gewesen].

> Gott gebe nur dass

es an [139]em[?] untergult[?unterhalt] nicht mancel[?mangeln] moge.

> Ihr Hochgräfl. Excellenz werden wegen ...

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 8 | 27-29 | `wecs` | wegs | `wecs[?wegs]` | printed as emendation (similarity 1.00); c for g (# read for H?) |
| 10 | 31-31 | `[293]` | (none) | `[293]` | not printed: no word in the ledger |
| 15 | 48-53 | `keinesfweges` | keineswegs | `keinesfweges[?keineswegs]` | printed as emendation (similarity 0.91) |
| 27 | 79-79 | `[112]` | (none) | `[112]` | not printed: no word in the ledger |
| 30 | 88-88 | `[418]` | (none) | `[418]` | not printed: no word in the ledger |
| 32 | 90-93 | `abzu[41]` | (none) | `abzu[41][?]` | not printed: no word in the ledger |
| 33 | 94-98 | `gefwesen` | gewesen | `gefwesen[?gewesen]` | printed as emendation (similarity 0.93) |
| 36 | 101-103 | `[139]em` | dem | `[139]em[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 37 | 104-110 | `untergult` | unterhalt | `untergult[?unterhalt]` | printed as emendation (similarity 0.78) |
| 39 | 112-115 | `mancel` | mangeln | `mancel[?mangeln]` | printed as emendation (similarity 0.92) |

## Caveats

- H/#: at 2 sites (517 H K; 1 H E) the blind reader b176 found one bar (H) where the first reader read #; the decode keeps #. Placement of the margin insert at the '#' caret is a judgment (FILE_NOW). b176 had seen the H/# chart (exposure E1).
- 1 E unit(s) decode c where the ledger's word has g (marked in the list). c is the value of #, g of H; given the H/# disputes these may be sign misreads rather than spelling. The decode is not changed.
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

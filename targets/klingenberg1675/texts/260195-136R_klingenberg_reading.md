# Biermann to Klingenberg, Aug 1675 (docket 137L), unit 260195 images 136R: German reading, holes in place

Built by rule from the frozen first transcription (`260195-136R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260195-136R_klingenberg_decryption.txt`) and the ledger (`260195-136R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 27/(27 + 10 + 1) = 27/38 = 71.05%. Of the 10 E units, 2 are printed with an emendation and 8 are left as decoded.

## Reading

> Ihr Königl. May. haben auch

der o[?] fel<w>[?] marechal lieutenant [377]

> [note: [insert mark]]

ertheilt die [93]

> [note: [struck row]]

rein

> [note: [struck]]

zu halten

> [note: [struck]]

und zu den

> [note: [struck]]

ende die darauf ligende[?liegende] zwo [335] <[>regatten[?] anzucrei<[>fen[?] und hin wec[?weg] zu [blot]

> und würde sich

an den ubrigen krieg schiff von ihr mit

> sonderbahren?

<[>leis[?] gearbeitet

> . Auß Schweden lauffet die nachricht ein daß daselbsten bereits in die 26. meist capitale Schiffe segelfertig liegen, daß [struck] die nur noch etwas munition und proviant einzunehmen hetten. Ihr Königl. May. werden gewis innerhalb wenig tagen nach Holstein aufbrechen, maßen dero bagage täglich dahin voraus gehet. Und Ich verbleibe

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> Ihr Königl. May. haben auch

der o[?] fel<w>[?] marechal lieutenant [377]

> [note: [insert mark]]

ertheilt die [93]

> [note: [struck row]]

rein

> [note: [struck]]

zu halten,

> [note: [struck]]

und zu den

> [note: [struck]]

ende die darauf ligende[?liegende] zwo [335] <[>regatten[?] anzucrei<[>fen[?] und hin wec[?weg] zu [blot]

> und würde sich

an den ubrigen krieg schiff von ihr mit

> sonderbahren?

<[>leis[?] gearbeitet

> . Auß Schweden lauffet die nachricht ein daß daselbsten bereits in die 26. meist capitale Schiffe segelfertig liegen, daß [struck] die nur noch etwas munition und proviant einzunehmen hetten. Ihr Königl. May. werden gewis innerhalb wenig tagen nach Holstein aufbrechen, maßen dero bagage täglich dahin voraus gehet. Und Ich verbleibe

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 2 | 1-1 | `o` | (none) | `o[?]` | not printed: no word in the ledger |
| 3 | 2-4 | `fel<w>` | feld | `fel<w>[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 6 | 17-17 | `[377]` | (none) | `[377]` | not printed: no word in the ledger |
| 9 | 25-25 | `[93]` | (none) | `[93]` | not printed: no word in the ledger |
| 19 | 44-47 | `ligende` | liegende | `ligende[?liegende]` | printed as emendation (similarity 0.93) |
| 21 | 50-50 | `[335]` | (none) | `[335]` | not printed: no word in the ledger |
| 22 | 51-56 | `<[>regatten` | fregatten | `<[>regatten[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 23 | 57-64 | `anzucrei<[>fen` | anzugreiffen | `anzucrei<[>fen[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 26 | 68-69 | `wec` | weg | `wec[?weg]` | printed as emendation (similarity 1.00); c for g (# read for H?) |
| 37 | 85-88 | `<[>leis` | fleis | `<[>leis[?]` | not printed: decode holds a code with no value, an unread sign or a blot |

## Caveats

- 136R is the last page of the letter 134R-136L whose body is parked (not filed). A margin insert beside 136R ('517 G 462') was missed by the first reader and is not in this reading; the row-13 blot is probably '11' (FILE_NOW caveat). 'ligende' is judged E (28/38 = 73.68% if S); not rescored.
- clear text '[struck]' stands in the transcription inside the token range of the word `halten` (after token 32); given after that word
- 1 E unit(s) decode c where the ledger's word has g (marked in the list). c is the value of #, g of H; given the H/# disputes these may be sign misreads rather than spelling. The decode is not changed.
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

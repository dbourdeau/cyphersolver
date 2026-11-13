# Biermann to Klingenberg, c. late Oct/Nov 1675 (estimated, undated draft), unit 260196 images 10R-11L: German reading, holes in place

Built by rule from the frozen first transcription (`260196-10R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260196-10R_klingenberg_decryption.txt`) and the ledger (`260196-10R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 40/(40 + 6 + 0) = 40/46 = 86.96%. Of the 6 E units, 3 are printed with an emendation and 3 are left as decoded.

## Reading

> ... dass ob zwar Ihr Königl. Mayt. lieber

die außrustunc[?außrüstung]

> . aber

[40] schiff selber thaten und

> also gerne

das meiste geld hetten so [418] sie

> doch

durch die

> schliesse

bezihlunc[?bezahlung] der subsidien

> dergestalt

abgeschrecket

> dass Sie für besser und sicherer halten die

wenigere summam zu nemmen und die staten die

> übrige

schiff

> wie Ich bereits in einem meiner vorigen schreiben berichtet

equippieren zu lassen

> als

in der gefahr zu

> stehen dass

wegen außpleibunc[?außbleibung] der subsidien

> gar

keine flotte in sae[?] gebracht werden

> können. Allermassen befinden Ihr Königl. Mayt. auch allergnädigst für gut ...

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> ... dass ob zwar Ihr Königl. Mayt. lieber

die außrustunc[?außrüstung]

> . aber

[40] schiff selber thaten und

> also gerne

das meiste geld hetten, so [418] sie

> doch

durch die

> schliesse

bezihlunc[?bezahlung] der subsidien

> dergestalt

abgeschrecket,

> dass Sie für besser und sicherer halten die

wenigere summam zu nemmen und die staten die

> übrige

schiff

> wie Ich bereits in einem meiner vorigen schreiben berichtet

equippieren zu lassen,

> als

in der gefahr zu

> stehen dass

wegen außpleibunc[?außbleibung] der subsidien

> gar

keine flotte in sae[?] gebracht werden

> können. Allermassen befinden Ihr Königl. Mayt. auch allergnädigst für gut ...

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 2 | 1-6 | `außrustunc` | außrüstung | `außrustunc[?außrüstung]` | printed as emendation (similarity 1.00); c for g (# read for H?) |
| 3 | 7-7 | `[40]` | (none) | `[40]` | not printed: no word in the ledger |
| 13 | 29-29 | `[418]` | (none) | `[418]` | not printed: no word in the ledger |
| 17 | 33-39 | `bezihlunc` | bezahlung | `bezihlunc[?bezahlung]` | printed as emendation (similarity 0.89) |
| 38 | 95-102 | `außpleibunc` | außbleibung | `außpleibunc[?außbleibung]` | printed as emendation (similarity 0.92) |
| 44 | 111-112 | `sae` | see | `sae[?]` | not printed: decode too far from the word (similarity 0.67 < 0.75) |

## Caveats

- The blind reader (b158) read a 6-token cipher insert in the 10R left column that the first reader did not transcribe; it is not in this reading. The 11L left-column margin insert (keyed '+') is clear text and was not transcribed (transcription head).
- H/# (b158 adjudication): at two sites the blind reader read H (one bar) where the first reader read #; the decode here keeps the first reader's signs.
- clear text '.' stands in the transcription inside the token range of the word `außrustunc` (after token 5); given after that word
- Code 262 (v4 'selbe') occurs 1 time(s) here and is printed as decoded; a glossed 1675 copy contradicts v4 for 262 in 3 of 3 places (query, key unchanged; NOTES caveat 7).
- 1 E unit(s) decode c where the ledger's word has g (marked in the list). c is the value of #, g of H; given the H/# disputes these may be sign misreads rather than spelling. The decode is not changed.
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

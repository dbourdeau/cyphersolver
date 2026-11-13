# Biermann to Klingenberg, 6 Sept 1675 (docket 191L), unit 260195 images 189R-190R: German reading, holes in place

Built by rule from the frozen first transcription (`1675-09-06_klingenberg_transcription.txt`), the single decode made from it with map v4 (`1675-09-06_klingenberg_decryption.txt`) and the ledger (`1675-09-06_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 102/(102 + 24 + 0) = 102/126 = 80.95%. Of the 24 E units, 3 are printed with an emendation and 21 are left as decoded.

## Reading

> Ihr Königl. May: seind vorgestern alhier glücklich angelangt ... da man dann Königl. seiten

die belagerung von wislur[?] vorgeschla[384]n[?] [211] [67] von den churfürst keineswegk[?keineswegs] vor gut und rathsam befunden werden wolen[?wollen]

> sondern

es [103] derselbe vielmehr davor gehalten das man gesamter hand in [293] [5] und den [118] daselbsten zu ruinieren trachten würde [211] den[?] auch

> allem ansehen nach unangesehen

sich dabey wegen der subsistence keine geringe difficulteten [242] von ihr [341] churfürst darauf feste bektehet[?] wol

> dörffte

endtlich eingewilliget werden

> welches hier ... insert # : Auß obigem würdt mein Hochgeneigter Herr Estats Rath von selbsten genugsam judiciren würdt, wie höchst nöthig es seye daß

die subsidien richtig erfolge

> zumahl

die subsistentz der [65] nicht anderst als mit bahrem geld [255] zuwegen gebracht werden

> [note: /insert]

> ...

mit der resilution[?resolution] sowol von ihr als von den [376] das sie denselben in seinem be[384]hren[?] wegen einer portion in den [250]

> wie

auch wegen einiger qvartier zum unterhalt seiner völcker

> weilen

ihn die subsidien von [189] ab [5] werden

> gantz

gerne so viel muglich an hand [5] wollen

> . wann sie ihn ...

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> Ihr Königl. May: seind vorgestern alhier glücklich angelangt ... da man dann Königl. seiten

die belagerung von wislur[?] vorgeschla[384]n[?] [211] [67] von den churfürst keineswegk[?keineswegs] vor gut und rathsam befunden werden wolen[?wollen],

> sondern

es [103] derselbe vielmehr davor gehalten, das man gesamter hand in [293] [5] und den [118] daselbsten zu ruinieren trachten würde, [211] den[?] auch

> allem ansehen nach unangesehen

sich dabey wegen der subsistence keine geringe difficulteten [242] von ihr [341] churfürst darauf feste bektehet[?], wol

> dörffte

endtlich eingewilliget werden

> welches hier ... insert # : Auß obigem würdt mein Hochgeneigter Herr Estats Rath von selbsten genugsam judiciren würdt, wie höchst nöthig es seye daß

die subsidien richtig erfolge

> zumahl

die subsistentz der [65] nicht anderst als mit bahrem geld [255] zuwegen gebracht werden

> [note: /insert]

> ...

mit der resilution[?resolution] sowol von ihr als von den [376] das sie denselben in seinem be[384]hren[?] wegen einer portion in den [250]

> wie

auch wegen einiger qvartier zum unterhalt seiner völcker,

> weilen

ihn die subsidien von [189] ab [5] werden,

> gantz

gerne so viel muglich an hand [5] wollen

> . wann sie ihn ...

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 4 | 9-12 | `wislur` | wismar | `wislur[?]` | not printed: decode too far from the word (similarity 0.67 < 0.75) |
| 5 | 13-20 | `vorgeschla[384]n` | vorgeschlagen | `vorgeschla[384]n[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 6 | 21-21 | `[211]` | (none) | `[211]` | not printed: no word in the ledger |
| 7 | 22-22 | `[67]` | (none) | `[67]` | not printed: no word in the ledger |
| 11 | 27-31 | `keineswegk` | keineswegs | `keineswegk[?keineswegs]` | printed as emendation (similarity 0.90) |
| 18 | 45-47 | `wolen` | wollen | `wolen[?wollen]` | printed as emendation (similarity 0.91) |
| 20 | 49-49 | `[103]` | (none) | `[103]` | not printed: no word in the ledger |
| 30 | 72-72 | `[293]` | (none) | `[293]` | not printed: no word in the ledger |
| 31 | 73-73 | `[5]` | (none) | `[5]` | not printed: no word in the ledger |
| 34 | 76-76 | `[118]` | (none) | `[118]` | not printed: no word in the ledger |
| 40 | 98-98 | `[211]` | (none) | `[211]` | not printed: no word in the ledger |
| 41 | 99-99 | `den` | (none) | `den[?]` | not printed: no word in the ledger |
| 51 | 127-127 | `[242]` | (none) | `[242]` | not printed: no word in the ledger |
| 54 | 131-131 | `[341]` | (none) | `[341]` | not printed: no word in the ledger |
| 58 | 139-143 | `bektehet` | (none) | `bektehet[?]` | not printed: no word in the ledger |
| 70 | 179-179 | `[65]` | (none) | `[65]` | not printed: no word in the ledger |
| 77 | 192-192 | `[255]` | (none) | `[255]` | not printed: no word in the ledger |
| 83 | 204-209 | `resilution` | resolution | `resilution[?resolution]` | printed as emendation (similarity 0.90) |
| 90 | 219-219 | `[376]` | (none) | `[376]` | not printed: no word in the ledger |
| 96 | 230-234 | `be[384]hren` | begehren | `be[384]hren[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 102 | 245-245 | `[250]` | (none) | `[250]` | not printed: no word in the ledger |
| 115 | 276-276 | `[189]` | (none) | `[189]` | not printed: no word in the ledger |
| 117 | 279-279 | `[5]` | (none) | `[5]` | not printed: no word in the ledger |
| 125 | 293-293 | `[5]` | (none) | `[5]` | not printed: no word in the ledger |

## Caveats

- Blind reader b172 saw the sign-to-letter map before transcribing this letter (NOTES caveat 2). The '# :' insert is clear text placed at its mark.
- Code 262 (v4 'selbe') occurs 2 time(s) here and is printed as decoded; a glossed 1675 copy contradicts v4 for 262 in 3 of 3 places (query, key unchanged; NOTES caveat 7).
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

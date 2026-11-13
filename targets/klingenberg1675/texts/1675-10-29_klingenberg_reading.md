# Biermann to Klingenberg, 29 Oct 1675 (docketed), unit 260196 images 205R-206L: German reading, holes in place

Built by rule from the frozen first transcription (`1675-10-29_klingenberg_transcription.txt`), the single decode made from it with map v4 (`1675-10-29_klingenberg_decryption.txt`) and the ledger (`1675-10-29_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 35/(35 + 9 + 0) = 35/44 = 79.55%. Of the 9 E units, 4 are printed with an emendation and 5 are left as decoded.

## Reading

> ... allergnädigst für gut, dass derselbe der

officierer und anderer zur defe<δ>sion[?] und sicherheit des reichs [107] begehrten mittel darauf bestehe dasselbe von den staten kraf[?krafft] der mit ihnen aufgerichteten tractaten auf ihre eigemu[?] unkmsten[?unkosten] geleistet werden

> müssen, massen da solches nicht geschehen solte man nicht sihet

woher die darzu erforderte mittel in [107]

> als woselbst ohne das alles gar

gemou[?] zummen[?zusammen] gehet her genemmen[?genommen] werden würden

> .

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> ... allergnädigst für gut, dass derselbe der

officierer und anderer zur defe<δ>sion[?] und sicherheit des reichs [107] begehrten mittel darauf bestehe, dasselbe von den staten kraf[?krafft] der mit ihnen aufgerichteten tractaten auf ihre eigemu[?] unkmsten[?unkosten] geleistet werden

> müssen, massen da solches nicht geschehen solte man nicht sihet

woher die darzu erforderte mittel in [107]

> als woselbst ohne das alles gar

gemou[?] zummen[?zusammen] gehet, her genemmen[?genommen] werden würden

> .

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 5 | 13-18 | `defe<δ>sion` | defension | `defe<δ>sion[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 10 | 31-31 | `[107]` | (none) | `[107]` | not printed: no word in the ledger |
| 19 | 54-56 | `kraf` | krafft | `kraf[?krafft]` | printed as emendation (similarity 0.80) |
| 27 | 74-77 | `eigemu` | eigene | `eigemu[?]` | not printed: decode too far from the word (similarity 0.67 < 0.75) |
| 28 | 78-84 | `unkmsten` | unkosten | `unkmsten[?unkosten]` | printed as emendation (similarity 0.88) |
| 37 | 108-108 | `[107]` | (none) | `[107]` | not printed: no word in the ledger |
| 38 | 109-111 | `gemou` | genau | `gemou[?]` | not printed: decode too far from the word (similarity 0.60 < 0.75) |
| 39 | 112-115 | `zummen` | zusammen | `zummen[?zusammen]` | printed as emendation (similarity 0.86) |
| 42 | 121-125 | `genemmen` | genommen | `genemmen[?genommen]` | printed as emendation (similarity 0.88) |

## Caveats

- The small triangle sign (label Δ, new in this draft) has no value in the sign map and stands as `<δ>` in `defe<δ>sion`.
- Code 262 (v4 'selbe') occurs 1 time(s) here and is printed as decoded; a glossed 1675 copy contradicts v4 for 262 in 3 of 3 places (query, key unchanged; NOTES caveat 7).
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

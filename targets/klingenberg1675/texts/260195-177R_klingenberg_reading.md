# Biermann to Klingenberg, [Aug] 1675 (estimated; answers relation of 30/20), unit 260195 images 177R-178: German reading, holes in place

Built by rule from the frozen first transcription (`260195-177R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260195-177R_klingenberg_decryption.txt`) and the ledger (`260195-177R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 43/(43 + 14 + 0) = 43/57 = 75.44%. Of the 14 E units, 4 are printed with an emendation and 10 are left as decoded.

## Reading

> ... auch die rückständige Subsidien ... mit der ersten post von meinem Hochgeneigten Herrn Estats Rath deßhalb vergnügliche nachricht zu erhalten, damit

sie in ermanglung des b[?]

> [note: insert]

m[?] guten vorsatz und vorhabe[?vorhaben] den

> [note: /insert]

en[?] in ihre krieg operationen nicht gehindert werden mo[384]n[?]

> . Von

den [356] habe wir noch keine nachricht es ist [67] nicht wenig zu besor[384]n[?] das er

> widrumb

so lang temporisieren. [301] er sehe wie die belagerung der detrier[?trier] und

> die Kriegsactiones

[424] den kehserlichen[?keyserlichen] general montecuculi und den [91] ablauefen.[?ablauffen.]

> Was die officierer anlangt ...

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> ... auch die rückständige Subsidien ... mit der ersten post von meinem Hochgeneigten Herrn Estats Rath deßhalb vergnügliche nachricht zu erhalten, damit

sie in ermanglung des b[?]

> [note: insert]

m[?] guten vorsatz und vorhabe[?vorhaben] den

> [note: /insert]

en[?] in ihre krieg operationen nicht gehindert werden mo[384]n[?]

> . Von

den [356] habe wir noch keine nachricht; es ist [67] nicht wenig zu besor[384]n[?] das er

> widrumb

so lang temporisieren. [301] er sehe, wie die belagerung der detrier[?trier] und

> die Kriegsactiones

[424] den kehserlichen[?keyserlichen] general montecuculi und den [91] ablauefen.[?ablauffen.]

> Was die officierer anlangt ...

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 5 | 11-11 | `b` | (none) | `b[?]` | not printed: no word in the ledger |
| 6 | 12-12 | `m` | (none) | `m[?]` | not printed: no word in the ledger |
| 10 | 21-22 | `vorhabe` | vorhaben | `vorhabe[?vorhaben]` | printed as emendation (similarity 0.93) |
| 12 | 24-25 | `en` | (none) | `en[?]` | not printed: no word in the ledger |
| 20 | 44-46 | `mo[384]n` | mogen | `mo[384]n[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 22 | 48-48 | `[356]` | (none) | `[356]` | not printed: no word in the ledger |
| 30 | 62-62 | `[67]` | (none) | `[67]` | not printed: no word in the ledger |
| 34 | 66-70 | `besor[384]n` | besorgen | `besor[384]n[?]` | not printed: decode holds a code with no value, an unread sign or a blot |
| 40 | 84-84 | `[301]` | (none) | `[301]` | not printed: no word in the ledger |
| 47 | 98-102 | `detrier` | trier | `detrier[?trier]` | printed as emendation (similarity 0.83) |
| 49 | 104-104 | `[424]` | (none) | `[424]` | not printed: no word in the ledger |
| 51 | 106-112 | `kehserlichen` | keyserlichen | `kehserlichen[?keyserlichen]` | printed as emendation (similarity 0.92) |
| 56 | 125-125 | `[91]` | (none) | `[91]` | not printed: no word in the ledger |
| 57 | 126-133 | `ablauefen.` | ablauffen. | `ablauefen.[?ablauffen.]` | printed as emendation (similarity 0.90) |

## Caveats

- Blind reader b172 saw the sign-to-letter map in a grep output before transcribing this letter (it froze its transcription before any decode or alignment; NOTES caveat 2).
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

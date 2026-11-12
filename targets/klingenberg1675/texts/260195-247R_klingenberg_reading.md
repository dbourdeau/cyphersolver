# Biermann to Klingenberg, late Sept 1675 (estimated; loose leaf, no docket), unit 260195 images 247R: German reading, holes in place

Built by rule from the frozen first transcription (`260195-247R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260195-247R_klingenberg_decryption.txt`) and the ledger (`260195-247R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 40/(40 + 8 + 0) = 40/48 = 83.33%. Of the 8 E units, 5 are printed with an emendation and 3 are left as decoded.

## Reading

zu beforderung ihrer commercien an hand zu gehen und keini[?keine] mubillig[?unbillig] massige mittel so dar zu diemun[?] können aufzuschlagen

> es ist unnoethig meinem hochgeneigten Herrn Estats Rath die motiven anzufuehren aber ... die Staten general ... zu einer favorablen entschliessung zu disponieren weilen dieselben Ihnen vorhin zur genuege bekandt

die staten auch selbsten durch die erfahrumng[?erfahrung] gelermut[?gelernet] den

> wir

ubel sie gethan das sie [280] zu denen in den [151] angezogemun[?angezogenen] bremsebroischen tractaten erlangten vortheilen geholfen und das sie

> fuer gewiss

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

zu beforderung ihrer commercien an hand zu gehen, und keini[?keine] mubillig[?unbillig] massige mittel, so dar zu diemun[?] können, aufzuschlagen.

> es ist unnoethig meinem hochgeneigten Herrn Estats Rath die motiven anzufuehren aber ... die Staten general ... zu einer favorablen entschliessung zu disponieren weilen dieselben Ihnen vorhin zur genuege bekandt

die staten auch selbsten durch die erfahrumng[?erfahrung] gelermut[?gelernet], den

> wir

ubel sie gethan, das sie [280] zu denen in den [151] angezogemun[?angezogenen] bremsebroischen tractaten erlangten vortheilen geholfen, und das sie

> fuer gewiss

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 10 | 26-27 | `keini` | keine | `keini[?keine]` | printed as emendation (similarity 0.80) |
| 11 | 28-32 | `mubillig` | unbillig | `mubillig[?unbillig]` | printed as emendation (similarity 0.88) |
| 17 | 44-46 | `diemun` | dienen | `diemun[?]` | not printed: decode too far from the word (similarity 0.67 < 0.75) |
| 26 | 67-74 | `erfahrumng` | erfahrung | `erfahrumng[?erfahrung]` | printed as emendation (similarity 0.95) |
| 27 | 75-79 | `gelermut` | gelernet | `gelermut[?gelernet]` | printed as emendation (similarity 0.75) |
| 34 | 91-91 | `[280]` | (none) | `[280]` | not printed: no word in the ledger |
| 39 | 98-98 | `[151]` | (none) | `[151]` | not printed: no word in the ledger |
| 40 | 99-104 | `angezogemun` | angezogenen | `angezogemun[?angezogenen]` | printed as emendation (similarity 0.82) |

## Caveats

- Both readers missed most of a left-margin cipher insert keyed by the triple-bar mark over 'y H 78' (b176: `124? [blot] 172 E x / 233 [blot] E y K # 461 140`); the first reader got only 'x' and '140', which stand in the main line. The words around `erfahrumng` and `gelermut` are therefore incomplete; nothing of the insert is supplied here.
- clear text 'es ist unnoethig' stands in the transcription inside the token range of the word `aufzuschlagen` (after token 51); given after that word
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

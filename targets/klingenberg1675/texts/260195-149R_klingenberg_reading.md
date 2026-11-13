# Biermann to Klingenberg, Aug 1675 (estimated; answers relation of 13/3 Aug), unit 260195 images 149R-150R: German reading, holes in place

Built by rule from the frozen first transcription (`260195-149R_klingenberg_transcription.txt`), the single decode made from it with map v4 (`260195-149R_klingenberg_decryption.txt`) and the ledger (`260195-149R_klingenberg_ledger.tsv`); not polished. No key value is added and no unread code is guessed. One word unit of the ledger is one word here:

- a word printed plain is an S unit: its cipher groups decode to it letter for letter;
- `decode[?word]` is an E unit printed with the ledger's intended word as an emendation (every E unit is in the list at the end). The word is printed only where the emendation is obvious by one fixed test: the decode holds no code without a value, no unread sign and no blot, and it matches the word at 0.75 or more (difflib ratio, after ä/ö/ü to a/o/u, ß to ss, and c taken as g, since # (c) and H (g) are the signs the readers dispute);
- `decode[?]` is an E unit whose ledger word is not printed (none given, or not obvious by the test);
- `[n]` is a code with no value in v4 (inside a decode as well); `<x>` is a sign with no value in the decoder's sign map (`<[>`, `<t>`, `<d>`, `<w>`, `<δ>`); `<blot>` inside a decode is a blotted token inside the unit; `[blot]` is an N unit (blot or unread group, no word to judge); a standalone ` .` is a full stop decoded as its own unit.

Lines beginning `>` are the clear (uncoded) text, copied from the braces of the transcription as the first reader wrote them: approximate, not counted, ae/oe/ue and `...` (not read) as written. `> [note: ...]` is a note of the first reader inside the braces (insert marks, struck text), not text of the letter. Spelling is the cipher's; no capitals are supplied in the cipher passages. The second section, `Punctuated reading`, repeats the text with punctuation of ours.

Ledger figures for this passage (unchanged, as filed; see `NOTES_addition_2026-11-13.md`): strict S/(S+E+N) = 39/(39 + 15 + 1) = 39/55 = 70.91%. Of the 15 E units, 2 are printed with an emendation and 13 are left as decoded.

## Reading

> ... alß was der

alhie befindlichen [327] schiff

> daß die darumb [struck] für ... nemblich desideriren daß [struck] dieselbe den

winter über alhie [219] mogen [341] alsden

> entweder

[blot]

> oder vorhero

in

> [note: [struck]]

den herbst sich gelegenheit praesentieren .[?] etwas

> [note: [insert mark]]

in [202]en[?] oder

> anderstwo

auf den [335] vorzunehmen [619]r[?] zu besacte[?besagte] schiff und die

> [note: [150L]]

darauf vorhanden etscha<[>t[?] [139] sein [418]

> daher Ihr Königl. May. gerne sehen daß mein hochgeneigter Herr Estats Rath es dahin bringen könte damit solche dero intention [struck] gemäß [struck]

alhie überwintern .[?]

> der andere punct betrifft die von dem Bischoff Münsterischen Ministro im Haag meinem hochgeneigten Herrn Estats Rath gethane eröffnung ... [150R] Herr Estats Rath die begehrte vollmacht zu zusenden [struck]

desen[?dessen] proposition anzuhoren

> und [struck]

darauß zu referieren

> damit Ihnen

die [139]e[?] [355]es[?] darauf können zugesandt werden

> . Die Flotte ligt allerdings fertig und wartet nur auff den windt ... Und Ich verbleibe

## Punctuated reading

The reading above, line for line, with punctuation of ours added to the cipher passages (13 Nov 2026) so that it can be read as sentences against the translation. Only commas, semicolons and full stops after words are added. No decoded letter, hole or word division is changed: a script stripped our marks and compared the result with the reading above, unit for unit, before filing. The word division is the ledger's. The clear-text lines (`>`) are unchanged.

> ... alß was der

alhie befindlichen [327] schiff

> daß die darumb [struck] für ... nemblich desideriren daß [struck] dieselbe den

winter über alhie [219] mogen [341] alsden

> entweder

[blot]

> oder vorhero

in

> [note: [struck]]

den herbst sich gelegenheit praesentieren .[?] etwas

> [note: [insert mark]]

in [202]en[?] oder

> anderstwo

auf den [335] vorzunehmen, [619]r[?] zu besacte[?besagte] schiff und die

> [note: [150L]]

darauf vorhanden etscha<[>t[?] [139] sein [418]

> daher Ihr Königl. May. gerne sehen daß mein hochgeneigter Herr Estats Rath es dahin bringen könte damit solche dero intention [struck] gemäß [struck]

alhie überwintern .[?]

> der andere punct betrifft die von dem Bischoff Münsterischen Ministro im Haag meinem hochgeneigten Herrn Estats Rath gethane eröffnung ... [150R] Herr Estats Rath die begehrte vollmacht zu zusenden [struck]

desen[?dessen] proposition anzuhoren,

> und [struck]

darauß zu referieren,

> damit Ihnen

die [139]e[?] [355]es[?] darauf können zugesandt werden

> . Die Flotte ligt allerdings fertig und wartet nur auff den windt ... Und Ich verbleibe

## Emendations and ledger words not printed

Every E unit of the ledger, in order. Unit = position in the ledger (1-based); tokens = first-last cipher token (0-based, as the ledger).

| unit | tokens | decode | ledger word | printed | note |
|---|---|---|---|---|---|
| 3 | 8-8 | `[327]` | (none) | `[327]` | not printed: no word in the ledger |
| 8 | 16-16 | `[219]` | (none) | `[219]` | not printed: no word in the ledger |
| 10 | 20-20 | `[341]` | (none) | `[341]` | not printed: no word in the ledger |
| 19 | 48-48 | `.` | (none) | `.[?]` | not printed: no word in the ledger |
| 22 | 53-55 | `[202]en` | (none) | `[202]en[?]` | not printed: no word in the ledger |
| 26 | 59-59 | `[335]` | (none) | `[335]` | not printed: no word in the ledger |
| 28 | 63-64 | `[619]r` | (none) | `[619]r[?]` | not printed: no word in the ledger |
| 30 | 66-69 | `besacte` | besagte | `besacte[?besagte]` | printed as emendation (similarity 1.00); c for g (# read for H?) |
| 36 | 80-86 | `etscha<[>t` | (none) | `etscha<[>t[?]` | not printed: no word in the ledger |
| 37 | 87-87 | `[139]` | (none) | `[139]` | not printed: no word in the ledger |
| 39 | 89-89 | `[418]` | (none) | `[418]` | not printed: no word in the ledger |
| 42 | 97-97 | `.` | (none) | `.[?]` | not printed: no word in the ledger |
| 43 | 98-100 | `desen` | dessen | `desen[?dessen]` | printed as emendation (similarity 0.91) |
| 50 | 124-125 | `[139]e` | (none) | `[139]e[?]` | not printed: no word in the ledger |
| 51 | 126-128 | `[355]es` | (none) | `[355]es[?]` | not printed: no word in the ledger |

## Caveats

- The shuffle margin is narrow on seed 20261112 (best -4.1559 against true -4.1543). One H/# disagreement with the blind reader b172 unresolved.
- 1 E unit(s) decode c where the ledger's word has g (marked in the list). c is the value of #, g of H; given the H/# disputes these may be sign misreads rather than spelling. The decode is not changed.
- One first reader, not blind to the key, transcribed, decoded once and judged this passage; the intended words were written after decoding (NOTES caveat 1). Umlaut-less spellings are counted S by the standing rule (NOTES caveat 3).

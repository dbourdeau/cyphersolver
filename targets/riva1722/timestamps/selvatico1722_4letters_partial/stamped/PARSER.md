# PARSER.md. Tokeniser/parser contract for the Riva-Vienna number cipher (Selvatico 1722, Starhemberg 1726)

Version P1, 12 Nov 2026 (AEST). Written BEFORE any decode in b70. One implementation: scripts/dec.py (python3 -I, standard library only).
It answers the red-team finding that 53 of 136 lines decoded differently because these rules were unstated.
Scope: WAINUT passes A/B (their TRANSCRIPTION_RULES.md), b57 pass A (20 Mar 1726) and b70 pass C.

## 1. Lines
- A data line is `ID: body` where ID matches `^\d+[rv]\.L\d+$`. Everything else (blank, `#...`) is ignored.
- One manuscript line = one data line. Units are numbered 1..n per line in order (struck and illegible groups keep a number).

## 2. Body, in this order
1. `{...}` = clear (plain) text. Passed through as «...». Never decoded, never a unit. (WAINUT's `{blot 52}` and `{struck-through}` are therefore not units.)
2. `[struck]` standing alone = a group cancelled by the writer: one unit of class X.
   `[...]` glued to a group: `[struck]` makes that group class X; any other bracket note (e.g. `[hatched below]`) is removed and sets flag D.
3. `^(G)` = a small raised group (written above the line end): unit G with flag R. R is not a doubt.
4. Split on whitespace. For each chunk:
   a. strip trailing `=` (line-end hyphen) and then trailing `. , : ;` (punctuation); repeat until stable. A chunk that is now empty is dropped.
   b. split on `-` (link stroke between groups). Empty pieces and a bare `?` are dropped.
   c. each piece is one unit.

## 3. Unit grammar
`[c][x]DIGITS` followed by any mix of `_`, `'`, `?`, `^n`.
- DIGITS = the number as written. Canonical token = DIGITS plus `_` if an underline is present. Lookup uses the canonical token only.
- `_` underline. Selects the underlined value. Order of suffixes is irrelevant: `74'_` = `74_'`, `56?_` = `56_?`, `8?_` = `8_?`.
- `'` short stroke/dot above. NEVER changes the key lookup. It is printed after the value as `'`. (K3 reading rule, section 6.)
- `^n` small raised numeral. Never changes the lookup. Printed as `^n`.
- `?` reader doubt. The value is still decoded. Sets flag D.
- `c` curl before the group (WAINUT). Ignored for lookup. Sets flag C (treated as a doubt: in this hand the curl is part of 3 or 8).
- `x` x-shaped sign before the group (1726 letters): value = `h` + value for 1 or 2 digit groups; for a 3-digit group the x is ignored and flag D set.
- `A|B` alternatives (WAINUT). The FIRST alternative is decoded. Flag ALT unless every alternative has the same canonical token.
- A piece containing `#`, or a `?` in place of a digit (`?28`), or anything that does not fit the grammar: class ILL.

## 4. Classes and literal output
| class | test | literal output |
|---|---|---|
| SYL | canonical token in key, value lower case | value |
| WORD | canonical token in key, value upper case | VALUE |
| CODE | DIGITS >= 100 | `{nnn}`; if the key gives a value, `{nnn=VALUE}` |
| UNK | DIGITS < 100, canonical token not in key | `{nn}` or `{nn_}` |
| ILL | illegible | `#` |
| X | struck by the writer | `[x]` |
No fallback: an underlined token missing from the key is UNK. It does not fall back to the plain value, or the reverse.

## 5. Strict ledger (per unit)
- X units are outside every denominator (listed, counted separately).
- N: class ILL.
- E: class CODE (always, even when K3 proposes a value); class UNK; any unit with flag D, C or ALT; any unit downgraded in the overrides file (reason given: value emended in the reading, or word not read).
- S: class SYL/WORD, no D/C/ALT flag, and not downgraded.
- Strict % = S / (S+E+N). A second figure "codes with a K3 value counted S" is reported separately and labelled.
- Overrides can only downgrade S to E. Nothing is ever upgraded by hand.

## 6. Reading rules (K3, applied in the Italian reading, not in the literal decode)
- `'` over a consonant+vowel group = the consonant is doubled (ssi, lla, nno, ffa, tto, bbe) or, on a final/vowel group, an accent (rè, tà, è, sarà).
- Doubled consonants not marked are written once (system feature, b57 LOG). Supplying them in the reading is not an emendation.
- `^3` over a code = plural/-i ending of the code word.
- Word division, apostrophes, capitals and accents are editorial.

## 7. What is NOT in the parser
No sense-based choice between alternatives; no silent repair; no mapping of `'` to underline.

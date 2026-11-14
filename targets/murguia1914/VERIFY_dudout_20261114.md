# murguia1914: independent check of the key (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/murguia1914` reads only `key.tsv` and the group column of
`transcription_LXVIII-1.14.1943.1.txt` (not `scripts/decrypt.py`). 23 segments, 488 groups. Every decoded segment is
identical to `decryption_LXVIII-1.14.1943.1.txt`.

## Key layout
Each decade of the table is a reversed alphabet block: 10-19 and 20-29 = a j i h g f e d c b; 30-39 and 40-49 = l rr r
q p o ñ n m ll; 50-59 and 60-69 = s . . z y x w v u t (51 = -mente); 7x-9x word groups. Every value taken from the pairs
fits this layout. Key correction: none.

## Scan (CEHM, LXVIII-1.14.1943.1.0001, public JPG)
- 88 (S13) and 97 (S12) are clearly typed; neither is a misread 78 or 87.
- S11, 22nd group: over-struck, 58 or 68 (both u), as noted.

## Reading note (not adopted)
S13 decodes `69 35 38 10 42 40 10` = *tomarla*, then 88. If 88 = *por*: "no habiéndonos sido posible tomarla por ser el
enemigo en número muy considerable", with no supplied word. 78 is already *por* (S17) and 88 occurs once, so this is
a second possibility beside [?plaza:88] + [por], not a reading.

## Read bar (README)
The recorded 0.952 (99 of 104 words: {+O} x2, [?no:97], [?plaza:88], [por] not read) follows the README rule.
`research/reading_audit/v10_relabel.measure` gives 0.985 on the same file: `v2_score.holes` does not treat the `{+x}`
markers of SIGN_CONVENTIONS.md as holes. A run of `v10_relabel.py --apply` would overwrite the stricter figure.

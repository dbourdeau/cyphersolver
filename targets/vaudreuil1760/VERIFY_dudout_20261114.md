# vaudreuil1760: independent check of the key and recount (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/vaudreuil1760` reads only `key/key274.json` and `key/overrides.json` and decodes
`transcription.txt` (not `tools/decode.py`). 2401 legible number groups; none lacks a cell. The decoded syllables,
accents and spaces removed, align with the letters of `reading.md` at 97.5% (per folio 0.958-0.996). The larger
differences are the clear words, the groups lost in the gutter and the open groups of `gaps.json`, with one exception:

- **f. 152r, l. 265 of transcription.txt**: `672 672^ 51 51 | 494` decodes "me me t t / un". `reading.md` has "me
  mettroit en état" with no mark. 494 = *un* is a confirmed cell (NOTES, f.149v); "roit" is a correction of the
  writer's group, and should be marked as supplied ([roit] or similar) like the other restorations.

Key correction: none found.

## Read bar (README)
`profile.json` gives `read_share` 0.96: that is the share of groups read (2328 of 2424, `tools/stats.py`). The README's
per-document bar is a share of words: `research/reading_audit/v10_relabel.measure` on `reading.md` gives **0.937** over
1531 words (the `[...]`, `[?]` and part-word restorations counted as holes). By that rule the letter is under 0.95 and
would be *read in part*. The profile is not changed here; the class is left to the maintainer.

## Not done
The LAC images (e000875753-58) were not fetched.

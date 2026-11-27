# gonzaga1537 re-check layer (27 Nov 2026)

A line-by-line check of the contributor's transcription of c. 13r (L01-L24) and c. 13v (L25-L30) against the open
Estense IIIF canvases (`.../images/iiif/db/73bcd847-3cc8-46c4-89d8-572438763b8e` for c. 13r and
`.../78a73966-7232-4e7a-af55-356d10d844de` for c. 13v; manifest
`https://edl-jarvis.cultura.gov.it/meta/iiif/22b3126b-3b70-4ede-a33b-1adf4a4491f6/manifest`). Each canvas was fetched
at full size (3094 x 4120 and 3094 x 4112 px) as nine 1500-px regions, one request at a time, and stitched; the images
are kept outside the repository.

**The images were viewed by an AI model only (Claude, for the maintainers).** No person has looked at these places.
The check was not blind: the filed transcription was in view. Every place where the model settled a choice between
look-alike signs is labelled `probable` and counts as a hole on the read bar until a blind human reader confirms it.

The contributor's files (`../transcription_13r_13v.txt`, `../key_gonzaga1537.tsv`, `../decryption_13r_13v.txt`,
`../reading_13r_13v.md`) are not edited.

## Files

- `corrections.tsv`: every place looked at (the 17 bracketed scribal slips, the places NOTES flagged, and the other
  doubts found on the read-through): place, filed label, label on the image, confidence, decode before and after,
  effect on the count.
- `transcription_13r_13v_recheck.txt`: the filed transcription with the 12 corrections applied (11 tokens changed, one
  token rejoined).
- `decrypt_recheck.py` -> `decryption_13r_13v_recheck.txt`: the contributor's own decoder and key run unchanged on
  the re-checked transcription.
- `reading_13r_13v_recheck.md`: the contributor's reading with only the corrected places changed; `[≈word]` marks a
  probable word.

## Counts (README rule: sure words only; `research/reading_audit/v10_relabel.py`, `clear_markup=⟨⟩`)

| | sure | probable | other holes | cipher words | read share |
|---|---:|---:|---:|---:|---:|
| filed reading (before) | 219 | 0 | 48 | 267 | 0.820 |
| re-check layer (after) | 221 | 10 | 36 | 267 | 0.828 |

Sure gains: L23 `essendo` (a sign left out of the transcription) and L19 `resa`. Probable (10): L02 and L03 `pio`, L04
`vero` and `è`, L10 `demostrato`, L11 `quele`, L13 `respetto`, L16 `Al`, L19 `è`, L27 `peggiore`. With the probable
words granted the share would be 231/267 = 0.865; with every hole except the 22 open codes granted, 245/267 = 0.918.
The short-text floor does not apply (267 words).

## What stays open

- 22 open codes (13 nomenclator tokens, 9 two-digit tokens): no key sheet, no same-key sibling online.
- 14 words where the image shows what the transcription has, and what it shows is the writer's slip or an unvalued
  shape: L01 `s4filaxagi`, L03 `icrftb394gb`, L05 `igb`, L05 `fiirsibpi4`, L06 `iffi`, L08 `riliérla4é4`, L09 `ir&`,
  L15 `ipirtiri4`, L19 `&lli`, L19 `fix`, L21 `e4,s.{ar}`, L23 `fi4ésir`, L27 `libigir`, L28 `tiusixdigi`.
- 10 probable words await a blind human sign check.

Not seen: the paper itself (ink, erasures under the blots at L20 and L27); signs under the blot on L20 `&u4` and the
struck sign between `o4éo4` and `3a`.

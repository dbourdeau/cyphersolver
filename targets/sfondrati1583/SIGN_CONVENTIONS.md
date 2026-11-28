# Sign & Factored Transcription Conventions — `targets/sfondrati1583`

This document defines the canonical ASCII notation used across `transcript_2077_v2.txt`, `transcript_2518.txt`, `diplomatic_2077_core.txt`, `diplomatic_2518.txt`, and `key.tsv` (`k-sfondrati1583-cg12`) for the 1583 Spanish Milanese chancery cipher written by the secretariat of Carlo d'Aragona Tagliavia, Duke of Terranova, to Baron Paolo Sfondrati (Aug–Oct 1583). In architecture and its one-letter `e -> f` shift, the system matches Satoshi Tomokiyo's web summary of Philip II's 1582 general cipher `Cg.12` (`https://cryptiana.web.fc2.com/code/spanish3.htm`, sections `Cp.30 (1581)` and `Cg.12 (1582)`); no period key sheet has been compared table-for-table, so all rules below are described directly from `#2077` and `#2518`.

## 1. Factored Syllable Structure: `<Base>[<VowelMark>][<CodaMarks>]`

Every syllabic token in these letters is factored into up to three components:
1. **Base sign:**
   - Bare vowels / letters: `7, f` (`e`, with `f` standing for `e`), `8, Δ` (`a`), `5` (`i`), `21` (`o`), `18` (`u`), `{, 17` (`y`).
   - Single-consonant bases: `1` (`b`), `2` (`d`), `3` (`f`), `4` (`h`/`b`), `5` (`j`/`p`), `6` (`g`), `9` (`c`), `10` (`l`), `11` (`n`), `12` (`p`), `13` (`r`), `14` (`t`), `15` (`x`), `16` (`z`/`ç`), `17` (`y`), `18` (`v`/`u`), `19` (`s`), `20` (`qu`), `22` (`m`), `D` (`ch`).
   - Partial alphabetical consonant-cluster series (`23..34`): `23` (`bl`), `24` (`br`), `26` (`cr`), `27` (`dr`), `29` (`fr`), `31` (`gr`), `32` (`pl`), `33` (`pr`), `34` (`tr`), while slot `25` (*cl*) is unattested in the sampled corpus and `28` (`1×`), `30` (`1×`) remain singleton guesses.
   - Inflected stem: `60` (`auis-` -> `60| = auisa`, `60|, = auisar`, `60e = auise`).
2. **Right-attached vowel marks (5):**
   - `|` = `a` (vertical stroke)
   - `e` = `e` (cursive e-hook)
   - `+` = `i` (4-shaped cross)
   - `.` = `o` (right baseline dot; on vowels and `14|.` / `96.` marks `-m`: `8. = am`, `7. = em`, `5_m = im`, `14|. = tam`, `96. = cum`)
   - `@` = `u` (6-shaped loop)
3. **Coda & orthographic marks:**
   - `'` (acute tick above) = coda `-n`
   - `^` (caret above) = coda `-s`
   - `,` (subscript comma) = coda `-r`
   - `:` (dot directly above) = coda `-l`
   - `*` (small cross above) = consonant gemination on `l, r, s, f` (`ll, rr, ss, ff`; across both transcripts the mechanical decoder produces zero `nn` onsets from starred signs — proposed `ñ` readings on `14+*` depend on reading an ambiguous onset as `n` and remain explicitly bracketed in `reading_*.md`)
   - `_m` = centered under-dot on `5` (`5_m = im`, visually distinct from right-dotted `5. = jo`)
   - `~` = horizontal overbar marking a **literal numeral** (`11~`, `100~`, `2~`, `3~`, `5~`, `10~`)
   - `°` = small circle above marking a scribal cancellation (`8° 2°`, `12°`, `2° 3°`) or special sign (`X° = la`, `c° = s`)

## 2. Handwritten Collisions & Contextual Alternatives

The transcripts preserve the manuscript's surface handwriting without silent retro-editing:
- **Reproducible `<1-digit base> + {|(1), +(4), @(6)}` forms (emitted directly by `decrypt.py`):** `31` (`3| = fa`, distinct from `31.` = `gro`), `36` (`3@ = fu`), `41` (`4| = ha`), `46` (`4@ = hu`), `56` (`5@ = ju`), `61` (`6| = ga`), `66` (`6@ = gu`), `91` (`9| = ca`), `96` (`9@ = cu`), `24` (`2+ = di`, distinct from vowel-bearing `24|`/`24e` = `bra`/`bre`), and `Di` (`D| = cha`).
- **Contextual alternatives NOT emitted by `decrypt.py` (always bracketed `[...]` in `reading_*.md`):** bare `21` emits `o` (contextual `2| = da`), bare `16` emits `z` (contextual `1@ = bu`), and bare `26` emits `a` (contextual `2@ = du`).
- **Ambiguous cursive pairs (always bracketed `[...]` in `reading_*.md`):** cross-bearing `14+`/`14|` sometimes sits where context requires `ni`/`na` (though `11e` and `14e` are clearly distinguishable on the scans); and three instances transcribed as bare `34` (`#2518 L08` *pliego*, `L15` *cumplimiento*, `Item 21 PS07` *suplico*) show a visible intermediate `2`-hook favoring `32+` (*pli*) rather than a rule that bare `34` means *pli* (see `NOTES.md`, `## Transcription doubts`).

## 3. Nomenclators & Diplomatic Conventions

- Underlined numeral nomenclators carry `=` (e.g., `21=`, `23=`, `38=`, `40=`, `48=`, `58=`, `59=`, `71=^`, `98e=^`).
- 2–4 letter alphabetical nomenclators are transcribed verbatim (`sim`, `hom`, `him`, `cem`, `hol`, `ful`, `sa`, `Si`, `xol`, `xa`, `Co`, `vul`, `vil`, `gil`, `com`, `nul`, etc.).
- Clear Spanish framing, virgules (`/`), and the three water-stain gaps on `#2518 p. 1 L01–L03` (`[stain]`) are isolated in `diplomatic_2077_core.txt` and `diplomatic_2518.txt` and excluded from the canonical cipher streams (`transcript_2077_v2.txt`, `transcript_2518.txt`).

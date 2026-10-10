# Transylvanian cipher letters, DECODE R4933-R4942

Status: in progress

## Sources

28 images downloaded from the ten DECODE records on 23 September 2026 using the existing authenticated session. Catalogue metadata saved alongside images. No document attachments listed. The catalogue dates are not confined to 1645. R4936 first page inspected: clear Hungarian introduction and long alphabetic cipher passages. No decipherment claimed.

## Prior work

User objective reports no published reading found on 22 September 2026. Independent verification remains pending.

The first R4936 annealing result preceded consultation of printed letters. Afterwards downloaded:

- Lukinich, *Keresdi Bethlen Ferencz levelezése*, first instalment (1907), https://real.mtak.hu/192384/1/MagyarTortenelmiTar_1907_55_4_08.pdf . Locally extracted to `Bethlen-correspondence-1907.txt`. Starts 1622, ends around 1647; no matching cipher reading established. Introduction points to a separate diplomatic study.
- Lukinich, *Keresdi báró Bethlen Ferencz*, first instalment (1908), https://real.mtak.hu/178743/1/717_cut_Szazadok_1908.pdf . First instalment is early biography, not yet an exact control.
- Unfollowed leads: the biography's later instalment https://real.mtak.hu/178739/1/825_cut_Szazadok_1908.pdf ; Szilágyi's 1873 *Okmánytár I. Rákóczy György svéd és franczia szövetkezéseinek történetéhez*; *Erdély és az északkeleti háború*, vol. 1, https://www.mek.oszk.hu/06500/06508/pdf/erdely1.pdf . These may contain independent editions or keys. Do not infer novelty from DECODE N/A.

## Progress, 23 September 2026

All 28 image files validated as image/jpg downloads; `image-manifest.json` gives hashes, sizes and exact download URLs. No credentials saved here. The contact sheet is for navigation only; inspect originals for reading.

| Record | Catalogue year | Work so far |
|---|---|---|
| R4933 | 1658, but name says 1628 | Two photographed spreads; requires detailed inspection and resolution of catalogue date conflict. |
| R4934 | 1628 | Two images; mostly cipher-looking text; not transcribed. |
| R4935 | 1628 | Four images; largely clear text, inspect short cipher insertions. |
| R4936 | 1645 | Both pages provisionally transcribed. Quadgram attack recovered Hungarian quickly. Many q/g, c/p, i/n transcription confusions remain. |
| R4937 | 1646 | Long single page. Partial extraction and successful Hungarian substitution fragments; no complete reading. |
| R4938 | 1647 | Four images, mainly clear text with short cipher insertion(s); not yet transcribed. |
| R4939 | 1648 | Two substantial text pages and address; not yet transcribed. |
| R4940 | 1648 | All surviving cipher read: 23 letters in two spans. See `R4940-reading.md`; both images inspected. |
| R4941 | 1648 | Different substitution, extract from pages 1–2 still not solved; pages 3–4 must also be inspected. |
| R4942 | 1648 | Partial page 2 extract yields Hungarian fragments. All other cipher spans still to inspect/transcribe. |

`attack.py` uses existing `hu-modern`, default quadgrams, no spaces, seed 4936, 50 x 12,000 trials. There was no need to add a duplicate Hungarian model. `python transylvania1645/attack.py R4941-extract 5` selects quintgrams. Early result filenames lack the order suffix; current script includes it. The raw inputs are PROVISIONAL and must not be presented as archival transcriptions.

Important transcription correction: a working shared alphabet family has c=p, p=c, g=u, q=t. The initial R4936 statistical key wrongly used c=u, g=t, q=p because the hand transcription confused these glyphs. `shared-key-hypothesis.json` fixes the proposed family mapping, with v/w representing a in different hands. This is not a verified full key for every record. First R4936 words are recognizably `persvadealni kell ...` and `... succumbalna szandekaban`; R4937 begins with `czasar dipplomaia ...`. R4940 is a useful held-out short reading using the family.

`noisy_probe.py` applies penalized alternatives to likely confused glyphs in R4936 and outputs `R4936-correction-hypotheses.json`. These are explicit UNVERIFIED hypotheses, not edits to the source transcription. They reveal coherent topics including musketeers, dragoons, payment, the king, the republic, Munkács and Rakovica. Every adopted correction needs an image check. Plaintext word spaces in explanatory notes are editorial.

## Remaining gaps

Nine records remain incompletely read, with many spans not attempted. These are NOT established outside blockers; continue work. R4940 still requires prior-art comparison and inclusion in the eventual group writeup. No percentage claimed for the group.

## Escalation / next work

1. Resolve transcription of R4936 q/g, c/e/p, i/n and other ambiguous forms against full-resolution crops; the substitution is substantially recoverable. Do not treat noisy language-model proposals as confirmed readings.
2. Transcribe the remaining R4937 and R4942 ciphertext; test shared family mapping, correcting the input rather than forcing bad mappings.
3. Inspect ALL original folios of R4933–35, R4938–39 and R4941. Short cipher spans may be solvable with sibling alphabets; R4941 needs separate attack and better transcription (long-s/f and g/q are suspects).
4. Follow the printed diplomatic-collection leads and compare dates/openings. Keep discovery chronology for contamination assessment. Consider period Hungarian corpus only if modern scoring remains insufficient after fixing the transcription.
5. Record every step in profile.json. It currently passes `docs/_check_profile.py` with unknowns explicitly retained.
6. Do not invoke writeup yet. User requires partial readings pushed toward completion first. Once the research is exhausted, use `.claude/skills/writeup/SKILL.md`, update DECODE queue and all required publication surfaces, and run its checker. Shared checkout has extensive unrelated modifications; stage explicit paths only if committing, and isolate any broad site rebuild as necessary.

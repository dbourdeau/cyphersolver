# Hellen to Frederick II, 1752–1763

Status: in progress. No cipher plaintext or key has been verified.

One-key check, 14 Oct 2026 (George Lasry's one-key rule): not split. The 1752 (R1953), 1756 (R1049) and 1763
(R1045-R1048, R1060, R1061) letters are grouped only provisionally into code families; no key or value has been
established for any of them, so the notes do not show that the families are distinct codes (or that they share
one). Split them into one entry per code as soon as a code is identified; until then the page says the grouping is
provisional and claims no shared key.

KHA, Prins Willem V, inventory 196; DECODE R1045, R1047, R1048, R1049,
R1060, R1061 and R1953. Related R1046 supplies additional 1763 material.

The 20 September 2026 audit and archival findings are recorded in
[AUDIT_2026-09-20.md](AUDIT_2026-09-20.md). This supersedes earlier claims
that the failed density tests proved random codebooks or an impossible solve.

Public progress report: https://dbourdeau.github.io/cyphersolver/hellen1752.html

## Reproduction

`audit_transcription.py` reads locally held DECODE `decode/DOC_*.txt` inputs.
Those source files and manuscript images are not distributed in this publication.
The measured projections used by `profile.json` are in `audit/`, with summary counts.
They preserve transcriber uncertainty and marks; they are not finished transcriptions.

The original analysis grouped the material provisionally into 1752, 1756 and 1763
code families. Searches of Politische Correspondenz volumes 9, 13, 22 and 23
found no matching plaintext. This does not establish that none exists elsewhere.

## Next step

Retrieve Nationaal Archief 1.10.29, Fagel inventory 5206 (catalogued as digitized
Hellen decipherments, 1752–1753), check for 4 January 1752, and compare the text
with R1953. No matching text has yet been inspected. The 1763 letters remain open.

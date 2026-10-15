# Latin numerical cipher letter of 1628, Riksarkivet Chifferklaver låda II:114 (DECODE R4284)

Status: attempted, open — 0 of 822 number groups deciphered; homophonic Latin annealing and two box keys failed; the
escalation (the other 68 box keys, the key-test leaf, Camerarius editions) is not done.

Split on 14 Oct 2026 from `riksarkivet1628` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 207
bundled 14 Riksarkivet records; they are unrelated ciphers, each now with its own entry: the Bremen letters of 1631
([`targets/riksarkivet1628/`](../riksarkivet1628/NOTES.md), read), R4282 (George Lasry's
[`targets/decode4282/`](../decode4282/NOTES.md)), R4306 ([`targets/riksarkivet4306/`](../riksarkivet4306/NOTES.md)),
Rusdorff 1628 ([`targets/rusdorff1628/`](../rusdorff1628/NOTES.md)) and E 708, 1633
([`targets/oxenstierna1633/`](../oxenstierna1633/NOTES.md)). Each is a different cipher, with its own page. The work
below was done on 21 Sept 2026 in the riksarkivet1628 session and is carried over from its NOTES; the transcription
moved here on 14 Oct 2026.

Work date: 2026-09-21. Catalogue item 207 (class A), still open for this record.

## The document

Riksarkivet, Stockholm, Chifferklaver låda II:114; DECODE R4284 (two PDF images, `IMG_R4284_I25750_P.pdf` and
`I25751`, public record; not committed). DECODE: undated (1600-1699), cleartext language Latin, Non-decrypted. An
archival note at the foot of the first page reads "Legat … till L. Camerarius bref för 1628": filed with the letters
to Ludwig Camerarius, the Palatine (and from 1626 Swedish) agent, for 1628. Comma-separated numbers with Latin words in
clear (*Sequentes etiam*, *pro eo tempore*, *praeter omnia alia*, *et quorum*, *Sed*, *Cum*, *Quo casu*, *Sed etiam
tam pro*). Beside it lies a leaf on which someone tried a *letter* cipher on four phrases: *effusorem sanguinis*,
*pestem patriae*, *praeter naturalem*, *disturbatorem religionis*.

## Transcription

`r4284_transcription.txt` (agent, 21 Sept 2026): 756 numbers and 108 distinct values in the 21 Sept count; about 20
multi-digit readings doubtful (possibly two numbers run together); one line is written twice in the manuscript.
Measured 14 Oct 2026 with `docs/_check_profile.py --measure`: 822 tokens, 170 distinct (the measure counts every
doubtful form as a value of its own).

## Work log

1. (21 Sept 2026) Homophonic Latin annealing (`targets/riksarkivet1628/solve_num.py`, quadgrams from `qg.py`;
   8 restarts x 250k), also over bands of four numbers: Latin-sounding nonsense only.
2. (21 Sept 2026) 70 key records of Chifferklaver låda II (R4259-R4329) fetched; the Siebenbürgen "Schauis" key
   (R4310, a = 9 50 71 86) and the 1632 key whose 30 ends every word (R4296) tested: neither fits.
3. (14 Oct 2026) Split from riksarkivet1628; transcription re-measured. No new attack.

## Remaining gaps
- R4284, all number groups - blocker: not-attempted; homophonic Latin annealing gave nonsense; only R4310 and R4296 of the 70 fetched key records tried; the key-test leaf is unused

## Escalation
- [x] siblings: all 14 records of catalogue 207 opened; 70 Chifferklaver key records R4259-R4329 fetched
- [ ] clear-pages: not done — the key-test leaf (four phrases over letter-cipher signs) not used
- [ ] known-keys: not done — only R4310 and R4296 tested; 68 key records untried
- [ ] print: not done — Camerarius correspondence editions not searched
- [x] key-rebuild: blind homophonic annealing on Latin (21 Sept 2026), no result
- [ ] retry: not done — no key to rerun with

## Next

Re-read the doubtful multi-digit numbers on the image; try the 68 other box keys; search the Camerarius editions for
a letter of 1628 matching the clear words.

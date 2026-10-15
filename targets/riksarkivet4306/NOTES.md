# Numerical cipher letter to "Mr ?ilick", Amsterdam, 1632?, Riksarkivet Chifferklaver låda II:133 (DECODE R4306)

Status: attempted, open — 0 of 465 number groups deciphered; annealing in ten languages and two box keys failed; the
other box keys and the digit-variant question are not settled.

Split on 14 Oct 2026 from `riksarkivet1628` under the one-key rule (George Lasry, 14 Oct 2026). Catalogue item 207
bundled 14 Riksarkivet records; they are unrelated ciphers, each now with its own entry: the Bremen letters of 1631
([`targets/riksarkivet1628/`](../riksarkivet1628/NOTES.md), read), R4282 (George Lasry's
[`targets/decode4282/`](../decode4282/NOTES.md)), R4284 ([`targets/riksarkivet4284/`](../riksarkivet4284/NOTES.md)),
Rusdorff 1628 ([`targets/rusdorff1628/`](../rusdorff1628/NOTES.md)) and E 708, 1633
([`targets/oxenstierna1633/`](../oxenstierna1633/NOTES.md)). Each is a different cipher, with its own page. The work
below was done on 21 Sept 2026 in the riksarkivet1628 session and is carried over from its NOTES; the transcriptions
moved here on 14 Oct 2026.

Work date: 2026-09-21. Catalogue item 207 (class A), still open for this record.

## The document

Riksarkivet, Stockholm, Chifferklaver låda II:133 (wrapper II:104); DECODE R4306 (three PDF images,
`IMG_R4306_I25832_P.pdf` - `I25834`, public record; not committed). DECODE: undated (1600-1699), no language,
Non-decrypted. Pencil "1632?" at the head; addressed to a "Mr ?ilick" at Amsterdam. Numbers separated by colons, no
clear text.

## Transcription

- `r4306_transcription.txt` (agent, 21 Sept 2026): 463 numbers in the 21 Sept count; measured 14 Oct 2026: 492 tokens,
  51 distinct, IoC 0.073.
- `r4306_v2.txt`: re-transcribed keeping the scribe's variant forms (34/74, 40/4o/9o, 30/3o/70/7o: 55 tokens);
  measured 465 tokens, 62 distinct. Whether the variants are distinct signs is not settled.

## Work log

1. (21 Sept 2026) Statistics: monoalphabetic by IoC (0.078 in the 21 Sept count), "34 42" x31.
2. (21 Sept 2026) Simple-substitution and homophonic annealing (`targets/riksarkivet1628/solve_num.py`) over
   quadgram models in nl, de, la, fr, sv, en, it, es, pt, da, also with low/high numbers as word breaks: no language
   converged (best about −4.3/char against about −2.5 for real text). A search bug (free changes propagating by swaps)
   and a backoff-model artefact were fixed first.
3. (21 Sept 2026) The same on `r4306_v2.txt`: no fit.
4. (21 Sept 2026) Box keys R4310 (Siebenbürgen "Schauis") and R4296 (1632, 30 ends every word) tested: no fit.
5. (14 Oct 2026) Split from riksarkivet1628; transcriptions re-measured. No new attack.

## Remaining gaps
- R4306, all number groups - blocker: not-attempted; annealing in ten languages failed on both transcriptions; the digit-variant question is open; only 2 of the 70 fetched key records tried

## Escalation
- [x] siblings: all 14 records of catalogue 207 opened; 70 Chifferklaver key records R4259-R4329 fetched
- [x] clear-pages: none; the letter has no clear text
- [ ] known-keys: not done — only R4310 and R4296 tested; 68 key records untried
- [ ] print: not done — the Amsterdam addressee not identified
- [x] key-rebuild: blind substitution and homophonic annealing in ten languages (21 Sept 2026), no result
- [ ] retry: not done — no key to rerun with

## Next

Settle the digit variants on the image; try the other box keys (a monoalphabetic key would show at once); identify
"Mr ?ilick" at Amsterdam.

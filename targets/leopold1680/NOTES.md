# leopold1680: Emperor Leopold I to Charles II of Spain, Prague, 14 April 1680 (catalogue 1599)

**Outcome (4 Nov 2026): not solved; transcribed, one control failed. The cipher system is not established.**

Status: in progress

## Source

Madrid, BNE, RES/261/58, "Carta cifrada del Emperador Leopoldo I a Carlos II de España. Praga, 14 abril 1680".
- BNE Digital viewer: https://bnedigital.bne.es/bd/es/viewer?id=29736cc9-91f0-4f84-b38e-93bb5f93f932 (10 pages,
  CC BY 4.0). Page 5 is the letter, 6 its verso, 7-8 seal and address panels, the rest blank.
- Card: https://bnedigital.bne.es/bd/es/card?id=29736cc9-91f0-4f84-b38e-93bb5f93f932
- Images are kept in `img/` (git-ignored). BNE Digital opened in Chrome without a Cloudflare challenge on 4 Nov 2026;
  a single page is fetched as `/bd/es/pdf?id=<id>&page=5` from inside the viewer session.

## The document

An autograph letter by Leopold I, in Spanish, to the young Charles II, written from Prague (where the court had gone
from the plague in Vienna). Clear opening: "Ser.mo [Rey?] ... He recibido la carta de V. Magd. de 8 de febrero y
holgado de veer en ella"; then about 20 lines of number groups; clear closing: "Guarde Dios a V. Magd. como deseo.
Praga 14 de Abril 1680. Buen tío y hermano de V. Magd. Leopoldo." No interlinear decipherment, no margin gloss, no
key sheet, no claro on any of the 10 pages.

## The cipher

`transcription.txt`: 250 number groups in 20 lines, 86 distinct tokens (85 distinct values) by `_check_profile.py
--measure`. Values run from 10 to 224 and fall in blocks (10-17, 30-67, 72-105, 108-154, then 181, 202, 224 alone);
none in the 20s. The commonest are 39 (13), 50 (11), 62 (9), 123 (9), 30 (8), 114 (8). The pair 62 39 occurs six
times, 59 129 104 twice. IoC 0.0165, 35 values appear once. Leopold writes 1 as `i` in the hundreds (i23 = 123).

Most groups carry a long pen-stroke through them, and a few (224 every time, 154, 150, 143, 139, 202, 72, 48) sit in
gaps of it. Whether the stroke means anything (nulls, a flourish, a word-end mark) is open; it is not transcribed.

Spanish-language cipher letters of this period from the imperial court use numeric ciphers (Auer, Tomokiyo
habsburg.htm), but no table is held, so letter, syllable and nomenclator structure are all still possible.

## Prior art

Nothing found (4 Nov 2026): known.py and the DECODE ledgers; Tomokiyo habsburg.htm (Leopold I used cipher
personally, Auer p. 158; no decipherment of any letter to Charles II); SNAC mirror of the BNE title; web searches in
English, Spanish and German. A Huntington record that surfaced in the vetting search was not opened.

## What was tried

- **Letter-level homophonic annealing** (`solve_homophonic.py`, es-golden-age-nospace order 5): on the letter, six
  restarts give pseudo-Spanish at -488.6. On two controls (own Spanish text, 250 letters, random 81-82-symbol
  homophonic key) the same code gets 4-22% of letters and scores -487 to -540 against a true plaintext at about
  -380, so the search does not reach the answer at this size. The output on the letter is not evidence of anything.

## Remaining gaps

- The whole letter. Blocker: no-key-material (no table for the Leopold-Charles II correspondence is held or online).

## Escalation

- Siblings: none deciphered. RES/261/73 (catalogue 1600) is a different letter in the same BNE series, not yet looked at.
- Known keys: Reichskanzlei numeric ciphers (Grana 1664 and 1668, in Pribram and Landwehr's Leopold-Pötting edition)
  and the Spanish court's general cipher of the 1680s are untested candidates; no table available online.
- Print: Auer's chapter "Die Verwendung von Chiffren in der diplomatischen Korrespondenz des Kaiserhofes im 17. und
  18. Jahrhundert" and the Spain chapter (Navarro Bonilla, Hernández-Castro) in the same volume (Kryptologie im
  frühneuzeitlichen Europa), not seen.
- Archives: OeStA Spanien and AHN Estado for a key or a clear copy of this letter; not searched.
- Structure: a syllabic or nomenclator reading of the value blocks, and the meaning of the stroke, not tried.
- Retry: a stronger solver cannot help a homophonic letter-level reading at 250 groups; a key is needed first.

## Files

`transcription.txt`, `profile.json`, `WORKLOG.md`, `solve_homophonic.py`, `img/` (images, git-ignored).
Catalogue 1599 and the DECODE queue (skip: no record) were updated the same day.

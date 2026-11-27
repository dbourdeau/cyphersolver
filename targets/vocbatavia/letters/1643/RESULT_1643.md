# Batavia letter of 23 Jan 1643 (NA 1.04.02 inv. 1141): number cipher decoded with KEY_v2 (25 Nov 2026 UTC = 26 Nov AEST)

## Bottom line
- Identified: Van Diemen and Council to the Heren XVII, Batavia 23 Jan 1643 (signed 1141_0908), sent by the English ship Ulysses
  (GM II p. 194 heading: KA 1050 unfoliated after fol. 383, copy fol. 384-389) [sourced].
- Unglossed copy 2 (scans 897-908; cipher on 901, 902, 905, 906): KEY_v2 (frozen 1634/1623 key, unchanged) decodes it on the first pass.
- FIGURE OF RECORD: 59/86 number groups covered by dictionary words = 68.60% (>= 65%), under a word-division rule frozen before the decode.
- Key shuffles 0/5,000 at both seeds; matched control (ciphertext shuffled) 0/5,000 at both seeds, rank 1 of 5,001. PASS, modest margin.
- The glossed copy 1 (0886, 0890), opened after the score, agrees with the decode for 10 of 12 checkable runs.
- New: the letter also uses a second, letter-for-letter cipher (Tartarien = mrkmrkcbd, Japan = crfrd ...) and Roman numerals as code words
  (XXI = silver, IV = gold). This is the system of the 1640 'LC' words.

## Freezes and stamps (all UTC 25 Nov 2026)
- Method + scorer: frozen/FREEZE_METHOD_1643.txt 21:09:15; stamps_01_freeze-method (manifest sha256 efd9ba0e...; sectigo and freetsa 21:09:16 GMT; OTS submitted).
- Transcription: frozen/FREEZE_T1643.txt 21:13:20 (T1643 sha256 bca33dfa...); stamps_02_freeze-tx (manifest 83214e7a...; 21:13:20/21 GMT).
- First pass recorded: RESULT_1643_firstpass.md; stamps_03_firstpass (manifest 0cff7623...; 21:14:08 GMT). Glossed copy fetched 21:14:20, after that stamp.

## Figures [measured] (decode_1643_output.txt)
- Groups 86 in 21 runs; keyed 82; coverage 82/86 = 95.35%. Unkeyed: 12 x1, 39 x1, 74 x2 (1 + 1 + 2 = 4).
- Covered by DP words: 59/86 = 68.60%. Per page: 901 49/59 = 83.05%; 902 0/5; 905 10/18 = 55.56%; 906 0/4. Runs fully covered 10/21.
- Key shuffle: seed 20261112 0/5,000 (max 48 = 55.81%, mean 25.56%); seed 7 0/5,000 (max 45 = 52.33%, mean 25.64%).
- Ciphertext shuffle (matched control): seed 20261112 0/5,000 (max 54 = 62.79%, mean 42.02%); seed 7 0/5,000 (max 55 = 63.95%, mean 41.94%).
- Caution: 12 of the 27 uncovered groups are isolated single numbers next to letter-cipher signs; the rule can never score them.

## Post-hoc check against glossed copy 1 (not the figure of record)
| copy 2 run | KEY_v2 decode | copy 1 gloss | agree |
|---|---|---|---|
| 33 9 65 31 17 3 74 2 44 53 22 | d aduis ? n uyt | 'dadvijse[n]' + 'uyt' (copy 1 writes 70 for 74 and a word break after 2) | yes (74 = copy variant of 70 = e) |
| 6 28 47 28 48 | geuen | 'geven' | yes |
| 2 28 6 20 32 11 71 | negotie | 'negotie' (copy 1 seems to write 12 for 2) | yes |
| 52 61 41 4 | rycx | 'rijcx' | yes |
| 20 2 22 3 71 53 32 | ontseyt | 'ontseyt' | yes |
| 69 70 3 | ses | 'ses' | yes |
| 54 11 2 15 22 | winst | gloss partly legible ('...nst') | probably |
| 56 25 48 50 71 2 | tonnen | 'tonnen' | yes |
| 31 25 20 52 | uoor (voor) | 'naer' | NO (gloss paraphrase or cipher variant) |
| 11 9 16 10 2 | iapan | 'Japan' (0890) | yes |
| 2 25 20 72 22 | noort | 'noordt' (0890) | yes |
| 24 39 17 30 16 5 50 20 | w?ippbno | 'eylanden' (0890) | NO: 6 of 8 values disagree with KEY_v2; unexplained |
| 2 12 10 20 24 | n?aow | gloss over the line 'drie tonnen' sits over gkcb; numbers not glossed | unresolved |
Count: agree 10 (incl. 'probably' winst) of 12 checkable; 2 disagree.

## Reading (normalised; KEY_v2 words in [ ], LC words { } with 1643 gloss)
- 901: [d'advisen uyt] {Japan} [geven] ons {groote} {hoope} van {beter} ... ende goede [negotie] met apparentie den {Chinees},
  ende alle andere {natien} (except de V[ereenichde Compagnie]) dat [rijcx] veel moet worden [ontseyt] ... van anno 1642, monterende omtrent
  [ses] {tonnen} ... [suyvere winst] gerendeert 4 3/4 [tonnen] ... desen jaere sullen [voor] {Japan} bestellen ... ruym MC tonnen ...
  sal worden {10 a 12} tonnen (gloss 'tien a 12 tonnen' over 'ml: tot mg': digits by letters).
- 902: ... als yder {drie} tonnen ...; voor anno 1644 eysschen {acht} tonnen.
- 905: Tot ontdeckinge vande Noordt Custe [sic] {Tartarien} ende van daer omme andermael op te soecken de XXI (silver) ende IV (gout) rijcke
  [24 39 17 30 16 5 50 20: gloss 'eylanden'] bij {oosten} {Japan}, sijn geprojecteert de fluyt Castricum ende 't jacht Breskens ...
  schipper Marten Gerritsz Vries; de cours is van hier bij noorden Celebes nae Ternate ende van daer bij oosten [Japan], om de [noort] custe
  van {Tartarien} aen te soecken.
- English (905): "To discover the north coast of Tartary, and from there to search again for the rich silver and gold islands east of Japan,
  the flute Castricum and the yacht Breskens are planned, under skipper Maerten Gerritsz Vries ..." This is the Vries voyage of 1643
  (Yezo, Sakhalin, Kurils); the cipher hid 'Tartary', 'Japan', 'silver', 'gold', 'islands' [derived; history from general knowledge, unverified here].
- 901 (Japan trade): "the advices from Japan give us great hope of better [trade?] ... with prospect of the Chinese and all other nations
  (except the Company) being refused that kingdom ..." [derived; LC words from the gloss].

## Exposure and limits
- Transcriber had KEY_v2 in context; recognised two or three values while viewing; disclosed before the freeze (METHOD_1643.md).
- No second transcription yet (owed). Header of the frozen transcription gives a wrong time range (21:10-21:30); actual about 21:09-21:13.
- GM II heading seen before the decode (only the heading and first line of the summary).
- 7 Mar 1643 letter: not worked; GM II p. 197 n. 6 prints that its italic words are cipher with the meaning beside, so it cannot be blind.

## Verdict
- Blind-ish test of KEY_v2 on a second unseen letter: PASS on the figure of record (68.60%; 0/5,000 in both controls at both seeds), modest margin.
- Same number cipher 1623 -> 1634 -> 1640 -> 1643 [derived]. Lasry category: read after matching with an external key (KEY_v2), checked against
  an existing contemporary decipherment (copy 1 gloss).

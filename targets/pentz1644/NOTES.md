# Christian Pentz, Glückstadt 1644-45: the Pentz-family index cipher with a contemporary decipherment (key v3)

Status: proposed (dudout, prepared 13 Nov 2026, not pushed). Letter of 29 Apr 1644 **read**; letter of 1645 **read in part**.

**Prior art, third party, credited:** Malcolm McBratney, `targets/pentz1636` (PR #522): the Pentz key family (index numbers selecting number alphabets; table 1 a-i = 37..29, k-z = 14..28; table 2; key v2 with index 64/12/10 from the Günther gloss and a partial third table). This folder uses that key unchanged for T1 and T2 and extends it. It is the same key, so the natural home may be `targets/pentz1636` as documents 3-4 and key v3; filed here as a sibling folder so that nothing in pentz1636 is touched. Maintainer's choice.

## Documents (same unit as pentz1636's Glückstadt letter: Rigsarkivet, Tyske Kancelli, SHLK A IV 89, unit 274999)
| | A. Pentz to Christian IV, Glückstadt, 29 Apr 1644 | B. Pentz to the Chancellor, 1645 |
|---|---|---|
| images | 321 (recto, ref 52789089), 322 = 323 (verso, refs 52789090/91) | 425 (ref 52789193) |
| cipher | 11 lines recto (all glossed letter by letter in a contemporary hand), 11 lines verso (only line 1 glossed) | 12 lines; contemporary marginal decipherment of lines 1-9 (another hand); later word glosses on lines 6, 10-12 |
| read share | 27/28 = 96.4% (verso alone 13/14 = 92.9%) | 38/41 = 92.7% (37/41 without the marginal 301) |

## Key v3 (`key.tsv`, `key_history/KEY-v3.json`, frozen 13 Nov 2026 21:36 CET, SHA-256 f5d41697…)
Built only from pentz1636 v1/v2 and the interlinear decipherment of image 321 (+ image 322 line 1); 41 figure-letter pairs in `key_history/GLOSES-1644.tsv`.
- Index: 62, 64 → T1; 13, 11 → T2; 10, 8 → T3 (all gloss-attested here; 63, 12, 9 kept from pentz1636 v2).
- T1, T2: pentz1636 values; every glossed value agrees.
- T3: mirror of T1 (a-i = 29 up to 37, k-z = 28 down to 14), with the glossed exceptions **g = 33, e = 35** (e/g swapped against the mirror; e = 35 agrees with pentz1636 v2) and **r = 39** (21 kept as rule value). Glossed: a29 c31 d32 g33 e35 h36 i37 k28 l27 m26 n25 o24 s20 t19 u18 r39.
- 251: null (twice on the recto, once on the verso, never glossed; it stands inside nich·251·t).
- Codes: 301 = Archbishop (of Bremen) from the marginal decipherment on image 425; 560, 756 open.

## Test (pre-registered, `scripts/PREREG-2.md`, frozen with `scripts/measure2.py` 21:35 CET before the key and the held-out)
Held-out: image 322 lines 2-11 (unglossed) + image 425 whole cipher block: 286 figures, two transcription passes (B on re-made crops without looking at A), identical; 4 doubtful figures marked. Frozen 21:41 CET (`controls/HASHES-HELDOUT.sha256`).
One run, `controls/MESURE-2.txt`: 255 letter figures, 254 resolved (99.6%); German 4-gram per character: true −2.338, 200 within-table permutations mean −4.046 (best −3.719), real German −1.797. **N = 0.760** (bar 0.75) and best control 0.145 (bar +0.30): **PASS**. The bar was met narrowly; the reading, not the score, carries the text.
Timestamps are local file times and SHA-256 files only (no RFC 3161 stamp).

## Reading
`readings/`, `translations/`. A: Pentz cannot harass the Swedes as before because the garrison was taken away to Dithmarschen; at times only four men hold the ravelin before the Krempe gate. B: with the Archbishop's consent Pentz sent a strong party against Wrangel's quarters; the men can move hidden through the wood by a separate road to Rendsburg (Torstensson war, 1644-45).

## Gaps
- Codes 560, 756 (image 425): no gloss. open-codes.
- Image 425 ‹29 33 28 20› (T1 i e z q): unresolved; perhaps a misread 23 (ietzt).
- {Revellin} on image 322: second figure transcribed 39 twice, probably 35.
- Other cipher letters in the same unit, 1644-45, not transcribed: images 402-405, 408, 411, 412, 420 (several pages each). The key should read them; not attempted here.
- prior solution: not searched beyond pentz1636's checks (Fridericia, Bricka-Fridericia); the 1644-45 letters may be printed in summary in Danish war histories.

## Addendum (prepared 13 Nov 2026, not pushed): the other 1645 cipher letters, key v3 applied unchanged

Five more letters of Christian Pentz from the same unit 274999 were transcribed and decoded with key v3 **as frozen** (SHA-256 f5d41697…, no value changed, no new test: key v3 was measured on PREREG-2, N 0.760). Files: `transcriptions/suite/` (pass A per page, `DIFF-AB.tsv`, arbitrated `TRANSCRIPTION-SUITE.json`), `scripts/decode_suite.py`, `decryptions/`, `readings/`, `translations/`.

| letter | images | cipher words | sure + probable | state |
|---|---|---|---|---|
| to the Chancellor, Glückstadt 31 Mar 1645 | 402-403 | 72 | 61 + 5 = 91.7% | read in part |
| to the Chancellor, Glückstadt 8 Apr 1645 | 404-405 | 52 | 42 + 3 = 86.5% | read in part |
| to the Chancellor, Glückstadt 20 Apr 1645 | 408-409 | 16 | 16 + 0 = 100% | read |
| to Christian IV, Glückstadt 20 Apr 1645 | 411-412 | 108 | 95 + 6 = 93.5% | read in part |
| to the Chancellor, 1645 (pencil 4/5, after 24 Apr) | 420 | 36 | 28 + 3 = 86.1% (second reader, 14 Nov) | read in part |

Per document, never pooled. Context: Torstensson's war, spring 1645; Glückstadt damaged by the March assault (the "Reithofel/Reithoffel" work, the new castle, the rampart, the old town gate); Pentz asks for money and orders for repairs, mentions the Spanish loan and a paymaster, and in late April Rendsburg "in the greatest danger".

- Transcription: two passes by the same model reader (B on re-made, differently processed crops, without reopening A); 14 differences, arbitrated on the image (`DIFF-AB.tsv`). Weaker than the held-out protocol: not frozen before decoding (the key was already measured; this is an application).
- New values: none counted as sure. Probable from context only: 252 = "im", 434 = "dass". Open codes: 1009, 306 (×2), 470, 311, 1000 (×2, images 404 and 411), 269, 305, 81, 393, 1011, 753, 1400, 101; 560 now twice (images 411 and 425), still open. No PREREG-3 was run (nothing to validate beyond these two probable values).
- Later word glosses (another hand) stand over many cipher words on images 402-420; they skip the codes. Only one was used: "Mayen" on image 404 for a word with one misread figure. They are not letter-by-letter and were not used for the key.
- Prior printing: not searched beyond pentz1636's checks (Bricka and Fridericia print the King's letters, not Pentz's). Kong Christian IV's egenhændige Breve VI (1644-48) not checked for these dates.

# Champagne 1590: nos. 24 and 60 read, key no. 25 checked, a second reading of no. 25

Contributed by Andrew Beling, with AI agents, 11 November 2026.
This folder adds to `targets/champagne1590/`. It changes nothing in Daniel Bourdeau's files or in Michael Brackx's
`brackx2026/` and `texts/`. The edits that go with it are in the same pull request: a dated section in `../NOTES.md`,
three gap lines there brought up to date, and in `../profile.json` four solution steps, the same gap changes and a
verification credit. The class and the read shares are not changed (nothing was measured), and `docs/` is not touched.

[V] = checked on the image or in output. [I] = inference.

## 1. What is here

| File | What it is |
|---|---|
| `PREREG.md` | the test of key no. 25 on no. 24's glosses, written before any transcription or script |
| `key/key25.md` | `../texts/key25.md` copied unchanged (sha256 `a88a36ac…`, the same as the repo file) |
| `transcription/n24_figures.tsv`, `n24_glosses.tsv` | the glossed figures of no. 24 and the letters written over them, in separate files |
| `transcription/n24_n60_runs.tsv` | every cipher run of nos. 24 and 60 as seen (barred 9 written `9b`) |
| `transcription/key25_noms_propres.tsv` | the key sheet's names 1-51 (52-55 numbered, blank) |
| `transcription/key25_noms_generaux.tsv` | the Roman-numeral word list |
| `transcription/key25_villes.tsv` | cities 58-89 and provinces a-z |
| `transcription/n25_second_reading.md` | a second, independent transcription of no. 25 (hashed before Brackx's was opened) |
| `results/check_n24_result.json`, `check_n24_output.txt` | the test result, figure by figure |
| `results/runs_mechanical.txt` | the runs of nos. 24 and 60 decrypted with key no. 25, nothing edited |
| `results/n24_reading.md` | no. 24 (50 lines) and no. 60 (5 lines): clear text and runs, with an English gist |
| `results/n25_compare.md` | the second reading of no. 25 against Brackx's, word by word |
| `results/frozen_inputs.sha256` | hashes of the files frozen before the test and before the comparison |
| `scripts/key25.py`, `check_n24.py`, `decrypt_runs.py` | the key parser, the test, the mechanical decryption |
| `names_check.md` | the search for "Ludouic" and "Launay" (not identified) |
| `images.txt` | the Gallica IIIF regions used; no images are committed |
| `CHECKS.txt` | checker output and script runs |

Scripts run from this folder with `python3 -I scripts/<name>.py`.

## 2. A held-out check of key no. 25 [V]

Both cipher runs of no. 24 (f. 37r, NOTES l. 8 and l. 22) carry small letters written over the figures by the decipherer
of the time. NOTES lists glosses only on nos. 25 and 60, so these had not been used. `PREREG.md` fixed the method
before any file existed: key no. 25 unchanged; figures and glosses transcribed into separate files and hashed; one run;
pass at 0.85 or more and a margin of 0.30 or more over the best of 200 shuffled keys (seed 1590).

Result: **13 of 14 glossed figures agree (0.929); shuffled keys mean 0.053, best 0.357; margin 0.571. Pass.** The one
miss is a "y" over the null 99 or the barred 9 (Roy), which the key cannot give as a letter. The sample is small. The
gloss over 05 was not legible and was left out, as the pre-registration says.

## 3. The key sheet (fr. 3995 f. 51r) [V]

- Names 1-51: this confirms the six in `../texts/key25.md` (9 Roy, 17 Soissons, 22 Guise, 39 La Noue, 44 La Chastre,
  51 La Guiche) and adds the other 45 (e.g. 19 duc de Nevers, 24 Mayenne, 42 Givry, 45 Balagny, 48 St Pol, 50 Revol).
- Words: Roman numerals x to lvii. Cities: lviii Paris to lxxix Lyon, then 80-89 written "iiij^xx" plus units (Dijon 80 ...
  Laon 89). Provinces: letters, a Champagne to z Angleterre. The "Mots" and "Dames" blocks are not transcribed.

## 4. No. 24 (f. 37r, 15 June 1590) and no. 60 (f. 88r)

- No. 24 is transcribed in full, about 15 words doubtful (`results/n24_reading.md`). It is a newsletter from the royal
  camp before Paris, 11-15 June 1590 [I for the gist].
- Runs [V]: "du faict de Ludouic" (NOTES l. 8; the fifth figure looks like 36 on the image, read 56 as Brackx did,
  which fits no. 60's glossed "Ludouic"); "le Roy lu[y] au[o]it refuzé ceste commission comme onereuse" (NOTES l. 22).
- Corrections to `ct_3623_twodigit.txt` / NOTES [V]: l. 22 "99 95 93 35" is **99 9̄ 56 93 35** (a barred 9, Roy, then 56).
  22, 44, 51 are barred: Guise, La Chastre, La Guiche. **84 is not barred**; it is plain s.
- "Les xlm 84 qui y sont" (NOTES l. 11): "xlm" is x, l and three minims, **xliij = 43 "Intelligence"**, with 84 = s:
  "Les intelligences qui y sont, qu'on dict s'accroistre de jour a autre" [V shape, I reading].
- No. 60: all five lines read, two words doubtful. Over the last figure of the second run (64) the decipherer wrote a dotted
  y: **"Launay"**, where the key gives n [V].

## 5. No. 25: a second reader

`transcription/n25_second_reading.md` was transcribed from the images and hashed before Brackx's transcription was
opened. Not fully blind: the reader had seen NOTES and its table of runs. Comparison in `results/n25_compare.md`.

- Brackx's 37 doubtful words: 14 agree, 13 get another reading with fair confidence, 10 stay doubtful for both.
- About 18 other words differ; in 7 of them the second reader now accepts Brackx's reading.
- Cipher runs: 5 of 6 agree. **The Soissons run (l. 34) seems to end 38 93 9̄, "du [Roy]"**, not barred 39 "du M. de La
  Noue": five digits after 43, the bar over the last 9 only. A third look is needed.
- "l'union": the page has **58**; the sheet gives l as 56 only, so 58→56 corrects the encipherer, not the reading [V].
- The isolated 3 in the Soissons run is on the page, with nothing written over it [V].

Two readers who disagree in about 30 places, mostly small, are not enough for the 95% bar: no. 25 stays read in part.

## 6. Open

- A third look at the l. 34 run of no. 25 and its l. 41-42 sentence; the ten words both readers mark.
- Who Ludouic and Launay were (`names_check.md`).
- The "Mots" and "Dames" blocks of the key sheet.

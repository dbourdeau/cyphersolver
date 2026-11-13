# Magdeburg envoys at Osnabrück, 1646-47: bare cipher slips in LASA A 1 Nr. 530, key recovered from the ciphertext (catalogue row 1639)

Bottom line: the cipher is broken. We recovered the key from the ciphertext alone, and four independent checks confirm it, including the clear drafts in the sister volume Nr. 529. The slips are read only in part: every bare slip is below our own 65% line (strict 34.57% to 47.06% on the first pass). The limit is our reading of the hand, not the key. The content of f.5, f.6, f.7 and f.101 exists in clear in Nr. 529, so it is not first.

## What this folder is

Landesarchiv Sachsen-Anhalt (Magdeburg), A 1 Erzstift Magdeburg, Auswärtige Angelegenheiten, **Nr. 530**: papers of the archbishopric's envoys at the Osnabrück congress, 307 frames. The images come from the Landesarchiv viewer (`https://recherche.landesarchiv.sachsen-anhalt.de/images//A_1/Nr_530/max/A_1__Nr_530__NNNN.jpg`). The folder holds:

| slip | frame | heading on the slip | role here |
|---|---|---|---|
| f.5 | 8 | 1647 ad Diarium No. 31 | key training text |
| f.6 | 10 right | 1647 ad Diarium No. 32 | held out from KEY_v1, then key training text for KEY_v2 |
| f.7 | 11 left | (1647) | held out from KEY_v2 |
| f.101 | 117 | ad Diarium No. 54 | held out |
| f.102 | 118 | ad Appendicem Diarii No. 22 | held out |
| f.104 | 121 | ad Diarium No. 22 | held out |
| f.204 | 233 | Annotata ad No. 40 | held out |

Plus three pieces of key material in the same file (`gloss/`): the Catalogus of name signs (frame 3), the glossed postscript (frame 51) and the key worksheet (frame 168).

## The system

A reciprocal letter substitution in Latin letters: 12 pairs, each letter enciphering to its partner. German and Latin plaintext. Names and titles are written with separate signs (the Catalogus), shown as `|` in the transcriptions. Word division is kept. The frame-168 worksheet writes the key as the keyword AMPHICTYONES over "zxwurqlkgfdb".

## The key and how it was obtained (`gloss/`, `key.tsv`)

- **KEY_v1** (frozen 12 Nov 2026 13:45:23 UTC, md5 c892c744): built by simulated annealing on f.5 alone. Seeds 3, 4 and 5 gave the same key.
- **KEY_v2** (frozen 13:47:27 UTC, md5 c8fade56): the same annealer on f.5 + f.6. It converged to an exact reciprocal table: (a z)(b s)(c q)(d e)(f n)(g o)(h u)(i r)(k y)(l t)(m x)(p w).
  - No value in it comes from context or from a gloss, and nothing was edited by hand.
  - One value is held out of the frozen file: j, which occurs once in f.6, had the annealer value x.
  - m (= x by the involution) does not occur in the training text, so m decodes as `?`.
  - b189 reran the annealer on 13 Nov: byte-identical output.
- `key.tsv` gives each value with its evidence: the annealer, the worksheet, the gloss words and the training counts.

**Confirmations** (`controls/confirmations.txt`, `scripts/confirm.py`, all run after the freeze):

1. **Catalogus, frame 3:** 8 of 13 name words exact with the frozen file. 9 of 13 if m = x is added from the involution. The other four differ by one or two letters ("resiednt" for "resident"). Our session log of 12 Nov said 13/13. That figure does not reproduce; 8/13 is the one we use.
2. **Postscript glosses, frame 51:** 11 of 18 glossed words exact. Counting letters position by position from the start of each word, 104 of 118 agree = 88.14%; allowing one shift, 111 of 118 = 94.07%. Both figures reproduce. The misses are our reading slips (g/q, t/l) and the unkeyed m.
3. **Key worksheet, frame 168:** 12 of 12 pairs equal the KEY_v2 involution in both directions. 23 of the 24 directed values are in the frozen file; the 24th is m = x.
4. **Clear drafts in Nr. 529** (13 Nov, `nr529/`): we enciphered our reading of the underlined clear text with KEY_v2 and compared it with our frozen transcriptions.
   - f.5: 248 of 271 letters agree = 91.51%.
   - f.6: 364 of 419 letters agree = 86.87%.
   - With 1,000 random reciprocal keys at each of two seeds, none comes near (best 114/271 and 186/419).
   - Credit for the lead: Malcolm McBratney's second checker (Perplexity). We verified it ourselves.

## Counting rule and counts of record (`counts.txt`, `scripts/build.py`)

- **Unit:** a cipher word.
- **Rule:** S if the decoded string is a German or Latin word as it stands (period spellings allowed), E otherwise. Strict share = S/(S+E+N); N = 0, because no code groups occur.
- **Labels:** the labels are the readers' own one-pass ledgers, written on 12 Nov after freezing. `build.py` matches them word by word to the decodes and recounts.
- **Holes:** nothing is emended. Under Dan Bourdeau's rule ('?' units are holes) every figure is unchanged, because no unit holding '?' was labelled S.

**First pass with the frozen KEY_v2, the figure of record, per slip:**

| slip | reader of record | strict |
|---|---|---|
| f.7 | R1 (b160) | 36/83 = 43.37% |
| f.101 | R2 (b162; R1 did not transcribe it) | 16/35 = 45.71% |
| f.102 | R1 | 28/81 = 34.57% |
| f.104 | R1 | 45/101 = 44.55% |
| f.204 | R1 | 24/51 = 47.06% |

**Second reader** (b162, glossed reference crops, frozen before its own single decode): f.7 38/81 = 46.91%; f.102 31/79 = 39.24%; f.104 46/101 = 45.54%; f.204 22/51 = 43.14%.

**Training text, not counted:** f.6 with KEY_v1 (held out from v1) scored 35/101 = 34.65%.

No pooled figure is given as a headline.

**Figures that do not reproduce** (we use the reproduced value):
- f.104 R2: the b162 ledger states 47/101, but its line 7 says 7 and lists 6 S words; recounted, 46/101 = 45.54%.
- f.204 R1: the b160 ledger states 24/53, but the frozen file holds 51 cipher words (its line 2 says 10, the file has 8); recounted, 24/51 = 47.06%.
- Catalogus: 8/13 (9/13 with m = x), not the 13/13 in our session log.

**Blind second reading:** none. Reader 2 (b162) did not see reader 1's transcriptions before freezing its own. It did know the key and the decodes of f.5 and f.6, so it is a second reader, not blind. Reader 1 is one reader, not blind: it had seen key output on f.5 and f.6. Word agreement between the readers (`agreement.txt`, `scripts/align.py`) is 162 of 312 R2 words = 51.92% over four slips: f.7 39/81, f.104 58/101, f.102 43/79, f.204 22/51. The systematic disagreements are g/q, c/e, t/l and a word-final f read as n.

## Controls (`controls/`)

- **Shuffled-key control** (`scripts/shuffle_control.py`): 5,000 keys at each of seeds 20261112 and 7, German 4-gram model on Simplicissimus, with a corpus header guard. The true key beats every shuffled key: 0 of 5,000 in all 18 runs (9 transcriptions x 2 seeds). Outputs are in `controls/shuffle/`.
- **Word-layer control:** not applicable. The readings do not rest on code words; name signs are left as holes.

## What the slips say (`readings/`, `translations/`)

German with Latin phrases, reports from the envoys at Osnabrück in 1647. Holes fall in almost every line, so these are lists of readable words, not prose. The English is MADE BY AN AI MODEL and marked so in each file.
- f.7: on the obstinacy of a legation, "praesertim in pari autoritate constituti".
- f.104: "post repulsam", a Münster burgher.
- f.102: "spiritu vertiginis", Groß-Glogau, Bremen.
- f.204: "uertrawen et pro certo berichten".
- f.101: Salvius kept at Münster, "als der Venetianische hierunter".

## What is not claimed

- No slip reaches our own 65% line or Dan's 95% read bar.
- The content of f.5, f.6, f.7 and f.101 is not first: it is in clear in Nr. 529 (`PRIOR_ART.md`).
- The contemporaries had this key (frame 168). A contemporary decipherment of f.102, f.104 and f.204 may survive.
- Our reading of the Nr. 529 drafts is one reader's and not blind.

## Remaining gaps

- **The hand.** g/q, c/e, t/l and final f/n confusions cap the readings. A third reader, or a person, reading against the Nr. 529 drafts would lift f.5, f.6, f.7 and f.101 at once, but those are not first.
- **Nr. 529 for f.102, f.104 and f.204** was searched only in the frames listed in `nr529/README.md`. Nr. 543 (Krull's draft reports) is not checked.

## How to reproduce (standard-library Python, no network)

Run from this folder. `python3 -I scripts/build.py` writes the decryptions, units and counts.txt. Then:
- `python3 -I scripts/confirm.py > controls/confirmations.txt`
- `python3 -I scripts/align.py f7_frame11 f104_frame121 f102_frame118 f204_frame233 > agreement.txt`
- `python3 -I scripts/readings.py`
- `python3 -I scripts/keytable.py`
- `python3 -I scripts/compare_nr529.py > nr529/COMPARISON.txt`

The shuffle control needs the Simplicissimus text (Project Gutenberg 55171) as its first argument. `scripts/original/` keeps the session scripts of 12 Nov as they ran. b189 reran everything on a scratch copy of this folder, and it came out identical file for file.

## Timestamps

See `timestamps/README.md`. The frozen key existed unchanged by 13 Nov 2026 09:08:54 GMT (Sectigo RFC 3161). The freeze order of the transcriptions rests on the session logs (`transcriptions/FREEZE_LOG.txt`).

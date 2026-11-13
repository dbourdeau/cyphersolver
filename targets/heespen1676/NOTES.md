# The Heespen/Baudissin code: Danish commissioners at Bremen, 1675-76 (Rigsarkivet unit 262098)

Status: key rebuilt from contemporary glosses; the one bare passage read in part, far below our own 65% line.
Text state of 537L: **decoded, not read** (only short function words are read: 9/60 = 15.0%). Entry class: read in part.
New entry: no catalogue row, lead or target covers RA 262098 or this code (row 602, the Oldenburg parallel relations, is
related but not digitised). No claim of a first reading (see PRIOR_ART.md).

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic).

## What the documents are

Copenhagen, Rigsarkivet, Department of Foreign Affairs, unit 262098: relations and enclosures of the Danish commissioners at
Bremen, Generalmajor Gustav Adolf Baudissin (governor of Oldenburg and Delmenhorst) and Wilhelm (von) Heespen, 1675 to
May 1676 (end card on image 643: "1675 - maj 1676"). Images by the Rigsarkivet API (`api.rigsarkivet.dk/ao/v1/images/<id>`).
Many relations carry passages in a German syllabic nomenclator, almost all deciphered between the lines by the chancery
in Copenhagen. One passage has no gloss: image 537, left page, Heespen's relation dated Bremen 17 April 1676.

Image id correction: image 537 is id **49059236** (Rigsarkivet API list). The header line of the frozen transcription, and
b179's PARKED.tsv, give 49059234 (worked out by a formula that breaks after image 96). The transcription is frozen and is
not edited; this note is the correction.

## The system

German syllabic nomenclator. One- and two-digit numbers and about 20 drawn signs stand for letters and syllables
(6 = n, 401 = de, 477 = ge, 709 = vö); three-digit numbers stand for syllables or whole words (336 = Allijrten,
97 = Stade, 100 = Carlstatt, 218 = Grafschafften, 253 = Coppenhagen). No word division. Sign labels used in our files
(t, ϙ, ϯ, α, Γ, T, Π, ...) are names for drawn glyphs, defined in the transcription header.

## Keys (both from the glosses only)

| key | run | frozen (UTC) | md5 | source images (unit 262098) | codes | attestations | conflicts |
|---|---|---|---|---|---|---|---|
| KEY_HB_v1 | b179 | 12 Nov 2026 17:59:12 | 5dad6d11 | 96, 117, 118 | 95 valued | 232 | 30 i/ei, 400 dar/da (tie, first seen kept), # n/sten |
| KEY_HB_v2 | b180 | 12 Nov 2026 18:47:22 | 374a472c | v1 images + 240 L/R, 241 L, 320 L | 121: 119 valued, 2 ties unvalued (9 r/t, 402 de/di) | 359 | 30 i 11/12, 400 da 2/3, # n 8/9 |

Rule: each code takes the value most often written over it by the glossator. v1 kept the first-seen value on a tie;
v2 leaves a tie unvalued. Both rebuild byte for byte from the gloss-pair files with `scripts/buildkey.py`.
`key.tsv` gives both values for every code with its provenance (image, side, line of each gloss). Every value is from a
gloss; none is from context and none is built from ciphertext. Every attestation, conflicts included:
`gloss/attestations_by_code.tsv` (359 rows; 7 do not match the v2 value: 3 conflicts and 4 tie rows).

Gloss pairs are our transcription of cipher groups and the words written over them; segmentation into code values is
ours, only where the letters align unambiguously. One reader, not blind.

## Figures, per document

### Held-out glossed pages (key tests)

Neither page was used to build the key it tests. Script: `scripts/heldout.py`; output `controls/heldout.txt`.

| page | key | tokens | valued | filed rule | allowances counted against | Dan's rule (unvalued = holes) | mechanical rule |
|---|---|---|---|---|---|---|---|
| 342R (5 glossed groups; tx md5 bec93dca) | v1 | 32 | 28 | 28/28 = 100.00% | 26/28 = 92.86% | 28/32 = 87.50% | 24/28 = 85.71% |
| 413 (18 glossed groups; tx md5 57b2af17) | v2 | 50 | 42 | 40/42 = 95.24% | 39/42 = 92.86% | 40/50 = 80.00% | 36/42 = 85.71% |

Working: 342R valued 4 + 4 + 8 + 8 + 4 = 28; 413 valued 2 + 3 + 1 + 2 + 3 + 2 + 1 + 4 + 2 + 1 + 2 + 4 + 2 + 1 + 1 + 3 + 3 + 5 = 42.

- 342R was filed in our log as **29 valued tokens, 0 contradictions**. That does not reproduce: the script finds **28**.
  b179 counted the n at the start of line 5 (token 6) in both "willigen" and "werden". We use 28.
- Allowances (spelling, listed in `heldout/judgements.tsv`): 342R t in "ansehntlich", + = ck for ch; 413 464 = führ for "für".
  The filed 413 figure 40/42 counts führ/für as agreement; 39/42 counts it against.
- Mechanical rule (added in this folder, stricter): the decoded values must spell the folded gloss exactly. It frees
  4 tokens on 342R (347, +, 558, 27) and 6 on 413 (711, #, 671, #, 464, 593).
- 342R first run dropped line 3 (decoder bug: a line starting with the token '#' read as a comment); fixed and re-run with
  key and transcription unchanged. Both outputs are in `heldout/`.

### The bare passage, 537L (Heespen, Bremen 17 Apr 1676)

| item | value |
|---|---|
| transcription | `transcriptions/heespen_1676-04-17_537L.txt`, md5 a9c2ae41, frozen 12 Nov 2026 18:05:46 UTC (b179); 12 lines + 1 marginal line, 158 tokens |
| second transcription | none. **One reader, not blind.** |
| key | KEY_HB_v1, frozen 17:59:12 UTC, before the page was seen (first seen 18:04:59) |
| decode | once, 18:05:51 UTC: `decryptions/heespen_1676-04-17_537L_v1_once.txt` |
| tokens | v1 valued 106 + unvalued 52 = 158 |
| units | 60 word units (segmentation by the judge, b179): S 9 + N 13 + E 38 = 60 |
| **figure of record** | **strict 9/60 = 15.0%** |
| Dan's rule | no '?' tokens; unvalued signs are named and every unit holding one is E, so the same 9/60 = 15.0% |
| emendations | none |
| shuffle control (key v1) | 0 of 5,000 at seed 20261112 (true -4.4246, best -4.6888, median -5.8100); 0 of 5,000 at seed 7 (best -4.5144, median -5.8166) |

S units: 2 der, 17 an, 21 den, 34 der, 38 der, 45 als, 48 an, 50 mit, 51 dem.
Ledger check (`counts_raw.txt`, `scripts/count.py`): five judging slips in the decoded column of the ledger (units 4, 28,
35, 52 show a hole where the decoder gave the letter t or p; unit 52 judged E though every sign has a v1 value). Applying the
E rule mechanically gives S 9 + N 14 + E 37 = 60. Strict stays 9/60 = 15.0%. The ledger is kept as judged.

### The same passage with key v2: NON-BLIND

b179 had seen 537L before b180 built v2, so this is not a test and does not count. v2 valued 122 + unvalued 36 = 158.
Strict 11/60 = 18.3% (S 11 + N 18 + E 31 = 60). Lenient, reading 709 as vo (gloss 240R6 "vor"): S 15 + N 14 + E 31 = 60,
15/60 = 25.0%. Shuffle (v2): 0 of 5,000 at both seeds (true -4.7075; best -4.9084 at 20261112, -4.9193 at 7).

## Controls

- **Shuffled-key control** (`scripts/shuffle_control.py`, `controls/shuffle_537L_v1.txt`): German character 4-gram model
  from Grimmelshausen's Simplicissimus (`controls/CORPUS.txt`; md5 and 'Language: German' asserted). The decoded values are
  permuted among the distinct valued cipher types of the passage; text between unvalued tokens is scored as separate runs.
  It shows the key's values read more like German than the same values on the wrong signs. It does not show that any
  word is right. `controls/shuffle_537L_v1_as_run_b179.txt` is b179's own run; byte for byte the same.
- **Word-layer control** (`scripts/word_control.py`, `controls/word_layer.txt`), because this is a nomenclator: word codes
  are codes a gloss writes a whole word over (v1 23, v2 28). In 537L the v1 decode rests on one word code only
  (330 = als, glossed twice: 117L3 "als", 118L2 "alßdann"); the v2 decode adds 743 = wie (one gloss, 240L2). On the
  held-out pages, 9 glossed groups open with a word code; 8 of 9 agree (413 711 = über against "übrigen" does not).
  Permuting values over the key's own word inventory: 0 of 5,000 reach 8 at seed 20261112 (best 5, mean 0.318) and
  0 of 5,000 at seed 7 (best 4, mean 0.309).

## Screening for more bare text

2,919 images screened: b179 628 (262098: 390; 262100: 238 sampled) and b180 2,291 (262100 non-sample 476; 262102
images 61-1005, 945; 262105, 509; 262107, 361). Sums in `screening/SCREENED_b179.tsv` and `screening/SCREENED_b180.tsv`.
No other bare passage in this code. b180 viewed most images at about 333 px, so detection there is weaker.

## Reproduction

Every figure above is printed by a script in `scripts/` from the files in this folder (standard-library Python, run with
`python3 -I`). This folder's run (b191, 13 Nov 2026) re-ran all of them: decodes, keys, counts, held-out checks, both
shuffles and the word-layer control are byte-identical to the stored outputs. The one figure that does not reproduce is
the 342R count of 29 (above).

## Timestamps

`timestamps/20261113T090853Z_fable_reply_ourkeys/`: RFC 3161 token (Sectigo), granted 13 Nov 2026 09:08:54 GMT, over a
manifest whose sha256 (650a82c9...) the token's imprint matches. The manifest lists KEY_HB_v2 (sha256 7f03d0a4...), the same
bytes as `gloss/KEY_HB_v2.tsv`. No server stamp covers KEY_HB_v1, the 537L transcription or its decode; their times are
our own log times only.

## Files

- `transcriptions/`: 537L, frozen.
- `decryptions/`: 537L once with v1 (record) and with v2 (NON-BLIND).
- `units/`: per-unit ledgers (v1 record; v2 non-blind) and the v2 judging note.
- `readings/`: German reading with holes, and an English version (AI-made).
- `key.tsv`, `gloss/`: keys v1 and v2, gloss pairs, attestations by code.
- `heldout/`: 342R and 413 transcriptions with glosses, decodes, judgement list.
- `controls/`, `counts_raw.txt`, `holes.md`, `screening/`, `scripts/`, `timestamps/`, `PRIOR_ART.md`, `MANIFEST.sha256`.

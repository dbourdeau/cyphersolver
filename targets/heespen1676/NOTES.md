# The Heespen/Baudissin code: Danish commissioners at Bremen, 1675-76 (Rigsarkivet unit 262098)

Status: in progress (integration check of 13 Nov 2026, PR #523: the gaps below are workable, chiefly the glossed pages of
unit 262098 not yet transcribed into the key; folder only, no page and no ledger row). Contributor's status: key rebuilt from
contemporary glosses; the one bare passage read in part, far below our own 65% line.
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

## Remaining gaps

- Key too small for 537L: 52 of 158 tokens have no v1 value (36 under v2) - blocker: not-attempted; most glossed pages of unit 262098 (336, 340, 342, 389, 391, 401, 411, 455, 481, 526 and others) were not transcribed into gloss pairs, the key rests on images 96, 117, 118 (v1) plus 240, 241, 320 (v2). Transcribing them is the way to a bigger key. Workable, so the target stays in progress.
- 537L has no blind second transcription - blocker: not-attempted; one reader, not blind. The integration check compared all 145 tokens of the 12 main lines with the image (below), so the transcription itself is sound.
- No fresh bare text to test a bigger key on - blocker: no-key-material; 2,919 images screened in units 262098-262107, no other bare passage in this code; a bigger key can be tested only on further held-out glossed pages.
- Oldenburg, NLA Best. 20-44 Nr. 8 (catalogue 602; parallel Klingenberg/Heespen relations with cipher) - blocker: needs-physical-access; not digitised, not seen.
- Prior art not reached - blocker: not-attempted; HathiTrust and Google Books full text, the rest of Vejledende Arkivregistraturer XVI, Rigsarkivet's own key collections (a contemporary key may survive), the literature on the Bremen talks of 1675-76.

## Escalation

- [x] siblings: glossed relations in the same unit used as the key source (six images); the other glossed pages listed above
  not yet used (open)
- [ ] clear-pages: no clear copy of the 17 Apr 1676 passage looked for in the Copenhagen answer drafts or the Oldenburg file
- [ ] known-keys: Rigsarkivet key collections not searched; checked here that the code is not klingenberg1675's (syllable
  table 432-525; 477 = le, 457 = ge there against 477 = ge here), nor biermann1675 K55, petkum1665 (French syllabary) or
  sehested1657 (no Heespen, Baudissin or 262098 in any of their files)
- [ ] print: Aarsberetninger VI and Danske Magazin only
- [x] key-rebuild: v1 and v2 from the glosses, frozen, held-out tests on 342R and 413; a v3 from the untranscribed glossed
  pages is the next step (open)
- [ ] retry: 537L to be decoded again with the bigger key (non-blind, since 537L has been seen; say so)

## Integration check (13 Nov 2026, PR #523)

Done by the integrating session after its own verification (report R8_bremen). The folder is merged as it came, with
`Status: in progress` and no page, ledger row or catalogue change. This is a new entry: no catalogue row or lead covers
RA 262098; it is not added to `catalogue.json` (a worked target, not a lead).

- **Reproduction** (scripts read first, run with `python3 -I` on a scratch copy): both decodes, both key rebuilds
  (`buildkey.py` v1 95 codes / 232 attestations, v2 121 codes / 119 valued / 359 attestations), `heldout.py`, `count.py` and
  `word_control.py` (both seeds) are byte-identical to the stored outputs. The shuffle control needs Project Gutenberg 55171
  (`controls/CORPUS.txt` is only a pointer); downloaded fresh, md5 f476bb74 as asserted, it reproduces seed 20261112 exactly
  (true -4.4246, best -4.6888, 0 of 5,000). md5s of KEY_HB_v1 (5dad6d11), KEY_HB_v2 (374a472c), the 537L transcription
  (a9c2ae41), 342R (bec93dca) and 413 (57b2af17) match.
- **Own decoder** written from `key.tsv` (not importing theirs): 537L gives the same letters line for line under v1 and v2
  (valued 106/158 and 122/158).
- **Held out**: the gloss-pair files hold only images 96, 117, 118 (v1) and those plus 240, 241, 320 (v2); 342 and 413 are
  absent, so both pages are held out from the key they test. The RFC 3161 tokens (Sectigo, 13 Nov 09:08:54 and 09:37:57 GMT)
  match their manifests (imprints 650a82c9..., 6e41ed1b...) and all 47 files of the PR-folder manifest still hash the same;
  they postdate the work, so the order of events (v1 frozen before 537L was seen) is by the contributor's record.
- **Strictest held-out figure**: counting unvalued tokens as holes *and* the mechanical rule (the decode must spell the
  gloss) together gives 342R 24/32 = 75.0% and 413 36/50 = 72.0%. The contributor's figures (filed 28/28 and 40/42;
  unvalued as holes 28/32 and 40/50; mechanical 24/28 and 36/42) all reproduce.
- **Images** (Rigsarkivet API, plain curl, HTTP 200): id 49059236 is image 537, Heespen's relation with the bare block on the
  left page and clear text around it ("Ob und wie weit ... mit Ew. Königl. Mayt. allergnädigsten absehen und interesse
  übereinkompt"); the correction of the id (49059234 in the frozen header) is right. All 145 tokens of the 12 main cipher
  lines agree with the transcription (the doubtful 30/130 on line 1 noted as such by the contributor). Image 413 (id 49059110):
  all 18 glossed groups and their glosses agree with `heldout/413_transcription_glosses.tsv` (den, übrigen, allijrten, das,
  nachsehen, Cassen, Stade, außgehen, der, Feind, den, setzen, das gantze, also, auch, fürter, unter, alleiniger), which
  checks key values 401 de, # n, 336 allijrten, 400 da, 330 als, 332 auch, 457 feind, 97 stade on the image.
- **Reading**: 537L is decoded, not read (9/60 = 15.0%, function words only); `_check_reading.py` agrees ("decoded, not
  read"). Entry class read in part; method key recovered from adjacent plaintext (same unit's glosses), as petkum1665.
- **One key, one entry**: no other target uses this code (checked against klingenberg1675, biermann1675, petkum1665,
  sehested1657).
- **Correction**: the first gap in `profile.json` was marked `no-key-material`, but its own detail says the glossed pages
  were not transcribed: changed to `not-attempted`. `outcome.codes_open` filled (key v1, 537L: 30 of 70 distinct signs, 52 of 158 tokens without a value; `holes.md` section 2).

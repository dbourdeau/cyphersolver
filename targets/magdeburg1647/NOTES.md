# Magdeburg envoys at Osnabrück, 1646-47: bare cipher slips in LASA A 1 Nr. 530, key recovered from the ciphertext (catalogue row 1639)

Status: in progress (integration check of 13 Nov 2026, PR #524: the key is right and is the envoys' own, but the slips
are decoded, not read, and the gap that holds them back, the transcription of the hand, is workable; folder only, no page
and no ledger row; catalogue 1639 narrowed, not removed). 13 Nov 2026, R8: a third, non-blind reading (R3) of f.102, f.104 and f.204 is
filed (`NOTES_R3.md`). 13 Nov 2026, R8: the blind fourth reading (b198, `blind4_b198/`) is in and verified; it is now the
figure of record for f.102, f.104 and f.204 and confirms that the hand, not the key, is the limit. The gaps are still
workable (the hand, frame 278, drafts not yet searched), so the target stays in progress. 14 Nov 2026, PR #558: the slip
labelled f.7 is fol. 6 verso, the second page of dispatch No. 32 (labels only; no figure changes; see "Correction of 14 Nov
2026" below), and the prior art of f.204 is not cleared. 14 Nov 2026, PR #578 (Andrew Beling, with AI agents): eight more
annexes of the volume decoded with the same key, the Nr. 540 clear copies of the 1645 annexes Nos. 31 and 32 found, and 23
gloss pairs of frame 278 checked against the key; all added texts are decoded, not read, and no figure of record changes
(see "Integration check of the Beling addition" at the end).
Outcome method set by the owner to "read with known key" (see Integration check of the R3 files).

Bottom line: the cipher is broken. We recovered the key from the ciphertext alone, and four independent checks confirm it, including the clear drafts in the sister volume Nr. 529. The slips are read only in part: every bare slip is below our own 65% line (strict 26.19% to 45.71% on the first pass, figures of record). The limit is our reading of the hand, not the key. The content of f.5, f.6 (recto and verso; the verso is the slip labelled f.7) and f.101 exists in clear in Nr. 529, so it is not first.

## What this folder is

Landesarchiv Sachsen-Anhalt (Magdeburg), A 1 Erzstift Magdeburg, Auswärtige Angelegenheiten, **Nr. 530**: papers of the archbishopric's envoys at the Osnabrück congress, 307 frames. The images come from the Landesarchiv viewer (`https://recherche.landesarchiv.sachsen-anhalt.de/images//A_1/Nr_530/max/A_1__Nr_530__NNNN.jpg`). The folder holds:

| slip | frame | heading on the slip | role here |
|---|---|---|---|
| f.5 | 8 | 1647 ad Diarium No. 31 | key training text |
| f.6 | 10 right | 1647 ad Diarium No. 32 | held out from KEY_v1, then key training text for KEY_v2 |
| f.7 (= f.6 verso) | 11 left | none (second page of No. 32) | held out from KEY_v2, but it is the other page of the dispatch whose recto (f.6) trained KEY_v2 |
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
| f.102 | b198, blind (since 13 Nov 2026; was R1 28/81 = 34.57%) | 22/84 = 26.19% |
| f.104 | b198, blind (was R1 45/101 = 44.55%) | 42/100 = 42.00% |
| f.204 | b198, blind (was R1 24/51 = 47.06%) | 19/52 = 36.54% |

The b198 figures count a word holding a letter the reader marked doubtful as a hole; R1 and R2 mark no doubtful letters,
so for them the rule changes nothing. See the integration check of the blind fourth reading below.

**Second reader** (b162, glossed reference crops, frozen before its own single decode): f.7 38/81 = 46.91%; f.102 31/79 = 39.24%; f.104 46/101 = 45.54%; f.204 22/51 = 43.14%.

**Training text, not counted:** f.6 with KEY_v1 (held out from v1) scored 35/101 = 34.65%.

No pooled figure is given as a headline.

**Figures that do not reproduce** (we use the reproduced value):
- f.104 R2: the b162 ledger states 47/101, but its line 7 says 7 and lists 6 S words; recounted, 46/101 = 45.54%.
- f.204 R1: the b160 ledger states 24/53, but the frozen file holds 51 cipher words (its line 2 says 10, the file has 8); recounted, 24/51 = 47.06%.
- Catalogus: 8/13 (9/13 with m = x), not the 13/13 in our session log.

**Blind reading:** one, b198 (the fourth reader, below), blind to the other readings but not to the key. Reader 2 (b162) did not see reader 1's transcriptions before freezing its own. It did know the key and the decodes of f.5 and f.6, so it is a second reader, not blind. Reader 1 is one reader, not blind: it had seen key output on f.5 and f.6. Word agreement between the readers (`agreement.txt`, `scripts/align.py`) is 162 of 312 R2 words = 51.92% over four slips: f.7 39/81, f.104 58/101, f.102 43/79, f.204 22/51. The systematic disagreements are g/q, c/e, t/l and a word-final f read as n.

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
- The content of f.5, f.6 recto and verso ("f.7") and f.101 is not first: it is in clear in Nr. 529 (`PRIOR_ART.md`).
- The contemporaries had this key (frame 168). A contemporary decipherment of f.102, f.104 and f.204 may survive.
- Our reading of the Nr. 529 drafts is one reader's and not blind.

## Remaining gaps

- Prior art of f.204 ("Annotata ad Num. 40", frame 233) - blocker: not-attempted; f.204 lies in the frames 226-259 Annotationes run linked to the margin notes of the Nr. 529 diary, and diary No. 40 was outside the ranges searched; Nr. 529 No. 40, the Nr. 545 fair copy and Nr. 546 are still to check (contributor's correction of 14 Nov 2026, follow-up promised).
- The hand: g/q, c/e, t/l and final f/n confusions cap every slip at 26-46% (f.7, f.101, f.102, f.104, f.204; the blind fourth reader b198 says the same of its own transcription) - blocker: not-attempted; the key is complete (the envoys' own table, frame 168), so a careful third transcription of the slips at full size with the frame-51 glossed reference is workable. The integration check found reader 2 closer to the image than reader 1 on f.204 lines 1-3 (below). Was marked "illegible" in `profile.json`; it is not.
- Clear drafts for f.102, f.104 and f.204 - blocker: not-attempted; Nr. 529 searched only in the frames listed in `nr529/README.md`; Nr. 543 (Krull's draft reports), 537, 538, 540, 546 not checked.
- Frame 278 of Nr. 530 ("Signatura catalogi sive clavis": a sign table and a long cipher passage with interlinear glosses) and frames 5, 6 - blocker: not-attempted; 23 gloss pairs of frame 278 now agree with the worksheet key (146/153 letters, PR #578, not blind), but its cipher passage is not read as a text and its signs are not used for the name signs; frames 5, 6 not compared.
- The 1645 annexes Nos. 31 and 32 (f.210-212): delta lines, the Elbe clause, zeta, the 27/72 year, the secretary's surname - blocker: not-attempted; 16 items in `nr540/f210_gaps.tsv`, the clear copies are in Nr. 540 Bd. 1.
- Nos. 20, 21, 22, 23 gamma (frames 250-259) and Nos. 3, 20 (frames 161-162): holes and marked repairs in most lines, strict 54-57% on the three with a word ledger - blocker: not-attempted; the hand again, and clear copies in Nr. 540 or drafts in Nr. 529 not yet searched for them. No. 29 (frames 244-245) and the cipher in the letters of frames 15-28, 186, 203, 252, 281, 283 are not filed.
- Name signs (Catalogus, frames 3 and 278) left as holes ('|') - blocker: not-attempted.
- f.101 is short (35 cipher words, one reader) - blocker: too-short for its own control; its clear draft is in Nr. 529 frame 532.

## Escalation

- [x] siblings: the five bare slips and the two training slips of Nr. 530 found and decoded; frame 278: 23 gloss pairs checked against the key (PR #578), passage unread; eight more annexes (frames 161-162, 240-243, 250-259) decoded by Andrew Beling, 14 Nov 2026 (open)
- [x] clear-pages: Nr. 529 clear drafts found for f.5, f.6, f.7 and f.101 (frames 875, 881-882, 532); not for f.102, f.104, f.204 in the frames searched; Nr. 540 Bd. 1 holds the clear copies of the 1645 annexes Nos. 31 and 32 (frames 633-634, 648-650; PR #578), not yet searched for the other annexes (open)
- [x] known-keys: the envoys' own key (frame 168, AMPHICTYONES) equals KEY_v2 in all 12 pairs; decoding the slips with it gives the same letters
- [ ] print: Acta Pacis Westphalicae and older Magdeburg histories not searched page by page
- [x] key-rebuild: not needed (the key is complete)
- [ ] retry: f.102, f.104 and f.204 re-transcribed by a third reader (R3, non-blind, 13 Nov 2026, `NOTES_R3.md`); f.7 also, as a check against its draft; f.101 not; blind fourth reader b198 (13 Nov 2026, `blind4_b198/`) on f.102, f.104, f.204: 26-42% strict, now the figures of record; still below 65% (open)

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

## Correction of 14 Nov 2026 (PR #558): "f.7" is fol. 6 verso

Contributor's file: `CORRECTION_2026-11-14_f7_is_f6v.md`. The slip labelled **f.7** (frame 11, left page) is not a separate
slip but the **verso of fol. 6**, the second page of the dispatch "ad Diarium No. 32"; the leaf foliated 7 (frame 11, right
page) is blank, and its verso (frame 12, left page) carries the endorsement "1647 ad Diarium No. 32". The contributor
credits the first notice to the frame sweep of a second checker (an AI model) and checked it on the images.

- **Checked at integration (14 Nov 2026).** LASA frames 10, 11 and 12 (`max` jpg, plain curl, 200) show exactly this:
  frame 10 right is fol. 6 recto headed "1647 ad Diarium No. 32"; frame 11 left is the same small slip turned over, and the
  right page is foliated 7 and has no cipher; frame 12 left is fol. 7 verso, blank but for "1647 ad Diarium No. 32". The md5
  values in the correction file cannot be re-checked: the viewer stamps each delivered image with the time of the request
  (footer "Landesarchiv Sachsen-Anhalt - 14.11.2026 02:15:49"), so every fetch gives a new file.
- **What changes.** Labels only: read every "f.7" in this folder as f.6v. File names stay as filed (they are inside the
  frozen manifests and timestamp tokens). The open set is four distinct slips plus f.6v (f.5, f.6r-v, f.101, f.102, f.104,
  f.204). No count changes: f.7 R1 36/83 = 43.37 % stays the figure of record for that page.
- **The held-out test of KEY_v2 on "f.7" (b160) was weaker than described.** It held out the other page of the dispatch
  whose recto trained KEY_v2, not a separate letter. The key does not rest on it: the Catalogus, the glossed postscript, the
  frame 168 worksheet (the envoys' own table, equal to KEY_v2 in all 12 pairs) and the Nr. 529 drafts confirm it.
- **f.204 prior art not cleared** (see Remaining gaps).

## Integration check (13 Nov 2026, PR #524)

Done by the integrating session after its own verification (report R8_bremen). The folder is merged as it came, with
`Status: in progress` and no page or ledger row; catalogue 1639 is narrowed (status text), not removed.

- **Reproduction** (scripts read first; `python3 -I` on a scratch copy): `build.py`, `confirm.py`, `align.py`,
  `compare_nr529.py`, `readings.py`, `keytable.py` rewrite every file byte for byte. Every per-slip figure reproduces,
  including the two the contributor corrected (f.104 R2 46/101, f.204 R1 24/51) and the catalogus 8/13. The original
  annealer (`scripts/original/solve_mono.py`, corpus path patched to a fresh Project Gutenberg 55171, md5 f476bb74 as
  asserted) run on `f5f6_combined_anneal_input.txt` with seed 3 and 3 restarts converges to KEY_v2 exactly (plus j = x).
- **Own decoder** from the frame-168 worksheet (AMPHICTYONES over zxwurqlkgfdb, both directions): all KEY_v2 decryptions
  agree word for word except the words holding cipher m, which the worksheet gives as x (f.102 "e?pecratdi" becomes
  "expecratdi"); no count changes.
- **Images** (LASA max jpgs, plain curl, HTTP 200): frame 168 shows the boxed AMPHICTYONES / zxwurqlkgfdb line, the
  untouched trial lines and "q: Centum, x: Mille", as `gloss/worksheet_frame168.txt` says. Frame 233 (f.204), lines 1-3
  (24 words) compared with both transcriptions: about 15 of 24 R1 words agree with my reading of the image, and R2 is closer
  (e.g. image "izodf", "odbzfldn", "hdlfduxdn", "tbdf", where R1 has idodf, odbzfdn, hdifdlxdn, tdsdf). The low shares are a
  transcription limit, as the contributor says. Frame 278 is a "Signatura catalogi sive clavis" with a glossed cipher passage
  (not in the folder; gap above).
- **Order of events**: KEY_v2 frozen 13:47:27, frame 168 first seen 14:00:36 UTC, by the contributor's record
  (`transcriptions/FREEZE_LOG.txt`); the first RFC 3161 stamp is 13 Nov 09:08:54 GMT. The catalogue entry the work started
  from already said the envoys' key was in the file, so the existence of a key was known, its content not.
- **Method** (superseded the same day, see the R3 integration check below): kept as "key recovered from ciphertext-only" (that is how the table was obtained, by the contributor's record),
  but the key is not new: it survives in the volume (frame 168) and gives the same decryption. The contribution is the
  transcription and the confirmation, not new key material. Recorded in `outcome.method_basis` and in catalogue 1639's
  vetting (`key_in_volume`).
- **Text state**: each slip's reading has holes in most lines (the contributor says so); `_check_reading.py` gives "not a
  reading" or "marginal" for every slip. State changed from "read in part" to "decoded, not read" per text; the entry class
  stays read in part.
- **fraction_read**: was the best single slip (f.204, 0.4706), which is selective. Now the five held-out slips at their
  figures of record, no selection: (36 + 16 + 28 + 45 + 24) / (83 + 35 + 81 + 101 + 51) = 149/351 = 0.4245 (135/354 = 0.3814 since the blind fourth reading). Per-slip
  figures stay as filed.
- **Gaps**: "the hand" was marked `illegible`; with a complete key and readable images it is `not-attempted`.
- **One key, one entry**: no other target or lead holds A 1 Nr. 530 or this table; thumbshirn1647 (Saxe-Altenburg envoys at the same congress) names catalogue 1639 but uses a homophonic key, a different system.

## Integration check of the R3 files (13 Nov 2026, R8)

By an AI agent for the maintainer, not a person. PR #524 received 14 more commits after the first integration (54 files
under `*_R3*`, `timestamps/b195/`, `gloss/REF_SIGNS_R3.md`, `NOTES_R3.md`, `PRIOR_ART_R3.md`); nothing existing changed.

- **What R3 is:** a third reader's transcription of f.102, f.104 and f.204 (and of f.7 as a check), with the same frozen
  KEY_v2, a sign reference built from the glossed frames and the Nr. 529 drafts, and one judging pass. Not blind: the reader
  knew the key and had seen reader 2's lists of read words for these slips (logged in `transcriptions/FREEZE_LOG_R3.txt`).
- **Reproduced** (`python3 -I`, scripts read first, outputs to a scratch folder): `decode_R3.py` gives the four
  `decryptions/*_R3.txt` byte for byte; `mkledger_R3.py` gives `units/f102_R3.tsv`, `f104_R3.tsv`, `f204_R3.tsv` byte for byte;
  `valscore_R3.py` gives f.7 against the draft as filed (59 pairs, 41 exact words = 69.49%, letters 318/341 = 93.26%).
  `shuffle_control.py` not re-run (needs the contributor's corpus); its outputs are filed.
- **Stamps:** the four RFC 3161 tokens in `timestamps/b195/` carry the SHA-256 of their manifests, and each manifest's hash
  equals the frozen R3 transcription (f.7 10:50:57, f.102 10:57:04, f.104 10:58:43, f.204 10:59:38 GMT). The TSA chain was
  not verified. That the decode came after (11:00:22) is by the contributor's record.
- **Counting:** `mkledger_R3.py` labels a unit S unless the reader listed it; "S?" marks borderline units (split-word halves,
  names spelt oddly, a dropped letter: "gesanten", "lasen", "genisenden", "crosen", "uehrden"). Under the strict rule
  (probable units are holes) the S? units are holes, so the strict figure is the contributor's "floor":

| slip | R3 strict (S? as holes) | contributor's figure, S? counted read | figure of record then (R1; replaced by b198 the same day) |
|---|---|---|---|
| f.102 | 53/84 = 63.10% | 61/84 = 72.62% | 28/81 = 34.57% |
| f.104 | 71/102 = 69.61% | 73/102 = 71.57% | 45/101 = 44.55% |
| f.204 | 42/51 = 82.35% | 45/51 = 88.24% | 24/51 = 47.06% |

- **Images:** LASA `max` jpg of frame 233 (2500 px, plain curl, 200). f.204: 7 lines, 51 cipher words and the name signs in
  the same places as R3. At this resolution letters in several words cannot be settled; where they can, R3 departs from the
  image at least once toward a word: image "tbdf" (as reader 2 and the first integration check read it), R3 "tzbdf" = "lasen"
  (labelled S?, so a hole in the strict figure). Frame 882 of Nr. 529 (fol. 807v, left): the underlined draft with "obstination"
  (margin), "gelangen", "schuldt an ihme nicht", "praesertim in pari ... constituti legati", "humeur", "nicht übel schicken" and
  the margin "...er autoritate" is there, cut at the gutter on the right as the pairs file says; the f.7 check pairs are sound in
  kind. Not checked word by word.
- **The reading reads:** f.204 under R3 is connected German: in confidence and for certain the envoys report dangerous counsels,
  that the archbishoprics and bishoprics be given up as recompense so that the others keep what they still hold. f.104 and f.102
  read in stretches.
- **Verdict on the figures:** R3 is a non-blind re-transcription after the reader had seen another reader's read words, and the
  image shows at least one word-seeking letter. Its figures are filed per slip as a third reading, labelled; they do **not**
  replace the figures of record, the text states stay "decoded, not read", and `fraction_read` stays 149/351. The contributor
  has said on the PR (13 Nov 2026) that a strictly blind fourth reader is running and will be added whatever it shows: that is
  the test that can move the figures, so the target stays `Status: in progress` until it is in.
- **Outcome method (owner's decision, 13 Nov 2026):** set to "read with known key", because the envoys' own key survives in the
  volume (frame 168, the AMPHICTYONES worksheet) and gives the same decryption. The facts stay as recorded: the contributor's
  table was recovered from the ciphertext by annealing and frozen before the worksheet was seen (by the contributor's record),
  and the worksheet then confirmed it in all 12 pairs. The label is the conservative one chosen by the owner for the paper.
- **Prior art for f.102, f.104, f.204** (`PRIOR_ART_R3.md`): no clear draft found in the frames searched (contributor's record,
  not re-checked here); the fair copies carry insertion marks only.

## Integration check of the blind fourth reading (13 Nov 2026, R8)

By an AI agent for the maintainer, not a person. PR #524 received six more commits (29 files in `blind4_b198/`: three
transcriptions, decodes and ledgers, scripts, a shuffle control, `REPORT.md`, `LOG.md`, `SHAPES.md` and two RFC 3161 stamps);
nothing existing changed. Report: `scratchpad/reports/R8_magd4.md` of the integrating session.

- **What it is:** reader b198 transcribed f.102, f.104 and f.204 from the five LASA frames (3, 51, 118, 121, 233) only,
  froze the three files, then decoded each once with the KEY_v2 table and judged each word once (S / SP period spelling / E).
  By its own list of what it opened, it saw no earlier transcription, decode, word list or reading. It **knew the key** (printed
  in its task text, as it says), as R1 and R2 did. The task text is not filed, so what else it carried is the contributor's record.
- **Stamps:** `openssl ts -reply -text`: the freeze token (Sectigo Public Time Stamping Signer R37, 13 Nov 2026 11:32:42 GMT)
  carries SHA-256 9817e417..., the hash of its `MANIFEST.sha256`, which lists the three frozen transcriptions with their
  current hashes; the result token (11:35:17 GMT) carries a3cf703f..., the hash of its 139-line manifest. `openssl ts -verify`
  with the system CA bundle: OK for both. 22 of the 23 filed files listed in the result manifest match; `LOG.md` matches
  without its last line ("result stamped", written after the stamp). So the transcriptions existed unchanged before the result;
  that no decode was run before the freeze is by the contributor's record (with the key known, it cannot be shown).
- **Own decoder** from the frame-168 worksheet (AMPHICTYONES over zxwurqlkgfdb), not the reader's script: 236 of 236 units equal
  `dec/*.decode.tsv`. `ledger.py` labels reproduce (S + SP: 33/84, 49/100, 25/52). The shuffle control was not re-run (needs
  Project Gutenberg 5323); the script was read and is sound.
- **Strict recount:** SP words are period spellings, which the target's rule counts as read. Words holding a letter the reader
  marked doubtful (`[x?]`) are holes under the '?' rule: 11 such S/SP units in f.102, 7 in f.104, 6 in f.204. Strict:
  f.102 22/84 = 26.19%, f.104 42/100 = 42.00%, f.204 19/52 = 36.54%. The reader's own figures, doubtful-letter words read:
  33/84 = 39.29%, 49/100 = 49.00%, 25/52 = 48.08%.
- **Image** (LASA `max` jpg of frame 233, plain curl, 200; the viewer burns its own date into each image, so md5s differ from
  the reader's): 50 cipher words over all seven lines compared with my reading. 36 agree, 3 differ (line 1: the initial capital
  of "[C?]odbpdodf" left out, which turns "deswegen" into "geswegen"; line 3: "tzbdf" where I see "tbdf", the reading R3 also
  made; line 5: "sdKzfcdf" written as one word where the image has a gap), 11 cannot be settled at this resolution (c/e and g/q,
  nearly all flagged by the reader). The signs agree in kind and place. I had the reader's file open, so this check is not blind.
- **The reading reads:** no. The decodes are lists of words with E words in every line; the text states stay "decoded, not read".
- **Figures of record:** b198 is the one reading of these slips that is blind to the others, has an external stamp on the frozen
  transcription and marks each doubtful letter; R1's freeze rests on session logs. It is better documented, so its strict figures
  become the figures of record for f.102, f.104 and f.204. f.7 (R1) and f.101 (R2) are unchanged. `fraction_read`:
  (36 + 16 + 22 + 42 + 19) / (83 + 35 + 84 + 100 + 52) = 135/354 = 0.3814 (was 149/351 = 0.4245). R1, R2 and R3 stay filed.
- **Status:** stays in progress. The blind reader puts its own shortfall on the transcription (c/e, g/q), not on the key, so the
  hand remains a workable gap; frame 278, the drafts in Nr. 537, 538, 540 and 546 and the Acta Pacis Westphalicae print are
  untried. None of these has an outside blocker.

## Addition of 13 Nov 2026 (Andrew Beling, with AI agents): eight more annexes, the Nr. 540 clear copies, frame 278

By Andrew Beling (`ajbeling`), with AI agents; not reviewed by a person. Added files carry the reader tag `BEL`. Nothing in
any earlier section or existing file of this folder was changed; this section and new entries in `profile.json` are the only
edits to existing files.

**Credit and courtesy.** Malcolm McBratney recovered this key from the ciphertext, identified the frame-168 worksheet as the
envoys' own key, and made the first readings of the slips; we use his key (identical to the worksheet) and his layout.
Two parts of this addition touch work he has announced: frames 250-259 lie in the frames 226-259 "Annotationes" run that his
correction of 14 Nov 2026 says he is checking against the Nr. 529 diary, and frame 278 is a gap he said on PR #524 he would
work on. He should feel free to take, replace or drop any of this.

**The diary numbers collide across series.** The 1644-45 No. 22 (by inference) and the 1645 Nos. 31 and 32 below are
different documents from this folder's f.104 (No. 22), f.5 (No. 31) and f.6 (No. 32).

| doc | Nr. 530 | annex, date | cipher words | state | files |
|---|---|---|---|---|---|
| f210 | ff. 210r-211r, frames 240-241 | No. 32, packet of 19 Mar 1645 | 922 (103 working records) | decoded, not read; complete source-assisted edition and English | `transcriptions/`, `decryptions/f210_frame240-241_BEL.txt`, `readings/f210_BEL.md`, `translations/f210_BEL.md`, `units/f210_BEL.tsv`, `nr540/` |
| f212 | f. 212r-v, frames 242-243 | No. 31, packet of 12 Mar 1645 | 328 (38 records) | decoded, not read; word-by-word source-assisted reading (S 187, S+L 231 of 328), edition and English | as above, `f212`, plus `readings/f212_BEL_read.md`, `units/f212_BEL_words.tsv` |
| f221 | f. 221r, frame 251 | 'Annotationes' No. 22, 1644-45 (by inference) | 294 | decoded, not read | `readings/f221_BEL.md` |
| f224 | f. 224r, frame 255 | 'Observationes' No. 21, 1644-45 (by inference) | 256 | decoded, not read; word-by-word reading (S 160, S+L 201 of 256) and English | `readings/f224_BEL_read.md`, `units/f224_BEL_words.tsv`, `translations/f224_BEL.md`, `readings/f224_f220_BEL.md` |
| f220 | f. 220r, frame 250 | No. 23, item gamma, 1645 (by inference) | 14 | decoded, not read | `readings/f224_f220_BEL.md` |
| f225 | ff. 225r-227r, frames 256-259 | 'Extra seriem Discursus' No. 20, 1644-45 (by inference) | 1,495 (164 records) | decoded, not read | `readings/f225_BEL.md`, `units/f225_BEL.tsv` |
| f138 | f. 138, frame 161 (+ slip 161/162 left) | 'ad Diarium No. 3' and the instruction slip | 48 | decoded, not read | `readings/f138_f139_f102_f104_BEL.md` |
| f139 | f. 139, frame 162 | 'ad Diarium No. 20' | 72 | decoded, not read; word-by-word reading (S 42, S+L 55 of 72) and English | `readings/f139_BEL_read.md`, `units/f139_BEL_words.tsv`, `translations/f139_BEL.md` |

In all, 386 working records and 3,429 cipher words. **A working record is not a verified physical line**: for No. 32,
the 103 records replace an earlier count of 104 that held an artificial label 37 (`nr540/f210_delta_crosswalk.tsv`).

- **How they were made.** Frames 161-162 and 250-259 (and f.102, f.104): two AI readers transcribed each group blind to
  each other and without the key, and hashed their files; one reconciler then settled the differences on the image,
  context-assisted and not blind. Nos. 31 and 32: transcriptions inherited from earlier reconciled rounds. Each
  `decryptions/*_BEL.txt` is the mechanical decode with the frame-168 table (`scripts/beling_build.py`; `--check`
  reproduces every file).
- **Word-by-word readings of f139, f224 and f212** (`readings/*_BEL_read.md`, ledgers `units/*_BEL_words.tsv`, one row per
  cipher word). Labels: S = the decode is the word as it stands (period spelling allowed); L = only the hand's known
  look-alikes (c/e/o, g/q/o, t/l, final f/n, h/k, u/h, i/r; at most two letters) or the second branch of a glyph the image
  did not settle, shown plain; R = any other marked repair, shown [?word]; E = not read, [...].

  | doc | words | S | L | R | E | strict S | S+L | S+L+R | `_check_reading` clean share of the reading |
  |---|---|---|---|---|---|---|---|---|---|
  | f139 (No. 20) | 72 | 42 | 13 | 15 | 2 | 0.5833 | 0.7639 | 0.9722 | 0.143 |
  | f224 (No. 21) | 256 | 160 | 41 | 50 | 5 | 0.6250 | 0.7852 | 0.9805 | 0.222 |
  | f212 (No. 31) | 328 | 187 | 44 | 83 | 14 | 0.5701 | 0.7043 | 0.9573 | 0.121 |

  The f139 ledger was set by hand; the f224 ledger was drafted by script from our earlier proposed reading and reviewed
  in one pass. For f212 the reading word is the word of the clear copy aligned by script within each paragraph (a few words are misaligned where cipher and copy differ):
  **187 of 328 cipher words agree with the Nr. 540 clear copy as they stand** (period spelling allowed), 231 with
  look-alikes; this is a source-assisted reading, not an independent recovery. **None of the three meets the repository's
  threshold for "read in part"** (about 0.60 clean sentences; a sentence with more than one hole in ten words is not
  clean, and every [?word] counts as a hole), so all three stay "decoded, not read", with `read_share` set to the strict
  share. The texts read as connected German and Latin once the marked repairs are accepted; the shortfall is in the
  repairs, which we leave marked.
- **Corrections after an independent check.** A second AI agent that had not seen our conclusions rechecked 51 words
  against the LASA images and the Nr. 540 clear copy: 37 confirmed, 10 differ, 4 not legible, and it found no duplicate
  of this folder's annexes. The differences: in No. 31, two transcription errors (L32 *erdbdsd* for *erdbdtsd* =
  dieselbe; L33 *qtxhla* for *gtxhla* = Olmütz), now corrected in `transcriptions/f212_frame242-243_BEL.txt` and
  `units/f212_BEL.tsv`; three g/q look-alikes (*ghx* = cum, *Wizdrhergritrqu* = praejudicirlich, *grigrldi* = circiter),
  where a crop of frame 242 shows the g-form as transcribed, so the transcription stays and the reading supplies c (label
  L); three words faithfully transcribed where the page itself has a near-miss (*ngf*, *trqdel*, *xzthm*). In No. 22 and
  No. 21 one word each where the reconciler had chosen the reader branch that decodes worse (*ehre* for *chre* = quid;
  *qgfurixrild* for *qgfnrixrild* = confirmirte); both branches stay in the transcriptions, and the f224 ledger reads the
  second branch (label L).
- **Nos. 31 and 32 are source-assisted, not independent recoveries.** Their editions were made with the envoys' clear
  copies in LASA A 1 Nr. 540 Bd. 1 open (No. 31: f. 585r-v, frames 633-634; No. 32: ff. 599r-600v, frames 648-650;
  `nr540/README.md`). The alignment of No. 32 is by paragraph units. The editions and English were reviewed by an AI
  agent (grade B, scoped: `readings/f21*_BEL_REVIEW.md`, where the reviewer label was changed from the model's product
  name to "Coordinating AI agent"). They are not in `fraction_read`.
- **Prior art.** Braun (2015) treats the March 1645 conversations of Lampadius from his reports (`PRIOR_ART_BEL.md`;
  selected indexed passages only). No edition of these cipher slips was found in that bounded check; that is not a
  novelty claim.
- **Frame 278 and the frame-4 booklet** (`gloss/frame278_BEL/`): two pre-registered checks of a key built from the
  booklet, both passed (0.8659 and 0.8889 of clear letters; best shuffled 0.2793 and 0.4314); rescored with the worksheet
  table, the 23 frame-278 gloss pairs give 146/153 letters and 18/23 words exact
  (`python3 -I scripts/beling_build.py --frame278`). Not blind. The pairs are name entries of the sign table and glossed
  words of the cipher passage; the passage was not read as a text and the name signs were not valued.
- **A further reading of f.102 and f.104** (`transcriptions/f102_frame118_BEL.txt`, `f104_frame121_BEL.txt`, decodes and
  `readings/f138_f139_f102_f104_BEL.md`), made without sight of any file in this folder. It changes no figure of record.
  Against b198, 57 of our 103 cipher words (f.104) and 43 of our 84 (f.102) are identical; most other differences are
  the c/e and g/q look-alikes (our readers wrote c-shapes as e). Our reading offers words where the strict ledgers have
  holes, by marked one-letter repairs (e.g. f.104 *ad dies [?vitae]*, *[?Recompens]*, *pro [?declinanda] sua aliisque
  [?concilianda invidia]*; f.102 *[?Reformierten]*, *[?Sagan]*, *Osna-brück*). These are proposals, not corrections. One
  image check (frame 121, alpha line 2): b198 and our transcription have *blidrlrodf* (= streitigen); R3 has *blidrtrodf*
  (streiligen). The sixth letter carries the crossbar of t, so the image favours R3's letter, and *streitigen* is an
  emendation in all three readings that give it.
- **Not added (held):** No. 29 (frames 244-245; 77 of 118 records low-confidence, η, θ2 and λ unread); our f.5 and f.6
  readings (Nr. 529 already gives their content); the cipher in the letters of frames 15-28, 186, 203, 252, 281 and 283
  (fragmentary, partly assisted by period glosses).
- **Our remaining gaps** (kept here so that this folder's own list is unchanged): 1645 No. 32 delta lines, the Elbe clause,
  zeta, the 27/72 year, and the secretary's surname in No. 31 are unsettled - blocker: not-attempted; the clear copies
  are in Nr. 540 (`nr540/f210_gaps.tsv` lists 16 items). Nos. 20, 21, 22, 23 gamma (frames 250-259) and Nos. 3, 20 (frames
  161-162) have holes and marked repairs in most lines - blocker: not-attempted; clear copies in Nr. 540 and drafts in
  Nr. 529 not yet searched for them.
- Copied reading files mention working paths of our project (`output/...`, `crops/...`, `sources/raw/...`); those
  files and the images are not in this repository.

## Integration check of the Beling addition (14 Nov 2026, PR #578)

Checked by an AI agent at integration; the contributor's section above is left as filed.

| claim | contributor | at integration | how |
|---|---|---|---|
| the ten decodes | reproduce | reproduce | `scripts/beling_build.py --check`: all identical; a second decoder written from the 12 pairs: 0 differing lines of 417 |
| cipher words, eight annexes | 3,429 in 386 records | 3,429 in 386 | recount (922, 328, 294, 256, 14, 1,495, 48, 72); f.102 84 and f.104 103 besides |
| frame-4 booklet key, right page | 0.8659, best shuffled 0.2793 | the same | `heldout_test.py` rerun on a copy |
| frame 278, 23 gloss pairs, booklet key | 0.8889, best shuffled 0.4314 | the same | `check_0278.py` rerun |
| frame 278 with the worksheet key | 146/153 letters, 18/23 words | the same | `beling_build.py --frame278` |
| SHA-256 lists of `gloss/frame278_BEL` | match | 11 of 11 match | `sha256sum -c` |
| word ledgers S / L / R / E | 42/13/15/2, 160/41/50/5, 187/44/83/14 | the same | recount of `units/*_BEL_words.tsv`; every `literal` equals the decode of its `cipher` |
| strict share f139 | 42/72 = 58.33% | **41/72 = 56.94%** | one S word stands on an unsettled glyph |
| strict share f224 | 160/256 = 62.50% | **139/256 = 54.30%** | 21 S words stand on an unsettled glyph |
| strict share f212 | 187/328 = 57.01% | 187/328 = 57.01% | no S word on an unsettled glyph |

- **The strict rule.** The ledgers count a word as S when the first of two branches of a glyph "the image did not settle"
  gives the word. For the blind fourth reading this folder counts a word holding a doubtful letter as a hole, and the same
  rule is applied here: f139 41/72, f224 139/256, f212 187/328. These are the `read_share` values in `profile.json`; the
  contributor's figures (58.33%, 62.50%) appear once, here and in the table of the section above. The ledgers are not blind (the
  readers knew the key; f212 is aligned with the clear copy), so none of the three enters `fraction_read`, which stays
  135/354 = 0.3814 on the five held-out slips.
- **Order of events.** That `PREREG.md` and `PREREG2_frame0278.md` were written before the key file and the frame-278
  transcription rests on the contributor's record (local dates, no external stamp). The frame-278 reader had seen the page.
  The booklet key differs from the worksheet in one pair (m/p for x/w, the W-shaped glyph written as m), which the
  contributor states; the tests confirm the known table and add no key.
- **Images** (LASA viewer, max jpg, 14 Nov 2026). Frame 162 (f139), all 72 words: 69 agree with the transcription, 3 are
  look-alikes (c/e in *bdehrhb*, g/q in *qgtldoz*, *giezd*). Frame 242 (f212) lines 1-6, 52 words: 48 agree, 4 are
  look-alike or smudged (*pdodf*, *qgÿdblWgferid*, *bdtsbt*, *xdrfd?*). Frame 278: ten of the 23 gloss pairs seen as
  transcribed (Mylonius, Rasquius, Medicus, Lampadius, Secretarii, General, Majeur, Minden, recomendiren,
  difficultaten). Nr. 540 Bd. 1 frame 633: headed "Annotationes ad continuationem Diarii sub No. 31", f. 585, opening
  "Praesertim cum sint Status Imperii atque inter eos plurimi Evangelici, quibus per Gallos non multum sperare liceat",
  which is the decode of f212 line 1 with its signs filled. Frames 648-650 (No. 32) and frames 250-259 were not opened.
- **Not first.** The content of the 1645 annexes Nos. 31 and 32 is in clear in Nr. 540 Bd. 1, as that of f.5, f.6 and
  f.101 is in Nr. 529. Braun (2015) was not opened at integration.
- **Class.** Every added text is below the 65% line and the gaps are workable, so the target stays `Status: in progress`:
  folder only, no page, no README row. Catalogue 1639 keeps its entry with one sentence added.
- **One key, one entry.** All added annexes use the frame-168 table; they belong in this folder.
- **Credit.** Andrew Beling, with AI agents (`ajbeling` in `outcome.credits`: transcription, identification of the
  Nr. 540 copies). The key and the first readings are Malcolm McBratney's. Two parts overlap work Malcolm McBratney has
  announced (frames 226-259 against the Nr. 529 diary; frame 278); both contributors' files stay side by side.


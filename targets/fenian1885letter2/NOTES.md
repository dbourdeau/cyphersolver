# fenian1885letter2: Fenian letter "No. II", London, 24 June 1885 (number code for names and key words)

Status: in progress. Filed as a pull request on 26 Nov 2026 AEST (25 Nov UTC) at Malcolm McBratney's direction, with the
open items below stated rather than closed. Work by Claude sessions (claude-opus-5-5) in hunts40 G3/B2, 25-26 Nov 2026.
No person has checked the transcription, the key or the reading yet (AI-checked only). The site write-up is left to the
maintainers, as in PR #996.

## Source
- [sourced] "Letter, no recipient and author given, June 24, 1885", Fenian Brotherhood Collection, The Catholic University
  of America (American Catholic History Research Center; formerly on WRLC Islandora, now a JSTOR Community collection).
  2 images (one folded sheet, 4 sides). Rights shown on JSTOR: "No Copyright - United States". Free to view.
  https://www.jstor.org/stable/community.38709311
- [measured] Viewed in the JSTOR viewer (Claude in Chrome, Mac) on 25 Nov 2026 UTC, without a JSTOR login. The PDF route
  could not be fetched by script (see IMAGE_ACCESS.md). Finding aid: https://findingaids.lib.catholic.edu/repositories/2/resources/109
- [derived] Writer and recipient are not named. The letter reports a meeting in a foreign capital with a man written as
  a number code (DEC below), arranged by "the Infant", at which the writer presented himself as "the English
  Representative of the firm". Context (1885, the Afghan crisis between Britain and Russia; the Irish World; Rossa and
  Clan na Gael approaches to Russia) is our inference, not checked in the literature.

## System [derived]
English clear text with 13 groups of two-digit numbers standing for letters: one shifted alphabet over 60-85,
A=77 B=78 ... I=85, J=60 ... Z=76 (letter n, A=1, goes to 60 + (n+16) mod 26). The writer runs the digits together and
often writes only the first letters and the last letter of a word, with a dash (RUS-A, NAT-E, L-D, PAT--S, R--S, OR--).
Word division is shown by the writer's spacing and punctuation. 19 distinct pairs occur (measured, below).

## Transcription (frozen)
- freeze/TRANSCRIPTION.txt: the whole letter, clear text and groups, line by line, with the doubts D1-D5. Frozen
  2026-11-25T23:31:52Z (freeze/FREEZE_TX.txt; sha256 af7f761b...; stamped: freeze/stamps/, RFC 3161 Sectigo and FreeTSA,
  OpenTimestamps pending). First pass = figure of record.
- freeze/NUMBER_GROUPS.tsv: the 13 groups as written. Known slip in a frozen file: the n_pairs column gives 7 for G11,
  which has 8 pairs (counted by script). The decode and all figures count from the pairs themselves, not that column.
- CIPHERTEXT_PAIRS.txt: pairs only, derived by script from NUMBER_GROUPS.tsv for measuring.
  `python docs/_check_profile.py --measure targets/fenian1885letter2/CIPHERTEXT_PAIRS.txt --digits --drop-first`:
  71 tokens, 19 distinct (the doubtful 7?7 counted as one token).
- Exposure [stated]: the transcriber saw the x-y-x pattern 85 68 85 and formed the key hypothesis BEFORE the freeze, and
  used it to look again at doubts D2 and D3 (freeze/DISCLOSURE.txt). The first transcription is not blind to the key.
  No held-out split: the whole letter was seen before the freeze.

## Key and how it was recovered (ciphertext-only)
- key/KEY.tsv (26 values; identical to result/KEY.tsv). Frozen 2026-11-25T23:32:04Z with decode v1, and again at
  23:32:10Z with decode v2 (decoder bug fix only, key unchanged): key/FREEZE_KEY.txt, result/stamps/.
- Crib [derived]: G08 "85 68 85 69 84 / 73 65 68 62 80" follows "we had the whole ... with us". The repeat x-y-x at the
  start fits IRI-, and IRISH WORLD fits all 10 pairs under one shift. One parameter fixes all 26 values.
- Checks not used to build the key: WOLFE TONE (9 pairs), CANADA (5 of 6 pairs; 1 doubtful), RUS-A, PAT--S,
  OUR NAT-E L-D.
- No key was found in the collection or in print. The Fenian "list of code words" on JSTOR (community.38709677) is an
  open word code for cables, with no number-for-letter table: not this key (PRIOR_ART.md).

## Decode of all 13 groups (result/DECODE.txt, scripts/decode.py, one pass with the frozen key)
| id | place | as written | key output | reading | status |
|---|---|---|---|---|---|
| G01 | P2.8 | 68 71 69 - 77 | RUS-A | Russia | read (writer's abbreviation) |
| G02 | P2.21 | 80 81 , 79 | DE,C | DEC, the man interviewed | letters read; referent NOT identified |
| G03 | P3.15 | 80 81 - 79 | DE-C | DEC | as G02 |
| G04 | P4.4 | 80 81 . 79 | DE.C | DEC | as G02 |
| G05 | P4.6 | 80 81 79 | DEC | DEC | as G02 |
| G06 | P4.11 | 73 65 62 82 81 70 65 64 81 | WOLFETONE | Wolfe Tone | read |
| G07 | P4.14 | 69 81 79 ^r? 81 70 , 65 68 —— | SEC[r]ET,OR—— | secret or[ganisation] | read; r is a plain letter written above; OR-- expansion is ours |
| G08 | P4.16-17 | 85 68 85 69 84 / 73 65 68 62 80 | IRISH WORLD | Irish World | read (crib) |
| G09 | P4.18 | 68 —— 69 | R——S | R--s | letters read; word open |
| G10 | P4.19-20 | 66 77 70 — — 69 | PAT——S | Patriots | read (abbreviation) |
| G11 | P4.20 | 77 71 ^70 64 65 64 63 75 | AUTNONMY | Autonomy | read with 1 emendation (N-O-N written for O-N-O) |
| G12 | P4.21 | 65 71 68 . 64 77 70 — 81 . 62 — 80 | OUR.NAT—E.L—D | our native land | read (abbreviation) |
| G13 | P4.23 | 79 7?7 64 77 80 77 | C(#/A)NADA | Canada | read; pair 2 doubtful |

## Reading (READING.txt; cipher words in ⟦ ⟧, letters we supply in [ ])
The letter, in short [derived]: the writer, back in London on 24 June 1885, reports that his "mission has been a most
complete success". With "the Infant" he met ⟦DEC⟧ in a richly furnished apartment; the Infant's written digest set out
"the mutual advantages likely to accrue to ⟦Rus[si]a⟧, and ourselves". DEC questioned the writer in English, and the
writer felt himself "⟦Wolfe Tone⟧ before the Directory". He told DEC that "we were not alone a ⟦secret⟧ ⟦or[ganisation]⟧"
but had "the whole ⟦Irish World⟧ with us"; that "we were not ⟦R[...]s⟧ in the strict sense of the word but
⟦Pat[riot]s⟧ struggling for the ⟦Aut[ono]my⟧ of ⟦our⟧ ⟦nat[iv]e⟧ ⟦l[an]d⟧". The sheet ends with DEC asking: "do you think a
diversion in ⟦C[a]nada⟧ feasible". The letter breaks off there; the continuation is not in this item.
The full text, line by line, is in READING.txt. English, so no translation is needed.

## Figures (per group, first pass, measured by script; never pooled across documents)
- Pairs [measured]: 71 pairs in 13 groups; all in 60-85 except the doubtful G13 pair 2 (47 if read 4-7).
  Pairs giving the letters of the reading: 71 - 1 doubtful (G13) - 3 out of order (G11) = 67; **67/71 = 94.4%**.
- Groups with an identified meaning [measured]: 13 - 4 (G02-G05, one person, DEC) - 1 (G09, R--S) = 8;
  **8/13 = 61.5%. This is UNDER our own 65% line, so the letter FAILS at group level.** The pair figure passes; the
  group figure does not, because one unidentified person recurs four times.
- Per group (pairs / clean pairs / meaning identified): G01 4/4 yes; G02 3/3 no; G03 3/3 no; G04 3/3 no; G05 3/3 no;
  G06 9/9 yes; G07 7/7 yes; G08 10/10 yes; G09 2/2 no; G10 4/4 yes; G11 8/5 yes (emended); G12 9/9 yes; G13 6/5 yes.
  Sum: 71 pairs, 67 clean.
- Read bar (README Conventions) [derived]: not met. Strict word count over the 18 cipher words (Russia 1, DEC 4,
  Wolfe Tone 2, secret or-- 2, Irish World 2, R--s 1, Patriots 1, autonomy 1, our native land 3, Canada 1): words given
  by the key with nothing supplied and no doubt = Wolfe, Tone, secret, Irish, World, our = 6 (DEC x4 is fully given as
  letters but its referent is unknown); 6/18 = 33% by that count. The writer's own abbreviations make most words holes
  under the strict rule. Class: read in part.
- G11 emendation: written 77 71 70 64 65 64 63 75 = AUT N O N MY; AUTONOMY needs 65 64 65 (O N O). The blind second reader
  also reads 64 65 64, so it is likely the writer's slip, not our misreading. Counted as 3 unclean pairs.
- G13 pair 2 doubtful: read 7?7 (first reader) and 4?7 (blind reader, alt 77); 47 is outside 60-85; CANADA needs 77 (A).
  Not counted as clean.

## Controls (result/CONTROLS.txt, scripts/controls.py)
Fixed before running: 5 test words (IRISH, WORLD, WOLFE, TONE, OUR); English lexicon lang/lexicons/en.json.gz (29,657
words; decompressed sha256 ea5582ab...; the .gz is byte-identical to the repository copy, sha256 0a58de21...).
- Real key: 5/5 words.
- Other 25 shifts: 0/5 each (max other than real: 0).
- 5,000 random keys, seed 20261112: 0 score >= real; max 2. Seed 7: 0; max 2.
- 5,000 shuffles of the ciphertext under the real key, seed 20261112: 0 >= real; max 2. Seed 7: 0; max 2.
- Held-out test: none possible (the whole letter was seen before the freeze). IRISH and WORLD are the crib words, so
  3 of the 5 test words (WOLFE, TONE, OUR) are independent of the crib.
- scripts/controls.py holds the working path of the lexicon; in a checkout set `lexp` to lang/lexicons/en.json.gz.
  Re-run on 26 Nov 2026 from this folder: DECODE.txt and CONTROLS.txt reproduce exactly.

- Repository statistical test (`python docs/_validate.py fenian1885letter2 --write`, validation.tsv, en-modern order 4,
  26 Nov 2026): 70 read tokens, 18 types, 64 letters, score -3.559 per letter; verdict **too short** (under 80 letters),
  so it neither confirms nor refutes the key. Recorded in profile.json outcome.validation.

## Blind second reading (blind2/)
An isolated AI reader (Claude subagent) read the number runs from the viewer crops only, with no transcription, key or
decode; frozen and stamped 2026-11-25T23:37:20Z (blind2/FREEZE.txt, blind2/stamps/). Alignment (blind2/ALIGN.txt):
- first reader 71 pairs, blind reader 72; position by position **70/71 = 98.59%** agree.
- the one difference: G13 pair 2 (7?7 vs 4?7, both doubtful).
- the extra blind pair: **64 at the end of G07** ("65 68 —— 64."), where the first reader read "—— but". 64 = N, which
  would make OR——N, the writer's first-letters-and-last-letter habit for "organisation". Not in the figure of record;
  owed to a human check.
- the blind reader reads the letters above the caret in G07 as "re" (low confidence); first reader "r?".
- figures of record unchanged.

## Transcription doubts
- ^r? (P4.14, G07, above a caret between 79 and 81) - read: r, a plain letter; checked: image, decode, transcription; SECRET needs r; blind reader reads ^re (low confidence); not a digit pair either way.
- 7?7 (P4.23, G13 pair 2) - read: 7?7 (77 or 47); checked: image, decode, transcription; CANADA needs 77; blind reader 4?7 best, alt 77; digit bottoms clipped by the page edge; stays doubtful and is not counted.
- 64 (P4.11, G06 pair 8) - read: 64 (first read 84); checked: image, decode, transcription; WOLFETONE needs 64 (N); blind reader 64; re-checked after the key hypothesis (exposure).
- 70 (P4.11 G06 pair 6; P4.14 G07 pair 5) - read: 70; checked: image, decode, transcription; T is needed in WOLFETONE and SECRET; blind reader best 70 in both, alt 76/78.
- 64 65 64 (P4.20, G11 pairs 4-6) - read: 64 65 64; checked: image, decode, transcription; the sense wants 65 64 65; blind reader agrees with 64 65 64, so kept as written and emended in the reading only.
- 64 after G07 (P4.14, after "——") - read: not in the frozen transcription ("—— but"); checked: image (blind reader's zoom), decode, transcription (blind reader 64); open until a person looks.
- struck word (P3.20) - read: not read; checked: image, decode (clear text, no number group); no effect on the figures.
- "Madame H—" (P1 top note) - read: H (or A); checked: image, decode (clear text, no number group); no effect on the figures.

## Remaining gaps

- **Reading review (26 Nov 2026):** Malcolm McBratney read the decoded letter as sentences and graded it A. He reads R—s (68 —— 69, side 4 line 18) as "revolutionaries". That reading comes from the sense, because only R and S are written. He also notes that DEC (80 81 79) is the same person in all four places, and that the dots and dashes between the numbers are loose handwriting. DEC is still not identified, and the struck word on side 3 line 20 is still unread.
- (a) Book prior art not checked: Devoy's Post Bag (O'Brien and Ryan, 1948-53), Short, The Dynamite War (1979), Whelehan, The Dynamiters (2012), Kenna, War in the Shadows (2014), Jenkins on F.F. Millen - blocker: needs-physical-access; no full text reachable from the sandbox; phrases for HathiTrust/Google Books are listed in PRIOR_ART.md. A historian may have read this simple alphabet in print without calling it a decipherment.
- (b) Human check of the transcription and the key (a person comparing the groups with the image) - blocker: not-attempted; owed. The blind AI second reading is done (70/71).
- (c) DEC (G02-G05), the man interviewed, not identified - blocker: open-codes; the letters are read; the referent (code name, initials or abbreviation) needs the literature or the other letters of the series.
- (d) R--S (G09) open - blocker: open-codes; letters read; the word ("we were not R--s in the strict sense of the word") is not settled (Revolutionists? Rebels? Republicans?).
- (e) The PDF could not be fetched by script; the working images are screen zooms from the JSTOR viewer - blocker: needs-physical-access; a person can download the PDF from JSTOR, or ask the CUA archive for images.
- (f) The letter breaks off at the foot of side 4 mid-quotation; the continuation (and Letter No. I) is not in this item - blocker: needs-physical-access; the rest of the series has not been found in the CUA collection on JSTOR.
- (g) G13 pair 2 doubtful (7?7 / 4?7) - blocker: illegible; digit bottoms clipped at the page edge in the viewer; a better image or the original would settle it.

## Escalation
- [ ] siblings: the Fenian code-word list (community.38709677) opened; F.F. Millen to Rossa, 23 Feb 1885, and R. Bennett to Rossa, 16 Dec 1885 (same JSTOR search) found but not yet opened; Letter No. I not found.
- [x] clear-pages: both images of the item read in full; no decipherment, key or gloss on the sheet.
- [x] known-keys: the Fenian code-word list (community.38709677) compared: an open word code, no number table; no other Fenian number key found.
- [ ] print: Devoy's Post Bag, Short, Whelehan, Kenna and Jenkins not checked (gap a); DECODE, Cyphersolver, JSTOR and web searched (PRIOR_ART.md).
- [n/a] key-rebuild: the key is a one-parameter shift; all 26 values follow from it and every pair maps to a letter, so there is nothing to extend.
- [x] retry: every group decoded with the frozen key; the open pieces (DEC, R--S) are referents, not undecoded pairs.

## Files
- freeze/ (frozen transcription, groups, disclosure, stamps); result/ (key, decode v1 and v2, controls, READING.md,
  stamps; the stamp manifests cover these files as they are); key/KEY.tsv and key/FREEZE_KEY.txt (copies);
  scripts/decode.py and scripts/controls.py (copies of the frozen scripts); blind2/ (blind reading, alignment, stamps);
  READING.txt; CIPHERTEXT_PAIRS.txt; PRIOR_ART.md; IMAGE_ACCESS.md; SOLVE_LOG.md; RUN_RECORD.tsv; profile.json.
- result/KEY_rule.txt is the v1 decoder (it carries the key rule as code); result/DECODE_v1_crashed.txt is the v1 output.
- Images: not filed. Viewer positions and the working crops are described in IMAGE_ACCESS.md.

## Record note
RUN_RECORD.tsv rows up to 23:33Z were written during the work; the blind reading and filing rows were added at filing
from the freeze files and stamp logs. Effort is not exposed on this surface.

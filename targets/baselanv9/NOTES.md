# baselanv9: Clavicula Salomonis and Septem sigilla planetarum in a secret alphabet, Basel UB, UBH AN V 9 (17th century)

Status: in progress. Contributed by pull request, not yet written up (pass 2 with the volume's key leaf added 25 Nov 2026 in `keyleaf/`, scored by a separate judge the same day; see "Pass 2" below; pass 3 added the same day in `pass3/`: H1 re-read, not held out, 399/405 = 98.5% judged, a fresh held-out passage H4 389/415 = 93.7% judged, 11 second-series rims 486/521 = 93.3% judged with one rim under the 65% line, see "Pass 3" below; pass 4 added 27 Nov 2026 in `pass4/` for Dan Bourdeau's re-review: Tk@ = ru, the nasal-dot rule on the rims, 16 rim words Dl@ -> X@ on the image, counted in sure words per text: S1 rims 385/474 (pass 2 366/472), 53 of 62 rims over 65%, H2 61.90% under, see "Pass 4" below; pass 5 added 27 Nov 2026 in `pass5/` for Dan's point 4: the signs inside the circles of ff. 52r-53r (21/63 sure words), the four figures of f. 54r (28/42) and f. 97r-v (24/42), and the 51 remaining `Dl@` words looked at on the image (15 -> `X@`), H2 62.70% still under, see "Pass 5" below; the first pass stays the figure of record), and a new target: the volume is in neither `catalogue.json` nor `research/leads.json`. The key was recovered from cipher ff. 4r-4v aligned with the volume's own clear copy, frozen, and used for one decode of three held-out passages. A separate strict judge finds 747 of 1,138 decoded letters in words that read as sense (65.6%: H1 62.4%, below the contributor's own 65% line; H2 67.0%; H3 69.6%), and the decode reproduces 988 of 1,231 letters of the clear copy (80.3%). Counted in words, 113 of 225 read as sense (0.502) and no sentence is clean, so each first-pass passage is "decoded, not read". **Since 28 Nov 2026 the target is classed read in part** at Dan Bourdeau's request (review of 27 Nov 2026 on PR #957): each pass-5 text, rim and part takes its state from its own sure-word count (72 read, 52 of them only by the short-text floor; 21 read in part; 7 decoded, not read; see "States per text" below); the reading reviews were recorded at the merge (28 Nov 2026) by an AI agent for the maintainers, not a person (see "Reading reviews at the merge" below). The volume's own key leaf, viewed only after the decode, agrees on 46 of the 52 values it covers. The page, ledgers, DECODE queue entry and any catalogue or lead entry are left to the maintainers.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Opus 5.5 the solver session, the separate strict judge and the assembly of this folder; pass 3 (`pass3/`) transcribed, decoded and assembled by Claude Fable 5.2, its judge's model not recorded.

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working sessions, not checked here; [unverified] = a reading of the text not checked by anyone else.

## The source

- Basel, Universitätsbibliothek, UBH AN V 9 (old shelfmark K IV 19): "Clavicula Salomonis, Septem Sigilla Planetarum", 17th century (catalogue: 1600-1699), one volume of 180 leaves in two parts (18.5-19 x 14.5 cm and 20 x 15 cm), Latin [sourced: the METS/MODS record of e-manuscripta 5353221 and its IIIF manifest].
- Online: e-manuscripta.ch, https://doi.org/10.7891/e-manuscripta-185551, online since 1 Sep 2025 (digitised April 2025); IIIF manifest https://www.e-manuscripta.ch/i3f/v20/5353221/manifest, 380 canvases [sourced]. Page images: `https://www.e-manuscripta.ch/i3f/v20/<page id>/full/2000,/0/default.jpg` (`FETCH_LOG.txt`; canvas, folio and page id in `work/canvases.tsv`). The held-out pages: f. 15r page id 5353252, f. 159r 5353544, f. 34r 5353290; training f. 4r 5353230, f. 4v 5353231 (`SPLIT.md`).
- Licence: the record's use and reproduction condition is the Creative Commons Public Domain Mark 1.0 (https://creativecommons.org/publicdomain/mark/1.0/) [sourced: `mods:accessCondition` in the METS record, the working folder's copy of 24 Nov 2026, read 25 Nov 2026]. No page images are committed; the URLs above are cited instead. The seven small reference crops made in pass 4 (`pass4/crops/*.jpg`) were removed by the maintainers when PR #957 was merged (28 Nov 2026), so the `crops/` files named in "Pass 4", `pass4/DL_CHECK.tsv`, `pass4/KEY_V4.tsv` and `pass5/DL_CHECK_P5.tsv` are not in the repository, and their seven sha256 lines in `pass4/FREEZE_P4.txt` can no longer be checked here; the same places can be cut again from the page images above (f. 99r, canvas 205; the rims of ff. 35r, 36r, 38r and 46r).
- Contents, from Martin Steinmann's unprinted description (https://ub.unibas.ch/digi/a100/kataloge/mscr/mscr_div_gr/BAU_9972848358705504_cat.pdf) and the swisscollections record, as quoted in `PRIOR_ART.md` [sourced]: ff. 3r-96v the Clavicula, "in einer Art Geheimschrift geschrieben", with pentacles drawn on the rectos of ff. 33r-55v (versos blank) and two more on f. 97r-v; ff. 98-99 two pasted-in, folded leaves, f. 99r "mit dem Schlüssel zu den Siglen der Geheimschrift sowie Erklärungen dazu auf Dänisch" and f. 98r "deutsche Uebersetzung von 99r"; f. 100r a clear title; ff. 101r-155r "Gleicher Text wie 3r-96v, aber in normaler Schrift geschrieben"; f. 157r magic squares; ff. 158r-162r the Septem sigilla in cipher; ff. 166r-170r the same in clear; ff. 172r-177r astrological tables in several hands. Modern pencil foliation I.1-179.

Length [measured]: `python docs/_check_profile.py --measure transcription.txt --drop-first` gives 2634 whitespace tokens = 2132 signs + 475 word separators (`/`) + 12 line fillers (`Fill`) + 15 line-end hyphens (`Eq`). By page: f. 4r 546 signs, f. 4v 681 (training, 1,227); f. 15r lines 1-12 290, f. 159r 563, f. 34r two rims 52 (held out, 905). With the dot above, the dot below and the diaeresis split off as tokens of their own (`scripts/common.py`): training 1,383 key tokens, held out 1,034 (331 + 644 + 59, `work/decode_counts.txt`). `transcription.txt` is the five frozen files of `tx/` put together unchanged, for this count.

## The system (`KEY.tsv`)

A secret alphabet of invented and digit-like signs for Latin letters, with signs for letter groups, a few signs for whole words, and marks written on a sign. Labels name shapes (`SIGNS.md`): 51 base labels and 6 marks. The recovered key values 62 tokens and states two rules [measured: KEY.tsv]:

| letter | sign(s) | letter | sign(s) | letter | sign(s) |
|---|---|---|---|---|---|
| a | Lm; Ea word-final | i | X | q | Oe |
| b | 1 | l | 7 | r | Tk; Cl; Pl word-final |
| c | 8 (Bl once) | m | 2; a dot above a sign | s | 6s; 6v; Ph; Ar word-final |
| d | 3 | n | 4; a dot below a sign | t | Ds; Lr word-final |
| e | 6; D1; Cd | o | Bx (D3 once) | u | Dl; Cs |
| f | 9 | p | Pe | x | Rt |
| g | 5 | h | Oc | | |

- Letter groups: 6t et, 6r er, 6L es, Xc it, Lb ct, 5b st, Hk sc, Dv nt, As ae, Lmt an, Dh ur, Tk@ ru, Ab tur, Am con, Dl@ s.
- Word signs: Oe" quod, Oe^m quam, Oei qui, Oe~ quas, Q3 que, Bx~ non, 5~ igitur (given no letters in the key).
- Rules: two dots on the line (D2) repeat the nearest vowel before them in the word (34 of 43 training cases; 43 of 43 for some earlier vowel); two dots above a sign double its letter (14 of 14) [measured: SOLVE_LOG.md].
- A fault of the key of record [derived: KEY.tsv and the transcriptions]: the placeholder label `?` (a sign the transcriber did not identify) has the value i from its one training use (f. 4r l. 17), so the 7 unidentified held-out signs all decode as i (in iorum; twice in aiunciai; in dniositam, iniicoen and consequei; and the lone i of pentacle 4).

### The volume's key leaf, compared after the decode

f. 99r was fetched and viewed only after `FREEZE_KEY.txt` and the decode, and transcribed with this project's labels (`tx/KEYLEAF_f099r.txt`; Danish quoted in the transcriber's own reading, unverified). The comparison is `work/keyleaf_vs_key.tsv` [measured]:

- 52 of the 62 recovered tokens are on the leaf; **46 agree**.
- 4 differ: Dl@ (recovered s, leaf us), Oe~ (quas, leaf quem), Lmt (an, leaf at), D3 (o, leaf: the same letter further back, a positional rule).
- Cl is context-dependent on the leaf (ri after Tk, rt and tr beside Ds, autem after Lm, enim after 4); the recovered key has its majority value r. The recovered two-dot rule (nearest vowel) approximates the leaf's ("the letter standing next before, with a dot in its middle").
- 10 recovered tokens are not on the leaf (6v, Cd, Ab, Ph, X~, 5~, ?, Bl, Ea~, Lm~).
- The leaf has signs the training leaves never met (k, y, z, oe, ar, ir, or, as, is, os, ot, ut, ter, te, gl, ph, pt, ps, ia, io, ch, sch, sp, quae) and context values for pairs of known signs (re, ri, ti, rt, tr, th, unt, enim, autem).

## Method

The pipeline is the contributor's: prior art first, a split recorded before any key building, transcription and key frozen before one decode, a separate strict judge, the first pass as the figure of record, shuffle controls. Times are UTC, from the sandbox clock and the freeze files.

1. **Prior art** before any transcription (11:59 to 12:10 on 24 Nov 2026): `PRIOR_ART.md`. See "Prior art" below.
2. **Access.** The IIIF manifest and the page images at 2000 px answered plain curl (`FETCH_LOG.txt`). The e-manuscripta title page and swisscollections showed bot checks to curl; they were not passed by the script, and swisscollections was read in the contributor's own browser session. The key leaves ff. 98-99 (canvases 199-206) were quarantined in `scripts/fetch.sh` until the key was frozen.
3. **Split** (`SPLIT.md`, 12:38): training ff. 4r and 4v against the clear ff. 101r-102r; held out H1 = f. 15r lines 1-12 (the first undamaged full text page at least ten leaves after the training leaves), H2 = f. 159r (Sigillum Iovis), H3 = the rims of pentacles 3 and 4 on f. 34r (no clear counterpart was expected).
4. **Transcription** by sign shape with neutral labels (`SIGNS.md`; `tx/`), one reader (Claude Opus 5.5), one pass, zoomed crops of the 2000 px images, the pentacle rims from a polar unwrap (`scripts/unwrap.py`). Frozen at 12:51:30 (`FREEZE_TX.txt`). **Blindness limits, stated in the freeze file:** the training leaves were transcribed with the clear copy beside them, so the common values were recognised while transcribing; the held-out leaves were transcribed without their clear counterparts but by a reader who already knew most of the system; the first two lines of H2's clear page (f. 167r) were seen at contact-sheet size during the first look (`SPLIT.md`).
5. **Key from the training leaves only** (`scripts/solve.py`, `SOLVE_LOG.md`): word alignment of cipher words to clear words by dynamic programming, an EM emission model over segmentations, Viterbi alignments, the key as each token's commonest emission. Run 1 failed in part (two modelling faults found on the training data, `work/KEY_run1.tsv`); run 2 aligned 301 word pairs with no cipher word left over and is the key of record. Frozen at 12:55:46 (`FREEZE_KEY.txt`: KEY.tsv ec59fefe..., matching the file here).
6. **One decode** of the three held-out passages with the frozen key (`scripts/decode_once.py`, written at 12:56; `DECODE.txt`). No emendation: the first pass is the figure of record. `DECODE.txt` was written again at 13:21 with identical content when `scripts/train_fit.py` imported the decoder; `work/DECODE_HASH.txt` records both hashes, and `judge/decode.txt` (13:05) is the copy given to the judge.
7. **Separate strict judge** (Claude Opus 5.5): given only `judge/BRIEF.txt` and `judge/decode.txt` [stated], and told not to consult any edition, the Clavicula literature or any other reading of the manuscript; it scored every decoded letter S (in a word that reads as sense in Latin), E (one-letter slip in a readable word) or N. Its word tags are in `judge/count.py` (strict rule: a word with more than one wrong, added or missing letter is N), which re-adds them into `judge/judge.tsv` [measured: re-run here on a copy, output identical].
8. **Clear-copy comparison**, made after the decode (12:56 to 13:04): the counterparts of the held-out passages were located and transcribed (`score/CLEAR_H1_f109v.txt`, `CLEAR_H2_f167r.txt`, `CLEAR_H3_f123r.txt`; f. 123r turned out to hold the pentacle rims, against the expectation in `SPLIT.md`), and the decode was scored letter by letter (`scripts/score_clear.py`).
9. **Key leaf** fetched at 12:59 and compared with the frozen key (above).
10. **Shuffle control** (`scripts/shuffle.py`, 13:33): the key's values permuted among its 58 base tokens (the three mark tokens and the two-dot rule fixed), 5,000 keys at each of seeds 20261112 and 7.
11. **Time-stamps** (`stamps/`): a sha256 manifest of 63 files of the working folder at 21:21:29 on 24 Nov 2026, stamped by RFC 3161 at Sectigo (21:21:29 GMT) and FreeTSA (21:21:31 GMT); OpenTimestamps submitted, pending (`stamps/STAMP_LOG.txt`).
12. **Assembly** (25 Nov 2026, Claude Opus 5.5): `reading.md`, `translation.md`, `validation.tsv` and `docs/_validate.py`, `profile.json`, this file.

Order of events: the stamps prove only that the files existed by 21:21 on 24 Nov 2026. `FREEZE_KEY.txt` lists the hashes of the training-side files and not of `DECODE.txt`, and the file times agree with the stated order (key frozen 12:55:46, decoder written 12:56:06, clear-copy page images fetched from 12:56:33, key-leaf images at 12:59:24, judge packet 13:05:21, key leaf transcribed 13:18:32), but the order rests on the contributor's record. The judge's tags in `judge/count.py` and `judge/judge.tsv` carry the time 21:20:54 [measured: file times in the working folder].

The scripts keep the working folder's paths (`/home/claude/keyless/round40c/basel_anv9/`, and `/home/claude/keyless/_cs` for `lang/`) and do not run from this folder as they stand.

## Figures (first pass of record)

Strict judge, letters (`judge/judge.tsv`, re-added by `judge/count.py`) [measured]:

| passage | S | E | N | letters | S share | signs with no value |
|---|---|---|---|---|---|---|
| H1, f. 15r lines 1-12 | 229 | 19 | 119 | 367 | 229/367 = **62.4%, below the 65% line** | 5 |
| H2, f. 159r | 470 | 30 | 202 | 702 | 470/702 = 67.0% | 5 |
| H3, f. 34r pentacles 3-4 | 48 | 3 | 18 | 69 | 48/69 = 69.6% | 0 |
| all | 747 | 52 | 339 | 1138 | 747/1138 = 65.6% | 10 |

Sums: 367 + 702 + 69 = 1138; 229 + 470 + 48 = 747. The pooled 65.6% is over the line only because H2 and H3 carry H1; per passage, H1 is under it. The lenient count (sensitivity only: a long word with two slips scored as two E) gives 837/1138 = 73.6%.

By line:

| line | passage | S | E | N | letters | S share | ? signs |
|---|---|---|---|---|---|---|---|
| L01 | H1 | 29 | 0 | 9 | 38 | 76.3% | 1 |
| L02 | H1 | 29 | 2 | 5 | 36 | 80.6% | 1 |
| L03 | H1 | 21 | 0 | 17 | 38 | 55.3% | 1 |
| L04 | H1 | 30 | 5 | 0 | 35 | 85.7% | 0 |
| L05 | H1 | 22 | 4 | 6 | 32 | 68.8% | 1 |
| L06 | H1 | 12 | 0 | 0 | 12 | 100.0% | 0 |
| L07 | H1 | 4 | 0 | 9 | 13 | 30.8% | 0 |
| L08 | H1 | 21 | 3 | 8 | 32 | 65.6% | 1 |
| L09 | H1 | 16 | 2 | 11 | 29 | 55.2% | 0 |
| L10 | H1 | 14 | 0 | 17 | 31 | 45.2% | 0 |
| L11 | H1 | 18 | 2 | 15 | 35 | 51.4% | 0 |
| L12 | H1 | 13 | 1 | 22 | 36 | 36.1% | 0 |
| L00 | H2 | 10 | 1 | 0 | 11 | 90.9% | 0 |
| L01 | H2 | 29 | 1 | 0 | 30 | 96.7% | 1 |
| L02 | H2 | 22 | 3 | 9 | 34 | 64.7% | 0 |
| L03 | H2 | 11 | 1 | 21 | 33 | 33.3% | 0 |
| L04 | H2 | 20 | 0 | 12 | 32 | 62.5% | 0 |
| L05 | H2 | 19 | 1 | 5 | 25 | 76.0% | 3 |
| L06 | H2 | 9 | 0 | 24 | 33 | 27.3% | 0 |
| L07 | H2 | 14 | 1 | 16 | 31 | 45.2% | 0 |
| L08 | H2 | 19 | 1 | 19 | 39 | 48.7% | 0 |
| L09 | H2 | 10 | 0 | 23 | 33 | 30.3% | 0 |
| L10 | H2 | 30 | 1 | 0 | 31 | 96.8% | 0 |
| L11 | H2 | 17 | 3 | 18 | 38 | 44.7% | 0 |
| L12 | H2 | 24 | 3 | 7 | 34 | 70.6% | 0 |
| L13 | H2 | 28 | 0 | 7 | 35 | 80.0% | 0 |
| L14 | H2 | 27 | 3 | 0 | 30 | 90.0% | 0 |
| L15 | H2 | 11 | 2 | 0 | 13 | 84.6% | 1 |
| L16 | H2 | 14 | 2 | 0 | 16 | 87.5% | 0 |
| L17 | H2 | 26 | 2 | 8 | 36 | 72.2% | 0 |
| L18 | H2 | 33 | 1 | 0 | 34 | 97.1% | 0 |
| L19 | H2 | 30 | 0 | 5 | 35 | 85.7% | 0 |
| L20 | H2 | 8 | 1 | 21 | 30 | 26.7% | 0 |
| L21 | H2 | 29 | 2 | 4 | 35 | 82.9% | 0 |
| L22 | H2 | 30 | 1 | 3 | 34 | 88.2% | 0 |
| P3 | H3 | 19 | 1 | 17 | 37 | 51.4% | 0 |
| P4 | H3 | 29 | 2 | 1 | 32 | 90.6% | 0 |

Error patterns in the decode, as the judge's session reported them [stated], with examples from `DECODE.txt` and, in brackets, what the clear copy has:

- the sign `1` (b in the key) where the sense wants a: fundbenta (fundamenta), gbudis (gaudio), grbait (gratia), gestbtum (gestatum);
- r or rr for te or i: parr (parte), anr (ante), monr (monte), prrmum (primum), imprrme (imprime);
- irr for the Xri abbreviation of Christi (`X~ Tk Cl`, five times in H1), and irrstiana (`X Tk Cl ...`) for christiana;
- c for h: pcilosopcu (philosophus), pcanta (phantasmata);
- a word-final t decoded as n: portan (portat), concilian (conciliat).

Two of these match the key leaf [derived, not checked on the image]: the final t is the sign Lmt, recovered as an and at on the leaf (portat, conciliat); and the leaf gives Tk Cl as ri, so `X~ Tk Cl` reads X-ri, the usual abbreviation of Christi, and prrmum reads primum. The leaf's te sign, a dash with a short down-tick at its right end, is close in shape to Tk (r), and may be the sign at the end of parr, anr and monr.

Clear copy, letters reproduced (`score/score_clear_out.txt`, Levenshtein, abbreviations of the clear copy expanded) [measured]:

| passage | clear counterpart | clear letters | matched | share |
|---|---|---|---|---|
| H1 | f. 109v (one passage) | 425 | 311 | 73.2% |
| H2 | f. 167r (line for line) | 733 | 616 | 84.0% |
| H3 | f. 123r | 73 | 61 | 83.6% |
| all | | 1,231 | 988 | 988/1,231 = 80.3% |

Sums: 425 + 733 + 73 = 1,231; 311 + 616 + 61 = 988. With the clear copy's expansions left out: H1 74.2%, H2 85.3%, H3 83.6%. Identical words in order: H1 33 of 76 (43.4%), H2 59 of 138 (42.8%), H3 8 of 14 (57.1%) (`score/worddiff_out.txt`). In-sample fit on the training leaves, not a held-out figure: 1,487 of 1,603 clear letters (92.8%, `score/train_fit_out.txt`).

Shuffle control (`score/shuffle_out.txt`), seed 20261112; seed 7 gives the same counts and z within 0.5 [measured]:

| statistic | real key | shuffled keys, mean (sd) | best shuffle | z | shuffles at or above real |
|---|---|---|---|---|---|
| la-letters model, all held out (per character) | -3.195 | -6.084 (0.409) | -4.821 | 7.1 | 0 / 5,000 |
| la-letters, H1 | -3.499 | -6.052 (0.442) | -4.612 | 5.8 | 0 / 5,000 |
| la-letters, H2 | -3.035 | -6.112 (0.426) | -4.902 | 7.2 | 0 / 5,000 |
| la-letters, H3 | -3.403 | -6.034 (0.504) | -4.011 | 5.2 | 0 / 5,000 |
| clear-copy match, all held out | 0.803 | 0.300 (0.037) | 0.448 | 13.7 | 0 / 5,000 |
| clear-copy match, H1 | 0.732 | 0.307 (0.035) | 0.466 | 12.1 | 0 / 5,000 |
| clear-copy match, H2 | 0.840 | 0.299 (0.042) | 0.467 | 13.0 | 0 / 5,000 |
| clear-copy match, H3 | 0.836 | 0.271 (0.053) | 0.479 | 10.6 | 0 / 5,000 |

Statistical validation (`docs/_validate.py baselanv9 --write`, 25 Nov 2026, model `la`, order 4 without spaces; `validation.tsv`) [measured]: 1,024 read tokens, 49 types; the reading scores -2.639 per letter; random keys of the same structure -4.459 (sd 0.366, z 5.0, n 200); a key annealed onto shuffled ciphertext at best -2.782 (mean -2.817, z 6.5); **verdict: pass**. The annealer started from random keys on the real text reaches -2.553, higher than the reading: the letter model alone does not single out this key. `validation.tsv` was made here from the frozen key and the transcriptions, and reproduces `DECODE.txt` on 37 of 37 lines.

Lexicon check, a mechanical pointer and not the judge (`score/lexcheck_out.txt`): decoded letters in words of the shared Latin lexicon H1 30.8%, H2 44.0%, H3 36.2%, against 79.8%, 77.1% and 54.8% for the clear copy.

## Reading and translation

This section is about the first pass. The pass-4 and pass-5 readings and translations, one file each per pass with every text and rim as its own section, are `reading_pass4.md`, `translation_pass4.md`, `reading_pass5.md` and `translation_pass5.md` (28 Nov 2026; see "States per text").

`reading.md` gives the three passages as the decode with the judge's word tags marked: word(?) for a one-letter slip, [?word] for a word with no sense, [?] for a sign with no key value; no letter is changed or supplied, only capitals and punctuation are added [measured: a script checked the marked words against `DECODE.txt` and the tags, 77, 133 and 15 words]. `translation.md` gives the English, with each passage's clear copy translated beside it for comparison. Both were made by Claude Opus 5.5 for the contributor, after the clear copy had been seen, and are **unchecked** by a person or a Latinist [unverified].

Read share by words (`research/reading_audit/v10_relabel.measure_text`) [measured]: H1 35/77 = 0.455, H2 70/133 = 0.526, H3 8/15 = 0.533, all 113/225 = 0.502. `docs/_check_reading.py` finds no clean sentence (H1 0 of 7, H2 0 of 11, H3 0 of 2). Holes stand in every sentence, so under README Conventions ("A reading must read") each passage is **decoded, not read**, and the target is filed not read with the method that obtained the key. The contributor's working class was "read in part" [stated]; it is not used here because the passages do not build clean sentences.

What the passages say, from the decode and the clear copy [unverified]: H1 ends one conjuration and opens another ("Alia coniuratio"), adjuring the spirits by the teachings of the faith, the saints and the life of Christ (Annunciation, coming, Nativity, circumcision, baptism, fast, Transfiguration on Mount Tabor). H2 gives the seal of Jupiter: cast in English tin on a day of Jupiter when the Moon enters Libra, with the planet's figure on one face and a priest-philosopher with a book on the other, kept in sky-blue silk; carried, it wins love, grace and favour, increases fortune and frees its bearer from fear. H3: the bearer will fear neither the devil nor phantoms, and will not perish in arms; the decode has a hole where "non" stands, so pentacle 4 read as decoded says the opposite.

## Prior art

`PRIOR_ART.md` (copied unchanged), searched 24 Nov 2026 before any transcription: Cyphersolver issues and issue bodies, the repository (catalogue, leads, COVERAGE), DECODE public search, web searches in English, German and Danish, Klaus Schmeh's list of encrypted books, the Clavicula literature (web only), Steinmann's description and the swisscollections record. **No reading, edition or study of the cipher was found.** The catalogue itself names the clear copy and the key leaves.

Checked again for this pull request (25 Nov 2026) in the issue and PR lists (`issues_index.tsv`, 931 lines; `issues_bodies.tsv`, 210 lines): `AN V 9`, `AN V9`, `ANV9`, `AN_V_9`, `AN-V-9`, `Clavicula`, `e-manuscripta`, `185551`, `Septem sigilla`, `Salomon`, `Solomon`, `UBH`, `magic`, `grimoire`: 0 lines each. `Basel`: 3 lines in the bodies, all the word "baseline" (#843, #736, #96). `AN V` without the 9 matches only other words (Christian V, Kristian V, an V). `conjur` matches #786, the Philadelphia MS 10a 132 love charm, another manuscript [measured].

Not checked: Skinner and Rankine, The Veritable Key of Solomon (2008), and Mathers (1889) in print; Boudet's census of Clavicula manuscripts in full; HathiTrust and Google Books full text. For the prior-art sheet: "Clavicula Salomonis" with "Basel" or "K IV 19"; "Septem sigilla planetarum" with "Geheimschrift".

## Not in the catalogue (not edited here)

- A new target: no entry in `catalogue.json` or `research/leads.json` names this volume (PRIOR_ART.md; checked again on upstream main of 24 Nov 2026, db86b487e: `AN V 9`, `Clavicula`, `5353221`, `185551`, `Septem sigilla` 0 hits; the `e-manuscripta` and `Basel` hits are other items). `catalogue.json` is not edited in this pull request.
- If it is entered as a lead or catalogue item, the vetting rule's `vetting.key_in_volume` applies: the key is in the volume (f. 99r, German translation f. 98r) and was tested here, after the decode, against the recovered key. Under the 3 Nov 2026 rule a key in the volume does not block a lead with no known decipherment; the clear copy in the same volume should be recorded beside it.

## Pass 2: the volume's key leaf (a separate result, read with known key)

Asked for by Dan Bourdeau on PR #957 (25 Nov 2026). Everything is in `keyleaf/`; the first pass above stays the figure of record and none of its files changed. **No person has checked any part of pass 2: not the key-leaf transcription, not the sign readings, not the pentacle transcription, not the decode.** Times are UTC from `keyleaf/RUN_RECORD.tsv`.

What was done, in order [measured: `keyleaf/RUN_RECORD.tsv`]:

1. The key leaf f. 99r and its German translation f. 98r, the 22 pentacle pages ff. 33r-54r, f. 97r-v and the clear pentacle pages f. 123r-v were fetched at full size by plain GET from the IIIF endpoint (`keyleaf/IMAGE_FETCH.tsv`: URL, UTC, HTTP status, md5; 37 images, all HTTP 200; no images committed).
2. `keyleaf/KEY_LEAF.tsv` was built from the leaf only (03:17): 73 sign values, 5 two-sign pairs (re, ri, ti, tr, rt), 2 whole-word forms (enim, autem) and 6 rules, with the leaf's Danish and the German quoted for each rule. New shapes on the leaf got labels in `keyleaf/SIGNS_KEYLEAF.md`, written before any pentacle was transcribed; a new mark `*` records the dot inside a sign. The leaf's two-dot rule reads "bemercker den bogstaff som staar nest for med en prick mitt udi" (it marks the letter standing next before with a dot in its middle; German f. 98r: "welcher nächst vorher stehet wo mitten darinnen sich ein Pünktchen befindet"), example ambulare; ".:" marks "den samme bogstab, naar dett mere er repetirit", example judicabitur [our reading of the hands, unverified].
3. The 8 first-pass `?` signs were looked at on the full-size images (03:20; see Transcription doubts; `keyleaf/SIGNS8.md`, crops not committed). The changes go only into the copies in `keyleaf/tx2/`, listed in `keyleaf/tx2/CHANGES.tsv` (6 lines changed). In pass 2 the placeholder `?` has no value.
4. The pentacle rims ff. 35r-51r (first series nos. 11-110) were unwrapped from the full-size images (`keyleaf/scripts/circles.py` finds the red rings, `keyleaf/scripts/unwrap2.py` unwraps them) and transcribed sign by sign into `keyleaf/tx/PENTACLES.txt`: **62 rims carry a cipher inscription**; 36 are blank or carry crosses only, 1 (no. 88) is in ordinary Latin capitals and 1 (no. 104) has ordinary script inside, so 100 = 62 + 38 [measured: 62 data lines and 38 comment lines for nos. 11-110]. Nos. 1-10 are out of scope: their clear text is on f. 123r-v.
5. Freeze before decoding: `keyleaf/FREEZE_PENT.txt` (03:33:21) hashes the key, the sign files, the transcriptions, the decoder and the judge brief; stamped at once by RFC 3161 (Sectigo 03:33:25, FreeTSA 03:33:26; `keyleaf/stamps/`), committed and pushed as b8cce3928 before the decode ran.
6. One decode (03:34) with `keyleaf/scripts/decode_keyleaf.py`: `keyleaf/DECODE_KEYLEAF.txt`, no emendation. **Declared fallback** (in the frozen decoder): the transcriptions record an inner dot only where it was seen, and the first-pass files never do, so where no earlier sign in the word carries `*` the two-dot sign takes the letter of the nearest preceding lambda, box or x (the three signs `SIGNS.md` notes as often dotted); ".:" repeats the letter the last ".." of the word took.
7. Shuffle control (03:37-03:40, `keyleaf/scripts/shuffle_keyleaf.py`): the leaf's 73 sign values permuted among its 73 signs, 5,000 keys at each of seeds 20261112 and 7, la-letters model (corpus sha256 asserted), per section and per pentacle.
8. Separate judge (03:43:24): the solver session could not start one itself (the headless CLI returned an authentication error, `keyleaf/RUN_RECORD.tsv` step 4), so the caller launched it: Claude Opus 5.5 (`claude-opus-5-5`), effort not exposed by the surface, an agent with its own context inside session https://claude.ai/code/session_01P5UF3myhVjFtgU9vTMj1qn, given only `keyleaf/judge/BRIEF.txt` (frozen, sha256 af20815f...) and `keyleaf/judge/decode.txt` (sha256 41b28e8b..., the same as `DECODE_KEYLEAF.txt`). Output `keyleaf/judge/JUDGE_OUT.tsv` (per word S/E/N tags and per-line counts) and `keyleaf/judge/JUDGE_SUMMARY.md`. Its separation from the solver is stated, not shown: it ran in the same session as the solver.

### Separate judge's scores (pass 2)

Strict, letters, S/(S+E+N), from `keyleaf/judge/JUDGE_OUT.tsv`. The judge's totals were recomputed here by a script from its 144 per-line rows (full arithmetic below) and agree on every section [measured].

| section | lines | S | E | N | [?] words | arithmetic | S share | 65% line |
|---|---|---|---|---|---|---|---|---|
| TRAIN f. 4r | 20 | 600 | 17 | 86 | 16 | 600/(600+17+86) = 600/703 | 85.35% | training, not a test |
| TRAIN f. 4v | 25 | 732 | 19 | 102 | 12 | 732/(732+19+102) = 732/853 | 85.81% | training, not a test |
| H1, f. 15r lines 1-12 | 12 | 237 | 15 | 130 | 5 | 237/(237+15+130) = 237/382 | 62.04% | **under: failed** |
| H2, f. 159r | 23 | 510 | 25 | 182 | 7 | 510/(510+25+182) = 510/717 | 71.13% | over |
| H3, f. 34r, pentacle 3 | 1 | 19 | 1 | 16 | 1 | 19/(19+1+16) = 19/36 | 52.8% | **under: failed** |
| H3, f. 34r, pentacle 4 | 1 | 32 | 1 | 0 | 0 | 32/(32+1+0) = 32/33 | 97.0% | over |
| H3 as one section | 2 | 51 | 2 | 16 | 1 | 51/(51+2+16) = 51/69 | 73.91% | not used: it hides pentacle 3 |
| pentacle rims, first series (62) | 62 | 2221 | 48 | 251 | 26 | 2221/(2221+48+251) = 2221/2520 | 88.13% | 57 over, 5 under (below) |
| all | 144 | 4351 | 126 | 767 | 67 | 4351/(4351+126+767) = 4351/5244 | 82.97% | pool, not used for any class |

Sums: lines 20 + 25 + 12 + 23 + 2 + 62 = 144; S 600 + 732 + 237 + 510 + 51 + 2221 = 4351; E 17 + 19 + 15 + 25 + 2 + 48 = 126; N 86 + 102 + 130 + 182 + 16 + 251 = 767; letters 703 + 853 + 382 + 717 + 69 + 2520 = 5244 [measured].

**Under the 65% line, stated plainly:** H1 (62.04%), H3 pentacle 3 (52.8%) and five pentacle rims: S1-025 11/26 = 42.3%, S1-039 27/44 = 61.4%, S1-070 25/42 = 59.5%, S1-071 23/37 = 62.2%, S1-096 23/40 = 57.5%. These are failed, and no pooled figure is used to carry them. The other 57 rims are at or over 65% (per rim in the table below).

The judge's rules, as it states them (`keyleaf/judge/JUDGE_SUMMARY.md`) [stated]: two letters swapped in a word (surgesn, obedietn, uenietn, treumnt) count as two slips and so N, and this recurring pattern carries much of the N; a word broken at a line end without "=" was not joined, since the brief allows only "=" joins (cogno|scu, po|tui, omni|um, opu|sculo, scored N). Joined, those breaks give 4377/5244 = 83.47% overall (f. 4r 612/703 = 87.06%, f. 4v 746/853 = 87.46%); no section moves across the 65% line either way, and the strict figures above are the ones used.

`docs/_check_reading.py` (upstream main 9600ed9ad, fetched 25 Nov 2026 03:48 UTC), run on each pass-2 section of `DECODE_KEYLEAF.txt` (one sentence per rim for the pentacles), finds clean sentences: pentacle rims 23 of 62 (clean share 0.371; 17 of 62 = 0.274 with Latin forced), H1 0 of 7, H2 0 of 11, H3 pentacle 3 0 of 1, pentacle 4 0 of 1, f. 4r 1 of 12, f. 4v 1 of 14; the whole file 6 of 113 (0.053) [measured]. Every section is under the checker's 0.45 MARGINAL bar (holes in most sentences), so the checker does **not** allow "read in part" wording for any part of pass 2: each section stays "decoded, not read".

**Class proposal for pass 2** (for the maintainers to decide; the first pass stays the figure of record and is unchanged): method "read with known key" (the volume's own key leaf) for the units that clear 65% on their own: H2 (71.13%), H3 pentacle 4 (97.0%) and the 57 rims at or over 65%. Shown as failed, never pooled: H1, H3 pentacle 3 and rims S1-025, S1-039, S1-070, S1-071, S1-096. The training leaves ff. 4r-4v are not a test and get no class. There is no H4 section in pass 2. Under `_check_reading.py` every one of these units is "decoded, not read", so no "read" or "read in part" state is claimed.

Exposure, stated plainly: the transcriber of the pentacles knew the key leaf and the first-pass key, so the shapes were recognised as letters while transcribing; in places the expected Latin will have steered the choice between similar shapes (named in the pentacle transcription only where a doubt was noticed). None of the pass-2 figures is a held-out figure, and nothing in pass 2 is called held-out: H1-H3 were decoded with the first-pass key before and their text was seen then, and the training leaves ff. 4r-4v were used to build the first-pass key and transcribed beside the clear copy, so their 85% is not a test. No person has checked any part of pass 2, judge included.

Decoded letters [measured: `keyleaf/work/decode_keyleaf_counts.txt`]: training leaves ff. 4r-4v 703 + 853 = 1,556 (28 signs with no value); H1 382 (5); H2 717 (7); H3 69 (1); pentacles 2,520 (26). The pass-2 decode of H1-H3 still carries the first pass's transcription faults (the sign `1` where the sense wants a, for instance), because only the 8 `?` signs were re-read.

Shuffle control [measured: `keyleaf/work/shuffle_keyleaf_out.txt`], per-character log-probability, real key against 5,000 shuffled keys:

| section | real | shuffles, mean (sd), seed 20261112 | best shuffle | z (seed 20261112 / 7) | shuffles >= real (both seeds) |
|---|---|---|---|---|---|
| training ff. 4r-4v | -2.340 | -5.902 (0.377) | -4.813 | 9.5 / 9.3 | 0/5000, 0/5000 |
| H1 | -3.075 | -5.877 (0.430) | -4.427 | 6.5 / 6.4 | 0/5000, 0/5000 |
| H2 | -2.860 | -6.010 (0.420) | -4.802 | 7.5 / 7.4 | 0/5000, 0/5000 |
| H3 | -3.029 | -5.936 (0.469) | -4.094 | 6.2 / 6.0 | 0/5000, 0/5000 |
| pentacles, 62 rims | -2.063 | -5.996 (0.373) | -4.788 | 10.5 / 10.3 | 0/5000, 0/5000 |

Every one of the 62 pentacles is 0/5000 at both seeds; the lowest z is 4.1 (S1-025) at both. This shows the leaf's key is far better than chance on each rim; it does not show that a rim reads.

Mechanical lexicon pointer (not the judge; `keyleaf/work/lexcheck_keyleaf.tsv`): letters in words of the shared Latin lexicon, pentacles 1,597 of 2,520 (63.4%), training 892/1,556 (57.3%), H1 164/382 (42.9%), H2 340/717 (47.4%), H3 28/69 (40.6%); 30 of the 62 pentacles are under 65% on this pointer. The lexicon lacks many inflected and magical forms, so this is a floor, not a read share.

Per pentacle (decode as produced; no emendation; letters a-z; z and shuffle counts from `keyleaf/work/shuffle_keyleaf_out.txt`; the last two columns are the separate judge's strict scores from `keyleaf/judge/JUDGE_OUT.tsv`, and each rim's S+E+N equals its letters column [measured]):

| pentacle | folio (canvas) | decode (pass 2, no emendation) | letters | in lexicon (pointer) | z, seed 20261112 / 7 | shuffles >= real, both seeds | judge S/E/N | judge S/(S+E+N) |
|---|---|---|---|---|---|---|---|---|
| S1-011 | f. 35r (c073) | portanti nullum uulnus lethale fieri potest | 38 | 23 (60.5%) | 6.8 / 6.8 | 0/5000, 0/5000 | 38/0/0 | 38/38 = 100.0% |
| S1-012 | f. 35r (c073) | dat bonam fortunam et morbotus pericula tollit | 40 | 32 (80.0%) | 6.7 / 6.8 | 0/5000, 0/5000 | 32/0/8 | 32/40 = 80.0% |
| S1-013 | f. 35r (c073) | huic omns furiae obedietn atque potentiae ifernales | 45 | 18 (40.0%) | 5.1 / 5.0 | 0/5000, 0/5000 | 35/2/8 | 35/45 = 77.8% |
| S1-014 | f. 35r (c073) | neine praetet creatore [?] deum timebit | 31 | 12 (38.7%) | 5.5 / 5.5 | 0/5000, 0/5000 | 25/1/5 | 25/31 = 80.6% |
| S1-015 | f. 36r (c075) | huic obedietn omnes spiritus et potentiae infernales | 46 | 28 (60.9%) | 7.0 / 6.7 | 0/5000, 0/5000 | 38/0/8 | 38/46 = 82.6% |
| S1-016 | f. 36r (c075) | obedietn tibit omnes creatuae et potentiae infernales | 47 | 16 (34.0%) | 6.8 / 6.6 | 0/5000, 0/5000 | 37/2/8 | 37/47 = 78.7% |
| S1-017 | f. 36r (c075) | contra inimicos serpentes et ua[?]mones tutissimum | 42 | 25 (59.5%) | 6.7 / 6.7 | 0/5000, 0/5000 | 42/0/0 | 42/42 = 100.0% |
| S1-018 | f. 36r (c075) | hoc signum portauit adam in fronte contra pericula | 43 | 43 (100.0%) | 7.8 / 7.9 | 0/5000, 0/5000 | 43/0/0 | 43/43 = 100.0% |
| S1-019 | f. 36r (c075) | ad sanguuinus fluxum respringendum optimum remedium | 46 | 23 (50.0%) | 6.2 / 6.0 | 0/5000, 0/5000 | 35/1/10 | 35/46 = 76.1% |
| S1-020 | f. 36r (c075) | furta reuelat conspirationes et secreta consilia hominum | 50 | 29 (58.0%) | 8.0 / 7.9 | 0/5000, 0/5000 | 50/0/0 | 50/50 = 100.0% |
| S1-021 | f. 37r (c077) | canitar~ confert et singularem fortunae gratiam | 41 | 34 (82.9%) | 8.3 / 8.5 | 0/5000, 0/5000 | 34/0/7 | 34/41 = 82.9% |
| S1-022 | f. 37r (c077) | deuu mihi adiutor quem tinebo et uiuam | 32 | 22 (68.8%) | 5.8 / 5.8 | 0/5000, 0/5000 | 30/2/0 | 30/32 = 93.8% |
| S1-025 | f. 37r (c077) | p[?]m[?] cou odium et magii[?]ines uerit | 26 | 8 (30.8%) | 4.1 / 4.1 | 0/5000, 0/5000 | 11/1/14 | 11/26 = 42.3% **under 65%** |
| S1-027 | f. 38r (c079) | hoc signum tecum sit et n~ timebus aduersarios | 38 | 30 (78.9%) | 7.2 / 7.0 | 0/5000, 0/5000 | 37/1/0 | 37/38 = 97.4% |
| S1-028 | f. 38r (c079) | quo die hoc signum uiderus liber erus ab [?]ipediment | 42 | 22 (52.4%) | 6.0 / 5.9 | 0/5000, 0/5000 | 40/2/0 | 40/42 = 95.2% |
| S1-030 | f. 38r (c079) | per hoc nomen treumnt omnes potestates infernales [?] | 43 | 16 (37.2%) | 6.4 / 6.3 | 0/5000, 0/5000 | 36/0/7 | 36/43 = 83.7% |
| S1-031 | f. 38r (c079) | hoc signum faciet omnes erga te mites et ben[?]uolos | 41 | 36 (87.8%) | 7.2 / 7.0 | 0/5000, 0/5000 | 41/0/0 | 41/41 = 100.0% |
| S1-032 | f. 38r (c079) | huic signo se subi[?]unt omnes creatuae uanimuque uiren | 45 | 20 (44.4%) | 5.5 / 5.5 | 0/5000, 0/5000 | 30/1/14 | 30/45 = 66.7% |
| S1-033 | f. 39r (c081) | nec a gladio nec a subitania morte tinebius | 36 | 19 (52.8%) | 5.7 / 5.6 | 0/5000, 0/5000 | 27/1/8 | 27/36 = 75.0% |
| S1-037 | f. 39r (c081) | cum hoc signo n~ peribis ferro nec igne | 31 | 23 (74.2%) | 5.3 / 5.1 | 0/5000, 0/5000 | 31/0/0 | 31/31 = 100.0% |
| S1-038 | f. 39r (c081) | omne timoris occasione auerti et conuerti | 36 | 30 (83.3%) | 6.6 / 6.5 | 0/5000, 0/5000 | 34/2/0 | 34/36 = 94.4% |
| S1-039 | f. 40r (c083) | contra maleficia et quemacunque praestigiau terla | 44 | 17 (38.6%) | 6.6 / 6.6 | 0/5000, 0/5000 | 27/1/16 | 27/44 = 61.4% **under 65%** |
| S1-041 | f. 40r (c083) | hoc signum facit contra s[?]tena uim et potestat[?] | 38 | 26 (68.4%) | 6.8 / 6.9 | 0/5000, 0/5000 | 38/0/0 | 38/38 = 100.0% |
| S1-044 | f. 40r (c083) | hoc signo sigilauit salomon da[?]mone in puteo | 37 | 14 (37.8%) | 5.7 / 5.7 | 0/5000, 0/5000 | 37/0/0 | 37/37 = 100.0% |
| S1-045 | f. 41r (c085) | contra metum et tiiore hoc signum habet efficaciam | 43 | 37 (86.0%) | 6.8 / 6.7 | 0/5000, 0/5000 | 37/0/6 | 37/43 = 86.0% |
| S1-049 | f. 41r (c085) | quicunque hoc signum portat diliget ab omnibus | 40 | 33 (82.5%) | 7.5 / 7.3 | 0/5000, 0/5000 | 33/0/7 | 33/40 = 82.5% |
| S1-051 | f. 42r (c087) | amabile facit tanquam ipsum deum et odium diurumpit | 44 | 28 (63.6%) | 6.3 / 6.4 | 0/5000, 0/5000 | 43/1/0 | 43/44 = 97.7% |
| S1-052 | f. 42r (c087) | pro imoris onfficina adirabale est hoc signum | 39 | 15 (38.5%) | 5.6 / 5.6 | 0/5000, 0/5000 | 28/2/9 | 28/39 = 71.8% |
| S1-055 | f. 42r (c087) | pro auxilio impetrando hoc signum bonum est | 37 | 27 (73.0%) | 7.2 / 7.2 | 0/5000, 0/5000 | 37/0/0 | 37/37 = 100.0% |
| S1-057 | f. 43r (c089) | a periculis liberabiit qui hoc signum gestat | 38 | 28 (73.7%) | 7.6 / 7.6 | 0/5000, 0/5000 | 37/1/0 | 37/38 = 97.4% |
| S1-063 | f. 44r (c091) | uulnera qque dei sunt medicina mei amen | 33 | 29 (87.9%) | 4.6 / 4.6 | 0/5000, 0/5000 | 29/0/4 | 29/33 = 87.9% |
| S1-064 | f. 44r (c091) | timor deus et totius mundi sancta mabiestus | 37 | 28 (75.7%) | 5.3 / 5.2 | 0/5000, 0/5000 | 28/0/9 | 28/37 = 75.7% |
| S1-065 | f. 44r (c091) | contra area et hostes i bello signum optimum | 37 | 37 (100.0%) | 6.4 / 6.4 | 0/5000, 0/5000 | 32/1/4 | 32/37 = 86.5% |
| S1-069 | f. 45r (c093) | hoc signum bonum est ftra dolore matricos | 35 | 23 (65.7%) | 6.3 / 6.3 | 0/5000, 0/5000 | 30/1/4 | 30/35 = 85.7% |
| S1-070 | f. 45r (c093) | contra uen[?]num est et mobtus incidenidia remedium | 42 | 25 (59.5%) | 5.3 / 5.2 | 0/5000, 0/5000 | 25/0/17 | 25/42 = 59.5% **under 65%** |
| S1-071 | f. 45r (c093) | portatum facit ftra inimicos et insidiator | 37 | 15 (40.5%) | 6.0 / 6.0 | 0/5000, 0/5000 | 23/0/14 | 23/37 = 62.2% **under 65%** |
| S1-072 | f. 45r (c093) | cum hoc signo in carcere detineri n~ potes | 34 | 25 (73.5%) | 6.2 / 6.0 | 0/5000, 0/5000 | 34/0/0 | 34/34 = 100.0% |
| S1-073 | f. 45r (c093) | contra mortus repentinae periculum optimum est | 41 | 35 (85.4%) | 7.8 / 7.6 | 0/5000, 0/5000 | 40/1/0 | 40/41 = 97.6% |
| S1-074 | f. 45r (c093) | hoc signum animum et animam confortat aduersus peric[?] | 45 | 31 (68.9%) | 7.8 / 7.7 | 0/5000, 0/5000 | 45/0/0 | 45/45 = 100.0% |
| S1-078 | f. 46r (c095) | mulier cum hoc signo n~ peribit in partu | 32 | 24 (75.0%) | 6.0 / 6.0 | 0/5000, 0/5000 | 32/0/0 | 32/32 = 100.0% |
| S1-079 | f. 46r (c095) | porta tecum hoc signum et inimici tus er[?] imore cedetn | 44 | 31 (70.5%) | 5.6 / 5.5 | 0/5000, 0/5000 | 32/1/11 | 32/44 = 72.7% |
| S1-080 | f. 46r (c095) | qui hoc signum habet a nemine laedi potest amen | 39 | 34 (87.2%) | 7.3 / 7.0 | 0/5000, 0/5000 | 39/0/0 | 39/39 = 100.0% |
| S1-081 | f. 47r (c097) | hoc sinum est contra omnia phantasmata re[?]ia homine graitsum | 51 | 28 (54.9%) | 6.7 / 6.6 | 0/5000, 0/5000 | 37/2/12 | 37/51 = 72.5% |
| S1-082 | f. 47r (c097) | incdo cit amore et ben[?]uolentiam apud omnes | 36 | 22 (61.1%) | 6.5 / 6.5 | 0/5000, 0/5000 | 27/1/8 | 27/36 = 75.0% |
| S1-084 | f. 47r (c097) | portante ab aquae et mabrius periclo soluit | 37 | 22 (59.5%) | 5.7 / 5.6 | 0/5000, 0/5000 | 29/1/7 | 29/37 = 78.4% |
| S1-085 | f. 47r (c097) | ecc[?] figua agni dominantus super omnes potestates | 42 | 14 (33.3%) | 7.1 / 7.0 | 0/5000, 0/5000 | 40/2/0 | 40/42 = 95.2% |
| S1-087 | f. 48r (c099) | cum hoc signo n~ timebius inimicos nec maleficia nec da[?]mones | 50 | 34 (68.0%) | 6.5 / 6.3 | 0/5000, 0/5000 | 49/1/0 | 49/50 = 98.0% |
| S1-090 | f. 48r (c099) | in bello securus erus cum hoc signo | 29 | 25 (86.2%) | 5.7 / 5.8 | 0/5000, 0/5000 | 28/1/0 | 28/29 = 96.6% |
| S1-091 | f. 48r (c099) | ab inimicos nos tutos reddit et inuincibiles | 38 | 26 (68.4%) | 5.2 / 5.2 | 0/5000, 0/5000 | 37/1/0 | 37/38 = 97.4% |
| S1-092 | f. 48r (c099) | in quocunque die hoc signum portau[?] a periculo liber | 43 | 37 (86.0%) | 7.0 / 7.1 | 0/5000, 0/5000 | 43/0/0 | 43/43 = 100.0% |
| S1-095 | f. 49r (c101) | screptum in ca[?]te n~ nata et portatum manu leua indicit mirabalia | 53 | 21 (39.6%) | 6.6 / 6.6 | 0/5000, 0/5000 | 51/2/0 | 51/53 = 96.2% |
| S1-096 | f. 49r (c101) | ad honc signum uenietn spiritu et obedietn tibi | 40 | 21 (52.5%) | 5.0 / 4.9 | 0/5000, 0/5000 | 23/2/15 | 23/40 = 57.5% **under 65%** |
| S1-097 | f. 49r (c101) | hoc signum portabit aron in fronte et liberat ab igne | 44 | 25 (56.8%) | 6.7 / 6.6 | 0/5000, 0/5000 | 43/1/0 | 43/44 = 97.7% |
| S1-098 | f. 49r (c101) | contra morte subitaneam hoc signum est accommodatum | 45 | 35 (77.8%) | 8.1 / 8.1 | 0/5000, 0/5000 | 44/1/0 | 44/45 = 97.8% |
| S1-099 | f. 50r (c103) | cum hoc signo mo[?]te subitanea n~ peribius | 33 | 13 (39.4%) | 4.8 / 4.7 | 0/5000, 0/5000 | 32/1/0 | 32/33 = 97.0% |
| S1-102 | f. 50r (c103) | super aspidde et basiliscum ambulabis et conculcabis leone et dracone | 60 | 16 (26.7%) | 6.6 / 6.6 | 0/5000, 0/5000 | 58/2/0 | 58/60 = 96.7% |
| S1-103 | f. 50r (c103) | sacto columbo sacrum est hoc signum et confect uictoria | 47 | 35 (74.5%) | 7.0 / 7.0 | 0/5000, 0/5000 | 38/2/7 | 38/47 = 80.9% |
| S1-105 | f. 51r (c105) | ecc[?] figua et facies per quod omnia facta sunt cui omnes obedi[?] | 50 | 37 (74.0%) | 7.5 / 7.5 | 0/5000, 0/5000 | 49/1/0 | 49/50 = 98.0% |
| S1-106 | f. 51r (c105) | cum hoc signo nec uinculus nec compedibus teri potes | 44 | 22 (50.0%) | 6.6 / 6.5 | 0/5000, 0/5000 | 39/1/4 | 39/44 = 88.6% |
| S1-107 | f. 51r (c105) | signum sacti gregorii contra uen[?]num et maleficia | 42 | 29 (69.0%) | 6.8 / 6.9 | 0/5000, 0/5000 | 41/1/0 | 41/42 = 97.6% |
| S1-109 | f. 51r (c105) | hoc signo sanguine perd[?]e nemo potest tutum est | 39 | 39 (100.0%) | 6.2 / 6.1 | 0/5000, 0/5000 | 39/0/0 | 39/39 = 100.0% |
| S1-110 | f. 51r (c105) | qui hoc signum portauerit nulla pericula timebit | 42 | 25 (59.5%) | 7.6 / 7.5 | 0/5000, 0/5000 | 42/0/0 | 42/42 = 100.0% |
| all 62 | ff. 35r-51r | | 2520 | 1597 (63.4%) | 10.5 / 10.3 (section) | 0/5000, 0/5000 | 2221/48/251 | 2221/2520 = 88.13% (57 of 62 rims at or over 65%) |

Sum check: the 62 rows add to 2,520 letters and 1,597 lexicon letters [measured]. What the rims say, from the decode and unchecked [unverified]: protection and power formulas ("hoc signum portat ...", "contra maleficia ...", "cum hoc signo non peribis ..."), Ps 91:13 on no. 102 ("super aspidem et basiliscum ambulabis et conculcabis leonem et draconem"), Salomon sealing the demon in a well (no. 44), Adam and Aaron bearing the sign on the forehead (nos. 18, 97).

## Pass 3: H1 re-read, a fresh held-out passage H4 and 11 second-series rims (a separate result, read with known key)

A third pass of 25 Nov 2026, in `pass3/`. **The first pass above stays the figure of record** (65.6% pooled; H1 62.4%) and none of its files, and none of pass 2's, changed. Pass 3 does not replace either earlier figure: it is reported apart, with its own freeze, decode, judge and controls. **No person has checked any part of pass 3.** Times are UTC from `pass3/RUN_RECORD.tsv` and `pass3/RUN_RECORD_FOLLOWUP.tsv`.

**The figures, stated plainly** (letters, S/(S+E+N), separate judge's central call, `pass3/JUDGE_P3_RESULT.md`) [measured]:

- **H4, f. 25r lines 1-12, held out: 389/415 = 93.7% judged** (judge's range on its own doubtful calls 386/415 = 93.0% to 398/415 = 95.9%; the solver's own stricter count 379/415 = 91.3%). No word of H4 uses rule C4 or C5, so the figure is the same without them.
- **H1, f. 15r lines 1-12, re-read: 399/405 = 98.5% judged. H1 is NOT held out** in pass 3: it was decoded twice before, and the reader had seen its clear copy f. 109v before re-reading. With C4 and C5 switched off: 378/398 = 95.0% (364/398 = 91.5% if every changed word is counted N).
- **Second-series rims, 11 (ff. 52r-53r): 486/521 = 93.3% judged.** Ten rims are over the 65% line; **S2-05 is 4/17 = 23.5%, under: failed** (two names, caraton and mathoi, that the judge could not verify).
- Controls: 0/5000 at seeds 20261112 and 7 for H1r, H4, the rims as a section and each of the 11 rims (`pass3/CONTROL_P3.txt`).
- No pooled figure across the three units is given or used.

What was done, in order [measured: the two run records]:

1. Split written before the new page was fetched or viewed (07:44, `pass3/SPLIT_P3.md`): H1r = f. 15r lines 1-12 re-read, declared not held out and not blind; H4 = f. 25r lines 1-12 (the recto ten leaves after H1), never transcribed or decoded in passes 1 or 2, its clear counterpart not to be looked for before the decode.
2. Key v3 (`pass3/KEY_V3.tsv`, `pass3/RULES_V3.md`): the 73 token values, 5 pairs and 2 word forms of pass 2's `keyleaf/KEY_LEAF.tsv`, re-checked against the leaf image f. 99r; **no value changed** (73 of 73 token values the same, `pass3/checks/VERIFY_OUT.txt`). `KEY_V3.tsv` gives the evidence per value: the leaf's own entry, whether the leaf's drawing and the label's shape agree (69 exact, 4 probable: Cs, As, Lr, Ab) and a note. The decoder's rules changed in five declared places, C1 to C5 (below and `pass3/EMENDATIONS.md`).
3. Transcription (to 07:55): H1 re-read from the full-size image (`pass3/tx/f015r_p3.txt`), H4 from the full-size image of f. 25r fetched by plain GET (`pass3/tx/f025r_H4.txt`), and the rims of second-series pentacles nos. 2-12, ff. 52r-53r, from own polar unwraps (`pass3/tx/PENT_S2.txt`). One reader (Claude Fable 5.2, as the file headers state), who knows the key leaf, so no transcription here is shape-blind. Doubts written before the freeze: `pass3/DOUBTS_P3.md`.
4. Freeze (07:55:17, `pass3/FREEZE_P3.txt`): md5 and sha256 of the key, the rules, the decoder, the three transcriptions, the doubts, the split and the f. 25r image. **Unlike pass 2, this freeze was not time-stamped or pushed before the decode.** That the freeze came first rests on the run record and the hashes in the freeze file; the outside time-stamp (step 9) is later than the decode and the judging.
5. One decode (07:55:25, `pass3/scripts/run_decode.py`, which asserts the frozen hashes): `pass3/DECODE_P3.txt`. No emendation (`pass3/EMENDATIONS.md`).
6. Solver's own strict count and a clear-copy match for H1 (08:02, `pass3/SCORE_P3.tsv`); shuffle control (08:02, `pass3/scripts/control_p3.py`): the 73 token values permuted, 5,000 keys at each seed, own Latin letter 4-gram model on `la-latlib-letters.txt` (sha256 asserted), statistic log10 probability per character, per section and per rim.
7. Prior-art look for the rim formulas (08:03, `pass3/PRIOR_ART_P3.md`): two web searches found no page with the Basel wording; a genre parallel only (BL Stowe MS 16, pseudo-Solomonic amulet seals with "Hoc signum" captions). The printed Key of Solomon legends were not compared.
8. Separate judge (file time 08:05, `pass3/JUDGE_P3_RESULT.md`): given only `pass3/judge/BRIEF.txt` and `pass3/judge/decode.txt` (the same bytes as `DECODE_P3.txt`). It was launched by the calling session, not by the solver. **The judge's brief was written at 08:03, after the decode** (pass 2's was frozen before its decode). The judge's model and session are not recorded in its file [stated by the caller: an independent judge]; its separation from the solver is stated, not shown.
9. Variant without C4 and C5, declared at 08:07:22 and then run (`pass3/variant/`), and the time-stamp of the whole working folder (08:08:04, `pass3/stamps/`: RFC 3161 Sectigo and FreeTSA both granted on the first try, OpenTimestamps submitted and pending; 37 files in the manifest, 36 committed here and matching, the 37th a `__pycache__` file; the manifest's `./pr_prep/variant/` is `pass3/variant/` here).

### Per-unit figures (pass 3)

Judge's central call beside the solver's own count. Where they differ the solver's is the stricter. Lines of H1r and H4 were controlled as sections only.

| unit | decode (no emendation) | judge S/E/N | judge S/(S+E+N) | solver's own S/E/N | solver's own share | controls, seeds 20261112 / 7 |
|---|---|---|---|---|---|---|
| H1r L01 | et per omnia documenta quae~ in fide christiana sunt | 43/0/0 | 43/43 = 100.0% | 43/0/0 | 43/43 = 100.0% | section only |
| H1r L02 | instituta et per sactorum agmina quae~ agni imma= | 39/1/0 | 39/40 = 97.5% | 39/1/0 | 39/40 = 97.5% | section only |
| H1r L03 | culati sequuntur uestigia et per omnes sanctos | 40/0/0 | 40/40 = 100.0% | 40/0/0 | 40/40 = 100.0% | section only |
| H1r L04 | quos deus elegit ante mundi iacta fundamenta | 38/0/0 | 38/38 = 100.0% | 38/0/0 | 38/38 = 100.0% | section only |
| H1r L05 | et pmer eorum merita qui~ in gaudio et gratia | 35/1/0 | 35/36 = 97.2% | 35/1/0 | 35/36 = 97.2% | section only |
| H1r L06 | sunt apud deum | 12/0/0 | 12/12 = 100.0% | 12/0/0 | 12/12 = 100.0% | section only |
| H1r L07 | alia coniuratio | 14/0/0 | 14/14 = 100.0% | 14/0/0 | 14/14 = 100.0% | section only |
| H1r L08 | adiuro uos dimones in quacunque parte mundi | 36/1/0 | 36/37 = 97.3% | 36/1/0 | 36/37 = 97.3% | section only |
| H1r L09 | situs per annunciationem ch~ri per aduentum | 36/1/0 | 36/37 = 97.3% | 36/1/0 | 36/37 = 97.3% | section only |
| H1r L10 | ch~ri per natiuitatem ch~ri per circumci= | 33/0/0 | 33/33 = 100.0% | 33/0/0 | 33/33 = 100.0% | section only |
| H1r L11 | sionem et baptisum ch~ri per ieiunium et trans | 37/1/0 | 37/38 = 97.4% | 37/1/0 | 37/38 = 97.4% | section only |
| H1r L12 | figurationem ch~ri in monte tabor per atundi= | 36/1/0 | 36/37 = 97.3% | 31/0/6 | 31/37 = 83.8% | section only |
| **H1r, all** | | **399/6/0** | **399/405 = 98.5%** | 394/5/6 | 394/405 = 97.3% | 0/5000, 0/5000 (z 11.7 / 11.7) |
| H4 L01 | post hac sugit et aperit brachia sua ac si | 33/1/0 | 33/34 = 97.1% | 33/1/0 | 33/34 = 97.1% | section only |
| H4 L02 | uellet amplexari aere dicendo [?] | 25/1/0 | 25/26 = 96.2% | 26/0/0 | 26/26 = 100.0% | section only |
| H4 L03 | per nooen iestius libri et per omnes eius uirtu= | 37/2/0 | 37/39 = 94.9% | 31/1/7 | 31/39 = 79.5% | section only |
| H4 L04 | tes [?] tortuosi ne[?] deformes sed in oni man= | 31/1/0 | 31/32 = 96.9% | 29/1/2 | 29/32 = 90.6% | section only |
| H4 L05 | sueta forma ad nos ueniatis et per nomen et in | 37/0/0 | 37/37 = 100.0% | 37/0/0 | 37/37 = 100.0% | section only |
| H4 L06 | nomine adonai sabaoth emloo eloi sadai | 28/0/5 | 28/33 = 84.8% | 28/0/5 | 28/33 = 84.8% | section only |
| H4 L07 | iod he uau aleph tetragrammaton ineffabale | 36/1/0 | 36/37 = 97.3% | 36/1/0 | 36/37 = 97.3% | section only |
| H4 L08 | eius uidelichet qui est deus uirtut~um deus | 35/1/0 | 35/36 = 97.2% | 35/1/0 | 35/36 = 97.2% | section only |
| H4 L09 | exel[?]us deus ueus ter imsrael qui super t[?]= | 27/2/4 | 27/33 = 81.8% | 24/2/7 | 24/33 = 72.7% | section only |
| H4 L10 | rar gerum habitat et in coelo sedes eius | 25/0/8 | 25/33 = 75.8% | 25/0/8 | 25/33 = 75.8% | section only |
| H4 L11 | per nomen eius qui dixit et facta sunt et stare | 38/0/0 | 38/38 = 100.0% | 38/0/0 | 38/38 = 100.0% | section only |
| H4 L12 | fecit omnia et ipse super omnia dominatur et | 37/0/0 | 37/37 = 100.0% | 37/0/0 | 37/37 = 100.0% | section only |
| **H4, all** | | **389/9/17** | **389/415 = 93.7%** | 379/7/29 | 379/415 = 91.3% | 0/5000, 0/5000 (z 9.8 / 9.8) |
| S2 S2-02 | hoc signum triumphatoris dni~ nostri iesu ch~ri mesteriosum | 49/1/0 | 49/50 = 98.0% | 49/1/0 | 49/50 = 98.0% | 0/5000, 0/5000 (z 5.9 / 5.9) |
| S2 S2-03 | cum hoc signo erus gratus omnibus et fortunatus | 39/1/0 | 39/40 = 97.5% | 39/1/0 | 39/40 = 97.5% | 0/5000, 0/5000 (z 7.3 / 7.2) |
| S2 S2-04 | iesus autem trasiens per medium ipsorum abiit | 38/1/0 | 38/39 = 97.4% | 38/1/0 | 38/39 = 97.4% | 0/5000, 0/5000 (z 6.0 / 6.1) |
| S2 S2-05 | caraton amen mathoi | 4/0/13 | 4/17 = 23.5% **under** | 4/0/13 | 4/17 = 23.5% | 0/5000, 0/5000 (z 4.6 / 4.5) |
| S2 S2-06 | deposuit potentes de sede et exaltauit humiles | 40/0/0 | 40/40 = 100.0% | 40/0/0 | 40/40 = 100.0% | 0/5000, 0/5000 (z 6.5 / 6.4) |
| S2 S2-07 | hoc signum reddit hominem uirtuosum et a periculo defendit | 50/0/0 | 50/50 = 100.0% | 50/0/0 | 50/50 = 100.0% | 0/5000, 0/5000 (z 8.5 / 8.5) |
| S2 S2-08 | hoc est ineffabale nomen dei quo aron usus est in periculus | 47/2/0 | 47/49 = 95.9% | 47/2/0 | 47/49 = 95.9% | 0/5000, 0/5000 (z 6.2 / 6.3) |
| S2 S2-09 | ad amorem ingribe hos caracteres in crusta panis et praebe ad commedendum | 54/1/7 | 54/62 = 87.1% | 54/1/7 | 54/62 = 87.1% | 0/5000, 0/5000 (z 7.4 / 7.5) |
| S2 S2-10 | hoc signum in sinu aut uestibus portatum auget hominem gratia mirabala | 59/1/0 | 59/60 = 98.3% | 52/0/8 | 52/60 = 86.7% | 0/5000, 0/5000 (z 8.6 / 8.6) |
| S2 S2-11 | gribe hoc cum manu sinistra sanguine digiti tui die iouus in aurgento | 51/2/5 | 51/58 = 87.9% | 51/2/5 | 51/58 = 87.9% | 0/5000, 0/5000 (z 6.6 / 6.6) |
| S2 S2-12 | contra ligaturam positum in uestibus ligati statim liberabiutur | 55/1/0 | 55/56 = 98.2% | 44/0/12 | 44/56 = 78.6% | 0/5000, 0/5000 (z 8.1 / 8.0) |
| **S2, all** | | **486/10/25** | **486/521 = 93.3%** | 468/8/45 | 468/521 = 89.8% | 0/5000, 0/5000 (z 12.6 / 12.6) |

Sum checks [measured: `pass3/checks/mk_tables.py` asserts them]: the 12 lines of H1r add to 399/6/0 (405 letters), the 12 lines of H4 to 389/9/17 (415), the 11 rims to 486/10/25 (521); the solver's own rows add to 394/5/6, 379/7/29 and 468/8/45. Signs with no value: H1r 0, H4 5, rims 0.

Judge's range per unit, every doubtful call taken against and then for the decode: H1r 394/405 = 97.3% to 400/405 = 98.8%; H4 386/415 = 93.0% to 398/415 = 95.9%; rims 479/521 = 91.9% to 500/521 = 96.0% (S2-05 4/17 to 17/17, on whether the two names are accepted). The judge's note of "7 instances" of ch~ri is 6 in the decode (5 in H1r, 1 in S2-02); all are scored S either way, so no figure moves [measured: `pass3/checks/VERIFY_OUT.txt`].

H1r against the clear copy f. 109v, which does not depend on anyone's judgement: the decode matches 399 of 425 clear letters = 93.9% (pass 1: 80.3% over all three passages); without C4 and C5, 386 of 425 = 90.8% [measured: `pass3/SCORE_P3.tsv`, `pass3/checks/VERIFY_OUT.txt`]. H4 has not been compared with its clear copy.

### The C4 and C5 caveat

Two of the decoder's rules are **not on the key leaf**: C4 (`Cl Tq` = rte, by analogy with the leaf's rt and te) and C5 (the x is ch in the chi-rho-iota abbreviation, from Latin usage; the leaf says only that other abbreviations follow Latin custom). The judge could give no figure without them from its packet. The variant was therefore declared and run afterwards on the same frozen key and transcriptions, with the decoder changed in those two places only (`pass3/variant/VARIANT_DECLARED.md`, `make_variant.py`). It is not a first pass. Words the variant leaves alone keep the judge's central call; the changed words were called by the assembling session with the judge's brief, not by the judge, and a strict figure counts every changed word N [measured: `pass3/variant/SCORE_VARIANT.tsv`]:

| unit | judged, C4 and C5 on | no C4 | no C5 | no C4, no C5 | no C4, no C5, strict |
|---|---|---|---|---|---|
| H1r (re-read, not held out) | 399/405 = 98.5% | 398/404 = 98.5% | 379/399 = 95.0% | **378/398 = 95.0%** | 364/398 = 91.5% |
| H4 (held out) | 389/415 = 93.7% | 389/415 = 93.7% | 389/415 = 93.7% | **389/415 = 93.7%** | 389/415 = 93.7% |
| S2 rims | 486/521 = 93.3% | 486/521 = 93.3% | 484/520 = 93.1% | 484/520 = 93.1% | 482/520 = 92.7% |

Changed words: christiana becomes iristiana (N, two slips), parte becomes pa[?]te (S under the brief's rule for a word holding [?]; N in the strict column), ch~ri becomes i~ri five times in H1r and once in S2-02 (E, as pass 2's judge scored i~ri; N in the strict column). H4 is letter for letter the judged decode in all three variants. Lowest H1r line without C4 and C5: L01 33/42 = 78.6%. Every unit stays on the same side of the 65% line.

### Why H1 failed in passes 1 and 2

Transcription, not the key [derived: the key table is unchanged and 30 of the 80 word groups of H1 differ between pass 2's `keyleaf/tx2/f015r.txt` and `pass3/tx/f015r_p3.txt`]. At full size the lambda (a) is a thin leg with a thick hook; passes 1 and 2 often wrote it as `1` (b) or as `Lm 1` (a + b), which gave sabctorem, bgnia, gbudi, qubcuque. Nasal dots were put on the wrong sign, and the leaf's ligatures ia, io, tio, tia, ur, pt and te were not used. The decoder's rule changes C1 and C2 also bear on H1 (rum, -ent). Since the re-read was made by a reader who had seen the clear copy, H1's pass 3 figure shows that the key leaf reads the passage once it is transcribed well; it does not test the transcriber. H4 is the unit that does.

### What pass 3 leaves unread

- H4 lines 9-10, "deus ueus ter imsrael qui super t[?]=rar gerum habitat": the judge's one stretch that does not read (L09 27/33 = 81.8%, L10 25/33 = 75.8%); 5 signs of H4 have no value; emloo (L06).
- S2-05, caraton amen mathoi, 4/17.
- The two-ring figures on f. 54r (three by pass 3's count, four by pass 2's note; not reconciled), the two figures on f. 97r-v and the texts written inside the circles: not transcribed.
- Second-series no. 1 (f. 52r) is in ordinary script and was not transcribed.

What the rims say, from the decode and unchecked [unverified]: use-captions ("hoc signum reddit hominem uirtuosum et a periculo defendit"), instructions (to be written on a bread crust and given to eat, for love; written with the left hand in the blood of one's finger on a Thursday, in silver; against a binding spell, placed in the bound person's clothes), and two Gospel verses, S2-04 Luke 4:30 and S2-06 Luke 1:52 [derived: recognised from the decode, not checked against an edition]. With pass 2's 62, 73 cipher rims are now decoded.

Class and outcome: unchanged. `docs/_check_reading.py` and the other repo checkers were not run on pass 3 (the contributor's sessions do not run repo scripts), so no "read" or "read in part" wording is claimed for any pass 3 unit, and `profile.json`'s outcome block is as pass 2 left it. Whether pass 3 changes the target's class is left to the maintainers.

## Pass 4: Dan Bourdeau's re-review of pass 2 (a separate result, read with known key)

Answers Dan Bourdeau's review of 25 Nov 2026 on PR #957 (head 57aae52, pass 2). Pass 1 stays the figure of record. Passes 2 and 3 are unchanged. Pass 4 (`pass4/`) has its own figures and was counted by this agent alone: no separate judge and no person has checked it. Done by Claude Opus 5.5 on 27 Nov 2026. The checks were done with AI tools and no person checked each record by hand.

**Sequence** [measured: `pass4/FREEZE_P4.txt`, `pass4/stamps/STAMP_LOG.txt`, file times]:
1. Key v4, transcription v4, rules, Dl@ evidence and decoder frozen at 2026-11-27T03:29:51Z.
2. Freeze stamped at 03:29:56Z: RFC 3161 Sectigo 03:29:56 GMT and FreeTSA 03:29:57 GMT, manifest sha256 3d4db9c3...; OpenTimestamps submitted.
3. One decode at 03:30:08Z (`DECODE_P4.txt`), plus the declared variant without C4/C5 (`DECODE_P4_noC45.txt`).
4. Tags and count after the decode (`TAGS_P4.tsv`, `WORDS_P4.tsv`, `SCORE_P4.tsv`), then controls (`CONTROL_P4.txt`).

### What changed, point by point (`pass4/RULES_V4.md`)

1. **`Tk@` = ru** (Dan's point 1). On f. 99r the label reads "ru", in the same letter forms as "rum" beside it (`pass4/crops/f099r_ru_rum.jpg`). `KEY_LEAF.tsv` and `KEY_V3.tsv` had re: this was our misreading of the leaf. `KEY_V4.tsv` differs from `KEY_V3.tsv` in this row only [measured].
   - No transcription has a bare `Tk@`. Dan's 11 words are all written `Tk^@` (f. 4r 5, f. 4v 4, pass 2's f. 15r 2) [measured].
   - Pass 3's mark-order rule C1 already reads `Tk^@` as the leaf's rum sign. Pass 4 keeps C1, so all 9 of them on the training leaves now come out with -rum: hebraeorum, rerum, creaturarum, secretorum (three times), torum, and the holes p[?]iloeophorum and magicirum [measured: pass-4 decode of every `Tk^@` word].
2. **Nasal dot after the vowel of a two-letter sign** (Dan's point 2). This is pass 3's rule C2, unchanged. Pass 4 applies it for the first time to the 62 first-series rims and the training leaves.
   - It gives obedient (S1-013, 015, 016, 096), uenient (S1-096), surgens (f. 4r L11), ruebant (f. 4r L14), fiebant (f. 4r L19) and the like.
   - It does harm in one place. The four "infernales" (S1-013, 015, 016, 030) become infenrales: there the dot under `6r` stands for the n after the whole sign. All four are counted as holes.
3. **`Dl@` checked on the image** (Dan's point 3; `pass4/DL_CHECK.tsv`). All 34 rim words written with `Dl@` were looked at again on the unwraps [measured: DL_CHECK.tsv]:
   - 16 show the leaf's "is" sign (an x whose right arm sweeps up into a big loop) and are now `X@`. Where `X Dl@` had been written, the x and the loop are one sign. These give timebis, peribis, uideris, eris (three times), mortis (S1-073), dominantis, uinculis, periculis, iouis, and the holes tinebis, mobtis, mabris, sanguuinis. Reference crops: `crops/S1-019_sanguinis_end.jpg`, `crops/S1-027_timebis_end.jpg`.
   - 16 show the leaf's "us" sign (a delta whose ascender curls into a small loop) and stay: spiritus, omnibus, deus, aduersus, securus, gratus, fortunatus, iesus, usus, uestibus ...
   - 2 are unresolved and stay as written: S1-012, a big loop round a delta-like sign (`crops/S1-012_word5.jpg`), and S1-079, under an ink blot (`crops/S1-079_tus_*.jpg`).
   - The leaf's five looped forms are in `crops/f099r_looped_as_es_is_os_us.jpg`. The value of `Dl@` stays us.
   - Not looked at again: the 12 `Dl@` words of H1r and H4, and the 39 of the training leaves, H2 and H3 (Remaining gaps).
4. **Second series ff. 52r-54r, f. 97r-v, signs inside the circles** (Dan's point 4): not transcribed in pass 4 (Remaining gaps). Pass 3 had already transcribed and decoded second-series rims nos. 2-12 (ff. 52r-53r). Pass 4 decodes them again with the corrected transcription.
5. **Count in sure words per text** (Dan's point 5). Cipher words only. A word with a slip, a transposition or a `[?]` is a hole, and a lone `[?]` is a hole word. Where a pass-4 word is the same as the pass-2 decode at the same place, the pass-2 separate judge's tag is used. Every other word (330) was tagged by this agent after the decode; the 64 holes among them are listed with reasons in `pass4/TAGS_P4.tsv`.

### Pass-4 figures: sure words / cipher words, holes (`pass4/SCORE_P4.tsv`) [measured]

| text | held out in pass 4? | pass 4 | holes | 65% line | pass 2, separate judge's tags (Dan's count) |
|---|---|---|---|---|---|
| TRAIN f. 4r | no (training) | 102/138 = 73.91% | 36 | over | 98/141 |
| TRAIN f. 4v | no (training) | 126/165 = 76.36% | 39 | over | 128/171 |
| H1r f. 15r l. 1-12 (pass 3 re-read) | no | 69/75 = 92.00% | 6 | over | (pass 2 H1 42/79) |
| H2 f. 159r | no | 78/126 = 61.90% | 48 | **under** | 83/138 |
| H3 f. 34r rims 3-4 | no | 10/15 = 66.67% | 5 | over | 10/15 |
| H4 f. 25r l. 1-12 | no (first decoded in pass 3) | 73/89 = 82.02% | 16 | over | - |
| S1, 62 first-series rims (each its own text) | no | 385/474 = 81.22% over the 62 | 89 | 53 of 62 rims over, 9 under | 366/472 = 77.54%; 49 of 62 over |
| S2, 11 second-series rims | no | 85/96 = 88.54% over the 11 | 11 | 10 of 11 over, S2-05 under | - |

The pass-2 word units are as the pass-2 judge split them. Pass 4 joins a word broken with "=" into one word and counts a lone `[?]` as a hole word. The S1 total of 474 is Dan's 472 plus the two lone `[?]` of S1-014 and S1-030.

**Rims with 2 holes or fewer (short-text floor, README Conventions):** S1 50 of 62 (pass 2: 46 of 62 by Dan's count); S2 11 of 11. Every rim has fewer than 40 cipher words, so the floor can apply to each. S2-05 (caraton amen mathoi, 3 words, 2 holes) meets the floor but is under our own 65% line. No rim is claimed as read here: a read rim also needs its reading and translation reviewed, which pass 4 does not do.

**Under our 65% line in pass 4:**
- H2 61.90%.
- Rims S1-014 50.00%, S1-016 57.14%, S1-025 33.33%, S1-030 62.50%, S1-032 50.00%, S1-039 50.00%, S1-052 57.14%, S1-081 55.56%, S1-082 57.14%.
- Rim S2-05 33.33%.

Not pooled to hide them.

**Without C4 and C5** (the two rules not on the leaf; `DECODE_P4_noC45.txt`) [derived: the 13 lines that differ, with the same tags]:
- H1r 62/75 = 82.67%: christiana, parte and five ch~ri become holes.
- S1 384/474 = 81.01%: morte in S1-099 becomes a hole.
- S2 84/96 = 87.50%: ch~ri in S2-02 becomes a hole.
- Other texts unchanged.

**Controls** [measured: `pass4/CONTROL_P4.txt`; same Latin 4-gram statistic as pass 3; 20 min 45 s run]:
- (a) 5,000 key shuffles at each of seeds 20261112 and 7 (the 73 single-sign values of `KEY_V4.tsv` permuted): no shuffled key scored as well as the real key on any text or any rim, 0/5000 at both seeds. The lowest z is 4.5 (S2-05); H3 has z 6.8-6.9; the other sections have z 9.9-13.9.
- (b) The same decoder with the real key, on each text's signs shuffled across its word slots, 5,000 per seed: the real text ranks 1 of 5001 on every text and every rim at both seeds. The lowest z is 3.5 (S2-05).
- There is no held-out test in pass 4 (see Limits).

**Limits.**
- No text is held out in pass 4: every one was decoded before, and the reader had seen those decodes.
- The tags are one agent's: no separate judge, no person.
- The 16 `Dl@` changes rest on one reader's look at 0.8x-2x unwraps.
- The training leaves, H2 and H3 keep pass 2's transcription; inner dots are not recorded there.
- Every text stays "decoded, not read" (superseded 28 Nov 2026: see "States per text").


## Pass 5: Dan Bourdeau's point 4, the rest of the second series and the looped-sign words (a separate result, read with known key)

Answers point 4 of Dan Bourdeau's review of 25 Nov 2026 on PR #957: the second-series pages ff. 52r-54r and f. 97r-v, the signs inside the circles, and (carried on from pass 4's point 3) the 51 `Dl@` words of the other texts. Pass 1 stays the figure of record. Passes 2-4 are unchanged. Pass 5 (`pass5/`) has its own figures and was transcribed, decoded and counted by this agent alone: no separate judge, no blind second reader, and no person has checked it. Done by Claude Opus 5.5 on 27 Nov 2026. The checks were done with AI tools and no person checked each record by hand.

**Sequence** [measured: `pass5/FREEZE_P5.txt`, `pass5/stamps_freeze/STAMP_LOG.txt`, `pass5/DECODE_RUN_UTC.txt`]:
1. Key (a byte copy of key v4), decoder (a byte copy of the pass-4 decoder), rules, doubts, the `Dl@` evidence and all transcriptions frozen at 2026-11-27T04:47:36Z, with md5 and sha256 of every file.
2. Freeze stamped at 04:47:37Z: RFC 3161 Sectigo 04:47:37 GMT and FreeTSA 04:47:37 GMT, manifest sha256 0d1d0dc8...; OpenTimestamps submitted.
3. One decode right after (`DECODE_P5.txt`, run started 2026-11-27T04:47:43Z), plus the declared variant without C4/C5 (`DECODE_P5_noC45.txt`; it differs from the decode on no pass-5 line of the new texts).
4. Tags and count after the decode (`TAGS_P5.tsv`, `WORDS_P5.tsv`, `SCORE_P5.tsv`), then controls (`CONTROL_P5.txt`).

### What was transcribed (`pass5/RULES_V5.md`, `pass5/DOUBTS_P5.md`)

- **Inside the circles of ff. 52r-53r** (`pass5/tx/S2_INNER_v5.txt`, 9 parts, 63 cipher words). No. 2's inner square, no. 4's "IB." lines, no. 10's "te tra[gramma]ton" and "Elion" and no. 11's square letters are in ordinary script; nos. 6 and 9 hold drawn characters only. These are listed in the file and not decoded.
- **f. 54r, the four figures** (`pass5/tx/F054R_v5.txt`, 7 parts, 42 cipher words). Figure B's inner ring is in Greek letters, figure C's inner ring is single letters with points, and figure D carries Latin labels and the four evangelists' names in ordinary script; these are not decoded.
- **f. 97r and f. 97v** (`pass5/tx/F097_v5.txt`, 7 parts, 42 cipher words): outer ring, inner ring, the four words in the square, and the two words under the handle of f. 97r. The single signs in the square's side cells (3, 7, a lambda, 5) look like numbers and are not counted.
- **The looped sign `Dl@`, the 51 words pass 4 left** (`pass5/DL_CHECK_P5.tsv`): 30 show the leaf's "us" form and stay; 15 show the "is" form (an x whose right arm sweeps up into a big loop) and become `X@`; 6 are unresolved and stay as written [measured: 30 + 15 + 6 = 51]. By text: f. 4r 3 changed of 12, f. 4v 6 of 15, H1r 0 of 2, H4 0 of 10, H2 5 of 11, H3 1 of 1. The changes give quamuis, habueris, meis, alienis, eis, eris, fueris, iouis (H2, "in aliquo die iouis"), armis (H3, "non peribit in armis"), and the holes scientiis, tmporis, s[?]is, nu[?]eris, ceuuulis, sanbcerdotolis.

The reader knew the key leaf and the earlier decodes, so none of this is blind or held out.

### Pass-5 figures: sure words / cipher words (`pass5/SCORE_P5.tsv`) [measured]

Same house rule as pass 4, made stricter for names: a variant spelling (tetragramaton with one m, mesias, iohans, adonaer, sembaoth, uincla for the psalm's uincula) is a hole.

| text | pass 5 | holes | 65% line | pass 4 |
|---|---|---|---|---|
| TRAIN f. 4r | 103/138 = 74.64% | 35 | over | 102/138 |
| TRAIN f. 4v | 131/165 = 79.39% | 34 | over | 126/165 |
| H2 f. 159r | 79/126 = 62.70% | 47 | **under** | 78/126 |
| H3 f. 34r rims 3-4 | 11/15 = 73.33% | 4 | over | 10/15 |
| H1r, H4, S1 rims, S2 rims | unchanged from pass 4 | | | |
| ff. 52r-53r inside the circles, 9 parts (each its own text) | 21/63 = 33.33% over the 9 | 42 | 2 of 9 over | new |
| f. 54r, 7 parts | 28/42 = 66.67% over the 7 | 14 | 3 of 7 over | new |
| f. 97r-v, 7 parts | 24/42 = 57.14% over the 7 | 18 | 2 of 7 over | new |

Arithmetic for the new parts [derived from `SCORE_P5.tsv`]: ff. 52r-53r per part: S2i-03 4/7, S2i-04 3/3, S2i-05 0/14, S2i-07h 2/3, S2i-07v 1/2, S2i-08 3/9, S2i-10 1/5, S2i-11 1/2, S2i-12 6/18; sum 21/63. f. 54r: A-top 1/1, A-rim 8/9, A-in 1/3, B-rim 5/9, B-in 0/1, C-rim 10/13, D 3/6; sum 28/42. f. 97: r-out 7/11, r-in 0/4, r-sq 3/4, r-lab 1/2, v-out 7/13, v-in 2/4, v-sq 4/4; sum 24/42. All new parts together 73/147 = 49.66%, listed only.

**At or over 65%:** S2i-04 "sinite hunc abire" 3/3; S2i-07h "fortis iuse deus" 2/3; F54-A-top "saluator" 1/1; F54-A-rim "salua me deus athanatos sanctus et fortis sanctus [?][?]ntenus" 8/9; F54-C-rim "gribe hoc in tuis uestimentis acenea lucena noua nomina mulierum tactis uestibus ueniet" 10/13; F97r square "lucas iohans mathias marcus" 3/4; F97v square "michael gabriel raphael uriel" 4/4.

**Under 65%, not pooled to hide them:** S2i-03, S2i-05 (the eight sectors of no. 5, 0/14: no sense), S2i-07v, S2i-08 (only tetra / gram / maton, split by the sector lines), S2i-10, S2i-11, S2i-12 (Ps 115:16 "dirupisti ... uincula mea" can be seen, but 12 of 18 words are holes), F54-A-in, F54-B-in, F54-B-rim ("signum ... contra ... probatum et approbatum", 5/9), F54-D ("rex uincit ... est", 3/6), F97r outer ring 7/11 (63.64%), F97r inner ring 0/4 (magical names), F97r label 1/2, F97v outer ring 7/13 ("agla rex alpha et omega mediator sponsus"), F97v inner ring 2/4.

**Controls** [measured: `pass5/CONTROL_P5.txt`; same Latin 4-gram statistic as passes 3-4; about 22 min run]: 
- Whole sections, both controls, both seeds: no shuffled key and no shuffled ciphertext scored as well as the real text on the new sections (ff. 52r-53r inside the circles z 5.8-5.9 key / 9.8-9.9 ciphertext; f. 54r z 10.4-10.5 / 15.2-15.5; f. 97r-v z 5.5 / 9.3), nor on the old ones (TRAIN f4r, f4v, H1r, H2, H3, H4, S1, S2): 0/5000, real text ranked 1 of 5001.
- Parts that pass both controls at both seeds (0/5000 or at most 3/5000 with z 3 or more): S2i-03, S2i-04, S2i-12, F54-A-top, F54-A-rim, F54-A-in, F54-B-rim, F54-C-rim, F97r-out, F97r-sq, F97r-lab, F97v-out (key shuffle 6 and 3 of 5000).
- Parts that do **not** stand apart from shuffles: S2i-05 (key 168 and 148 of 5000; ciphertext rank 23 and 22), S2i-07h (3-10 of 5000), S2i-07v (275-1,037), S2i-08 (112-148), S2i-10 (z -0.4, about 3,200), S2i-11 (about 2,500), F54-B-in (10-53), F54-D (8-17), F97r-in (129-149), F97v-in (34-49), and F97v-sq, the four archangels' names (z 0.4-0.9; 1,638 key and 935-960 ciphertext shuffles as good). A Latin 4-gram model does not favour names, and a part of 1-5 words gives the test little to work on; the counts are reported as they came.
- Old rim S2-05 now has 1 ciphertext shuffle of 5000 as good as the real text at seed 20261112 (rank 2 of 5001; pass 4: rank 1); the new sections change the random draws. Every other old rim is 0/5000 in both controls at both seeds.
- There is no held-out test in pass 5 (see Limits).

**Limits.**
- Nothing in pass 5 is blind or held out: the reader knew the key leaf and the earlier decodes and recognised many words while transcribing; label choices helped by sense are listed in `DOUBTS_P5.md`.
- One reader, one tagger, no separate judge, no blind second reader, no person.
- f. 4v exists here only at 2000 px; six `Dl@` words stay unresolved.
- Short parts (1-4 words) meet the short-text floor easily; they are listed, not claimed.
- Every text stays "decoded, not read" (superseded 28 Nov 2026: see "States per text").


## States per text (28 Nov 2026, Dan Bourdeau's review of 27 Nov 2026 on PR #957)

Dan Bourdeau's points 1-3: set each text's state from its own count, give each rim and part its own `outcome.texts` entry, keep only the latest pass for each passage, and add a reading and a translation for passes 4 and 5. Done by Claude Opus 5.5 on 28 Nov 2026. No frozen file, no tag and no figure was changed: the counts are those of `pass5/SCORE_P5.tsv`, which Dan reproduced (H1r 69 of 75, H4 73 of 89, H2 79 of 126, first-series rims 385 of 474 with 50 of 62 within the floor, second-series rims 85 of 96 with 11 of 11). The checks were done with AI tools and no person checked each reading by hand.

**The rule used** (README Conventions, 19 Nov 2026) [derived from `pass5/SCORE_P5.tsv`]:
- read: 95% or more of the cipher words sure, or, under 40 cipher words, at most 2 holes (5% never allows more here); `floor_used` is true when only the floor makes it read;
- read in part: under that bar, and the sure words build sentences with holes;
- decoded, not read: no word sure (F54-B-in 0/1, F97r-in 0/4, S2i-05 0/14), or the sure words do not build a sentence (S1-025 "... odium et ...", S2i-08 "tetra gram maton" only, S2i-10 "amor" only, S2i-12 a psalm verse glimpsed through 12 holes in 18). These four calls are ours, by reading, and are open to the maintainers.

**`outcome.texts`** now holds pass 5 only, the latest pass for every passage: 100 entries, one per text, rim and part (4 passages, 62 first-series rims, 11 second-series rims, 9 parts inside the circles, 7 of f. 54r, 7 of f. 97r-v). Each carries `cipher_words`, `holes`, `read_share` and `floor_used`. The pass-1 and pass-4 entries were dropped from `outcome.texts`; their figures stay above in this file. The training leaves ff. 4r-4v are the key's source and have no entry.

| state | entries | which |
|---|---|---|
| read, 95% or more | 20 | S1-011, 018, 020, 027, 031, 037, 055, 072, 073, 078, 080, 090, 099, 110; S2-03, 06, 07; S2i-04; F54-A-top; F97v-sq |
| read, only by the short-text floor | 52 | 36 first-series rims, 8 second-series rims (S2-02, 04, 05, 08-12), S2i-07h, S2i-07v, S2i-11, F54-A-rim, F54-A-in, F97r-sq, F97r-lab, F97v-in |
| read in part | 21 | H1r 71/77, H2 81/133, H3 11/15, H4 75/92 (with the 12 words broken at a line end, see below); S1-014, 016, 030, 032, 039, 052, 079, 081, 082, 095, 103; S2i-03; F54-B-rim, C-rim, D; F97r-out, F97v-out |
| decoded, not read | 7 | S1-025, S2i-05, S2i-08, S2i-10, S2i-12, F54-B-in, F97r-in |

[measured: 20 + 52 + 21 + 7 = 100 entries; first-series rims 14 at 100% + 36 by the floor = 50 of 62 read, as Dan counts; second-series 3 + 8 = 11 of 11.]

With some of these, read by the floor is thin: S2-05 (1/3), S2i-07v (1/2), S2i-11 (1/2), F54-A-in (1/3), F97r-lab (1/2) and F97v-in (2/4) have half or more of their words as holes, mostly magical names, and several short parts do not stand apart from shuffles (Pass 5 controls). They are read by the rule as written; we list them so the maintainers can judge. **Maintainers' decision at the merge (28 Nov 2026):** these six, S2-05 (1/3), S2i-07v (1/2), S2i-11 (1/2), F54-A-in (1/3), F97r-lab (1/2) and F97v-in (2/4), keep the state "read" that the short-text floor gives them, since the floor is the rule as written, but none of them is a sentence: each is one or two sure words beside names or words in holes, and their reading reviews say so.

The target's class is therefore **read in part** (a target classed read may hold only read entries). The method stays "key recovered based on adjacent plaintext" for the first pass of record; passes 2-5 are read with known key (`outcome.parts`). `fraction_read` (0.502) is the first pass's figure of record and is not changed. No `reading_review` was recorded by the contributor: Dan Bourdeau said that review is the maintainers' to push; it was recorded at the merge (below).

**Readings and translations** (Dan's point 3): `reading_pass4.md` and `translation_pass4.md` (77 sections: H1r, H2, H3, H4 and the 73 rims), `reading_pass5.md` and `translation_pass5.md` (100 sections, the same as `outcome.texts`). The reading is the decode word for word, holes marked `[?word]`, a sign group with no value `[?]`; the translation renders each hole as `[?]` and adds no word the reading does not give [measured: a script checked that each section's hole marks equal its `holes` in the SCORE file, and that each translation has one `[?]` per hole]. Each section header gives its count and state. Pass 4 differs from pass 5 only in H2 (iouius, a hole, where pass 5 has iouis) and H3 (armus, where pass 5 has armis), and in the training leaves, which are not included. The translations are Claude's, from the Latin as decoded; no person or Latinist has checked them [unverified].

**Found while doing it:** the pass-4 and pass-5 scorers left 12 words broken at a line end out of the counts (see Remaining gaps). They are shown in the readings in angle brackets with our own tags. **Corrected at the merge (28 Nov 2026, maintainers):** `outcome.texts` and the reading and translation headers now give the counts with them, H1r 71/77 = 92.21% (6 holes), H2 81/133 = 60.90% (52 holes), H4 75/92 = 81.52% (17 holes); the frozen `pass5/SCORE_P5.tsv` and `WORDS_P5.tsv` predate this fix and still give 69/75, 79/126 and 73/89. No state changes.


## Reading reviews at the merge (28 Nov 2026)

At the merge of PR #957 an AI agent working for the maintainers recorded a `reading_review` on each of the 93 read or read-in-part entries of `outcome.texts`, signed "integration review of PR #957 (AI agent, for the maintainers); not a person"; the 7 decoded, not read entries get none. For each entry it read that section of `reading_pass5.md` as Latin and the same section of `translation_pass5.md`, and recounted the count from `pass5/WORDS_P5.tsv` (all 100 entries agree; H1r, H2 and H4 with the 12 words broken at a line end, checked against their tags in the reading). Each review's note says what the agent found in that text. In short: the 20 texts at 95% or more read as complete sentences; most rims read by the floor are one sentence with one or two holes that are recognisable slips (infenrales, tinebis, figua); S1-032, S1-052 and F54-D give only a sentence frame; H2 reads only in its opening and closing lines; and the six thin parts above are not sentences. All are grade B: the decode is raw (no punctuation, abbreviation bars, u for v) and the translation normalises it. No image, transcription or held-out check was made, and no person has read the Latin.


## Remaining gaps

- Holes in the three decoded passages of the first pass, 112 of 225 words (H1 42 of 77, H2 63 of 133, H3 7 of 15) - blocker: not-attempted; key faults the judge's errors show (the sign 1 where the sense wants a; r or rr for te or i; irr for Xri; c for h; final t as n). Pass 2 (`keyleaf/`) applies the key leaf to the same transcriptions; the transcription faults behind several of these (1 for a) are not re-read. Pass 3 (`pass3/`) re-read H1 only (399/405 = 98.5% judged, not held out); H2 and H3 are not re-read.
- Pass 2 units under the 65% line: H1 (62.04%), H3 pentacle 3 (52.8%), rims S1-025, S1-039, S1-070, S1-071, S1-096 - blocker: not-attempted; swapped letter pairs and the first pass's transcription faults (not re-read) carry most of the N; a re-read of these lines on the images would be a third pass with its own figure: pass 3 did this for H1 only (see "Pass 3"); H3 pentacle 3 and the five rims are not re-read. Every pass-2 section is under `_check_reading.py`'s 0.45 clean-sentence bar, so none is read. No person has checked pass 2.
- 1 of the 8 first-pass `?` signs is still not identified (f. 4r l. 17, a small reversed-e loop joined to a looped delta; not on the key leaf) - blocker: no-key-material; the leaf has no such sign.
- Pentacles with no clear counterpart: the second-series figures (signs inside the circles of ff. 52r-53r, the four figures of f. 54r, f. 97r-v) were transcribed and decoded in pass 5; the texts inside the circles of the first series (e.g. nos. 62, 101) are still not transcribed - blocker: not-attempted; images fetched (`keyleaf/IMAGE_FETCH.tsv`).
- Pass 3 unit under the 65% line: second-series rim S2-05, caraton amen mathoi, 4/17 = 23.5% - blocker: no-key-material; two names with no clear counterpart and no source found to check them against.
- Pass 3, H4 (f. 25r) lines 9-10, "deus ueus ter imsrael qui super t[?]=rar gerum habitat", and 5 signs of H4 with no value (L02, L04 twice, L09 twice) - blocker: not-attempted; the lines were not re-read on the image after the decode (freeze rule), and H4 has not been compared with its clear copy.
- Decoder rules C4 and C5 of pass 3 are not on the key leaf - blocker: no-key-material; the leaf has no rte entry and no chi-rho entry; figures with and without them are in "Pass 3".
- The rest of the volume's cipher text, ff. 3r-96v and ff. 158r-162r, apart from the passages transcribed here - blocker: not-attempted; the clear copy ff. 101r-155r and 166r-170r gives the same text per the catalogue.
- Inner dots (`*`) were not recorded on the first-pass leaves, so the two-dot sign there runs on the declared fallback of the pass-2 decoder - blocker: not-attempted; a re-transcription of those leaves with the dots would remove the fallback.
- Prior art in print: Skinner and Rankine 2008, Mathers 1889, Boudet's census - blocker: needs-physical-access; not opened; web searches found no mention of a Basel cipher copy.
- `Dl@` words still unresolved: S1-012 and S1-079 (pass 4) and six of the 51 looked at in pass 5 (f. 4r L16 and L17 last word; H2 L04, L07, L08, L22; `pass5/DL_CHECK_P5.tsv`) - blocker: illegible at the resolution available (f. 4v only at 2000 px; S1-079 under a blot); they stay as written.
- Pass 5 parts under the 65% line: ff. 52r-53r S2i-03, S2i-05 (0/14), S2i-07v, S2i-08, S2i-10, S2i-11, S2i-12; f. 54r A inner ring, B inner ring, B rim, D; f. 97r outer ring (63.64%), inner ring, label; f. 97v outer and inner rings; H2 62.70% - blocker: not-attempted; one reader's transcription of crowded figures, many signs `?`, magical names with no attested spelling to check against; a blind second reader (images only) and a separate judge have not been run on pass 5.
- Pass 5 inner texts written in ordinary script or Greek letters (no. 2, no. 4 IB lines, no. 10 centre, no. 11 square, f. 54r B and C inner rings, D labels) are listed but not read or translated - blocker: not-attempted.
- Pass 4 units under the 65% line: H2 61.90%; rims S1-014, S1-016, S1-025, S1-030, S1-032, S1-039, S1-052, S1-081, S1-082, S2-05 - blocker: not-attempted; most holes are pass-2 transcription faults not re-read (H2, the training leaves and the first-series rims keep pass 2's transcription), plus rule C2 turning infernales into infenrales four times.
- Passes 4 and 5 were counted by one agent (tags in `pass4/TAGS_P4.tsv`, `pass5/TAGS_P5.tsv`) with no separate judge and no person; no pass-4 or pass-5 text is held out - blocker: not-attempted.
- 12 words broken at a line end are left out of `WORDS_P4/P5.tsv` and `SCORE_P4/P5.tsv`: H1r immaculati, circumcisionem; H2 adhibenda, librum, iuupiten, iupitet, signillum, miratbilitet, negotius; H4 uirtutes, mansueta, t?rar - blocker: not-attempted; found 28 Nov 2026 while making the readings: the pass-4 and pass-5 scorers join a word broken with "=" but drop the joined word unless it is broken again. The frozen and stamped score files are left as they are; the readings show the words in angle brackets with our own tags. Side count [derived]: H1r 71/77 = 92.21%, H2 81/133 = 60.90%, H4 75/92 = 81.52%; no state changes. Since the merge of PR #957 (28 Nov 2026) these are the counts in `outcome.texts`; the gap that stays open is that the frozen score files leave the 12 words out.
- Pass-5 parts "read" only by the short-text floor with half or more of their words holes: S2-05 1/3, S2i-07v 1/2, S2i-11 1/2, F54-A-in 1/3, F97r-lab 1/2, F97v-in 2/4 - blocker: too-short; the floor allows 2 holes under 40 cipher words, and these are mostly magical names with no attested spelling to check. F54-B-in (0/1) is kept "decoded, not read": no word of it is read.
- The reading reviews of the 93 read or read-in-part entries are an AI agent's, recorded at the merge of PR #957 (28 Nov 2026); no person has read the Latin - blocker: not-attempted.
- Leaf sign "unt" (delta with a division sign) is not in the key tables (Dan Bourdeau, not blocking) - blocker: not-attempted; pass 3 called it a compound of Dl + Dv; no row added.

## Transcription doubts

The 8 signs transcribed `?` on the first pass, looked at on the full-size images on 25 Nov 2026, after the first decode, the clear copy and the key leaf had been seen (so not blind). The frozen first-pass files are unchanged and the first pass stays the figure of record; the readings below go only into the second-pass copies `keyleaf/tx2/` (`keyleaf/tx2/CHANGES.tsv`), decoded once with the key leaf in pass 2 with its own figures. No person has checked these readings. [Looked at by Claude Opus 5.5; `keyleaf/SIGNS8.md`]

- ? (f. 4r l. 17, training, last word "6 ? Dl@") - read: a small closed loop open to the left, like a reversed e, joined to the following looped delta, with no tail; not drawn on the key leaf; checked: full-size image (canvas 11); stays `?`, no value in pass 2.
- ? (f. 15r l. 5, third word "? Bx Tk^@") - read: a six-shape (e) written joined to the following box; the first pass took the joined pair for an unknown sign; checked: full-size image (canvas 33); pass 2 `6`; the word decodes eorem with the leaf (eorum in the clear copy; the leaf's Tk@ with a dot above is rum, the first pass's split dot gives rem).
- ? and ? (f. 15r l. 9, third word "Lm ? Dl_ 8 X Ea ?") - read: the first is a four-shape with two dots above (diaeresis, nn); the second is the crossed x joined to a six-like loop with a dot below (the leaf's tio, + n), followed by a blotted six-shape with a dot above that the first pass did not record; the same look shows the first pass's "X Ea" to be one sign, an x with a ʒ-like tail (the leaf's ia); checked: full-size image (canvas 33); pass 2 `Lm 4" Dl_ 8 Xz Xco_ 6^`, which decodes annunciationem (clear copy annuntiationem).
- ? (f. 159r l. 3, third word "3_ ? Bx 6s X Ds Ea^") - read: a small x written raised, then a hook-sign with a cross stroke through its descender (the leaf's sp); checked: full-size image (canvas 325); pass 2 `X Hkf`; the word decodes dnispositam (clear dispositam; the first pass's dot below the d gives the n).
- ? (f. 159r l. 7, second word "X_ ? D2 8 D3 6_") - read: the same crossed hook-sign (sp); checked: full-size image (canvas 325); pass 2 `Hkf`; decodes inspicien (clear inspiciens).
- ? (f. 159r l. 22, last sign of the fourth word "Am 6s 6 Oe Dl 6 ?") - read: a hooked bowl joined to a delta, crossed by a stroke running out to the right: the leaf's tur sign; checked: full-size image (canvas 325); pass 2 `Ab`; decodes consequetur (clear consequetur).
- ? (f. 34r pentacle 4, fifth word) - read: a four-shape with a bar above (a barred n; the leaf gives non only as the barred box, and says other abbreviations follow Latin usage); checked: full-size unwrap (canvas 71); pass 2 `4~`; decodes n~ where the clear copy has non.
- Marks not recorded on the first pass (`SIGNS.md`): an inner dot in Bx, a dot inside Lm, a dot in the crossing of X - read: the key leaf shows that this dot carries meaning (the two-dot sign refers back to the letter with a dot in its middle; example ambulare, with the dot drawn inside the lambda); checked: key leaf f. 99r at full size; on the first-pass leaves the dots are still not recorded, and the pass-2 decoder uses a declared fallback there.

## Escalation

- [x] siblings: the volume itself: its clear copy (used for the key) and its key leaf f. 99r with the German translation f. 98r; no other manuscript of this secret alphabet found (`PRIOR_ART.md`)
- [x] clear-pages: the clear copy ff. 101r-155r and 166r-170r is the plain text of the cipher (catalogue); used for training (ff. 101r-102r) and, after the decode, for scoring (ff. 109v, 167r, 123r); its pentacle pages f. 123r-v carry only nos. 1-10 (looked at 25 Nov 2026, canvases 253-254)
- [x] known-keys: the volume's own key leaf, transcribed into `keyleaf/KEY_LEAF.tsv` and applied in pass 2
- [x] print: no edition or study of this cipher found (`PRIOR_ART.md`); Skinner and Rankine, Mathers and Boudet's census not opened
- [x] key-rebuild: done as pass 2 with the key leaf (`keyleaf/`), frozen and stamped before one decode; reported apart from the first pass of record
- [ ] retry: in part. The 8 `?` signs were looked at (7 now labelled); the 62 inscribed first-series pentacle rims were transcribed and decoded; pass 2 was scored by a separate judge (25 Nov 2026); pass 3 (25 Nov 2026) re-read H1 with inner dots recorded, decoded a fresh held-out passage (H4, f. 25r) and the 11 inscribed rims of second-series nos. 2-12, and was scored by a separate judge; the figures on f. 54r, f. 97r-v, the texts inside the circles, and a re-transcription of ff. 4r, 4v, 159r and 34r with inner dots remain; pass 4 (27 Nov 2026) corrected Tk@ = ru on the leaf, applied the nasal-dot rule to every text, re-looked at all 34 rim words written Dl@ (16 changed to X@), froze, stamped, decoded once and counted in sure words per text; pass 5 (27 Nov 2026) transcribed and decoded the signs inside the second-series circles, f. 54r and f. 97r-v, and looked at the 51 remaining `Dl@` words (15 changed), frozen, stamped, decoded once and counted; the first-series inner texts and a re-transcription of ff. 4r, 4v, 159r and 34r with inner dots remain

## Files

Copied unchanged from the contributor's working folder (sha256, first 16 hex) [measured]. `FREEZE_TX.txt` and `FREEZE_KEY.txt` match all 14 files they list; 53 of the 63 entries of `stamps/MANIFEST.sha256` are committed here and match; the manifest hashes to 6f8f7ff0..., as `stamps/STAMP_LOG.txt` says, and both RFC 3161 tokens carry that digest.

| file | what | sha256 |
|---|---|---|
| `PRIOR_ART.md` | prior-art searches, before transcription | 61fca2e46be0c0b6 |
| `FETCH_LOG.txt` | image URLs, HTTP status, sizes, sha1 | d9bc455b23c4aa66 |
| `SPLIT.md` | training and held-out split, before key building | a508ff03a8beb87e |
| `SIGNS.md` | sign labels and marks | 21cd4d1ce8363e9d |
| `FREEZE_TX.txt` | transcription freeze | fd27efcb3d2835a7 |
| `SOLVE_LOG.md` | both solver runs | 18b6f5f1af59af90 |
| `KEY.tsv` | the key of record | ec59fefe2a0fef6a |
| `FREEZE_KEY.txt` | key freeze | c7f89762ce450e40 |
| `DECODE.txt` | the one decode (the decryption) | 8108bf8b4efb2db3 |
| `tx/f004r.txt`, `tx/f004v.txt` | training transcriptions | 7573c6faf0aa2cf1, fd842c8aff2aac9a |
| `tx/f015r.txt`, `tx/f159r.txt`, `tx/f034r_p34.txt` | held-out transcriptions H1, H2, H3 | fcf3e9b98e3c9073, 3ba786cd1664eea7, f9de0d13de2140c3 |
| `tx/CLEAR_TRAIN.txt` | clear copy ff. 101r-102r, training | a488db1ff7fd1083 |
| `tx/KEYLEAF_f099r.txt` | the key leaf, after the decode | ec95c4b1825b595e |
| `judge/BRIEF.txt`, `judge/decode.txt`, `judge/judge.tsv`, `judge/count.py` | the judge's packet, scores and adder | 511ce682face3fa9, 03a1087e99c7ba02, 2d3a057e4a33f96f, 22b99477950a22f2 |
| `score/CLEAR_H1_f109v.txt`, `CLEAR_H2_f167r.txt`, `CLEAR_H3_f123r.txt` | clear counterparts, after the decode | 4afa937d2995b877, 424aa8df4113700a, ee78d4ba2e1ce211 |
| `score/score_clear_out.txt`, `worddiff_out.txt`, `lexcheck_out.txt`, `train_fit_out.txt` | clear-copy scores, word diff, lexicon check, in-sample fit | 2954a7e8a8437d1b, e46994f1823129ba, 5b5d17394c4c0132, 4de5d1a83ee5d061 |
| `score/shuffle_out.txt`, `shuffle_run.log`, `shuffle_run_partial_slow.log` | shuffle control | 2c79d7b5ebcb7f04, 32c3dd32f01a65b6, 573d8eebc04a583a |
| `work/keyleaf_vs_key.tsv` | key leaf against the frozen key | ea44cd19b29d720c |
| `work/train_alignment.tsv`, `work/KEY_run1.tsv`, `work/solve_out.txt`, `work/solve_out_run1.txt` | training alignment of record, run 1 key, solver output | 2c645606241a190f, 46ca2d31123efb49, 640182286b089337, 7e250fd1c0631e43 |
| `work/decode_counts.txt`, `work/DECODE_HASH.txt`, `work/SCORES_HASH.txt` | decode counts and hash records | 5964607a2618186a, 97a5acbf026c61aa, 6c4b50876474b53e |
| `work/canvases.tsv` | canvas, folio and page id of every image | 24520a5cc2b75023 |
| `scripts/` (14 files) | `common.py`, `solve.py`, `decode_once.py`, `score_clear.py`, `shuffle.py`, `lexcheck.py`, `worddiff.py`, `train_fit.py`, `fetch.sh`, `grid.py`, `sheet.py`, `strips.py`, `unwrap.py`, `zoom.sh` | solve.py 31616ce3bb4491a2, common.py 454414ae8114fa44, decode_once.py 4c23afc8bc916be5 |
| `stamps/` (6 files) | manifest of the working folder and its time-stamps | MANIFEST.sha256 6f8f7ff0975153f5 |

Pass 3 (`pass3/`, 47 files, added 25 Nov 2026; sha256, first 16 hex) [measured]: `KEY_V3.tsv` 0c7768e67ff56f77, `RULES_V3.md` 72905d3249d72048, `scripts/decode_p3.py` 11bf6e1b02b6ec5c, `tx/f015r_p3.txt` 33e5de612bb11a48, `tx/f025r_H4.txt` c0f2a584154fe686, `tx/PENT_S2.txt` 8746be67ae7081cc, `DOUBTS_P3.md` a72f05ebd36e40f0, `SPLIT_P3.md` 81a07fba0e4c39a1 (the eight text files of `FREEZE_P3.txt`, 5a16f2a8734892bd; its ninth entry is the f. 25r image, not committed); `DECODE_P3.txt` and `judge/decode.txt` 76f334c53450a421; `judge/BRIEF.txt` a1fd9095fa59183e; `JUDGE_P3_RESULT.md` 70f48c45442e4ed3; `SCORE_P3.tsv` fa0b2f47b7e576e6 (the solver's own count); `CONTROL_P3.txt` 5d18be0f43a39991; `RUN_RECORD.tsv` e882edaf10d084b6 and `RUN_RECORD_FOLLOWUP.tsv` (judge, variant, stamp, checks); `RESULT.md` 02206d3320ee8aef (the solver's own report, written before the judge ran: where it says no separate judge has scored pass 3, this file governs); `EMENDATIONS.md` (none made); `PRIOR_ART_P3.md`, `BLOCKED.tsv` (nothing blocked); `scripts/` (6 files; they carry the working folder's absolute paths, left unchanged so the hashes hold); `variant/` (12 files: the declared decode without C4 and C5 and its score); `checks/` (3 files); `stamps/` (6 files; `MANIFEST.sha256` 4836e7313b019c80, 36 of its 37 entries committed and matching).

Pass 5 (`pass5/`, added 27 Nov 2026; sha256, first 16 hex) [measured]: `FREEZE_P5.txt` 1995c8bd49d6588d, `RULES_V5.md` c5c3a564a755795d, `DOUBTS_P5.md` 43cd8492956fcbd1, `DL_CHECK_P5.tsv` 08013ab02f82d840, `tx/S2_INNER_v5.txt` 56d4eb262cf7f513, `tx/F054R_v5.txt` 0a1d9abeba0512d7, `tx/F097_v5.txt` 69b019657e166e12, `DECODE_P5.txt` 37e50146668e42e2, `SCORE_P5.tsv` 1d7190ea9f62d70b, `TAGS_P5.tsv` bb97ac5ce8f2a7a9, `CONTROL_P5.txt` 87af77ad62a86231; `KEY_V5.tsv` and `scripts/decode_p5.py` are byte copies of the pass-4 files; `tx/` also holds the pass-4 texts (H1r, H4, S1, S2 unchanged; f. 4r, 4v, 159r, 34r with the 15 `Dl@` -> `X@` changes, made by `scripts/apply_t2.py`); `DECODE_P5_noC45.txt`, `WORDS_P5.tsv`, `DECODE_RUN_UTC.txt`; `scripts/` (10 files; the image tools carry the working folder's absolute paths); `stamps_freeze/` (6 files, manifest 0d1d0dc8...). `stamps_result/` (6 files): the results stamped after the decode, count and controls at 05:12:14Z (RFC 3161 Sectigo and FreeTSA 05:12:14 GMT, manifest 5959fa4e...). The md5 and sha256 lists in `FREEZE_P5.txt` match the committed files. No images.

Not committed: the page images, contact sheets and every crop except the seven pass-4 reference crops in `pass4/crops/`; the downloaded IIIF manifests, METS record, Steinmann PDF and catalogue HTML; `__pycache__`. They are in the stamp manifest where it lists them.

Made here (28 Nov 2026): `reading_pass4.md`, `translation_pass4.md`, `reading_pass5.md`, `translation_pass5.md`, from `pass4/WORDS_P4.tsv` and `pass5/WORDS_P5.tsv` (no frozen file changed).

Made here (25 Nov 2026): `transcription.txt` (the five files of `tx/` that `FREEZE_TX.txt` lists, put together unchanged), `reading.md`, `translation.md`, `validation.tsv` (input for `docs/_validate.py`), `profile.json`, this file. No images.

Name: the folder is `baselanv9`, in lower case as the site's page slugs and checkers require. The working folder (`basel_anv9`) and the files copied from it call the target `baselANV9`; they are left unchanged, so their hashes still hold.

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person has read the signs or the text without AI.
- One transcription, one reader, one pass. The training leaves were transcribed with the clear copy beside them, and the held-out leaves by a reader who knew most of the system; the held-out passages test the key, not the transcriber.
- The judge was a model session scoring sense by its own lights; its separation from the solver is stated, not shown.
- The reading and the translation were made after the clear copy had been seen, and are unchecked.
- Pass 3: H1 is not held out and its re-read was not blind; H4 is held out in that its text was never transcribed or decoded before the freeze and its clear copy was not looked for, but its reader knew the key leaf; the pass 3 freeze was not time-stamped before the decode, and the judge's brief was written after it; the judge's model is not recorded; C4 and C5 are not on the key leaf.
- Three passages on parts of three pages, out of about 100 leaves of cipher (ff. 3r-97v and 158r-162r, by the catalogue's foliation): the figures say nothing yet about the rest.

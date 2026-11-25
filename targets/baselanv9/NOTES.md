# baselanv9: Clavicula Salomonis and Septem sigilla planetarum in a secret alphabet, Basel UB, UBH AN V 9 (17th century)

Status: in progress. Contributed by pull request, not yet written up (pass 2 with the volume's key leaf added 25 Nov 2026 in `keyleaf/`, its judge's scores still to come), and a new target: the volume is in neither `catalogue.json` nor `research/leads.json`. The key was recovered from cipher ff. 4r-4v aligned with the volume's own clear copy, frozen, and used for one decode of three held-out passages. A separate strict judge finds 747 of 1,138 decoded letters in words that read as sense (65.6%: H1 62.4%, below the contributor's own 65% line; H2 67.0%; H3 69.6%), and the decode reproduces 988 of 1,231 letters of the clear copy (80.3%). Counted in words, 113 of 225 read as sense (0.502) and no sentence is clean, so each passage is "decoded, not read" and the target is filed not read: key recovered from adjacent plaintext, text not read. The volume's own key leaf, viewed only after the decode, agrees on 46 of the 52 values it covers. The page, ledgers, DECODE queue entry and any catalogue or lead entry are left to the maintainers.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Opus 5.5 the solver session, the separate strict judge and the assembly of this folder.

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working sessions, not checked here; [unverified] = a reading of the text not checked by anyone else.

## The source

- Basel, Universitätsbibliothek, UBH AN V 9 (old shelfmark K IV 19): "Clavicula Salomonis, Septem Sigilla Planetarum", 17th century (catalogue: 1600-1699), one volume of 180 leaves in two parts (18.5-19 x 14.5 cm and 20 x 15 cm), Latin [sourced: the METS/MODS record of e-manuscripta 5353221 and its IIIF manifest].
- Online: e-manuscripta.ch, https://doi.org/10.7891/e-manuscripta-185551, online since 1 Sep 2025 (digitised April 2025); IIIF manifest https://www.e-manuscripta.ch/i3f/v20/5353221/manifest, 380 canvases [sourced]. Page images: `https://www.e-manuscripta.ch/i3f/v20/<page id>/full/2000,/0/default.jpg` (`FETCH_LOG.txt`; canvas, folio and page id in `work/canvases.tsv`). The held-out pages: f. 15r page id 5353252, f. 159r 5353544, f. 34r 5353290; training f. 4r 5353230, f. 4v 5353231 (`SPLIT.md`).
- Licence: the record's use and reproduction condition is the Creative Commons Public Domain Mark 1.0 (https://creativecommons.org/publicdomain/mark/1.0/) [sourced: `mods:accessCondition` in the METS record, the working folder's copy of 24 Nov 2026, read 25 Nov 2026]. **No images are committed**; the URLs above are cited instead.
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
8. Separate judge: **not run.** This session could not start a separate judge (the headless CLI returned an authentication error, `keyleaf/RUN_RECORD.tsv` step 4). The packet is ready: `keyleaf/judge/BRIEF.txt` (frozen) and `keyleaf/judge/decode.txt` (a copy of the decode). Until a separate judge has scored it, **no S/E/N figure, no read share and no class is claimed for pass 2**; the method is "read with known key".

Exposure, stated plainly: the transcriber of the pentacles knew the key leaf and the first-pass key, so the shapes were recognised as letters while transcribing; in places the expected Latin will have steered the choice between similar shapes (named in the pentacle transcription only where a doubt was noticed). None of the pass-2 figures is a held-out figure.

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

Per pentacle (decode as produced; no emendation; letters a-z; z and shuffle counts from `keyleaf/work/shuffle_keyleaf_out.txt`; the judge's S/E/N column is to be added when a separate judge has scored `keyleaf/judge/decode.txt`):

| pentacle | folio (canvas) | decode (pass 2, no emendation) | letters | in lexicon (pointer) | z, seed 20261112 / 7 | shuffles >= real, both seeds |
|---|---|---|---|---|---|---|
| S1-011 | f. 35r (c073) | portanti nullum uulnus lethale fieri potest | 38 | 23 (60.5%) | 6.8 / 6.8 | 0/5000, 0/5000 |
| S1-012 | f. 35r (c073) | dat bonam fortunam et morbotus pericula tollit | 40 | 32 (80.0%) | 6.7 / 6.8 | 0/5000, 0/5000 |
| S1-013 | f. 35r (c073) | huic omns furiae obedietn atque potentiae ifernales | 45 | 18 (40.0%) | 5.1 / 5.0 | 0/5000, 0/5000 |
| S1-014 | f. 35r (c073) | neine praetet creatore [?] deum timebit | 31 | 12 (38.7%) | 5.5 / 5.5 | 0/5000, 0/5000 |
| S1-015 | f. 36r (c075) | huic obedietn omnes spiritus et potentiae infernales | 46 | 28 (60.9%) | 7.0 / 6.7 | 0/5000, 0/5000 |
| S1-016 | f. 36r (c075) | obedietn tibit omnes creatuae et potentiae infernales | 47 | 16 (34.0%) | 6.8 / 6.6 | 0/5000, 0/5000 |
| S1-017 | f. 36r (c075) | contra inimicos serpentes et ua[?]mones tutissimum | 42 | 25 (59.5%) | 6.7 / 6.7 | 0/5000, 0/5000 |
| S1-018 | f. 36r (c075) | hoc signum portauit adam in fronte contra pericula | 43 | 43 (100.0%) | 7.8 / 7.9 | 0/5000, 0/5000 |
| S1-019 | f. 36r (c075) | ad sanguuinus fluxum respringendum optimum remedium | 46 | 23 (50.0%) | 6.2 / 6.0 | 0/5000, 0/5000 |
| S1-020 | f. 36r (c075) | furta reuelat conspirationes et secreta consilia hominum | 50 | 29 (58.0%) | 8.0 / 7.9 | 0/5000, 0/5000 |
| S1-021 | f. 37r (c077) | canitar~ confert et singularem fortunae gratiam | 41 | 34 (82.9%) | 8.3 / 8.5 | 0/5000, 0/5000 |
| S1-022 | f. 37r (c077) | deuu mihi adiutor quem tinebo et uiuam | 32 | 22 (68.8%) | 5.8 / 5.8 | 0/5000, 0/5000 |
| S1-025 | f. 37r (c077) | p[?]m[?] cou odium et magii[?]ines uerit | 26 | 8 (30.8%) | 4.1 / 4.1 | 0/5000, 0/5000 |
| S1-027 | f. 38r (c079) | hoc signum tecum sit et n~ timebus aduersarios | 38 | 30 (78.9%) | 7.2 / 7.0 | 0/5000, 0/5000 |
| S1-028 | f. 38r (c079) | quo die hoc signum uiderus liber erus ab [?]ipediment | 42 | 22 (52.4%) | 6.0 / 5.9 | 0/5000, 0/5000 |
| S1-030 | f. 38r (c079) | per hoc nomen treumnt omnes potestates infernales [?] | 43 | 16 (37.2%) | 6.4 / 6.3 | 0/5000, 0/5000 |
| S1-031 | f. 38r (c079) | hoc signum faciet omnes erga te mites et ben[?]uolos | 41 | 36 (87.8%) | 7.2 / 7.0 | 0/5000, 0/5000 |
| S1-032 | f. 38r (c079) | huic signo se subi[?]unt omnes creatuae uanimuque uiren | 45 | 20 (44.4%) | 5.5 / 5.5 | 0/5000, 0/5000 |
| S1-033 | f. 39r (c081) | nec a gladio nec a subitania morte tinebius | 36 | 19 (52.8%) | 5.7 / 5.6 | 0/5000, 0/5000 |
| S1-037 | f. 39r (c081) | cum hoc signo n~ peribis ferro nec igne | 31 | 23 (74.2%) | 5.3 / 5.1 | 0/5000, 0/5000 |
| S1-038 | f. 39r (c081) | omne timoris occasione auerti et conuerti | 36 | 30 (83.3%) | 6.6 / 6.5 | 0/5000, 0/5000 |
| S1-039 | f. 40r (c083) | contra maleficia et quemacunque praestigiau terla | 44 | 17 (38.6%) | 6.6 / 6.6 | 0/5000, 0/5000 |
| S1-041 | f. 40r (c083) | hoc signum facit contra s[?]tena uim et potestat[?] | 38 | 26 (68.4%) | 6.8 / 6.9 | 0/5000, 0/5000 |
| S1-044 | f. 40r (c083) | hoc signo sigilauit salomon da[?]mone in puteo | 37 | 14 (37.8%) | 5.7 / 5.7 | 0/5000, 0/5000 |
| S1-045 | f. 41r (c085) | contra metum et tiiore hoc signum habet efficaciam | 43 | 37 (86.0%) | 6.8 / 6.7 | 0/5000, 0/5000 |
| S1-049 | f. 41r (c085) | quicunque hoc signum portat diliget ab omnibus | 40 | 33 (82.5%) | 7.5 / 7.3 | 0/5000, 0/5000 |
| S1-051 | f. 42r (c087) | amabile facit tanquam ipsum deum et odium diurumpit | 44 | 28 (63.6%) | 6.3 / 6.4 | 0/5000, 0/5000 |
| S1-052 | f. 42r (c087) | pro imoris onfficina adirabale est hoc signum | 39 | 15 (38.5%) | 5.6 / 5.6 | 0/5000, 0/5000 |
| S1-055 | f. 42r (c087) | pro auxilio impetrando hoc signum bonum est | 37 | 27 (73.0%) | 7.2 / 7.2 | 0/5000, 0/5000 |
| S1-057 | f. 43r (c089) | a periculis liberabiit qui hoc signum gestat | 38 | 28 (73.7%) | 7.6 / 7.6 | 0/5000, 0/5000 |
| S1-063 | f. 44r (c091) | uulnera qque dei sunt medicina mei amen | 33 | 29 (87.9%) | 4.6 / 4.6 | 0/5000, 0/5000 |
| S1-064 | f. 44r (c091) | timor deus et totius mundi sancta mabiestus | 37 | 28 (75.7%) | 5.3 / 5.2 | 0/5000, 0/5000 |
| S1-065 | f. 44r (c091) | contra area et hostes i bello signum optimum | 37 | 37 (100.0%) | 6.4 / 6.4 | 0/5000, 0/5000 |
| S1-069 | f. 45r (c093) | hoc signum bonum est ftra dolore matricos | 35 | 23 (65.7%) | 6.3 / 6.3 | 0/5000, 0/5000 |
| S1-070 | f. 45r (c093) | contra uen[?]num est et mobtus incidenidia remedium | 42 | 25 (59.5%) | 5.3 / 5.2 | 0/5000, 0/5000 |
| S1-071 | f. 45r (c093) | portatum facit ftra inimicos et insidiator | 37 | 15 (40.5%) | 6.0 / 6.0 | 0/5000, 0/5000 |
| S1-072 | f. 45r (c093) | cum hoc signo in carcere detineri n~ potes | 34 | 25 (73.5%) | 6.2 / 6.0 | 0/5000, 0/5000 |
| S1-073 | f. 45r (c093) | contra mortus repentinae periculum optimum est | 41 | 35 (85.4%) | 7.8 / 7.6 | 0/5000, 0/5000 |
| S1-074 | f. 45r (c093) | hoc signum animum et animam confortat aduersus peric[?] | 45 | 31 (68.9%) | 7.8 / 7.7 | 0/5000, 0/5000 |
| S1-078 | f. 46r (c095) | mulier cum hoc signo n~ peribit in partu | 32 | 24 (75.0%) | 6.0 / 6.0 | 0/5000, 0/5000 |
| S1-079 | f. 46r (c095) | porta tecum hoc signum et inimici tus er[?] imore cedetn | 44 | 31 (70.5%) | 5.6 / 5.5 | 0/5000, 0/5000 |
| S1-080 | f. 46r (c095) | qui hoc signum habet a nemine laedi potest amen | 39 | 34 (87.2%) | 7.3 / 7.0 | 0/5000, 0/5000 |
| S1-081 | f. 47r (c097) | hoc sinum est contra omnia phantasmata re[?]ia homine graitsum | 51 | 28 (54.9%) | 6.7 / 6.6 | 0/5000, 0/5000 |
| S1-082 | f. 47r (c097) | incdo cit amore et ben[?]uolentiam apud omnes | 36 | 22 (61.1%) | 6.5 / 6.5 | 0/5000, 0/5000 |
| S1-084 | f. 47r (c097) | portante ab aquae et mabrius periclo soluit | 37 | 22 (59.5%) | 5.7 / 5.6 | 0/5000, 0/5000 |
| S1-085 | f. 47r (c097) | ecc[?] figua agni dominantus super omnes potestates | 42 | 14 (33.3%) | 7.1 / 7.0 | 0/5000, 0/5000 |
| S1-087 | f. 48r (c099) | cum hoc signo n~ timebius inimicos nec maleficia nec da[?]mones | 50 | 34 (68.0%) | 6.5 / 6.3 | 0/5000, 0/5000 |
| S1-090 | f. 48r (c099) | in bello securus erus cum hoc signo | 29 | 25 (86.2%) | 5.7 / 5.8 | 0/5000, 0/5000 |
| S1-091 | f. 48r (c099) | ab inimicos nos tutos reddit et inuincibiles | 38 | 26 (68.4%) | 5.2 / 5.2 | 0/5000, 0/5000 |
| S1-092 | f. 48r (c099) | in quocunque die hoc signum portau[?] a periculo liber | 43 | 37 (86.0%) | 7.0 / 7.1 | 0/5000, 0/5000 |
| S1-095 | f. 49r (c101) | screptum in ca[?]te n~ nata et portatum manu leua indicit mirabalia | 53 | 21 (39.6%) | 6.6 / 6.6 | 0/5000, 0/5000 |
| S1-096 | f. 49r (c101) | ad honc signum uenietn spiritu et obedietn tibi | 40 | 21 (52.5%) | 5.0 / 4.9 | 0/5000, 0/5000 |
| S1-097 | f. 49r (c101) | hoc signum portabit aron in fronte et liberat ab igne | 44 | 25 (56.8%) | 6.7 / 6.6 | 0/5000, 0/5000 |
| S1-098 | f. 49r (c101) | contra morte subitaneam hoc signum est accommodatum | 45 | 35 (77.8%) | 8.1 / 8.1 | 0/5000, 0/5000 |
| S1-099 | f. 50r (c103) | cum hoc signo mo[?]te subitanea n~ peribius | 33 | 13 (39.4%) | 4.8 / 4.7 | 0/5000, 0/5000 |
| S1-102 | f. 50r (c103) | super aspidde et basiliscum ambulabis et conculcabis leone et dracone | 60 | 16 (26.7%) | 6.6 / 6.6 | 0/5000, 0/5000 |
| S1-103 | f. 50r (c103) | sacto columbo sacrum est hoc signum et confect uictoria | 47 | 35 (74.5%) | 7.0 / 7.0 | 0/5000, 0/5000 |
| S1-105 | f. 51r (c105) | ecc[?] figua et facies per quod omnia facta sunt cui omnes obedi[?] | 50 | 37 (74.0%) | 7.5 / 7.5 | 0/5000, 0/5000 |
| S1-106 | f. 51r (c105) | cum hoc signo nec uinculus nec compedibus teri potes | 44 | 22 (50.0%) | 6.6 / 6.5 | 0/5000, 0/5000 |
| S1-107 | f. 51r (c105) | signum sacti gregorii contra uen[?]num et maleficia | 42 | 29 (69.0%) | 6.8 / 6.9 | 0/5000, 0/5000 |
| S1-109 | f. 51r (c105) | hoc signo sanguine perd[?]e nemo potest tutum est | 39 | 39 (100.0%) | 6.2 / 6.1 | 0/5000, 0/5000 |
| S1-110 | f. 51r (c105) | qui hoc signum portauerit nulla pericula timebit | 42 | 25 (59.5%) | 7.6 / 7.5 | 0/5000, 0/5000 |
| all 62 | ff. 35r-51r | | 2520 | 1597 (63.4%) | 10.5 / 10.3 (section) | 0/5000, 0/5000 |

Sum check: the 62 rows add to 2,520 letters and 1,597 lexicon letters [measured]. What the rims say, from the decode and unchecked [unverified]: protection and power formulas ("hoc signum portat ...", "contra maleficia ...", "cum hoc signo non peribis ..."), Ps 91:13 on no. 102 ("super aspidem et basiliscum ambulabis et conculcabis leonem et draconem"), Salomon sealing the demon in a well (no. 44), Adam and Aaron bearing the sign on the forehead (nos. 18, 97).

## Remaining gaps

- Holes in the three decoded passages of the first pass, 112 of 225 words (H1 42 of 77, H2 63 of 133, H3 7 of 15) - blocker: not-attempted; key faults the judge's errors show (the sign 1 where the sense wants a; r or rr for te or i; irr for Xri; c for h; final t as n). Pass 2 (`keyleaf/`) applies the key leaf to the same transcriptions; the transcription faults behind several of these (1 for a) are not re-read.
- Pass 2 has no separate judge's scores yet - blocker: not-attempted; the packet `keyleaf/judge/BRIEF.txt` + `keyleaf/judge/decode.txt` is frozen and ready; this session could not start a separate judge. No read share or class is claimed for pass 2 until it is scored.
- 1 of the 8 first-pass `?` signs is still not identified (f. 4r l. 17, a small reversed-e loop joined to a looped delta; not on the key leaf) - blocker: no-key-material; the leaf has no such sign.
- Pentacles with no clear counterpart still not transcribed: the second series ff. 52r-54r (nos. 1-12 and the four figures on f. 54r, several with two rings and numerals), the two magic-mirror figures f. 97r-v, and signs written inside circles of the first series (e.g. nos. 62, 101) - blocker: not-attempted; images fetched (`keyleaf/IMAGE_FETCH.tsv`), not transcribed in this pass.
- The rest of the volume's cipher text, ff. 3r-96v and ff. 158r-162r, apart from the passages transcribed here - blocker: not-attempted; the clear copy ff. 101r-155r and 166r-170r gives the same text per the catalogue.
- Inner dots (`*`) were not recorded on the first-pass leaves, so the two-dot sign there runs on the declared fallback of the pass-2 decoder - blocker: not-attempted; a re-transcription of those leaves with the dots would remove the fallback.
- Prior art in print: Skinner and Rankine 2008, Mathers 1889, Boudet's census - blocker: needs-physical-access; not opened; web searches found no mention of a Basel cipher copy.

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
- [ ] retry: in part. The 8 `?` signs were looked at (7 now labelled); the 62 inscribed first-series pentacle rims were transcribed and decoded; the judge's scoring of pass 2, the second-series pentacles, f. 97r-v and a re-transcription of the first-pass leaves with inner dots remain

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

Not committed: the page images, crops and contact sheets; the downloaded IIIF manifests, METS record, Steinmann PDF and catalogue HTML; `__pycache__`. They are in the stamp manifest where it lists them.

Made here (25 Nov 2026): `transcription.txt` (the five files of `tx/` that `FREEZE_TX.txt` lists, put together unchanged), `reading.md`, `translation.md`, `validation.tsv` (input for `docs/_validate.py`), `profile.json`, this file. No images.

Name: the folder is `baselanv9`, in lower case as the site's page slugs and checkers require. The working folder (`basel_anv9`) and the files copied from it call the target `baselANV9`; they are left unchanged, so their hashes still hold.

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person has read the signs or the text without AI.
- One transcription, one reader, one pass. The training leaves were transcribed with the clear copy beside them, and the held-out leaves by a reader who knew most of the system; the held-out passages test the key, not the transcriber.
- The judge was a model session scoring sense by its own lights; its separation from the solver is stated, not shown.
- The reading and the translation were made after the clear copy had been seen, and are unchecked.
- Three passages on parts of three pages, out of about 100 leaves of cipher (ff. 3r-97v and 158r-162r, by the catalogue's foliation): the figures say nothing yet about the rest.

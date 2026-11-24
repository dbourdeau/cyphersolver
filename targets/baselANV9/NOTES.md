# baselANV9: Clavicula Salomonis and Septem sigilla planetarum in a secret alphabet, Basel UB, UBH AN V 9 (17th century)

Status: in progress. Contributed by pull request, not yet written up, and a new target: the volume is in neither `catalogue.json` nor `research/leads.json`. The key was recovered from cipher ff. 4r-4v aligned with the volume's own clear copy, frozen, and used for one decode of three held-out passages. A separate strict judge finds 747 of 1,138 decoded letters in words that read as sense (65.6%: H1 62.4%, below the contributor's own 65% line; H2 67.0%; H3 69.6%), and the decode reproduces 988 of 1,231 letters of the clear copy (80.3%). Counted in words, 113 of 225 read as sense (0.502) and no sentence is clean, so each passage is "decoded, not read" and the target is filed not read: key recovered from adjacent plaintext, text not read. The volume's own key leaf, viewed only after the decode, agrees on 46 of the 52 values it covers. The page, ledgers, DECODE queue entry and any catalogue or lead entry are left to the maintainers.

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

Statistical validation (`docs/_validate.py baselANV9 --write`, 25 Nov 2026, model `la`, order 4 without spaces; `validation.tsv`) [measured]: 1,024 read tokens, 49 types; the reading scores -2.639 per letter; random keys of the same structure -4.459 (sd 0.366, z 5.0, n 200); a key annealed onto shuffled ciphertext at best -2.782 (mean -2.817, z 6.5); **verdict: pass**. The annealer started from random keys on the real text reaches -2.553, higher than the reading: the letter model alone does not single out this key. `validation.tsv` was made here from the frozen key and the transcriptions, and reproduces `DECODE.txt` on 37 of 37 lines.

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

## Remaining gaps

- Holes in the three decoded passages, 112 of 225 words (H1 42 of 77, H2 63 of 133, H3 7 of 15) - blocker: not-attempted; key faults the judge's errors show (the sign 1 where the sense wants a; r or rr for te or i; irr for Xri; c for h; final t as n) and the placeholder value of ?; an amended key (the key leaf, more training) and a second decode would close many, reported apart from the first pass of record.
- 10 held-out tokens with no key value (Oei~ 3, Bx@ 2, Pe~, 5b~, Yy, Sz, Ec) - blocker: not-attempted; none occurs in the training leaves; the key leaf gives some (quae), not applied here.
- 8 signs transcribed ? (not identified), 1 in training and 7 held out - blocker: not-attempted; not re-read on the image after the decode (freeze rule); see "Transcription doubts".
- The rest of the volume's cipher, ff. 3r-96v (conjurations, pentacles on ff. 33r-55v and 97r-v) and ff. 158r-162r (Septem sigilla), apart from the passages transcribed here - blocker: not-attempted; not transcribed or decoded; the clear copy ff. 101r-155r and 166r-170r gives the same text per the catalogue.
- Pentacle inscriptions with no clear counterpart, about 112 by the contributor's session's count (not counted here) - blocker: not-attempted; new text, not transcribed or decoded yet; the two rims decoded here do have a counterpart on f. 123r.
- Prior art in print: Skinner and Rankine 2008, Mathers 1889, Boudet's census - blocker: needs-physical-access; not opened; web searches found no mention of a Basel cipher copy.

## Transcription doubts

Doubts were not settled against the image after the decode: under the freeze rule no sign was changed, and none was re-read. Each is listed with what the frozen key gives.

- ? (f. 4r l. 17, training, last word "6 ? Dl@") - read: not identified; checked: decode (the training alignment gives i, the source of the key's placeholder value ? = i); image not re-read.
- ? (f. 15r l. 5, third word "? Bx Tk^@") - read: not identified; checked: decode; gives iorum, a one-letter slip for eorum; image not re-read.
- ? and ? (f. 15r l. 9, third word "Lm ? Dl_ 8 X Ea ?") - read: not identified; checked: decode; gives aiunciai (no sense; the clear copy has annuntiationem); image not re-read.
- ? (f. 159r l. 3, third word "3_ ? Bx 6s X Ds Ea^") - read: not identified; checked: decode; gives dniositam (no sense; clear dispositam); image not re-read.
- ? (f. 159r l. 7, second word "X_ ? D2 8 D3 6_") - read: not identified; checked: decode; gives iniicoen (no sense; clear inspiciens); image not re-read.
- ? (f. 159r l. 22, last sign of the fourth word "Am 6s 6 Oe Dl 6 ?") - read: not identified; checked: decode; gives consequei, a slip for consequetur; image not re-read.
- ? (f. 34r pentacle 4, fifth word) - read: a bold barred 4-like sign, possibly a planet sign (`SIGNS.md`); checked: decode; gives i (no sense; the clear copy has non); image not re-read.
- Marks not recorded (`SIGNS.md`): an inner dot in Bx, a dot inside Lm, a dot in the crossing of X - read: not recorded; checked: decode (the key gives o, a, i whatever the dot); whether the dots carry a value is open; image not re-read.

## Escalation

- [x] siblings: the volume itself: its clear copy (used for the key) and its key leaf f. 99r with the German translation f. 98r (viewed after the decode; 46 of 52 values agree); no other manuscript of this secret alphabet found (`PRIOR_ART.md`)
- [x] clear-pages: the clear copy ff. 101r-155r and 166r-170r is the plain text of the cipher (catalogue); used for training (ff. 101r-102r) and, after the decode, for scoring (ff. 109v, 167r, 123r)
- [x] known-keys: the volume's own key leaf, compared after the decode (`work/keyleaf_vs_key.tsv`); no other key known
- [x] print: no edition or study of this cipher found (`PRIOR_ART.md`); Skinner and Rankine, Mathers and Boudet's census not opened
- [ ] key-rebuild: not done. The key leaf gives values the training leaves never met and differs on 4 values (Lmt at, Dl@ us, Oe~ quem, D3 a positional rule); its os, a box with a big loop, may be the unvalued Bx@ of H1 (sanct[?], u[?]: sanctos, uos in the clear copy) [derived, not checked on the image]. Applying the leaf is a second decode, to be reported apart from the first pass of record
- [ ] retry: not done. The 8 unidentified signs and the slips are not re-read on the image (freeze rule); a second transcription pass, and a decode of the remaining cipher pages with the frozen key, are the next steps

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

## Limits

- Model sessions did all the work: transcription, key recovery, decode, judge, reading and translation. No person has read the signs or the text without AI.
- One transcription, one reader, one pass. The training leaves were transcribed with the clear copy beside them, and the held-out leaves by a reader who knew most of the system; the held-out passages test the key, not the transcriber.
- The judge was a model session scoring sense by its own lights; its separation from the solver is stated, not shown.
- The reading and the translation were made after the clear copy had been seen, and are unchecked.
- Three passages on parts of three pages, out of about 100 leaves of cipher (ff. 3r-97v and 158r-162r, by the catalogue's foliation): the figures say nothing yet about the rest.

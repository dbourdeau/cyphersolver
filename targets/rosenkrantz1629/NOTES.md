# rosenkrantz1629: Palle Rosenkrantz's relations from London, 1628-29 (Rigsarkivet, TKUA England A II 13, unit 261258); code A in his letters of 2 and 15 February 1629 to the Statholder Frands Rantzau

Status: in progress. Contributed by pull request, not yet written up: the letter figures of code A were recovered from the main letter of 2 February 1629 alone, frozen, and used for one decode of all code A text (strict judge: held-out 127 of 136 letters, 93.4%; training 305 of 370, 82.4%; all 432 of 506, 85.4%; 0 of 5,000 shuffled keys as good, at two seeds). The 48 word codes are not solved. By the README read bar, counted in words over the cipher words only, 95 of 179 words read as sense (0.531), so the target is filed read in part. Code B and the sign cipher to the king, in the same folder, are not broken. This is a new target, found from a Zobel lead; it is not in `catalogue.json`. The page, ledgers, DECODE queue and catalogue are left to the maintainers.

Contributed by Malcolm McBratney (Brisbane), working with Claude (Anthropic): Claude Fable 5.2 and Claude Opus 5.5 the solver sessions, Claude Opus 5.5 the strict judge and the assembly of this folder.

Provenance tags: [measured] = counted or hashed from the files in this folder; [derived] = worked out from them; [sourced] = from a named source; [stated] = given by the contributor's working sessions, not checked here; [unverified] = a reading of the text not checked by anyone else. Times are UTC on 24 Nov 2026 from the sandbox clock; the assembly was made on 25 Nov 2026, Brisbane time.

## The source

Rigsarkivet (Copenhagen), Tyske Kancelli, Udenrigske Afdeling, England A II 13 (1620-34), folder "Relation fra Palle Rosenkrantz 1628-1629" (cover, image 263); Arkivalieronline unit 261258 [sourced: the folder cover and the unit's image list, `pass1/WORKLOG.md`, `FETCH_LOG.txt`]. Images 263-293 hold 15 letters: two in clear, six in number codes to the Statholder Frands Rantzau and the Chancellor Christian Friis, and seven in a sign cipher to the king, Christian IV [measured: `pass1/REPORT.md`, `pass1/WORKLOG.md`; the clear Kurrent was read by a model at 2000 px, not collated].

Code A is used in two letters to the Statholder (the addressee from the salutation "Kiere Her Statholder och kiere Broder" and the address panel) [measured: `pass1/WORKLOG.md`]:

- **L2**, "Aff London d. 2 Febr. 1629" (270L), images 266R-270L: the main letter on 266R, 267L, 268R, 269L, 269R, 270L, and a postscript leaf bound inside it, 267R-268L. In clear the writer says the king's letter is "y Zifre" and asks the Statholder to decipher it himself.
- **L5**, 15 February 1629, images 274R-276L, cipher on 275R and 276L.

Images: **none are committed.** The openings were fetched at full size (4416-4435 x 3436 px) from Arkivalieronline; the URLs and status codes are in `FETCH_LOG.txt` [measured].

Length [measured]: `python docs/_check_profile.py --measure transcription_L2.txt --drop-first --digits` gives 509 tokens with a digit, and `transcription_L5.txt` gives 66. Less the writer's struck groups ([del:246] in L2; [del:87 33 85], three tokens, in L5) that is 508 + 63 = 571 cipher tokens: 412 in the main letter (A1), 96 on the postscript leaf (A1P), 63 in L5 (A2), as `pass2/FREEZE_TX_CODE_A.txt` records. Of the 571, 500 are figures below 200 (66 distinct), 70 are 200 or more (51 distinct: 48 word codes and three figures read as h), and one has its first digit unread (?3).

## The system: code A (`pass2/codeA/KEY_A.tsv`)

A homophonic number cipher with a nomenclator [derived: the key and the decode]:

- Figures 3-199 stand for letters, several per letter. They sit on a 9-column grid: each letter's figures step by 9, and along each row of figures with the same value mod 9 the letters rise in alphabetical order (`pass2/ATTEMPTS.tsv` P2-004). The solver of record was held to that order for figures below 200.
- The frozen key gives 66 letter values for 20 letters [measured]:

| letter | figures | letter | figures | letter | figures | letter | figures |
|---|---|---|---|---|---|---|---|
| a | 3, 11, 30, 31 | f | 155, 164 | m | 48, 94, 103, 111 | s | 44, 52, 60, 171, 193 |
| b | 39, 56 | g | 173, 181, 190, 199 | n | 130, 139, 148 | t | 69, 78, 87 |
| c | 65, 74, 83 | h | 308, 317, 1135 | o | 157, 166, 175 | u | 96, 105, 114, 133, 141 |
| d | 36, 91, 100, 109 | i | 5, 14, 33 | p | 184 | y | 177, 186, 195 |
| e | 118, 137, 146, 154, 163 | k | 41, 50 | r | 7, 16, 35 | | |
| | | l | 67, 76, 85, 191 | | | | |

- Figures from 200 up stand for words or names: 33 in the training letter, 48 distinct (62 tokens) in the two letters, none solved. The solver read three high figures, 308, 317 and 1135, as h ("at holde", "holt", "har", "och").
- Figures not seen in training are decoded by rules written before the decode (`pass2/codeA/RULES_A.txt`): a figure below 200 takes the letter of its two grid neighbours when they agree, else "?"; a figure of 200 or more is a word code. Three figures below 200 occur only in held-out text: 136 (rule 2 gives e), 63 and 81 (no value).
- The writer separates the figures with full stops; the transcription uses spaces. The cipher has no word breaks; doubled letters are written twice [derived].

## Other systems in the folder: not broken

- **Code B**, a larger number code (word codes up to 2431) in four letters of 13-24 March 1629: to the Statholder (280R-281L, 289L) and to the Chancellor (283R-284L, with the same ciphered sentences as 280R-281L; 284R-285L). 273 tokens, frozen in `pass2/tx/CODE_B_FROZEN.tsv`. The margin of 289L reads "NB. detta er effter dj sidste Ziffer som jeg sende med Christen Clementsön" (a model's reading; the first pass read "Clemetsen"). The code A key does not fit it, and grid, modulus, register-layout and annealing attacks failed (`pass2/ATTEMPTS.tsv` P2-012 to P2-017, P2-022).
- **The sign cipher** of drawn signs and digits in seven letters to the king (No. 12, 13, 14, 20, 21, 22, 23; 2 February to 9 April 1629). 408 tokens, 63 types, 49 labels, frozen in `pass1/TRANSCRIPTION.tsv` with `pass1/SIGNS.md`. 24 solver runs gave no Danish; a planted-key control shows the solver recovers 21 and 28 sign classes and fails at 36 on text of this size (`pass1/SOLVE_LOG.md`). The best candidate, frozen as a failed candidate (`pass1/KEY.tsv`), does no better than shuffled keys on the held-out letters (1,360 and 1,407 of 5,000 at or above it, `pass1/shuffle_out.txt`). Its judge packet (`pass1/judge/`) was prepared; no scores were recorded. A manuscript key by Temler to Christian IV's own sign cipher of 1625-27 exists (Royal Library, Kallske Saml. 4to 436; Bricka and Fridericia vol. 1 p. 408 note) and was not reached: whether it is this alphabet is unknown.
- **Book codes** were tested for codes A and B and ruled out (seven printed books in nine texts, Beale-type keys at every offset, a planted-key positive control; `bookcode/ATTEMPTS.tsv`).

## Method

The pipeline is the contributor's: prior art first, frozen transcription and key, one decode, a separate strict judge, a shuffle control. The working folder is `/home/claude/keyless/rosenkrantz1629/`; its first session is in `pass1/` here, the second in `pass2/`, the second reader's transcription in `bookcode/`.

1. **Prior art** before transcription: `PRIOR_ART.md` items 1-6, and items 7-12 from the second session. No key, decipherment or printed reading of these letters found (see "Prior art" below).
2. **Period keys** of the Rigsarkivet "Chiffer" packet (unit 260610, images 123-200 and 305-309) compared with both number codes and the sign cipher before transcription: none fits (`pass1/REPORT.md`, `pass1/WORKLOG.md`; again in pass 2, P2-018 and P2-021).
3. **Transcription of code A** (`pass2/tx/CODE_A_FROZEN.tsv`) by one model reader from strips at 1.03-1.12x native, doubtful digits marked ?. Frozen at 11:53:54Z with the split (`pass2/FREEZE_TX_CODE_A.txt`, sha256 08867ad2..., matching the file here) [measured].
4. **Held-out design.** Training = the main letter A1 (370 decoded letters); held-out = the postscript leaf A1P and the letter of 15 February A2 (136 letters, 26.9% of 506). See "The exploratory run" below for what was seen before the key was frozen.
5. **Key from A1 only** (`pass2/ATTEMPTS.tsv` P2-003 to P2-009):
   - Unconstrained homophonic annealing on A1 (P2-003) converged; the converged key showed the grid order (P2-004).
   - Annealing held to the grid order with cascade moves (`pass2/tools/gsolve2.c`, problem files from `pass2/tools/mkprob2.py`), with figures of 200 or more allowed to be letters at a cost: costs 2, 3, 4 and 6 give the same letters for every figure below 200 (P2-008).
   - **Language model:** the solver's own Danish 5-gram character model (`pass2/tools/build_lm27.py`, Witten-Bell, word-anchored) from 576,754 letters of Christian IV's own Danish letters 1589-1635 in the Bricka and Fridericia OCR, German and Latin blocks filtered out (`pass1/tools/build_lm.py`). `lang/` has only a modern Danish model (da-modern, 1800-1920). The corpus (`lm/da1620.txt`, sha256 4191e4f574e832cc in the stamped manifest) and the model binary (`pass2/lm/da1620.bin`, 59 MB) are not committed [stated: the corpus and model are named in `pass1/REPORT.md` and `pass2/ATTEMPTS.tsv` P2-002].
   - **Key of record:** the cost-4 run, seed 1 (identical key at seed 2), score -911.353 (`pass2/runs/A1n_monoP4_s1.txt`, `_s2.txt`). `KEY_A.tsv` is that run's key, value for value (99 entries: 66 letters, 33 word codes) [measured]. No hand edits.
6. **Key frozen** at 12:24:05Z (`pass2/codeA/FREEZE_KEY_A.txt`: `KEY_A.tsv` 2b473d0d..., `RULES_A.txt` c8716d3b..., `decode_A.py` 8361997b..., and the transcription, all matching the files here) [measured]; then **one decode** of all code A text at 12:24:08Z (`pass2/codeA/decode_A.py` -> `pass2/codeA/DECODE_A.txt` and `pass2/judge/decode_A.txt`; `DECODE_RUN_TIME.txt`). No emendations: the first pass is the figure of record.
7. **Separate strict judge** (Claude Opus 5.5): saw only `pass2/judge/BRIEF_A.txt` and `pass2/judge/decode_A.txt`; scored every decoded letter S (sense), E (one-letter slip in a readable word) or N (no sense), with its word split of each line (`pass2/judge/judge_A.tsv`). `pass2/judge/count_A.py` re-adds it [measured, re-run here].
8. **Shuffle control** (`pass2/codeA/shuffle_A.py`, `shuffle_A_out.txt`): 5,000 shuffled keys per seed, letters permuted among the letter figures, word codes kept, scored with the same model.
9. **Time-stamps** (`stamps/`): a sha256 manifest of the working folder (641 files) made at 21:18:02Z, stamped by RFC 3161 at Sectigo (21:18:02 GMT) and FreeTSA (21:18:03 GMT); OpenTimestamps first failed, and the manifest was submitted again at 21:24:46Z (`stamps/MANIFEST.sha256.ots`, pending at four calendars) [measured: `stamps/STAMP_LOG.txt`, and the digests checked here].

The scripts keep the working folder's paths (`/home/claude/keyless/rosenkrantz1629/...`) and do not run from this folder as they stand.

### The exploratory run, and what it means for the held-out test

- **Disclosed slip (P2-002):** before the transcription freeze and before any split, one exploratory annealing run was made on all code A text, and its decode of every line, held-out lines included, was seen by both solver sessions (`pass2/tmp/A1_run1.txt`, kept here). It read as Danish.
- The transcription was not changed after it: the draft that run used (`tx/CODE_A_v1.tsv`, last written at 11:49:58Z; the run's output is from 11:52:45Z) is byte-identical to the frozen file of 11:53:54Z (the stamped manifest lists both with sha256 08867ad2...) [measured; the file times are the sandbox's, not time-stamped].
- **Glance at held-out figures:** while checking the contexts of 308, the session that froze the key also looked at the figures of one held-out line, 267R line 9 (`FREEZE_KEY_A.txt`).
- The key of record is mechanical output from A1 only. The exploratory key and the key of record agree on 51 of the 63 figures below 200 they share. For the three figures that occur only in held-out text, the key of record does not carry the exploratory values: the exploratory key has 136 = n and 63 = d; the frozen rules give 136 = e and 63 no value [measured]. What cannot be shown blind is that the solver settings chosen after the exploratory run (the grid constraint, the cost for high figures) were chosen without regard to how the held-out text read.
- **Order of events:** `FREEZE_KEY_A.txt` lists the key, rules, decoder and transcription, not the decode. Everything was stamped together at 21:18:02Z, about nine hours after the decode, so the order (transcription freeze 11:53:54Z, key freeze 12:24:05Z, decode 12:24:08Z) rests on the contributor's record and the file times.

### The solver's report

`pass1/REPORT.md` is the first session's report: the survey, the period keys and the failed sign-cipher attack ("No key. No reading."). It was written before the second session broke code A. The second session left no report: its record is `pass2/ATTEMPTS.tsv`, the freeze files and the judge's scores, from which this file was written by the assembling session.

## Figures (first pass of record)

Strict judge, letters (`pass2/judge/judge_A.tsv`, re-added by `pass2/judge/count_A.py`) [measured]:

| part | split | S | E | N | letters | S share |
|---|---|---|---|---|---|---|
| A1, main letter of 2 Feb, images 266R-270L | training | 305 | 37 | 28 | 370 | 305/370 = 82.4% |
| A1P, postscript leaf, 267R-268L | held-out | 76 | 0 | 4 | 80 | 76/80 = 95.0% |
| A2, letter of 15 Feb, 275R-276L | held-out | 51 | 5 | 0 | 56 | 51/56 = 91.1% |
| held-out total | | 127 | 5 | 4 | 136 | **127/136 = 93.4%** |
| all | | 432 | 42 | 32 | 506 | **432/506 = 85.4%** |

Sums: 370 + 80 + 56 = 506; 305 + 76 + 51 = 432; 37 + 0 + 5 = 42; 28 + 4 + 0 = 32 [measured]. Our own line is 65% S on the held-out block. The lowest lines: training 267L line 14 (S 0 of 6, "fuldmact", E), held-out 267R line 16 (S 0 of 2, "ag", N); per line in `judge_A.tsv`. The judge's caveat: the held-out sample is small and easy [stated by the contributor; not in `judge_A.tsv`].

The judge's E words (one-letter slips, 8 words, 42 letters), none emended: uidde (266R l.2), reste (266R l.3), fuldmact (267L l.13-14), holt (267L l.16), folade (268R l.6), oguer (268R l.15), lant (269R l.15) in training; ietet (275R l.3) held out, where the figure 136 is read e by rule 2 and the sense wants n (see "Transcription doubts").

The judge's N runs (no sense, 32 letters): eysteden (267L l.17-18), e (268R l.1), letan (268R l.2-3), feren (268R l.7-8), s (268R l.13), ster and e (269L l.3), o (269L l.4), re (270L l.2) in training; ag (267R l.16) and am (267R l.17) held out.

Shuffle control (`pass2/codeA/shuffle_A_out.txt`, re-run here with the same output) [measured]:

| split | letters | real key (per letter) | seed 20261112: mean, best, at or above real | seed 7: mean, best, at or above real |
|---|---|---|---|---|
| held-out A1P + A2 | 136 | -346.1 (-2.545) | -802.6, -669.5, 0 / 5,000 | -803.5, -667.0, 0 / 5,000 |
| training A1 | 370 | -882.9 (-2.386) | -2124.1, -1848.7, 0 / 5,000 | -2123.9, -1825.6, 0 / 5,000 |

Read share by words, the README read bar (`reading.md`, counted with `research/reading_audit/v10_relabel.measure_text`, cipher words only, `cipher_markup` ⟦⟧) [measured]:

| text | cipher words | read as sense | holes | read share |
|---|---|---|---|---|
| L2, 2 Feb (main letter and postscript leaf) | 160 | 84 | 76: 56 word codes, 11 N words, 2 tokens without a value, 7 E words | 0.525 |
| main letter alone | 123 | 65 | 58 | 0.528 |
| postscript leaf alone | 37 | 19 | 18 | 0.514 |
| L5, 15 Feb | 19 | 11 | 8: 6 word codes, 1 letter without a value, 1 E word | 0.579 |
| both letters | 179 | 95 | 84 | **0.531** |

Most of the holes are the nomenclator: 62 of the 84. The class is **read in part**: the letter table reads, the word codes do not. The sentence check (`docs/_check_reading.py`) is reported under "Checks made for this PR".

## Reading and translation

`reading.md` gives both letters as Danish sentences: the writer's clear text as transcribed, with the decoded cipher words in ⟦ ⟧ and every hole marked; `translation.md` gives the English. Both were made by Claude Opus 5.5 for the contributor and are **unchecked** by a person or a reader of seventeenth-century Danish [unverified]. The clear text in both rests on a loose, uncollated transcription.

Danish, two passages (reading.md, marks abridged):

> Siden er mig berett, att dj skulle ville ⟦[513] med mig⟧ om nogen ⟦afkortning af de [568]⟧ som ⟦resterer⟧ och siden ⟦betale⟧. (postscript leaf, held out)

> ... en stor omkostning, som ieg frycter, ⟦til forgefuis⟧, effterdj dett gaar endnu ⟦ietet(?) bedre til end [673] uar [1091]⟧. Och dett seer selsom ⟦ud med [1544] alting⟧ er och bleffuen ⟦uuist⟧ och ⟦lang[s]omt⟧. (15 February, held out)

English [unverified: the contributor's translation]: "Since then I have been told that they would [513] with me about some reduction of the [568] that remain outstanding, and then pay." "... a great expense, which I fear is in vain, since it still goes no better than [673] was [1091]. And it looks strange with [1544]; everything is and has become uncertain and slow."

The setting (Rosenkrantz's embassy to Charles I, the debts and subsidies owed to Christian IV, the Parliament of 1629) was not checked against any source beyond the cribs gathered in the working folder.

## Prior art

`PRIOR_ART.md` (copied unchanged). Searched 24 Nov 2026, before transcription and again in the second session: the gate record (Cyphersolver issues, PRs, catalogue and leads; DECODE public search, where "Rosenkrantz" gives three unrelated 18th-century records); Bricka and Fridericia, *Kong Christian den Fjerdes egenhændige Breve*, vols 1-7 (archive.org OCR; no Rosenkrantz letter of 1629 printed); Molbech 1848; the 47th Report of the Deputy Keeper of the Public Records (1886, p. 57: the folder calendared as "partly in cipher", no decipherment); Rigsarkivet's Daisy for key series; web searches; the repository (Rosenkrantz only as Niels Rosenkrantz, 1801-10). **No earlier key or reading of code A was found.**

Checked again for this PR (25 Nov 2026): `issues_index.tsv` and `issues_bodies.tsv` (931 and 210 lines, made 24 Nov 2026) give **0 hits** for Rosenkrantz, Rosenkrands, Rosencrantz, Rosenkranz, 261258, Palle, Rantzau and Statholder; the near hits are other Rigsarkivet targets of the same contributor (#456 Zobel, #450 and #483 Quem novit, #522 Pentz, #443 and #444 Petkum).

Open: Temler's key (KB, Kallske Saml. 4to 436), which bears on the sign cipher, not on code A; Molbech's page images (a plate of signs?); Danske Magazin; TNA SP 75 (Rosenkrantz's memorials of 14 Nov 1628 and 14 Feb 1629, cited by Beller 1928, per the working folder's crib notes); HathiTrust and Google Books full text. For the prior-art sheet: "Palle Rosenkrantz" with 1629 and Chiffer or Zifre; "Temler" with "Christian IV" and Chiffer; "Kallske Samling 436".

How the target was found: from the Zobel lead search of 24 Nov 2026 (the working folder `zobel_leads/`), which looked for more of Johan Zobel's cipher (targets/zobel1629) in unit 261258 and found Rosenkrantz's relations in a different cipher instead.

## Remaining gaps

- Word codes used more than once (568 seven times; 379 and 539 three times; 551, 673, 1444 and 1530 twice; 21 tokens) - blocker: no-key-material; no code A nomenclator was found in the Chiffer packet, the bound register or the Daisy key series; context suggests a field for some (568 is "lent" in "de laante [568]" and "outstanding" in "de [568] som resterer"), but a guess stays a hole.
- Word codes used once (41 values, 41 tokens; 15 of them only in held-out text) - blocker: too-short; one use gives no second context.
- Figures below 200 seen only in held-out text: 63 (no value; the sense wants s), 81 (no value), 136 (rule 2 gives e; the sense wants n) - blocker: too-short; absent from the training letter, one use each; see "Transcription doubts" for 63 and 136.
- No-sense runs (judge N: 32 letters) and one-letter slips (judge E: 8 words, 42 letters) - blocker: too-short; rare figures fitted on 370 training letters; two runs are tied to doubtful digits at 269L lines 3-4; none emended under the first-pass rule.
- Doubtful digits not settled on the image: ?3 (268R l.14, under an ink blot), 166 or 186 (269L l.4, overwritten), 100 or 106 (269L l.7), 136 or 130 (275R l.3), and the group read as clear "ey" (269L l.3) - blocker: illegible; read by a model on full-size archive images; a person's reading or the original would settle them.
- Code B, four letters of 13-24 March 1629 (273 tokens), not broken - blocker: no-key-material; a larger nomenclator, "the last cipher" the writer sent home; no key in the Chiffer packet or the register; ciphertext-only attacks failed.
- The sign cipher, seven letters to the king (408 tokens), not broken - blocker: needs-physical-access; Temler's key to Christian IV's sign cipher of 1625-27 is in the Royal Library and not online; ciphertext-only attacks failed, with a matched control.
- Prior-art gaps: Temler's key, Molbech's page images, Danske Magazin, TNA SP 75, HathiTrust and Google Books - blocker: needs-physical-access; not online or not searchable from the sandbox.

Not a gap in the text, but open: the repository's statistical validation (`docs/_validate.py`) has not run (see "Checks made for this PR").

## Transcription doubts

The doubts are the transcriber's own ? marks and every place where the second transcription (`bookcode/tx/NUM_FROZEN.tsv`, another session, frozen 12:07:11Z) differs. Each was looked at for this PR on the enlarged strip of the full-size image, without overlays, by the assembling model session (a model's reading, not a person's). By the freeze rule no sign of the frozen transcription was changed; the reading and the figures stay as decoded.

- 1739? (266R l.4) - read: 1739, last digit doubtful; checked: image, decode, transcription; the second reader has 1735; on the image the last digit is a 5-or-9 form with a flourish: not settled; a word code either way, no effect on the letters.
- 246 (267L l.7) - read: struck by the writer ([del:246]); checked: image, decode, transcription; the second reader takes it as a live group; on the image the middle digit is heavy and no clear stroke crosses the group: not settled; if live, one more word code ("ville herefter [246] [210] contribuere"), no effect on the letters.
- 1687 (267L l.16) - read: 1687; checked: image, decode, transcription; the second reader has 1087; on the image the second digit is a round loop crossed by a stroke from the line above, 6 or 0: not settled; a word code, no effect.
- ?3 (268R l.14) - read: first digit unread; checked: image, decode, transcription; the second reader has 83, which the key gives as c ("commendo"); on the image the first digit is under an ink blot: illegible here; the reading supplies [c] by sense and counts the word as a hole.
- 76 (268R l.18) - read: 76 (l); checked: image, decode, transcription; the second reader has 78 (t); on the image the second digit is this hand's 6 (one closed lower loop under a top stroke), not the two loops of an 8: 76 as frozen, giving "lande".
- ey? (269L l.3) - read: a clear word "ey", doubtful; checked: image, decode, transcription; the second reader has the group 109; on the image it is written like the 109 of the next line (1, an o-shaped 0, a y-tailed 9), so probably 109 (d); with it the run reads "sterde", still no sense (judge N): not settled.
- 166? (269L l.4) - read: 166 (o), doubtful; checked: image, decode, transcription; the second reader has 186? (y); on the image the middle digit is overwritten in heavy ink, likely an 8 written over another digit; 186 would give "saa haarde y deris" (so hard in their), where 166 gives the judge's N "o": not settled.
- 1679? (269L l.5) - read: 1679, last digit doubtful; checked: image, decode, transcription; the second reader has 1679; on the image the last digit is a 9-or-4 form beside a smudge: not settled; a word code, no effect.
- 100 (269L l.7) - read: 100 (d); checked: image, decode, transcription; the second reader has 106; on the image the third digit carries a rising stroke taller than the flick this hand puts on a 0 (compare 100 at l.5), so 106 cannot be ruled out; 100 gives "deris", 106 has no value in the key: not settled; a training letter, so at most one letter of the training figure.
- 595? (269L l.13) - read: 595, doubtful; checked: image, decode, transcription; the second reader has 595; on the image 595 with the last 5 small and raised: consistent with the frozen reading; a word code, no effect.
- 85 (269L l.14) - read: 85 (l); checked: image, decode, transcription; the second reader has 89?; on the image the second digit is this hand's 5 (as in 175 later in the line) with a small c-like mark above: 85 as frozen, giving "imellom".
- 859? (269L l.14) - read: one group 859, doubtful; checked: image, decode, transcription; the second reader has two groups, 85 and 9?; on the image there is no stop between 85 and 9, where stops part the other groups of the line: one group, as frozen; a word code, no effect.
- 31 (269R l.18) - read: 31 (a); checked: image, decode, transcription; the second reader has 30 (a); on the image the second digit is a short stroke beside a blot; both figures are a, no effect.
- 67 (267R l.9, held out) - read: 67 (l); checked: image, decode, transcription; the second reader has 87 (t); on the image the first digit is a 6, not the two closed loops of the 8 in 308 two groups before: 67 as frozen, giving "tage half".
- 81 (267R l.18, held out) - read: 81; checked: image, decode, transcription; the second reader has 81; seen on the strip at half size only; the key has no value for 81 and rule 2 cannot fill it: one unread token.
- 109 (267R l.19, held out) - read: 109 (d); checked: image, decode, transcription; the second reader has a clear word ("lang?") there; on the image the group is written like this hand's 109: a cipher group as frozen, giving "mod".
- 1863? (268L l.1, held out) - read: 1863, doubtful; checked: image, decode, transcription; the second reader has 1863?; on the image the third digit is partly blotted: not settled; a word code, no effect.
- 136 (275R l.3, held out) - read: 136; checked: image, decode, transcription; the second reader has 136?; rule 2 gives e ("ietet", judged a slip for intet); on the image the third digit is a loop with a stroke rising on its right, unlike this hand's 6 (ascender on the left, as in 69 beside it) and nearer the 0 of 130 in the next line; 130 is n in the key and would give "intet": not settled; the slip stays a hole.
- 63 (275R l.8, held out) - read: 63; checked: image, decode, transcription; the second reader has 63?; on the image the second digit is crossed by a descender from the line above but reads 3, not 0 (60 would be s); the key has no value for 63; the reading supplies [s] by sense ("lang[s]omt"), a hole.

Not listed: digits the second reader marks ? where both readers have the same figure (184, 186 at 268R l.17, 39, 14, 136 and 63 apart).

## Escalation

- [x] siblings: the whole folder (images 263-293) was surveyed; L2 and L5 are the only letters in code A; the other eleven cipher letters are code B or the sign cipher (not broken, above); the Zobel lead's survey of the neighbouring images and units noted one other number code (Wolffen, unit 261258 image 201, three lines), not compared with code A
- [x] clear-pages: every sheet was read at full size; no interlinear or marginal decipherment; the margins are the writer's clear Danish; the clear passages were used only to cut the cipher into runs, not as cribs
- [x] known-keys: the Chiffer packet (unit 260610, images 123-200 and 305-309, with the bound register of 151-200) and the Daisy key series were compared with code A before transcription and again in pass 2: none fits
- [x] print: Bricka and Fridericia vols 1-7, Molbech 1848, the 47th Deputy Keeper's Report, DECODE, web searches; not reached: Danske Magazin, TNA SP 75, HathiTrust and Google Books
- [x] key-rebuild: the letter table was rebuilt from the training letter (66 figures, 20 letters, grid order); the word codes cannot be rebuilt (41 of 48 used once, no codebook found); the held-out-only figures 63, 81 and 136 were left as the frozen rules give them
- [ ] retry: not done; the image check of the doubts made for this PR points to readings that would change letters (269L l.3-4 "109" and "186", and possibly 136 = 130 and 100 = 106), and a second transcription pass and a regrade under a new freeze are the next step

## Checks made for this PR

By the assembling session (Claude Opus 5.5), 25 Nov 2026 [measured]:

- Decode: a decoder written afresh from `KEY_A.tsv` and the rules of `RULES_A.txt` gives `DECODE_A.txt` on 117 of 117 lines: 571 tokens = 506 letters + 62 word-code tokens + 3 tokens without a value (?3, 63, 81).
- Key: `KEY_A.tsv` equals the best key of `pass2/runs/A1n_monoP4_s1.txt` on all 99 entries, and the seed-2 run has the same key.
- Judge: `count_A.py` re-adds `judge_A.tsv` to the figures above.
- Shuffle: `shuffle_A.py`, re-run in the working folder, prints the same four lines as `shuffle_A_out.txt`.
- Reading: the letters, codes and unread tokens inside ⟦ ⟧ in `reading.md` equal the decode's, item for item (L2: 450 letters, 56 codes, 2 unread; L5: 56, 6, 1).
- Freezes: `FREEZE_TX_CODE_A.txt`, `FREEZE_KEY_A.txt` (4 files), `FREEZE_TX_CODE_B.txt`, `bookcode/FREEZE_TX_NUM.txt`, `pass1/FREEZE_TX.txt` (2 files) and `pass1/FREEZE_KEY.txt` all match their files.
- Stamps: the 48 committed files that the manifest lists match their entries (the paths of `pass1/` files are at the root of the working folder there); the manifest hashes to 2c024232...01025d01, as `STAMP_LOG.txt` says; both RFC 3161 tokens and the `.ots` file carry that digest.
- Second reader: 560 of the 571 code A tokens agree by value with `bookcode/tx/NUM_FROZEN.tsv`; the 13 places that differ are under "Transcription doubts".
- Sentence check (`docs/_check_reading.py`, a pointer, not the verdict): with the language detected per sentence, 17 of 78 sentences of `reading.md` are clean (0.218) and 1 of 66 of `DECODE_A.txt` (0.015); with Danish fixed, as `_check_writeup.py` scores it, 0 of 78 and 1 of 66. Both files read as "not a reading" by its thresholds. The scorer counts every word code as a hole and judges the clear text's 1629 spelling (haffde, dett, att, ieg) against modern lexicons; most sentences carry a code hole, so the review grade is B, raw, and a reader who is not the author should look at it.
- Repository validation: **not run to a result.** `docs/_validate.py rosenkrantz1629` needs the da-modern corpus (Danish Gutenberg texts, 1800-1920), which is not cached in any checkout here; gutenberg.org answered HTTP 503 twice on 25 Nov 2026. `validation.tsv` (571 tokens, 506 read; word codes, figures without a value and clear text as gaps) is ready for a run. A period Danish model is not in `lang/`; the solver's own (Christian IV's letters) is outside it.

## Files

Copied unchanged from the contributor's working folder (sha256, first 16 hex) [measured]. Paths under `pass2/` and `bookcode/` are as in the working folder; `pass1/X` was `./X` there, and `PRIOR_ART.md`, `FETCH_LOG.txt` and `stamps/` keep their places.

| file | what | sha256 |
|---|---|---|
| `PRIOR_ART.md` | prior-art searches, both sessions | d323bc6a4dbee2a4 |
| `FETCH_LOG.txt` | image URLs and status codes | dde3fc8dd21d1cde |
| `pass1/REPORT.md`, `pass1/WORKLOG.md` | the first session's report and survey notes per image | 7a725f77dccc1dcc, f11db616712ef6d4 |
| `pass1/TRANSCRIPTION.tsv`, `pass1/SIGNS.md`, `pass1/FREEZE_TX.txt` | sign cipher: frozen transcription, sign labels, freeze | 2423cb7808fc23bf, 6090da790d198eca, 911b2e2c53686434 |
| `pass1/SOLVE_LOG.md` | sign cipher: every run and the control | 31f9d0b1719a8c12 |
| `pass1/KEY.tsv`, `pass1/FREEZE_KEY.txt` | sign cipher: the failed candidate, frozen (not a key) | 444b7f53acaac121, 093ee1c5b9359ef6 |
| `pass1/decode_once.py`, `pass1/DECODE.txt` | sign cipher: the one decode of the failed candidate | 0e76ffdd0cc1cea0, 89b54b4f32f8a462 |
| `pass1/shuffle.py`, `pass1/shuffle_out.txt` | sign cipher: shuffle control | dc7de6d332f4a058, 5e4b08255c98406b |
| `pass1/judge/BRIEF.txt`, `pass1/judge/decode.txt` | sign cipher: judge packet, not run | 34b51570d0df48fe, fa1fb9d2bbb18f0d |
| `pass1/tools/build_lm.py`, `common.py`, `solve.py`, `synth.py` | corpus build, helpers, sign solver, planted-key control | 0e3e996b8100b3e6, 5e6da06884944a88, 06f9774cb8e6eb28, add56c46501fb1fe |
| `pass2/ATTEMPTS.tsv`, `pass2/SEARCH_LOG.tsv` | every pass-2 attempt; Daisy searches | 205c3bf5ffa39b82, d7baa41c86df34b3 |
| `pass2/FREEZE_TX_CODE_A.txt`, `pass2/tx/CODE_A_FROZEN.tsv` | code A: freeze and split; the frozen transcription | 5be84783d1db5b25, 08867ad2b7954b6b |
| `pass2/tx/FREEZE_TX_CODE_B.txt`, `pass2/tx/CODE_B_FROZEN.tsv` | code B: freeze; the frozen transcription | 450203d6f6bea1c5, f539632e84c0b5dd |
| `pass2/codeA/KEY_A.tsv`, `RULES_A.txt`, `FREEZE_KEY_A.txt` | code A: the key of record, its rules, the key freeze | 2b473d0d7cefed4f, c8716d3b54e546f3, cf6ee6ed7ba161f1 |
| `pass2/codeA/decode_A.py`, `DECODE_A.txt`, `DECODE_RUN_TIME.txt` | code A: the one decode (the decryption) and its time | 8361997beb42092f, ec9df19f5485fab5, 1205a5548210abe3 |
| `pass2/codeA/shuffle_A.py`, `shuffle_A_out.txt` | code A: shuffle control | 4e132fa832b7983a, c9594666e9b0f298 |
| `pass2/judge/BRIEF_A.txt`, `decode_A.txt`, `judge_A.tsv`, `count_A.py` | code A: the strict judge's packet, scores and adder | eedde23b428c6d33, b7572b4b974d87c6, 503a103dcf32d2b4, c81f41372f105d63 |
| `pass2/tools/numlib.py`, `mkprob2.py`, `gsolve2.c`, `build_lm27.py` | loader, problem builder, constrained annealer, language model | 3e57413b0094f97d, 339f76f98fde5dc4, bca99b44d96b5830, e3d684d64550e708 |
| `pass2/runs/A1n_monoP4_s1.txt`, `_s2.txt` | the solver runs that gave the key of record | b3ef25c0ee847c7e, 39aa90aa1d6849db |
| `pass2/tmp/A1_run1.txt` | the exploratory run P2-002 (disclosed) | f17bc1b3d57c162e |
| `bookcode/FREEZE_TX_NUM.txt`, `bookcode/tx/NUM_FROZEN.tsv` | the second reader's transcription of codes A and B, frozen | 225e5cf00518f22d, b9a8a7e44492bc2a |
| `bookcode/ATTEMPTS.tsv` | book-code tests on codes A and B | 8517e89c27ab41e1 |
| `stamps/` (6 files) | manifest of the working folder and its time-stamps | MANIFEST.sha256 2c02423258b361e0 |

The manifest lists the working folder's 641 files, including those not committed here (images, crops, corpora, the model binary, `cribs/`, other solver runs and tools). `stamps/MANIFEST.sha256.ots.prev_failed_run`, from a failed attempt on an earlier manifest, is not committed.

Made here (25 Nov 2026): `transcription_L2.txt` and `transcription_L5.txt` (the rows of `CODE_A_FROZEN.tsv` for each letter, unchanged, with the three label columns joined), `reading.md`, `translation.md`, `validation.tsv` (input for `docs/_validate.py`), `profile.json`, this file. No images.

## Limits

- Model sessions did all the work: transcriptions, key recovery, decode, judging, image checks, reading and translation. No person read the figures or the text without AI.
- One transcription of record, one reader, one pass; a second model transcription agrees on 560 of 571 tokens. The held-out letters test the key, not the transcriber.
- The held-out block is 136 letters, was seen as images, and was seen decoded once by the exploratory run before the key was frozen.
- The judge was a model session scoring sense by its own lights; the judge called its own sample small and easy.
- The clear Danish, the reading, the translation and the historical setting are unchecked.

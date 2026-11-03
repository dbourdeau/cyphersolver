# Independent check of catalogue 1245 (Barlow to Grenville, 12 Feb 1807), 3 Nov 2026

The checker did not take part in the solve. Scratch files are in `verify/`.

> Published copy, 3 Nov 2026: unchanged except that one line naming AI vendors and models (section 7) and one
> line of the hygiene list (section E) were removed. `verify/` (crops and scratch files) and `drafts/` are not
> included. The letter files were renamed after the check: `*_grenville1807.*` is now `*_12feb1807.*` and
> `*_tierney1807.*` is now `*_15jun1807.*`. The changes made after the second check are listed in NOTES.md.

## Verdict

The decipherment is real. The key, the nulls and the two code groups hold up. The status **"read" does not hold**. It
should be **"read in part"**:

- 95.4% is reached only by counting 120 words with letters changed from context as read.
- Dan's rule 2 makes a context-only value doubtful.
- Without those changes the letter reads 1207/1391 = 86.8%. Even with the three known key errors corrected
  (80=c, 99=b, 58=m), it reads about 1255/1391 = 90.2%.
- Of the 666 cipher words, 482 read with no changed letter (72.4%).

## 1. Blind transcription sample

The checker transcribed three pages from 2x crops before opening any solver file:

- image 16 (letter page 2);
- image 8 (middle);
- image 19 (last cipher page).

Both versions have the same number of signs per page: 202, 249 and 246.

**Raw disagreement:** 15 of 697 signs (2.2%).

**Result after settling on 3-4x crops** (`verify/z_*.jpg`):

- **The solver is wrong at 3 signs (0.4%), all on held-out image 19:**
  - line 6, `54,39,75,79,70` should be `64` (assigning);
  - line 9, `47,69,98,60,77` has the third sign as `95` (pass B also read 95). This is "ought";
  - line 9, `44,11,96,21` should be `36` (pass B read 26). This is "to".

  Each of these errors produced a "changed letter" repair in `reading/r19.txt`: `o{o>u}{i>g}ht`, `t{h>o}{d>}{d>}`,
  `as[s]ig{r>n}ing`.
- **Unsettled; ink ambiguous; the solver's choice fits the sense:**
  - image 19: `402,30` (30 or 80), `70`/`73` at the start of line 3, `69`/`89`, `98`/`96` in "maintain", `86`/`36`
    on line 13;
  - image 8: `89`/`39` in "produce";
  - image 16: `35?`/`85`. The solver already marks this one.
- **The checker was wrong at 5 signs, and the solver right:**
  - image 16: 70, 99, 96, 4 and 101.

## 2. Nulls (10, 11, 12, 20, 21, 22)

They are **supported as nulls**:

- **Position.** On pages 1-19 they stand at word edges 163 times and inside words 200 times, with no fixed position.
- **Sample check.** In the three sample pages, every place that can be checked reads correct English when they are
  dropped: `44,10,51,22,40` the; `22,66,22,73,39,44,20,40,33,10` system; `44,20,60,75,39,10` this; `36,11,53,22,85`
  our; `65,11,60,54,90,11,64,40` change; `36,11,90,11` on.
- **The e/i alternative fails.** Reading these signs as omitted vowels fails at every one of those places: thehe,
  sisystem, tehis.

Minor point: in read words the reading drops 269 occurrences but keeps 16 as their key letter and changes 4. Pick one
rule and state it.

## 3. Rebuild

- `apply_patches.py` and `build_docs.py`, run in a scratch copy, reproduce `decryption_`, `transcription_` and
  `reading_grenville1807.md` byte for byte.
- `check_marks.py 01..19` exits 0, with no unmarked departures.
- Its total is 1315/1379. NOTES gives 1327/1391 because it adds the 12 clear subscription words of image 20. NOTES
  should say so.
- Running `apply_patches.py` in place rewrote `trans_final/*` with identical content, so only the file times changed.

## 4. Held-out test

The rerun gives the same figures: 85.4% of letters kept and 45.2% of cipher words clean. Two limits:

- The figures are self-graded. They are computed only over words the solver chose to read, by a reader who knew the
  key while settling the transcription.
- The 3 transcription errors above sit on these held-out pages.

Lead with 45.2% clean, not 85.4%.

## 5. Code groups

- **4990 = India.** It fits all 7 places: "establishment in", "natives of" (x2, plus one with a doubtful "of"),
  "British empire in" (x2), "establishment in ... may be rendered".
- **5650 = British.** It fits all 4 places: "the _ dominions", "authority of _ government", "_ empire" (x2).

Both values come from context but hold at every occurrence, so they are acceptable as given.

## 6. Count, and recount on the sample

On image 19 the solver counts 35 of 37 cipher words as read, using 58 repairs. Strictly, without changed letters,
22 of 37 read. With the 3 transcription fixes above, about 25 of 37 read.

Across the letter:

- 725 of the 1391 words are clear words, counted as read automatically;
- cipher words alone read at 90.4% even with every repair accepted.

## 7. AI vendor and model names

- **`scripts/transcribe_api.py`:**
  - line 21 names two AI vendors and two models [names removed for publication];
  - line 4 has a local user path.

  Do not ship this file as it is.
- **Everything else is clean.** No other file in the folder names a vendor or model. NOTES says "two different vision
  models", which is fine.

## Must fix before Dan

1. Change the status to "read in part". Give 86.8% (no changed letters) as the headline and 95.4% only as "with
   marked context repairs".
2. Correct image 19: `79` to `64`, `98` to `95`, `96` to `36`. Re-examine the 7 ambiguous signs listed above. Rerun
   `check_marks.py` and the counts.
3. Remove the vendor and model names and the local path from `transcribe_api.py`, or leave the file out of the PR.
4. In NOTES, state that the 12 subscription words are in the 1391, that the held-out figures are self-graded, and the
   single rule for nulls.


---

# Second check, 3 Nov 2026: were the fixes applied, and does the reading read as sentences?

A second independent checker made this pass. As instructed, it did not repeat the blind sign check. The scratch copy
it worked in was not kept.

## A. Were the must-fixes applied?

| Must-fix | State |
|---|---|
| 1. Status "read in part"; headline without changed letters | **Done.** NOTES gives 1195/1379 = 86.7% as the headline and 95.0% only "with changed letters". The recount below confirms the figure. |
| 2. Image 19 corrections | **Done in the transcription.** `trans_final/p19.txt` line 6 is `54,39,75,64,70,98,83` and line 9 is `47,69,95,60,77. 44,11,36,21.`. These match the first checker's blind file exactly. The NOTES wording is wrong, though. It says "The checker read the first of the three as 64; the crop shows 70". The blind file (`verify/blind_img19.txt` line 7) has `64,70`, so the checker also read 70. The error was only in the summary of the first check ("`54,39,75,79,70` should be `64`"). Fix the NOTES sentence. The six other ambiguous signs are now marked doubtful, as NOTES says. |
| 3. Vendor names and local path in `transcribe_api.py` | **Not done.** The file was moved to `drafts/transcribe_api.py` without being cleaned. Line 4 still has a local user path. Line 21 still names two vendors and two models. `drafts/run_pass.sh` line 1 also has a local user path. NOTES still lists `drafts/` among the files. |
| 4. NOTES: the 12 subscription words, self-graded held-out figures, one rule for nulls | **Done.** |

## B. Rebuild (scratch copy)

- `apply_patches.py`, `check_marks.py 01..19` and `build_docs.py` reproduce byte for byte:
  - all six `transcription_`, `decryption_` and `reading_` files;
  - all 26 `trans_final/` pages.
- `check_marks.py` exits 0. Its total is 1310/1379 = 95.0%, cipher words 597/666, 444 repairs (315 dropped, 129 changed),
  28 code groups.
- I introduced three unmarked departures into `reading/r19.txt`. `check_marks.py` caught each one and exited 1:
  - `f{h>}or` to `for`;
  - `{n>c}lergymen` to `clergymen`;
  - `l[i]v[e]{t>}s` to `l[i]v[e]s`.
- No script prints the 1195 headline. It is derived by hand from the counts.

## C. Recount

I classified the tokens in `reading/r*.txt` myself:

- 691 tokens: 25 code-group tokens and 666 cipher words.
- Of the 666 cipher words, the classes match NOTES:
  - 315 read with no repair;
  - 167 read with signs dropped only;
  - 115 read with a changed letter;
  - 69 doubtful.
- Headline: 713 clear + 315 + 167 = 1195/1379 = 86.7%.
- Held out (images 14-19): 221 cipher words, 100 clean (45.2%), 53 dropped-only, 47 changed, 21 doubtful.
  `heldout_stats.py` reproduces this.
- Cipher words alone, with no changed letter: 482/666 = 72.4%. With no repair at all: 315/666 = 47.3%.
- 713 of the 1379 words (52%) are clear and count as read automatically.

Code groups are left out of the 1379. This covers the four unread single groups (4087, 5089, 4845, 4600) and also
India and British. The net effect is small. NOTES should say it in one line.

**The held-out test is graded against the solver's own reading.** No independent text or gloss exists.

## D. Read as sentences

Every image section of `reading_grenville1807.md` was read as running English. There is no translation, because the
letter is English. Grades:

- **A:** coherent, few holes.
- **B:** mostly sense, weak places named.
- **C:** not acceptable as a reading of that passage.

| Image | Grade | Weak places |
|---|---|---|
| 15 | A | Codes 4087 and 5089 are open. Clear "stating that is in the contemplation" is probably "that it is". |
| 16 | A | `[?delicacy]` is sound in sense. "of which ye ye professed obiect": the doubled "ye" (`ye{t>}{?>}`, `ye{t>}_pr...`) is suspicious, and the first token may be another word. |
| 17 | A | `[?andts]` and `[?and]` x2 are small holes. `m{h>o}[s]t` "most" and `{s>}t{o>}o` "to" are heavily repaired. |
| 18 | B | A four-word hole: "but also the [?mfap] [?iit] [?oott] [?accomplishing] that important obiect". "stated stated": the cipher word duplicates the clear word, so check whether the cipher word is something else. Clear "come circumstances" should be "some". `b{v>l}[e]{p>s}s[i]ngs` and `t{?>}e{?>n}[e]ts` have two changes each. |
| 1 | B | "in [?wotcth] these have generally been supposed"; "the record of [?this] derived". |
| 2 | A | Doubtful `[?are]`, `[?some]` and `[?natives]` are all well supported by sense. |
| 3 | **C** | The passage does not parse: "[?ato310] to contemplate without [?emotion] the operatyon of [?that] [?restricted] to the obiect of [?diffusing]"; "the result of long experience however this adverse to these conclusions" lacks a verb. The holes are honestly marked, but this paragraph is not read. |
| 4 | A | none |
| 5 | B | "a sentiment of religious jealousy it if once connected with [?100] ye measures of government [?its] animated": the clause is not grammatical as read. |
| 6 | B | "our empire India" lacks "in". "[?not] [?130mgr] can be so extreme" is a hole at the clause head. |
| 7 | B | **A word counted as read is wrong.** `c[o]nv[e]ntion{h>}` "convention" is `65,70,53,80,44,75,36,83,11`. With 80 = c, the key error NOTES itself admits, it is "conviction" (`{n>c}`). The next doubtful word, `[?nnuitind]` (`80,83,84,32,77,98,70,21`), then reads `c[o]nui[c]ti[o]n{d>}`. The sentence becomes "would not be precluded even by a conviction (if indeed such a conviction could be established) that persuasion alone would be employed". This is correct sense, and "convention" is not. "[?print] of their conversion" is probably "projects". "would i [?uioomahtedto]" is a hole at the page end. |
| 8 | B | Four-word hole on the actors: "the auowed [?dotr] [?snrt] [?sntmies] of the [?shtratrpsdimployd] to excite it" (sense: avowed and secret enemies of the government employed). Also "occurrences [?ofhuntsd]". |
| 9 | A | Small holes: `[?of]`, `[?religious]`, `[?ss]`. |
| 10 | B | "the purposes **or** [?tumult] and sedition": "or" (`o{d>}r{d>}`) is counted as read without a change, but sense needs "of". It should be marked changed or doubtful. `i{o>}{h>}{m>}n{o>}` "in" drops sign 2 (= m), which is not one of the claimed nulls. `{w>m}ight b[e]_{v>a}dduc[e]d` and `coa{u>s}t` are heavy repairs. |
| 11 | B | "[?withsh] [?atr] success" (with what success), "the discontented [?adntdhdsfntd]", "[?odt] [India]", "recent [?surenhtsh]". `chara{n>c}t{t>}{d>}er{s>}` drops the s to make "character". |
| 12 | A | "religiou s topics"; college of [code 4845]. |
| 13 | A | "spirit d bigotry" (clear "d" = "of"); "in the [?nlng] of [?all] subiect of [?a] religious nature". |
| 14 | B | "than [?st] **it** solicitude for ye preservation": `{h>}it{h>}` is counted as read "it", but sense needs "with". Also "[British] empire [?ihonnh] [India]", "community [?oihn] this country", "clerical offices [?vtt] the several". |
| 19 | A | "[?yiets]" (purity?); `[?ought]`, `[?maintains]` and `[?society]` are marked for ambiguous signs, but the sense is sure. |
| 20 | A | Clear subscription. |

**`reading_grenville1807.md` overall: B.** The argument of the whole letter is recoverable from start to end. Barlow
argues against the proposed ecclesiastical establishment on the Buchanan plan, citing the danger of religious alarm
after the troubles "on the coast", and proposes respectable clergymen with adequate allowances in its place. Image 3 is
not read. Holes of four or more words remain on images 8 and 18. At least one word counted as read is wrong
("convention"), and two more are doubtful against sense ("or" on image 10, "it" on image 14).

The sign 80 problem is not confined to the marked `{n>c}` repairs. Any word where 80 was read as n without a mark could
hide another such error, which bears on the 315 "clean" count. 80 occurs 33 times.

**`reading_tierney1807.md`: A.** It is clear text, coherent throughout, and correctly called "transcribed; no
cipher".

## E. Grep (vendor and model names, local paths)

- `drafts/transcribe_api.py`: line 4 has a local path. Line 21 names two vendors and two models.
- `drafts/run_pass.sh`: line 1 has a local path.
- `scripts/__pycache__/` exists. Leave it out.
- NOTES says "An independent AI checker". Use "an independent AI language-model agent".
- Images are ignored by the parent `.gitignore` (`*.jpg`).

## F. Prior art (one search)

One web search turned up three things, but no edition or decipherment of these letters:

- the SNAC/DPLA catalogue record of the 26 pages;
- Buchanan's 1805 Memoir;
- the Minto-era printed papers on the Vellore aftermath.

The Grenville and Dropmore papers and the India Office records remain unsearched. A clear copy in London is possible.

## Must fix before Dan (second check)

1. Remove `drafts/` from what ships, or scrub `drafts/transcribe_api.py` (vendor and model names, local path) and
   `drafts/run_pass.sh` (local path). Drop the `drafts/` line from NOTES "Files". Also leave out `scripts/__pycache__/`.
2. Name the target consistently. The planned target is `barlow1807`, but the files are `*_grenville1807.*` and
   `*_tierney1807.*`. Follow the ferdinand1552 and ercole1544 convention.
3. Image 7: read "convention" as "conviction" (80 = c, marked `{n>c}`), and give `[?nnuitind]` its reading
   "conuiction". Check every other unmarked 80 that was read as n. Rerun `check_marks.py` and the counts. The headline
   moves by about 1.
4. Image 10 "or", which should be "of", and image 14 "it", which should be "with": mark them changed or doubtful, not
   clean.
5. Correct the NOTES sentence about the checker and 64/70.
6. Change "independent AI checker" to "AI language-model agent".

Verdict of the second check: **fix**. The status "read in part" at 86.7% (1195/1379, no letter changed) is honest and
is reproduced. Expect about 86.5-86.6% after fixes 3 and 4.
7. `VERIFY.md` itself (line 99, first check) names the vendors and models. Do not ship `VERIFY.md` as it is; scrub that line or keep the file out of the PR.

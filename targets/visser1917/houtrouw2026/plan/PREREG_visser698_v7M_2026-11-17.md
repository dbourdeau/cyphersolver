# PLAN (sealed) · catalogue 698, the Kolbeck and de Visser symbol message · v7-M

*Provenance. The model's words throughout (M), except J.'s rulings, quoted in §2 from the chain entries named there, and the desk's words where they stand in quotation marks under its name. V as measured by `prov/words2.py` is given at the end of §14a, for draft v6; draft v7 adds the desk's words in §16, quoted under its name, and none of J.'s. Models on record, from the logs, draft by draft: `claude-fable-5-2` for the second cipher chat (session `78298d5e`), which wrote drafts v1 and v2 and readings v1 and v2; `claude-fable-5-2` for the third (session `eea13873`) until 03:54:37Z on 17 Nov, which built the solver and the rehearsal, made reading v3 and wrote drafts v3, v4 and v5; `claude-opus-5-5` for the third since 03:55:25Z on 17 Nov, set by J. at 03:54:26Z, which wrote draft v6 and this draft and the question's third form. The desk, by its own account: `claude-fable-5-2` until 14:33:12Z on 16 Nov, for its verdicts on drafts v3 and v4; `claude-opus-5-5` since 04:25:16Z on 17 Nov, for its verdict on draft v5 and the cover file. The desk saw draft v5; its verdict of 05:16Z on 17 Nov: FIX BEFORE SEAL, two findings; every fix of 14:23Z is in; yes to the tiles, with its finding 1. **The desk saw draft v6; its verdict of 18:00Z on 17 Nov (ask 21; chain entry 245): FIX BEFORE SEAL, one sentence. Draft v7 (18:25Z on 17 Nov, SHA-256 `7b705f9976a072755e684c0ce3b66f8588f13340e5565f984813ec998656f989`) made it, in the desk's words. J. ruled by box at 18:34:50Z on 17 Nov to seal on the desk's own wording without a further round, and to run stage A (entry 256). This sealed text is draft v7 with four things changed: the title line, this sentence, §15 and the chain's head.** J.'s own acts: the rulings of §2; two of the three Spanish texts, saved by his hand; the release of frame 58 and of the desk's suggestion on the Bureau's text; his word that the match of the strip is made with its letters covered, that one letter of a word may be wrong, and that the desk cuts the tiles.*

**Nothing has been run on the message: no solver, no letter value tried, frame 42 not opened by this chat (the desk has it open, §4). The stage A script refuses reading v3 unless it is given a plan that is not a draft and that holds the hashes of §13; that refusal was tested three ways. This draft replaces draft v6 (05:47Z on 17 Nov, SHA-256 `9b4d4aa380bced09f0e62ba4ddbcb877f1ba8fdce22ed342d260529318c3cc40`), which stays as it is, as v6 replaced v5. §14 lists every change from v6, and from v5 to v6, with the desk's finding or J.'s ruling behind each. What is still open before the seal is in §15, and the weaknesses known now are in §16.**

## 1. The target and what is held
- **The message:** one sheet in NARA M1085 roll 302, Bureau of Investigation case OG 2889, photographed twice. Frame 39: JPEG, 992 by 1328, SHA-256 `7bfe35dad9e765ede229ac749fadda50a0aa99c5da6d356fdca9c791ed31efcc`. Frame 58: JPEG, 1048 by 1344, SHA-256 `9bf08619ac976a2ff9ba827b6877be400e85c99c5eac8ba4dc4e30091ef348c7`, released by J.'s ruling of 01:11:22Z on 16 Nov (§2). Seven lines of pen-drawn signs with dashes between groups, and a line set apart like a signature.
- **The input:** blind reading v3, made from both frames (`visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md`, SHA-256 `ddb270fbe48f6973be35256819d0452df81c6953e11d44e15e35810592e2cded`, stamped by three authorities at 02:38:45Z on 16 Nov; chain entry 135). By the parser: 120 signs, of which 77 are sure, 41 doubtful and 2 unread; 17 sign classes; 30 of the doubtful signs list one or two alternates; 11 dividers, 3 of them doubtful.
- **The groups:** 17, counting each dash and each line end as a break: 2, 8, 6, 6, 5, 7, 6, 10, 11, 6, 6, 6, 5, 9, 7, 7, 13 signs.
- **Reading v2** (frame 39 alone: 125 signs, 20 classes, 69 sure; SHA-256 `24d3f1ab3641c1dd0ff37fd14b670a39e8a675eb92e8bd581a2d16646b0e1ab5`) stays as it is and is no longer the input. Reading v3 is not independent of it: the same reader made both and knew v2's labels. The reading file says where that could have leaned on a choice. It is as blind as v2 was: no letter value has met the message.
- **The ledger:** the language texts and the engine are those of main `37fe838406c010e15734125dc0938b760a3d8ca1`, kept in `ledger_pin_37fe8384/`. At main `b13ebd1b3b18d015ee6eeff12f5889e7e57c9095` (committed 05:36:49Z on 17 Nov, fetched 05:42:18Z) `lang/corpora.py` and *Don Quijote* have the pin's hashes. `lang/lm.py` has gained two normalisers for Arabic since the pin: 33 lines added, none taken away (SHA-256 now `d4f2a016b7905d0c20b60fd155fd2cfdb76e9a6f01d7a112f453bf156d09ba58`). The plan keeps the pin's file, whose hash is in §13. In `catalogue.json` at that commit only rows 1424 and 1534 carry a `reserved` field; row 698 carries none. At main `e857642f` (17:54:44Z on 17 Nov), by the desk's own clone, all of that still holds, and `targets/visser1917` has had no commit since `fe4c0370` (the desk's verdict of 18:00Z; it did not re-check *Don Quijote*'s hash).
- **Another contributor's folder.** By the desk's findings (19:56Z on 15 Nov and 14:23Z on 16 Nov), from pages closed to this chat, the ledger tags 698 "in progress" in the folder `targets/visser1917`, contributed by WAINUT on 27 Oct; the tag was set at the maintainer's offer so that an unfinished write-up could be merged; and the ledger gives that contributor's pull requests as coming from the GitHub account LcCompany. Read here as hash and date only: the folder has three commits, the last `fe4c0370d31f2731034496dafd2fe3ed3ad010be` of 19:01:53Z on 27 Oct, and no file under it differs between main of 14 Nov (`ce16c281`) and main now. This chat's copy of the ledger leaves the folder off its disk.

## 2. J.'s rulings
**By box, 21:54:05Z on 14 Nov (chain entry 22).**
- Key strip: "Blind first, strip as check (Recommended)".
- Language: "Spanish, then German and English (Recommended)".
- Claim: "Claim it (Recommended)". Superseded by the ruling of 01:28:03Z on 16 Nov, below.
- Meanwhile: "Second pass, then scope 1536 (Recommended)".

**By box, 22:24:49Z on 14 Nov (chain entry 26).**
- Null test: "Shuffle the message; strip decides (Recommended)".
- Runs: "One, picked by a rehearsal (Recommended)".
- Strip check: "Chance-based bar (Recommended)".
- Prior work: "Top one but you do searching". Read by the second chat as: the model searches, and learns only whether a reading exists.

**By box, 02:28:58Z on 15 Nov (chain entry 70).**
- Seals: "Desk first, both (Recommended)".
- The strip rule, in the light of rehearsal part 3: "Keep as drafted (Recommended)".

**In the desk's chat, 01:11:22Z on 16 Nov, as the desk's addendum quotes it (chain entry 119).** `"Yes" on D1. Yes on both.` By the addendum this releases two things to this chat and nothing else: frame 58, and the desk's suggestion that the Bureau's 1917 text be given a sealed role. The two questions J. answered are not shown to this chat.

**By box, 01:28:03Z on 16 Nov (chain entry 122).**
- The claim: "Ask first (Recommended)".
- Stage B: "Bar on the blind reading (Recommended)".

**By box, 03:45:21Z on 16 Nov (chain entry 143).**
- The Bureau's text: "Sealed claim only (Recommended)".
- Its word file: "The desk, now, by hash (Recommended)".
- Whether "Ask first" covers the seal and the run: "Yes, wait for the answer (Recommended)".

**By box, 14:39:56Z on 16 Nov (chain entry 159), on the desk's verdict of 14:23Z.**
- The match of the strip's signs to the reading's classes: "Letters covered first (Recommended)".
- The word count of §10b: "One letter may be wrong (Recommended)".
- The question for issue #542: "With the at-sign (Recommended)".

**By box, 05:39:51Z on 17 Nov (chain entry 180), on the desk's verdict of 05:16Z.**
- The key strip's tiles: "Desk cuts the tiles (Recommended)".
- The Tools line of the question for issue #542: "Both models (Recommended)".

## 3. Prior work
- **The ledger's folder** records the message as located, with a key strip, and not deciphered (title and outcome fields only), and the ledger tags the entry "in progress" for that folder (§1).
- **A yes-or-no search by title** (22:25:42Z on 14 Nov, five queries, 54 titles, no page opened): no title claims a reading. The one title that names the message is the ledger's pull request #108, "located … not deciphered". Record: `visser698/PRIOR_WORK_visser698_search_2026-11-14_2241Z.md`.
- **The desk's answer to the question whether a reading exists** (ask 3; its note of 19:56Z on 15 Nov; chain entry 118): **"No."** In the desk's words: "No reading of the message and no text of the Bureau's 1917 reading is printed in what the desk opened. The word answers the question as asked; it does not say the sources are empty."
  - *Opened by the desk:* the ledger's folder and catalogue row; pull request #108 and its comments; a search of issues and pull requests; both Project Gutenberg books, by windows of the fetch tool's reader and not by an exact search; the Pennsylvania paper of 4 Oct 1917.
  - *Not opened by the desk,* each behind a bot check: the *San Antonio Light* of 15 Sept 1917; the *Texhoma Times* of 28 Sept 1917; and a third page a web search turned up, the *San Antonio Light* of 14 Dec 1917, p. 2.
- **Not searched by anyone:** DECODE; Reddit (J.'s).
- **The question to the ledger.** By J.'s rulings the question about the other contributor's folder goes on issue #542 before any claim, seal or run (`visser698/DRAFT_question_542_visser698_2026-11-17_0542Z.md`). The desk saw the first and the second forms and each time asked for lines to be changed (asks 17 and 19). The third made the changes of 05:16Z, with the Tools line by J.'s ruling of 05:39:51Z. It went up at 13:41:00Z on 17 Nov, posted by this chat from J.'s Chrome at his word, with the record line of entry 224 and no other change (comment 6949722637; entries 225 and 226). **The answer has come.** By the desk's relay of J.'s copy of the thread (entry 245), LcCompany answered at about 13:46Z and 13:47Z that we are free to pick 698 up and work on it. They did not say whether their own work goes on, and nothing else of the thread is known here.
- **Owed before anything is called new:** the sources of §5, opened at the time §5 gives.

## 4. Known before the seal (exploratory, not evidence)
**Read before the first reading, on 14 Nov** (`visser698/QUARANTINE_visser698_2026-11-14_2123Z.md`, SHA-256 `c79c8fd2073a6304d7e7d97fd8921a5510ad2b8b73c57233a70f29a5ba07c309`, written before any reading; its addendum, SHA-256 `5cb52b5d95b79949c68d24847a48cf800a4f1af7e091bb8d767a5c9d44047e74`). The catalogue row was printed whole to the second chat at 21:20:25Z on 14 Nov; its log copy `SESSION_78298d5e_2026-11-14_222834Z_pre_compaction.jsonl` shows every field:
- **Title and correspondents:** a code message carried by Henry Kolbeck and Olga de Visser from Mexico City to San Antonio, seized with its key at Laredo; the claimed correspondents are Hugo Horotwischka, secretary of the Austro-Hungarian legation in Mexico City, and Joe Bolner of San Antonio, "self-styled representative of the Central Powers".
- **Shelfmark and folio note:** NARA RG 165, MID file 9140-103, with its index card on M1194 roll 243, frame 1821, and a pointer to file 4131-44, "Olga de Visser message and Kolbeck key"; "One message plus key."
- **The status line, whole:** seen 2 Nov 2026 on M1085 roll 302, frames 39 and 42; a seven-line symbol message in a Spanish-alphabet substitution with a key strip, both photostats of poor resolution; the Bureau read it in 1917, in Spanish, but no plaintext is located; **"Kolbeck later claimed he wrote it himself."** Draft v4 called its account of this line whole and left that last clause out; the desk found it.
- **Why, verify, score note, prior art:** "Central Powers courier traffic between Mexico City and Texas in February 1917"; a note to order the two MID files and check whether the ciphertext copy survives; that the row was scored from index cards and case-file text and not viewed; "open as far as checked (27 Oct 2026 …)".
- **Links:** the labels and addresses of the index card and of frames 39 (message) and 42 (key strip). No link was followed but frame 39's.
- **The first 420 characters of the row's vetting block:** the two frame addresses; "Seven lines of handwritten signs (about 170-200 signs) plus a signature line; a torn key strip of two rows"; and the words "Viewed: seven lines of pen-drawn symb".
- **From the folder's `profile.json`:** the title and the outcome fields, which are the class "not read", the method "not solved", the credits and the names of the five gaps, one of them "left half of the key strip".
- File names only, of every ledger file that names Kolbeck, de Visser, Bolner or the file numbers; and the result titles of two web searches on 14 Nov (one at "21:2xZ", as the quarantine file has it, one at 22:25:42Z), nothing from the pages.
- **So this chat knows that the strip is torn, has two rows, and that its left half is named as a gap; and that Kolbeck is said to have claimed the message as his own writing.** The first bears on the forecasts of §11. The second bears on whose language the message is in; this chat knows nothing of Kolbeck's, and the three languages of §6 stand as J. ruled them on 14 Nov. Neither bears on the reading.

**Since then:**
- The class counts of readings v2 and v3. In v3 the commonest classes are `E` (15), `R` (15), `3` (14), `Q` (13) and `P` (11).
- One language assumption went into reading v2: `3` and `K` were kept apart partly because together they would be more common than any Spanish letter. The reader of v3 knew that remark. v3 sorts the three-like signs by their strokes on both frames (`3` 14, `Z` 7, `K` 5).
- **Frame 58,** from the desk's addendum of 01:13Z on 16 Nov (SHA-256 `c712711e805a6c2dd345bb653599e85735696730cbeaac7015ef458dacea3ed9`), which says of it: the same sheet as frame 39, signs only, no letter in clear, a separate exposure.
- **From the desk's note** (SHA-256 `452ff04362a874d9a92194e813fdea9eb62303e7329a7753ebe50303925e6d86`) **and its addendum:** the "in progress" status line of §1; the answer of §3 with what was not opened; that the desk keeps a file for J. alone on what the closed sources hold (SHA-256 `74499de9fdf47c725cd1eade9a6ab71f72b8b39a51bb49bbd8a3fd164c802e23`), which this chat has not seen; and the wording of its suggestion on the Bureau's text: a word "of eight letters or more", "the spelling the source gives", a word given "in more than one form".
- **That suggestion was written with the closed sources open.** The desk says it could not show it would have raised the point blind. So the shape of the word rule of §10b may reflect what a source prints. The solver and the reader took nothing from it.
- **From the desk's verdict of 14:23Z on 16 Nov** (SHA-256 `d3dcd8df257ade23d70fe4bbc2cdfc10e6f5a93ac7dbe1010a25ed9256f655c6`; chain entry 157): the two status facts of §1 on the other folder; that the words file exists, with its hash; and nothing of what it holds, nor whether it holds a word.
- **From the desk's verdict of 05:16Z on 17 Nov** (SHA-256 `d2d555e6dd16b260a5104d2ab82eda5423cb648296575ca540fc7d0c1aad3da1`; chain entry 179): that the desk fetched frame 42 at 04:36Z on 17 Nov, with its address, hash and size; that the cover file exists, with its hash; that it holds 193 cover rectangles and 27 sign rectangles of one size, one for each mark the desk judged may be a sign; that tiles cut from the covered frame could be put back in order from the cover file; and the ledger's status facts. Nothing of any letter.
- **The cover file's whole text.** When J. attached it at 05:33:22Z on 17 Nov, the app read it into this chat's context: the frame's address, hash and size, the 193 cover rectangles and the 27 sign rectangles in the strip's order. It holds no letter. No command of this chat has read it but to copy it, hash it and verify its receipts, and nothing has been reckoned from its rectangles. J. was told before he ruled that the desk cuts the tiles (§8 step 2), so that these rectangles cannot place them.
- **The desk's count of 27 marks that may be signs** bears on the forecasts of §11, and they are changed for it.
- **The rehearsal and the trials of §9.** On made-up Spanish messages the best-scoring key is usually not the true key once a third of the doubtful labels are wrong. So I expect stage A to miss.
- **Files J. supplied.** Two PDFs, the maintainer's mail on ledger issues #542 and #602, screened for the quarantined names before they were opened (chain entry 42). The mobile session's ledger on the Mauborgne break (entry 114): the names and numbers of the quarantine lists were counted in it by script at 03:55Z on 16 Nov, and none occurs.
- Commit subjects of the ledger were read for the refresh of §1, with any subject naming the message's people or number filtered out unseen; none was.
- No letter value has been tried, no solver run on the message, and frame 42 has not been opened.

## 5. Quarantine, and what opens when
| Stays closed until | What |
|---|---|
| Each stage A results file is hashed and stamped, unread | The desk's tiles of frame 42: each sign centred on a plain ground, numbered in an order of the desk's drawing (§8, step 2). Their hashes are checked against the chain. This chat sees nothing else of frame 42 |
| The match of the tiles to the reading's classes is hashed and stamped | Frame 42 itself, fetched by this chat; the desk's order file, which says where on the strip each tile stood; the desk's tile script |
| The strip's letters and `STRIP_v1.json` are hashed and stamped | The stage A results files themselves |
| The strip check's output is stamped; and, if stage A missed, stage B's output and the fills are stamped too | The desk's file of the Bureau's words, known here until then only by its SHA-256 (§10b) |
| The word rule's output is stamped | Every other frame of case OG 2889; NARA's page text; the ledger's notes on the message and its page `docs/solve/698.html`; MID files 9140-103 and 4131-44; the six sources of the quarantine addendum; the *San Antonio Light* of 14 Dec 1917, p. 2; any web page naming the message; comments on issue #542 after 15:01Z on 14 Nov; the desk's chat and its file for J. |

Frame 58 came off this list by J.'s ruling of 01:11:22Z on 16 Nov. Nothing else has.

## 6. Hypotheses
- **H1.** The message is a one-to-one substitution of signs for letters and the plaintext is Spanish. Dashes and line ends are breaks between groups. A group may hold more than one word.
- **H2, H3.** The same, with German or with English plaintext. Sealed alternates, by J.'s ruling, at a stricter bar.
- **Not covered:** a sign that stands for two letters (ch, ll, rr), nulls, a code word, or two letters that share one sign class in the reading. If the strip shows any of these, stage A's model was the wrong one and that prints.

## 7. Language models (unchanged from draft v3)
- **Engine:** the ledger's `lang/lm.py`, unchanged: its "modern" normaliser (lower case, accents stripped, a to z, so ñ counts as n) and its dense letter model with interpolated discounting, no spaces. Built by `visser698/solve/build_lm_v1.py`.
- **Scoring from a fresh start.** The same text is built at orders 1, 2, 3 and 4, and a string is scored as log P(c1) + log P(c2|c1) + log P(c3|c1c2) + the four-letter terms.
- **Spanish, three texts, 4,031,951 letters after the header strip.** *Don Quijote* (Project Gutenberg no. 2000, in the ledger), 1,651,320 letters; *Fortunata y Jacinta* (1887, no. 17013, saved by J.), 1,738,110; *Los cuatro jinetes del apocalipsis* (1916, no. 24536, saved by J.), 642,521.
- **German:** the eight files of `targets/adfgvx/corpus/` in the ledger, 2,654,576 letters.
- **English:** this project's `bapco1534/lang/quad26.f32`, a table of joint four-letter probabilities from twelve prose books, sealed once already in the BAPCO plan. The same four conditional tables are derived from its marginals. Each language is judged only against its own null.
- **Tables:** one file a language, `round(1000 · ln P)` as integers. Hashes in §13.

## 8. Stage A: blind
- **Solver** (`sa_core_v1.c`, `lib698_v1.py`), unchanged. Annealing over one-to-one maps from the sign classes (17 in reading v3) to the 26 letters, then a climb to a local best; the best of the restarts. It works in integers with its own generator, so the same seed gives the same answer on any machine. A Python copy of it gave the same key, score and restart scores on nine test problems, and 18 solves of the first rehearsal came out the same on J.'s PC (chain entry 63).
- **The design, picked by the rehearsal on both shapes (§9): D3.** Every read sign is scored; each doubtful sign may take its first label or any alternate the reading lists, whichever the solver prefers. On reading v3 that is 118 places in 18 runs, 30 of them with a choice of two or three classes. An unread sign ends a run and scores nothing.
- **Budget:** 16 restarts of 800,000 proposals; one proposal in four changes the class of one doubtful sign, the others swap two letters of the key; the temperature falls in a straight line from 4.0 to 0.5 nats.
- **Seeds:** master seed 6980001. Null copy c (1 to 1,000) is shuffled with `subseed(master, 10, c)`: the same 1,000 copies for all three languages. The solver's seed is `subseed(master, 20 + language, c)`, with Spanish 0, German 1, English 2, and c = 0 for the message. Parameters: `visser698/solve/stageA_params_v1.json`, unchanged.
- **One run per language** (`stageA_v3.py`, one invocation each, in the order Spanish, German, English), each writing its own results file. `stageA_v3.py` is `stageA_v2.py` with one change: its guard knows reading v3 and parses it with v3's 17 class labels. If a run is cut off it is started again under a new output name; the solver is deterministic, and the part file of the first start is kept.
- **Null.** The same solver and design on 1,000 copies of the reading with the signs shuffled over the whole message, group lengths kept. Each sign carries its doubt mark and its alternates with it. p = (b + 1)/1,001, b being the copies that score at least as well as the message.
- **Bars.** H1: p ≤ 0.01. H2 and H3: p = 1/1,001 each. The chance that some language passes on score alone, if the message is not language, is about 0.012.
- **The strip decides.**
  1. The script prints nothing of the solution: no score, no p, no letter. Each results file is hashed and stamped unread.
  2. **The tiles** (J.'s ruling of 05:39:51Z on 17 Nov, on the desk's finding 1 of 05:16Z). The desk, which has frame 42 open, cuts one tile for each of the 27 marks the cover file's "signs" names. Each sign is centred on a plain ground, every tile is of one size, no two tiles share a pixel, and neither the cover's black nor a sign's place in its rectangle is left in a tile. It numbers them `tile_01.png` and on, in an order of its own drawing, and keeps, with J., a file in the shape `{"tile_to_place": {"<tile number>": <place in the cover file's "signs", 1 = the first>, ...}}`. Before the seal it gives this chat the SHA-256 of every tile and of every tile's pixels, of that order file and of its tile script; they are entered in the chain. The pixel hash is there because an image's file hash can change on its way between the chats while its pixels do not (it is the SHA-256 that `prov/chain.py`'s `pixel_hash` computes). The tiles come to this chat after the stage A results are stamped (§5), and their hashes are checked against the chain. The cover file's rectangles are in this chat's context already (§4): they give where each sign's rectangle lies on the frame, not which tile is which. `cover_frame42_v1.py` is not used.
  3. **The match, from shapes alone.** For each tile: its shape, and which class of reading v3 it is, with a doubt mark where the match is not sure, or no class. `STRIPMATCH_v1.json`, in the shape `{"way": "tiles", "signs": [{"id": <tile number>, "class": "<label>" or null, "sure": true or false, "note": "..."}]}`, and a note on the shapes are hashed and stamped. If a letter in clear shows on a tile, the match stops, the tile is reported to the desk, and the weakness of the desk's finding 2 of 14:23Z prints.
  4. **The frame, the check of the tiles, and the letters.** Only then does J. bring the desk's order file and tile script, each checked against its hash in the chain, and this chat fetches frame 42 and checks it against the hash the cover file gives. The tile script, run here on that frame and the cover file, must give every tile again at the place the order file names for it. If it does not, that prints, and the desk is asked why before any letter is read. Then the letter or letters at each place of the strip are read from the frame and written to `STRIPLETTERS_v1.json`, its places numbered as the cover file numbers its "signs" (the desk's note of 05:16Z), hashed and stamped.
  5. **The strip file, by script.** `make_strip_v2.py` puts the two stamped files and the order file side by side and judges nothing. `STRIP_v1.json` holds the pairs whose match is sure and whose letter is sure. A class that two strip signs are matched to with different letters is left out and named. A letter that two or more classes are given is named and kept, reported only (the desk's note). Stamped. Only then are the results files opened.
  6. Let n be the sign classes of reading v3 that the strip gives with a single letter. Signs the strip gives as two letters are left out. Let k be the number of those n on which a solution agrees with the strip, after the same normalising (`strip_check_v1.py`; its text says "reading v2", its code takes whatever classes the results file names).
  7. **Pass:** n ≥ 5, k ≥ n/2, and the message's k is greater than the k of every one of the 1,000 null solutions.
  8. With n below 5, stage A cannot hit, whatever the score.
  9. A second count with the doubtful matches added (`STRIP_v1_with_doubtful.json`) is reported and decides nothing.
- **A hit needs the bar and the strip,** and nothing else makes one: by J.'s ruling of 03:45:21Z on 16 Nov the word rule of §10b is a claim rule and not a second way to a hit. If no language passes its bar, stage A has missed; k is still computed for all three and printed.

## 9. The rehearsal (no real data): what it found, and what of it still holds
**On the shape of reading v2 (15 Nov; as draft v3 gave it).**
- Part 1 (protocol: chain entry 45; result: entry 48): 30 made-up Spanish messages written by the model, laid on the shape of the reading with its labels thrown away, enciphered under random keys and given reading errors. The rule of draft v2 (the highest share of keys with 80% or more of the letters right at q = 0.35) picked D3.
- Part 2 (entry 64; reported only): each made-up reading at q = 0.35 against 100 shuffled copies of itself. 19 of 30 beat every copy; of those, 5 had the key at 80% or more, 5 between 50% and 80%, 9 under 50%. **So a pass on the score bar says that the reading has the structure of enciphered language. It does not say that the key is right.**
- Part 3 (entries 65 and 66; reported only): the strip rule of §8 tried on the made-up keys. The table is below, beside its repeat.

**On the shape of reading v3 (16 Nov).** The desk's addendum asks what still holds on the new shape.
- **Part 1, repeated** (protocol: entry 140; result: entry 142; the same 30 messages, seeds and rule). Keys with 80% or more of the letters right, of 30, new shape and (in brackets) old:

| Condition | D1 | D2 | D3 |
|---|---|---|---|
| q = 0.20 | 8 (12) | 3 (3) | 12 (10) |
| **q = 0.35 (decides)** | **0** (2) | **2** (1) | **4** (6) |
| q = 0.50 | 0 (0) | 4 (1) | 5 (0) |
| No errors at all | 30 (30) | 8 (4) | 28 (30) |
| q = 0.35 and one sign in ten missed | 1 (1) | 2 (1) | 1 (1) |

  **The choice holds: D3 on both shapes.** At q = 0.35 its share is 4 of 30 on the new shape (95% interval 4% to 31%) and was 6 of 30 on the old (8% to 39%); the difference is within chance, and together they are 10 of 60 (8% to 29%). On the new shape D3 read more of the letters than D1 in 16 of the 30 readings, fewer in 14, the same in 0. My forecast that D3 would again reach 6 of 30 missed.
- **The power to expect, restated.** If about a third of the doubtful signs are wrong, about one chance in six that the key comes out right; next to none if the reading has missed one sign in ten. On a reading without errors D3 found the key in 28 of 30 and D1 in 30: the limit is the reading far more than the search.
- **Part 2 was not repeated in full.** For parts 3 and 4 each made-up reading was solved with 20 shuffled copies of itself, every solution kept (protocol: entry 146; 630 solves; the solution of each reading has the score part 1 found in 30 of 30). Against 20 copies, a looser bar than the plan's, 25 of 30 beat every copy; 4 had the key at 80% or more, of which 4 beat every copy; 12 beat every copy with a key under 50%. The point of part 2 stands on the new shape: the score bar passes on wrong keys. The run with 100 copies can follow if the desk wants it before the seal; the seeds go on where these stop.
- **Part 3, repeated from those kept solutions** (the analysis of the first, line for line; the null k modelled from 600 null keys, where the first had 300). Chance that the strip rule passes, new shape and (in brackets) old:

| n, the classes the strip gives | Key at 80% or more (4 readings; old 6) | Key 50% to 80% (9; old 7) | Key under 50% (17; old 17) | Bar and strip, all 30 readings |
|---|---|---|---|---|
| 5 | 56% (46%) | 11% (5%) | 0% (0%) | 11% (9%) |
| 8 | 80% (79%) | 25% (12%) | 0% (1%) | 18% (15%) |
| 12 | 91% (93%) | 49% (25%) | 0% (1%) | 27% (20%) |
| all | 100% (100%) | 44% (14%) | 0% (0%) | 27% (20%) |

  In the last column the bar is "beat every one of 20 copies" on the new shape and "every one of 100" on the old, so the two are not like for like. A null key gives the commonest class its true letter 38% of the time (old 36%) and the second commonest 18% (old 17%). **Read plainly, as before: the rule is safe, and it is weak when the strip is short.** Nothing in the rule was changed on the strength of either run; J. ruled on 15 Nov to keep it as drafted.
- **Part 4, new: the word rule of §10b tried on made-up data** (protocol: entry 146). The "Bureau's words" were the words of eight letters or more of each made-up plaintext; nothing came from a closed source. Of the 30 readings, 29 have such a word in their text.

| The solution's key | Readings (with a long word) | A long word found | Rule passes against its 20 null solutions | Long words found, of all in those texts |
|---|---|---|---|---|
| 80% or more right | 4 (4) | 2 | 2 | 2 of 16 |
| 50% to 80% | 9 (9) | 1 | 1 | 1 of 23 |
| Under 50% | 17 (16) | 0 | 0 | 0 of 46 |

  Of 600 null solutions, 0 hold a long word of their reading's plaintext; 4 hold one of five to seven letters. Under a true strip the decode holds a long word in 0 of 116 trials when the strip gives 8 classes, 1 of 116 at 12 and 60 of 116 at all; under the same strips with the letters moved one place round, 0, 0 and 0. **Read plainly: the word rule is safe and weak.** At this rate of reading errors most stretches of eight signs hold one that is wrong, and one wrong sign loses the word.
- **Part 4 again, for the count J. ruled on** (protocol: entry 168; result: entry 169; nothing solved, the same kept solutions). A word is found if all its letters fit, or all but one. Run with no letter allowed wrong, part 4's figures came out again.

| | Every letter fits | One letter may be wrong |
|---|---|---|
| Keys at 80% or more: readings with a long word found, of 4 | 2 | 3 |
| Keys at 80% or more: long words found, of 16 | 2 | 6 |
| Keys 50% to 80%: long words found, of 23 | 1 | 2 |
| Keys under 50%: long words found, of 46 | 0 | 0 |
| Null solutions with a long word, of 600 | 0 | 0 |
| Null solutions with a word of five to seven letters (decides nothing) | 4 | 83 |
| True strip of 8, 12, all classes: decodes with a long word, of 116 | 0, 1, 60 | 2, 7, 104 |
| Wrong strips with a long word | 0, 0, 0 | 0, 0, 0 |

  **On this data the new count is as safe as the old and about three times as strong for a right key.** It is still weak when the key is half right or the strip is short.
- **Stage B, two trials** (protocols: entries 141 and 145; results: 144 and 147). Each of the 30 made-up readings at q = 0.35 was decoded under strips drawn at random from its true key, four strips for each size, and under the same strips with the letters moved one place round. Passes with the true strip, of 120:

| Signs on the strip | Word coverage, "first" | Word coverage, "sure" | Letter table, "first" | Letter table, "sure" |
|---|---|---|---|---|
| 5 | cannot pass | cannot pass | cannot pass | cannot pass |
| 6 | cannot pass | cannot pass | cannot pass | cannot pass |
| 7 | 0 | 0 | 31 | 29 |
| 8 | 1 | 0 | **54** | 51 |
| 12 | 13 | 2 | **100** | 99 |
| every class of the key (18 to 22) | 109 | 41 | **120** | 120 |

  Wrong strips passed in 1 of 720 trials with word coverage and "first", and in 0 of 720 with the letter table and "first". The first trial had word coverage alone and showed it to have next to no power on a short strip: the signs the strip lacks cut the decode into stretches too short to hold a word. The second added the letter table and chose by a rule entered before it ran: the most passes with the true strip at 8 and 12 signs together, among pairs whose wrong strips pass in at most 1% of their trials. **Chosen: the letter table with decode mode "first".**
- **Every forecast of the rehearsal's protocols of 16 and 17 Nov, with what came** (the desk's finding 2 of 05:16Z). All on made-up data. "Missed" marks a forecast of 0.50 or more that did not come, at full weight. Mean Brier score over the 22: 0.1375. The forecasts of part 3 of 15 Nov are scored in chain entry 66.

| Protocol (chain entry) | Forecast | P | What came | |
|---|---|---|---|---|
| Part 1 on the new shape (140) | D3 is chosen | 0.60 | D3 | came |
| | D1 is chosen | 0.35 | D3 | did not |
| | D3 finds 6 right keys of 30 or more at q = 0.35 | 0.50 | 4 | **missed** |
| Stage B, first trial (141) | "first" is chosen | 0.60 | "first" | came |
| | at 8 signs the chosen mode passes in half the trials or more | 0.15 | 1 of 120 | did not |
| | at 12 signs, the same | 0.60 | 13 of 120 | **missed** |
| | wrong strips pass in 1% of their trials or fewer | 0.90 | 1 of 1,200 | came |
| Stage B, second trial (145) | the letter table is chosen | 0.90 | the letter table | came |
| | "first" with it | 0.60 | "first" | came |
| | at 8 signs the chosen pair passes in half the trials or more | 0.45 | 54 of 120 | did not |
| | at 12 signs, in three quarters or more | 0.55 | 100 of 120 | came |
| | its wrong strips pass in 1% or fewer | 0.90 | 0 of 720 | came |
| Parts 3 and 4 (146) | no null solution of 600 holds a long word | 0.90 | none | came |
| | every reading with a key at 80% or more and a long word in its text has one found | 0.60 | 2 of 4 | **missed** |
| | some reading with a key under 50% has one found | 0.20 | none | did not |
| | the strip rule at 8 classes passes for keys at 80% or more with a chance of 70% or more | 0.60 | 80% | came |
| | for keys under 50%, 2% or less at every size | 0.85 | 0.2% at most | came |
| Part 4 again (168) | no null solution of 600 holds a long word | 0.80 | none | came |
| | keys at 80% or more find 6 or more of their 16 long words | 0.60 | 6 | came |
| | all four of those readings pass against their 20 null solutions | 0.50 | 3 | **missed** |
| | some reading with a key under 50% has one found | 0.25 | none | did not |
| | under a true strip of 12 classes, a long word in 10 or more of 116 trials | 0.50 | 7 | **missed** |

- **One thing the rehearsal does not model.** A made-up key has a class for every letter its text uses: 18 to 22 classes in these 30 messages, and 0 of them with 17 or fewer. Reading v3 has 17. Either the message is short of rare letters, or two letters share a class in the reading. In the second case no one-to-one key reads the message whole.

## 10. Stage B: with the strip (sealed fallback, runs only if stage A misses)
- **Input.** Blind reading v3 as stamped, through `STRIP_v1.json` as made at §8 steps 2 to 5. By J.'s ruling of 01:28:03Z on 16 Nov nothing is read again by a reader who knows the letters before the bar is computed, and by his ruling of 14:39:56Z the one judgment stage B still rests on, the match of strip signs to classes, is made with the strip's letters covered. Every input of stage B is fixed before any result is opened.
- **Decode** (`stageB_v3.py --stat letters --decode first`). Every read sign takes its first label. A sign that is unread, or whose class the strip does not give, breaks its group there. A sign the strip gives as two letters decodes as those letters.
- **Statistic: the letter table.** The mean score of a decoded letter under the plan's Spanish table (`lm_es_v1.i32`, the table stage A uses), each stretch of decoded letters scored from a fresh start as §7 has it. Changed from word coverage after the first made-up trial, by the rule of the second (§9). Word coverage is computed beside it (`--stat words`, the list of draft v3: 18,062 words from the plan's three Spanish texts) and decides nothing; so are the German and English tables.
- **Null.** Re-pairings of the strip's letters over its signs, each different way of decoding the reading counted once. If there are at most 50,000 they are all listed and p = (those whose statistic is at least the message's, the strip's own among them) / (all of them). Otherwise 1,000 are drawn, none equal to the strip's own, with seed 6980002, and p = (b + 1)/1,001.
- **Bar:** p ≤ 1/1,001.
- **The smallest p the strip allows.** With n signs on the strip, m of them in the reading, there are n!/(n − m)! re-pairings when the strip's letters all differ, and the smallest p is one over that number, or 1/1,001 when they are drawn. **Stage B cannot pass unless there are at least 1,001 re-pairings: with every strip sign in the reading, 7 signs or more.** Six give 720. The script prints the smallest p and says when the test cannot pass.
- **Power on made-up readings at q = 0.35** (§9): the true strip passed in 26% of trials at 7 signs, 45% at 8, 83% at 12, and in every trial when the strip gave every class.
- **What a pass shows.** That the strip's pairing fits the message better than its letters shuffled over its signs. It does not show that the message is read.
- **After the bar.** A re-reading of both frames against the strip's shapes may be made once stage B's output is stamped; its first line says "not blind", its figure is reported beside the bar's and decides nothing. **Fills** for letters the strip lacks are graded and kept apart, as in catalogue 756: by the strip; by a fill that fits at two or more places; by a single fill; unread. The fills are stamped before the words file of §10b is opened.

## 10b. The Bureau's 1917 reading: a sealed claim rule
**By J.'s rulings of 03:45:21Z and 14:39:56Z on 16 Nov.** The desk suggested the rule's shape (its addendum, release 1); see §4 on what that may mean.
- **What it is for.** Draft v3 gave the Bureau's text no sealed role: "the agreement is reported". Now a claim of agreement may be made only through this rule. It makes no hit.
- **The words file is the desk's, and it is made.** SHA-256 **`60d507b9c0bbb8a842be0e6b5e619cf2e9368e623f0b742f8432f650ca1ee879`**, by the desk's verdict of 14:23Z on 16 Nov. Three receipts on it, all of 14:22:21Z on 16 Nov, are in `from_desk/WORDS_visser698_receipts_2026-11-16_1422Z.zip` (SHA-256 `4963ded0b560e96ef28462efbcff6a004da64dac83c26292a506f1454e4265fd`); they verify here against that digest alone and fail against a digest changed in one figure. The chain holds the hash in entry 157, before any run. The file is with the desk and J.; this chat has not seen it and does not know whether it holds a word. Its "rule" field names draft v4, by whose six points it was written; they stand here unchanged:
  1. A source counts if it gives one or more words as standing in the 1917 reading of this message, in the language of that reading. A source that gives the reading only in translation counts for the names of persons and places it gives, and for nothing else.
  2. Every such word is entered once for each form in which a source prints it. A word broken at a line end is joined. No word is corrected.
  3. Words of any length are entered; the script takes those of eight letters or more.
  4. The file is JSON: `{"salt": "<32 random hex digits>", "rule": "<SHA-256 of the plan draft this rule was read from>", "sources": [{"id": "S1", "what": "…", "address": "…", "opened_utc": "…", "gives": "words" | "names from a translation" | "nothing"}], "words": [{"form": "<as printed>", "source": "S1", "where": "<page, column or frame>"}], "left_out": [{"form": "…", "why": "…"}]}`. The script reads "words" alone.
  5. If no source gives such a word, "words" is empty and the file is still written. The salt keeps the hash from telling whether it is.
  6. The desk gives this chat the SHA-256 of the file and nothing else. It is entered in the chain before the seal, so the chain shows the words fixed before any run. The file stays with the desk and J. until §5 opens it; the script refuses a file with any other hash.
- **The count** (`bureau_check_v2.py`; J.'s ruling of 14:39:56Z on 16 Nov: "One letter may be wrong"). Each form goes through the plan's normaliser; the forms of eight letters or more, each once, are the words. The message is one row of places in reading order; a word may run over a dash or a line end. At each place stand the letters the sign may have: under a stage A solution, the letter of its first label and of every alternate the reading lists; under the strip, the letter or letters the strip gives for those labels. An unread sign has none. **A word is found if it can be laid on consecutive places with every letter fitting, or every letter but one:** one place may be taken as one letter of the word whatever stands there, be it a sign read or keyed wrongly, an unread sign or, under the strip, a sign the strip does not give. K is the number of words found. The count with every letter fitting is written beside it and decides nothing.
- **Whose idea.** Draft v4 said such a count would be stronger and left it out. The desk suggested it in its verdict, as a hand that knows the words file and says so. Its safety does not rest on either of us: the null solutions and the re-pairings are counted in the same way.
- **Stage A form.** K for the message's solution and for each of the 1,000 null solutions, in each language. **Pass: K ≥ 1 and K greater than the K of every null solution.**
- **Stage B form.** K under the strip's pairs and under re-pairings listed or drawn as in §10 (seed 6980003). **Pass: K ≥ 1 and p ≤ 1/1,001.**
- **What may be claimed.** Where a form passes, the note may say that the solution, or the strip's decode, holds, but for one letter at most, a word that a source gives from the Bureau's reading, and that shuffled signs or shuffled strip letters do not; and it says whether every letter fitted. Where none passes, or the file holds no word of eight letters or more, the note claims no agreement with the Bureau's reading, whatever is seen once the sources are open; what is seen is then printed as seen, marked "not evidence".
- **What a pass does not show:** that the whole message is read.
- **The check on the desk's file.** After the word rule's output is stamped this chat opens the closed sources and checks the file against them: that every word stands where the file says, and whether the sources give any word of eight letters or more that the file lacks. Such a word takes no part in the rule and is printed.
- **On made-up data** (§9, part 4 again): of 600 null solutions, 0 held a long word of their reading's plaintext. A key at 80% or more found 6 of 16 long words, in 3 of 4 readings.

## 11. Forecasts (a calibration record, not evidence)
| Event | P, this draft | v5 | v4 | v3 | v2 | v1 |
|---|---|---|---|---|---|---|
| Stage A hits (bar and strip) | 0.05 | 0.04 | 0.04 | 0.04 | 0.15 | 0.25 |
| Stage A passes its bar but fails the strip | 0.30 | 0.30 | 0.30 | 0.30 | 0.05 | 0.05 |
| The strip gives five or more legible pairs | 0.75 | 0.65 | 0.65 | 0.65 | 0.65 | not asked |
| The strip gives seven or more classes of reading v3, surely matched | 0.50 | 0.40 | 0.45 | not asked | | |
| Stage B passes its bar, given that stage A missed | 0.25 | 0.22 | 0.25 | 0.60 | 0.60 | 0.60 |
| The plaintext language is Spanish, given any reading | 0.85 | 0.85 | 0.85 | 0.85 | 0.85 | 0.85 |
| The Bureau's 1917 text is found on the roll | 0.25 | 0.25 | 0.25 | 0.30 | 0.30 | 0.30 |
| The desk's words file holds a word of eight letters or more | 0.70 | 0.70 | 0.70 | not asked | | |
| The word rule passes in either stage | 0.10 | 0.10 | 0.06 | not asked | | |

- **The strip, 0.75 and 0.50; they were 0.65 and 0.40.** The desk counts 27 marks on the strip that may be signs (its verdict of 05:16Z). Before that this chat knew only that the strip is torn and has two rows. Reading v3 has 17 classes, and a key of 27 places could give most of them. What holds both figures down is the match: by shape alone, between a strip and a message photographed apart at poor resolution; and whether the letters can be read.
- **Stage A: the hit 0.05, a pass on the bar that the strip refuses 0.30.** The new shape gave 4 right keys of 30 where the old gave 6; reading v3 has more sure signs than v2 (77 against 69) and may be nearer the truth. The two pull against each other. The hit moves from 0.04 to 0.05 for the strip's count alone.
- **Stage B, 0.25; it was 0.60 in drafts v1 to v3, 0.25 in v4 and 0.22 in v5.** The 0.60 was made for a test that, as coded, could not pass on a short strip, and that had next to no power once that was mended. With the letter table a true strip of 8 signs passes in 45% of made-up trials and of 12 in 83%. The strip is known to be torn (§4), it must give 7 classes or more, and H1 may be wrong. In v5 it went from 0.25 to 0.22, and the strip's seven classes from 0.45 to 0.40, for the covered match: from shapes alone I expect to call fewer matches sure. Both go up here for the desk's count of the strip's marks.
- **The Bureau's text on the roll, 0.25 as in v4; it was 0.30 before,** on the desk's "No" of §3, which covers what the desk opened and not the roll's other frames.
- **The words file, 0.70.** The desk's suggestion speaks of a word of eight letters or more and of its spelling; it was written with the sources open (§4). I read that as a sign that such a word exists and say so, since it is a guess from the wording.
- **The word rule, 0.10; it was 0.06 in v4.** It needs a word in the file, and then a key and a reading that are right over that word but for one sign, or a strip that gives its letters but for one. On made-up data a right key found 6 long words of 16 with one letter allowed wrong, where it found 2 with none.

## 12. Stopping and kill rules
- One run per language in stage A; stage B once; the word rule once per form; no further design without a new sealed plan.
- If neither stage reads the message, the target is closed with a report and the miss prints.
- **Nothing is sealed or run on catalogue 698 until the question on issue #542 is answered, or J. rules again** (his ruling of 03:45:21Z on 16 Nov). The desk may pass the plan meanwhile. The answer is a comment on a thread this chat keeps closed: J. or the desk reads it first, and this chat is told only whether the other folder's work goes on.

## 13. Inputs and scripts (SHA-256)
| File | SHA-256 |
|---|---|
| `visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md` | `ddb270fbe48f6973be35256819d0452df81c6953e11d44e15e35810592e2cded` |
| `visser698/solve/stageA_v3.py` | `380ab0cf808f3ca8bd96db33b6eb0683f8be59c381dbfee95d3f710d4e003b34` |
| `visser698/solve/stageA_params_v1.json` | `4b4fa755a49bc8ce79a3762303cfac4d1ba98a83054758f7c4e25e342019c4e3` |
| `visser698/solve/lib698_v1.py` | `40ad0f9a1c5dce5c66b0722ecde236973468747aadde6b3f6e9f3de21455793b` |
| `visser698/solve/sa_core_v1.c` | `7441355ca2a942f13cabfb52cfb469567b70fbd77399711b724bbf6fc2551229` |
| `visser698/solve/sa_core_v1.so` (gcc 13.3.0, `-O2 -shared -fPIC`, x86-64 Linux) | `783bbe13131772359fac9f7de811678634582a3d9e50513aa6378dcbc8c08b3d` |
| `visser698/solve/lm/lnq4096_v1.i32` | `23a658b2a16e62d18845a92633af24f741e70c937f0f580c901719305006edd5` |
| `visser698/solve/lm/lm_es_v1.i32` | `558c1251d529b3853ecde5ed99c72b3b1c31dcbe5b4451a4fc2219a62fc5bdbf` |
| `visser698/solve/lm/lm_de_v1.i32` | `a13b5b6ffd83e63b9bbbb70977a42cbc7a3ecce3dc0237a6b0b9fdd231e92556` |
| `visser698/solve/lm/lm_en_v1.i32` | `a47e58f5134a7384cae0b36918dc3da11c5dc6e4c9922db72b2ca005bb1133b2` |
| `visser698/solve/build_lm_v1.py` | `ed6230a5036d4f2789fe912eda165129c6054b9924376ab61aa212152918a7a3` |
| `visser698/solve/strip_check_v1.py` | `1f56bd9231bef2bddc9e51488cac775c1c892b2d1a02e2b9c646905df22f4075` |
| `visser698/solve/stageB_v3.py` | `350720377d81b9353aa9bd57e320957ba9d397baee7458833677744573f8f75c` |
| `visser698/solve/bureau_check_v2.py` | `71fc6eee98a2a39b365bbc55ac4a86c9a7f4a2f88a0627f665d2123cbf874f72` |
| `visser698/solve/make_strip_v2.py` | `50e95f234fdf93c85fc28436b8709a3caf55805ac973db91378d65a1315fcfa9` |
| `from_desk/COVER_frame42_v1.json`, the desk's; its receipts in `from_desk/COVER_frame42_v1_receipts_2026-11-17_0507Z.zip` (`930eca269ed6b103abd66e1ed023069ae1202c3c6adbe95305225919df7b226e`) | `e49f163dd50feeaca3884f484e857c4e38d82b107c7f717ea5cb6db3f83556d8` |
| Frame 42 as the desk fetched it at 04:36Z on 17 Nov (not held here) | `503696999c8ce5295dbeb49d5c35c7a469e294c8cbca87a16152e0f90ac2cf1b` |
| The desk's hash list of its 27 tiles, with each tile's SHA-256 and pixel hash and the SHA-256 of its order file, its tile script, the cover file, the frame and its pixel hash, and the tiles zip: `from_desk/HASHES_tiles_frame42_v1_2026-11-17_1759Z.txt`, stamped 17:59:55Z, 17:59:58Z and 18:00:02Z, chain entry 246 (§8 step 2) | `e7478813cbcbb0a0cfe094657f058b2b000e2db33501f2ec7bae726faf7b3fe8` |
| The desk's words file (not held here; receipts in `from_desk/WORDS_visser698_receipts_2026-11-16_1422Z.zip`) | `60d507b9c0bbb8a842be0e6b5e619cf2e9368e623f0b742f8432f650ca1ee879` |
| `visser698/solve/words_es_v1.json.gz` (reported only) | `272a7c29c1bef2b3e81bd55310e5282857b9aecde05965397c192f0a717721d3` |
| `visser698/solve/build_words_v1.py` | `ff4f88d7b1b6eb4194b59d41a458e84ee68ae44bdad48ca93bfec58bd23529e9` |
| `visser698/solve/gen698_v1.py` | `865eb5465aee1950199aed690161837bf233f41620302faf65077b7ccf121302` |
| `visser698/rehearsal/messages_v1.txt` | `762f1ff042c0c40c432e740669b4e49e793adec88e4a492044a3cfe3be906089` |
| `visser698/rehearsal/rehearsal_params_v1.json` | `94ee8c003de338a16afd740231135fdc0b605a160753292bd0fadcf37b45693f` |
| `visser698/solve/rehearsal_v1.py`; `visser698/solve/rehearsal_v2.py` | `879d456c0ba979f99c1869414205dcfdb8f6ce4456eabfa656e8c7c5d6004c1f`; `d3ba51888a8acfd0f4c214e58019c2985f66f11cb0b9c9c24063958d3f74c1df` |
| `visser698/solve/rehearsal_null_v1.py`; `visser698/solve/rehearsal_null_v2.py` | `2f23cae3e6b3833ae35b961ca1d5d9c1d51edf3960a747fffc3f8dfc16540174`; `039901a9cb12497f7a570eb20973f1f2ca59b98676d640b89495a385ecec157a` |
| `visser698/solve/rehearsal_strip_v1.py`; `visser698/solve/rehearsal_strip_v2.py` | `c7055c4e0db0712e8507f267cdaabdfb5a95e16543d53fad0b2f68658551663e`; `cd8c5a39121aadd72e253b3bcb174816cc2cbc57ef09a6991ce2098518eab73b` |
| `visser698/solve/rehearsal_stageB_v1.py`; `visser698/solve/rehearsal_stageB_v2.py` | `c5b22e5cf2a5a44eab0a47c72e4cd1383613473ee04cc07dfccbd4d908b94061`; `0a4eedafce75f21c39a2e0435317c09dc141d7c46f2e67da58818d12b886c8ab` |
| `visser698/solve/rehearsal_bureau_v1.py`; `visser698/solve/rehearsal_bureau_v2.py` | `146471435651ed55d6ecc8a8f65ca62fa645abcc8c1c5400a0abfa6d35c6a183`; `b8c36aa510a1d5593d592f8963748fbf9c9f8601b662aed294757ebaf1c2ecd6` |
| `visser698/solve/crosscheck_v1.py` | `dfcb75ba4d5ab91225209fd7313df1f6e70f0f3d03282da7ff9be9ad04075214` |
| `visser698/rehearsal/PROTOCOL_rehearsal_v1_2026-11-15_0021Z.md` | `936d0f30c4f7d489ad4a6964ebff685b420133e2dd2dd56a5340ddac20c4acf3` |
| `visser698/rehearsal/PROTOCOL_rehearsal_v1_part3_2026-11-15_0159Z.md` | `4be0ee86cf58f9bb2eae189506f3ddd069e660e656b7a52817b8a7185f9907d8` |
| `visser698/rehearsal/PROTOCOL_rehearsal_v2_part1_2026-11-16_0244Z.md` | `990cbc76e9908ae41d36e82ac03d2df5c165f66392d59bf7f7b06b03d641e051` |
| `visser698/rehearsal/PROTOCOL_rehearsal_stageB_2026-11-16_0248Z.md` | `108100ed00d7a9eefa32cfddcdd5915ffd8f81b2ea66c0bd15c9c504572c1fb6` |
| `visser698/rehearsal/PROTOCOL_rehearsal_stageB_v2_2026-11-16_0349Z.md` | `f43800b3d8e7aacc1c8e042ccf3752949c612e91921f799435e710a5ae62cc88` |
| `visser698/rehearsal/PROTOCOL_rehearsal_v2_parts3and4_2026-11-16_0355Z.md` | `a29b7963a77469d15bd937348e71afcb876ac1000eee0ffed4780a72bd7320ab` |
| `visser698/rehearsal/PROTOCOL_rehearsal_v2_part4b_2026-11-16_1452Z.md` | `4e3b6f96ff881921e1443011fb1cad9787ebd2a1baebd756f31c0be0db4010c9` |
| `visser698/rehearsal/REHEARSAL_v1_part1.json` | `0c5f19d37381256d10a716e5765f861872d4249b7dfde3a2eb36296ce27b7a0b` |
| `visser698/rehearsal/REHEARSAL_v1_part2_D3.json` | `aab8744bc15a568b46cb1f7ea4533e10251bf5517d97deb1cc1a9658e81b1e9a` |
| `visser698/rehearsal/REHEARSAL_v1_part3_strip.json` | `a66ec8a0ef696c454fa8f44b3ecf9b329e30d9092a8b2d9f783c28a7b42e54fd` |
| `visser698/rehearsal/REHEARSAL_v2_part1.json` | `a58b6244e4ee3d98f839600b44ac3baf760e34e011a43bce221416973704b8ed` |
| `visser698/rehearsal/REHEARSAL_stageB_v1.json` | `6a6e5a9a94f7970c47441dd0ac5216c520fde59ba44ccfb507d3f1c21d2e5151` |
| `visser698/rehearsal/REHEARSAL_stageB_v2.json` | `70d56d5b74492d591f0c2048ec5337c9fce9dbd8286daeaec223964df523474e` |
| `visser698/rehearsal/REHEARSAL_v2_null20.json` | `ce453d8a42ec82992e5491fc7984d461e49088c8ec79ca0d9716acd6ce0e28d7` |
| `visser698/rehearsal/REHEARSAL_v2_part3_strip.json` | `a6b2978e0c85d60070ed1e94ebd3c26c94698c9c1a1b0b814059ab0950c74386` |
| `visser698/rehearsal/REHEARSAL_v2_part4_bureau.json` | `3006a0b81b918847c788e26a9a62b0c63567fe10e2d5510bb638fef48624e9d2` |
| `visser698/rehearsal/REHEARSAL_v2_part4b_exact.json` | `7e2164c3ea73bffda75ea78dac237f824474b155e31d4801b1df3e2022565929` |
| `visser698/rehearsal/REHEARSAL_v2_part4b_one_wrong.json` | `a11b061225b88b23082d99613f8c71f12939aade6a0d783f3d4f31931687f53a` |
| The ledger's `lang/lm.py` and `lang/corpora.py` | `4fc50cdd52276d6820aa79df8e6e5bf484673b4b932d2282581cc04dc407f1b4`, `8c9fb1da43ba9f1a67e158d923f428f6358b3d5ea0653530505da9d66373062c` |
| *Don Quijote*; *Fortunata y Jacinta*; *Los cuatro jinetes* | `27f5064a245209b6d83f7d95e51b2cb6a15ebec02b2518c80cbc1d2cd036429e`; `0070a89a2c2d927c333fed0d2b0801e518d05dbbfc9e328eabddf718ccf6ad2f`; `1900a99c90662dfdab798d020d7c186a888992f253c8d8156f22f5f2f53ed8e2` |
| The eight German files; `bapco1534/lang/quad26.f32` | in `visser698/solve/lm/lm_de_v1.json`; `058b1e5f6743bb3a8a0cc47db239bc31530ec165508ee584bbb98e49071546aa` |
| Not inputs any longer, kept: `visser698/READING_visser698_blind_v2_2026-11-14_2157Z.md`; `visser698/solve/stageB_v1.py`; `visser698/solve/stageB_v2.py`; `visser698/solve/bureau_check_v1.py`; `visser698/solve/cover_frame42_v1.py`; `visser698/solve/make_strip_v1.py` | `24d3f1ab3641c1dd0ff37fd14b670a39e8a675eb92e8bd581a2d16646b0e1ab5`; `a3ad5cfb5dd36a5c068c83b1409d270866166ee04568e2b039e43cafbb3396c0`; `f20a0f070a055ea46713896bc0654f381dcd4d9ff8878667f2de647ed7273a65`; `16411a52263cd8db60b77981a601197cac4328c7c1e5cdd8d9d0c88c3d2ff0bb`; `d1ffc65019cb4b5bf3d7a526ebb76b00745f24b2bc4d8fb3a7a76dbbb49b719f`; `d4bc83fece5c58e511fb41459a086821751adfbb628ea472ef2c6e3333b96bf8` |

**The runs, as they will be typed** (PLAN is the sealed file; `<lang>` is `es`, then `de`, then `en`; TILES is the folder of the desk's tiles, ORDER its order file, CUT its tile script, COVER its cover file and WORDS its words file):
1. `python3 -I visser698/solve/stageA_v3.py . visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md visser698/solve/stageA_params_v1.json visser698/RESULTS_visser698_stageA_<lang>.json --sealed-plan PLAN --langs <lang>`
2. `sha256sum -c` of TILES against the hashes the chain holds, and, for a tile whose file hash differs, its pixel hash; the match is made from TILES alone.
3. After the match is stamped: ORDER and CUT checked by `sha256sum` against the chain; frame 42 fetched with `curl -sS --fail` from the address COVER gives, the fetch logged, its SHA-256 checked against COVER's; CUT run on that frame and COVER, as its own usage line gives, into a new folder; each tile compared with TILES at the place ORDER names. After the letters are stamped: `python3 -I visser698/solve/make_strip_v2.py visser698/STRIPMATCH_v1.json visser698/STRIPLETTERS_v1.json visser698/STRIP_v1 --order ORDER`
4. `python3 -I visser698/solve/strip_check_v1.py visser698/RESULTS_visser698_stageA_<lang>.json visser698/STRIP_v1.json visser698/STRIPCHECK_visser698_<lang>.json`
5. If stage A missed: `python3 -I visser698/solve/stageB_v3.py visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md visser698/STRIP_v1.json visser698/solve/words_es_v1.json.gz visser698/RESULTS_visser698_stageB_letters.json --stat letters --decode first`; beside it, reported only, the same with `--stat words`, and with `--stat letters --lm` for the German and the English table, each to its own output.
6. `python3 -I visser698/solve/bureau_check_v2.py stageA visser698/RESULTS_visser698_stageA_<lang>.json visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md visser698/solve/stageA_params_v1.json WORDS visser698/BUREAU_visser698_stageA_<lang>.json --expect 60d507b9c0bbb8a842be0e6b5e619cf2e9368e623f0b742f8432f650ca1ee879`, and, if stage B ran, `python3 -I visser698/solve/bureau_check_v2.py stageB visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md visser698/STRIP_v1.json WORDS visser698/BUREAU_visser698_stageB.json --expect 60d507b9c0bbb8a842be0e6b5e619cf2e9368e623f0b742f8432f650ca1ee879`

## 14. What changed from draft v6, and why
**By the desk's finding on ask 21** (its verdict of 18:00Z on 17 Nov; chain entry 245): **weakness 12's last sentence** is replaced by the desk's words, quoted under its name. One sentence of this chat's is put before them, "The cover file's rectangles are in this chat's context.", so that the desk's "They" has its subject; it keeps the fact of the sentence it replaces.

**What §15 asked for, now in hand.**
- **§13:** the row for the tiles names the desk's hash list of 17:59Z and its SHA-256 (entry 246), where v6 said "to come before the seal".
- **§15:** items 1 to 3 are marked as met, with their sources; item 4 is given at the seal.
- **§3:** the question went up on #542 at 13:41:00Z (entry 225), and the answer has come, as the desk relays it (entry 245).
- **§1:** the desk's check of the ledger at main `e857642f`.

**Not changed:** every other line of v6, as `visser698/DIFF_plan_v6_to_v7.txt` shows: the hypotheses, the language models, both stages, the seeds, the bars, the forecasts, the word rule, and every hash of §13 but the tiles' row.

## 14a. What changed from draft v5 to draft v6, and why
What changed from draft v4 to draft v5 is in draft v5's own §14 and is not repeated here.

**By the desk's two findings on ask 18** (its verdict of 05:16Z on 17 Nov; chain entry 179).
- **Finding 1 (the tiles hid the order from a look, not from a reckoning).** J. ruled "Desk cuts the tiles" (entry 180), after this chat told him that the cover file's whole text is already in its context. §8 steps 2 to 5, §5 and §13: the desk cuts each sign centred on a plain ground and keeps the order with J.; this chat gets the tiles alone after the stage A results are stamped; after the match it fetches the frame, runs the desk's tile script on it and checks every tile at its place; the letters are read then. Draft v5 said its tiles came "in an order this chat cannot know". That was not true of those tiles, and is withdrawn. `cover_frame42_v1.py` is no longer used.
- **Finding 2 (the missed forecasts of part 4 again were not printed).** §9 now prints every forecast of the rehearsal's protocols of 16 and 17 Nov with what came: five misses, at full weight.

**The desk's notes.**
- The places of `STRIPLETTERS_v1.json` are numbered as the cover file numbers its "signs" (§8 step 4).
- `make_strip_v2.py` names a letter given to two or more classes as well, reported only (§8 step 5).
- The cover and the tiles rest on the desk's judgment of which marks are signs: §16, weakness 14.

**Otherwise.**
- **§4:** what the desk's verdict of 05:16Z tells this chat, and the cover file's text in its context.
- **Forecasts (§11):** the strip's two lines up for the desk's count of 27 marks; stage A's hit from 0.04 to 0.05; stage B from 0.22 to 0.25.
- **§1:** the ledger at main `b13ebd1b`.
- **§3:** the question in its third form, gone to J. to post.
- **The provenance block** names the model of each draft, as the desk asked in its message of 05:33Z.
- **§16:** weakness 12 rewritten; 14 and 15 new.
- **Not changed:** the hypotheses, the language models, stage A's solver, design, budget, seeds, null and bars, the strip rule, stage B's statistic, null and bar, the word rule, and every hash of draft v5's §13 for a file still in use.

**Provenance, measured.** `prov/words2.py`, runs of six words or more, against six log copies (`SESSION_78298d5e_2026-11-14_222834Z_pre_compaction.jsonl`, `SESSION_78298d5e_2026-11-14_234311Z_at_handoff_close.jsonl`, `SESSION_eea13873_2026-11-15_011817Z_pre_compaction.jsonl`, `SESSION_eea13873_2026-11-15_192308Z_pre_compaction.jsonl`, `SESSION_eea13873_2026-11-16_025158Z_pre_compaction.jsonl` and `SESSION_eea13873_2026-11-17_054654Z_before_plan_v6_draft.jsonl`). Six of this file's words are J.'s verbatim: the ruling he typed in a box at 22:24:49Z on 14 Nov, quoted in §2. The tool reports more, and every further run it finds lies in the turns of 14:34:40Z on 16 Nov and 05:33:22Z on 17 Nov, which are the desk's messages as J. pasted them: those are the desk's words and file names, not his, and the tool cannot tell a paste from typing. 129 words stand in labels he chose by box, which the model wrote. Turns of J.'s read: 43 chosen by box, 21 typed, 2 typed in a box; the 21 include the desk's messages he pasted. J.'s words of 01:11:22Z on 16 Nov, quoted in §2 from the desk's addendum, stand in no log this chat holds; they are quotation and are not measured.

## 15. Settled at the seal
1. **The desk's check:** FIX BEFORE SEAL, one sentence, on draft v6 (verdict of 18:00Z, entry 245), made in draft v7 (§14). J. ruled at 18:34:50Z to seal on the desk's own wording without a further round (entry 256). Draft v7 goes to the desk with the stage A results.
2. **The desk's tiles:** their hashes are in the chain before the seal, entry 246 (the hash list of 17:59Z, SHA-256 `e7478813cbcbb0a0cfe094657f058b2b000e2db33501f2ec7bae726faf7b3fe8`).
3. **The answer on issue #542** has come (§3; entry 245), and J. has ruled to seal and run (entry 256). The rule of §12 is met.
4. **The chain's head at the seal.** The chain stands at 256 entries, head `2ba942b4a25625f392369294847beed3771c3b5ea6acf1f39f0da693c4dde2bd`. When draft v7 was written it stood at 253 entries, head `787aa085f5404e1334de002918b517a8015c2e522f6d7f88380e2121dcf431a1`.
5. **The ledger at the seal:** main `e857642f05223ae75f1b8385dee93c6adcf2dda2` (committed 17:54:44Z on 17 Nov, fetched 18:36Z). Row 698 has no `reserved` field in `catalogue.json` (SHA-256 `b5c1e2a3691b7491c3fdfad338d5d36a6926d077551cfb8a5129abecd6b8515b`); only rows 1424 and 1534 carry one. The last commit under `targets/visser1917` is still `fe4c0370` of 27 Oct, seen by its commit ids alone; the folder's text was not opened.
6. **The runs, as they will be typed** (PLAN is this sealed file; one invocation per language, in this order):
   - `python3 -I visser698/solve/stageA_v3.py . visser698/READING_visser698_blind_v3_two_frames_2026-11-16_0238Z.md visser698/solve/stageA_params_v1.json visser698/RESULTS_visser698_stageA_es_v1.json --sealed-plan PLAN --langs es --nproc 2`
   - the same with `de` and `RESULTS_visser698_stageA_de_v1.json`;
   - the same with `en` and `RESULTS_visser698_stageA_en_v1.json`.
   Each results file is hashed and stamped unread, as §8 says. On this workspace's two processors a language is expected to take about 50 minutes (four test solves on a made-up reading took 12 s).

## 16. Weaknesses known before the seal
1. **Reading v3 is not independent of v2.** The same reader made both and knew v2's labels, its remark on Spanish letter counts and the plan's remark on the split sign.
2. **Seventeen classes.** The made-up messages have 18 to 22. If two letters share a class in the reading, no one-to-one key reads the message whole, and the rehearsal does not model that.
3. **The count of signs.** The ledger's vetting text speaks of about 170 to 200 signs; the reading has 120. If signs were missed, stage A has next to no power: with one sign in ten missed the rehearsal found 1 key of 30.
4. **The sign `V`.** If it is in truth two signs, five places are each a letter short.
5. **The torn edge.** Signs may be lost at the ends of lines 5 and 6.
6. **The strip is torn.** Below 5 classes stage A cannot hit; below 7 stage B cannot pass.
7. **The word rule's shape, and its looser count, came from a hand that had the sources open.** That cannot make a wrong solution pass: the words were fixed by hash before any run, and the null solutions are counted the same way. It can mean that the rule was shaped to what exists.
8. **Stage B's statistic was changed twice on made-up trials,** and it tests the pairing with the Spanish table alone.
9. **The made-up messages are the model's own modern Spanish.** A real message of 1917 may hold names, abbreviations, code words and misspellings that they lack.
10. **The score bar passes on wrong keys** (§9, part 2). The strip rule carries stage A's decision, and it is weak when the strip is short.
11. **The word rule is still weak.** With one letter allowed wrong a right key found 6 of 16 long words on made-up data; two wrong signs in a word lose it.
12. **The order of the strip.** The desk cuts the tiles and keeps their order (§8 step 2). A tile still shows what its sign shows of where it stood: its slant on a tilted strip, the weight of its ink, any trace the cut leaves. The cover file's rectangles are in this chat's context. In the desk's words (its verdict of 18:00Z on 17 Nov): "They give where each sign's rectangle lies and, through the band the cover leaves at each place, roughly how tall each sign is. Set against the tiles' heights, that could place some tiles: in the desk's test, at most 8 of 27, with the offset chosen in hindsight. That it was not done rests on this chat's log."
13. **Whose language.** The catalogue says Kolbeck later claimed he wrote the message himself. This chat knows nothing of his language. Spanish first, then German and English, is J.'s ruling of 14 Nov and is not changed.
14. **The desk's judgment of which marks are signs.** The cover and the tiles rest on it. A sign the desk missed has no tile, and the match can say nothing of it; a mark taken for a sign may be none, and the match can say "no class". A cut that takes in part of a neighbour, or leaves out part of its own sign, would spoil a match.
15. **More of the desk's hand in an input.** The tiles are the desk's work. That each is the sign of its place and nothing else is checked only after the match, by running the desk's tile script on the frame this chat fetches.

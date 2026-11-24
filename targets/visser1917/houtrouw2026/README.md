# Catalogue 698: a sealed attempt, November 2026, and its miss

**This is the report of a failed attempt, sent at the maintainer's request (issue #542, 19 Nov 2026).** It offers no reading. The plan was sealed before anything was run, and the attempt missed:
- The best Spanish key passed its statistical bar, and the sheet's own key strip on frame 42 refused it.
- German and English did not pass their bars.
- The fallback with the strip could not pass, and did not.
- No word of the Bureau's 1917 reading was found by the sealed word rule.

The target folder and its class are WAINUT's, and this subfolder changes neither.

The work was done by Jacob Houtrouw with Claude (Anthropic). The model's words are in every file here; the rulings were his.

## The sealed plan and its timestamp
`plan/PREREG_visser698_v7M_2026-11-17.md`, SHA-256 `fc31c799649c3844c7a1581df06f3363828051c8d253eca980b5f02c32c1d73a`.
- **Sealed at 18:38:11 UTC on 17 Nov 2026,** by three RFC 3161 receipts beside it (FreeTSA, DigiCert and Sectigo, each at 18:38:11 GMT).
- **Every result below was made after it.**
- **One dated correction to it is beside it** (`plan/CORRECTION_plan_visser698_v7M_2026-11-17_2018Z.md`). It came on the audit's finding at 20:05 UTC, and it touches neither the design, the bars, the forecasts nor the runs.

## The three bars
Stage A solved the message blind, as a one-to-one substitution of its sign classes for letters, once in each language. The plan's §6 names the three hypotheses, and its §8 sets their bars. A message's p is (b + 1)/1,001, where b is the number of the 1,000 shuffled copies of the reading that score at least as well.

| Hypothesis | Language of the plaintext | Bar |
|---|---|---|
| H1 | Spanish | p ≤ 0.01 |
| H2 | German | p = 1/1,001 |
| H3 | English | p = 1/1,001 |

- **The chance that some language passes on score alone,** if the message is not language, is about 0.012.
- **A bar alone made no hit.** The key strip had to agree too (§8):
  - n is the number of the reading's sign classes that the strip gives, each with a single letter, its match and letter both sure;
  - k is the number of those classes on which the key agrees;
  - a hit needed n ≥ 5, k ≥ n/2, and k greater than that of every one of the 1,000 null solutions.
- **The fallback, stage B, had a bar of its own** (§10): p ≤ 1/1,001. It cannot pass with fewer than seven strip signs.
- **The word rule** (§10b) is a claim rule, not a way to a hit.

## The results
**Stage A, by language** (`results/RESULTS_visser698_stageA_*_v1.json`, stamped unread from 18:59:47 to 19:42:49 UTC on 17 Nov):

| Language | Score of the message | Null scores: min / median / max | Copies at or above | p | Bar | n | k | Hit |
|---|---|---|---|---|---|---|---|---|
| Spanish | −278,934 | −341,213 / −313,683 / −285,547 | 0 | 0.0010 | passed | 2 | 0 | no |
| German | −300,894 | −334,780 / −313,581 / −288,806 | 45 | 0.0460 | not passed | 2 | 0 | no |
| English | −284,205 | −322,264 / −302,753 / −283,636 | 2 | 0.0030 | not passed | 2 | 0 | no |

**The strip** (`results/STRIP_v1.json`, stamped 20:58:27 UTC) gives two classes with a sure match and a sure letter. They are class 4 = u and class X = x. The Spanish key has 4 = n and X = m, so k = 0 of 2. Below n = 5 no language could hit, whatever its score.
- **The match of the tiles to the classes** was made from the shapes alone, with the letters unseen (`results/STRIPMATCH_v1.json`, 20:17:52 UTC).
- **The strip's letters were read from the frame afterwards** (`results/STRIPLETTERS_v1.json`, 20:57:45 UTC): 9 sure, 14 doubtful and 4 not read.

**Stage B** (`results/RESULTS_visser698_stageB_letters.json`, 21:00:23 UTC): 2 strip signs, 2 re-pairings, p = 0.5. It could not pass.

**The word rule** (`results/BUREAU_visser698_*.json`, 01:06:03 UTC on 18 Nov). The file of the Bureau's words was fixed by its hash before the seal. It holds three forms of one word of eight letters or more.
- K = 0 in every language.
- K = 0 for every null solution.
- K = 0 in stage B.

So no agreement with the Bureau's reading is claimed.

**Forecasts** (§11; a calibration record, not evidence):
- **Eight are scored:**
  - mean Brier 0.18625;
  - 0.20393 over seven, if §8's "stage A has missed" is read narrowly, which drops stage B's conditional forecast.
- **Two misses at 0.50 or more,** printed at full weight:
  - "the strip gives five or more legible pairs" (0.75);
  - "seven or more classes surely matched" (0.50).
- **One is open:** that the Bureau's typed text is found on the roll.

The notes in `notes/` give each result with its weaknesses first, and the corrections stand beside the notes they correct.

## The blind readings
`blind_readings/`, each with its three receipts:

| Reading | Made from | Signs | SHA-256 | Stamped (UTC) |
|---|---|---|---|---|
| v1 | frame 39 | 121 signs, 45 doubtful | `cfc6acef461c…` | 14 Nov, 21:31:06 |
| v2 | frame 39 | 125 signs, 20 classes, 69 sure | `24d3f1ab3641…` | 14 Nov, 21:57:50 |
| v3, the input of the plan | frames 39 and 58 | 120 signs, 17 classes, 77 sure, 41 doubtful, 2 unread | `ddb270fbe48f…` | 16 Nov, 02:38:45 |

- **All three were made by shape alone,** before any letter value met the message and before frame 42 was seen.
- **v3 is not independent of v2:** one reader made both.
- **`blind_readings/strip_second_look/`** holds a later check. On 18 Nov a new chat, in a new and empty project, read the strip's 27 places blind, from views cut for it: the task sheet, its table as received with two receipts, and a recount. It agrees, sure, at 5 of the 9 places read sure the first time. It bears out class X's x and not class 4's u. The sealed result does not move.

## What the checking session saw of frame 42 before the solving session did
The question on #542 put it so on 17 Nov 2026, at 13:41:00 UTC (https://github.com/dbourdeau/cyphersolver/issues/542#issuecomment-6949722637):

> A separate checking session of mine has read the notes, to look for prior work, and has opened frame 42 to cover the strip's letters before the solving session sees it; it keeps what it has seen from the first.

The times follow.

**The work ran in two sessions:** one read and solved, and the other checked and kept the closed sources.

The checking session saw frame 42 first:
- It had read the ledger's notes on the message, from 15 Nov, to look for prior work.
- It fetched frame 42 at 04:36 UTC on 17 Nov and saw it whole, the strip's letters with it.
- From it, it made a cover file of 193 rectangles over the letters and 27 around the marks it judged may be signs.
- It cut those 27 marks into tiles, each on a plain ground, and numbered them in an order of its own.

The solving session saw it in four steps:
1. The cover file's rectangles, with no letter, from 05:33 UTC on 17 Nov.
2. The tiles, from 20:09 UTC. That was after its stage A results were stamped unread: the plan was sealed at 18:38:11, and the results were stamped from 18:59:47 to 19:42:49.
3. Frame 42 itself, from 20:45:09 UTC. That was after its match of the tiles to the reading's classes was stamped, at 20:17:52.
4. The strip's letters, read then from the frame.

The checking session kept what it had seen from the solving session from the first, and gave it only the hashes of what it held.

## Seen after the bars, and not evidence
- **A re-reading of both frames against the strip,** stamped 21:25:37 UTC on 17 Nov. It was made with the strip's letters, Spanish and the setting in view, and so is not blind. It decides nothing. It exists in the contributor's record and is not filed here, as a not-blind reading of a target WAINUT holds.
- **Its line 4 begins "abasteceran".** That is the word this target's `NOTES.md` gives as the one known word of the Bureau's 1917 reading, written by its writer with v for b.
- **No form of that word was in the solving session's record** before the re-reading's stamp, by its session logs.
- **Its line 8 agrees with "Horotwischka" at 9 of 13 signs.** The corrections say how much of that agreement was chosen.
- **Frames 30 to 70 of roll 302 were read page by page** for the Bureau's typed plaintext, and none was found. The rest of the case was not read.

## Did a reading already exist, and when was it found?
**Yes: the Bureau's of 1917, in Spanish.** By this target's `NOTES.md`, one word of it survives in print.
- **The solving session kept the target's notes and every source that might hold that reading closed** until the word rule's output was stamped (01:06 UTC on 18 Nov), and opened them then.
- **The checking session had read them from 15 Nov.** It made the file of the Bureau's words from them. The solving session knew that file only by its hash until 01:03 UTC on 18 Nov, when it was given the file to run the word rule.

## Weaknesses
1. **At n = 2 the strip could refuse a key but not confirm one.** The Spanish key fails on both pairs, but two pairs are a thin refusal.
2. **The strip went thin where the match and the letters met.**
   - Six tiles were matched sure, and three of them fell out on conflicts.
   - A fourth class has a doubtful letter.
   - The strip's letters were read once, at the frame's poor resolution, the doubtful ones partly by the order of the alphabet along the strip.
3. **A pass on the bar shows only that the message scores better than shuffled copies of itself.** The Spanish decode is strings with a Spanish look and no sentence.
4. **Every hand was a Claude session:** the readers, the solver's operator, the checking session and the blind second reader.
5. **The rehearsal on made-up messages had predicted a miss,** and the forecasts say so.

## Tools
Claude (Anthropic), in both sessions:
- **the solving session:** `claude-fable-5-2` to 03:54 UTC on 17 Nov, and `claude-opus-5-5` from 03:55 UTC;
- **the checking session:** `claude-fable-5-2` to 16 Nov, and `claude-opus-5-5` from 04:25 UTC on 17 Nov;
- **this report:** `claude-opus-5-5`.

The solver is the project's own simulated annealing over one-to-one keys, scored by four-letter models built with the ledger's `lang/lm.py`. The plan's §7 and §13 give the texts and the SHA-256 of every input and script.

**The images** are frames 39, 42 and 58 of NARA M1085 roll 302, case OG 2889, from NARA's online catalogue. The plan gives their addresses and hashes. None is committed here, and no conditions came with them.

## Files
- `plan/`: the sealed plan with its request and receipts, and its dated correction.
- `blind_readings/`: readings v1, v2 and v3 with their receipts; `strip_second_look/`, the blind second reading of the strip.
- `results/`: stage A's three results files, the strip files, the strip checks, stage B's and the word rule's outputs, each with its receipts.
- `notes/`: the notes on the match, the letters, stages A and B and the word rule, and their corrections. The not-blind re-reading and its corrections are not filed here.
- `timestamps/`: a manifest of this folder and its receipts.

Some names in the notes refer to the contributor's own record: "J." is the contributor, "the desk" the checking session, and "entry N" a step of his record chain, a hash-linked list of every reading, plan, run and ruling. The pull request gives the chain's head.

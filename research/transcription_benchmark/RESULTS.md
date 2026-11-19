# Transcription benchmark: results (17-19 Nov 2026)

How accurately can an AI read the digits of handwritten cipher pages, measured against a human transcription it never saw?

## What was run
- **4 documents, 3 independent blind passes each (12 runs), 5,581 reference digits.**
  dandini1580 R72 (Rome 1580, continuous digits), hellen1752 R1049 (The Hague 1752, dot-separated numbers, photographed
  sideways), santacroce1552 R6 and R7 (Vatican, 16th-century continuous digits).
- **Reference:** the DECODE manual transcription of the same record (D1824, D1890, D1624, D1625). One human reference
  per document. A second human transcription does not exist in the repository (the D3190, D3202, D3203 files are key
  tables), so the human-to-human ceiling is unmeasured.
- **Method:** page images rotated where sideways, cut into overlapping bands (`prep_tiles.py`), read by a separate
  Claude subagent per pass that was given only the tile images and told not to look at anything else. The scorer
  (`score.py`) strips both sides to digits and counts Levenshtein edits; `analyze.py` gives confusions and a consensus
  vote. The scorer was checked: identity scores 0, and 20 injected errors were recovered as 10 substitutions, 5
  insertions and 5 deletions. Raw transcriptions are in `runs/`, numbers in `scores.json` and `analysis.json`.

## Results (digit error rate; accuracy = 100% minus it)
| Document | Pass 1 | Pass 2 | Pass 3 | Consensus of 3 |
|---|---|---|---|---|
| dandini R72 (1,059 digits) | 4.3% | 4.7% | 4.3% | 3.9% |
| hellen R1049 (1,661) | 10.7% | 7.1% | 10.9% | 10.3% |
| santacroce R6 (1,540) | 3.3% | 5.1% | 3.4% | 2.7% |
| santacroce R7 (1,321) | 2.1% | 2.2% | 1.6% | 1.8% |
| **All four, pooled** | 5.4% (94.6%) | 4.9% (95.1%) | 5.4% (94.6%) | 5.0% (95.0%) |
| **Without hellen, pooled** | 3.1% (96.9%) | 4.0% (96.0%) | 3.0% (97.0%) | 2.7% (97.3%) |

Hellen, exact groups (dot-separated numbers): 60%, 82%, 74% by pass.

## What it shows
1. **Accuracy is about 97% on clear continuous-digit hands and about 90% on the hardest hand tested.** The 97% holds for
   three of the four documents. It does not hold for hellen, and it is a digit rate, not a rate of whole groups.
2. **Repeated attempts help only a little, and not where the errors are systematic.** The consensus vote improved
   dandini (4.4% to 3.9%) and santacroce R6 (3.9% to 2.7%), barely moved R7, and did not help hellen. Best-of-three is
   not usable in practice because nobody knows which pass is best without the reference.
3. **Hellen's errors are mostly one glyph.** 176 of the substitutions over the three passes are the reference 4 read as
   2 (about 59 per pass; hellen has 359 substitutions in total over the three passes, so about half). In this hand a 4 is written like an open "a". This is
   a systematic misreading, which is why voting cannot repair it. It is a hypothesis, not tested, that telling the
   reader the hand's convention would remove most of them. Santacroce's main confusion is 8 read as 4 or 6.
4. **Disagreement between passes predicts errors well.** Where the three passes disagree, the pass-1 character is wrong
   34% to 81% of the time; where they agree, 0.8% to 4.3%. Disagreement caught 48% to 58% of pass-1 errors. This is a
   cheap automatic flag for where a human should look.
5. **The reader's own "unsure" flags are not reliable.** In pass 1 it flagged every line; with a stricter
   instruction in passes 2 and 3 the flag counts varied from 2 to 28 lines per document. They were not scored.

## Limits (read before quoting any number)
- **This is not the frozen 41-document sample.** The frozen sample (`sample.json`) was drawn from a frame that turned out
  too loose: for many documents `reference_file` was only a length-measuring script and "images in the folder" were
  article figures. A clean pairing of a human transcription with page images of the same record exists for about ten
  documents; these four digit-cipher documents were the ones run. They are a convenience subset chosen after the
  audit, not a random draw. The frozen sample stays in the repository as committed.
- **Not run:** the letter and mixed-symbol documents (carpio1677, ferdinand3, r1873), hellen R1953, kauderbach R2078,
  the Pillon telegram, and the downstream solver test (key recovery from AI vs human transcription). None of these
  results says anything about letter ciphers or cleartext mixed with cipher.
- **One reference per document.** DECODE transcriptions carry their own errors and uncertainty marks (stripped here).
  The error rates are upper bounds on the AI's error where the reference is wrong, and unknown where it is right but
  the AI agrees with the same slip.
- **One model family.** The transcribers were Claude subagents; no other model was tested, and "the AI" in this report
  means that.
- **Tiling affects the result.** Insertions and deletions in dense pages partly reflect band overlaps and misses,
  not only misreading. Four documents, 5,581 digits: enough for the pattern, not for fine claims.
- **The Pillon pilot** (95.8% of groups exactly right, typed digit groups) is a different task and was not rerun.
- No expert checked these transcriptions.

## Files
`PLAN.md`, `inventory.py`, `sample.py`, `audit_pairs.py`, `prep_tiles.py`, `score.py`, `analyze.py`, `runs/`,
`scores.json`, `analysis.json`, `frame.json`, `sample.json`.

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

## Second round: letter and mixed documents (19 Nov 2026)
Four documents whose cipher mixes letters with numbers: carpio1677 R1009 and R1010 (Spanish, 1677, a scan of a
letter with small crossed numbers and letter pairs) and ferdinand3 R1889 and R1890 (Latin, 1635 and 1640, photographs,
cipher lines between prose lines). Same method: three blind passes, scored against the DECODE transcription (D2422,
D2421, D3605, D3604) on the lower-cased letter-and-digit stream; DECODE's cross marks ('+') and separators are not
compared. Only the cipher lines were to be read; the prose was to be skipped.

| Document | Pass 1 | Pass 2 | Pass 3 | Consensus of 3 |
|---|---|---|---|---|
| carpio R1009 (798 signs) | 17.7% | 17.8% | 18.7% | 18.1% |
| carpio R1010 (609) | 15.9% | 16.4% | 16.9% | 15.4% |
| ferdinand R1889 (684) | 3.7% | 2.9% | 2.9% | 2.9% |
| ferdinand R1890 (1,443) | 2.3% | 3.0% | 2.7% | 2.5% |
| **carpio, pooled** | 16.9% | 17.2% | 17.9% | 16.9% |
| **ferdinand, pooled** | 2.7% | 3.0% | 2.8% | 2.6% |

1. **Letters are not harder as such: the hand and the sign set decide.** Ferdinand, with letters and two-digit numbers
   in a clear, upright italic hand, reads at about 97%. Carpio, at about 83%, is the worst result in the benchmark.
2. **Carpio's errors are systematic and have two visible sources.** A crossed 1 is read as a 4 (62 times over the three
   passes); the letters b and o are read as the digits 6 and 0 (47 and 50 times); and, as in the hellen hand, a 4 is read as
   a 2 (82 times). About a third of carpio's substitutions swap a letter for a digit or the reverse. Ferdinand has
   fewer swaps (0 and o, 9 and g, 1 and i, b and 6).
3. **Voting does nothing for systematic errors.** The consensus is about equal to the single passes on carpio, and the
   passes agree on their mistakes: disagreement flags only 19% to 24% of carpio's pass-1 errors, against 48% to 58%
   on the digit documents, and 19% to 64% on ferdinand. Where all three passes agree on carpio, the error rate is still
   about 11% to 13%. Disagreement finds random misreadings, not a consistent misreading of a glyph.
4. **The comparison is convention-dependent here.** The DECODE reference records crossed numbers with '+' and writes
   letter pairs separated by dots; the reader was told to ignore crosses. A convention mismatch may inflate carpio's
   rate; it cannot explain a crossed 1 read as 4, which is a different digit.
5. **Process notes.** The first ferdinand attempt used pages cut at the wrong rotation (90 degrees, upside down; the
   transcriber rotated its own copies and returned reversed lines); it was discarded and all three ferdinand passes
   were redone on pages cut at 270 degrees. The other session's guess of 90 degrees in `prep_tiles.py` was wrong for
   ferdinand and was corrected there. R1889 page 2 is mostly show-through, so only 3 cipher lines were read on it.

## Extension and replication (a second session of this project, 19 Nov 2026)
A forked session transcribed the six documents that had been prepared but not run in the first round: hellen R1953
and kauderbach R2078 (digits), and its own three passes each of carpio R1009 and R1010 and ferdinand R1889 and
R1890. Its 30 raw pass files are in `passes/` (the 12 passes on dandini, hellen R1049 and santacroce are identical to
those in `runs/`). These numbers were re-scored here from the raw files and reproduce (`scores.json` and
`analysis.json` now hold all 30 passes).

| Document | Digit/sign error, three passes | Note |
|---|---|---|
| hellen R1953 (2,858 digits) | 1.4%, 1.5%, 1.5% | 94% to 95% of dot-separated groups exact |
| kauderbach R2078 (2,522) | 4.0%, 3.7%, 4.4% | dense continuous digits, photographed sideways |
| carpio R1009, second set of passes | 17.9%, 17.9%, 18.2% | mine: 17.7%, 17.8%, 18.7% |
| carpio R1010, second set | 14.0%, 15.9%, 17.9% | mine: 15.9%, 16.4%, 16.9% |
| ferdinand R1889, second set | 3.5%, 3.5%, 2.5% | mine: 3.7%, 2.9%, 2.9% |
| ferdinand R1890, second set | 3.2%, 2.9%, 3.0% | mine: 2.3%, 3.0%, 2.7% |

- **The letter results replicate.** Two independent sets of three passes land within about two points of each other on
  carpio and one point on ferdinand, so the carpio-versus-ferdinand gap is not noise from one run.
- **All 30 passes pooled: 5.1% error (94.9% accuracy);** digit-only documents (18 runs) 4.0%, alphanumeric documents
  (12 runs) 8.7%.
- **Accuracy varies widely inside one correspondence.** Hellen R1953 reads at about 98.5% while hellen R1049, from the
  same target, reads at 89% to 93%; the 4-read-as-2 confusion that dominated R1049 does not dominate R1953. The cause is
  not established here (page images, photographing, hand, or number layout are all untested explanations).
- The top confusions over all 30 passes are 4 read as 2 (269), a crossed 1 read as 4 (89), 8 read as 0 (72), o read as 0
  (51), 4 read as 9 (50) and b read as 6 (49).

## Limits (read before quoting any number)
- **This is not the frozen 41-document sample.** The frozen sample (`sample.json`) was drawn from a frame that turned out
  too loose: for many documents `reference_file` was only a length-measuring script and "images in the folder" were
  article figures. A clean pairing of a human transcription with page images of the same record exists for about ten
  documents; these four digit-cipher documents were the ones run. They are a convenience subset chosen after the
  audit, not a random draw. The frozen sample stays in the repository as committed.
- **Not run:** r1873, the Pillon telegram, and the downstream solver test (key recovery from AI vs human
  transcription). The letter pairs (carpio, ferdinand) and the two further digit documents (hellen R1953, kauderbach
  R2078) are reported in the next two sections; that is ten documents from at least six hands in all.
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
`scores.json`, `analysis.json`, `frame.json`, `sample.json`; second round: `runs_letters/`, `scores_letters.json`,
`analysis_letters.json`.

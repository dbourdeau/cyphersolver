# METHOD: Batavia letter of 23 Jan 1643 (inv. 1141, copy 2 scans 901, 902, 905) with KEY_v2. Written and frozen BEFORE transcription and decode.

## Exposure, disclosed before the freeze
- The selection step (blindtest/SELECTION.txt) saw masked HTR context of inv. 1141 with some HTR letter strings of the letter-cipher words.
- GM II heading only, seen 25 Nov about 21:07 UTC while identifying the letter: p. 194, "Batavia 23 januari 1643. 1050, ongefolieerd (na fol. 383),
  copie fol. 384-389. (Brief verzonden met de Engelse Ulysses; samenvatting der 3 voorafgaande ...". The body of GM II pp. 194-195 not read.
- Half-size previews of 1141_0901, 0902, 0905 viewed (about 21:07-21:08 UTC). On 0901 the clear text is legible: a Tonkin/Quinam passage
  (war of Tonkin with Quinam, trade in Tonkin, Japan, Siam, Cambodia, Tonkin, 'Tonnen'). I recognised from memory the KEY_v2 values of the
  first two or three numbers of the first 0901 run (I have KEY_v2 in context). No run was decoded on paper or by script.
- Glossed copy 1 (1141_0886, 0890) NOT viewed at legible size. It is a control, opened only after the score is fixed.

## Transcription convention (T1643.txt)
- One line per manuscript line: `<scan>.<line> | content`.
- Number groups as read, separated by single spaces (the scribe's '/', '.', ':' between numbers are all written as a space).
- A comma or other stop written by the scribe after a number is kept as ' , '.
- Clear words in [ ]. Letter-cipher words (letters, not numbers, e.g. 'ulcdbbe') in < >. Neither is decoded with KEY_v2.
- Illegible group = 0. Doubtful readings noted in a `# doubt:` line, the first reading kept.

## Word-division rule (frozen; the copy writes '/' between every number, so the key's '/' word divider is unavailable)
- A RUN is a maximal sequence of number groups not interrupted by a [clear word], a <letter-cipher word> or a comma. Line ends do not interrupt.
- Each number decodes to one letter with KEY_v2 (first value: i/j -> i, u/v/w -> u). Number not in KEY_v2 -> '?'.
- Each run is segmented by dynamic programming into pieces:
  * a piece of 3+ groups is a WORD if it has no '?' and score.norm(piece) is in W (trackB score.py wordlist(): 37,386 types, freq >= 2);
  * a piece of 2 groups is a WORD only if norm(piece) is in S2 = {en, de, te, in, op, is, al, of, na, om, ia, er, so, ie, uw, nu};
  * a piece of 1 group is never a word;
  * maximise groups covered by WORD pieces; ties: fewest pieces, then leftmost-longest.
- FIGURE OF RECORD: covered groups / all groups in runs, whole letter and per page. Read bar: >= 65%, strict.
- Also reported: runs fully covered / all runs; coverage (groups keyed / all groups); unkeyed numbers.

## Controls
1. Key shuffle: 5,000 keys at seed 20261112 and 5,000 at seed 7, each a random permutation of KEY_v2 values over its 60 numbers;
   same runs, same DP. Count shuffles >= real; max; mean.
2. Matched control (shuffled ciphertext, Martin 1696 lesson): 5,000 at each seed; all number groups of the letter permuted at random
   across positions (run lengths and positions kept), decoded with the real KEY_v2, same DP. Count >= real; rank of the real score.
3. After the score: glossed copy 1 (1141_0886, 0890) read as a check of the decode. Nothing changes the figure of record.

## Run
scripts/run_1643.py, once, with python3 -I. Output run_1643_output.txt and decode_1643_firstpass.tsv.

## Addendum before the freeze (dry run of the code on known text, 25 Nov about 21:08 UTC)
- scripts/run_1643.py was dry-run on the already-read 1640 postscript with its '/' removed (test/T_test1640.txt; test only).
  It gave 54/57 = 94.74%, key shuffle mean 35.5% (max 77.2%), ciphertext shuffle mean 55.4% (max 80.7%).
- So the DP letter coverage is generous: random text can pass 65%. PASS therefore needs ALL of:
  (a) figure of record >= 65%; (b) 0/5,000 key shuffles >= real at both seeds; (c) 0/5,000 ciphertext shuffles >= real at both seeds.
  The 65% bar alone is not treated as evidence.

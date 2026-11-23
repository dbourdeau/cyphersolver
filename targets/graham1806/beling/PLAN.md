# Plan: Graham's 2 Jan 1806 letter against Weber's code tables

This plan was written on 22 Nov 2026 for the rerun. **The first run (11 Nov 2026) had no plan or pass mark filed
before it.** What was fixed beforehand that day is listed below; everything else is a measurement, not a
pre-registered pass. The rerun changes only the random seeds (one seed per table and per test, so that a reader's
figures do not depend on which other tables their file holds). The scorer's rules are unchanged.

## What was fixed before any table was opened (11 Nov)

- The transcription of frames 0006-0009. Frames 0010-0011 were read after about 40 groups had been looked up in WE023.
  Groups re-read after a lookup carry `?` and are excluded.
- The unit: a span of groups under one word of Wagner's. A span is usable if it has a word, no doubtful or unreadable
  group, and no group of 1594 or above (WE023 ends at 1593).

## Measures

1. **Table test.** For each table and each usable span, look up the table's element at each number and join them.
   - Strict: the result equals Wagner's word. If Graham put a caret on the span, -s, -es, -ed, -d, -e, -n or -en may be
     added.
   - Lenient: the result is within one letter (edit distance 1).
   - Controls: 200 shuffles of each table's values over its own numbers.
   - Reported: strict, lenient, the highest shuffled strict and lenient, the mean shuffled lenient.
2. **Held-out test, no table.**
   - Build a key from single groups under one word on frames 0006-0008, using the most frequent word.
   - Count how many single groups it covers on 0009-0011, and how many it gives Wagner's word for. Then do the reverse.
   - Controls: 200 permutations of the key's values.
3. **Table choice held out.** Rank the tables by lenient score on 0006-0008 and report the winner's score on 0009-0011.
4. **The [22 Nov] 1806 extract.**
   - The 18 numbers the editors could not read or only conjectured: 10 19 30 33 35 36 39 41 51 61 65 77, and 18 46 54
     67 71 73.
   - Does the January key give any of them? How many January groups are 77 or below?
   - What is the chance that 18 distinct numbers drawn evenly from 1-1593 all fall at 77 or below?

## What would count against "the 2 Jan letter is in WE023"

If WE023's strict score were within the range of its shuffled controls, or if another table scored as well, the letter
would not be shown to be in WE023. No numeric pass mark was set in advance. The result is reported against the
controls as it stands.

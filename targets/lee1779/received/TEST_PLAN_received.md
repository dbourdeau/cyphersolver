# Test plan: our reading against the interlined decipherment on the received copies

Written 14 November 2026 before any image of the received copies was opened by this worker (the claims reviewer
had looked at them earlier and reported one disagreement, 243,a,XVII; that is known going in). Hashes of our key
table, reading table, code-group lists, transcription and letter files at that moment: `FREEZE_received.txt`
(branch `lee1779-beling`, commit 431ad082d). None of those files is changed before the score is run.

## What is compared
- Letters 2 (22 April 1779), 3 (27 April 1779) and 4 (the letter-book entry before 9 May; received copy dated
  21 May 1779): 16 + 23 + 56 = 95 code groups in `decoding.tsv`.
- For every one of the 95 groups: our frozen reading (column `reading`, with its grade) against the word written
  above the group on the received copy (Lee Family Papers, University of Virginia, 1966 microfilm, roll 6,
  Internet Archive `per_lee-family-papers_the-lee-family-papers_1742-1795_6`, images n73-75, n109-111, n203-209).
- Groups are matched by their place in the letter (the sentence they stand in), not by number, so that a group
  written differently on the received copy is still compared with the letter-book group it stands for.
- Every difference between the group as written in the letter book and the group as written on the received copy
  (page, column, entry, ending mark) is recorded separately.

## Scoring (one run, reported whatever it shows)
Each of the 95 groups gets exactly one score:
1. **same word**: the interlined word is our word (spelling and capitals ignored).
2. **same word, different inflection**: same headword, different ending (named/name, troops/troop, -ed, -s, -ing),
   or an abbreviation that can only be our word.
3. **different word**: the interlining gives another word (including a partial word such as "c - h -" that does not
   fit ours, and "X (Y?)" where neither X nor Y is our word). A partial or alternative interlining that includes our
   word counts as 2 if it is our headword in another form, otherwise it is listed as "partial, consistent" under 4.
4. **interlining absent or illegible**: nothing written above the group, only letters too few to decide, or not
   legible on the microfilm image; also groups missing from the received copy.

Agreement is reported as (1+2) of those scored 1-3, and also of all 95, per letter and overall. Our firm groups
and our doubtful and unread groups are reported separately. For our 16 doubtful and 5 unread groups (those that fall
in letters 2-4, and for any in letters 1, 5, 6 if their received copies are found), the interlined word is listed
whatever its score.

## What would count against our reading
More than a handful of "different word" scores on groups we call firm, or any pattern (one page, one column, one
offset) in the disagreements. Agreement does not make the two readings independent of the dictionary: both may come
from the same book; agreement shows the counting rule and edition give the same words as the older decipherer's.

## Afterwards
Only after the score is fixed may grades be changed, and every change is listed with its reason. Readings of
doubtful or unread groups taken from the interlining are marked as such (help from a period or later decipherment
is not independent).

# barlow1812: the key (`key.tsv`)

The Paris legation code of 1811-1813: a numerical code of words and syllables, numbers from 7 to 1700, with "the" at 1700.
No code book or key sheet is known. The table here is rebuilt from ten letters in the same code that were deciphered
at the time. It holds **644 numbers, 623 of them with a value**; if the code had about 1,700 entries, that is
under two fifths of it.

## Where the values come from

| Short name in `key.tsv` | Letter | Where | Decipherment |
|---|---|---|---|
| B1811 | Joel Barlow to Monroe, Paris, 29 Sep 1811 | NARA M34 roll 16 frame 11 | a separate decipherment by the State Department, frames 15-16 (printed in Manning, *Diplomatic Correspondence ... Latin-American Nations*, 2:1372-73) |
| Mon-Apr | Monroe to Barlow, 23 Apr 1812, last page | Sotheby's sale N08864 (2012) lot 39, photograph | between the lines, hand of the time |
| Mon-Jun | Monroe to Barlow, 16 Jun 1812 | Library of Congress, Monroe Papers, series 4 (item mss33217018, images 8-12) | between the lines, hand of the time; printed decoded in *The Papers of James Monroe* 6:200-201 |
| Mad-Aug | Madison to Barlow, 11 Aug 1812 | Library of Congress, Madison Papers (series 1, images 423-424 of reel 14) | between the lines |
| B-Sep26 | Barlow to Madison, 26 Sep 1812 | Library of Congress, Madison Papers (images 607-612 of reel 14) | between the lines, by Madison (so *The Papers of James Madison*, Presidential Series 5:354-57) |
| D19, D20 | Barlow's despatches 19 and 20, 20 and 25 Oct 1812 | M34 roll 16 frames 242, 244 | State Department clerk, between the lines |
| Wilna | Barlow to Monroe, Wilna, 23 Nov 1812 | M34 roll 16 frames 249-250 | clerk, between the lines |
| TB-Feb | Thomas Barlow to Monroe, 10 Feb 1813 | M34 roll 16 frames 291-293 | clerk, between the lines (frames 291 and 293 are poor film) |
| TB-dup | Thomas Barlow, "Duplicate", 1813 | M34 roll 16 frame 295 | clerk, between the lines |

Every value in `key.tsv` is one that a decipherer of 1811-1813 wrote, or that follows from a word he wrote. None of
our own guesses is in it; those are in `proposals.tsv` and are marked `?` wherever they are used.

## Columns and grades

`number`, `value`, `grade`, `occurrences`, `witnesses` (the short names above), `other_values` (other values seen for
the same number, with their grade and count). `key_evidence.tsv` lists every occurrence behind every number.

| Grade | Meaning | Numbers |
|---|---|---|
| P | the decipherer wrote this value above this number alone (the four letters outside M34) | 386 |
| C | the State Department clerk's writing between the lines on the M34 frames; where he wrote one word over several numbers, the division is ours | 123 |
| D | aligned with the separate decipherment of the 29 Sep 1811 despatch; the division of each word is ours | 59 |
| W | the number stands in a word a decipherer wrote over several numbers; the value is what is left when the known neighbours are taken away | 41 |
| L | doubtful occurrences only (poor film, a blot, or a number the blind readers did not confirm) | 14 |
| in-word | seen only inside a word whose division we could not make | 21 |

## How it was checked

- Every source was read twice more on 21 Nov 2026 by AI readers who saw only the images (two per source), and each
  number on which both differed from the first transcription was looked at again on the image. Of 3,297 numbers
  compared, 56 had been misread and were corrected, and 22 doubtful occurrences were set aside (14 numbers are
  left with doubtful occurrences only, grade L).
- 290 of the 623 values rest on a single occurrence. A value seen once can be wrong.
- I and J are one letter in this code, and so are U and V (1125 serves for "iv" and "ju", 1651 for "ued" and "ved").
- Known open conflicts: 862 is "army" (TB-dup) and "same" (Mon-Jun); 183 is "soon" (Mon-Jun) and stands in "persons"
  (B-Sep26); 133 is "ti" and "ty"; 939 was deciphered "11th" and "fifth" by Madison in the same letter (B-Sep26).

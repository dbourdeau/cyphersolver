# James Lovell's solution of the 16 March 1782 letter, April 1782 (added 14 Nov 2026)

Papers of the Continental Congress, item 51 vol. 2, catalog images 185-186 of the volume file (naId 475671370; NARA
files 408452 and 408455), the same volume as the cipher at p. 227. The images were found by our PCC paging sweep of
14 Nov 2026. They were read for this note on 14 Nov 2026 by our AI agent (Andrew Beling, with AI agents), at 2600
pixels from the catalog's image server. Hashes are in `sources.json`; the images are not in the repository.

## What the two images are

- **Image 185, p. 221: a letter signed "James Lovell"** to "Honble R R Livingston" (Robert R. Livingston, Secretary for
  Foreign Affairs). It is dated from the ironworks near Ringwood ("... Iron Works, at ...", place name partly
  illegible) "in a Storm April 19. 82". Lovell writes that the contents of the ciphered paper, which he copied by
  favour of "the Gentleman at Mrs House's", turn out to be of little importance. He adds that the writer's names may
  be found later, and that he conjectures the surname to be "F—". He points out the "regularity of sense in the
  Alphabets when placed by the Columns of Numbers from 1 upwards", which will help with "any more Papers cyphered by
  the same Party". He ends: "See my Supplements to the first Column. I made a few to [circled] 8 which makes that
  Column compleat."
- **Image 186, two leaves:**
  - p. 225 (filmed sideways) is **his table of the key**: columns headed by circled numbers 1-18 (the lines), each
    listing place and letter (`lovell_table.tsv`). Column 1 has small marginal additions, the "supplements" his
    letter mentions.
  - p. 223 is **his clear text** of the letter, headed "dupl:", ending "Sorel March sixteenth". The signature is left
    in figures, "6-11 11-1".

## Whose hand

- p. 221 is signed by Lovell.
- p. 223 and the figures of p. 225 are in the same hand as p. 221. We compared letter forms: the looped capital P
  (Papers, Pleasure), the R (Reports, Routes), the long s, and the joined "y" and "f". This is our judgement from
  two images, not an expert identification.
- The covering letter speaks of "my Labors" and "my Supplements", which places the table and the solution with him.

## What the table is

It is a **reconstruction of the Army List title-page alphabet from the cipher alone**: a period cryptanalysis.

- **How he worked.** He did not know the page (as far as these sheets show). He built the 18 lines the letter uses
  from the dotted line-and-place numbers. Where a run of cells spelled a phrase, he wrote out a whole line: line 1
  "By Permission of the Right Honourable", all 32 letters; line 18 "And the Marines on Full and Half Pay", 24 of 29.
- **His guessed wordings.** For line 16 he wrote a different but plausible wording of the same length: "whether a
  Regiment of Artillery or a Corps of Engineers" against the true "The Royal Regiment of Artillery, and Corps of
  Engineers".
- **Cell by cell against our key** (`compare.py`, `comparison.tsv`):
  - He gave a letter for 168 cells; 147 agree with our key and 21 differ.
  - Of the 137 cells the letter uses, he lettered 134; 118 agree and 16 differ.
  - He has no letter for **6.11 and 11.1, the signature** (hence his "F—" and the figures left on p. 223), nor for
    15.14.
- **The differences fall into two kinds.**
  - The differences that produce his two wrong words: 12.3-5 read as "any" for *the*, and 13.17-21 read as "other"
    for *least*; 14.5, 14.21 and 15.4 read for "would" against *will*.
  - Cells where his table differs but his decipherment is right, filled from sense: 16.4, 16.5 and 16.7 belong to
    his line-16 wording, while his text has *received*, *common*, *a*. The same holds for 13.21 and 16.29 in
    *intelligence*, 14.9 in *sixteenth*, and 9.5 in *directly* (o or c in his hand).

## How it relates to the translation on vol. 1 p. 738

- **The text.** p. 738 is the same text as Lovell's p. 223, with the same errors: "any other" for *the least* and
  "would" for *will*. It adds the guessed signature "(perhaps) A. F.", which follows from his conjecture "F—". It
  depends on Lovell's solution, not on a separate attempt.
- **The hand.** p. 738 is written across the back of a cipher sheet, faster and smaller than p. 223. We do not
  identify its hand; it may be Lovell's rough copy or a clerk's copy of his reading.
- **What this changes.** Our earlier wording, "a decipherer working without the key", stands. The decipherer is now
  identified as **James Lovell**, by April 1782, who rebuilt the key line by line from this one letter.

## Credit

The first reader of the 16 March 1782 cipher outside British headquarters was James Lovell, delegate for
Massachusetts and the Continental Congress's cryptanalyst. He broke it from the intercepted copy by analysis in
April 1782, with two word-level errors and the signature unread. Our decode reproduces his text, and our key confirms
147 of the 168 cells he lettered. Ours was made without knowledge of his sheets: the PCC sweep found them on 14 Nov,
after our 13 Nov work.

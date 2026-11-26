# K24.37 recto, blind reading 3 (STOPPED EARLY)

Stopped on the coordinator's instruction. The comparison step was not done and no earlier reading was opened.

## What is done
- Pass 1 (image windows 1.3k px wide at 1.5x, background-flattened + CLAHE): **all 8 lines**, right to left. Files: `signs.tsv` (218 marks), `transcription.txt`, `legend.txt`, `doubts.txt`, `stats.txt`.
- Pass 2 (independent re-read, different windowing): **only L1 and L2 finished**, and they agreed with pass 1 on sign order and classes. Differences: FLG at the start of L1 includes its tail (4962-5090) rather than a separate dash; the L2 bracket-with-detached-bottom-bar at x~2190 is better read as a GAMD (top bar + stem + inner dash), as in L3. L3 pass 2 was viewed but not recorded. L4-L8 have no pass 2. Pass 2 notes are not in the files below; signs.tsv and transcription.txt are pass 1 only.
- Not done: reconciliation at 3-4x, contact sheet (classes are unmerged provisional shape labels, e.g. V+f1 / V+f2 / V+f3 are bar with short / long flat / long curved left foot and may merge), shuffle comparison, consensus.

## Method
Image fetched from CUDL IIIF (MS-TS-K-00024-00037-000-00001.jp2) in 1800-px regions, stitched to 5673 x 6438. Skew measured by maximising the sharpness of the ink row-projection: lines rise **2.2 degrees** to the right; rotated clockwise by 2.2 degrees (frame rule then level). x-centres in signs.tsv are in this deskewed image, native pixels. Lines at about y = 530, 1230, 2010, 2230, 2430, 3360, 4310, 5300.

## Extents (x, deskewed px; sign count includes dividers and doubtful marks)
L1 1925-5040 (26), L2 1720-3785 (22), L3 1880-5017 (32), L4 1950-4900 (32), L5 1833-4935 (29), L6 1750-4865 (26, hole at 2513-2813), L7 1880-4860 (25, tear at 2780-2840), L8 2410-4815 (26, line empty left of ~2360). L5-L8 end at the frame rule (vertical rule at x about 4930-4960; L8 sits above the bottom rule). `python docs/_check_profile.py --measure transcription.txt`: 226 tokens, 89 distinct (incl. "?" variants), IC 0.025 on raw tokens. Excluding dividers/blobs: 143 signs, 57 labels, normalised IC 1.75 (unmerged labels, so inflated inventory).

## Direction
Right to left (moderate confidence): lines 1 and 5-8 begin flush against the paper edge or frame rule on the right and thin out ragged on the left; the "dash + bar with left foot" pairing recurs with the dash on the left of the bar; heavy foot strokes point left. No shuffle test was run.

## Quality
L5-L8 and the left halves of L1-L3 are well preserved. L3 right half, L4 and L8 are faint and fragmentary: many marks graded doubtful (see doubts.txt). Images are in the scratchpad, not committed.

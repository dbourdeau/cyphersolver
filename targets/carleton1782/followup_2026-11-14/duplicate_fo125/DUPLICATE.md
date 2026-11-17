# B.148 pp. 126-128: the second cipher of 25 September 1782 (post-test, 14 Nov 2026)

Read 14 Nov 2026 by our AI agent (Andrew Beling, with AI agents) on full-resolution Canadiana IIIF crops of H-1649
frames 1207-1210 (hashes in `sources.json`). Everything here was done after the 12 Nov test; the frozen files are
unchanged.

## What the pages are

Not a rearranged copy made by the clerk, and not the clerk's working copy: a transcript of a **second original cipher
letter**, BL Add MS 21808 **fo. 125**, while pp. 123-125 transcribe **fo. 124**.

- p. 123 margin: "fo. 124" and "(See another copy (differently arranged) on pp. 126-8 infra. For decoded copy see
  p. 102 supra; also B.146, p. 54.)". p. 125 foot: "Cypher Signed." and "fo. 124v blank".
- p. 126 margin: "fo. 125" and the matching note "(See another copy differently arranged on pp. 123-5 supra. ...)".
  p. 128: the clear naval sentence, "Guy Carleton/" and the copyist's "Cypher L.S." (letter signed); foot "fo. 125v
  Endorsed: Rd Oct. 26 -82".
- So Carleton's office enciphered the letter twice, each copy signed, packed in different columns (fo. 124: six
  columns; fo. 125: seven), and both reached Quebec. Only fo. 125 carries the receipt endorsement of 26 October, the
  date of the express (B.146 p. 54, "Recd by Express 26th Octr"). Whether fo. 124 came by the same express or by
  another route is not stated on the transcript [not established].

## Collation (`collate.py`, `collation.tsv`)

Both witnesses reduced to number pairs and clear words: 432 tokens in fo. 124 (our post-test transcription), 428 in
fo. 125; 424 align exactly. The differences, each checked on the images:

| place | fo. 124 (pp. 123-125) | fo. 125 (pp. 126-128) | what it shows |
|---|---|---|---|
| head of column 1 | 3-4 | absent | the heading 3-4 (duplicate) is on fo. 124 only, so fo. 124 is the copy marked as the duplicate |
| Susquehannah, 4th letter | 26-9 (n) | 26-8 (u) | see q below |
| before *assemble* (unit 96) | **17-22 on the image**, missing from our transcription | 17-22 | *will*: our transcription of p. 123 column 3 dropped it (between 4-3 and x23-2, checked on frame 1205); the clear copies' "will assemble" is in the cipher |
| *force* | 9-2 9-1 9-7 9-5 9-6 | 9-2, three rows left blank, 9-6 | the copyist of fo. 125 left space for three figures he did not write [cause not established] |
| *Orders* | 5-14 | 8-14 | one copy has a digit slip; the letter structure (o, column 14) fits both; not settled |
| after column 5 | "Cypher Signed." | "Cypher L.S." | copyist's notes, not cipher |
| naval sentence | after the date | after *Boston* (end of column 6) | placement only |

## What it settles

- **The three failed predictions.** 22-19 (*thence*, clear *there*), 43-19 (*thousand*) and 9-8 (*has*, clear *have*)
  stand identically in both 1782 cipher copies. None is a slip of one copy or of the Canadian copyist. 9-8 is in the
  h column of the code sheet and 4-8 is *have* (Clinton), so the cipher says *has* and the clear copies' *have* is the
  decipherer's grammar; 22-19 is a t-word in both readings and stays open; 43-19 was our own error (already corrected).
  A third clear copy found for gap 2 (Q series vol. 20 p. 384) also reads "from there", "One thousand" and "have
  contributed".
- **The spelled groups that did not match.**
  - *susnuehannah* / *reuuire*: in *require* both copies write the q with the u cell (26-8 26-8), and fo. 125 does the
    same in *Susquehannah* (26-8 26-8). The title page has no q; this encoder wrote q with the cell for u. fo. 124's
    26-9 is then a one-digit slip (8 to 9) in that copy. Both groups are explained; neither is an error of the key.
  - *incuosions*: both copies have 26-12 (o) where *r* is 26-13 on line 26. The slip is common to both 1782 copies, so
    it was made by the encoder (or in a common draft), not by a copyist; one figure off.
  - *escaped* (seven pairs) and the split groups *assembl+y*, *repairin+g* are the same in both copies.
- **The cipher's repeated "to Pines Creek"** (units 66-68) is in both 1782 copies, so it is the encoder's repetition,
  not a copying error at Quebec or in the 1880s. None of the three clear copies has it.
- **The 56 code occurrences the table did not cover.** fo. 125 gives the same figures for all 56 except *Orders* (5-14 /
  8-14). It adds no reading (it is a cipher, not a decode), but it confirms the transcription of those 56 occurrences,
  one digit apart.
- **Post-hoc, not added to the score:** had the frozen transcription carried 17-22 at unit 96, the frozen Clinton table
  (17-22 *will*, unqualified) would have predicted *will*, which the clear copies have. The 55 of 58 stands as frozen.

## Files

- `transcription_fo125.txt`: full transcription of pp. 126-128, column by column, dittos written out.
- `collate.py`, `collation.tsv`: the mechanical collation against `../../carleton_1782-09-25/transcription.txt`.
- `sources.json`: the IIIF addresses and hashes of the crops read.

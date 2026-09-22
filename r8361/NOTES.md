# R8361 — BL Harley MS 260 ff. 367r–369v (Walsingham letter-book, November 1572)

Status: attempted, open (catalogue 125). Cipher content is a handful of name codes and one short
letter run; no key survives and the run is too short to break. Letters themselves are clear and in print.

## What the record is

DECODE R8361 ("BL_Harley_MS_260_367", "Unknown sender to unknown recipient", Nov 1572, 6 pp., "Short parts
encrypted only") is six images of a later fair-copy **letter-book of Sir Francis Walsingham's Paris embassy**
(running head "November 1572"). The images are, in page order:

| image | folio | content |
|---|---|---|
| P1 | 367r | end of Leicester → Walsingham (Nov 1572); Burghley → Walsingham, Westminster 7 Nov 1572 (begins) |
| P2 | 367v | Burghley ends; Walsingham → Sir Thomas Smith, Paris 27 Nov 1572 (begins) |
| P3 | 368r | Walsingham → Smith continues |
| P4 | 368v | Walsingham → Smith ends ("At Paris the xxvij of November 1572"); Walsingham → Burghley (begins) |
| P6 | 369r | Walsingham → Burghley continues |
| P5 | 369v | Walsingham → Burghley ends (Paris, 27 Nov 1572); Walsingham → Smith (5 Dec 1572, begins) |

DECODE images P5 and P6 are in reverse folio order.

All four letters are printed in Dudley Digges, *The Compleat Ambassador* (London 1655), pp. 297–301
(`burghley1572/lit/digges1655.txt` lines ~23300–23480 in the shared checkout). Digges prints the cipher
passages as garbled figures ("vI9T#tw516p I 6", "[5]", "3", "H") without deciphering them. CSP Foreign vol. 10
(Nov 1572, BHO pp. 200–210) does not calendar these letters. So the letters were known; the cipher was not read.

## The cipher passages (transcription from the scans)

Burghley → Walsingham, 7 Nov 1572 (f. 367r):
- "a person come, as he saith, from Florence **[9]**" (boxed 9)
- "letters which the partie hath written to Rome **[9]**"
- "The partie (L^ds) **776 + w5 ‡ 6 3 ∩ 6** remaineth here in London as in a …, and yet I doubt the P. will smell of him" — a letter-cipher run of about nine signs, probably a name.

Walsingham → Burghley, 27 Nov 1572 (ff. 368v–369v):
- "delivered to Steward, for that Glasgow **[7]** was not here"
- "bideth me tell him as **[3]** that he is now without fear of danger"
- "He wisheth **[3]** to look well to Scotland"
- "If Steward himself, or the **[9]**, shall learn any thing that toucheth **[3]**"
- "within these 8 days ff. … **[7]** protested that he should never be quiet so long as the exercise of Religion continued"
- "both he and Spain shall … entertain the **[3]** with good words"
- "I have requested **H** to be throughly advertised"

## Reading

- **[3] = the Queen (Elizabeth)**: four occurrences, every one fits and no other value fits all four. Grade C.
- [7], [9], H and the nine-sign run: unread.

Cipher tokens (measured, transcription.txt): 21; 4 read (19%).

## Remaining gaps
- letter run "776 + w5 ‡ 6 3 ∩ 6" (f. 367r) - blocker: too-short; nine signs of an unknown alphabet, no key in print or on DECODE
- codes [7] (×2), [9] (×3), H - blocker: no-key-material; Walsingham–Burghley 1572 key not known to survive, contexts do not fix a single person

## Escalation
- [x] siblings: R8357 and R8363 (same volume) are being worked in `burghley1572/`, `walsingham1572/`; neither holds a key
- [x] clear-pages: all six pages are clear text; no decipherment or interlinear glosses
- [x] known-keys: Tomokiyo's Elizabethan cipher page (Cecil–Norris, Throckmorton, Stafford) has no Walsingham 1570–73 key
- [x] print: Digges 1655 prints all four letters, cipher left as figures; CSP Foreign x Nov 1572 does not calendar them
- [x] key-rebuild: context fixes [3]; [7]/[9]/H occur 1–3 times with no consistent reading; nine-sign run too short
- [n/a] retry: nothing new to rerun; no extended key

## Next leads
- The originals Walsingham sent (Hatfield / SP 70/125) may carry Burghley's clerk's decipherment interlined.
- Digges's other 1571–73 letters use the same boxed codes; a full inventory could pin [7] and [9].

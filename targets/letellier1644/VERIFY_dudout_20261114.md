# letellier1644: independent decoder, reading-side check and the open signs on the image (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Code groups
`contributed/data/key.tsv` holds the letters only. The code groups were taken from their sources:
Tomokiyo's table (cryptiana `louisxiv0.htm`, image `louisxiv_0marca1644.png`, read 14 Nov 2026) gives
=9 pour, =11 que, =12 qui, =26 vous, =32 Barcelone, =34 ambassadeur, 39 Catalogne, 81 faire (39 and 81 drawn
without a bar, as on f. 50), "roy" and "Roine?" (n̄ō); the contributor's `docs/METHOD.en.md` adds =y Monsieur le
Mareschal, =3 de La Motte, =11 =o la Reyne, =83 le Gouverneur. =34 (ambassadeur) does not occur on f. 50.
Source of "22 troupes" (READING.en.md, note to v05): not given in the contributor's files.

## Decoder
`verify_dudout_20261114.py targets/letellier1644` reads only `key.tsv`, `transcription_f50.txt` and the line table of
`docs/READING.en.md` (not `measure.py`).

1. Bare decode (main value of each sign) against `contributed/data/decoded_f50.txt`: **725/725 letters agree**.
2. Reading side (the other direction from `measure.py`, which asks which signs reach the reading): of the 741 letters
   of the line readings, 24 are marked as supplied in [ ]. **13 more letters are given by no sign and are not
   marked**:
   - 9 are the documented *qu'il* read from an unbarred `12 19` / `12 6` (v08, v10, v12; OPEN.en.md, "Not checked");
   - **4 are silent supplies**: r02-r03 *pr[i]s soing* has one s sign (7) for two s; v03 *c[e] que* (R 24 m 14: no
     e after c); v04 *[d]'icy* (line begins q 12 n); v06 *p[a]ssent* (`23 7 8 14 a 6`, checked on view 112: there
     is no sign between 23 and 7). The reading should mark them [ ].
   The 12 signs left without a letter are the ones the contributor lists as open, plus the cut sign of r10 and the
   struck-out sign of v08.

## Image check (Gallica / BnF IIIF btv1b9001389d views 111-112, full size 4864 x 6996)
The open signs, read on the image:
- r02 `p`: a clear plain p. It is the s of Tomokiyo's s column (row 4); the same p is s in v01 *paquet[s]*. So
  r02 reads *ayant s pr…*: the sign has a value; the word is still not understood.
- r03 end: `m·a·6` then the torn paper edge; the dots also stand between plain letters here, so the dots of r04
  (`·14·22`) do not mark a code group.
- r06 end `23`: the curved mark stands over the 3 only (as the straight bar of =3 on r19 stands over the 3), not
  over both figures as the bar of =32 (r18) does. It may be `2` + a marked 3 rather than a code 23; open.
- r16 `Ꝺ 22`: confirmed, followed by a large end-of-line flourish.
- r19: the sign before =3 is a ‡ with two bars, as the contributor has it.
- v05 `=18`: a clear straight bar over both figures (a code group). With 9 pour, 11 que, 12 qui, 26 vous in
  alphabetical order, 18 falls between *qui* and *vous*: *sçavoir* (after *de faire*, in clear) fits that order.

## Read bar (README)
`v10_relabel.measure` on `f50_reading.md`: 182 words, 15 holes, **0.924**, equal to the recorded `read_share`.
Marking the four silent supplies would lower it; the class (read in part) does not change.

Key correction: none to the letter values. The code values used come from Tomokiyo's table and METHOD.en.md.

## Not done
Only the open signs and v06 were looked at on the image; this is still an AI look, not the human check the notes ask for.

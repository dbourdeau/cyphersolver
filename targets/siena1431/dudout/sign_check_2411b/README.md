# Siena, Concistoro 2308 no. 24 (DECODE R4812 P2): the merged "c" label, blind sheet 2411b (24 Nov 2026, Brice Dudout, with Claude)

Images: DECODE R4812 (private study; not republished). No image or crop is in this folder.

Our transcription (`../../project_attempt/no06_24all.tok`) uses one label "c" (and partly "e") for two signs of George
Lasry's key R4755: the plain open c (h) and the e-like c with a tongue (n). The family "c / c^ / e" has 228 tokens.

Brice Dudout looked at 11 places on line-sorted crops of R4812 P2. The sheet was blind, with no values: 8 targets and
3 controls (a plain c, a c with a tongue, a closed e); all 3 controls passed. The rule (`sheet-2411b-rule.md`,
SHA-256 1a4d06d9...) and its amendment (`sheet-2411b-rule-amendment.md`, 04c0069a...) are in French as hashed, before
the thumbnails. The key was opened only after the answers were exported. Targets were taken line by line (m.02-m.07)
without looking at their value.

## The reader's question: one sign or two?
At q01 Brice asked whether the plain c and the c with a tongue are the same form. We kept **two signs**:
- On the image (P2 at 5x, the 15 places whose form is known), the tongued c closes its upper part with a horizontal
  stroke; the plain c stays open, at most with a small hook at the end of the top stroke (at 20-25 px this hook looks
  like a tongue, hence the doubt). The key sheet R4755 also draws two signs.
- Both merges were tested with the frozen key over the 228 tokens: all to n breaks 26 sure words (che, Chamerino,
  ghiacciatie, chamino...), all to h breaks 100. **The merge is rejected.**

## Results (`sheet-2411b-results.tsv`)
- **Plain open c (h)** at 3 targets: m.03 "d+ e p p" gives *par che* (our "e" there was a plain c); m.04 "YCROSS c 0"
  falls in an unread run (‹epinaqnl› -> ‹epihaqnl›, still unread); m.03 "ETA c t" is a plain c, which would give
  *vegho* for *vegno*. We keep *vegno* but mark its n **{probable}** (context only) until the place is checked again.
- **c with a tongue (n)** at 5 targets: all give n where the reading already has n (noie, in ponto, non, con) or in an
  unread run.

New labels in `no06_24all_2411b.tok` (a copy of the 2411a transcription with these 11 places relabelled; 3,685 tokens,
unchanged in number): CH (plain open c, h), CN (c with a tongue, n), EF (closed e, n). `reading_no24_rev_2411b.txt` is
the 2411a revised reading with the one changed run. The target's transcription and reading files are unchanged.

## Effect
Under the `understood` rule of `verify.py`: 1,815 of 2,279 decrypted letters understood (79.6%), **unchanged** (1,814
on a strict count that leaves out the n of *vegno*). No word of the reading changes, and no. 24 stays "decoded, not
read". Next useful step: a sign-by-sign pass over the 114 "c" and the "e" of our transcription inside the unread runs,
and one more question on q11.

## Credit
- Reading and key: George Lasry.
- Reviewer (form check): Brice Dudout.
- Sheet built, scored and integrated by Claude (AI agent).
- Images: DECODE R4812.

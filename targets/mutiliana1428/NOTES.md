# Ricc. de Mutiliana (Forlì) to Gianfrancesco Gonzaga, 6 November 1428 (DECODE R1854 image 3)

Read 22 Sept 2026, with a key taken from the letter's own contemporary interlinear decipherment. Split on 14 Oct 2026
from `targets/r1854/` under the one-key rule (George Lasry, 14 Oct 2026): DECODE R1854 holds four letters to
Gianfrancesco Gonzaga in four ciphers. This entry is the Forlì letter. The others, each a different cipher with its
own page: image 2 (`targets/r1854/`, Rome 9 Aug 1428), images 4-5 (`targets/cattanei1430/`, Rome Feb 1430), image 1
(`targets/malatesta1428/`, not solved). Images are git-ignored in `targets/r1854/` (main checkout) and not reproduced
(Archivio di Stato di Mantova).

894 cipher signs (`p3_signs.txt`, `ct_p3.txt`, measured), 869 read as sense (0.972), re-counted 5 Oct 2026. Italian,
clear text interspersed with runs of graphic signs.

## Method

The key was taken from the contemporary interlinear gloss (30 sign values, each attested 2–56 times; the gloss is
faint and about two-thirds legible, transcribed in `p3_gloss.md`), rare signs from context (db=q, wp=p, p=i, div=d,
tri=s, z=o, stb=mp, qm=co, E=è/e); signs transcribed by a subagent (`p3_signs.txt`), decoded to `p3_decoded.txt` with
`key3_p3.txt`. Name codes glossed: MALx = el signor Malatesta, FIOL = el fiol / li fioli del signor marchese, PAPA =
el papa. Nulls: +, hk (-♀-), hatched star, T, I, ℓ, Lh, tc, quatrefoil. Reading `reading_p3.md`.

## Content in brief

The governor of Forlì secretly favours the marquess's sons; the pope is said to be with them; an enterprise with the
lord Malatesta and the count of Urbino would make the lord of Mantua a great lord; Guidantonio of Urbino in secret
contact with Giovanni de Ramberto.

## Remaining gaps
- signs Z (2×) and fk (1×) - blocker: too-short; no gloss over them, two and one occurrences

## Escalation
- [x] siblings: R1853 register and the Mantova key records on DECODE opened (see `targets/r1854/NOTES.md`); the other R1854 letters are other ciphers
- [x] clear-pages: the interlinear gloss is the contemporary decipherment, used as the key source
- [x] known-keys: the register keys tried; none fits
- [x] print: web search; nothing printed for this letter
- [x] key-rebuild: key completed from context for the rare signs
- [x] retry: every run deciphered from its signs with the completed key, checked against the legible gloss

## Assumptions for George's review
- Method recorded as "key recovered based on adjacent plaintext", not "read from existing decipherment": the gloss is about two-thirds legible and the key taken from it was applied to all 894 signs. If George counts a contemporary interlinear decipherment as an existing decipherment however partial, the method changes and the entry leaves the key-recovery count.

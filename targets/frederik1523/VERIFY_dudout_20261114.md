# frederik1523: image 94 collated sign by sign with the edition's apparatus (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Check
`verify_dudout_20261114.py targets/frederik1523` reads `key.tsv` and `transcription_094.txt` (sign labels and the
label-to-Ch concordance in its header) and compares:

1. **Every sign of image 94, in order, with the edition's K1 sequence.** Hanserecesse III/8 n. 292 (pp. 324-325 =
   PDF pp. 344-345 of hanserecesse_3_8_low.pdf) gives a footnote at each sign with the Ch number for L, K and K1
   (= XIII 47c = image 94). Typed in text order (notes b, a, c, d … zz, a*, xx, b*), K1 has **51** signs; the
   transcription has 51 labels (the profile's transcription step says 50). **50/51 agree**; the one difference is
   the known l. 10 sign (Frederik's on the scan, Ch. 41 Lübeck in note o), already recorded in NOTES.md.
   Note a* confirms that K1 alone has "knechte adir rutere" in signs at l. 29 (L and K have Ch. 66 krygesvolck).
2. The 51 values from `key.tsv` all stand in `decryption_094.txt` at their lines (51/51).

## Words "as printed" (decryption header)
Of the ten spans in < >, nine are the words of the printed text (L): *leve besonderen, onen, steden, vorsument,
Up, eschent, iligesten, itzundes, 4000*. The tenth, l. 29 **<durchtheent>**, is not in the printed text, which
reads **durchthendes**; *durchtheent* occurs only in note l*, in a passage struck out in the drafts K1/K2. On
image 94 (Rigsarkivet id 41301914) the word is written in a cramped form ending in *-nde*; it is not *durchtheent*
either. `decryption_094.txt` is corrected to <durchthendes>, following the file's own rule (words given as printed).

## Read bar (README)
`v10_relabel.measure` on decryption_094.txt: 279 words, 0 holes, **1.0**, equal to the recorded read_share.

Key correction: none.

## Not done
Image 95 (the rest of the letter) and the other letters of item 8 were not looked at; the l. 10 sign was not
re-read (NOTES.md has it).

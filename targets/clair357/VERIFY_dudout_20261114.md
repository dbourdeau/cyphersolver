# clair357: the f. 168r copy checked against its cipher, three passages corrected (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
NOTES lists as open "word-by-word decoding of the ~30 cipher lines above the ✝, to check f. 168 phrase by phrase".
This pass did it for the last seven lines before the ✝ (f. 167r ll. 23-29, 266 figure groups), the part of the copy
with the most holes. The figures were read on the Gallica image (btv1b9001053r, canvas 331, full size) and written to
`texts/f167r_l23-29_figures_dudout.txt`, one manuscript line per row, each with the f. 168r words it corresponds to.

`verify_dudout_20261114.py targets/clair357` decodes them with Tomokiyo's table (typed from `henryiii_Anonymous.png`)
plus the additions in `key.md` (87 = e, 71 = a, 22 and 66 nulls). It does not use `b26_clair_dec.py`.
**293 of 311 letters agree with the copy (0.942).** All the disagreements are one of these:
- 9 groups not in the key: 30, 33, 46, 48, 75, 79, 89, 90, 94 (values below);
- one place where the cipher spells differently from the copy: *chacun* (33) for *chascun*. The cipher also gives
  *ferez congnoistre* where the copy is read *faire*; the copy word was not settled on the image;
- two surplus 7s, both straight after 27 (s): *ins 27 (7) 26 ance*, *pours 27 (7) 24 icte*. They may be a scribe's
  habit or a stroke read as a figure.

The same script also decodes the FIG lines of `f167_interlinear_transcription.txt` (after the ✝): 222 of 235 letters
match the DEC lines there. The remainder is where the DEC lines stop short or skip groups. No wrong letter value was
found.

## Image check (f. 168r, canvas 333)
The decode settles three doubtful passages of `f168_reading.md`. Each was then read again on the clear copy, and the
copy has the same words as the cipher:

| f168_reading.md (23 Oct) | cipher ll. 23-29, decoded | f. 168r re-read |
|---|---|---|
| faisant des stances [?] et autres places | faisant instance des [22] autres places | *faisant / instance des autres places* |
| que vous n'y quictez rien. La poursuite ne les travaux [?] de la brouillerie du Roy de Navarre | que vous ne quictez ny la poursuicte ny l'esperance [30]ur la reconciliation du Roy de Navarre | *ne quictez ny / la poursuicte ny l'esperance p[ou]r la reconciliation* |
| luy de [protecteur?] … Catholiques … Huguenotz … qui passe avant | l'un de proteger [46][cross sign] l'autre [46][⊖] sans l'autre qui passe avant | *l'un de proteger les Catholiques, l'autre les Huguenotz, sans / l'autre qui passe avant* |

The sense of the sentence changes. It is the hope of a **reconciliation** between Navarre and the addressee, which the
writer thinks very difficult because one protects the Catholics and the other the Huguenots. It is not a "brouillerie".
This fits the rest of the letter: Fumée's repeated proposals of "cette reconciliation" after the ✝. In the cipher,
*l'autre* (first time) is written in clear.

`texts/f168_reading.md` and `texts/f168_en.md` are corrected for these three passages. The header of each says so.
`f167_decryption.md` and NOTES.md ("Text") still carry the old wording. That is left to the maintainer.

## Key (new values, each read against the copy)
| group | value | where (l.) |
|---|---|---|
| 46 | les | vous **les** p[ourrez] (24); **les** Catholiques, **les** Huguenotz (29) |
| double-barred cross (part blotted) | Catholiques | 29 |
| ⊖ | Huguenotz | 29 (confirms the NOTES "uncertain" row) |
| 94 | t | distrai**t**es (24), **t**res (27) |
| 89 | ff | di**ff**icile (28) |
| 33 | c | cha**c**un (28) |
| 30 | p(o) | [30]ur = pour (26/27, at a line end) |
| 75, 90 | d, s? | **d**istraite**s** (24), one each |
| 79 | r(r) | pou[79]ez = pourrez (25) |
| 48 | null? | ne [48] quictez (26) |

Also: in Daniel's sample run "25 28 88 22 20 24 …" (NOTES, key.md) the third group is **82** (s) on the image. So "des"
is written in full and the bracket in "de[s]" is not needed. 22 stays a null there. 87 stands where the copy has no
letter ("prinse [87] l'un", l. 28), so its value e (from *Fumée*) is not confirmed here.

## Read bar (README)
`v10_relabel` on `f168_reading.md`: 0.955 (364 words, 17 holes) before, **0.964** (371 words, 14 holes) after. Both
are above 0.95, and that entry was already *read*. The class of the target ("read in part", set by the other entry at
0.942) is unchanged. read_share and class were left as they are.

## Not done
Lines 1-22 of f. 167r were not transcribed, so the holes of the copy there ("Charry …", "Nemours [?]", "vingt [?]",
"[au]mosnier …") are still open. The method above would close them. The sender's signs on f. 167v were not looked at.
No human palaeographer. Images not stored in the repository.

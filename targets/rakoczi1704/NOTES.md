# "Ferenc Rákóczi II to unknown recipient": three French letters to Rákóczi — DECODE R852, R912, R922

Status: read. The three French letters (R852, R912, R922) are reports *to* Rákóczi. R912 and R922 read with the
preserved key DECODE R639 at about 97% of groups from a fresh transcription of the images. About a third of those
groups had been deciphered at the time, between the lines: nearly all of R912's first page, the first lines of its
pages 2 and 3, and the first two lines of R922 (recorded 30 Sept 2026, "Deciphered at the time" below). R852 has its own clear
copy.

Split on 14 Oct 2026 under the one-key rule (George Lasry, 14 Oct 2026). The fourth record of catalogue item 44,
Rákóczi's own Latin letter R483 (Lwów, 27 June 1711), is in a different cipher, a Latin syllabary whose key was
rebuilt from its interlinear decipherment. It is now [`targets/rakoczi1711/`](../rakoczi1711/NOTES.md) (a different
cipher, with its own page); its section below is kept as a pointer.

Catalogue item 44 (class B, scored by rule). All four records are MNL OL, and the images are not in the public
domain, so none is reproduced. Worked 21 Sept 2026. Pass 1 used DECODE's text transcriptions. Pass 2 fetched the
images (`fetch_img.py`, into the git-ignored `img/`) and re-transcribed every cipher page into `tr/`.

## Correction to the catalogue

DECODE gives Ferenc Rákóczi II as the author of all four. That holds only for R483. R852, R912 and R922 address
"Monseigneur" and "Votre Altesse" and report on Rákóczi's affairs at the Polish court, so Rákóczi is their
recipient, as with R902 (`../rakoczi1707/`). The catalogue's "1704–1711" is DECODE's span for the volume.

## The French letters and the Bonac–Groffey key (DECODE R639)

The key is a one-part numerical nomenclator, codes 10–560. The twelve odd numbers 97–119 are nulls. The groups of
500 and above that open a line (563, 564, 574, 589, 607, 609, 620 …) behave as nulls too.

Reading the key image (`img/IMG_R639_I3927_P1.png`) corrected DECODE's transcription of the table:

- S is 44, **45**, 100, 83 and T is 46, **47**, 102, 85. The 45 and 47 are overwritten on the sheet, and DECODE
  read them as 95 and 96. On the sheet, 95 belongs to *es* and 96 to Q.
- Z is 54, 55, 110. DECODE wrote "100/110?", which made the old decoder drop the whole Z line, and with it 55.
- The table's numbering jumps from 172 (Da) to 175 (de). The letters use **173 and 174 as "de"** throughout
  ("le Roy 173 Pologne", "Palatin 174 Belz"). Grade C.
- **561 and 562 = "nt"** (after *poi-*, *souve-*), beyond the end of the table. Grade C.

`decode_tr.py` applies the corrected table to the new transcriptions. The old `decode.py` output on DECODE's
transcription, `R*_key08_read.txt`, is kept for comparison.

| Record | Shelfmark (G15 Caps. C. Fasc. 39) | Date | Groups (image) | Keyed | Pass 1 (DECODE text) |
|---|---|---|---|---|---|
| R922 | pp. 346–347 | Dantzig, 28 Oct [1707] | 722 | 705 (97.6%) | 683/730 |
| R912 | pp. 312–314 | "au quartier", 5 Nov [1707] | 1,630 | 1,585 (97.2%) | 1,473/1,596 |
| R852 | pp. 115–117 | Dantzig, 22 Jan 1706 | 523 | clear copy on pp. 116–117 | 497/513 |

Unread in R912 and R922: 62 groups (61 before the 30 Sept 2026 re-reading of 509 as 589). They are line-opening
and line-closing fillers of 500 and above, the closing and signature
block of R912 p. 3 (`589 4 5 710 607 3 586 1000 …`, probably a date and a name in figures), and a handful of
values outside the table: 93 (×3), 89 (×3), 9 (×2), 3–8 and 699. The re-transcription corrected about 40% of
DECODE's lines. It found a line DECODE had dropped in each of R912 and R852, repeated runs, merged groups, and the
misreadings 350/380, 324/329, 489/459/497 and 687/607.

**R852 uses a different issue of the table.** Its letters and syllables agree with R639, but many of its word
codes, mostly those ending in 4 (144, 254, 194, 404, 294, 314, 424 …), mean something else: 144 = *de*, 254 = *la*
where R639 gives *beaucoup*, *jusque*. The letter's own clear copy (p. 116 and the top of p. 117, read from the
image into `R852_clear.txt`) supplies the text, so the variant table has not been rebuilt. The date is written
"22 janvier 1706". It speaks of "l'action", probably Zsibó (Nov 1705).

### What they say

- **R852** (Dantzig, 22 Jan 1706). The writer acknowledges Rákóczi's letter of 26 December and will pass letters on
  "au Sr. Groffey". He vouches for Groffey's loyalty and prudence. He waits for "le Sr. Roth." to join him. He asks
  for a weekly Latin paper like the *Mercurius hungaricus*, because every German and Dutch gazetteer "destroys the
  Kingdom of Hungary at his ease", and in Berlin people believed that no Hungarians were left after "l'action".
  Bercsényi ("Bertoti") could print the news and send it by way of Cracow. P. 117 adds a short clear note offering to
  register M. de Bonnac's letters and bills of exchange for Rákóczi.
- **R922** (Dantzig, 28 Oct [1707]). The writer reports a sale carried out for Madame la Palatine de Belz (Elżbieta
  Sieniawska), with an authentic copy sent to the sieur Kray. He has kept out of the business "as far as possible, by
  my credit and my advice". There are orders for carbines. He is leaving to join the King of Poland and asks that
  Kray be given orders so that he can continue "mes services à la Cour de Pologne". P. 2 covers money matters and a
  prisoner.
- **R912** (5 Nov [1707]). A survey of Polish and Swedish politics: King Stanisław, the Palatine of Belz and the
  Grand Hetman, the Muscovites under the Field Hetman, the King of Sweden's pacification and a new election, the
  Tsar, and Rákóczi's letter to Rehnskiöld (the affair of R902). The Palatine of Ruthenia and a regiment asked of
  Rákóczi, which Stanisław and the Germans hold against him, also come up, as do Tököly and his siege.

### Deciphered at the time (30 Sept 2026)

Reported while quotations were pulled for Lasry's list and checked on DECODE's transcriptions
(`DOC_R912_D2230_2230.txt`, `DOC_R922_D1861_1861.txt`) and on the images (`IMG_R912_I4877_P1`–`I4879_P3`,
`IMG_R922_I4911_P1`, in the git-ignored `img/`; a copy is in the main checkout's `.worktrees/rk2/rakoczi1704/img/`).
The earlier write-up mentioned interlinear decipherment only for R483.

- **R912** has a contemporary decipherment written between the lines. DECODE records it as `<PLAINTEXT FR …>` lines:
  29 of them on page 1 (image 4877), 5 on page 2, 2 on page 3. On page 1 it covers every line of figures except the
  end of the line that begins 113 (after 504 *Allemagne*) and the two lines below it (229 …, 358 …): 659 of the
  page's 713 groups. On page 2 it covers the first four lines and the start of the fifth ("M. que vous na luy au e"),
  about 98 of 686 groups; on page 3 the first line and the start of the second ("ce de tant st le garde"), about
  25 of 231. In all about 780 of R912's 1,630 groups (48%). `tr/R912_p1.txt` already noted "decipherment written above
  lines throughout", but the reading and the page did not say so.
- Under it lie most of the phrases the page quotes for R912: the opening "J'ay eu l'honneur de marquer à V. A.", the
  Palatine of Belz, the grand général, the pacification, the new election, the Tsar (p. 2 l. 3) and the letter to
  Rehnskiöld. Not deciphered on the leaves, and deciphered here with R639 alone: the rest of pp. 2–3 (Palatine of Ruthenia, the regiment,
  Stanisław and the Germans, Tököly, the closing "avec un profond respect et un zèle parfait") and the three
  uninterlined lines of p. 1 (next section).
- **R922** has an interlinear over its first two lines only (the date and "je me suis privé pendant quelque temps de
  l'honneur d'escrire à Vostre Altesse"), 37 of 722 groups. The rest was read here with R639.
- R912 + R922 together: about 820 of the 2,352 groups (35%) were deciphered at the time; about 1,530 were read
  only here. The 97.4% key coverage still stands as a measure of the key, but not of what is new.
- Profile: `conditions.prior_solution` and the R912/R922 `plaintext.source` now give these extents. `outcome.method`
  was left as it is ("read after matching with key from external sources"): the parts with no contemporary
  decipherment (R912 pp. 2–3 after the first lines, three lines of p. 1, and R922 after line 2) were read with the
  external key R639. A `parts` split (R912 p. 1 "read from existing decipherment") is for the main session to decide.

### R912 page 1 without an interlinear (30 Sept 2026)

The contemporary decipherer stopped after "… pour ne pas s'éloigner de l'Allemagne" (line beginning 113) and left
the rest of that line and the two below (54 groups; `R912_image_read.txt` lines 17–19, `tr/R912_p1.txt` lines 19–21).
The sentence begins two lines higher: "il est à mon avis plus vraisemblable que ce Prince [the King of Sweden] s'est
voulu réserver un prétexte de rester cet hiver en Pologne pour ne pas s'éloigner de l'Allemagne". It continues:

> … ni perdre de veue les affaires generales de l'Europe. Aussy publie-t-on comme une chose presque certaine qu'il
> n'entrera en Moschovie que la campagne qui vient.

"… nor lose sight of the general affairs of Europe. So it is given out as an almost certain thing that he [Charles
XII] will not enter Muscovy until the coming campaign." (He invaded Russia in the campaign of 1708.) Every group was
checked on `IMG_R912_I4877_P1` and against the key sheet `IMG_R639_I3927_P1`. 44 groups read directly (H); 589, 619
(fillers) and 115, 97 (nulls) are dropped; six are graded M:

- *publie*: the image has **327** = *pu*, not 329 = *pas* as transcribed (the report suggested 324). The last figure
  has the open, angular top of this hand's 7 (257, 297 in the next line), not the round bowl of its 9 (349, 149,
  the 9 of 297); 324 is ruled out, its 4 being closed (the 324 two groups earlier). Transcription corrected to `327?`.
- *une*: the image has **87** = U, not 57 = *Et* (our transcription and DECODE's both had 57). The first figure closes
  in a loop at the foot like the 8 of 87 in "un homme" (line beginning 125) and the 8s of 81 and 18 in the same line,
  not the open hooked 5 of 315, 405, 255 and 583. Corrected to `87?`.
- *veue*: 427 426, both *ve* in the key. The key's alphabet has no V (T, U, X), and the contemporary decipherer
  wrote *ue* over 427 in "se r ue r" (the end of *réserver*) a line higher, so the second is read *ue*.
- *presque*: 343 350 = *présent que*; the sheet has "présent – 343". The writer used 343 for *pré-* in *prétexte*
  two lines higher, where the decipherer wrote *pre* over it. Read *pres-que*.
- *campagne*: 58 = *ns* on the image (5 as in 358 and 589, 8 looped) and on the key sheet (ns = 58, 59, 114). Read as
  a slip for 88 = M (M = 32, 33, 88).
- *vient*: 534 46 = *Vienne* + T (534 underlined on the leaf). The place code is used for its sound, as 266
  *leur* gives *l'Eur-* in *de l'Europe* in the same line.

Also corrected: the last line's 509 (*France*) is **589** on the image (the middle figure is the looped 8), as DECODE
reads it, a line-end filler. That moves one group from keyed to unread: R912 p. 1 702/713, R912 1,585/1,630 (97.2%),
R912 + R922 2,290/2,352 (97.4%), unread 62. `R912_image_read.txt` regenerated with `decode_tr.py`; the page's table,
this file's table and the profile grades updated. Not changed here (shared files): the README results row still says
2,291 of 2,352; `papers/lasry/excerpts.json` and George Lasry's list do not mention the contemporary interlinear.

Writer: unsigned. R852's writer names Groffey in the third person and was at Danzig. R922 is also from Danzig and
may be the same man. Grade M. The key heading *De Monsieur de Bonac et Graffei* suggests that the key served the
whole Bonac–Groffey correspondence.

## R483: moved to rakoczi1711

Rákóczi's Latin letter of 27 June 1711 (P237 Festetics 10. d. 2. 42–44, 2,531 groups) was filed here until 14 Oct
2026. R639 gives nonsense on it (`decode.py` control, `R483_key08_read.txt`, kept here with DECODE's transcription
`DOC_R483_D2172_2172.txt`). Its transcription `tr/R483_p*.txt`, the aligner `align483.py`, `check483.py`, the
rebuilt key and its reading are now in `../rakoczi1711/`.

## Files

- `fetch_decode.py`, `fetch_img.py`: fetch the DOC transcriptions and the images (cookie from `../bordeaux/decode/`).
- `tr/`: new transcriptions from the images (R922 p1–2, R912 p1–3, R852 p1–3; R483's are in `../rakoczi1711/tr/`).
- `decode_tr.py`: the corrected R639 table. `R922_image_read.txt`, `R912_image_read.txt`: readings.
- `R852_clear.txt`: the contemporary clear copy of R852.
- `decode.py`, `R*_key08_read.txt`: pass 1 on DECODE's transcriptions.

# Rome, January 1478 (st. fior.): Giovanni Mazzinghi and a second writer to the Medici, cipher (catalogue 2307, 2320)

Status: in progress. Started 6 Nov 2026 at the user's request after the overnight sweep. Transcription under way;
no key yet.

## The documents

All three are in the Archivio di Stato di Firenze, Mediceo avanti il Principato (MAP). Images from the ASF MAP viewer
(full server size, 1272 px wide), fetched with `getdoc.py FILZA DOC` into `img/` (git-ignored).

| Catalogue | MAP | Date as written | Writer | State |
|---|---|---|---|---|
| 2307 | LXXXIX 142 (recto; verso is show-through plus endorsement) | "In Roma a dì 16 di gennaio 1478" | Giovanni Mazzinghi (verso: "1478 ad 16 di gennaio / da G. Mazinghi / Cifra") | bare: about 40 lines of cipher words with clear connectives, no decipherment |
| 2320 | CXXXVII 252 (recto) | "a dì 13 di gennaio 1478" | unsigned (same signs and hand as 2307) | bare: about 17 lines, no decipherment |
| (lead 2308, closed read) | LXXII 170 (recto) | "a dì 2? di gennaio 1478" | same system | the key source: a decipherment written over the cipher words in a second hand |

**Dating.** All three say "gennaio 1478". A Florentine writer counted the year from 25 March, so this is very probably
January **1479** in modern style: nine months after the Pazzi conspiracy (26 April 1478), during the Pazzi War, with
Florence under Sixtus IV's interdict. 2307 is headed "In Roma". The overnight vetting (batches n08, n10, c32, c33)
called them January 1478 and Lorenzo's *Lettere* II-III were searched for both years without a hit; the catalogue
entries are corrected to "January 1478 st. fior. (1479)".

## The system (first look)

Words are enciphered one by one and left as words, separated by spaces or dots; clear words ("com[e]", "che", "quanto",
"papa", numerals) stand between them. The signs are letter-like (o, +, double-barred crosses, q, 4, r, z, t, s, b, m,
n, l, p, 8, x, =). Probably a homophonic substitution of letters with word division kept. The glossed letter LXXII 170
gives cipher-word / plain-word pairs.

Not the system of `targets/siena11` (Acciaiuoli, Rome, June 1478, Lasry's key).

## Plan

1. Glyph inventory and transcription of LXXII 170 with its glosses (`glyphs.md`, `t170.tsv`).
2. Transcribe 2320 and 2307 with the same tokens.
3. Fit the key on the 170 pairs; hold out a share of the pairs to test it.
4. Decipher 2320 and 2307; read, translate, check against the 1479 events.

## Prior work checked

- Lorenzo de' Medici, *Lettere* II and III (Google Books ids 1hpdAAAAMAAJ, MBxdAAAAMAAJ): no citation of LXXXIX 142
  or CXXXVII 252 (Chrome passes c32, c33, 6 Nov 2026). The Pazzi War letters of early 1479 fall in vol. III-IV;
  vol. IV was searched for LXXII 171 only. To repeat for these two shelfmarks.
- DECODE has no MAP records; Tomokiyo and Lasry's GL.htm have nothing on them (vetting batch n08).

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

## 6 Nov 2026: 2307 key recovered from its own ciphertext, read in part (parallel session, PR #301)

This section was worked in a parallel session from the catalogue 2307 task prompt, before the plan above was
merged in; its files are `transcription_89_142_v1.txt`, `reading_89_142.txt`, `key.md`, `solve.py`, `measure.py`,
`decode_lines.py`, `WORKLOG.md` (images in `images/`, git-ignored). Steps 2-4 of the plan are done for 2307 only;
step 1 (the 170 pairs) is still the way to settle the merged sign classes. 2320 is not touched.

**System.** Monoalphabetic substitution in letter-like signs, word division kept, numerals for persons, barred p for
*per*, many clear words. About 1,050 cipher signs in 189 cipher words, plus about 190 clear words. The key is in
`key.md`.

**How the key came out.** A first-pass transcription (`transcription_89_142_v1.txt`, 29 sign classes) went into a
homophonic annealer (`solve.py`, it-cinquecento order 5 with spaces, KL penalty on letter frequencies; without the
penalty it collapsed onto all-*i*). It returned sense straight away ("contra di voi molto crudele", "la vita", "molte
volte", "di loro altro", "grandissimo", "gli crede assai", "messere ... da castello"). Control: an Italian passage of
537 signs in a random 29-sign homophonic key came back 655/667 letters right. Then each line was re-read in 3x crops and
deciphered word by word (`reading_89_142.txt`). One gloss pair from the sibling 72/170 ("publichamente mostra lectere")
agrees with the key (p q = 6 s o + 8 x n H x; 8 r 4 H r +).

**What the letter says (so far).** News from Rome after the Pazzi conspiracy, so 16 January 1479 in modern style:
the chancery has revoked "tutti i privilegi" of the Church (`cancelleria ... arrivocati tutti i privilegi`) that the
Pope "aveva mai conceduti"; the Pope is "acceso contra di voi molto crudele", "abbino el diavolo in corpo"; a Iacopo
"da Pistoia" and another "pistolese che si chiama ..." are named; "ordinò la morte del 30"; "sarete avisato come
ognuno"; "è di venuto messer Lorenzo[?] da Castello ... molto gagliardo[?]"; "mi fanno mille carezze e spesso mi
dicono mille novelle"; "dua travestiti"; "gl'imbasciadori lucchesi"; "lettere del 40"; "al popolo". The clear words
("Bisognerà", "mille", "quanto", "effetto", "mostrando", closing "mi raccomando") are read only roughly so far.

**Measured** (`python measure.py`): of 189 cipher words, 111 read (58.7%), 30 read with doubt, 48 open; by signs
61.8% read, 79.9% read or doubtful. Read in part.

**Date and post.** The cipher confirms the Florentine-style date: the content is after April 1478 (Pazzi conspiracy,
the papal interdict). Rome is implied by the papal news and the ambassadors; no place is written.

## Remaining gaps

- 2320 (CXXXVII 252): not transcribed yet; same signs, so the 2307 key should apply.

- Sign classes the 1272-px scan does not separate (o, 4, H, b/6, q): values chosen from context; about 30 words
  carry a doubt from this. Not an outside blocker yet: the sibling key rebuild has not been done.
- 48 cipher words open, mostly in lines 1-3, 9-12, 18-19, 23, 26-31 (see `reading_89_142.txt`).
- Code numerals 2, 3, 10, 12, 30, 40 and the groups `olop`, `ov+`, `cop`, `oxP`: open codes, no key material yet.
- Clear words: only a rough reading of the mercantesca; needs a careful pass.

## Escalation

- Next: transcribe MAP 72/170 cipher and gloss pairwise (lead 2308) and rebuild the sign table sign by sign; this
  should split the merged classes and may give the code numerals (the sibling has "a Giovanni ...", "del papa").
- Check MAP LXXII and LXXXIX neighbours for more letters in this system (same sender, Jan-Feb 1479).
- Read the clear passages carefully; they carry the context for the open runs.
- Higher resolution: the ASF server caps at 1272 px; a request to ASF for a high-resolution scan of 89/142 would
  settle the sign classes if the sibling does not.

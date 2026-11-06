# Giovanni Mazzinghi, cipher letter of 16 January 1478 (1479 modern), ASF MAP LXXXIX 142

Status: in progress

Catalogue no. 2307 (https://cyphersolver.com/solve/2307.html). Sibling with interlinear decipherment: lead 2308,
MAP LXXII 170 (23 Jan 1478, anonymous), same sign set.

- Document: Archivio di Stato di Firenze, Mediceo avanti il Principato, filza LXXXIX, doc. 142 (old c. 149). One leaf,
  recto 37 lines of cipher with clear words between runs; verso endorsed "1478 ... adi 16 di gennaio ... da G. Mazinghi",
  "Cifra". Inventory vol. 3: "Giovanni Mazzinghi. (cifrato). s. l., 1478 gen. 16, n. 142".
- Images: IIIF recto https://archiviodistatofirenze.cultura.gov.it/iipsrv/iipsrv.fcgi?IIIF=/data/iip-data/asfi/mediceo_avanti_principato/00100089/A0000463.ptif/full/full/0/default.jpg
  (1272 x 1837 is the full size; info.json gives nothing larger), verso A0000464. Sibling recto 00100072/A0000397.
  Images are kept out of git (`images/`).

## 6 Nov 2026: first session

**Prior art.** The vetting record on catalogue 2307 (6 Nov 2026) already covers DECODE (no record), Tomokiyo (no MAP
item), Lasry (GL.htm, Siena 2308 report: no), Lorenzo's *Lettere* II and III (no citation of 89/142) and the Google
Books feed. Nothing added this session; no decipherment of this letter is known.

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

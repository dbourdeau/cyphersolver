# idiaquez1577: Juan de Idiáquez and Pedro de Mendoza to Philip II, Genoa, 24 November 1577 (catalogue 754, AGS Estado 1410,115), cipher of images 1-2 read in part

Status: in progress. Folder integrated 13 Nov 2026 without a page: images 3-6 (about 105 cipher lines) are not transcribed (workable gap); the contributor's state for images 1-2 is read in part.

## Document

- Archivo General de Simancas, Estado, leg. 1410, no. 115 (PARES 3577720): "Carta cifrada de Juan de Idiáquez y Pedro
  de Mendoza, embajadores en Génova, a Felipe II, rey de España, sobre la llegada del tercio de Lope de Figueroa a
  Lombardía". Genoa, 24 November 1577 (dated in clear on image 6). 4 folios, 8 images; signed by both ambassadors.
- Images: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3577720 (viewer
  `catalogo/show/3577720`). Not copied into the repo.
- Image 1: address and two paragraphs in clear (the King's letters of 16 and 21 October; troops leaving Flanders; Lope
  de Figueroa's tercio in Lombardy; the troops of Naples to embark on the 15th), then 4 lines of cipher. Images 2-6:
  cipher, about 130 lines in all, with the clear close and signatures on image 6. Images 7-8: address leaf and docket.
  No decipherment is filed with the letter (none on the images; the PARES description has no note of one).

## System and key

The 1577 Genoa embassy syllabary that Brice Dudout rebuilt for `targets/perez1578/` (K_P2, from cipher/"descifrada"
pairs of AGS Estado 1410 and validated by him on the fresh pair 1410,65-66): a numeral is a consonant (6 d, 7 c, 8 b,
11 g, 12 h, 15 l, 16 m, 17 n, 20 p, 21 qu, 22 r, 23 s, 24 t, 25 v, 28 y, 29 z, 33 fr, 35 pr...), a mark after it is the
vowel (cross a, dot e, 6-loop i, hook o, stroke u), the bare numerals 10, 4, 2, 18, 1 are the vowels a, e, i, o, u,
and marks above add n (caret), s (bar), r (check) or l (tick). Code groups carry a small cross above: 145 = V.Md.,
8 + hook = Señoria, 6 + hook = republica.

`key_frozen.tsv` is K_P2 as published on origin/main, with only the changes his own notes give for the Genoa table
(8 = b, not g as in Pérez's hand; Pérez-only values dropped). It was frozen (SHA-256 in `key_frozen.sha256`) before
this letter was decrypted, and nothing in it was learnt from this letter. `key.tsv` = `key_frozen.tsv` (no values were
added afterwards). Signs this letter shows that the key does not give: a tilde over 33 (twice, in *frances(es)*), an
underline under 31, 30 and 35 (three times; by sense it may turn *r* into *l*: *excluydo*, *exemplar*), a small 2 over
7+ and over 6 + hook, and a dot after the bare vowel 2. One value looks different from K_P2: 35 + hook is *pri* (once,
in *principales*) where the key gives *pro*. It is marked as a repair in the reading, not added to the key.

## Held-out test

The whole passage is held out: the key was built by another contributor on other letters. `scripts/heldout.py`
compares the mechanical decryption of each line with the read text: frozen key 97.0% of characters and 91.0% of the
122 words of three or more letters (111 of 122); 200 control keys (100 with consonant values permuted, 100 with vowels and vowel
marks permuted) at most 92.2% characters and 74.6% words, mean 8.0% words. The frozen key is above every control. The
reference is our own reading, so this is not independent of the key; the stronger evidence is that a key made on
other letters gives coherent Spanish on 26 lines it never saw, with 173 of 187 words verbatim.

## Reading

`reading_1410_115.md` (running text in Spanish), `marked_1410_115.md` (line by line against the signs, every departure marked), `translation_1410_115.md`. Cipher of images 1-2 only (26 of about 130
cipher lines). Words: 187 cipher words; 173 verbatim from the signs (92.5%; 169/183 = 92.3% without the 4 code-group
occurrences, which are 3 distinct groups: V.Md. twice, Señoria and republica once each), 3 with a marked repair,
3 guesses, 8 holes; none from a gloss. `scripts/check_marks.py` rebuilds the decryption from
the transcription and the frozen key and passes. Dan's `docs/_check_reading.py idiaquez1577` (run in a throwaway
worktree of origin/main): `reading_1410_115.md` readable, clean share 0.727 (16 of 22 sentences, hole rate 0.109, es);
the raw mechanical decryption scores 0.296 (unspaced, not a reading) and the line-broken marked file 0.548.

Content: the ambassadors play down the report that the French will send an ordinary ambassador to Genoa: perhaps the
Count of [Fiesco] and some of the exiles of the conspiracy, or their relatives, pushed for it, but it is no general
request of the "new" nobles, whose leading men now make one body with the "old" nobles; if a French ambassador could
ever be kept out, it is now, though Genoa is so changeable that nothing can be promised. On the conspiracy, they have
given the Signoria the King's letter on investigating it and punishing the guilty exemplarily.

State: **read in part** (coherent sentences, 92.5% verbatim, a few holes in some sentences; four fifths of the cipher
not yet transcribed). An independent blind review (13 Nov 2026) confirmed the state, grade B; see below.

## Notes on the marked places


- L01, L16 `33+` with a small tilde: 33+ is *fra* in the key; the tilde is not in the key, so the sign is counted as a
  hole. Both places are *frances(es)* by sense.
- L02 *ordinario*: the mark over 18 is drawn as a caret (n) but the word is *ordinario*; caret and check (r) are close
  in this hand. Repair.
- L04 *Fiesco*: the signs give *fiesbo* (8 = b). Read by the contributor as the Fieschi family, whose exiles lived in
  France, from the sense; the cipher does not say which count is meant. 8 for 7 is a slip of the cipher clerk or a
  misreading. Guess.
- L05 *por lo*: a dot after 22 gives *re*; the dot may be punctuation. Repair.
- L08: `7+` with a small 2 above it and the group *qui-la-man* are not clear; *acá llaman nuevos* ("those who are
  called 'new' here", the *nobili nuovi*) is a guess from the sense.
- L10 *principales*: the frozen key gives 35e = *pro*. Here 35 + hook stands for *pri*. Marked as a repair.
- L12 *agora*, L15 *algun*, L21 *negocio*, L24 *averiguacion*: the sign before the vowel mark has one shape in all
  four words, an upright 1 followed by a stroke with a crossbar. It is transcribed 11 in all four (11e = *go*,
  11| = *gu*, straight from the key). The first reconciliation had read it as 14 (the crossed 4 of this hand) in
  *agora* and *negocio*, which needed a repair *guo* -> *go*; the blind reviewer saw the same shape in all four places
  at 5-6x zoom, and the transcription now follows that. The shape is close to this hand's 4 (see Remaining gaps).
- L13 *inferiores*: the signs give 13^ (*jn*), then the vowel 2 with a dot (not in the key), then *rio res*. Guess.
- L17 *excluydo*: 31 with stroke, underlined. 31 is *cr* in the key; the underline is not in the key. *excluydo* by
  sense; the underline may turn *r* into *l* (see L25). Guess.
- L18: `30.` underlined, unidentified (hole).
- L20: `6e` with a small 2 above, unidentified (hole); *recato* by sense.
- L23 *mucho*: the signs give *meco* (16. 7e). Guess.
- L25 *exemplar*: 35+ underlined; 35+ is *pra*; *pla* by sense, as on L17. Guess.

## Prior art (checked 12 Nov 2026)

- Dan's repo (local origin/main 65445e3f8; live head 7dcbe3f68, 12 Nov 2026 17:56 UTC, checked by GitHub API and code search): no target folder for this letter; 1410 is cited only as the key
  source in `targets/perez1578/`. No open PR or issue on Genoa, Mendoza, Idiáquez, Padilla, Binasco or leg. 1410/1414.
- Two web searches (Idiáquez, Mendoza, Génova 1577, carta cifrada, embajador francés, nobles nuevos/viejos): no edition
  or decipherment of this letter found; only catalogue records and general work on the Genoese nobility after the
  1576-1577 settlement. CODOIN and the Genoa volumes in Memorie digitali liguri were not searched in full.
- Collision recheck 13 Nov 2026: live head 65cdcd9d5 (12 Nov 2026 21:56 UTC); no `targets/idiaquez1577`; no target or
  research file on origin/main that works 1410,115; no open or closed PR or issue on Idiáquez, 1410,115 or PARES 3577720.

## Blind review (13 Nov 2026)

An independent AI language-model agent, which did not make the solution, checked the folder. It read 4 lines of
image 2 (img2 L11, L14, L18, L20; 68 signs) by shape from 3x-6x crops before opening the transcription: 64 of the 68
signs agree with the transcription, and none of the 4 differences changes a word. It reran `check_marks.py`,
`decrypt.py` and `heldout.py`, compared the frozen key line by line with `targets/perez1578/key.tsv` (no value learnt
from this letter), and reran Dan's `docs/_check_reading.py` (clean share 0.727). Verdict: read in part, grade B.
Changes made after it: the 11/14 shape above (two repairs became verbatim readings), and the English of the first
sentence made to follow the reading's punctuation.

## Remaining gaps

- Images 3-6 (about 105 cipher lines) - blocker: not-attempted; not transcribed in this round. The same key should
  apply.
- Unidentified marks - blocker: open-codes; tilde over 33; underline (3 times); small 2 over 7+ (L08) and over
  6 + hook (L20); dot after vowel 2 (L13); code 30. underlined (L18). Proposals from sense only (underline r -> l).
- Guesses - blocker: not-attempted; *Fiesco* (signs: *fiesbo*), *acá llaman* (signs: *a? quilaman*; the blind
  reviewer calls it the weakest guess), *inferiores* (signs: *jn?riores*), *mucho* (signs: *meco*). To be retried on
  the image and against images 3-6.
- The shape "upright 1 + crossed stroke" (L12, L15, L21, L24) - blocker: not-attempted; read 11 in all four places
  after the blind review; it is close to the crossed 4 of this hand. Read as 14, *agora* and *negocio* would need the
  repair *guo* -> *go*, and *algun* and *averiguacion* a repair *guu* -> *gu*. Other words with this shape on
  images 3-6 should settle it.
- Small marks the blind reviewer saw differently - blocker: not-attempted; on L22 a small o-like hook after 8 under
  the cross-bar of the code group `8e†` (same sign class); on L24 the last mark over 18 is a caret with a tail, or a
  bar (RECONCILE.md). Neither changes a word.
- Blind check - blocker: not-attempted; the only blind check is the reviewer's 4 lines (68 signs); no full
  independent blind transcription; no human palaeographer.

## Escalation

- [x] siblings: the other items of catalogue 754 listed; 1414,4 (1581) opened, a later table on which K_P2 does not
  apply as it stands; images 7-8 of 1410,115 (address leaf, docket) opened; the 1410 cipher/decipherment pairs are the
  key's source (targets/perez1578).
- [x] clear-pages: the clear passages of images 1 and 6 read; no decipherment on any image of 1410,115 and none noted
  on PARES.
- [x] known-keys: K_P2 (targets/perez1578), the known key of the 1577 Genoa embassy, applied frozen; no other key of
  this series is in the repository; DECODE was not searched for another Genoa table.
- [x] print: two web searches (12 Nov 2026), no edition found; CODOIN and Memorie digitali liguri not searched in full.
- [ ] key-rebuild: not done; the key was kept frozen for the held-out test, and the proposed values (35 + hook pri,
  underline r -> l) are marked in the reading, not added.
- [ ] retry: not done; the guesses and holes wait for images 3-6.

## Other items of catalogue 754 (not worked in this round)

- EST,LEG,1414,4 (PARES 3549587, Mendoza to Philip II, 7 Jan 1581): 4 images fetched and looked at. Almost all cipher
  (about 60 lines), no decipherment filed. The same family of syllabary (numerals with vowel marks and superscripts) but
  with Latin letters (a, g, n, q, r, s, t, v, y...) as further signs, so a later table; K_P2 does not apply as it
  stands. Its duplicate 1414,8 and the other 1580-1582 originals/duplicates give depth for a ciphertext-only attack on
  that later table. Open.
- The 1571 Padilla letters (1401,41/53/54) and Oviedo (1401,225), 1575 (1405,119), 1576 (1408,159), 1585-1603: not
  opened in this round. The catalogue's toledo1565 lead does not apply: no García de Toledo item remains in this row.

## Access

PARES `catalogo/show/<id>` then `ViewImage.do?accion=42&txt_descarga=1&dbCode=<db>&txt_id_imagen=<n>&txt_zoom=10`,
cookie jar, User-Agent WAINUT-research, one request at a time 6-9 s apart (`../scripts/fetch_pares.py`). 12 Nov 2026:
16 requests in all (1410,115: show + 8 images + description page; 1414,4: show + 4 images), no 429.

Work by AI language-model agents for WAINUT (credit lccompany), from the images.

## Integration check (13 Nov 2026)

- Reproduced exactly: `decrypt.py` (own decoder from `key_frozen.tsv` gives the same text; the file has CRLF line ends), `check_marks.py` (187 words, 173
  verbatim = 92.5%), `heldout.py` (0.970 characters, 0.910 of 122 words; 200 controls at most 0.922 and 0.746), `docs/_check_reading.py` (0.727, 16 of 22
  sentences), `docs/_check_profile.py` (valid). `key_frozen.sha256` matches. The frozen key agrees with `targets/perez1578/key.tsv` (K_P2) except the changes
  the notes name (8 = b, 13 j, 26 fi); perez1578's NOTES confirm 8 = b in the Genoa table.
- The held-out score compares the decryption with the contributor's own reading, so it is not independent of the key; the evidence that counts is that
  the mechanical decryption of 26 lines is fluent Spanish with a key made on other letters.
- Figure: 92.5% verbatim of the transcribed part (the 4 code-group occurrences, 3 distinct groups, are counted verbatim by the contributor; without
  them 169 of 183). Of the whole cipher about 26 of 130 lines are transcribed (fraction 0.19). No page until images 3-6 are read.
- Images not compared: PARES returned 429 to the checking session. The reviewer's 64 of 68 signs is the contributor's.
- One key, one entry: K_P2 is `targets/perez1578`'s key; this is a different document, cross-referenced, no second key page.

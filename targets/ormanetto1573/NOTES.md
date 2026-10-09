# Ormanetto 1573: copy of Philip II's letter to the nuncio, with two cipher passages. READ (key from outside, 1 Oct 2026; measured 98.0%, 5 Oct 2026)

Catalogue item 259 (class C). ASV (AAV), Segreteria di Stato, Spagna 7 (DECODE "i. 1025, doss. 7"), ff. 303r–304r,
address leaf f. 320v. DECODE R116 (Non-decrypted, 2 images + address leaf, transcription by KL, 18 Aug 2020).

**Result (5 Oct 2026): read. 1,298 of 1,324 cipher tokens (98.0%) belong to words read as sense, measured with `measure.py` on the
image-corrected `r116_cipher_v2.txt` (A 97.8%, B 98.4%; strictest variant 95.0%).** Six single-context code groups stay open. The
1 Oct figure (about 90%) was AJ's count of words, not a measure; see "Image re-transcription and measure" below. The two passages are Italian, in the Spain
nunciature's "cifra ordinaria", a key reconstructed by Ajaydas Devadas (AJ) with Claude and sent by email on 1 Oct 2026. The 21 Sept result
(not read, no key, five keys ruled out) is kept below as the history; the reason it failed is in the next section.

## The key (AJ, 1 Oct 2026) and why 21 Sept failed

Homophonic, two signs per letter, no doubled letters, no h, u = v. Zero rule: an undotted 0 closes the digit before it (x0); a dotted 0 opens the
digit after it (0x); every other digit stands alone, dotted or not. **The cross-stroke on 2, 4, 5 (DECODE's "1", the 4/X of the old R118 file) is a
word-end mark.** Everything tried on 21 Sept treated it as a letter or digit, so the polyphonic, pair-parity and homophonic models all read the wrong units.
Nomenclator: a dotted digit + doubled digit (6̇11 tutto, 2̇44 quello), doubled digits (66 che), some two-plain-digit groups (97 officii, 63 Imperatore, 87 non),
lone 3 = et, dotted 5̇2̇2 / 7̇2̇2 = qua / qui. Final nulls: five or six consonant signs. Numbers in plain figures with an overline (15, 19).

| letter | signs | letter | signs | letter | signs |
|---|---|---|---|---|---|
| a | 40, 4̇ | i | 3, 0̇8 | r | 0̇5, 8 |
| b | 4, 0̇2 | l | 80, 2̇ | s | 20, 9̇ |
| c | 50, 7̇ | m | 2, 0̇1 | t | 0̇7, 9 |
| d | 0̇4, 7 | n | 90, 6̇ | u/v | 10, 1̇ |
| e | 60, 5̇ | o | 0̇3, 6 | z | 0̇9 |
| f | 0̇6, 5 | p | 30, 8̇ | g | 7̈ (two dots), 3̇ |

(0̇x = a dotted zero followed by x; x0 = x closed by an undotted zero; a dot over a lone digit is part of the sign.)

## What was checked here (1 Oct 2026)

- `dec_aj.py` rebuilds the decoder from AJ's description and applies it to **our own** `r116_cipher.txt` (DECODE's transcription), without his code.
  Both passages read as Italian: "ho visto il foglio mandatomi a parte sopra le cose di pitigliano ... procuraro quanto sara in me come ho fatto sempre
  che si levi affatto ogni occasione".
- `test_aj.py`: with only the 16 well-supported code groups substituted, 597 letters score −3.02 per letter (`it-modern`, with spaces); the best of 200
  letter-shuffled keys of the same structure scores −6.69 (mean −8.50).
- The same key reads R118 (`../ormanetto1576/`), and the leaf's own decifrato there agrees (lines 1-3 and 5 of the scan compared here).
- Code values are AJ's alone, graded by him: groups 32, 2̇88, 53, 4̇22, 62, 48, 84, 422, 47/93, 3̇22 are guesses or open. Several collide with a letter pair
  or a stroke (35 "lega", 62 "canto"), so they are not adopted here beyond the 16 well-supported ones.
- `make_reveal.py` writes `docs/reveal/ormanetto1573.json` from the same decoder.
- Contamination: the reading came from outside on 1 Oct 2026. No earlier decipherment is known.

## The reading (AJ; passage A = f. 303r, point 4; passage B = f. 304r)

A: "As to making representations to the Emperor my brother to join the new league proposed by His Holiness: I am sending a special envoy to treat of this business,
and I have ordered that the representations I thought fitting be made on this point ... It will be well for His Holiness to do the same on his side, as you say he offers."
B: "I have seen the sheet sent to me separately on the affairs of Pitigliano, and understood in detail everything that has happened, and what His Holiness [decides] should
be done on my part. I so desire the peace and quiet of all Italy and the service of God that I will do all in my power ... to remove every occasion that might disturb it. But nothing has been
learned so far, nor has the Emperor informed me of the state of ..." (the passage ends). Context: Gregory XIII's league against the Turks, which collapsed when Venice made peace in 1573.
Pitigliano (the Orsini county) has not been checked against 1573 sources.

## Image re-transcription and measure (5 Oct 2026)

**How the 0.90 was measured.** It was not: it was AJ's own count of words (112 of 139 non-code words ordinary Italian). Code groups
were left out, nothing was counted per cipher token, and "ordinary Italian" was not checked for sense. `measure.py` now counts every
cipher token (digits and the word-end strokes, 1,324) and credits a stroke-delimited word only if every piece is (a) a letter run that
splits into words attested in Renaissance Italian (`lang/corpora` it-renaissance + it-nunziature, written as the cipher writes: no h, no
doubled letters, u = v; one- and two-letter words from a closed list, three-letter words only if frequent), or (b) a code group with an
adopted value, or (c) the final nulls. Words that a context guess would fill but other words would also fit count as unread. On DECODE's
transcription unchanged it gives 1,248/1,324 (94.3%). Control (`measure_control.py`): 20 shuffled letter keys with the codes kept,
mean 23.0%, max 32.9%.

**Re-transcription.** The two scans were fetched at full resolution (2136x3075, `decode/`, git-ignored) and every unread stretch was
re-read at 3-4x. Changes, in `r116_cipher_v2.txt`:

| place | DECODE | scan | reading |
|---|---|---|---|
| f.303r l.1-2 | 6 0̇ 6 0̇ 7 0̇5 3 | same (dots over both zeros, checked) | writer's slip: one dot moved from 6 0 6̇ to 6 0̇ 6; *entri* ("perche entri nella nuova lega") |
| f.303r l.4-5 | 30 4 0̇5 9 3 7̇ | 4 undotted (a later hand pencilled marks above) | writer's slip 4 for 4̇; *particular* |
| f.303r l.8 | 7 0̇3 2̇ (dol) | a struck sign with a **dotted 7 written above** | 7̇ = c, *col Imperatore* |
| f.303r l.14 | 6 6 4̇ 1 9̇ | the 4 is the stroke-4, no dot over it | *che si oferisce* |
| f.304r l.3 | 3 ?̇ 4 60 | a dotted round sign lost in a paper hole | 0̇ by shape, 0̇4 = d: *desidera* (echoed by *io desidero* two lines on) |

`particolari` + dotted 7 before *tutto quello* (f.304r) is read *particolar[mente]*: Meister p. 265 says a dot marks the nomenclator
sign for *mente*.

**Measure after the re-transcription:** A 739/756 (97.8%), B 559/568 (98.4%), **1,298/1,324 (98.0%)**. Strictest variant, with the
single-context codes 62 *canto*, 48 *essere*, 4̇22 *perche*, 47/93 *tutta* and 3̇22 *Italia* also counted unread: 1,258/1,324 (95.0%).

**Pooling the open codes.** 32, 2̇88, 84, 42 and 53 occur once each in R116 and not in R118's reading (`../ormanetto1576/`); no other
text in this key is known. 3̇22 is *Italia* twice (after 47 and 93, *tutta*), but in *ogni occasione che sia [3̇22] alterarla* the sense
wants *per*; left open.

## Remaining gaps

- 32 and 2̇88 in *se ben dal canto mio l'ho [32] de la buona [2̇88] havuta* (f.303r, 9 tokens) - blocker: open-codes; one context each, not in R118, no key sheet
- 84 and 42 in *sara [84] che S.S.ta [42] dalla parte sua facia il medesimo* (f.303r, 8 tokens) - blocker: open-codes; *bene*/*ancora* fit, but so do other words, so counted unread
- 3̇22 in *che sia [3̇22] alterarla* and 53 before *finora* (f.304r, 9 tokens) - blocker: open-codes; 3̇22 = *Italia* elsewhere, *per* wanted here; 53 reads *fi* as letters (a dittography before *finora*?) or a code

## Escalation

- [x] siblings: R118 (same series) reads with the same key; no other 1573 record on DECODE
- [x] clear-pages: the clear Spanish frame is the King's letter and does not carry the decipherment; no decifrato on the leaves
- [x] known-keys: Lasry 1568, Meister V.8 and VI.1-3 all fail (21 Sept); the "cifra ordinaria" key now fits
- [x] print: Olarra-Larramendi and Carini 1894 are not online; nothing found
- [x] key-rebuild: AJ's key reproduced here; the open codes have no second context
- [x] retry (5 Oct 2026): every unread stretch re-read on the full-resolution scans, five signs corrected (table above); 4̇22, 62, 48, 47/93, 3̇22 adopted from context and recurrence, 84, 42, 32, 2̇88, 53 left open; R118 pooled, none of the open codes occurs there
- [x] measure (5 Oct 2026): `measure.py` per cipher token, attested-word lexicon, shuffled-key control; 98.0% (strictest 95.0%)

## History: 21 Sept 2026 (before the key)

## What the document is

DECODE's catalogue line ("Ormanetto to the nuncio of the Secretariat, 7 Jan 1573") comes from the volume heading
("Nunzio alla Segreteria, dal 7 gennaio 1573 al 31 dic 1573"), not from this item. The leaves hold:

- f. 303r, headed in Italian *Copia della l[ette]ra di S. M.tà al Nuntio*: a clear Spanish copy of Philip II's letter to
  "el obispo de Padua" (Niccolò Ormanetto, nuncio 1572–77). He has been ill and is now up. He will answer the points
  the nuncio raised for His Holiness. Then comes cipher passage **A**, 13 lines of figures (marginal "A." and "H").
  Italian note pasted over the heading: *Della sanità ragguagliata del Re* ("on the King's reported health").
- f. 304r: clear numbered answers. (1) Jurisdiction: already written to Don Juan de Zúñiga, the ambassador in
  Rome. (2) The order for dividing the Turkish slaves in Rome has been sent. (3) The affairs of the bishop of Liège,
  recommended by the Pope. Then cipher passage **B**, 10 lines (marginal "B."). Italian summary at the head:
  *Risposta del Re … 1 sopra la materia di giurisdittione, 2 della ripartitione de' schiavi, 3 de negotii del
  vescovo di Lieggi raccomandato dal papa*.
- Address leaf (DECODE doc 1342, f. 320v): *All'Ill.mo et R.mo S.r mio Col.mo Mons.r Ill.mo Cardinal di Como. A Roma.
  Per servitio di N. S.re*, docketed *73 / a 17 Junii*. So this is the nuncio's despatch to Tolomeo Galli
  (Cardinal of Como, Gregory XIII's secretary of state), received or answered 17 June 1573. The King's letter
  itself is undated in the copy (spring 1573).

The cipher passages are therefore in the nunciature's cipher with Como. The nuncio enciphered the King's
confidential points for Rome, or copied them as the King's office sent them. The plaintext language is not
established: the clear frame is Spanish, the filing notes are Italian.

## The ciphertext

`r116_cipher.txt`, from DECODE's transcription (DOC_R116_D2580) and checked against the images at 2–3× for lines
1–2 of A. There are 1,098 digits in 23 lines: A 756 signs, B 568 (dots and underlines kept; `.` = dot over the digit,
`_` = underlined).

- Digits 0–9 with dots above (0̇ very common: 148; 4̇ 46; 5̇ 36). Many runs are underlined by a later hand.
- A "t"-like cross-stroke, transcribed by DECODE as a digit **1**, joined to the digit before it: 2t, 4t, "st"
  (5t). In the image it is a separate stroke fused to the previous digit, not a bare 1. Before-"1" counts:
  2 74×, 4 59×, 5 51×, others ≤10.
- No word division. Lines are not pair-aligned: second-digit parity is 60/40 at both offsets.
- The same system (dotted digits, barred 4) is on R118, Ormanetto/Clementino 1576–77 (`targets/ormanetto1576/`): two
  samples of one nunciature cipher.

## Keys tried (all fail)

| Key | Source | Result |
|---|---|---|
| Spain nunciature 1568 (Castagna), polyphonic digit = 2 letters, Lasry | `targets/alessandrino1568/decrypt.py` | nonsense (−3.0/item) |
| Crivelli, nuncio in Spain 1561: polyphonic an/so/ti/re…, codes X9/X3/X5 | Meister 1906 p. 259 (V.8) | nonsense (−3.7) |
| "Cifra col cardinal di Como" with Spain nomenclator (Zayas, Idiáquez, card. Deza, Antonio Pérez, Cruzada) | Meister pp. 262–264 (VI.1), `key1.py`, `decrypt.py` | nonsense. Its nomenclator marks (hooked 2, crossed 4/6) resemble the "t" here, but letters with an odd second digit do not parse. The Idiáquez and Deza entries date it after 1578 (Sega). |
| "Cifra col s. card. di Como", nulla 8, *che/chi* 116 | Meister p. 264 (VI.2) | bigram hits 347/1323, no parse |
| Spain–Flanders cipher, nulla 1, even-digit pairs | Meister p. 265 (VI.3) | impossible: 330 odd digits |

Meister VI.2 comes with the rules of "la cifra ordinaria di mons. nuntio di Spagna" (p. 265): null 8 at the end of
each word, a dot over nomenclator groups for *chi, che, qua, que, qui, et, mente*. The ordinary Spain key
itself is not printed. The dots here fit that practice, but the rules alone do not give the table.

## Ciphertext-only attacks (all fail)

- Simple and homophonic substitution over three sign sets (single digits with or without dots; digit + dot +
  underline; "0̇X" and "X t" as units, 31 signs, IC 0.055), Spanish and Italian 4-gram models with a unigram-KL
  penalty (`fa.py`, the Caprile annealer). Control: an Italian text of the same length with 28 homophones comes out
  largely readable. R116 gives nothing readable in any setting.
- Polyphonic digit = two letters (the 1568 family), letter pairs annealed with a Viterbi pass (`polyanneal.py`,
  `pa3.py`). Control: Alessandrino R97, 1,100 digits, recovers 7 of 9 of Lasry's pairs at −2.18/char. R116:
  −2.30 to −2.47, and five restarts give five different keys (`pa_it.txt`, `pa_es.txt`). With 1 as a null and
  0 as a letter digit: −2.36, again unstable.

## What would move it

1. The decifrato of the Como despatch of June 1573. Nunciature ciphers were deciphered in Rome, and the decifrato
   may sit in Spagna 7 near f. 303 or in the Nunziatura di Spagna registers. DECODE has no other record for 1573.
2. The King's minute (AGS Estado, Roma legajos, 1573) or the original letter sent to Ormanetto, if the cipher was
   the King's own. PARES catalogues only Ormanetto items of 1575 (EST,LEG,1407,217/218).
3. Carini, *Mons. Niccolò Ormaneto … nunzio apostolico alla corte di Filippo II* (Rome 1894), which prints
   nunciature documents. Not found online.
4. The key of the ordinary Spain nunciature cipher of 1572–77. Meister prints only its rules. Pooling R116 with R118
   (389 digits) for a second ciphertext-only pass is worth trying once the system is guessed.

## Remaining gaps

- Passage A (756 signs) and passage B (568 signs): unread. Blocker: no-key-material.

## Escalation

Every step open from here was checked, and each is blocked by something outside the ciphertext.

- siblings: DECODE has no other 1570-80 Spain nunciature record except R118 (unread, same system) and R5624
  (Sega 1579, N/A). Done.
- clear-pages: the record's two images and the address leaf are all read. No decifrato is imaged. The rest of
  Spagna 7 is not digitised. Blocker: needs-physical-access (AAV).
- known-keys: five period keys tried (1568 Spain, Crivelli 1561, Meister VI.1-VI.3). Meister prints only the
  rules of the Spain ordinary cipher, not its table. Done.
- print: Carini 1894 is not online (web, archive.org, Google Books). PARES has no 1573 minute. Olarra-Larramendi
  covers Philip III. Blocker: needs-physical-access.
- key-rebuild: homophonic and polyphonic annealers read same-length controls but not R116. The system is not
  identified, so there is no hypothesis left that the text is long enough to test. Blocker: too-short for an
  unknown system.
- pooled with R118 (21 Sept, second pass): 1,660 undotted signs, R116's 4t = R118's barred 4 (X). Polyphonic
  annealer (`pa_pool.py`): -2.37 to -2.46/char against -2.18 for the control, and the restart keys disagree.
  No fit. Only 11 undotted sign types, so plain homophonic substitution over them cannot carry an alphabet.
- academic print search: Fernández Terricabras, "El nuncio Niccolò Ormaneto y la reforma de las órdenes
  religiosas" (Madrid, Felipe II y las ciudades, iii, 2000, pp. 321-332) has no online full text. No edition of the
  1572-77 nunciature registers was found. Blocker: needs-physical-access.
- Tomokiyo (cryptiana: vatican, spanish, spanish2*, spanish3*, spanish4, spanish6): no mention of Ormanetto
  or of this letter. His Philip II general ciphers of 1567-75 (Cg.4-Cg.10) build syllables from a base numeral
  plus a vowel mark. Tested that hypothesis (`syll.py`): digit = letter, dot = + vowel, "t" = + vowel, annealed
  with a KL penalty. Spanish -3.99/char, Italian -3.74, both nonsense. His tables are not printed in full, so the
  royal ciphers themselves cannot be applied.
- retry: nothing read, nothing to regrade.

## Files

- `r116_cipher.txt` the ciphertext; `tok.py` reads DECODE's transcription, `units.py` builds the sign sets.
- `key1.py` + `decrypt.py` Meister VI.1 test; `poly.py` Crivelli test; `polyanneal.py`, `pa3.py` polyphonic
  annealer; `fa.py` homophonic annealer with its control (`CTL=1`).
- `decode/` (git-ignored): DECODE images (`f303r.jpg`, `f304r.jpg` at full resolution, 5 Oct 2026), transcription, statistics, the Meister page scans.
- `r116_cipher_v2.txt` the image-corrected ciphertext; `words.py` splits it at the strokes; `measure.py` the sense measure; `measure_control.py` its shuffled-key control.

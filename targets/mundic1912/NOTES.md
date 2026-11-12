# mundic1912: "Mundic", Mexico, to Luis León de la Barra, Paris, February and March 1912 (catalogue 1463)

WAINUT, 12 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the reading blind from the scans (below).

Read in part, 12 Nov 2026: both telegrams (X-1.3.207.1, X-1.3.239.1) are read in part. Written up on the site
(mundic1912.html) at the integration of PR #466, 12 Nov 2026.

## Documents

| doc | shelfmark | date | form | cipher |
|---|---|---|---|---|
| 207 | CEHM-Carso, Fondo X-1, X-1.3.207.1 (2 images) | 13 Feb 1912 (Paris Bourse stamp) | French received form, Mexico no. 139, 23 words, VIA ANGLO; address "Barradella 42 / M. Luis L. de la Barra / 9 Alfred de Vigny / Paris" | 10 groups, 75 letters, word division kept; signed "mundic" in clear |
| 239 | CEHM-Carso, Fondo X-1, X-1.3.239.1 (2 images) | 15 Mar 1912 (Paris Bourse stamp) | French received form, Mexico no. 103, 18 words, VIA ANGLO | 15 groups of five, 75 letters; "= Mundic" in clear |

Images (direct JPG, no login): http://visor.cehm.org.mx/assets/docx/fondos/jzd/X-1/3/207/1/X-1.3.207.1.0001.jpg
(and .0002), .../X-1/3/239/1/X-1.3.239.1.0001.jpg (and .0002). Catalogue records reached from
https://www.cehm.org.mx/Buscador/FichaBasica/58286?Tipo=A. Scans are not in this folder.

## System

Lower-case monoalphabetic letter substitution of Spanish, the same key in both telegrams. 21 cipher letters seen
(key.tsv). Two cipher letters each stand for two plain letters: n = t and u (situación has both: m-o-n-n-x-z-o-b-w),
u = n (necesario) and w (Wilson). Three single slips, marked in the readings: o = o once (embajador; i in eight other
places), e = l once (vuelvas; d elsewhere), one l missing (resuelvas).

The key sheet in the same fondo, X-1.5.466.1 ("Abecedario y su clave", typed on Secretaría Particular del Presidente
paper, addressed to Lic. Francisco L. de la Barra), is a different key: applied either way it gives no Spanish
(scripts/keysheet_test.py, output in work/keysheet_test.txt).

## Key source

Ciphertext only. No decipherment is on either form and none was found in the fondo or in print. Simulated annealing
over the 150 letters with Spanish 4-gram statistics (two Project Gutenberg texts) gave fragments (considera necesario,
situación incierta tendencia); the word division of 207 finished it by hand (regresar, Wilson, pronto), and each value
was checked on the 2x crops.

## Held-out test

key_frozen.tsv holds only the values needed by telegram 207's reading (19 letters, majority value where there were two).
Applied mechanically to telegram 239 (scripts/heldout.py; line 1 counted by hand because its first letter is marked not
read): **72 of 75 letters right (96.0%), 0 wrong, 3 not in the frozen key** (l twice, t once). The frozen key alone
turns 239 into "?aclaraciones buena impresion situacion incierta tendencia general vivo an?elo de pa?".
Weakness: both telegrams were run together in the first machine solve, so 239 was not unseen in the strict sense.

Statistical check (docs/_validate.py on validation.tsv, 149 read letters, es-modern 4-grams): the reading scores
-2.899 per letter, against -7.18 for random keys of the same structure (z 5.9) and -3.68 at best for a key annealed
onto the shuffled ciphertext (z 6.7). Verdict: pass.

## Reading

- 207 (reading_207.md): "Aplaudo resuelvas regresar. Embajador Wilson considera necesario vuelvas pronto ayudar.
  Mundic." 10 cipher words: 7 verbatim, 3 with a marked one-letter repair, 0 holes. State proposed: **read in part**
  (70% verbatim; every word read).
- 239 (reading_239.md): "[H...] aclaraciones, buena impresión. Situación incierta; tendencia general, vivo anhelo de
  paz. Mundic." 12 cipher words counting the opening h: 11 verbatim, 1 not read. State proposed: **read in part**
  (91.7%).
- Dan's reading checker (docs/_check_reading.py --file, origin/main 4a71baf89) on the normalised sentences:
  reading_207_sentences.txt clean share 0.5 (1 of 2 sentences; flagged words are Wilson, Mundic and modern words not
  in the period word list); reading_239_sentences.txt clean share 1.0 (2 of 2).
- Context: Francisco León de la Barra left the interim presidency in November 1911 and went to Europe; he returned
  in spring 1912. Henry Lane Wilson was US ambassador in Mexico. "Mundic" is not identified.

`python scripts/check_marks.py` rebuilds both decryptions from transcription + key.tsv and fails on any unmarked
departure; it passes.

## Integration check (12 Nov 2026)

Done by the integrating session, not by the contributor. Reproduced: check_marks.py passes; heldout.py gives 58 of 60 on
lines 2-4 (line 1 counted by hand, 72 of 75 in all), 0 wrong. An own decoder written from key_frozen.tsv gives the same
decryption of 239. Own control (lang es-modern, 4-grams, no spaces): the frozen-key decode of 239 scores -2.317 per
letter against -6.91 for 2000 keys with the same plain values shuffled over the cipher letters (best -3.99, z 5.1), so
the key is not an overfit of the short texts. Images X-1.3.207.1.0001 and X-1.3.239.1.0001 were fetched from the CEHM
viewer (no host refused) and compared with the transcriptions: all groups agree at that reading.
Order of events: the freezing of key_frozen.tsv before the 239 count rests on the contributor's record (one commit, no
external timestamp); both telegrams had been solved together first, as the held-out section says. Strict read share by
the README rule (a word with a marked repair or not read counts as not read): 207 7/10 = 70%, 239 11/12 = 91.7%,
together 18/22 = 81.8%. The profile's earlier fraction_read of 1.0 was key coverage and is replaced by 0.818.

## Remaining gaps

- 239: the first letter (h) is not read; it may be the remnant of a word such as "Hechas". - blocker: too-short; one
  letter before "aclaraciones", and nothing on the form decides it.
- 207 L2 g1, 8th letter (o, read with the marked repair Embajad{i/o}r). - blocker: illegible; the independent blind
  review found that the sign may be this hand's b (= o), which would make "embajador" verbatim and remove one repair;
  on a 5x crop it could not be settled, so the repair stays marked.
- 239: "buena" rests on reading the first sign of group 4 as a variant f (pass 1 f, pass 2 t). - blocker: illegible;
  the shape is unusual for this hand; the independent blind review also reads f.
- The three slips in 207 are read from sense, not from a second witness. - blocker: too-short; ten cipher words give
  no second place for any of them (cipher o read as o, not i; cipher e read as l, not d; one l missing).
- t (z) and l (h) rest on one and two occurrences. - blocker: too-short.

Not reading gaps: "Mundic" (the sender) is not identified, and the telegraphic address "Barradella" is read from the
address strip. Pass 2 of both telegrams was made after a first machine solve had been seen; the independent blind
review of 12 Nov 2026 re-read every sign from the scans and agreed in all but the one sign of 207 listed above.

## Prior art (checked 12 Nov 2026)

No decipherment on the forms; the CEHM catalogue records them "En clave" with no translation. Web search
'"Mundic" León de la Barra telegrama 1912 clave' found nothing on these telegrams. The vetting of 2 Nov 2026 (DECODE
harvest, Tomokiyo, Lasry, Narváez 2011/2015/2019/2025 titles) found no edition. Narváez 2019 (SRE book) was not read.
No collision in dbourdeau/cyphersolver (PRs, issues, targets/ and research/ on origin/main, 12 Nov 2026).

## Independent review (12 Nov 2026)

An AI language-model agent that did not take part in the solve read the scans before opening any transcription,
re-ran every script, and read both texts as sentences against the translations. It agreed with the reconciled
transcription in every sign but one (207 L2 g1, 8th letter: o or b, above), reproduced the held-out count (72/75,
0 wrong) and the mark check, and agreed with the states: 207 read in part (grade B: 7 of 10 words verbatim, 3 marked
one-letter repairs, no holes), 239 read in part (grade A: 11 of 12 words verbatim, only the opening h unread). It also
noted a second check on the key: in plain-to-cipher order it shows regular runs (abc -> xyz, de -> ef, gh -> kl,
ij -> op, mn -> vw, op -> bc, st -> mn, yz -> st), which points to a structured key alphabet, not an overfit one.
Its grades are recorded as `reading_review` in profile.json.

## Escalation

- [x] siblings: the other items of catalogue 1463 opened: X-1.4.310.1 (1913, a different key, target delabarra1913),
  X-1.4.380.1 (clear), X-1.1.94.1 (clear letter with person numbers, seen at the 2 Nov vetting; its key is not in the
  file), and the key sheet X-1.5.466.1.
- [x] clear-pages: both forms and their address strips checked; no decipherment is written on either.
- [x] known-keys: the fondo's key sheet X-1.5.466.1 tested in both directions (scripts/keysheet_test.py): not this key;
  the 1913 key of X-1.4.310.1 differs as well.
- [x] print: two web searches (12 Nov 2026) and the vetting of 2 Nov 2026 (DECODE, Tomokiyo, Lasry, Narváez titles);
  no edition found. Narváez 2019 not read.
- [x] key-rebuild: every cipher letter of both telegrams has a value (key.tsv), from annealing and by hand.
- [x] retry: every doubtful sign re-checked on 2x-5x crops, by the solver and again blind by the reviewer; the gaps
  left have the blockers listed above.

## Files

transcription_<doc>.txt (+ _pass1, _pass2), decryption_<doc>.txt, reading_<doc>.md, reading_<doc>_sentences.txt,
translation_<doc>.md, key.tsv, key_frozen.tsv, validation.tsv (cipher letter and reading pairs for docs/_validate.py),
scripts/ (decrypt.py, check_marks.py, heldout.py, keysheet_test.py), work/ (sa.py and saw.py, the annealing solvers,
which need two Project Gutenberg Spanish texts, pg2000 and pg15532, not included; keysheet_test.txt).

AI language-model agents (WAINUT) did the transcription, solve and reading; no human palaeographer checked it.

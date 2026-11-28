# dieguez1914: Gral. M. M. Diéguez, Guadalajara, to the Governor of Chihuahua, July 1914 (catalogue 1462)

AI agents (Claude Opus 5.5) did all of this work, on 25 Nov 2026 (transcription, key, first count, blind second
reading) and 27 Nov 2026 (third blind reading of the groups, recount, this folder). No person has checked the
transcription, the key or the reading against the images. Times are local file times (EST); the order of the work
rests on our own record.

**This is the other half of the maintainers' follow-up in `targets/villa1914`.** On 26 Nov 2026 Daniel Bourdeau set
villa1914 to "in progress" (commit a64929ac6c), naming this telegram and CMXV.35.3492.2-3 as its next step, to test
Ashton Allen's March and June keys on them and fix groups 33, 37, 69 and 99. The answer for this telegram: it is in
another key, so it cannot settle those groups (see "Bearing on villa1914" below).

## Result

- **Read in part: 19 of 33 cipher words (0.576), with a key rebuilt from a clear copy of the time.** A twentieth word,
  Corrua, is spelt by the key only with 49 = rr. The blind reader had r there, and the copy does not settle it (it
  spells Corrua with rr, but contrarevolución with one r where the cipher has 49), so Corrua is counted as a hole. If
  49 = rr is accepted, 20 of 33 (0.606). The class is "read in part" either way.
- **Method: key recovered based on adjacent plaintext.** The next item in the file, CMXV.35.3433.2-2, is a clear
  manuscript copy of the message, dated Guadalajara 22 July 1914 and initialled M. M. D. The key was rebuilt by laying
  the coded runs against it. A word counts as read when the key's output for its groups, unedited, spells it: the
  copy's word (17 words) or, where the copy has nothing there, the Spanish word
  the groups spell (2 words, "a" and "los"). Every word with one wrong group, a group with no value, or the code 121
  is a hole (README Conventions, 19 Nov 2026).
- **No held-out test.** No other telegram in this key has been found (CEHM records 13000-13420 checked on 25-26 Nov),
  so the key is not validated on any other text. The one-digit slip rule does not apply, as the key is rebuilt here.
- **Earlier tests missed.** In a plan frozen on 25 Nov 2026 at 19:18:47 EST (filed as `plan/PLAN_2026-11-25.md` in
  `targets/ornelas1914`, pull request #1032) and run once at 19:28 EST, nine existing keys (14 variants) were tried on
  this telegram: Allen's 1914 key, Clave No. 0, the fonds' grids and alphabets and the syllabary card. All missed
  (agreement with the copy 0.000-0.072). The plan's own rebuild step (T1-R, a table from the copy-aligned runs) also
  missed: it found 13 groups given two or more letters, so no key was formed (`plan/plan_run_2026-11-25.txt` there).
  The grid key here was built after the plan, from runs 0, 1, 9 and 10 of the copy. The plan declares that the clear
  copy had been opened and read before it was frozen. The order of plan, run and rebuild rests on local file times
  only; there is no external timestamp.

## The telegram

- CEHM-Carso, Fondo CMXV (Archivo Federico González Garza), CMXV.35.3433.1-2 (catalogue record 13235, "EN CLAVE"),
  two "Telégrafos Nacionales" forms, Num. 3, from Guadalajara, received at Chihuahua; addressed "Gobernador del
  Estado" [Fidel Ávila]. The day on the form is written 2-something; the copy has 22 July 1914 (villa1914 gives 27 Jul).
  Images: [0001](https://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/35/3433/1-2/CMXV.35.3433.1-2.0001.jpg),
  [0002](https://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/35/3433/1-2/CMXV.35.3433.1-2.0002.jpg);
  record https://www.cehm.org.mx/Buscador/FichaBasica/13235?Tipo=A.
- Clear copy CMXV.35.3433.2-2 (two images, same folder, `.../3433/2-2/CMXV.35.3433.2-2.0001.jpg` and `0002.jpg`); its
  catalogue record was not found (13233-13237 checked).
- 211 groups (209 two-figure, two of 121) on 20 lines, with clear words between them (Ayer, por, favor, habiéndose,
  recogiéndoseles más de cien armas con bastante parque así como, que, como, de la, el director, ha sido, con,
  enérgica) and a clear close "Salúdolo. El Gral. M. M. Diéguez". A pencil note above line 1 in another hand
  ("para armas y ...") was not read with confidence.
- **What it says** (reading and translation in this folder): a clerical plot in favour of counter-revolution, under the
  motto "Religión y Fueros", was discovered the day before; priests were arrested, more than a hundred weapons and
  ammunition taken, with documents naming them as the promoters; the director, the priest Antonio Corrua, has been
  arrested; Diéguez will punish those responsible.

## The key

`key.tsv`. A 3 x 10 grid: the units figure gives the column and the tens figure the row; each row has two tens
figures, used at will. Tens 8/9 = a..j, 6/7 = k..r (with ll and ñ), 4/5 = rr..z; each row runs right to left, its first
letter on units 0. 121 = -ción, from the copy only. 39 grid cells are used.

- This is the layout of Clave Extra 3 (`targets/murguia1914`, and carranza1914, fuentes1914), with another split of the
  alphabet and other tens figures (Clave Extra 3: tens 1/2 = a..j, 3/4 = l..rr, 5/6 = s..z, and word groups in 7x-9x).
  It is not the same key, so under one key per target it is a new target, not an addition to murguia1914.
- The blind second reader (below) rebuilt the same grid on its own. It put r, q on 49/59 and 40/50 where this key has
  rr and no value. With rr the groups spell the copy's "Corrua" and the standard "contrarrevolución"; with r, "Corua"
  and the copy's own spelling "contrarevolución". The copy therefore does not settle it. The layout favours rr (r is
  already 61/71, and rr..z fills the third row), but that is the model, not a witness, so Corrua is counted as a hole.
- A scan of every key file under `targets/` on origin/main 7d5fc3415d (27 Nov 2026; `scripts/compare_keys.py`) found
  none that agrees with this key on more than 3 of the groups they share (3 of 58, two synthetic control keys in
  `targets/sp53`). Clave Extra 3 (murguia1914) agrees on 0 of 28, Allen's villa1914 key on 0 of 14-16.

## Bearing on villa1914

None. Allen's March and June keys (`targets/villa1914/key.tsv`) give 96 = A, 92 = E, 99 = C or CH and 69 = CH. Here
96 = e, 92 = i, 99 = b and 69 = l, and the copy confirms each. Groups 33 and 37 do not occur in this telegram (no group
has tens figure 1, 2 or 3 except the strays 10 and 16). The frozen run of 25 Nov had already found that Allen's key
gives no reading here. The other sibling, CMXV.35.3492.2-3 (Ornelas), reads in the fonds' syllabary card
(`targets/ornelas1914`). So neither sibling fixes groups 33, 37, 69 or 99; a missed test does not rule Allen's key out
for other telegrams.

## "fraguado" or "Irapuato"

The copy reads "plan Ira-|puato", and the CEHM subject ("Plan Irapuato promovido por el clero") follows it. The
telegram's eight groups are 95 61 90 84 50 80 97 74, which the key reads f r a g [50] a d o.

- Irapuato would need i (82/92) for 95, p (63/73) for 84, u (46/56) for 50, and t (47/57) for 97.
- 95 and 84 are read the same by all three transcriptions, and the third reader, given only line crops and no key,
  marked both "sure". 95 = f is also the f of "fueros" in the same column; 84 = g has 94 = g in castigaré and religión.
- 50 is read 50 by the third reader ("sure") and by the first; the second first wrote 80 and then, enlarged, 50. It has
  no value: neither u nor anything in Irapuato.
- 97 is doubtful on the image: 97 to the first reader's pass B and the blind reader, "17, 47 or 97" to pass A, and 17
  (47 or 97 not excluded) to the third reader. With 47 the groups end -ato.
- So the telegram has "plan frag?a?o por clero", most probably "plan fraguado por clero", where the copy has "plan
  Irapuato por clero". It is a hole in the count either way, written `{frag[u]ado}`. Irapuato fits at most four of the
  eight groups (r, a, a, o, and t if 97 is 47); fraguado fits six or seven.
- Why they differ is not known. A person should look at groups 95, 84, 50 and 97 on image 0001, line 2, last five
  groups.

## Count

`words_CMXV.35.3433.1-2.tsv`, from `scripts/decrypt.py`. 33 cipher words:

- **Read (19):** plan, clero, en, bajo, fueros, a (not in the copy), a, los, curas, documentos, los (not in the copy),
  los, promotores, del, cura, aprehendido, castigaré, mano, los.
- **Holes (14):** Corrua (49 = rr or r, not settled by the copy; above), descubriose (94 for e), fraguado/Irapuato (above), contrarrevolución twice (97 for t, 10 and 88 for
  re; and 121 each time), lema (47 81 for m a), religión (46 for n), y (the cipher has 85 46, f u), procedido (16),
  aprehender (43 for p), denuncian (98 for e), movimiento (41 for v, 87 for i, no group for n), Antonio (84 for o),
  responsables (41 for r, no group for the first s, 80 66 for l e).
- The stray group 80 after Corrua is not counted as a word.
- **Against the first count of 25 Nov (16 of 31):** "Corrua" was a hole then because the copy had been transcribed
  "Correa"; the image reads Corrua (the blind reader read Corrua on 25 Nov; checked again 27 Nov). It stays a hole,
  now because of 49. "y
  fueros" is now two words, the f u in place of y a hole and fueros read. The cipher's "a" before aprehender and "los"
  after denuncian were holes as "not in the copy"; they are now read, as the key gives them with nothing supplied.

## The wrong groups

About 19 of 211 groups give a letter the sense does not want (listed in the word list). They are not transcription
slips here: three readers agree on them (below). The blind reader noticed that six become right if one tens figure is
swapped 4/6 or 1/9 (94 -> 96 e, 47 -> 67 m, 46 -> 66 n, 16 -> 96 e, 43 -> 63 p, 41 -> 61 r), pairs whose Morse signs
are mirror images. That was noticed after the reading and is not tested; the rest have no single explanation. None is
emended in the count.

## Transcription doubts

- 97 (p1 line 2, group 14, in fraguado) - read: 97; checked: image, decode, transcription; pass A ?7 (17, 47 or 97), pass B 97, blind reader 2: 97, blind reader 3: 17 (47, 97 not excluded); a hole either way.
- 50 (p1 line 2, group 12, in fraguado) - read: 50; checked: image, decode, transcription; blind reader 2 wrote 80 and, enlarged, favoured 50; blind reader 3: 50, sure; no value in the key either way.
- 80 (p1 line 2, group 13, in fraguado) - read: 80; checked: image, decode, transcription; blind reader 3 unsure (10 or 60 not excluded): the first figure is a long slanted 8 as in this hand's 58.
- 66 (p1 line 4, group 1, in contrarevolución) - read: 66; checked: image, decode, transcription; retraced; blind reader 3 read 64 (66 not excluded); the word is a hole either way.
- 74 (p1 line 2, group 1; p1 line 3, group 1) - read: 74; checked: image, decode, transcription; the 4 is written over another figure; blind reader 2 marked the second with a query; o fits both places.
- 58 (p1 line 1, group 3; p1 line 13, group 3; p2 line 6, group 10) - read: 58; checked: image, decode, transcription; the 8 is a tall loop; s fits each place.
- 99 (p2 line 6, group 7) - read: 99; checked: image, decode, transcription; a stroke from the line above crosses it; blind reader 3: 99 (49 not excluded); b fits responsables.
- 83 (p2 line 3, group 12) - read: 83; checked: image, decode, transcription; second figure small; h fits aprehendido.

## Remaining gaps

- descubriose, religión, procedido, aprehender, denuncian, Antonio (one wrong group each) - blocker: no-key-material; three readers agree on the groups; the key is rebuilt, so the one-digit slip rule does not apply, and no period key or other telegram in this key has been found.
- contrarrevolución (twice), lema, movimiento, responsables, y (two or more wrong or missing groups, or the code 121) - blocker: no-key-material; 121 = ción comes from the copy only; no key sheet found.
- Corrua (98 64 49 56 90) - blocker: no-key-material; 49 is rr in this key and r to the blind reader, and the copy
  supports each once; only another text in this key would settle it.
- fraguado / Irapuato (95 61 90 84 50 80 97 74) - blocker: illegible; 50 has no value and 97 may be 17 or 47 on the image; the copy's word does not fit 95 or 84; no person has looked.
- the key itself - blocker: no-key-material; rebuilt from the copy of this one telegram and not tested on any other text.

## Escalation

- [x] siblings: 3433.2-2 (the clear copy) used; 3492.2-3 (Ornelas) is in another system (`targets/ornelas1914`); 1914 telegrams with coded text in CEHM records 13000-13420 checked on 25-26 Nov (33.3233.1, 33.3231.1-2, 33.3231.2-2, 31.3079.1, 35.3464.1): none in this key. Not searched: CMXV after record 13420, and other fonds with Diéguez telegrams.
- [x] clear-pages: the clear copy is the source of the key; the pencil note above line 1 was not read with confidence.
- [x] known-keys: Clave Extra 3 (murguia1914) has the same layout but another key; Allen's 1914 key, Clave No. 0, the CMXV.16.1557.1 grids, alphabets and syllabary card all missed in the frozen run of 25 Nov; every `targets/*/key*.tsv` on origin/main scanned, none agrees.
- [x] print: no edition known. Narváez 2019 (*Criptografía diplomática, política y militar en México*, searched in the OCR of our own photographs of the book, 27 Nov 2026) names neither Diéguez nor Irapuato. Narváez 2025 ("Algunos casos criptográficos del movimiento constitucionalista, 1914-1915") not read.
- [x] key-rebuild: the grid filled from the copy, then rebuilt blind by a second reader (same grid except 40/49/50/59).
- [x] retry: every wrong group re-read on the image by a third, blind reader (27 Nov 2026); none was a misreading.

## Readers and checks

- **First reader** (Claude Opus 5.5, 25 Nov 2026, about 19:00-19:41 EST): two passes, the second from fresh crops; 210
  of 211 agree, the one difference settled on the image (97). The key and the first count (16 of 31).
- **Blind reader 2** (Claude Opus 5.5, own session, 25 Nov 2026, 20:10-20:33 EST), given only the four images (telegram
  and copy): 209 of 211 groups agree; the same grid; it reads the copy's name as Corrua. Its transcription is
  `transcription/groups_CMXV.35.3433.1-2_blind2.tsv`.
- **Blind reader 3, the reading review** (Claude Opus 5.5, own session, 27 Nov 2026, 22:58-23:02 EST), given only 40
  crops of the telegram's lines, told nothing of the key, the copy or any reading, and asked to read the marks only:
  209 of 211 agree (`transcription/groups_CMXV.35.3433.1-2_blind3.tsv`). The two differences are listed above.
- `python targets/dieguez1914/scripts/compare_readings.py` prints these comparisons.
- **Statistical validation** (`python docs/_validate.py dieguez1914`, 27 Nov 2026, model es-modern; the corpus texts
  were fetched from the gutenberg.pglaf.org mirror, as gutenberg.org answered 503): 208 read tokens, 40 types; the key's
  output scores -2.668 per letter, random keys -6.658 (z 9.5), keys annealed onto shuffled groups at best -3.347
  (z 18.6). Verdict: pass. This shows the key's output is Spanish-like beyond what a fitted key gives; it is not a
  held-out test, since the key was rebuilt from this telegram's own copy.

## Files

| file | what |
|---|---|
| `transcription/groups_CMXV.35.3433.1-2.tsv` | the settled transcription, one group per row, clear words in place |
| `transcription/groups_CMXV.35.3433.1-2_blind2.tsv`, `_blind3.tsv` | the two blind transcriptions |
| `transcription/clearcopy_CMXV.35.3433.2-2.txt` | the clear copy of the time (not a decryption) |
| `key.tsv` | the key, with the source of each value |
| `decryption_CMXV.35.3433.1-2.txt` | the key applied to the groups, unedited |
| `reading_CMXV.35.3433.1-2.md`, `translation_CMXV.35.3433.1-2.md` | the reading with its marks, and English |
| `words_CMXV.35.3433.1-2.tsv` | each cipher word, its groups and how it is counted |
| `validation.tsv` | group and key output, for `docs/_validate.py` |
| `scripts/decrypt.py` | writes the decryption, the word list and validation.tsv; `--key49 r` uses the blind reader's 49 = r (same count) |
| `scripts/compare_readings.py` | compares the three transcriptions |
| `scripts/compare_keys.py` | compares `key.tsv` with every key file under `targets/` (`python targets/dieguez1914/scripts/compare_keys.py origin/main`) |

No images are in the folder. The CEHM viewer images are free to view and marked "Todos los Derechos Reservados".

## Credits

Andrew Beling (ajbeling), with AI agents: transcription, key, reading. Daniel Bourdeau named this telegram as the
villa1914 follow-up (commit a64929ac6c, issue #845) and listed catalogue 1462. Ashton Allen's villa1914 readings
are the context for the sibling check; his key was tested here and does not fit.

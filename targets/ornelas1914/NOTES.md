# ornelas1914: Gral. Tomás Ornelas to Federico González Garza, Ciudad Juárez, 24 August 1914 (catalogue 1462)

AI agents (Claude Opus 5.5) did all of this work on 25 Nov 2026 (the frozen run's scripts were added and rerun, and the
ink line at the foot was read again, on 27 Nov 2026); no person has checked the transcription, the key or
the reading against the images. Every time below is a local file time (EST) and rests on that alone: the order of the
plans, the runs and the readings rests on local file times only, with no external timestamp.

**This answers the maintainers' follow-up in `targets/villa1914`.** On 26 Nov 2026, the day after this work, Daniel
Bourdeau set villa1914 to "in progress" (commit a64929ac6c), with the transcription of this telegram and of
CMXV.35.3433.1-2 as its next step, to test the March and June keys and fix groups 33, 37, 69 and 99. His closing
comment on issue #845 (Ashton Allen's, 26 Nov 2026) says the same. For this telegram the answer is in result 1 and in
"Ashton Allen's key on this telegram" below: Allen's published key and a model built from it gave no reading here
(W 0.115 and 0.106), and the telegram reads instead in the fonds' syllabary card, a different system. So it probably
cannot settle those four groups. Allen's villa1914 readings are the context for that test, and the credit for the key
tested is his.

## Result

**Registered results first.**

1. **The frozen test of the card missed.** A plan frozen by hash at 19:18:47 (`plan/PLAN_2026-11-25.md`, SHA-256
   `0d8e81fd…bb841`) tried 16 key variants on this telegram in a fixed order: Allen's key; a model of it, alone and
   with the División del Norte card in both directions; Clave No. 0; the two Antero grids; the reyistas grid; the two
   typed alphabets; and this card, each read both ways where that applies (`plan/plan_run_2026-11-25.txt`). No
   variant met the fit rule (lexicon coverage W >= 0.80 and above all 1,000 permuted keys). The syllabary card read
   row digit then column digit came closest: W 0.969 against a control maximum of 0.980. Plan step T2-P (the ink line
   at the foot as a letter crib) gave no consistent position; step T2-S (a hill-climb) was not run, a departure.
2. **The held-out test missed.** A second plan (`plan/PLAN_2026-11-26.md`, frozen 20:36:45, SHA-256
   `8b024c74…12330`) named three 1914 telegrams of the fonds with coded text, found in the CEHM catalogue before their
   images were opened. Two are in two-digit groups. CMXV.33.3233.1 (Silvestre Terrazas to Fidel Ávila, 11 May 1914)
   has a decipherment of the time; the card gives nonsense on it (A = −1.455, where A is the held-out plan's character agreement with the period decipherment, 1 minus the edit
   distance over the decipherment's length; the rule needed 0.80;
   `scripts/heldout_test.py`). CMXV.33.3231.2-2 (Villa to Ávila, 16 May 1914) has no period text, so it could not be
   measured; the card gives no Spanish on it. The third, CMXV.31.3079.1, is in letters. As the plan said, this miss is
   reported first and **lowers the standing of the reading: no other telegram has been found in this card.** After
   the plan we noticed that 3233.1 has one group per letter of its period text (24 groups for *se encargará Ud. del
   Gobierno*), and that a letter key rebuilt from it after the plan has no conflict
   (`scripts/after_plan_terrazas_key.py`). That suggests it uses another system, but this was noticed after the test.

**After the first plan**, the card applied unchanged gives one grammatical message:

> Se rumora por aquí, y la prensa también lo dice, que biene a ésta mi general Billa. Sir{va}se informarme lo que
> aya de cierto. *Salúdolo afecte. Gral. J. de A. T. Ornelas.*
>
> It is rumoured here, and the press says so too, that my general Villa is coming to this place. Please let me
> know what truth there is in it. Affectionate greetings. General Tomás Ornelas, Jefe de las Armas.

- **Count, cipher words only:** 24. *biene* (viene), *Billa* (Villa) and *aya* (haya) are read as written: the card
  has no v, h or ll cell, so the writer could not spell them otherwise. No letter is supplied for them. *sírvase* is a
  hole: the key gives *si r ra se*, and 46 (*ra*) stands where *va* is wanted. That gives **23 of 24 (0.958)**. If
  *aya* is also taken as a hole, as the first reader (in its working notes of 25 Nov) and the blind reader did, it is 22 of 24 (0.917).
  **The entry is marked read under the short-text floor** (README Conventions, 19 Nov 2026: a document of fewer than 40
  cipher words is read when it has at most 2 holes); it meets the floor either way. Both planned tests missed (above),
  and the card was found by testing 16 variants, so the class rests on the decode itself, not on a test.
  `scripts/decrypt.py` rebuilds the decryption and the count.
- **Method:** read after matching with key from external sources. The card was not tied to this telegram: it is unheaded,
  filed in another legajo that the CEHM dates 1911, and was found to fit by testing 16 key variants. The key is a typed card of the time in the same fonds (CMXV.16.1557.1 image 0003)
  with no heading, date or name. It is used unchanged, in Daniel Jalkut's transcription
  (`targets/duron1911/siblings/syl.py`). A blind AI reader's own transcription of the card agrees on all 100 cells
  (`key.tsv`).
- **What the reading rests on:** the decode itself. 61 groups, used unchanged, give 24 Spanish words in order. They
  form one grammatical message that fits its date, sender and place, with one wrong group. The best-scoring permuted
  cards give word salad (`scripts/measures.py --controls`). No statistic separates the card from permuted cards (see
  Controls). **With a fresh control draw, the card does meet the first plan's rule (W 0.9691 against a maximum of
  0.9688), so the registered miss turns on the control draw.**
- **The ink line at the foot.** It is in another hand: "¿Ez cierto que viene ésta mi general Avila?". Three AI readers
  read the last word *Avila*: the first reader, the cold reviewer, and on 27 Nov a fresh reader given only the line
  and the image (Transcription doubts). The blind reader read *Villa*, but it read the line after its own decode. The
  word reads *Avila*: Fidel Ávila, governor of Chihuahua (the reply 3492.1-3 is about the governor's health). The line
  then agrees with the decode in wording but differs at the name, so it is not a decipherment of the groups. No
  person has read it on the image.
- **What was seen before the first plan** (declared in it): the images of the telegram and of 3492.1-3, the reply,
  were read; the ink line was glimpsed and read as "...mi general Ávila"; and all 31 key scans were seen as
  thumbnails.

## The telegram

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo CMXV, Archivo Federico González
Garza, **CMXV.35.3492.2-3** (record 13262, "2-3. EN CLAVE. Telégrafos Nacionales. Dirigido a Federico González
Garza"), one image. It is a Telégrafos Nacionales form, Mod. C.-2:
- Núm. 16, from C. Juárez, 24 August 1914, received at Chihuahua; handed in 11.15, received 12.16.
- To Lic. F. González Garza, Palacio de Gobierno.
- 61 two-digit groups in pencil, with check marks over nearly every group.
- In clear: "Saludolo afecte." and the signature "Gral J de A T. Ornelas".

Tomás Ornelas was then Jefe de las Armas at Ciudad Juárez. González Garza was in Chihuahua with Governor Fidel
Ávila. The other two items of the folder are:
- 3492.1-3 (record 13261): González Garza's clear reply to Ornelas the same day, about the governor's health.
- 3492.3-3 (record 13263): a clear telegram from Torreón.

## The key

`key.tsv` is a 10 x 10 card. The rows are labelled 1 3 5 7 9 0 2 4 6 8 down the left, the columns 1-0 across the
top. Single letters are typed in red, syllables and short words in violet (a, able, accion, ado ... ya, yo, z). The
card has no h, k, v or ll, and no plain q (only *que*, *qui*). A group is read row digit, then column digit.

The card is filed among the 21 key sheets of CMXV.16.1557.1, which the CEHM dates "[El Paso, Texas, 1911]". The
folder also holds a 1914 División del Norte card of the Jefatura de Armas, Ciudad Juárez, signed F. A. Sommerfeld.
**Whose card this was, and when it was made, is not known.**

## Method and order of events (local file times, EST, 25 Nov 2026)

1. **Checks before any work.** Catalogue 1462's `_claims` entry, open issues and pull requests (none on 3492), and our
   own files were checked. Daniel Jalkut tried this card on CMXV.34.3344.1 (to Villa, 1914) on 20 Nov and found no
   reading. That telegram is in Ashton Allen's key.
2. **Images fetched:** the telegram at 19:07:12, the card at 19:08:00, the reply 3492.1-3 at 19:13:38.
3. **First plan.** The plan file was written at 19:18:44 and its hash recorded at 19:18:47. Its header says
   "19:20-19:45"; that was written in advance and is wrong. In the package the files are renamed: `PLAN.md` became
   `plan/PLAN_2026-11-25.md`, and `PLAN.sha256` became `plan/PLAN_2026-11-25.sha256`. The hash line inside the
   `.sha256` file still names `PLAN.md`.
4. **Transcription, twice, by one agent.** Pass A was saved at 19:20:21. Pass B was made from fresh crops without
   opening A and saved at 19:23:48. All 61 groups agree. The two passes are not blind.
5. **The plan run.** The run of 19:28:06 is the registered one. `plan/plan_run_2026-11-25.txt` is that run's output.
   It was rerun at 19:36 with the same figures, and the file's own time is 19:37:19. Its SHA-256,
   `28c4ba14…10fa`, is the value recorded for the original output, but the file time alone cannot show that the kept
   file is the 19:28 run.
   - The run's script is `scripts/run_plan.py`, with `scripts/common.py`, added on 27 Nov 2026. Its inputs are the key
     transcriptions in `plan/frozen_run/keys/`, the settled transcriptions in `plan/frozen_run/transcription/`, and
     keys already in the repository (`targets/duron1911/siblings/syl.py` and four other 1911 targets' key files, named
     in `common.py`).
   - Ashton Allen's key file is not copied, because his repository states no licence. The script reads it at run time
     from the path in `ALLEN_JSON` (his `decode-result.json` at commit 0dc067a460fc66a9e36eb6c796ab7a4ba86d4779).
   - The other telegrams of the run (T1 and T4-T6 in the script) are in `plan/frozen_run/transcription/` only so that
     the run can be repeated whole. They are a record of work and are not part of this entry. The Diéguez telegram
     CMXV.35.3433.1-2 (T1) is the maintainers' own follow-up in villa1914.
   - Rerun twice on 27 Nov 2026 (about 22:00 EST) on the repository's main branch of that day: the output equals
     `plan/plan_run_2026-11-25.txt` byte for byte except lines 31 and 33 (both T1). There the elements inside Python
     sets print in a different order, which changes with Python's hash seed from run to run; every figure is the same.
   - `scripts/measures.py` rebuilds the card's own rows.
6. **After the plan,** 19:30-19:45. The card's decode was read as Spanish, and the statistic S was computed (file
   19:32:47).
7. **Blind second reading,** files at 19:45:47. A separate AI agent (Claude Opus 5.5, its own session) was given only
   the telegram image and the card image, and was told not to open the work.
   - Its transcription agrees with ours on 61 of 61 groups (`transcription_CMXV.35.3492.2-3_blind.txt`).
   - Its own card agrees on 100 of 100 cells.
   - Its decode gives the same Spanish (`blind_decode_CMXV.35.3492.2-3.txt`).
   - It puts the wrong group in *sírvase* at 45 (*r*) rather than 46 (*ra*). Either way one letter is wrong (r for v).
   - It counts *aya* as a hole: 22 of 24.
8. **Held-out test.**
   - The plan was frozen at 20:36:45.
   - The eight images of the four items were fetched from 20:36:52 to 20:37:07.
   - The groups and the period text of 3233.1 were transcribed. Both files and their hashes (`heldout/HASHES.txt`) all
     carry the time 20:38:01, so the order the plan asked for (groups hashed first) cannot be shown.
   - The test was run at 20:38:25.
   - Later, after the test: the groups of the two Villa telegrams of 3231 were transcribed once
     (`heldout/Hb_3231_groups.tsv`) and decoded with the card (`scripts/heldout_test.py`, last two lines).
9. **Cold review,** 20:53-21:04: an AI agent (Claude Opus 5.5) that built none of this re-read the 61 groups and the
   card from the images before opening the folder. It reported agreement on 61 of 61 groups and 100 of 100 cells. Its
   own transcription was not saved, so no file is behind those two figures; they are given as it reported them. It
   reran the scripts and listed the corrections that are made here.

## Ashton Allen's key on this telegram

In the frozen run (`plan/plan_run_2026-11-25.txt`, section T2), Allen's published key at commit 0dc067a (his
`verified_key`, 53 values) and a 30-letter alphabet model formed from his values before any group of this telegram was
decoded were the first two of the 16 variants:

| Variant | W | control maximum | groups with no value |
|---|---|---|---|
| K-ALLEN, his key as published | 0.115 | 0.328 | 27 of 61 |
| K-ALLEN-X, the alphabet model | 0.106 | 0.328 | 21 of 61 |
| K-ALLEN-X with the División del Norte card, each direction | 0.030, 0.045 | 0.292, 0.242 | 29, 26 of 61 |

Neither gave any Spanish. A missed test does not rule his key out for other telegrams, but this telegram reads in the
syllabary card instead (above), so it is in a different system and probably cannot fix groups 33, 37, 69 and 99 of
villa1914. CMXV.35.3433.1-2 was also in the frozen run (T1). Its settled transcription and its clear copy 3433.2-2 are in
`plan/frozen_run/transcription/` as run inputs only; no reading of it is claimed. The clear copy is dated 22 July 1914;
villa1914 gives 27 Jul.

## Controls (scripts/measures.py; two reruns on 25 Nov give the same lines)

| Measure | Card | 1,000 permuted cards | Note |
|---|---|---|---|
| W, the plan's measure (lexicon coverage) | 0.9691 | max 0.9688, mean 0.867 (frozen run: max 0.980) | See note 1 |
| S, chosen after the plan run (frequency-weighted segmentation score) | 2.765 | max 2.894, mean 1.997; 3 of 1,000 at or above the card | After the plan, so a check only. It does not separate the card |

1. The frozen run drew this card's controls late in one seeded stream shared with the other 15 variants. The fresh
   draw here puts the card just above every control, which would meet the rule. Permuted syllables also join into
   dictionary words, so the measure does not separate the card either way.

The three best controls under S, segmented, are word salad ("senor ente don ore tras P tras mi tu seal pro era ...").
**Neither statistic rules the card in or out.**

## Remaining gaps

- sírvase (63 45 46 61) - blocker: too-short; group 46 (ra) stands where va is wanted; the card has no va (the writer would need 31 b + 11 a); it occurs once, and no other telegram in this card is known.
- the ink line's last word (not a cipher word), read Avila - blocker: illegible; three AI readers read Avila and one Villa (after its own decode); the fresh reader of 27 Nov 2026, not told any reading, read Avila and did not list Villa among the readings it could not exclude; no person has read it on the image.
- no measure separates the card from permuted cards on 61 groups - blocker: too-short; permuted syllables also join into dictionary words.

## Transcription doubts

The blind reader's file and the frozen plans name local folders (`sources/raw/`, `output/`): these are the
contributor's local copies and work folders, not in the repository. The image links are under Access and conditions.


- 28 (L1 group 7) - read: 28 = por; checked: image, decode, transcription; the second digit could be 3 (23 = osa, which does not fit); the blind reader and the cold reviewer also have 28.
- 33 (L5 group 1, group 57) - read: 33 = c; checked: image, decode, transcription; the blind reader saw the first 3 partly formed or overwritten by a tick (3, perhaps 5: 53 = di, which does not fit cierto); the first reader's two passes have 33, and the cold reviewer reported 61 of 61 in agreement.
- 63 (L3 group 14) - read: 63 = si; checked: image, decode, transcription; could be 65 (su, which does not fit); the blind reader and the cold reviewer also have 63.
- strokes after 02, 76 (L3 groups 4-5) and 52 (L4 group 14) - read: separators, not digits; checked: image, decode, transcription; the other readers read them the same way.
- "Ez" in the ink line at the foot - read: Ez (perhaps Es); checked: image, decode, transcription; not part of the cipher.
- last word of the ink line - read: Avila; checked: image, decode, transcription; the first reader and the cold reviewer read Avila, the blind reader Villa (after its decode). AI reading review, 27 Nov 2026, 22:53-22:54 EST: a fresh agent (Claude Opus 5.5, own session, built none of this) was given only a crop of the line and the full image, and not told the candidates or the decode. It read "¿Es cierto que viene ésta mi general Avila?" and the last word letter by letter as a capital A, a v-shaped wedge, one minim, a looped l (the only ascender) and an open a: *Avila*, probable (about 80 percent); the other readings it could not exclude were Avilu, Anila, Arila and Aula, not Villa. It read the first word as *Ez* written for *Es*. No person has read the line on the image.

## Escalation

- [x] siblings: 3492.1-3 and 3492.3-3 (the same folder) read for context. 1914 telegrams of the fonds with coded text
  in CEHM catalogue records 13000-13420 fetched and checked against the card (`scripts/heldout_test.py`): 33.3233.1
  (record 13158) the held-out test, missed; 33.3231.2-2 (13156) and 33.3231.1-2 (13155) the card gives no Spanish;
  31.3079.1 (13092) in letters. Not searched: the other 1914 legajos of CMXV and other fonds.
- [x] clear-pages: the ink line at the foot (a clear gist of the question, not a decipherment of the groups) and the
  clear reply 3492.1-3 (about the governor's health, not this question) checked.
- [x] known-keys: the fonds' own card; the other cards of 1557.1 and Allen's 1914 key tried in the frozen plan.
- [x] print: no edition found. The index of Narváez 2019 (*Criptografía diplomática, política y militar en México*,
  from our photographs) names Enrique and Plutarco Ornelas, not Tomás. Narváez 2025 ("Algunos casos criptográficos
  del movimiento constitucionalista, 1914-1915") not read.
- [n/a] key-rebuild: the key is the archive's card, used unchanged; nothing is rebuilt.
- [x] retry: the one wrong group (46 in sírvase) re-read on the image by three AI readers (46 each time); no other cell
  of the card gives va; the doubtful groups 28 and 63 re-read the same way (Transcription doubts).

## Not checked

- The card's owner and date (not a gap in the text, but it bears on the reading): the card has no heading; the 1914
  telegrams checked on 25 Nov are listed under Escalation; not searched: the other 1914 legajos of CMXV (after
  catalogue record 13420) and other fonds.
- No person has compared the groups, the card or the ink line with the images.
- All the AI readers (the first agent, the blind reader, the cold reviewer, the agent of the second round, who
  transcribed the held-out telegram, and the reader of the ink line on 27 Nov) are the same model (Claude Opus 5.5), though in separate sessions.
- Whether Villa went to Ciudad Juárez in late August 1914 was not looked up.
- Plan 2 (`plan/PLAN_2026-11-26.md`) also covers attempts on four other telegrams of catalogue 1462 (A3-A6). They all
  missed and are not part of this entry. They are recorded in our own work notes, which are not in this repository.

## Access and conditions

Records: `https://www.cehm.org.mx/Buscador/FichaBasica/<record>?Tipo=A`. Image files:
`http://visor.cehm.org.mx/assets/docx/fondos/jzd/CMXV/<legajo>/<carpeta>/<doc>/CMXV.<legajo>.<carpeta>.<doc>.000N.jpg`
(plain http; the https host failed). Both are free to view online, and the viewer marks the images "Todos los
Derechos Reservados". **Use of the CEHM-Carso images with AI readers: Andrew Beling's decision of 25 Nov 2026.** No
images are in this folder.

| Item | Record | Image(s) |
|---|---|---|
| CMXV.35.3492.2-3 (this telegram) | 13262 | `.../CMXV/35/3492/2-3/CMXV.35.3492.2-3.0001.jpg` |
| CMXV.16.1557.1 (key sheets; the card is image 0003) | 9076 | `.../CMXV/16/1557/1/CMXV.16.1557.1.0003.jpg` |
| CMXV.35.3492.1-3, 3-3 (same folder) | 13261, 13263 | `.../35/3492/1-3/...0001.jpg`, `.../35/3492/3-3/...0001.jpg` |
| CMXV.33.3233.1 (held-out) | 13158 | `.../33/3233/1/CMXV.33.3233.1.0001-0003.jpg` (0002 the coded form, 0003 the typed clear text) |
| CMXV.33.3231.1-2, 2-2 | 13155, 13156 | `.../33/3231/1-2/...0001-0002.jpg`, `.../33/3231/2-2/...0001.jpg` |
| CMXV.31.3079.1 | 13092 | `.../31/3079/1/CMXV.31.3079.1.0001-0002.jpg` |

## Files

| File | Content |
|---|---|
| `transcription_CMXV.35.3492.2-3.txt` | settled transcription (groups by line, form fields, clear words, ink line) |
| `transcription_CMXV.35.3492.2-3_passA.txt`, `_passB.txt` | the first reader's two passes |
| `transcription_CMXV.35.3492.2-3_blind.txt`, `blind_decode_CMXV.35.3492.2-3.txt` | the blind reader's transcription and its own decode and count |
| `key.tsv` | the card: Jalkut's values and the blind reader's |
| `decryption_CMXV.35.3492.2-3.txt` | the key's unedited output, written by `scripts/decrypt.py` |
| `reading_CMXV.35.3492.2-3.md`, `translation_CMXV.35.3492.2-3.md` | reading; translation |
| `words_CMXV.35.3492.2-3.md` | each cipher word with its groups, the card's values, its status, and the count |
| `scripts/decrypt.py` | decryption, `--check`, count |
| `scripts/measures.py` | W and S with 1,000 permuted cards each; `--controls` prints the best three |
| `scripts/heldout_test.py`, `heldout/` | the held-out test on CMXV.33.3233.1, and the card on the two Villa telegrams of 3231 |
| `scripts/after_plan_terrazas_key.py` | after the plan: the letter key of 3233.1 |
| `plan/` | both plans with their hashes, and the frozen run of 25 Nov (a record; see step 5) |
| `scripts/run_plan.py`, `scripts/common.py` | the frozen run of the first plan, which rebuilds `plan/plan_run_2026-11-25.txt` (step 5) |
| `plan/frozen_run/` | that run's inputs: the key transcriptions of CMXV.16.1557.1 and the settled transcriptions of the run's telegrams (T1 and T4-T6 are a record of work, not part of this entry) |

```
python3 -I scripts/decrypt.py --check
CYPHERSOLVER_REPO=<checkout> python3 -I scripts/measures.py --controls
python3 -I scripts/heldout_test.py
python3 -I scripts/after_plan_terrazas_key.py
ALLEN_JSON=<path to decode-result.json> python3 -I scripts/run_plan.py
```

## Credits

- Daniel Jalkut, for the transcription of the syllabary card (`targets/duron1911/siblings/syl.py`).
- Daniel Bourdeau, for catalogue 1462 and the pointer to the key sheets CMXV.16.1557.1.
- Ashton Allen, for his 1914 key and his villa1914 readings (issue #845, pull request #865), which the frozen run tested
  on this telegram.
- The CEHM-Carso, which holds the telegram and the card.

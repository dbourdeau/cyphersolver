# argumedo1921/beling: eight more letters of Cristóbal M. Argumedo to Félix Díaz, Sept 1921 - June 1922 (related to catalogue 1445)

Status: read in part (Andrew Beling, with AI agents, 25-27 Nov 2026). Narváez's published table, applied unchanged:
330 cipher words, 299 read as the key gives them, 31 holes (0.906). No person has checked the transcriptions, the
reading or the slip readings; every "check" below is an AI agent's.

**An addition to argumedo1921, not a new target.** These letters use the same table as Brice Dudout's two October
letters, so under the one-key-per-target rule they belong in this target. They sit in this subfolder. Nothing in
`../` (Brice's files) is changed; `../key.tsv` is used as it is.

**Limit of a subfolder.** The repository's scripts read only `targets/*/profile.json`: `docs/_export_profiles.py`, the
`docs/_check_profile.py` audit and the site do not read `beling/profile.json`. Until the parent's `profile.json` and
`NOTES.md` carry these letters, they are on record here but not on the argumedo1921 page or in the figures.
`beling/profile.json` is complete and valid on its own (`python docs/_check_profile.py argumedo1921/beling`), so its
document, text and credit entries can be moved into the parent as they stand, if the parent's author wants that.

**It extends Narváez's reading to letters he did not discuss; it is not a new break.** Roberto Narváez broke the
two-digit table on the letters of 5 and 20 October 1921 (Documenta & Instrumenta 13, 2015, pp. 117-122; book 2019
pp. 358-364). He wrote that the table reads "otras de ese autor" (2019 p. 364) without naming them. None of the eight
letters here is in catalogue 1445's list, and Narváez names none of them.

## Documents

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz. All
are addressed to "Sr. Gral. Díaz" (in cipher) and signed in cipher C. M. Argumedo. They were found by a catalogue search
for "Argumedo" (59 records in the fonds, 25 Nov 2026). Their catalogue records were already in this repository's
raw hit list `research/latam_mexico/cehm_hits.json` (the Oct 2026 Mexico sweep), which the plan names as what was seen
first; none of them was a lead or catalogue row, so no finder's "new cipher" credit is claimed (CONTRIBUTING, issue
#969). Catalogue record numbers are in the last column
(`https://www.cehm.org.mx/Buscador/FichaBasica/<record>?Tipo=A`).

| Letter | Date, place | Form | Runs | Catalogue |
|---|---|---|---|---|
| DCXXI.3.235.1 | 9 Sep 1921, [Mexico City] | typed, 1 f., stamp "SEP 13 REC'D" | 13 | 90943, "carta mecanografiada en clave", "lista de nombres no descifrada" |
| DCXXI.3.296.1 | 26 Dec 1921 | typed, 2 ff., stamp "JAN 1 '22" | 30 | 91067, "incluye clave no descifrada" |
| DCXXI.4.344.1 | 26 Jan 1922, Mexico City | typed, 2 ff. | 37 | 91164, "en clave" |
| DCXXI.4.361.1 | 5 Feb 1922, [Mexico City] | handwritten, 2 ff. | 10 | 91198, "en clave" |
| DCXXI.4.378.1 | 22 Feb 1922, [Mexico City] | handwritten, 1 f. | 4 | 91230, "en clave" |
| DCXXI.4.425.2 | 25 Mar 1922, [Mexico City] | typed, 1 f., ink margin note; slip .0001 | 20 | 91316 (catalogue does not say "en clave") |
| DCXXI.5.444.2 | 10 Apr 1922, [Mexico City] | typed, 1 f. | 33 | 91355, "en clave" |
| DCXXI.5.510.1 | 9 Jun 1922, [Mexico City] | handwritten, 2 ff. | 20 | 91486, "en clave" |

Images are on the CEHM-Carso public viewer, on the same path pattern as #941 and #962:
`http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/<a>/<b>/<c>/DCXXI.<a>.<b>.<c>.000<n>.jpg`. AI agents fetched them
with curl on 25 Nov 2026, with no sign-in, one request every 5-6 s. Pencil letters over some runs and pencil
"C. M. Argumedo" under the signatures are in a later hand and are not used.

Four other Argumedo letters of 1922 in the fonds were checked for runs in round 2 and have none: DCXXI.7.655.2 and
7.709.2 (Laredo, 6 Nov and 27 Dec 1922), 7.710.1 (a copy of 7.709.2) and 7.726.2 (n.d.).

**Conditions of the images.** The images are on CEHM-Carso's public viewer, which needs no sign-in. CEHM's site carries
"Todos los Derechos Reservados" in its footer and publishes no terms of use; it says nothing about AI readers. No
conditions came with the images and nothing was signed or agreed. Nobody at CEHM was asked. Andrew Beling decided on 25
Nov 2026 that the CEHM-Carso images may be used with AI readers. No image is committed here; the images are linked.

## System and key

The key is Narváez's table as already in this repository, `../key.tsv` (SHA-256
69ce383ff6c3062dd64ab850d6cd28cd02f84564d5071708f816fb577856831e at main b0f1a1d797): A=34 B=35 C=36 D=37, E=01 ...
N=10, Ñ=11, O=12 ... Z=23. It is applied unchanged and not copied here. Codes outside 01-37 (30 and 55, once each)
decode to "?".

## Plan, transcription and controls

**Round 1** covers the seven letters other than 4.425.2, done on 25 Nov 2026.
- **Plan.** `PLAN.md` was written and hashed before any run was decoded (`PLAN.sha256`: 18:58 EST, with addendum 1 at
  19:39 EST, before the controls were run). The order of plan and run rests on local file times only. Before the plan,
  one image (3.235.1) was looked at reduced, and two runs were recognised by eye; the plan says so. The first hash in
  `PLAN.sha256` is of the plan before addendum 1 (the first 64 lines of `PLAN.md`); its third line names the local path
  where the file was written. **Addendum 1 changed a frozen choice:** the plan had fixed the C2 model text as the
  letters' own clear text or else the Madero Epistolario; the addendum (after T1 and T2 were compared and the settled
  transcription written, before C1 and C2 were run) replaced it with *Archivo Santander* XIV, because the Epistolario
  may not be processed by computer and the clear text had not been typed.
- **Transcription.** There are two transcriptions:
  - T1 (`transcription_T1.txt`) is by the solving agent, which knew the table.
  - T2 (`transcription_T2_blind.tsv`, notes in `transcription_T2_blind_notes.md`) is by a separate AI agent (Claude
    Opus) working blind: no key, no T1, no decode.

  Both were hashed before decoding: T1 at 19:36:53 EST and T2 at 19:32:38 EST (`transcriptions.sha256` holds every
  hash record of the transcriptions). `scripts/compare_t1_t2.py` finds that
  1,591 of 1,599 pair places agree. The differences were settled on the image without the decode (`transcription.txt`
  header).
- **C1, the printed runs.** The frozen table was applied to the ten runs Narváez prints with their clear (2019 pp.
  359-363). It gives **87 of 89 letters (0.978)**; the pass mark was 0.95. The two misses (PELIGRN, PDNCHO) are the
  writer's slips, which Narváez corrects. The runs were read from the OCR of photographs of a library loan copy; the
  addendum says p. 360 was checked by eye, and pp. 359 and 364 were checked by eye on 27 Nov 2026. One input was
  changed: the book prints the Benítez run as ...-10-05-L7(sic)-01-23 (p. 360); the script has 17 there, as the
  letter's image has it. Scored as printed, with L7 a miss, C1 is 86 of 89 (0.966), still a pass (comment in the
  script).
- **C2, chance.** All new runs were scored with Spanish letter trigrams. The model is the public-domain OCR of *Archivo
  Santander* XIV, Bogotá 1918, Internet Archive `archivosantander14bogo`
  (https://archive.org/details/archivosantander14bogo), file `_djvu.txt`, SHA-256 766fa610ee2e4757... (not committed). The frozen
  table scores -2.669 per letter; the best of 1,000 permutations of the code values scores -4.590. **None of the 1,000
  scores at or above** the table, so C2 passes.

**Round 2** covers DCXXI.4.425.2, done on 25-27 Nov 2026 (`round2/`).
- **Plan.** `round2/PLAN.md` was hashed at 25 Nov 21:54:49 EST, before any image of the five later letters was looked
  at by the solving agent (the plan's own text says "about 21:56", an estimate written before the hash). This also
  rests on local file times.
- **Transcription.**
  - A blind helper (AI, Claude Opus; no key, no decode, no other project file) found runs in only one of the five
    letters. Its T2 has 20 runs and was hashed 25 Nov 21:59:56 EST. It could not avoid seeing image .0001, the
    period slip that gives the clear of the runs; its notes say so, and that it did not use it.
  - T1 is by the solving agent, hashed 27 Nov 18:54:18 EST, then rehashed at 18:54:25 after a wrong time in its header
    line was corrected (nothing decoded; the first version is not kept; both hashes in `transcriptions.sha256`). Before
    T1, that agent had seen the helper's report, which quoted runs 19 and 20 and the repeated chain of runs 10, 13 and
    16; T1 says so.
  - `round2/scripts/compare_t1_t2.py`: 19 of 20 runs agree digit for digit. In run 7, T1 had [0|1]2 and T2 had 02; it
    was settled as 02 on the image before decoding.
  - One edit after the first decode: in run 3 the page gap after "37-" had been taken by the script for a sign. It was
    removed, and no digit changed (`round2/transcription.txt` header, `round2/transcription.sha256`).
- **C2.** Run with seed 20261126: frozen table -3.089, best of 1,000 permutations -4.245, none at or above. Pass. C1
  was not rerun, as the plan says.

**Scripts.** Each was run twice, with the same output both times:
- from this folder, `python3 -I scripts/decrypt_and_tests.py ../key.tsv <archivosantander14bogo_djvu.txt>` writes
  `decryption.tsv` and prints C1 and C2 (`run_tests.txt`);
- from `round2/`, `python3 -I scripts/decrypt_round2.py ../../key.tsv <same file>`;
- `scripts/count_words.py` and `round2/scripts/count_words.py` check the marks against the decryption and count.

## Reading and counts

The marked readings are `reading_marked.tsv` and `round2/reading_marked.tsv`:
- a plain word is read: the table gives it letter for letter;
- `{x/y}` is a hole: the table gives x where the sense needs y. This covers a writer's one-code slip, a code outside
  the table, or a dropped letter.
- `{x?/y}` is an open transcription doubt.

The runs in their sentences are in `reading_<letter>.md` (`round2/reading_DCXXI.4.425.2.md`), and their English,
sentence by sentence with the same holes, in `translation_<letter>.md`. AI helpers wrote both from the images on 27
Nov 2026 with the counted words unchanged; `translation.md` is a summary of all eight letters. Word division in the
runs is editorial (most runs carry no word marks), so the word count follows the sense. Abbreviations (GRAL, FCO, LIC, DR, EDO, FDEZ, SR,
SRES) and initials count as words. The one-digit rule of 14 Nov 2026 is not applied, because the table is a
reconstruction, as in argumedo1921.

| Letter | cipher words | read | holes | read share |
|---|---|---|---|---|
| DCXXI.3.235.1 | 26 | 25 | 1 | 0.962 (read) |
| DCXXI.3.296.1 | 61 | 51 | 10 | 0.836 |
| DCXXI.4.344.1 | 64 | 58 | 6 | 0.906 |
| DCXXI.4.361.1 | 26 | 24 | 2 | 0.923 (read by the short-text floor: under 40 words, 2 holes) |
| DCXXI.4.378.1 | 7 | 7 | 0 | 1.000 (read) |
| DCXXI.4.425.2 | 47 | 43 | 4 | 0.915 |
| DCXXI.5.444.2 | 61 | 58 | 3 | 0.951 (read) |
| DCXXI.5.510.1 | 38 | 33 | 5 | 0.868 (short-text floor does not apply: 5 holes) |
| **All** | **330** | **299** | **31** | **0.906** |

BOUNELLIE (4.344.1 runs 5 and 10, spelt the same both times) is counted as read as the table gives it, but the name is
not identified. The period slip gives "Boneglia", and catalogue 1445 names a Charles Moneglia in this network.

## What the cipher hides

This is a summary; the English is in `translation_<letter>.md`.
- 9 Sep 1921: money was raised to rescue Gral. Vicente Benítez; Argumedo met Rafael Delgado, Hermenegildo Heredia and
  Aurelio C. García; there is a belligerency memorial; García offers the cadets of the Colegio Militar.
- 26 Dec 1921: railwaymen and wireless sets for the campaign; strikes and divisions; Dr. Arturo de la Fuente in the
  State of Mexico; Pimentel, Castillo, Pablo Ariza, Enríquez de Rivera and Pancho C. González; Oaxaca; new claves.
- 26 Jan 1922: Fidencio López in Puebla; Charles Bounellie is to receive war material in Michoacán; a letter from San
  Antonio, Texas, for Gral. Sánchez Díaz; Ing. Carlos M. Peralta.
- 5 Feb 1922: Esteban Cantú's manifesto; Enrique Estrada and M. Caraveo are preparing a defection and a provisional
  presidency.
- 22 Feb 1922: Teziutlán.
- 25 Mar 1922: don Pablo Ariza's first meeting; Isauro and Fidencio López brought to agree in Puebla; Guadalajara and
  the fall of Governor Badillo and of the police inspector, Col. Francisco Pérez; Toluca and Zitácuaro; Dr. de la
  Fuente; "se nos perseguirá con saña"; a margin note against Escobar's "obra de disolución".
- 10 Apr 1922: fifty armed men for $20,000; Pimentel as organiser in Oaxaca; Gral. Ismael Hernández; Mario Ferrer's
  manifesto.
- 9 Jun 1922: sixty armed men and $500 for Gral. Agustín Ramírez; De la Huerta in New York.

## Period decipherments (compared after decoding; not used)

**Order.** The slip images DCXXI.3.306.1.0001-0008 and DCXXI.4.425.2.0001 were on disk from 25 Nov 19:05-19:06 EST,
before the round-1 decode (19:39) and the round-2 decode (27 Nov). That they were first opened after decoding (about
19:45 EST for DCXXI.3.306.1) rests on the agents' account, and on the file times for 0009-0013 (fetched 19:41).

**DCXXI.3.306.1** (record 91087, "transcripción de notas en clave", 13 images) is a set of slips on which hands in
Díaz's office wrote the clear of Argumedo's runs, in order. Three slips carry the letters' own stamps ("SEP 13 REC'D",
"DEC 31 ANS'D"). They gloss five of the round-1 letters (not 4.378.1 or 5.510.1) and both letters of argumedo1921;
slip 0001 (Calero / Gral. García Cuéllar / Vera Estañol) matches no letter found.

The slips were read twice:
- first reader: the solving agent, 25 Nov 2026, after decoding (`period_slips_DCXXI.3.306.1.tsv`);
- second reader: a helper AI agent, 25 Nov 21:47-21:54 EST, working blind. It saw only the 13 images: not the first
  reading, the decode or the key (`period_slips_DCXXI.3.306.1_blind.tsv`, notes in `..._blind_notes.md`, SHA-256
  5ffdf587... for the TSV).

Against the reading:
- The slips fit run for run, except at two faint words of slip 0012 (5.444.2 runs 4 and 12, BELICOS and CARITA),
  which only the first reader, after decoding, read as the run's word. They give the intended word at 20 of the 27
  round-1 holes. Those words are counted as holes all the same: words from another witness count as probable, not read. Read plus probable comes to 276 of 283.
- **There are six divergences in meaning where both transcriptions agree on the figures. The blind slip reader
  and the third reader of 27 Nov confirm each slip word**:
  - 3.296.1 run 17: cipher PROVECHO, slip "producto";
  - 4.344.1 run 4: cipher FIDENCIO LOPEZ, slip "Francisco López";
  - run 29: cipher CARLOS, slip "Charles";
  - run 30: cipher CARLOS M PERALTA, slip "Carlos R. Pereyra" (blind: "Carlos [?R.] Pereyra");
  - 5.444.2 run 16: cipher DON PABLO, slip "Don Pancho";
  - 4.361.1 run 7: cipher MANDATARIO, slip "Legítimo presidente".

  The slips' writers wrote what they took the runs to mean, not always pair by pair. For the two persons (Peralta or
  Pereyra, Fidencio or Francisco López), which is right is not settled here. Differences of spelling or addition only
  are in the slip file's comparison column (BOUNELLIE/"Boneglia", EPIGMENEO/"Epigmenio", the C. of Francisco C.
  González left out, MINISTRN read as "Ministro", PRESIDENCEA as "presidencia").
- The two slip readers (first reader, then blind reader) differ at ten places, none of which bears on a count. A third
  AI reading of 27 Nov 2026 (see AI reading review) is given after each, as "third":
  - 0002 l. 1: "Francisco González" or "Fra[...]o González" (a tear; the first reader supplied the letters unmarked); third: four
    letters lost to the tear;
  - 0004 l. 1: "peligro" or "[?Peligro]"; third: "Peligro";
  - 0006 l. 2: "Horda" or "[?Lorda]" (the argumedo1921 run reads HORDA); third: "[N|L|H]orda";
  - a struck word on 0006: "Otros", or unread with a D-like first letter; third: a D-like first letter and about three
    more, perhaps "Díaz";
  - 0008 l. 4: "inalámbricos" or "[malambricos]"; third: "malamb[ru|ri]c[o|a]s" (the run reads INALAMBRICOS);
  - 0008 l. 9: "entre" or "ente" (the cold reviewer saw "ente" on the image); third: "ent[?r]e";
  - 0008 l. 17: "no López" or "[?Tió] López"; third: "[N|T]o' López";
  - 0009 l. 15: "Fndz de Castro" or "[?Jndz] de Casti[...]"; third: "Fndz de Casti", stopping short with no tear
    (the run reads FDEZ DE CASTRO);
  - 0012: three faint words ("bélicos", "conflagración", "carita"), which the blind reader left unread or read
    otherwise ("[confragacion|conflagacion]", "[canta-|cauta-]"); third: "[?V]al[o|e]r[e|o]s",
    "confla[g]ación" and "ca[u|n]ta-". The runs (5.444.2 runs 4 and 12) read BELICOS and CARITA from the table; only the first
    reader, who read after decoding, saw those words on the slip, so "fits" is not shown there;
  - 0013 l. 2: "Mata" or unread; third: "M[a][...]", the end under the watermark.

**DCXXI.4.425.2 image .0001** is a handwritten list in pencil, then blue ink, of the clear of that letter's runs 2-18
and 20, in order (`round2/period_slip_DCXXI.4.425.2.0001.tsv`). One AI reader read it after decoding; there is no blind
second reading.
- It fits, and gives the words at three of the four holes: DON, POLICIA, and the G of PERSEGUIRA.
- It diverges twice:
  - run 4: cipher PABLO ARIZA, slip "Pancho Ariza";
  - run 7: cipher D{F/O}N PABLO, slip "don Pancho".
- It adds "Gral." before "Dr. de la Fuente" and writes "perseguirán con zaña" (an N the cipher lacks; Z as in the
  cipher).

The same chain gives PABLO in runs 10, 13 and 16, where the slip has "don Pablo". Pablo Ariza is named elsewhere in the
fonds (catalogue 91087, 91487).

## AI reading review (27 Nov 2026)

At Andrew Beling's request, the open overstrikes and the period slips were given to fresh AI reviewers of ours: two
Claude Opus agents (model alias "opus") that had not worked on this package, started by the orchestrating agent on 27
Nov 2026. Each was shown crops and the full page images only and asked to transcribe what it saw; neither was shown our
transcriptions, the decode, the key, the earlier slip readings or the candidate answers. No person has checked them.

- **The five open overstrikes** (one reviewer, 22:55:39-22:57:43 EST). Shown: 3.296.1.0001 x 130-580, y 580-645;
  4.344.1.0001 x 1380-1770, y 1910-1980; 5.444.2.0001 x 780-1600, y 2330-2410; 5.510.1.0001 x 740-1020, y 730-830 and
  x 200-1984, y 640-900; 4.425.2.0002 x 200-1100, y 1790-1880 (each enlarged 1-4x), and the full pages. Answers:
  - 3.296.1 run 3: 10-23-54-08-01-23, a dark 5 typed over a fainter 3 (medium confidence);
  - 4.344.1 run 27: 08-?2-16-34-10, a dark 1 struck over the left half of a lighter 0; leaning 12, 02 possible (low to
    medium);
  - 5.444.2 run 33: ...-09-01-3?-12, the 7's top bar with a closed lower bowl of a 5 or 6, both equally dark;
    undecided between 35 and 37;
  - 5.510.1 run 4: 04-03-?2, a thin light 0 under a heavy stroke shaped like this hand's 6; undecided between 02 and
    62, leaning 62 (low);
  - 4.425.2 run 18: 01-0?-18-..., a 5 and the machine's Z-shaped 3 in one bowl; undecided, slight lean to 05.

  **None is settled**, so the five words stay holes as before and no reading or count changes. All other figures in
  these crops agree with the settled transcription.
- **The 13 period slips DCXXI.3.306.1** (one reviewer, 22:55:40-23:01:33 EST, a third reading after the first and the
  blind second). Shown: the 13 full images and overlapping 2x strips of each. Asked to transcribe every line, marking
  doubtful letters, with extra care on names. Answer, at the places that bear on the reading:
  - all 20 words the slips give at round-1 holes are read the same way (HERMENEGILDO; PANCHO, HOZ, MOVIMIENTO, DE LA,
    JIMENEZ, PABLO, ARTURO, ENRIQUEZ, OAXACA, GONZALEZ; CHARLES, SAN ANTONIO, TEXAS, ERNESTO, LOS, PRESIDENCIA;
    MINISTRO; CONFLAGRACION, ARMADOS);
  - all six divergences in meaning are read as the slip words: "producto", "Francisco López", "Charles", "Carlos R.
    Pereyra", "Don Pancho", "Legítimo presidente";
  - slip 0007 gives "Arí[j|z]a" (a dot over the descender), where the first two readers had "Ariza"; the run reads
    ARIZA from the table, so nothing changes;
  - two places, both read words in the cipher, are not confirmed on the slips (see the list of reader differences).

  The three readings agree on everything that the counts and the "probable" words rest on. Read plus probable stays
  276 of 283 in round 1.

## Prior art

- **Narváez 2015 and 2019.** Narváez 2015 is Documenta & Instrumenta 13, pp. 107-132,
  https://revistas.ucm.es/index.php/DOCU/article/view/49742. Narváez 2019 is *Criptografía diplomática, política y
  militar en México (1813-1926)*, SRE, pp. 358-364, read from photographs of a library loan copy. Both give only the
  system, the table and the 5 and 20 Oct 1921 letters; "otras de ese autor" (2019 p. 364) is left to the reader. The
  2019 pages print the clear of the same ten runs as 2015. They print three further runs of 3.244.1 (08-05-36.-P,
  04-12-15-37-34, 34-06-18-34-13-15-05-01-17-34) and the f. 2 runs of 3.250.2 in cipher only, without their clear.
- **This repository** (`research/archive_sweep_2026-10/known.py`, main b0f1a1d797, 27 Nov 2026). There are no hits for
  any of the eight shelfmarks or for DCXXI.3.306.1 (known.py does not search `research/latam_mexico/cehm_hits.json`,
  the raw hit list that holds their catalogue records; see Documents). Catalogue 1445 lists none of them, and no open
  pull request names them (`gh pr list`, 27 Nov 2026).
- **DECODE.** The record-list search (`https://de-crypt.org/decrypt-web/RecordsList?search=<term>`, 27 Nov 2026
  18:57-19:00 EST) found no record for Argumedo, Felix Diaz, Díaz, DCXXI, Carso, Mexico, Wellington or Cortes. The
  control "Add MS 72438" returned 20 records. The saved result pages are kept outside the repository.

## Transcription doubts

Every place where a transcriber flagged a sign, and every place where T1 and T2 differed. "Decode" means the place was
looked at after decoding, once the sign had been settled on the image.

- 3.296.1 run 3 (GONZ{A?/A}LEZ) - read: [3|5]4, a 5 and a 3 typed over each other; checked: image, decode, transcription (T1 34, T2 [5|3]4); not settled; 34 gives A, 54 is outside the table. AI reading review (27 Nov): a dark 5 over a fainter 3, so 54 (medium confidence); either way the word stays a hole.
- 3.296.1 run 8 (SRES) - read: a struck character (Z or 3) before 34, left out; checked: image, decode, transcription (both left it out).
- 3.296.1 run 2 and run 11 - read: 16 with the 1 overtyped, 18 with a mark under it; checked: image, decode, transcription (both agree); no effect.
- 3.235.1 runs 8 and 9 - read: each run on one line, no repeated pair; checked: image, decode, transcription (T2 had 36-12-|12 and 12-15-|15 at supposed line ends; not adopted).
- 3.235.1 runs 3 and 6 - read: 17 typed over a dash, 19 with the 1 overtyped on a dash; checked: image, decode, transcription (both agree).
- 4.344.1 run 27 (L{O?/O}S) - read: [1|0]2, the 1 overtyped D-like; checked: image, decode, transcription (both); not settled; 12 gives O. AI reading review (27 Nov): a dark 1 struck over a lighter 0, leaning 12 (low to medium confidence); left open.
- 4.344.1 runs 11, 12, 14 - read: last 12 overtyped (struck); a struck character between 10 and 17, left out; first 15 overtyped on another figure; checked: image, decode, transcription (both agree); no effect.
- 4.378.1 run 3 - read: one run; the separator between 17 and 08 unclear (a loop from the line above); checked: image, decode, transcription (both agree).
- 5.444.2 run 1 (GRAL DON FELIX DIAZ) - read: 05 with a handwritten slash through it; checked: image, decode, transcription (both 05).
- 5.444.2 run 5 (CONFLAGRA{B/C}ION) - read: 35; checked: image, decode, transcription (T1 36, read to fit; T2 35; the image shows 35); the hole rests on this.
- 5.444.2 run 16 (DON PABLO) - read: 10, the last figure of the line overtyped or damaged; checked: image, decode, transcription (T1 10, T2 "1 [0|Q]").
- 5.444.2 run 33 (ARGUME{D?/D}O) - read: 37 and 35 typed over each other; checked: image, decode, transcription (both); not settled. AI reading review (27 Nov): the 7's top bar and a closed lower bowl of 5 (or 6), equally dark; undecided between 35 and 37.
- 5.510.1 run 1 (GRAL DIAZ) - read: 34 retraced; checked: image, decode, transcription (both 34).
- 5.510.1 run 4 (HG{F?/O}) - read: 02, the first figure a heavy 0 over or under a 1; checked: image, decode, transcription (T1 [1|0]2, T2 02); not settled (marked {F?/O} on 27 Nov 2026 after the cold check; count unchanged); 12 would give HGO. AI reading review (27 Nov): a thin light 0 under a heavy later stroke shaped like this hand's 6; undecided between 02 and 62 (62 is outside the table), leaning 62 at low confidence; no reading gives 12 clearly, so it stays open.
- 5.510.1 run 7 (RAMIREZ) - read: 09; checked: image, decode, transcription (T1 [8|0]9, T2 09); the loop above the 0 is the descender of a letter on the line above.
- 5.510.1 run 14 (OAXACA) - read: 36 written over another figure, then 34 retraced; checked: image, decode, transcription (both 36, 34).
- 4.361.1 run 9 and 5.510.1 run 15 - read: end of line partly under the CEHM watermark; checked: image, decode, transcription (both agree).
- 4.425.2 run 7 (D{F/O}N) - read: 02; checked: image, decode, transcription (T1 [0|1]2, T2 02; settled 02 before decoding); 12 would give DON.
- 4.425.2 run 9 (BADILLO ... POLICIA) - read: 12 with a slanting stroke through the 1; no hyphen at the two line ends, taken as one run; checked: image, decode, transcription (both).
- 4.425.2 run 11 (TOLUCA ZITACUARO) - read: 17, the 7 overtyped; checked: image, decode, transcription (both 17).
- 4.425.2 runs 2, 3, 7, 8, 20 - read: small marks taken as separators or nothing (a comma-like mark under the hyphen 10-01, a space after 37-, a dot above a hyphen, 0634 typed together and split, an =-like joiner); checked: image, decode, transcription (both agree).
- 4.425.2 run 18 (PERSE{I?/G}UIRA) - read: 05 typed heavy, perhaps over 03; checked: image, decode, transcription (both 0[5|3]); not settled; 03 would give G. AI reading review (27 Nov): a 5 and this machine's Z-shaped 3 share one bowl; undecided, a slight lean to 05.

## Remaining gaps

- 26 holes that are writer's slips or codes outside the table (`reading_marked.tsv`, `round2/reading_marked.tsv`) -
  blocker: illegible; seen on the image: one-code slips, codes 30 and 55 outside the table, two dropped letters
  (ENRRIQU{-/E}Z, ANTONI{-/O}); the key does not give the word as written and no clear copy of the letters is known.
  20 are given by a period slip (probable); 6 have no other witness: 4.361.1 FELI{Z/X}; 5.510.1 ED{N/O}, {D/A}RIZA,
  DO{Ñ/N}, {A/C} M; 4.425.2 {Z/S}AÑA (the slip also writes Z).
- 5 open overstrikes: GONZ{A?/A}LEZ, L{O?/O}S, ARGUME{D?/D}O, HG{F?/O}, PERSE{I?/G}UIRA - blocker: illegible; two
  figures typed or written over each other (Transcription doubts). 3 are given by a period slip; ARGUME{D?/D}O and
  HG{F?/O} have no other witness. The AI reading review of 27 Nov 2026 settled none of the five.

## Limits of the check

- No person has checked the transcriptions, the reading or the slips. The 13 slips of DCXXI.3.306.1 had three AI
  readers (the second and third blind); the 4.425.2 slip had one AI reader. The
  sentence files are one AI reader's.
- C1 used the book's printed runs from OCR of loan photographs, checked by eye on pp. 359-360 and 364.
- An open doubt is decoded with its first reading only; the second reading's effect is given in Transcription doubts.
- Untried in the same fonds:
  - the Argumedo letter (probably of 18 Nov 1921) that slip 0001 points to, not found;
  - the 1923-28 letters the catalogue marks "en clave" by other writers (logged as leads, not opened);
  - later pencil letters under or over some runs (4.378.1, 5.444.2, 4.425.2, and "Gral Díaz" over 5.510.1 run 1), a
    third witness of a few words, not transcribed or compared.

## Escalation

- [x] siblings: all Argumedo records of the fonds listed (catalogue search, 59 records); eight with runs read here; four later letters have no runs.
- [x] clear-pages: period slips DCXXI.3.306.1 (two readers, one blind) and DCXXI.4.425.2 .0001 found and compared.
- [x] known-keys: Narváez's table applied unchanged.
- [x] print: Narváez 2015 and 2019 (pp. 358-364) checked; neither prints these letters.
- [x] retry: the five later letters tried under a frozen plan (round 2).

## Credits

Andrew Beling. Transcriptions, decoding, reading, translations and slip comparison by AI agents (Claude,
claude-opus-5-5); a separate AI agent made the cold check on 27 Nov 2026; no person has checked any of it. Key and system: Roberto Narváez (2015, 2019). Parent target and `../key.tsv`: argumedo1921
(Brice Dudout, #962). The viewer route: wellington1922 (#941). Images and catalogue: CEHM-Carso.

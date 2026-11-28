# wellington1922/letters1922: two more letters of the Wellington correspondent to "José González", 1922, read with Narváez's key 313

Status: read in part (Andrew Beling, with AI agents, 25-27 Nov 2026). AI agents (Claude Opus 5.5) wrote a first version on
25 Nov 2026 (file time 21:34 EST) and revised it on 27 Nov 2026. No person has checked any of it; every "check" below is a
model's.

**An addition to wellington1922, not a new target.** These letters use the same key as the parent, Narváez's 313,
with the same rule: the cycle runs on through each run. Under the one-key-per-target rule they belong there.
targets/sanchez1922 also uses 313, but there the cycle restarts at every word. The maintainers said on PR #941 that
they would decide whether wellington1922 joins sanchez1922. If it moves, this subfolder moves with it. Nothing in
`../` is changed; the key is `../key.txt`.

**Limit of a subfolder.** The repository's scripts read only `targets/*/profile.json`. The export, the
`_check_profile.py` audit and the site do not read `letters1922/profile.json`. Until the parent's `profile.json` and
`NOTES.md` carry these letters, they are on record here, but not on the wellington1922 page or in the figures.
`letters1922/profile.json` is valid on its own (`python docs/_check_profile.py wellington1922/letters1922`). Its entries
can be moved into the parent as they stand.

**Registered result first.** Narváez's key 313 was tested unchanged, under a plan frozen before any decoding
(`PLAN.md`, SHA-256 304a1ffa...), on six unread letters of the network in CEHM-Carso Fondo DCXXI. **Two passed**
(DCXXI.6.576.1 and DCXXI.8.731.1; read here). **Four missed**: DCXXI.5.442.1 (it beat every other shift triple on the
trigram score but its word coverage, 0.38, fell short of the plan's 0.50 mark), and DCXXI.6.624.1, 7.647.1 and 7.657.2
(their cipher is mostly hyphenated number-letter groups, a different system; 313 does not stand out). The misses are
not read here and do not rule the key out for those letters under some other phase rule (`test313_output.txt`).

Counts (strict: a word with any changed, supplied, dropped or doubtful letter is a hole; `scripts/count_words.py`):
- DCXXI.6.576.1: **411 clean words of an estimated 516 word places (0.797)**; 490 places (0.839) if each unread
  stretch counts as one word. 160 runs, 2,953 cipher letters.
- DCXXI.8.731.1: **76 clean words of 86 word places (0.884)**. 14 runs, 493 cipher letters.
- Together: 487 clean of an estimated 602 word places (0.809); 576 places (0.845) if each unread stretch counts as
  one word.
- TOPETE (L2.048) was first counted a hole as unattested; the clear text of the same letter names Topete (image .0003),
  so under the plan's own rule it is clean (changed on 27 Nov 2026 after the cold check: 411 to 412).
- CASTILLO (L2.036) is counted a hole because the AI reading review of 27 Nov 2026 could not settle its Ñ bars
  (changed the same evening: 412 to 411). The key gives CASTILLO if the bars are Ñ bars.

## Documents

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz.
Images on the CEHM viewer (plain http, no login), linked here, not committed:

- **DCXXI.6.576.1** (CEHM archive record 91616): typed letter, 7 pages (images .0002-.0008), dated "Agosto 25 de
  1922.-" at the head of page 1 (the catalogue has the same date; the first version of these notes wrongly said the
  date line was not on the pages), "[?P.O.] Box. 1549----N.[?O].", "Muy señor mío y fino amigo", to "José González"
  (Félix Díaz's cover name in this fondo). The catalogue gives the signer as "ilegible"; the typed signature is a cipher
  run, ODRUUHV, which the key gives as M CORTES. Image .0001 is a handwritten slip (see "Period glosses").
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/6/576/1/DCXXI.6.576.1.0001.jpg to ...0008.jpg (0009 does not
  exist: 404 on 25 Nov 2026).
- **DCXXI.8.731.1** (record 91927): typed letter, 2 pages, "[Puebla]", "...10 de 1922" (the month is torn away), to
  "José González", signed in ink "J. [?J.] Wellington" (two AI readings see a second J, see AI reading review; the first version of
  these notes gave the catalogue's "J. W."); the catalogue gives the signer as "[López, Fidencio E. seudónimo de
  J.W. Wellington]". http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/8/731/1/DCXXI.8.731.1.0001.jpg and .0002.jpg.
- One target for both because they are the same network, the same correspondent, the same key and the same handling
  of the cycle; and DCXXI.6.576.1 itself announces the change of signature that links its writer to the Wellington
  letters ("MI NUEVA FIRMA: J J WELLINGTON", run L2.142-143).

## System and key

Gronsfeld-type shift over the 27-letter Spanish alphabet (A-N, Ñ, O-Z): cipher = plain + 3, +1, +3, repeating, spaces
dropped inside a run, the cycle starting at the first letter of each run and running on to its end (variant A of the
plan, chosen by the plan for both letters; variant B, a restart at each visible space, gives the same text here since
these runs have no spaces). `../key.txt` states the rule (the parent's key file, used as it is); `scripts/f313.py`
and `scripts/decrypt.py` apply it.
In DCXXI.6.576.1 the typist made Ñ as an N with a typed bar; where the bar is missing the key gives M for N
(CORO{M/N}A, L2.005), counted as holes.

**The key is Roberto Narváez's**: "Sobre algunos criptosistemas mexicanos de principios del siglo XX", *Documenta &
Instrumenta* 13 (2015), pp. 107-132, at pp. 123-127 (https://revistas.ucm.es/index.php/DOCU/article/view/49742); and
*Criptografía diplomática, política y militar en México (1813-1926)* (Mexico, 2019), pp. 364-369. He found it in the
Wellington letter DCXXI.6.588.1 (`../`, the parent target); it is applied here unchanged. This is not a new break.

## Plan, controls and the registered test

- `PLAN.md` (SHA-256 304a1ffa01aab948cc36074a921c06e163d839cc13fdd318e138b460e56a6f06, written and hashed 19:51 EST
  25 Nov 2026) fixed the key, the two cycle variants and how one is chosen (higher trigram score on the first third of a
  letter's runs, then frozen), the transcription method, the controls, the pass marks and the counting rule.
- **Order (file times only).** The page images were fetched by AI agents working for Andrew Beling at 19:00-19:09 EST
  and looked at once at reduced size, to sort them, before the plan; the plan states what was seen then (pencil digits
  "3133133" over one run of DCXXI.5.442.1, interlinear words on DCXXI.6.576.1, one run decoded in the head while
  sorting). The two transcriptions were hashed at 21:11 EST, the settled transcription at 21:16 EST, and the first
  decoding ran at 21:20 EST (`transcriptions.sha256`, `PLAN.sha256`). Nothing on disk proves the order beyond these
  local file times. The handwritten slip .0001 and the interlinear glosses of DCXXI.6.576.1 were on the fetched pages
  before decoding (and seen at reduced size while sorting, as the plan says); that they were read only after decoding
  rests on the agents' account.
- **C1 (decoder check, as registered): failed as worded.** The plan asked the decoder to reproduce Narváez's printed
  decipherment of the four runs of folio 2, paragraph 2 of the Wellington letter. Two runs match exactly (REPUBLICA;
  SOBRE TODO FALTAS DE ELEMENTOS). The other two match up to a slip in the key cycle: the first to CONTINGENTES DE
  PARTIDA A, where Narváez himself restarts the cycle (his footnote 20, at the 23rd sign); restarted there, it goes on
  RIOS TIEME, and his USTED has no cipher letters in the copy of the string used here (the article's PDF text layer);
  the third to ...ELEMENTOS A UNA L; restarted after that, it gives CHA TAN TRASCENDENTAL, against his printed
  "LVCHA (sic)". So the registered check fails on cycle slips that the plan did not allow for, not on the decoder
  (`control_c1.txt`).
- **C1b (decoder check, added after C1, before any reading):** the decoder reproduces the merged wellington1922
  decryption of all 60 runs letter for letter (`scripts/control_c1b.py`, `control_c1b.txt`).
- **C2 and P2 (registered test, `scripts/test313.py`; raw output `test313_stdout.txt`, summarised in `test313_output.txt`).** Spanish letter-trigram score from
  Archivo Santander vol. XIV (Bogotá, 1918; public domain; Internet Archive item archivosantander14bogo,
  https://archive.org/details/archivosantander14bogo, file `_djvu.txt`, SHA-256
  766fa610ee2e475753525e49918afb08fc73348503364db782c0dbc0ff41f6f8; its
  `_djvu.txt`, not committed); 313 against 1,000 random shift triples and ranked among all 19,683 triples; word
  coverage against 100 random triples. Pass = 313 above every random triple and coverage at least 0.50 and above every
  control.

| Letter | Letters | Trigram score 313 | Best of 1,000 random | Rank of 313 / 19,683 | Coverage 313 | Best control | Verdict |
|---|---|---|---|---|---|---|---|
| DCXXI.5.442.1 | 342 | -3.362 | -3.868 | 1 | 0.383 | 0.079 | miss (coverage) |
| DCXXI.6.576.1 | 2,953 | -2.509 | -3.922 | 1 | 0.708 | 0.075 | **pass** |
| DCXXI.6.624.1 | 100 | -3.673 | -3.562 | 58 | 0.000 | 0.130 | miss |
| DCXXI.7.647.1 | 110 | -3.998 | -3.440 | 3,943 | 0.027 | 0.227 | miss |
| DCXXI.7.657.2 | 522 | -3.986 | -3.781 | 952 | 0.017 | 0.079 | miss |
| DCXXI.8.731.1 | 493 | -2.574 | -3.893 | 1 | 0.645 | 0.118 | **pass** |

- Diagnostics only, not a test (`scripts/diagnostics.py`, `diagnostics_output.txt`): the three missed Wellington
  letters use hyphenated groups of numbers (mostly one or two digits, a few of three) and a few letters (only A-N, X, Z occur), a code or
  nomenclator rather than this cipher; DCXXI.7.657.2 also has 20 runs typed in red, index of coincidence 0.048 (the
  passed letters' runs: about 0.054-0.057).
- After decoding, one transcription error was found and corrected (L2.008: the first pass doubled an F; the blind
  pass and the image have one). The test was rerun on the corrected file; nothing changed in the verdicts. The table
  above and `test313_stdout.txt` are from that rerun; the registered first run gave for DCXXI.6.576.1 2,954 letters,
  C2 -2.507, P2 0.710, best control 0.076.
- **A departure from the plan:** the plan made C1 a gate ("must pass first"). C1 failed as worded and the run went
  ahead after C1b was added; the verdicts rest on C2 and P2 as registered. The words of
  that run are holes in any case.

## Transcription

`transcription_DCXXI.6.576.1.txt` (160 runs), `transcription_DCXXI.8.731.1.txt` (14 runs); `test313_transcription.tsv`
holds all six letters as tested. Pass T1 by the main agent from its own crops; pass T2 by a separate AI agent (Claude
Opus), blind (it saw neither T1 nor the key nor any decoding, and did not open the handwritten leaves). Both hashed
before decoding. They agree letter for letter on DCXXI.8.731.1 and on 153 of 160 runs of DCXXI.6.576.1 (after reading
"N with a typed bar" as Ñ in both); the seven differences were settled on the image as listed under the doubts below.
A sign counts as settled when T1 and T2 agree on it without the decode; an overtyped sign counts as settled when both
read the same top layer.

## Transcription doubts

- L2.002 sign 6 (image .0002, paragraph 1) - read: no sign; checked: image, transcription, decode (looked at only after the sign was settled); both passes saw a sign
  struck out with a #-like overstrike; taken as a deletion, like the seven "/"-struck signs of L2.136. The run is a hole.
- L2.008 (image .0002, paragraph 2) - read: VFQSSFPURND (11 signs); checked: image, transcription, decode; T1 had a
  doubled F, T2 and the crop have one F; corrected after decoding. A hole either way.
- L2.011 sign 2 - read: F; checked: image, transcription, decode (looked at only after the sign was settled); F and T superimposed in both passes. SEÑPR is a hole.
- L2.012 sign 26 - read: Ñ; checked: image, transcription, decode (looked at only after the sign was settled); the bar is mixed with pencil numerals (both passes). MOVIMIENTO is a hole.
- L2.031 sign 6 - read: E; checked: image, transcription, decode (looked at only after the sign was settled); E or F, overtyped (both passes). PELAEBISTA is a hole.
- L2.036 signs 12-13 - read: ÑÑ; checked: image, transcription, decode (looked at only after the sign was settled); T1 missed the typed bars, T2 and the image show them; the AI reading review of 27 Nov 2026 found the light bars as likely to belong to the line above as to the N's (undecided). DOCTOR [?CASTILLO] is a hole.
- L2.048 sign 5 - read: D; checked: image, transcription, decode (looked at only after the sign was settled); D or B typed over a lighter F (T2); the F would give SE PRESENTO. PRESENTO is a hole.
- L2.124 signs 4 and 8 - read: Ñ; checked: image, transcription, decode (looked at only after the sign was settled); ñ overprinted with a round sign (both passes). ELEMENTOS is a hole.
- L2.129 sign 2 - read: P; checked: image, transcription, decode (looked at only after the sign was settled); P and D superimposed (both passes). HOMBRES is a hole.
- L2.130 signs 2-4 - read: JJJ; checked: image, transcription, decode (looked at only after the sign was settled); T1 had two J, T2 and the image three. The run gives no words.
- L2.145 sign 15 - read: M; checked: image, transcription, decode (looked at only after the sign was settled); dark M over another sign (T2), H or M (T1). Inside a stretch with no words.
- L2.094/095 - read: page order JFPHSDÑCULHDGJHU, then FPURÑHÑ; checked: image, transcription, decode (looked at only after the sign was settled); T1 had them swapped.

## Reading

`decryption_*.txt` (unedited output of the key), `marked_*.txt` (word division and marks; `scripts/count_words.py`
checks the marks against the decryption), `reading_*.md` (the clear text of both letters transcribed in full, with each
run's marked words in CAPITALS at its place and its run id; written on 27 Nov 2026 by two AI helpers from the images,
the counted words unchanged), `translation_*.md` (English, sentence by sentence, with the same holes). Word division
inside the runs is editorial.

What DCXXI.6.576.1 hides (25 Aug 1922): its writer fears the CORRESPONDENCIA is INTERCEPTADA; a JUNTA LOCAL was
CONSTITUYOSE ABRIL; the MOVIMIENTO of GRAL PALMA near TUXTEPEC is stalled for want of APROVISIONAMIENTO; at a JUNTA EN
VILLA GUADALUPE with CASTULO PEREZ the INTENSIFICACION of the CAMPAÑA in the REGION DE VERACRUZ and the {I}STMO, with
PEQUEÑOS MOVIMIEN{T}OS in PUEBLA, was agreed, GRAL PEREZ to RECIBA Y DISTRIB{U}YA war materiel for PUEBLA, TLAXCALA,
OAXACA, GUERRERO E HIDALGO; YSABEL GUERRERO will rise in arms; FEDERICO CORDOBA spreads PELAEZ's programme; GRAL BARRIOS
is proposed as JEFE OPERACIONES TLAXCALA PUEBLA with DOCTOR [?CASTILLO] and CORONA; commissions as GRAL BRIGADIER for ROMAN
JIMENEZ and JOSE [?MOLLANO]; the new JEFE DE LA GUARNICION (clear text: Topete) killed Díaz Figueroa, who secretly
had LIGAS CON NOSOTROS known only to DR CASTILLO and the writer; the trip to MEXICO met DIVISION Y EGOISMO; a BRIGADA
QUE LLEVE VUESTRO ILUSTRE NOMBRE is being raised among EXFEDERALES DEL RUMBO DE TEHUACAN; delegates in CADA UNO DE LOS
DISTRITOS DE PUEBLA Y TLAXCALA; LA JUNTA HA EXPEDIDO CUATRO NOMBRAMIENTOS of GENERAL DE BRIGADA, then BRIGADIER, CORONEL,
TENIENTE CORONEL; the garrison chief PRESIDED the CONSEJO SUMARISIMO that SENTENCED LAZCANO and SALGADO to MUERTE; GRAL
JOSE GAMBOA, held AQUI, is informing on MUCHOS FELICISTAS; CINCO MILLONES DE PESOS at five years would finance the
rising; and, at the end, "MI NUEVA FIRMA: J J WELLINGTON", a NUEVA DIRECCION in PUEBLA, replies by the CONDUCTO LIC
AMAYA, HABANA or by the route of SR CORONA of HOLLYWOO{D}. Signed M CORTES.

What DCXXI.8.731.1 hides: who will lead the rising in each part of Puebla state: TOMAS HUERTA in the districts of
TEHUACAN, TECAMACHALCO, TECALI, TEPE{X}I, ACATLAN, CHALCHICOMULA and SAN J{U}AN {DE} LOS LLANOS; JOSE LOPEZ GUILLEMIN on
the Puebla-Tlaxcala border; ROMAN JIMENEZ in {CHIAUTLA}, MATAMOROS, {ATLIXCO}, CHOLULA, HUEJOTZINGO, TEPEACA and around
{PUEBLA}; YSABEL GUERRERO in the REGION DE LOS VOLCANES; in LA SIERRA, MIGUEL MARQUEZ GALINDO, FRANCISCO {MACHORRO} and
SERGIO BONILLA; all wait for the JUNTA's LAST INSTRUCTIONS; a letter of the PRESIDENTE DE [?] is enclosed.

Checks (27 Nov 2026, in a worktree of the repository at main b0f1a1d797): `python docs/_check_profile.py
wellington1922/letters1922` valid; `python docs/_check_reading.py wellington1922/letters1922` gives "marginal" for both
readings (0.528 and 0.537 clean sentences by its word list, which lacks most place and personal names).

## Notes on the holes

- One-letter slips (counted as holes): e.g. ESTA REGIO{L/N}, DOCTOR CASTI{KK/LL}O, GUER{TY/RA}, DE{H/F}INITIVA,
  NUESTR{U/O}S, M{T/I} NUEVA FIRMA, TEPE{H/X}I, MACH{S/O}RRO; the N-without-bar cases (CORO{M/N}A).
- {SEÑPR/SEÑOR} [?CNTOLC] (L2.002, .008, .011, .067, .070, .126): the same group six times; the key gives SEÑPR and then
  no word.
- Names not attested in clear text, in another run or as common Spanish names are holes: [?MOLLANO],
  [?MOROPEZA], [?OLOARTE], [?TERRER], [?MAMEL], [?YNURRETA], [?YNTRRETA], [?GMMYOR].
- Stretches with no words, estimated from their letters: L2.006 (34 letters), .009 (20), .033 (17), .042 (11),
  .089 (20), .130 (17), .145 (61).

## Post hoc (not counted)

Found after the registered run, by the main agent, while marking; none of it is in the counts.
- L2.144-146 (image .0008): read as one run continuing the cycle across the colon and the line-end dashes (as
  Wellington's f3.13 continues f3.12), the stretch gives "SRITA GUADALUPE LANDE{RO}S CALLEJON DE LA AVENIDA VEINTIDOS
  PONIENTE NUM|ERO DOS MIL DOSCIENTOS CUATRO PUEBLA", which fits the handwritten slip image .0001 (below).
- The SEÑPR group: with the cycle restarted at its sixth sign it gives CORONA (SEÑ{P/O}R CORONA); a period pencil
  "Corona" stands over one of them (L2.011).
- L2.006: with one dropped letter it gives JUNTA LOCAL DENOM(I)NADA JUNTA REVOLUCI(P)NARIA DE ORIENTE.
- DCXXI.5.442.1 (missed): its mechanical decryption has whole words in many runs (MEXICO, FERROCARRILERO, QUINCE MIL
  HOMBRES, LANDEROS, LAZCANO, MIXTECA, BRIGADAS) and its signature run gives CORTES; the plan's coverage mark was not
  met, so it is not read. DCXXI.6.576.1 begins "Desde mi última carta de 7 de abril", the date of DCXXI.5.442.1.

## Later-hand glosses and catalogue (compared only after decoding; "fits" is not proof)

The hand of the glosses is not dated; "later hand" means only that it is not the typist's.

- Image .0001 of DCXXI.6.576.1, a handwritten slip: "Srta. Guadalupe Landeros / Callejón de la Av. 22 / o Poniente #
  2204 / Puebla, Pue." and "Ricardo Suárez Escalante". Fits L2.146 (DOS MIL DOSCIENTOS CUATRO PUEBLA). The name
  Suárez fits the unread stretch L2.009 (KIBRSUARE...) only loosely; not counted.
- Pencil and ink words over the runs of images .0002-.0003 (a later hand; the pencil digits 313313... under some runs
  show the reader used the same key): "interceptada correspondencia" (L2.001: fits), "Señor CNtoke" (L2.002: a garbled tail like ours, CNTOLC, differing at two letters), "esta región" (L2.003: fits, the gloss has N), "Castillo" (L2.004: fits; the gloss omits
  DOCTOR), "Corona" (L2.005: fits), "Corona" over L2.011 (diverges: our strict reading has no word there; fits only the
  post hoc restart), "Junta local" (L2.038, .041, .063: fit), "de México" (L2.039: fits), "Juan Barrios" (L2.040:
  diverges, the cipher has GRAL, not a first name), "José Moyano" in the margin near L2.042-046 (our L2.046 has JOSE
  [?MOLLANO]: diverges, ll/y; which run the gloss belongs to is uncertain).
- CEHM catalogue, record 91616 (DCXXI.6.576.1, read 25 Nov 2026 21:27 EST): "incluye clave sin descifrar"; it names
  Guadalupe Landeros, Ricardo Suárez Escalante, Castillo, [Luis Corona], Juan [Francisco] Barrios (fit), "Junta
  [Central] y Local [de Michoacán]" (diverges: our runs give JUNTA LOCAL and DE MEXICO; nothing about Michoacán), and
  "firmado por ilegible" (our signature run gives M CORTES).
- Record 91927 (DCXXI.8.731.1): "[Puebla]" (fits the Puebla districts in the runs); signer "[López, Fidencio E.
  seudónimo de J.W. Wellington]" (not tested by the cipher). Record 91779 (DCXXI.7.657.2, a missed letter) names Tomás
  Huerta, Isabel Guerrero, Román J. Méndez, Federico Córdoba, Cástulo Pérez, Juan Francisco Barrios: the same people as
  these runs, which fits a single network.
- Record 91350 (DCXXI.5.442.1, missed): "firmado por Cortez", 7 Apr 1922, "carta mecanografiada en clave".

## Prior art (checked 25 and 27 Nov 2026)

- Repository (main b0f1a1d797, 27 Nov 2026; `research/archive_sweep_2026-10/known.py`, `gh pr list` read-only):
  catalogue 1445 lists DCXXI.6.576.1 as not worked (a row of the project's own Oct 2026 Mexico sweep, so no
  contributor's "new cipher" credit applies) and does not list DCXXI.8.731.1, which known.py finds only in the parent's
  NOTES (its catalogue summary); no target, pull request or issue reads either. Siblings: `../` (wellington1922,
  PR #941), `../../sanchez1922/`, `../../duhart1921/`, `../../argumedo1921/` (PR #962).
- DECODE: the record-list search (`https://de-crypt.org/decrypt-web/RecordsList?search=<term>`, 27 Nov 2026
  18:57-19:00 EST) found no record for Wellington, Cortes, Felix Diaz, Díaz, DCXXI, Carso or Mexico (control "Add MS
  72438": 20 records); the result pages are kept outside the repository.
- Narváez 2015 and 2019 discuss only the Wellington letter DCXXI.6.588.1 and Argumedo's letters (the 2015 article text;
  the 2019 book pp. 358-369 from photographs of a loan copy, read for the parent and for argumedo1921/beling).

## Remaining gaps

- Stretches with no words in DCXXI.6.576.1 (L2.006, .009, .033, .042, .089, .130, .145) - blocker: too-short; slips or restarts of the key cycle; post hoc readings exist for .006 and .145 but no frozen test.
- The SEÑPR group (six runs) - blocker: too-short; reads only with a restart of the cycle (post hoc).
- Unattested names ([?MOLLANO], [?MOROPEZA], [?OLOARTE], [?TERRER], [?MAMEL], [?YNURRETA], [?GMMYOR]) - blocker: too-short; one occurrence each in the cipher, no clear-text witness.
- Doubtful signs (L2.011, .012, .031, .036, .048, .124, .129) - blocker: illegible; overtyped or barred signs.
- PRESIDENTE DE [?JAJSNTY] (L6.14) - blocker: too-short.

## AI reading review (27 Nov 2026)

At Andrew Beling's request, two places were given to a fresh AI reviewer of ours: a Claude Opus agent (model alias
"opus") that had not worked on this package, started by the orchestrating agent and run on 27 Nov 2026 from 22:55:39
to 22:59:31 EST. It was shown only crops and the two full page images, and was asked to transcribe what it saw; it was
not shown our transcription, reading, the key or the candidate answers, and did no decoding. No person has checked it.

- **L2.036, the bars over the two N's of GPFWPUFBVWJNNP.** Shown: DCXXI.6.576.1.0002, crops x 1000-1786, y 2140-2300
  (3x) and x 1380-1580, y 2200-2280 (6x), and the full page. Answer: each N has two bars above it. The upper bar is dark,
  in the ink of the overtyping on the line above, touches the feet of the overtyped D and A and has their width; it
  judged it an underline of that line (about 90%). The lower bar is thin and light, one per N, about 3 px above the N
  tops, in the tone of the bottom line but equally of the first typing of the line above; it put "a bar typed with each
  N" at about 50-55% and "a light underline of the line above" at about 45-50%. **Inconclusive.** The reading (ÑÑ,
  settled from the image by T2 before decoding) is kept, but under the strict rule CASTILLO is now counted a hole
  (6.576.1 412 to 411 clean; together 488 to 487, 0.809).
- **The ink signature of DCXXI.8.731.1.** Shown: DCXXI.8.731.1.0002, crops x 820-1450, y 260-520 (2x) and x 850-1150,
  y 300-480 (4x), and the full page. Answer: "J. J. Wellington"; two initials, each followed by a stop (about 90%); the
  first initial J (about 80%; I about 12%); the second a single tall narrow loop, J about 50%, I about 25%, G or H about
  15%. With the cold reviewer's reading (J. J.), the second initial is now given as "J. [?J.]": changed in the reading,
  translation, transcription header and profile labels; the catalogue's "J.W." is kept as the catalogue's. No count
  depends on it.

## Limits

- The clear Spanish of the two letters was transcribed on 27 Nov 2026 by AI helpers in one pass (no second reading of
  the clear text); the runs inside it are the two-pass transcription.
- Not compared: a slanted ink word on image .0003 near L2.045-047 (perhaps "Guerrero"), seen by the cold reviewer.
- The Ñ bars at L2.036 (with them the key gives CASTILLO) sit next to dark bars of the overtyped line above. The AI
  reading review of 27 Nov 2026 could not settle them (below), so CASTILLO is counted a hole.
- Every transcription, reading and translation here is a model's (two AI passes for the runs, one main reader); no
  person has checked it, and only a person or the originals would settle the overtyped signs.
- The missed letters (DCXXI.5.442.1, 6.624.1, 7.647.1, 7.657.2) are untried with any other key or phase rule. Material
  in the same fondo not compared: the handwritten slips filed with DCXXI.6.624.1 (.0001), 7.647.1 (.0001) and 7.657.2
  (.0001-.0003), which look like period lists of plain text for the number-letter groups of those letters.

## Escalation

- [x] siblings: wellington1922, sanchez1922 (same key); the four missed letters (above)
- [x] clear-pages: the interlinear glosses and slip .0001 of DCXXI.6.576.1, compared after decoding
- [x] known-keys: Narváez's key 313 applied unchanged under a frozen plan
- [x] print: Narváez 2015 (article text), 2019 (pp. 358-369, loan photographs)
- [n/a] key-rebuild: the key is three shifts and reads both letters; the misses are slips in single runs (for the four
  missed letters, outside this target, the slips .0001 of DCXXI.6.624.1 and 7.657.2 could serve as cribs)
- [x] retry: every unread stretch and the SEÑPR group retried post hoc with restarts or continuations of the key cycle
  (Post hoc, above); not counted, no frozen test

## Conditions of the images

The images are on CEHM-Carso's public viewer, which needs no sign-in. AI agents working for Andrew Beling fetched them
one at a time on 25 November 2026. CEHM's site carries "Todos los Derechos Reservados" in its footer, publishes no
terms of use and says nothing about AI readers. No conditions came with the images and nothing was signed or agreed.
Nobody at CEHM was asked. Andrew Beling decided on 25 Nov 2026 that the CEHM-Carso images may be used with AI readers.
No image is in this folder; the images are linked.

## Credits

Roberto Narváez (key 313 and the system, 2015, 2019); CEHM-Carso, Fundación Carlos Slim (images and catalogue);
Andrew Beling (transcription, decryption, reading, translation by AI agents, Claude Opus 5.5; no person has checked them).

## Files

`transcription_DCXXI.6.576.1.txt`, `transcription_DCXXI.8.731.1.txt`, `decryption_*.txt`, `marked_*.txt`,
`reading_*.md`, `translation_*.md`, `PLAN.md`, `PLAN.sha256`, `transcription_T1.tsv`, `transcription_T2_blind.tsv`,
`transcriptions.sha256` (the hash records of T1, T2 and the settled versions, 25 Nov 2026), `test313_transcription.tsv`,
`test313_output.txt` (summary), `test313_stdout.txt` (raw output),
`test313/` (mechanical decryptions of all six letters, both variants, and results JSON), `control_c1.txt`,
`control_c1b.txt`, `diagnostics_output.txt`, `scripts/f313.py`, `scripts/decrypt.py`, `scripts/count_words.py`,
`scripts/test313.py`, `scripts/control_c1.py`, `scripts/control_c1b.py`, `scripts/diagnostics.py`, `profile.json`.
`.gitattributes` keeps the files byte for byte so that the plan's SHA-256 holds on any checkout.
Commands: `python3 -I scripts/decrypt.py`; `python3 -I scripts/count_words.py`; `python3 -I scripts/test313.py
test313_transcription.tsv <archivosantander14bogo_djvu.txt> test313`; `python3 -I scripts/control_c1.py`;
`python3 -I scripts/control_c1b.py ..` (the parent folder); `python3 -I scripts/diagnostics.py test313_transcription.tsv`.

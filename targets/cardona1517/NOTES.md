# cardona1517: Ramón de Cardona, viceroy of Naples, to Charles I, 1517-1520 (catalogue 854)

**Outcome (4 Nov 2026): key recovered ciphertext-only; decoded, not read.**
- **Signs.** The sign alphabet was recovered without a crib.
- **Code groups.** The frequent code groups are read; about a quarter of the code types (mostly single
  occurrences) are open.
- **Confirmation.** Two historical names confirm the key: *al magnífico Burgès de Petrucis* (Borghese Petrucci, 1517)
  and *[Io]han Paulo Ballón … han degollado* (Giampaolo Baglioni, beheaded in Rome in June 1520).
- **Reading.** Long passages read, but many sentences still have holes (about 75% of the plaintext letters read as
  sense; about half of the sentences without a hole).

Issue #262 (status report, then update).

## Source

Madrid, BNE, MSS/20210/11/1-4, "Cartas de Ramón de Cardona, Virrey de Nápoles, a la Sacra Cesárea y muy Católica
Magestad".
- BNE Digital: https://bnedigital.bne.es/bd/es/card?oid=0000173169 (public domain).
- Four signed letters from Naples. The record gives 5 Mar 1517, 2 Mar 1519, 24 Dec 1520 and 18 Jun 1520.
- The images are about 1,070 px per page.

| part | date as written | cipher |
|---|---|---|
| /1 | *a v de otubre de M D xvij*: **5 Oct 1517** (the record has 5 Mar) | blocks A (22 lines, PDF images 3-4), B (11 lines, images 7-8), C (28 lines, image 8) |
| /2 | 2 Mar 1519 | none |
| /3 | 24 Dec 1520 | none |
| /4 | 18 Jun 1520 | block D (19 lines, images 4-5) |

No decipherment is written on any page. No edition or study of these letters was found: the BNE record cites no
literature, and a web search found nothing beyond biographies.

## Transcription

`transcription/[abcd]_transcription.txt`, one written line per row. A label legend heads `a_transcription.txt`.
- **Reading.** Read from 2-3.6x crops. Every sign label in blocks A and C was checked against the images for the
  frequent confusions (`Lo`, `EO`, `z`, `p`, `O`, `d#`, `E`); B and D were checked where the reading stopped making
  sense.
- **Corrections**, listed in the file headers and below:
  - `L o` is one sign `Lo`;
  - `E O` is written as one unit (`EO`) but is capital E + circled dot;
  - `far` is `fax`;
  - D08 and D11 have a rounded `ε`, not the capital `E`;
  - D07 `c)#` is `c#`.
- **Frame marks.** Each cipher piece opens and closes with marks (`ratio`, `D`, `P#`, `=`, `S°`). `scripts/read.py`
  drops them at the ends of the six pieces (A, B01-B03, B04-B11, C, D01-D12, D13-D19).
- **Size:** 1,663 tokens (frame marks included): 706 three-letter code-group tokens of 115 types, 30 tokens of 11
  two-letter groups (`mo`, `mj`, `fe`, …), and 927 sign tokens.

## The system

Aragonese chancery nomenclator, the family of Charles de Lannoy's Naples cipher of 1522-27 (O. Kolosova, *El
lenguaje secreto de la diplomacia de Carlos V (1521-1527)*, thesis, Valencia 2017, http://hdl.handle.net/10550/66216,
pp. 65-89).

- **Letter signs.** Homophonic, about 60 types in use. Several stand for letter pairs (`Lo` *re*, `A` *ll*, `x#` *qu*,
  `z#o` *as*). Capital `E` is *rr*, as in Lannoy's table.
- **Code groups.** Three letters, consonant + vowel + consonant, with initials f g m n p r s t z; a few have two
  letters (`mo` *por*, `mj` *pues*, `fe` *gente*). **They stand for whole words** (*que, de, en, lo, se, el papa, Su
  Santidad, cosa, gente…*). The short ones are now and then also used as syllables (*par-la-me-nto*, *mag-ni-fico*,
  *pre-se-nte*), but there are no syllable groups as in the 1511-15 Vich ciphers. Treating the groups as words is
  what made the solution possible.
- **Class rule (from Lannoy's key).** The initial and the final letter of a group fix the first letter of its word;
  the vowel is free. Lannoy has `fay` *lo* / `fey` *la* and `moq` *el* / `meq` *enemigo* / `maq` *ejército*. Here
  `fed` *lo* / `fid` *la*.
- **One table for both letters.** 53 of the 67 code types in /4 (1520) also occur in /1 (1517).

The table is not Lannoy's: values such as Lannoy's `tum` *razón* or `fus` *Milán* do not fit, and his letter values
decode Cardona barely above chance. It is not the 1511 or 1515 Vich table either. BRAH 9/15 ff. 1-6, the "Cifra del
visorrey" (Galende Díaz 1994; DECODE R9815-R9820, restricted images), was not compared.

## How the key was recovered

Ciphertext-only. Done by Michael Brackx with Claude Code (Claude Opus 5.5) on 4 Nov 2026, with the joint
annealer from vich1515 (#94).
- **Solver.** It anneals a value for every sign (a letter or one of the 40 commonest letter pairs) and for every code
  group (an entry from an option list, or unknown).
- **Score.** A Spanish character 5-gram plus the encipherment cost n log(n/N).
- **`scripts/wsa5.c`** is that annealer (`wsa4.c`) plus a penalty for groups of the same class (initial + final)
  whose words start with different letters (PC = 4 per pair). `scripts/real5.py` adds the classes to the task.

| step | what | result |
|---|---|---|
| 1 | Own solvers (letter n-gram annealing; code groups as words or syllables) and a control on vich1511 N.60 | no convergence; the scoring itself preferred wrong keys |
| 2 | wsa4 with the vich1515 option list (words, syllables, letters); matched control (Lazarillo at Cardona's size) | control: 99-100% of signs at 10M iterations, 14-29% at 300k; Cardona: top runs agree on at most about 75% of signs |
| 3 | Noisy control (35% of group values outside the option list, 5.5% misreadings) | best 2 of 16 runs 90% of signs; Cardona still did not converge |
| 4 | Tokenisation variants (two-letter labels as signs, frame marks dropped, `gnc gnd zme` as signs) | no gain |
| 5 | wsa5 (class rule) on a structured noisy control | 5 of 16 runs at 88-91% of signs (wsa4: 2 of 16) |
| 6 | wsa5 on Cardona with the option list restricted to **whole words** | **top 6 runs agree on 85-94% of sign tokens**; 35 of 63 sign types 6/6 |
| 7 | Chancery model (`build_lm_chancery.py`: Celestina, Villa's *Memorias*, vich1511 clear letters; no Quijote) with 34 signs fixed | frequent code groups agree (67-83% of group tokens pairwise) |
| 8-11 | Rounds 2-5: firm values fixed, the rest re-annealed (16-32 runs each), reading by context between rounds | remaining signs and about 60 more code types settled |
| 12 | Context pass after the first PR version: the stretches that decoded but did not read, sign by sign and group by group, with the class rule; a word-segmentation score (`scripts/coverage.py`) as a check | 2 signs and 2 groups overruled against unanimous runs, 4 groups read, 2 groups found to be nulls (below) |

In step 6 the Quijote-built model still filled rare groups with its own names (`zen fus` = *don quijote*); step 7
removed that.

**Reading by context.** Between rounds, each value was set only when it read in every occurrence. Examples:
- `tul` *entre* (*de entretener*);
- `tek` *dicha* (*entretener la dicha gente*, as in the clear text *entretener la dicha ynfanteria*);
- `fid` *la* (*con la presente*, *la dicha gente*);
- `EO` = `E` + `O` = *re* (*se reciba*, *su real*, *remitirme*);
- `o+` *u* (*vivir*, *escreve*);
- `ε` *t* (*parlamento*);
- `ref` *Su Santidad* (round 4, 8/8; *porque fiziera Su Santidad*).

The runs' value was overruled where the image or every context disagreed:
- `E` *rr*: the runs gave *st* (they cannot produce *rr*);
- `o+` *u* (runs: *al*); `fid` *la* (runs: *a*);
- step 12, against 6/6 runs:
  - `A` *ll* (runs: *si*): D14 *Ballón* (the Spanish form of Baglioni), D17 *degollado*, A01 and A03 *preuillegio*;
  - `ll` *e* (runs: *on*): A20 *recelo*, D02 *terra*, D17 *padre han degollado*, A15 *vieren*;
- step 12, against the runs' *qu*, *he* and *e*:
  - `nag` *que*: always followed by an *e* group or *ello*/*la*/*su*;
  - `tic` *dezir*: D18 *he oído dezir que*, C27 *que dezir, sino remitirme a ellos*;
  - `zes` and `sim` are probably nulls: A19 *en ningún*, A20 *no hay persona*, C11 *un número*, C13 *en breue*.

Step 12 also read, by context and the class rule:
- `sal` *cosa* (C03 *[dos] cosas: la primera … en segundo*);
- `gec` *necesario* (C10 *es necesario reduzirlos*);
- tentatively `mel` *mando*, `toq` *da* and `tud` *dar* (C12 *que-dar-en*).

The word-segmentation score alone did not find these: it proposed `t#` *s*, which context refutes (*dize*, *traço*).
The solver cannot represent *ll*, *rr* or *gi*, so `A` (*ll*) and `E` (*rr*) could never get their values from it.
`ll` (*e*) shows that values agreed by all runs can still be wrong where a sign is rare and its neighbours unsettled.

Each change is logged in the key's `basis` column.

## Key

`key/key.tsv`: label, value, class, basis, token count.

| | firm | probable | doubtful | open |
|---|---|---|---|---|
| signs | 54 | 4 | 1 | 5 |
| code groups | 78 | 14 | 12 | 22 |

- **firm:** agreed by the runs (6/6, or 6+/8 later) or read by context in every occurrence.
- **probable:** 4-5/6 in an early run, not re-tested.
- **doubtful:** a tentative context reading or a model filler. These are written `[?word]` in the reading.

## Reading

- `decryption/decode.txt`: the line-by-line decryption. Sign letters are lower case, code groups UPPER CASE, a
  trailing `?` marks a probable or doubtful value, and `[x]` / `{x}` mark no value.
- `decryption/reading.md`: the passages that read, as sentences with holes marked, with English. Also a summary and
  the clear context of each letter.

The two confirmations:
- **1517 (C16-C20):** *…lo que el papa esto le dize … al magnífico Burgès de Petrucis*. Borghese Petrucci, former
  lord of Siena, brother of Cardinal Alfonso Petrucci, executed in the summer of 1517 for the plot against Leo X. The
  passage goes on *su deseo era vivir y morir debazo [de la] protección del papa, y su padre y los suyos…*
- **1520 (D14, D17):** *de [Io]han Paulo Ballón y [Io]han Ur[…]* and *[Io]han Paulo, que a su padre han
  degollado*. Giampaolo Baglioni, lord of Perugia, beheaded in Castel Sant'Angelo on Leo X's order in June 1520. The
  words before the second name are unread; the phrase fits Baglioni's sons, whose father was beheaded. Around it: *se procederá en la [?sentencia]*, *los
  [?cardenales] y Su Santidad de pronunciar…*, *se proceda en ellos*.

Other readings tie the cipher to the clear text around it:
- *de entretener la dicha gente … pues que no tene con que pagarles* (C05-C06);
- *es que han quitado la cárcel* (B01);
- *la imposibilidad* (B04);
- *el gasto … se ha[n] de despedi[r] los cincuenta [...]* (A21-A22);
- *a parte de Gaeta, porque fiziera Su Santidad…* (A17);
- *me ha parecido tener la paga* (D10);
- *parlamento* (D08, D11);
- *los es necesario reduzirlos … a un número que a los pareciere, y que sean tales los que [?quedaren]* (C10-C12);
- *en este he oído dezir que se [?mandó] ir a los dichos* (D18).

## Remaining gaps

- 22 code types without a value and 12 doubtful, most once or twice (the commonest open one: `gie` 3 tokens; probably names: *las cosas de* `nac` *y* `feg`; doubtful `gnd` *mes* reads in neither place, *la causa del* `gnd` *de Abruço*) - blocker: no-key-material; BRAH 9/15 ff. 1-6 (DECODE R9815-R9820) is the candidate key, and its images need DECODE access, not available here
- rare signs `=`, `c#`, `7+`, `S`, `^L#` (1-7 tokens each); `o+` may be two shapes (B09 prefers *al*) - blocker: needs-physical-access; at 1,070 px several small signs are hard to separate, and no larger image is published
- garbled runs A09 *pedrona … rroarribare*, C18 *nuuosacredo*, D07 *ato…rondacreracho*, and `fax` (5 tokens, *esto* in C16 but *cardenales* in D03 and A11, perhaps two groups confused) - blocker: needs-physical-access; probably a misread or an open sign; the published scan was checked and is the largest available, so a recheck needs a better image from the BNE

## Escalation

- [x] siblings: all four letters of MSS/20210/11 opened; /2 (2 Mar 1519) and /3 (24 Dec 1520) are wholly in clear, and no leaf carries a decipherment or a key
- [x] clear-pages: the clear text around each block read for context (lances, the count of Potenza, Fabriano, Urrea, the Turkish fleet, Gaeta); no page deciphers the blocks
- [x] known-keys: the vich1511 and vich1515 keys and Lannoy's Naples key (Kolosova 2017) compared sign by sign and group by group; same family, different values; the candidate key BRAH 9/15 ff. 1-6 needs DECODE access
- [x] print: the BNE record cites no edition, and web searches found none of these letters; Kolosova 2017 (Lannoy's key) and Galende Díaz 1994 (the BRAH 9/15 key book) consulted
- [x] key-rebuild: sign alphabet recovered ciphertext-only by joint annealing (whole-word code options, Lannoy's class rule, chancery model), then five fixing rounds
- [x] retry: rounds 2-5 re-annealed every unfixed sign and group with the firm values held; the unread groups were then retried by hand from context, and a last context pass (step 12) re-read every stretch that did not make words

## Files

| file | what |
|---|---|
| `transcription/[abcd]_transcription.txt` | the four cipher blocks |
| `key/key.tsv` | the key with class and basis |
| `decryption/decode.txt` | line-by-line decryption |
| `decryption/reading.md` | reading with holes, English, summaries |
| `scripts/load.py`, `scripts/read.py` | load the transcription; decode (`read.py text`) or show the contexts of a group (`read.py ctx GROUP`) |
| `scripts/coverage.py` | word-segmentation score of the decode, and of alternative values for signs and groups (step 12) |
| `scripts/wsa5.c`, `scripts/real5.py` | the annealer with the class rule, and its driver |
| `scripts/syl.py`, `scripts/drv.py` | task building and run helpers (from vich1515) |
| `scripts/build_lm_chancery.py` | the chancery model and the whole-word option list |
| `scripts/to_wsa.py` | the transcription as an annealer token file |
| `scripts/control_matched.py`, `control_noisy.py`, `control_cls.py` | the Lazarillo controls: matched, noisy, structured |

**Reproduce.**
1. Decode: `python3 scripts/read.py text`.
2. The runs need Gutenberg 1619 (*Celestina*), 2000 (*Quijote*, for the controls' model) and 320 (*Lazarillo*) in a
   work folder's `corp/`, and `gcc -O3 -o wsa5 wsa5.c -lm`.
3. Build the model with `python3 build_lm_chancery.py <repo>`.
4. Then, for example:
   `FIXS='...' SOLVER=./wsa5 WIDE=1 ITERS=10000000 RUNS=16 python3 real5.py cardona_tokens.txt`.
   The fixed values of each round are in the key's basis column.

## Credit

Michael Brackx (`brackx`), working with Claude Code (Claude Opus 5.5). The joint annealer is Brackx's, from
vich1515.
- **Leads:** the class rule and the code family from Kolosova 2017; the BRAH 9/15 lead from Galende Díaz 1994.
- **Licence:** the manuscript is the BNE's, public domain. The transcriptions, key, reading and scripts may be used
  under the project licence (CC BY 4.0 for text and data, MIT for code).

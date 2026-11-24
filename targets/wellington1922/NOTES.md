# wellington1922: "J. W. Wellington" to "José González" (Félix Díaz), n.d. [1922?], the felicista junta of Puebla (catalogue 1445)

Contributed by Andrew Beling, working with AI agents, 23 Nov 2026. No human palaeographer has checked the text.

Status: in progress (read in part; the runs where the typist slipped in the key cycle are read only post hoc; not
written up on the site).

Read in part, 23 Nov 2026. This **completes Roberto Narváez's reading** of the letter: he found the key 313 and printed
the decipherment of folio 1's two runs, folio 2's second paragraph and one run of its third, and said that all the other runs
decode with the same key, printing none of them (Narváez 2015, pp. 126-127; 2019, pp. 364-369). Here the 60 other
runs (folio 2 paragraphs 4-7, all of folio 3) are transcribed three times (second and third passes blind) and decrypted with his key:
**250 clean words of an estimated 296 word places (84%)**, 275 if each unread stretch is counted as one word
(`scripts/count_words.py`; a word with any repaired, supplied or doubtful letter is a hole). It is not a new break.

## Document

- CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz,
  **DCXXI.6.588.1**. Typed letter, 3 folios, signed in ink "J. W. Wellington", to "Señor don José González, N. O."
  (New Orleans), the cover name under which Félix Díaz received this fondo's letters (as in `../sanchez1922/`). No date.
  The item also holds two handwritten slips (images 0001-0002; see "Other leaves of the item").
- Images (CEHM viewer, plain http, no login): folio 1
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/6/588/1/DCXXI.6.588.1.0003.jpg, folio 2
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/6/588/1/DCXXI.6.588.1.0004.jpg, folio 3
  http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/6/588/1/DCXXI.6.588.1.0005.jpg (the two slips are .0001.jpg
  and .0002.jpg). The site marks its images "Todos los Derechos Reservados": they are
  linked here, not committed.
- Date: none on the letter. Narváez (2019, p. 364) puts it at the start of the 1920s. The letter reports that Murguía,
  with Cándido Aguilar, has crossed the border and that Peláez is trying to land on the Veracruz coast, and it names
  "Calles y Obregón"; Murguía's rising was in 1922, hence [1922?] in the folder name (our inference from general
  history, not checked against a dated source here). It refers to "mi anterior, fecha 25 ppdo.".
- Folio 3 is **faint** (pale typing, an archive watermark over the right margin of paragraphs 1-2, ink loops of the
  signature over paragraph 4 and the postscript). Its runs were read on contrast-stretched crops (red channel).

- Scope: only the 60 runs above. Folio 1's two runs and folio 2 paragraphs 2-3 are Narváez's printed reading; they
  are not transcribed or counted here (folio 1's first run was checked for the Suárez correction only).

## System and key

Gronsfeld-type shift over the 27-letter Spanish alphabet (A-N, Ñ, O-Z): cipher = plain + 3, +1, +3, repeating, spaces
dropped inside a run; in this letter the cycle starts at the first letter of each run and runs on to its end (in
`../sanchez1922/` it restarts at every word). `key.txt` states the rule; `scripts/decrypt.py` applies it. The same
three-digit rule is already in this repository: `../sanchez1922/key.tsv` and `docs/keys.json` ("Gronsfeld-type key
313 ... from the Wellington letter DCXXI.6.588.1 (Narváez 2015)").

**The key is Roberto Narváez's.** Narváez, "Sobre algunos criptosistemas mexicanos de principios del siglo XX",
*Documenta & Instrumenta* 13 (2015), pp. 107-132 (open access,
https://revistas.ucm.es/index.php/DOCU/article/view/49742), at pp. 126-127: the rule, the worked example
"Contingentes", folio 1's runs, and the statement that the remaining runs decode with 313 (page numbers as checked by
the independent reviewer of this package, an AI agent of ours (Claude Opus 5.5, 23 Nov 2026, 00:35-00:55 EST), who
read the article; one model reader). And Narváez, *Criptografía diplomática, política y
militar en México (1813-1926)* (Mexico, 2019), pp. 364-369: fig. 6 (p. 366) reproduces folio 2; pp. 367-368 derive
the key from the two words written in ink over two runs of folio 2 ("Contingentes", "Republica"); p. 369 prints his
decipherment of folio 2 paragraph 2 and the end of paragraph 3. His printed table and pages are not reproduced here.

**A correction to Narváez, offered with respect.** He prints folio 1's first run as "LIC JUAREZ ESCALANTE" (2015,
p. 127; 2019, p. 369). The run is ÑLFVVDUFCHTFDMDPUH (image 0003, folio 1, "de acuerdo el ___ y yo"; read by us and,
blind, by the reviewer); its fourth sign V gives S, so it decodes LKC SUAREZ ESCALANTE ("Lic. Suárez Escalante", with
the typist's K for I), and folio 3 (f3.14) names in clean letters "el Lic. Ricardo Suárez Escalante". The man is Suárez,
not Juárez.

## What was read before, and what is new here

- **Narváez (2015, 2019):** the key; folio 1's two runs (Suárez Escalante, Corona); folio 2 paragraph 2 (the runs from
  "Contingentes" to the end of the paragraph) and the end of paragraph 3. He says the rest decode with 313 and leaves
  them to anyone working on the whole item at the CEHM. Those runs are not transcribed or counted here.
- **Here:** every other run: folio 2 paragraphs 4-7 (38 runs) and all of folio 3 (22 runs), transcribed from the CEHM
  images and read with his key. As far as we found, they have not been printed deciphered.
- A contemporary hand wrote "Inminencia" in pencil in the margin of folio 2, paragraph 5: it is the decipherment of
  run f2.12 (LÑOLÑHPDLD = INMINENCIA), the only gloss on folios 2-3 besides the two words Narváez used.

## Transcription

`transcription_DCXXI.6.588.1.txt`: 60 runs, 1,605 cipher letters, all 27 letters of the alphabet used (counted with a one-line script over the signs column; `docs/_check_profile.py --measure` would also count the id and clear-word columns).
Pass 1 by one agent from the full images and crops; pass 2 blind by a separate agent from its own crops (it had not
seen pass 1). Folio 2: the passes agree on every letter. Folio 3: they differ at the places below.
Pass 3 (23 Nov 2026), blind, by two further AI agents from their own crops (one for folio 3 paragraphs 1-2, one for
the rest), each measuring the typewriter pitch (about 21.7 px a sign) to check for missing or extra signs: it agrees
with this transcription on all 1,605 letters except six signs listed below (f2.19 s20, f3.04 s5, f3.07 s13-16, f3.10
s42, f3.12 s110, f3.14 s151), and finds no missing, squeezed or extra sign. In particular it agrees on every sign of the
one-letter slips and of the stretches that give no words, which supports their being slips of the typist or
encipherer rather than misreadings (a model reading, not a person's).
Rule used for the counts: a doubtful sign is settled when pass 1 and at least one blind pass agree on it without the
decode being used.

## Transcription doubts

- f2.19 sign 20, before the line break (folio 2, paragraph 5) - read: "?" (an overtyped sign: Ñ typed over B); checked: image, decode, transcription; pass 1 could not read it, pass 2 read Ñ over B or H, pass 3 (blind) Ñ over B. Kept as "?", it holds its place in the key cycle, and the 17 letters after the line break give no words (a hole). As Ñ, it is the letter due in PAULATINAS under the post hoc restart (below); not counted.
- f2.27/f2.28 (folio 2, paragraph 6) - read: two runs ("para que" between them); checked: image, decode, transcription; pass 2 took them as one run broken at the line end, pass 3 two runs. The decode is the same either way: f2.27 has 21 letters, a whole number of 3-1-3 cycles.
- f3.02 sign 2 (folio 3, paragraph 1) - read: F; checked: image, decode, transcription; the first four signs are overtyped (WFPH over another typing); pass 2 read E or F; pass 3 F over E; on our crop the order of the two layers cannot be told. F gives TENEMOS, E gives TDNEMOS. Chosen with the decode, so TENEMOS is counted as a hole.
- f3.03 signs 18 and 20 and the first sign of the second line - read: D, N, Q; checked: image, decode, transcription; under the watermark; pass 2 D or E, N or Y, Q or O; pass 3 [D|B|E], [N|M], Q. The word gives MISPOSICIONES ({M/D}ISPOSICIONES, a hole) with these readings.
- f3.04 sign 5 - read: S; checked: image, decode, transcription; S and B typed over each other (pass 1 B, pass 2 S over B, pass 3 B perhaps over S; the clear "su" just before is struck out too). S gives SU PARECER, B gives nothing, so S is chosen by the decode and PARECER is a hole ([?PARECER]).
- f3.07 signs 9-17 (folio 3, paragraph 2) - read: HTWDSXGFPPPUÑPDDT, signs 13-16 unsure; checked: image, decode, transcription; under the watermark, an overtyping and the "Carlos Slim" stamp. Sign 9: pass 1 first read C (the watermark's C), passes 2 and 3 (blind) read P (pass 3: F possible), the image shows P; P gives EN, counted clean under the rule above (pass 1 and a blind pass agree). Signs 13-16 stay unsure ([Ñ|N] [P|F] D [D|E]; pass 3: S, illegible, D, [B|E|Ñ]); the 8 letters after EN give no words either way (a hole).
- f3.10 sign 42 - read: K; checked: image, decode, transcription; pass 2 H or K, pass 3 [H|K] with an ink blot on the next sign. Inside a stretch that gives no words with either letter (a hole).
- f3.12 sign 18, the start of line 2 and BHMWHT (folio 3, paragraph 2) - read: P; no sign before F; BHMWHT; checked: image, decode, transcription; pass 2 read F, a faint I, and BHMVWHT, which break the run into nonsense (DECEC..., FESMG..., TGQOT...). Pass 3 (blind) agrees with pass 1 at all three places (a paper crease makes the F look like IF; the line's 63-64 signs fit the pitch), so DOCUMENTOS and TESORERO are counted clean.
- f3.12 sign 110 - read: I (TGHIXH); checked: image, decode, transcription; pass 2 I or H, pass 3 [H|I|L]; on the enhanced image the H before it has its bar and this sign is one stem. It is the slip in {H/G}UERRA (I for H, one step); a hole with either reading.
- f3.14 sign 151 (third line) - read: H; checked: image, decode, transcription; pass 2 H or I (prefers H), pass 3 I. H gives CONSTANTEMENTE, I gives CONSTANTFMENTE. On this line the H prints as two stems with a very faint bar (compare the H three signs on), and the pitch allows one sign. Counted clean (pass 1 and pass 2 agree); a stricter count, which also holds EN, would give 248.
- f3.19 sign 6 - read: H; checked: image, decode, transcription; pass 2 H or M, pass 3 H (SUS IDEAS).
- f3.18, f3.20, f3.22 (M in f3.18, S in f3.20, D/R in f3.22) - read: M, S, D and R, through the ink loops of the signature; checked: image, decode, transcription; all three passes agree.

## Plan and control

`PLAN.md` is the plan (SHA-256 e02991a7...), with what was decided afterwards. Key 313 unchanged, cycle restarting at
each run, running on across line breaks; 1,000 random 3-digit keys as controls (Spanish bigram score).

**Order.** The plan, its hash, the decoding script and its output were written within nine seconds of each other
(00:37:33-00:37:42 EST, 23 Nov 2026, file times); nothing on disk proves that the plan came before the first decoding.
The evidence was opened earlier: the five CEHM images were fetched at 00:22 EST and pass 1 was saved at 00:25:37 (file
times), and Narváez's pages had been read from photographs of the book on 21 Nov 2026.
It matters little here: the key, the alphabet and the phase rule are Narváez's published ones, so there was nothing
to tune except the handling of line breaks, which the plan states.

**Control.** Final transcription and the fixed decoder (`control_313.txt`, `python3 -I scripts/control.py
<AFIM_Epistolario_T2_djvu.txt>`): key 313 -2.469; controls' mean -5.353. Key 313 ties with one control only, which is
3-1-3 itself, drawn by chance; 999 of 1,000 are lower; the best other key, 3-1-7, scores -3.626 (-3.664 on the first
transcription with the first decoder).

**Script fix (after the independent review).** The first decoder skipped an unsure sign ("?") without advancing the
key, which shifted the rest of such a run by one place. `scripts/decrypt.py` now keeps the place. What changed:
f2.19 - the first run had read ATINAS ORIENTACIÓN after the line break only because the "?" was skipped; with the
place kept those 17 letters give no words, so ORIENTACIÓN moved from clean to hole (the struck-sign reading is now
post hoc). f3.02 and f3.07 had "?" in the first transcription; their final transcription has no "?" (both passes and
the image), so the fix does not touch them. The control score is -2.505 on the first transcription with the
first decoder and -2.469 on the final transcription with the fixed one (an intermediate run with the first decoder
gave -2.444).

## Reading

`decryption_DCXXI.6.588.1.txt` (unedited output of the key), `marked_DCXXI.6.588.1.txt` (word division and marks),
`reading_DCXXI.6.588.1.md` (the runs in their clear sentences), `translation_DCXXI.6.588.1.md`.
`python scripts/count_words.py` checks the marks against the decryption and counts **250 clean words** (247 before the third transcription settled EN, DOCUMENTOS and TESORERO). Holes: 11
one-letter slips, TUEER for "que es" (2), ULTMIAS, TENEMOS (sign chosen with the decode), PARECER (an overtyped sign
settled by the decode) and 4 unidentified words (RYN, ARMORA, BNOIJNA, CELA), which makes 20 hole words, plus 5
stretches that give no words (f2.19 17 letters, f3.07 8, f3.10 36, f3.13 41, f3.20 37). Counting each stretch as one
word gives 275 word places (0.909); estimating each stretch's words from its letters (5.38 letters per clean word,
about 25.9 words) gives **296 word places, 250 clean (0.845)**, the figure used here. (The post hoc readings below
give 28 words where the count has two unidentified words and four stretches estimated at about 24.3 words; none is
counted.)

`python docs/_check_reading.py wellington1922` (23 Nov 2026, after the third transcription): reading 0.417 (20 of 48 sentences
clean; 0.396 before it), decryption 0.184. Most of the words it does not know are modern Spanish words and names that its period word
list lacks (obregonismo, gobiernistas, desintegraciones, prosecretario, Torruco, Cástulo ...), as for
`../sanchez1922/` (0.46).

What it says: a felicista agent writes to Félix Díaz ("José González") from a state that the context makes Puebla
(the junta's names; compare `../sanchez1922/`). He fears that discouragement will spread among their ranks for lack of
a strong united force; asks for guidance suited to the danger; reports that General Mallén, now serving Obregón, has
bought Torruco of Cástulo Pérez's forces, and that Torruco is now Pérez's chief enemy; warns that Federico Córdoba,
who is in arms, claims to act for Peláez and Díaz. On folio 3: a movement is ready throughout the state, waiting
for Díaz's last orders; Sr. Corona has put off his journey to the United States; the junta is Lic. José María Camacho
(president), Fidencio E. López (secretary), Miguel Márquez Galindo (deputy secretary), Dr. Alberto Moreno (treasurer),
and Francisco Machorro, Miguel Alvarado, Lic. Arturo Osorio, Lic. Luis García [?] and Pomposo Bonilla (members); the
four officers have taken war names (read only post hoc, below); Lic. Ricardo Suárez Escalante, who works with the writer outside the
junta, will be called "Ricardo Lobato"; Lic. Juan Crisóstomo Bonilla, first elected, has left the state, and a Bonilla
(Pomposo) has been named in his place.


## Notes on the holes

- {E/G}RANDES, {F/H}AN, TRAI{E/C}IONARA, LE{W/V}ANTADO, {M/D}ISPOSICIONES, {E/A}, JO{T/S}É, DE{C/B}EN, P{Ñ/R}OSECRETARIO,
  {H/G}UERRA, JU{Y/A}N: one wrong letter each (a typing or enciphering slip); the word the sense wants is given.
- {T/Q}UE E{R/S}: the key gives TUEER; "que es" is the sense. ULT{MI/IM}AS: two letters swapped (ULTMIAS).
- [?RYN?]: before the overtyped sign of f2.19; the rest of that run is a hole (see Post hoc).
- [?ARMORA]: decoded verbatim, but we could not confirm the surname (García Armora? García Zamora?).
- [?BNOIJNA]: BONILLA garbled; after it the run gives no words (see Post hoc).
- [?CELA]: after ENCAREZCO, perhaps the start of "celeridad"; the run ends there.
- [?PARECER]: decoded as this word, but its fifth sign is S and B typed over each other; only the decode picks S.
- {TENEMOS/TENEMOS} (f3.02): its second sign is overtyped, E or F on the image; F, which gives TENEMOS, was chosen with
  the decode, so the word is a hole. Pass 3 (blind) reads F typed over E, but on our enhanced crop the order of the two
  layers cannot be told, so it stays a hole.
- Stretches with no words: f2.19 after the line break (17 letters), f3.07 after EN (8, partly under the watermark),
  f3.10 after LOS NOMBRES (36), f3.13 (41), f3.20 after the name (37). Counted by estimate from their letters.

## Post hoc: slips in the key cycle (not counted)

First found after the registered run by the independent reviewer of this package (the AI agent named above) as "one shift of the cycle per run";
restated on 23 Nov 2026 after the third, blind transcription confirmed every sign of these runs (so the irregularity is
in the typescript, not in our reading). `scripts/posthoc_shift.py`, output `posthoc_shift.txt`. In every case but
one the cycle **restarts (shift 3) at the first letter of a word**, which is what the Sánchez letter
(`../sanchez1922/`) does at every word, or a run **continues the cycle of the run before it** across a colon:

- f2.19: DESINTEGRACIONES `<restart>` PANLATINAS ORIENTACIÓN = "desintegraciones pa{N/U}latinas" ("gradual
  break-ups"), one wrong letter (sign 19, P typed where X was due); the overtyped sign 20 is Ñ over B, and Ñ is the
  letter due there. (The earlier post hoc reading dropped that sign and gave RYN ATINAS.)
- f3.10: LOS NOMBRES `<restart>` DE LAS PERSONAS QUE I{Q/N}TEGRAN NUESTRA JUNTA.
- f3.13: `<continue f3.12>` J. SILICEO, F. SÁNCHEZ, MIGUEL ALTAMIRANO Y LUIS MORA: f3.12 has 130 letters (130 mod 3 =
  1), and f3.13, after "respectivamente:", carries on its cycle. On this reading these would be the war names of the president, secretary,
  deputy secretary and treasurer. **"F. Sánchez" is the signature of the Sánchez letter of 12 Jan 1922
  (`../sanchez1922/`, "F. Vbpfihc.")**: on this reading it is the war name of the secretary, Fidencio E. López.
- f3.20: DESIGNAR AL SR. D. POMPOSO `<restart>` BONILLA, HERMANO DEL LIC., COMO VOCAL EN LA PROP `<+1>` IA JUNTA
  ("Pomposo Bonilla, the licenciado's brother, as member of the junta itself"): the end needs a second, one-place skip
  inside PROPIA, which is not a restart.
- Not reached: f3.07 after EN (8 letters, partly under the stamp), f3.22 after ENCAREZCO (CELA, 4 letters).

**Frozen test (23 Nov 2026, plan SHA-256 c17933f51479..., in the contributor's work folder, not committed; script
`scripts/restart_test.py`, output `restart_test.txt`).** The
restart rule was written down before it was run on any stretch it had not been seen on, with 1,000 shuffles of each
stretch's signs as controls (pass: at least 80% of the letters in words and above the controls' 99th percentile). It
had little unseen material: f3.07's tail and f3.22's tail are too short (shuffles reach 100% too) and missed; f3.20's
end meets the script's mark (coverage 1.00 against a control 99th percentile of 0.82) only because its word list
splits PRORIA into PRO RIA; the sense needs a skip inside PROPIA, which the rule does not allow, so we do not count it
as a pass. On the
stretches already seen it beats the shuffles (f3.10 0.94 against a control maximum of 0.89; f3.13 0.93 against 0.83),
which suggests (the rule was formed on these stretches, and the scorer's word list includes this letter's names) the readings are not an artefact of trying many restart points, but these are not blind tests. So none of
these words is counted.

**Outside support (CEHM catalogue, searched 23 Nov 2026).** The record of another letter signed "J. W. Wellington"
(DCXXI.6.624.1, 5 Oct 1922) names **José Siliceo** and a journey with **Ricardo Lobato** and Luis Corona; the record
of DCXXI.8.731.1 gives "J. W. Wellington" as a pseudonym of **Fidencio E. López** ([Puebla], 1922); DCXXI.7.657.2
(Wellington, 7 Nov 1922) names Pomposo Bonilla, Federico Córdoba, Cástulo Pérez and "José Mallan o Mollan"; and
DCXXI.6.576.1 names Ricardo Suárez Escalante and Luis Corona. These are catalogue summaries, not our reading of those
letters, but they fit the war name J. Siliceo (f3.13), the war name Ricardo Lobato (f3.14), and a secretary,
Fidencio E. López, who signs as Wellington here and, on the f3.13 reading, as F. Sánchez in `../sanchez1922/`.

## Other leaves of the item

- Image 0001: a handwritten slip listing, in order, the cipher words of the Sánchez letter DCXXI.3.323.1
  (`../sanchez1922/`): "Landeros / nombrar una Junta / Tlaxcala / "El Látigo" / Figueroa / Mixteca Baja, Oax. /
  Miguel Gutiérrez / Manuel Márquez / Arturo Osorio / Rodolfo Urdapilleta / Francisco Machorro / Lic. ?ulas / Emilio /
  Manuel Cortez / Plazuela Parral #1 / Puebla, Pue." That is that letter's plain text in order, without "Goitia" and
  the signature. It differs from the signs at that letter's three holes:
  - "?ulas": its capital is this hand's J (or F), not a Y, so probably Julas. The signs spell YULAS exactly.
  - "Baja": the signs spell VAIA.
  - "Cortez": the signs give COR?ES, either CORTES with its fourth sign dropped or CORES with a skip in the key cycle.

  So it supplies words that the cipher does not settle, and the upstream target keeps all three as holes. It is
  reported to that target separately (a "Fuller reading" note) and is not used here.
- Image 0002: a handwritten form "Junta de Puebla" with the headings Pres., Sec., Pro[sec.], Tes., Vocales, left blank.
  It matches the officers named on folio 3.

## Prior art (checked 23 Nov 2026)

- CEHM catalogue: the record of this item (archivo no. 91642) says "incluye claves no descifradas" and lists the names
  of the slip (image 0001), "Landeros, Figueroa, Miguel Gutiérrez, Manuel Márquez, Arturo Osorio, Rodolfo Urdapilleta,
  Francisco Machorro, Manuel Cortez"; it does not decipher the letter. Records of the other Wellington letters: see
  "Outside support" above.
- Narváez 2019 pp. 364-369 (read from photographs of the book); Narváez 2015 pp. 126-127 (read by the independent
  reviewer; it prints the rule and folio 1-2's runs as above, and none of the 60 runs read here).
- This repository: catalogue 1445 credits Narváez 2015 with the Wellington letter; no target, pull request or issue
  covers DCXXI.6.588.1 (pull request #512 is the Sánchez letter, #511 the Duhart letter); checked against main
  9011d5568 (23 Nov 2026).

## Remaining gaps

- f3.07 after ESTAR UD. EN (8 letters) - blocker: illegible; under the watermark, an overtyping and the stamp.
- f2.19 after DESINTEGRACIONES (21 letters), f3.10 after LOS NOMBRES (36), f3.13 the four war names (41), f3.20 after POMPOSO (44) - blocker: too-short; here this means too little unseen text to test the restart rule. These are slips in the key cycle, read post hoc above (with catalogue support for f3.13). The restart rule was frozen and tested on 23 Nov 2026, but the only stretches it had not been seen on were too short to decide it, so these are not counted.
- [?ARMORA] (f3.11), [?CELA] (f3.22) - blocker: too-short; one occurrence each.
- [?PARECER] (f3.04) - blocker: illegible; S and B typed over each other, chosen by the decode. EN, DOCUMENTOS and TESORERO were settled by the third transcription.
- No human check of folio 3's faint letters - blocker: needs-physical-access; a better image or the original would settle the faint signs.

Outside this target: folio 1's two runs and folio 2 paragraphs 2-3 are Narváez's printed reading. They are not transcribed or counted here; folio 1's first run was checked for the Suárez correction only.

## Escalation

- [x] siblings: the Sánchez letter (`../sanchez1922/`, same key, cycle per word) and the Duhart letter
  (`../duhart1921/`, a letter swap) of catalogue 1445; the two slips filed with this item (above)
- [x] clear-pages: the clear text of the letter; the pencil "Inminencia" (f2.12) and the ink "Contingentes",
  "Republica" over two runs of folio 2 (the latter used by Narváez)
- [x] known-keys: Narváez's key 313 applied unchanged
- [x] print: Narváez 2015 pp. 126-127 (via the reviewer) and 2019 pp. 364-369
- [n/a] key-rebuild: the key is three shifts; the misses are slips in single runs
- [x] retry: restarts of the key cycle; post hoc readings above; a frozen restart rule tested with shuffle controls on
  23 Nov 2026 found no unseen stretch long enough to decide it (not counted)

## Conditions of the images

The images are on CEHM-Carso's public viewer (DCXXI.6.588.1), which needs no sign-in. AI agents working for Andrew
Beling fetched the five page images one at a time on 23 November 2026. CEHM's site carries "Todos los Derechos
Reservados" in its footer, publishes no terms of use and says nothing about AI readers. No conditions came with the
images and nothing was signed. Nobody at CEHM was asked; Andrew Beling decided on the use himself. No image is in
the repository or shared.

## Files

`transcription_DCXXI.6.588.1.txt`, `decryption_DCXXI.6.588.1.txt`, `marked_DCXXI.6.588.1.txt`,
`reading_DCXXI.6.588.1.md`, `translation_DCXXI.6.588.1.md`, `key.txt`, `PLAN.md`, `control_313.txt`,
`posthoc_shift.txt`, `restart_test.txt`, `scripts/decrypt.py`, `scripts/control.py`, `scripts/count_words.py`,
`scripts/posthoc_shift.py`, `scripts/restart_test.py`, `profile.json`. `.gitattributes` keeps the files byte for byte,
so the plan's SHA-256 (lines 4-20 of `PLAN.md`) holds on any checkout.

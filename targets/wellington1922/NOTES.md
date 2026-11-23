# wellington1922: "J. W. Wellington" to "José González" (Félix Díaz), n.d. [1922?], the felicista junta of Puebla (catalogue 1445)

Contributed by Andrew Beling, working with AI agents, 23 Nov 2026. No human palaeographer has checked the text.

Status: in progress (read in part; the runs where the typist slipped in the key cycle are read only post hoc; not
written up on the site).

Read in part, 23 Nov 2026. This **completes Roberto Narváez's reading** of the letter: he found the key 313 and printed
the decipherment of folio 1's two runs, folio 2's second paragraph and one run of its third, and said that all the other runs
decode with the same key, printing none of them (Narváez 2015, pp. 126-127; 2019, pp. 364-369). Here the 60 other
runs (folio 2 paragraphs 4-7, all of folio 3) are transcribed twice (second pass blind) and decrypted with his key:
**247 clean words of an estimated 296 word places (83%)**, 275 if each unread stretch is counted as one word
(`scripts/count_words.py`; a word with any repaired, supplied or doubtful letter is a hole). It is not a new break.

## Document

- CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo DCXXI Archivo de Félix Díaz,
  **DCXXI.6.588.1**. Typed letter, 3 folios, signed in ink "J. W. Wellington", to "Señor don José González, N. O."
  (New Orleans), the cover name under which Félix Díaz received this fondo's letters (as in `../sanchez1922/`). No date.
  The item also holds two handwritten slips (images 0001-0002; see "Other leaves of the item").
- Images (CEHM viewer, plain http, no login):
  `http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/6/588/1/DCXXI.6.588.1.000{1,2,3,4,5}.jpg`
  (0003 folio 1, 0004 folio 2, 0005 folio 3). The site marks its images "Todos los Derechos Reservados": they are
  linked here, not committed.
- Date: none on the letter. Narváez (2019, p. 364) puts it at the start of the 1920s. The letter reports that Murguía,
  with Cándido Aguilar, has crossed the border and that Peláez is trying to land on the Veracruz coast, and it names
  "Calles y Obregón"; Murguía's rising was in 1922, hence [1922?] in the folder name (our inference from general
  history, not checked against a dated source here). It refers to "mi anterior, fecha 25 ppdo.".
- Folio 3 is **faint** (pale typing, an archive watermark over the right margin of paragraphs 1-2, ink loops of the
  signature over paragraph 4 and the postscript). Its runs were read on contrast-stretched crops (red channel).

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
the independent reviewer of this package, who read the article). And Narváez, *Criptografía diplomática, política y
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

## Transcription doubts

- f2.19 sign 20, before the line break (folio 2, paragraph 5) - read: "?" (an overtyped sign); checked: image, decode,
  transcription; pass 1 could not read it, pass 2 read Ñ typed over B or H. It holds its place in the key cycle, and
  with it the 17 letters after the line break give no words (a hole). If the sign is a struck-out letter and is
  dropped, they give ATINAS ORIENTACIÓN: listed under "Post hoc", not counted.
- f2.27/f2.28 (folio 2, paragraph 6) - read: two runs ("para que" between them); checked: image, transcription; pass 2
  took them as one run broken at the line end. No effect on the decryption: f2.27 has 21 letters, a whole number of
  3-1-3 cycles.
- f3.02 sign 2 (folio 3, paragraph 1) - read: F; checked: image, decode, transcription; the first four signs are
  overtyped (WFPH over another typing); pass 2 read E or F; F gives TENEMOS, E gives TDNEMOS. Chosen with the decode,
  so TENEMOS is counted as a hole.
- f3.03 signs 18 and 20 and the first sign of the second line - read: D, N, Q; checked: image, decode, transcription;
  under the watermark; pass 2 D or E, N or Y, Q or O. The word gives MISPOSICIONES ({M/D}ISPOSICIONES, a hole) with
  these readings.
- f3.04 sign 5 - read: S; checked: image, decode, transcription; S typed over B (pass 2); pass 1 had B. S gives SU
  PARECER; as the passes differ, the plan makes PARECER a hole ([?PARECER]).
- f3.07 signs 9-17 (folio 3, paragraph 2) - read: HTWDSXGFPPPUÑPDDT, signs 9 and 13-16 unsure; checked: image,
  transcription; under the watermark and a dark overtyping; pass 1 read C for sign 9 (the watermark's C), pass 2 P; the
  image shows P. As the passes differ, EN is a hole ([?EN]). Signs 13-16 stay unsure ([Ñ|N] [P|F] D [D|E]); the
  stretch after it is a hole.
- f3.10 sign 41 - read: K; checked: image, transcription; pass 2 H or K. Inside a stretch that does not decode
  either way (a hole).
- f3.12, three places (folio 3, paragraph 2) - read: P at sign 18; no letter before F at the start of line 2; no V in
  BHMWHT; checked: image, decode, transcription; pass 2 read F, a faint I, and BHMVWHT. On the enhanced image sign 18
  is a faint P, the mark before the line is fainter than the type and not a letter, and BHMWHT has one letter between M
  and H at most. Pass 2's readings break the run into nonsense (DECEC..., FESMG..., TGQOT...); pass 1's give DECEN FIRMAR
  DOCUMENTOS ... TESORERO HAN ADOPTADO. Settled partly by the decode, so, as the plan says, DOCUMENTOS and TESORERO
  are counted as holes ([?DOCUMENTOS], [?TESORERO]).
- f3.14 sign 151 (third line) - read: H; pass 2 H or I; checked: image, decode; H gives CONSTANTEMENTE, I gives CONSTANTFMENTE.
- f3.19 sign 6 - read: H; pass 2 H or M; checked: image, decode (SUS IDEAS).
- f3.18, f3.20, f3.22 - letters crossed by the ink loops of the signature (M in f3.18, S in f3.20, D/R in f3.22); read
  through the stroke; checked: image, transcription; both passes agree.

## Plan and control

`PLAN.md` is the plan (SHA-256 e02991a7...), with what was decided afterwards. Key 313 unchanged, cycle restarting at
each run, running on across line breaks; 1,000 random 3-digit keys as controls (Spanish bigram score).

**Order.** The plan, its hash, the decoding script and its output were written within nine seconds of each other
(00:37:33-00:37:42 EST, 23 Nov 2026, file times); nothing on disk proves that the plan came before the first decoding.
It matters little here: the key, the alphabet and the phase rule are Narváez's published ones, so there was nothing
to tune except the handling of line breaks, which the plan states.

**Control.** Final transcription (`control_313.txt`): key 313 -2.444; controls' mean -5.353. Key 313 ties with one
control only, which is 3-1-3 itself, drawn by chance; 999 of 1,000 are lower; the best other key, 3-1-7, scores
-3.617 (-3.664 on the first transcription).

**Script fix (after the independent review).** The first decoder skipped an unsure sign ("?") without advancing the
key, which shifted the rest of such a run by one place. `scripts/decrypt.py` now keeps the place. What changed:
f2.19 - the first run had read ATINAS ORIENTACIÓN after the line break only because the "?" was skipped; with the
place kept those 17 letters give no words, so ORIENTACIÓN moved from clean to hole (the struck-sign reading is now
post hoc). f3.02 and f3.07 had "?" in the first transcription; their final transcription has no "?" (both passes and
the image), so the fix does not touch them. The control score changed from -2.505 to -2.444 with the corrected
transcription.

## Reading

`decryption_DCXXI.6.588.1.txt` (unedited output of the key), `marked_DCXXI.6.588.1.txt` (word division and marks),
`reading_DCXXI.6.588.1.md` (the runs in their clear sentences), `translation_DCXXI.6.588.1.md`.
`python scripts/count_words.py` checks the marks against the decryption and counts **247 clean words**. Holes: 11
one-letter slips, TUEER for "que es" (2), ULTMIAS, TENEMOS (sign chosen with the decode), 4 words with a sign on which
the blind second pass differs (PARECER, EN, DOCUMENTOS, TESORERO), 5 unidentified words, and 6 stretches that give no
words. Counting each stretch as one word gives 275 word places (0.898); estimating each stretch's words from its
letters (5.36 letters per clean word) gives **296 word places, 247 clean (0.834)**, the figure used here.

`python docs/_check_reading.py wellington1922` (23 Nov 2026, after the script fix): reading 0.396 (19 of 48 sentences
clean), decryption 0.184. Most of the words it does not know are modern Spanish words and names that its period word
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
- [?PARECER], [?EN], [?DOCUMENTOS], [?TESORERO]: decoded as these words, but each holds a sign on which the blind
  second transcription differs; the plan counts such letters as unsure.
- {TENEMOS/TENEMOS} (f3.02): its second sign is overtyped, E or F on the image; F, which gives TENEMOS, was chosen with
  the decode, so the word is a hole.
- Stretches with no words: f2.19 after the line break (17 letters), f3.07 after EN (8, partly under the watermark),
  f3.10 after LOS NOMBRES (37), f3.13 (41), f3.20 after the name (36). Counted by estimate from their letters.

## Post hoc: the typist's slips in the key cycle (not counted)

Found after the registered run, by the independent reviewer of this package, and reproduced here with
`scripts/posthoc_shift.py` (output `posthoc_shift.txt`). **Rule, written after the fact:** where a run stops giving
words, the 3-1-3 cycle may be resumed one or two places on from one stated letter to the end of the run, once per run;
an unreadable overtyped sign may instead be dropped (the same as a one-place shift). The point is marked `<+1>`, `<+2>`
or `<drop>`. None of these words enters the counts above.

- f2.19: DESINTEGRACIONES RYN `<drop>` ATINAS ORIENTACIÓN ("desintegraciones [...] orientación"; RYN ATINAS still unclear).
- f3.10: LOS NOMBRES `<+2>` DE LAS PERSONAS QUE I{Q/N}TEGRAN NUESTRA JUNTA ("the names of the persons who form our
  junta").
- f3.13: `<+1>` J. SILICEO, F. SANCHEZ, MIGUEL ALTAMIRANO Y LUIS MORA: the whole run is enciphered one place off; these
  are the war names of the president, secretary, deputy secretary and treasurer. **"F. Sánchez" is the signature of the
  Sánchez letter of 12 Jan 1922 (`../sanchez1922/`, "F. Vbpfihc.")**: on this reading it is the war name of the junta's
  secretary, Fidencio E. López. A hypothesis that ties the two letters together; not counted.
- f3.20: DESIGNAR AL SR. D. POMPOSO `<+1>` BONILLA, HERMANO DEL LIC., COMO VOCAL EN LA PROP[...] ("Pomposo Bonilla,
  the licenciado's brother, as member in the ..."); the last seven letters still give nothing.
- Not reached by the rule: f3.07 after EN (under the watermark), f3.22 after ENCAREZCO.
- (The reviewer reads f3.02 as "[H]EMOS YA PREPARADO ..." with a restarted cycle; with the overtyped sign read F the
  registered cycle already gives TENEMOS YA PREPARADO ..., counted as a hole above.)

## Other leaves of the item

- Image 0001: a handwritten slip listing, in order, the cipher words of the Sánchez letter DCXXI.3.323.1
  (`../sanchez1922/`): "Landeros / nombrar una Junta / Tlaxcala / "El Látigo" / Figueroa / Mixteca Baja, Oax. /
  Miguel Gutiérrez / Manuel Márquez / Arturo Osorio / Rodolfo Urdapilleta / Francisco Machorro / Lic. Yulas / Emilio /
  Manuel Cortez / Plazuela Parral #1 / Puebla, Pue." It is that letter's plaintext in order (without
  "Goitia" and the signature). It confirms YULAS as decoded; for "Baja" and "Cortez" it supplies the words, which the
  cipher does not spell, so under the strict rule they stay repaired words. Reported to that target separately (a
  "Fuller reading" note), not used here.
- Image 0002: a handwritten form "Junta de Puebla" with the headings Pres., Sec., Pro[sec.], Tes., Vocales, left blank.
  It matches the officers named on folio 3.

## Prior art (checked 23 Nov 2026)

- CEHM catalogue: "incluye claves no descifradas" (as quoted by Narváez 2019, p. 364).
- Narváez 2019 pp. 364-369 (read from photographs of the book); Narváez 2015 pp. 126-127 (read by the independent
  reviewer; it prints the rule and folio 1-2's runs as above, and none of the 60 runs read here).
- This repository: catalogue 1445 credits Narváez 2015 with the Wellington letter; no target, pull request or issue
  covers DCXXI.6.588.1 (pull request #512 is the Sánchez letter, #511 the Duhart letter); checked against main
  9011d5568 (23 Nov 2026).

## Remaining gaps

- f3.07 after ESTAR UD. EN (8 letters) - blocker: illegible; under the watermark and an overtyping.
- f2.19 after the overtyped sign (17 letters), f3.10 after LOS NOMBRES (37), f3.13 the four war names (41), f3.20 after
  POMPOSO (43) - blocker: not-attempted; slips in the key cycle, read post hoc above; a rule for them was written
  after the reviewer's observation, so they are not counted until a frozen test is run on other material.
- [?ARMORA] (f3.11), [?CELA] (f3.22) - blocker: too-short; one occurrence each.
- [?PARECER], [?EN], [?DOCUMENTOS], [?TESORERO] - blocker: illegible; faint signs on which the two passes differ.
- Folio 1's two runs and folio 2 paragraphs 2-3 are Narváez's reading; not re-transcribed here (folio 1's first run
  checked for the Suárez correction only) - blocker: not-attempted.
- No human check of folio 3's faint letters - blocker: needs-physical-access (a better image or the original would
  settle the faint signs).

## Escalation

- [x] siblings: the Sánchez letter (`../sanchez1922/`, same key, cycle per word) and the Duhart letter
  (`../duhart1921/`, a letter swap) of catalogue 1445; the two slips filed with this item (above)
- [x] clear-pages: the clear text of the letter; the pencil "Inminencia" (f2.12) and the ink "Contingentes",
  "Republica" over two runs of folio 2 (the latter used by Narváez)
- [x] known-keys: Narváez's key 313 applied unchanged
- [x] print: Narváez 2015 pp. 126-127 (via the reviewer) and 2019 pp. 364-369
- [n/a] key-rebuild: the key is three shifts; the misses are slips in single runs
- [ ] retry: one shift of the key cycle per run (post hoc readings above; not counted)

## Files

`transcription_DCXXI.6.588.1.txt`, `decryption_DCXXI.6.588.1.txt`, `marked_DCXXI.6.588.1.txt`,
`reading_DCXXI.6.588.1.md`, `translation_DCXXI.6.588.1.md`, `key.txt`, `PLAN.md`, `control_313.txt`,
`posthoc_shift.txt`, `scripts/decrypt.py`, `scripts/control.py`, `scripts/count_words.py`,
`scripts/posthoc_shift.py`, `profile.json`.

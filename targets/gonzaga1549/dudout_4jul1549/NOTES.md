# 4 Jul 1549, Charles V to Ferrante Gonzaga: the cipher copy (cc. 41v-42r) decoded with frozen keys, measured twice against the contemporary decipherment (cc. 43v-44r)

Contributed by Brice Dudout, working with Claude (Anthropic), 17 Nov 2026. Status: **decoded, read in part**. Two pre-registered tests
on two separate portions: KB3 on 41v lines 1-18 (letters 0.744) and KB4 on 41v lines 19-30 + 42r (letters 0.835). Both rank 1/201, both under
the 0.85 letter line, so nothing here is a validated key and nothing is emended. The whole cipher of the letter is now used up (burnt).

## The document
Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. III, cc. 40-45 (Lodovico record
fe5db48d-18d3-42dd-a058-bd9efa3c11c6, 12 canvases, CC BY-NC-SA; images used for study only and not reproduced here).
The catalogue says: "In allegato (cc. 41-44) una copia di lettera parzialmente cifrata (con testo decifrato annesso)".
- cc. 40r-40v: covering letter in clear, signed.
- c. 41r: copy, clear text; **c. 41v: a full page of cipher (30 lines)** opening with the clear words "Si ya no fuessen"; 42r: three more lines and two signs.
- cc. 43r-44r: the contemporary decipherment, another hand ("Annesso al n° 24" pencilled on 43r), beginning "Don Diego de Ayala vuestro
  secretario nos dio la carta que nos escrivistes ... cerca delas cosas de Sena y Plumbin". The subject is the fortress at Siena.
- The cipher is the Imperial Cipher of 1544-1554 (base sign + vowel indicator), as in the other 1549 letters of this folder,
  written here by a copyist whose hand differs from the chancery hand of 13 May / 23 Dec.

## Prior art (checked 17 Nov 2026, before any decoding)
- This repository, main at 66b985bef: `targets/gonzaga1549` (Daniel Bourdeau's page, WAINUT's `wainut/`, Malcolm McBratney's
  `mcbratney_27may1549/`) does not mention 4 Jul 1549, sfasc. III cc. 40-45 or the record id (only in `labels.json`, the raw id list).
  `gh pr list --state all --search "gonzaga1549 OR ferrante1549 OR campori OR 1549"`: no PR on this letter; no open third-party PR.
- The plaintext is not new: the decipherment is in the same file. What is new is the measured test of a key on a page that had never been
  transcribed or decoded. Bertomeu Masiá 2009 (*La guerra secreta de Carlos V contra el Papa*) still not checked, as for the other letters here.

## Protocol (frozen files in FREEZE.txt; originals in French)
1. Key frozen first: `key_dudout_kb3.tsv` = our table KB3 (built 29 Oct 2026 on 9 Dec 1549 cc. 66r-67r and 23 Dec 1549 c. 76r, scored
   0.849 there), byte for byte, sha256 107a2eea... No value from this letter, no value from McBratney's key or `sign_table.tsv`.
2. PREREG (`PREREG_fr.md`, sha256 d8de2c32...) before any legible view of cc. 41-44: portion = c. 41v from line 1 until at least 300 tokens;
   pass criterion letters >= 0.85 AND >= best of 200 controls + 0.30; rank 1 below 0.85 = "partial".
3. Transcription in two passes (A on native-resolution line crops, B on full-width two-line strips without rereading A), 41v lines 1-18,
   324 tokens of which 2 are clear words; A/B agreement 306/324 = 0.944; 18 differences settled on the image, without the clear and without
   decoding; frozen (`4jul1549_41v_signs.txt`, sha256 37fcf2ea...) before c. 43v was opened. Same reader for both passes: the second pass is
   not independent in the strict sense.
4. Amendment 1 (`AMENDMENT_1_fr.md`, written after the freeze and before decoding): the only clear word inside the portion is `quod`
   (= embaxadores, line 10), so the end of the reference was fixed mechanically: letters per token on lines 1-10 (278 letters / 182 tokens)
   times the 140 remaining tokens, cut at the nearest word boundary.
5. One measurement, `score_4jul1549.py` (normalisation: accents, j=i, y=i, v=u, z=c, h dropped, doubled letters merged), seed 704.

## Result
`4jul1549_score.txt`: 322 tokens, key coverage 0.935, reference 488 letters.
**Letters 0.744, words 0.515; controls max 0.135 / 0.097; rank 1/201 on both. Under the 0.85 line: PARTIAL, not validated.**
The margin over the controls is +0.609, so the key is the right key; the shortfall is in the details below.
Daniel's strict count on the decoded passage (`4jul1549_reading_ledger.txt`, reference words classed by the alignment):
59 sure + 29 probable of 111 = **0.793 < 0.95: read in part**.

## Why it falls short (seen after the measurement; nothing re-measured)
- `cp` (c with a p-tail, 8 times) has the table value `nu`; the decipherment has **que** every time. This copyist writes que with this sign.
  Malcolm McBratney's key (`../mcbratney_27may1549/key_cv1549.tsv`, row `cslash que`, from `sign_table.tsv`) has que for the crossed c:
  his table and the decipherment agree against ours on this sign.
- New forms of this hand without a value in our table: a large looped sign `E` / `E.` (11 times), `o7`, `vn`, `G` (Gamma, probably rr as in
  `sign_table.tsv`), `Z_`, a lone `+`.
- `o-` (o then dash) was given the table value ga; on this page it is the bare letter **g** each time (tengays, pongan, luego, diligencia,
  tenga, llegada), in line with McBratney's note that g is drawn o-first and l (`dash-o`) dash-first. (This bullet corrected on 17 Nov after
  the second test was prepared: the first version said "l".)
- The end of the reference by Amendment 1 stops at "se havra de"; the decode runs on into "effectuar": a few letters are lost to the cut.

## The passage (decipherment c. 43v, our transcription; the copy's own clear words "Si ya no fuessen" before it)
"[si ya no fuessen] en camino procureys y tengays diestramente la mano que se pongan luego en el, usando dela diligencia que buenamente
pudieres, porque se pueda con tiempo dar principio ala obra y se halle en terminos de defension para el que en vuestra intencion se appunta;
y en esto convernia que se tenga muy gran secreto pro[curando que] antes dela llegada aqui delos dichos embaxadores no se suena ny entienda
que sea tal nuestra intencion, sino que solamente vienen para pedir el remedio de su bivir como arriba se appunta, y dentro de quatro o cinco
dias se os respondera particularmente y dara aviso dela forma y medio por donde y como se havra de [effectuar]"
(uncertain in our reading of the decipherment: "pro" at the line end, "suena", "nuestra intencion").

English: "... if they are not already on the way, contrive skilfully that they set out at once, using what diligence you can, so that the work
can be begun in time and be in a state of defence for the purpose you have in mind; and in this it will be fitting to keep very great secrecy,
so that before the said ambassadors arrive here it is neither felt nor understood that this is our intention, but only that they come to ask a
remedy for their government, as said above; and within four or five days you will be answered in detail and told the form and means by which,
and how, it is to be carried out."

## Second test (C13, 17 Nov 2026): KB4 on 41v lines 19-30 and c. 42r
1. **Key KB4 frozen first** (`key_dudout_kb4.tsv`, sha256 fe2552a8...): KB3 with exactly three changes, all learnt on the burnt portion
   (41v lines 1-18 against 43v) and compared with Malcolm McBratney's table (`../mcbratney_27may1549/key_cv1549.tsv` = `sign_table.tsv`, PR #684):
   `cp` = que (6 times on the burnt lines; McBratney/Daniel `cslash que`); `o-` = g (6 times; McBratney's stroke-order note);
   the looped `E` family = the r row (E re, E. ra from the burnt lines; E- re, E: ri, Eo ro, Ep ru, E_ ra by the system's rule,
   as McBratney's row "ra re ri ro ru"). One burnt E- pointed to "ne" (vienen); the rule value was kept. These three are credited to
   McBratney as agreement; no other value of his was taken. Seen on the burnt lines and **not** put in KB4: `g` read y four times, `4` read o twice.
   In-sample check on the burnt lines (not evidence): 0.807.
2. **PREREG-C13** (`PREREG_C13_fr.md`, sha256 e405e729...) frozen with the key, before any legible view of the new portion, of the lower part
   of 43v or of 44r. Thresholds unchanged: letters >= 0.85 AND >= best of 200 controls + 0.30; rank 1 below that = partial.
3. **Transcription in two blind passes**: pass A by a second, blind Claude sub-agent (Opus), which saw only the sign notes, the burnt
   lines with their settled transcription for calibration, and the new line crops (no key, no reference, no decode); pass B by the
   main agent on its own crops, frozen before A was opened. 261 tokens, agreement 228/261 = 0.874; 33 differences settled on the image
   without the plaintext and without decoding; frozen (sha256 a5e6f411...). No clear words in the portion. 41v has 30 lines, not 31.
   **Declared gap: 261 tokens, under the 300 asked**; this is all the cipher left in the letter (c. 42r has only three lines and two signs).
4. **Reference** (`4jul1549_44r_decipherment_passage.txt`): 43v ends "... como arriba se appunta y"; 44r goes on "y dentro de quatro ...
   se havra de effectuar para que lo entendays antes que por ninguna se sienta ... la que arriba se os significa". Bounds set by the written
   rule (letters-per-token rate of the first test, 488/322): the first 18 letters dropped for the 12 burnt tokens that end line 18,
   then 261 x 1.516 letters cut at the nearest word boundary (ends at "arriba se os").
5. **One measurement**, seed 1307 (`4jul1549_c13_score.txt`): 261 tokens, key coverage 0.969, reference 395 letters.
   **Letters 0.835, words 0.716; controls max 0.147 / 0.136; rank 1/201. PARTIAL (margin +0.69 passed, 0.85 not).**
   After the measurement, for information only (not a second test): with exact word bounds ("que lo ... significa") the same decode
   scores 0.870; the mechanical bounds cost the start ("que lo") and the last word ("significa"), which the decode does contain.
6. **Strict count** (`4jul1549_c13_reading_ledger.txt`): 64 sure + 20 probable + 10 restored of 94 words; **sure 0.681** (sure + probable
   0.894), under 0.95: **read in part**. Whole letter (both tests): 123 sure of 205 words = 0.60.
7. What still fails: every "y" (and) of the passage decodes as "re" from sign `g` (the y/g question above), `n` + dash vs. `n-`,
   and a few `x`/`xo`, `A` dot readings.

The 44r passage (the decipherment; abbreviations expanded): "y dentro de quatro o cinco dias se os respondera particularmente y dara aviso
dela forma y medio por donde y como se havra de effectuar, para que lo entendays antes que por ninguna se sienta; y a don Fernando se embia
copia desta para que sepa en lo que hasta agora quedamos, encargandole assimesmo el secreto, pues el y vos sabeys quanto va en ello; y en este
medio no sera sino bien que ambos penseys de donde y como se podran haver los dineros para la obra y tambien los materiales, para que no se
pierda tiempo, sin hazer obra de demostracion ni señal por donde se pueda comprehender en ninguna manera que sea nuestra intencion la que
arriba se os significa."
English: "... how it is to be carried out, so that you understand it before it is sensed by anyone; and a copy of this is sent to Don Fernando
so that he knows where we stand so far, charging him likewise with secrecy, since you both know how much is at stake; and meanwhile it will be
well that you both consider where and how the money for the work and the materials can be had, so that no time is lost, without any show or
sign by which our intention, as signified above, could in any way be understood."

## Credits
Malcolm McBratney's key and notes: an outside comparison for the first test (none of his values in KB3); for the second test the three KB4
changes (cp = que, o- = g, the r row for E) agree with his table and are credited to him; no other value of his was used.
WAINUT's work on this folder was not used for this letter. Images: Biblioteca Estense Universitaria / Lodovico Media Library (CC BY-NC-SA), study only.

## Files
`4jul1549_41v_signs.txt` (settled), `_passA`, `_passB`, `4jul1549_41v_tokens.txt` (clear words removed); `SIGN_NAMES_fr.md` (sign names);
`4jul1549_43v_decipherment_passage.txt`; `key_dudout_kb3.tsv`; `score_4jul1549.py` + `tools_metric.py`; `count_4jul1549.py`; `FREEZE.txt`.
C13 files (second test): `key_dudout_kb4.tsv`, `PREREG_C13_fr.md`, `4jul1549_c13_signs_passA.txt` / `_passB` / `4jul1549_c13_signs.txt` (settled),
`4jul1549_c13_tokens.txt`, `4jul1549_44r_decipherment_passage.txt`, `4jul1549_c13_score.txt`, `count_4jul1549_c13.py`, `4jul1549_c13_reading_ledger.txt`.
Reproduce: `python3 -I score_4jul1549.py 4jul1549_c13_tokens.txt 4jul1549_44r_decipherment_passage.txt key_dudout_kb4.tsv 1307 AR`.

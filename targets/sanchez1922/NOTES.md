# sanchez1922: [F.] Sánchez to "José González" (identified as Félix Díaz), 12 January 1922 (catalogue 1445)

WAINUT, 12 Nov 2026. Work by AI language-model agents for WAINUT; no human palaeographer checked the text.

## Document

- CEHM-Carso, Fondo DCXXI Archivo de Félix Díaz, **DCXXI.3.323.1** (archivo no. 91121). Typed letter, 2 pages,
  "Enero 12 de 1922", to "Señor Dn. José Gonzzález, N. O." (New Orleans), whom the contributor identifies as
  Félix Díaz under a cover name (inferred from the fondo and the subject; the letter does not name Díaz); signed
  "F. Vbpfihc." = F. Sánchez in cipher. The CEHM record has "Firmado por ILEGIBLE, MANUEL" and "incluye claves no descifradas". The writer
  lives in a state whose governor could suppress his paper, next to Tlaxcala, and gives a cover address in Puebla.
- Record: https://www.cehm.org.mx/Buscador/FichaBasica/91121?Tipo=A
- Images (no login, plain http): `http://visor.cehm.org.mx/assets/docx/fondos/jzd/DCXXI/3/323/1/DCXXI.3.323.1.000{1,2}.jpg`.

## System and key

Cipher words typed in lower case inside the clear Spanish. It is the system Narváez (2015, pp. 125-126) solved in
the Wellington letter DCXXI.6.588.1 of the same fondo: a Gronsfeld-type shift over the 27-letter alphabet
(A-N, Ñ, O-Z), cipher = plain + 3, +1, +3, +3, +1, +3 ..., key "313". Here the key **restarts at every word**
(commas separate the words of a name). The letter names the key in clear: "me indica anule la 103, y haga uso de
la 313 [...] desde hoy he hecho uso de ella."

Key source: Narváez's published key from another letter (a sibling key), not built from this letter, so the whole
letter is held out. `key.tsv` and `key_frozen.tsv` are the same 3 entries (shift by position in the word, mod 3:
0 -> 3, 1 -> 1, 2 -> 3). Credit for the key: Roberto Narváez (2015), cited under Prior art.
Result with the key as published, restart per word: **22 of 32 cipher words exact (68.8%),
177 of 185 letters (95.7%) in the 29 identified words**; 3 words not identified. The misses are typing slips: in
four long words the 7th or 8th shift is off the 3-1-3 cycle, three words have one wrong letter. The key 103 was
also tried: it gives no sense.

## Reading

`reading_DCXXI.3.323.1.md`, `translation_DCXXI.3.323.1.md`; `scripts/decrypt.py` (key 313, restart per word);
`scripts/check_marks.py` rebuilds the decryption and checks the marks: passes.

Words: **32 cipher words: 22 verbatim, 7 repaired, 0 from a gloss, 3 holes.** Repairs: LANDERO{U/S},
TLAX{E/C}ALA, MIXTEC{Y/A}, MARQUE{X/Z}, URDAP{Q/I}LLETA, MACHOR{P/R}{Q/O}, MAN{T/U}EL. Holes: W06 "ybld" (VAIA),
W08 "bvñdt" (YULAS, after "Lic."), W10 "fpufv" (CORCU, a surname in the cover address).

What the cipher hides: the death of General Landeros in the district of Huejotzingo (the CEHM record of DCXXI.3.330.1
mentions the death of Landeros); the plan to "nombrar una junta"; the newspaper "El Látigo" to be printed in
Tlaxcala (DCXXI.3.330.1 says El Látigo will soon come out); the incident of "our good friend Figueroa" in Veracruz;
an act from the Mixteca of Oaxaca; greetings from Miguel Gutiérrez Goitia, Manuel Márquez, Arturo Osorio, Rodolfo
Urdapilleta, Francisco Machorro and a Lic. [?]; the man who told him to use key 313 (Emilio, decoded verbatim; a typed V
overstruck by another sign stands before it and is not transcribed); the cover address "Sr. Manuel [?], Plazuela Parral # 1, Puebla" (see the pencil note below); and the signature, Sánchez.

Dan's `docs/_check_reading.py` (13 Nov 2026, after the review points were applied): reading 0.46 (23 of 50
sentences), translation 0.773 (17 of 22); on 12 Nov, before [?Baja] and the notes on it, 0.50 and 0.80 (the name lists and modern Spanish words in the
reading are what the period word lists do not know).

Pencil note, foot of p. 2 (read by the independent reviewer on an enhanced scan, 13 Nov 2026): roughly "Manuel
Co/Ro z[a]... [overwritten]   Parral". It looks like a contemporary decoding of the W10 cover address and supports
MANUEL and PARRAL independently of the key; the surname is unsure and was itself corrected by the pencil writer.
It is a partial gloss only: no word count above rests on it.

State proposed: **not prose** (names, a place, a title and one short phrase in a clear letter).

## Prior art (checked 12 Nov 2026)

- CEHM: "incluye claves no descifradas"; signer "ilegible, Manuel".
- Narváez 2015 (Documenta & Instrumenta 13, pp. 107-132) gives the key 313 for DCXXI.6.588.1 and does not discuss
  this letter. The key is his; the decipherment of this letter is new as far as we found. The CEHM records do not
  name Landeros as a general in this letter or the Sánchez signature.

## Independent review (13 Nov 2026)

An AI language-model agent working for WAINUT, separate from the solver, copied 6 of the 11 runs blind from its own
crops (W01, W04, W07, W08, W10, W11): 0 disagreements with the transcription, including the pen strokes over `xf`,
`uu` and `lw` in W07. It checked the key in Narváez 2015 (pp. 125-126), decoded W07 GUTIERREZ, W09 EMILIO and W10
PLAZUELA and PUEBLA by hand with exact results, and re-ran `check_marks.py` (passes: 32 words, 22 verbatim, 7
repaired, 3 holes). It counted 6 of 9 context sentences without holes; the other 3 have one hole each. It agreed
with the state not prose and graded the reading B. Its points, now applied: the pencil note is recorded as a
partial gloss (above); "[? Emilio]" in sentence 7 is now "[Emilio]" (W09 decodes verbatim); W06 is offered as
[?Baja] in the sentences.

## Remaining gaps

Transcription: 6 of 11 runs were copied blind by the independent reviewer (W01, W04, W07, W08, W10, W11), 0
disagreements; W02, W03, W05, W06 and W09 were not in its spot-check, and W03 (Wmdafdñb) is transcribed from the
full page only. No human palaeographer has checked the text. Who Sánchez is is open (the cover address in Puebla and
"Gral Landeros" may help a historian); that is identification, not reading.

- W06 "ybld" (VAIA) in "la Mixteca, [?], de Oaxaca" - blocker: too-short; one occurrence. The reviewer suggests
  "Baja" (the Mixteca Baja is a region of Oaxaca); with the third shift 2 instead of 3 the word gives VAJA, which
  fits "Baja" with V for B. Offered as [?Baja] in the sentences, counted as a hole.
- W08 "bvñdt" (YULAS), the name after "Lic." - blocker: too-short; one occurrence, and no single-shift change gives
  a name we can confirm.
- W10 "fpufv" (CORCU), the surname in the cover address - blocker: illegible; the pencil note at the foot of p. 2
  that seems to decode this address ("Manuel Co/Ro z[a]...", read by the reviewer on an enhanced scan) is
  overwritten at the surname.
- Pen strokes over letters in W07 (xf, uu, lw, ut), perhaps a reader's marks - blocker: illegible; not interpreted
  on the scan. The typed letters under them decode to MIGUEL GUTIERREZ GOITIA and MANUEL MARQUE{X/Z}.

## Escalation

- [x] siblings: the 12 records of catalogue entry 1445 opened at contact-sheet size (the others use number or
  number-and-letter systems; listed in duhart1921/NOTES.md); the CEHM summary of DCXXI.3.330.1 checked (Landeros, El Látigo)
- [x] clear-pages: the clear text of this letter names the key ("haga uso de la 313"); no decipherment page; the
  pencil note at the foot of p. 2 read by the reviewer as a partial gloss
- [x] known-keys: Narváez's key 313 (Wellington letter DCXXI.6.588.1) applied; key 103, which the letter says was
  dropped, tried (no sense); Argumedo's number table (Narváez 2015) does not apply to letters
- [x] print: Narváez 2015 read in full; the CEHM catalogue records; the European calendars of the standard list do
  not cover 1920s Mexico
- [n/a] key-rebuild: the key is published and fixed (3 entries); the misses are typing slips in single words, so
  there is nothing to extend
- [x] retry: the three holes retried with every single-position change of shift (0 to 4) and with key 103: only
  VAJA for W06 comes near a word (see above); YULAS and CORCU stay holes

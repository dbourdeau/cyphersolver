# 4 Jul 1549, Charles V to Ferrante Gonzaga: the cipher copy (c. 41v) decoded with a frozen key, measured against the contemporary decipherment (c. 43v)

Contributed by Brice Dudout, working with Claude (Anthropic), 17 Nov 2026. Status: **decoded, read in part**. The key passes the
rank test (1/201) but not the 0.85 letter line, so nothing here is a validated key and nothing is emended.

## The document
Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. III, cc. 40-45 (Lodovico record
fe5db48d-18d3-42dd-a058-bd9efa3c11c6, 12 canvases, CC BY-NC-SA; images used for study only and not reproduced here).
The catalogue says: "In allegato (cc. 41-44) una copia di lettera parzialmente cifrata (con testo decifrato annesso)".
- cc. 40r-40v: covering letter in clear, signed.
- c. 41r: copy, clear text; **c. 41v: a full page of cipher (31 lines)** opening with the clear words "Si ya no fuessen"; 42r: about ten more lines.
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
- `o-` (o then dash, this hand's stroke order) was given the table value ga; several places read l: the same order question McBratney notes
  for `dash-o`.
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

## Credits
Malcolm McBratney's key and notes are cited above as an outside comparison only; none of his values was used in the key or the measurement.
WAINUT's work on this folder was not used for this letter. Images: Biblioteca Estense Universitaria / Lodovico Media Library (CC BY-NC-SA), study only.

## Files
`4jul1549_41v_signs.txt` (settled), `_passA`, `_passB`, `4jul1549_41v_tokens.txt` (clear words removed); `SIGN_NAMES_fr.md` (sign names);
`4jul1549_43v_decipherment_passage.txt`; `key_dudout_kb3.tsv`; `score_4jul1549.py` + `tools_metric.py`; `count_4jul1549.py`; `FREEZE.txt`.
Next: lines 19-31 of 41v and c. 42r have not been decoded; they are a fresh portion for a second test after a key revision made on this
page (cp = que, the E family), under a new pre-registration.

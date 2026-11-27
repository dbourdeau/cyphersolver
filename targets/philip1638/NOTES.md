# Philip IV to the Count of Siruela, Madrid, 20 November 1638 (catalogue 841, AGS EST,LEG,3594,312)

Status: in progress (read in part: 884 words, 758 sure, 42 probable, 38 restored, 46 unresolved; below the 95% read bar; the unread part is the nomenclator).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct and 27 Nov 2026. Not published.

## Document

Archivo General de Simancas, Estado, legajo 3594, no. 312 (EST,LEG,3594,312; PARES 3588323), images 01-03 (04 is the back).
PARES title "Minuta de despacho cifrada". It is a despatch entirely in cipher; only the address is in clear ("Conde de
Siruela, Pariente, … mi embajador extraordinario en Génova y a los Príncipes de Italia"). Signed "Yo el Rey", Madrid,
20 November 1638. It answers Siruela's letters of 4 and 20 October 1638.
PARES record: https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3588323. Images are not reproduced here.
3594,311 (PARES 3588327) is a consulta of the Council of State on the same matter (its last page is dated 27 Nov 1638);
it paraphrases the thanks to Genoa for the episode of the French fleet and the galleys.

Subject: the negotiation with the Republic of Genoa after the French fleet tried to take galleys out of the port of
Genoa: thanks to the Republic, the dispute between the colegios and the supremos over the passes, the exchange of
prisoners, more galleys for Naples, Sicily, Genoa and Sardinia, the King's need of ports and passes for the State of
Milan, the port of Finale, and Galeazzo Giustiniani.

## System

The Genoa embassy cipher of 1638 (family of `targets/genes1638`, key K3): vowels 16-20, syllabic series of five numbers,
disguised syllables, single letters and a nomenclator of three-digit codes and underlined sigla. 312 is in the hand of
the royal chancery, which gives some signs other values than the embassy hands (ℰ = t or h, ꝓ = n, tall long-s = s).

## Key and validation

`key_K3k.tsv` (SHA-256 55df1254…), trained on declared pairs of the same chancery hand (3594,149/148, 158/157, 160/159,
151/150 pp. 1-2, 3595,308/309), frozen, then tested once on 3594,151 image 3 against its clear 3594,150 image 3, never
seen before: 0.888 of characters, 0.812 of words (normalised spelling fixed in advance; 0.877 / 0.776 without it);
200 permuted-value control keys: 99th percentile 0.313 / 0.161 (`validation/`). Two earlier frozen keys (K3h, K3j)
failed their tests (0.694 / 0.569 and 0.788 / 0.612) and were not used.
`key_K3k_read.tsv` adds values declared after the test (87 = que, 0 = a, 4 = i, 22/2 = z, 7 = f, m = s or p…).
`transcription.txt` (1,818 tokens, frozen 28 Oct 2026, SHA-256 568ba1dd…) keeps its French header lines.

## Reading

`reading.md`, line by line. Count (one mark per word, the weakest): **884 words: 758 sure, 42 probable, 38 restored,
46 unresolved** = 0.857 sure; 0.905 sure + probable; 0.948 everything but unresolved. About 45 sure words are decoded
but do not yet build a sentence (listed on 11 Nov 2026); without them, sure + probable is about 0.85.
Before 27 Nov (reading C07, 28 Oct): 758 sure, 8 probable, 57 restored, 61 unresolved.

## Nomenclator codes read through contemporary clears (27 Nov 2026)

Each code below was found in another letter of the same cipher that has a contemporary clear copy, at the same place
in the text (`nomenclator_alignments.tsv` gives the piece, line, cipher context and clear words):
106 consideración, 311 posible, 154 dicho, 293 príncipe, 75 dan, nef(s) teniendo, 262 ministro, gor carta,
nas también, mal satisfacción, 117 conveniente, 208 habiendo. The values V̲ galeras, 94 camino, 251 Milán, 321 cuanto
and 167 ere (read from the sense in C07) are confirmed the same way.
These words are marked probable, not sure: the values are outside the validated key K3k (same rule as duben1764,
27 Nov 2026). Making them sure would need a new key tested on a clear not used yet.
The pairs come from legajo 3594 (1638) and from 3595,308/309 (Leganés to Olivares, Asti, 24 July 1639), which is
another legajo but the same cipher; its clear pages 309 images 06-08 were read for this.
New cipher transcriptions made for this, each before its clear was opened: `alignments/3594-165_cipher.txt` (clear
3594,164), `alignments/3595-308_img03_cipher.txt` (clear 309 images 05-06). `alignments/3594-169_img02_l16-27_cipher.txt`
was transcribed after its clear 3594,168 had been seen (in Oct 2026).

**One contradiction.** In 3594,146 (Medina de las Torres), "se le remitiría 191" is "luego" in the clear 3594,145.
In 312 the five uses of 191 need "Francia" (el rey de 191, el residente de 191, la armada de 191); the image shows 191.
The royal chancery may use this code otherwise. It stays [Francia] (restored).

**Erratum for genes1638.** `targets/genes1638/key_K3f.tsv` has "97 = camino". The group in 3594,143 image 2 line 3 is
the same glyph "9ʒ" with a bar as the 4 of "43" on that line, and unlike the 7 of 17, 27, 37: it is 94, as in 3594,147
("en el 94 que podrá tomar" = "en el camino que podrá tomar"). The frozen key file is left unchanged; 94/97 is not used
in 3594,156.

## Remaining gaps

- 32 codes have no attestation in a letter with a clear: 282 (×2, "ocasión" from the consulta only), bis ("Armada",
  same), P̲ (×3, "Génova" from the sense), A̲ (×3), cli, du, 392, lat, 6, 76, go, ge, lest, 236, lis, 168, 324, cla, loc,
  bus, 160 (×2, "embajador" from the consulta only), 264, 300, 100, pul (×4), clu (×2), 64, 258, 197, pel (×2), 113,
  149. Most are words of the royal voice (vuestra, vos, Génova, embajador, gracias) that the ambassadors' letters to
  the King do not use. Blocker: no other royal despatch in this cipher with its clear copy is known.
- 33 places of the transcription were flagged for a second look at the image (11 Nov 2026), without seeing it. Most
  are questions of sense or of codes, not of sign shape. If every shape question went the expected way, the count
  would gain at most 4 sure words (758 → 762) and correct about 8 sure words that build no sentence; the letter would
  stay below the read bar. A blind sheet was therefore not built (27 Nov 2026). The PARES images are 963 px wide, and
  two places checked on 27 Nov ("du" line 13, "go" line 21) show the transcribed signs.

## Escalation

- Siblings with clears: every 1638 cipher letter of EST,LEG,3594 with a clear copy (142-169, 164 fetched 27 Nov) and
  3595,308/309 searched for the codes of 312 (27 Nov 2026).
- Clear pages: consulta 3594,311 (all four images): crib for 282, bis, P̲, 160 only.
- Siruela's letters of 1639 in EST,LEG,3595 marked "Descifrada" (116, 117, 128, 130 checked): clear deciphered copies
  only; no cipher original next to them, so no pair.
- Known keys: the Rome embassy keys of Philip IV (philippe4-rome-1643, OSUNA CT.2 and CT.7, letters to Siruela in
  1644-45) have another nomenclator (88, 250, 294 differ) and were not used.
- Not yet tried: the original sent to Genoa and Siruela's own papers.

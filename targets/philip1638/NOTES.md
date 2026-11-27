# Philip IV to the Count of Siruela, Madrid, 20 November 1638 (catalogue 841, AGS EST,LEG,3594,312)

Status: in progress (read in part: 868 words, 561 sure, 180 probable, 81 restored, 46 unresolved, recount of 27 Nov 2026 after review on #1024; below the 95% read bar).

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
`key_K3k_read.tsv` adds values declared after the test (87 = que, 0 = a beside 0 = b, 4 = i, 22 = z, 2 = z, 7 = f,
n = z, m = p beside m = s): it is the key the reading uses (`outcome.key_file`). On 27 Nov 2026 its m line was written
`s|p`: the copy had replaced K3k's m = s by p, while the reading takes m as s in most places. ʒ = a is already in K3k.
`decryption.txt` is `key_K3k_read.tsv` applied to `transcription.txt` by `decode.py`, token by token, nothing edited
(69 lines, 1,818 tokens, 116 without a value).
`transcription.txt` (1,818 tokens, frozen 28 Oct 2026, SHA-256 568ba1dd…) keeps its French header lines.

## Reading

`reading.md`, line by line; English translation in `translation.md`. Count by `count_words.py` (one mark per word,
the weakest; a word cut at a line end counted once): **868 words: 561 sure, 180 probable, 81 restored, 46 unresolved,
307 holes, 0.646 sure**; 0.854 sure + probable.

Recount of 27 Nov 2026, after Daniel Bourdeau's review (#1024), with one rule for values outside the validated key:
- Before: 868 words (884 when the halves of a word cut at a line end were counted apart), 742 sure, 42 probable,
  38 restored, 46 unresolved (0.855; 0.857 by the old split).
- 138 sure words that rest on a value added after the test (87 = que 48 tokens, 0 = a 82, 4 = i 18, m = p 15, 22 = z 8,
  n = z 6, 7 = f 3, 2 = z 1) are now probable, as the period-clear codes already were. The words were found by aligning
  `decryption.txt` with the reading line by line; an alignment can place a token one word off, so the figure is
  within a few words.
- 43 sure words where the reading departs from what the key gives for the signs as transcribed are now marked [x]
  (holes), among them the three Daniel Bourdeau named: L07 "si lo vno" read "[y] lo [que]", L26 "heteido" read
  "he te[n]ido", L29 "assi de" read "[año] de". The others: n (= z) read d five times (a[d]mitirla, a[d]mitirle,
  serenida[d], a[d]vierte, po[d]ría); the unvalued t read c five times (es[c]rito, a[c]reciente, es[c]ribe, es[c]-ribir,
  es[c]ribiran) and ꝯ read ge/je (reco[ge]r, re-se[je]cutando); 9 (= c) read m or n (ro[m]per, desco[m]prar, e[n]vía);
  vowels changed (p[e]lo, qu[i]ero, com[u]nicar, algun[o]s, cas[o], re[u]nidas, [e]stas, cu[a]rtel, aqu[í] twice,
  est[a]r for 2 = z, [se] for 38 = so); letters added (te[n]dido, ente[n]der, [a]cuerdo, [l]o, di[fe]rencia for the
  unvalued exo, [i]nstant[e], [pre]cisamente); S̲ = genovesado read genoves[es] twice; whole words not given by the key
  ([entendiendo] for "en se g u n do", [esa] for "s h|t a", [hallado], [t]as for 32 = ci).
- ʒ = a is in K3k (line 193), so its words stay sure.
Before 27 Nov (reading C07, 28 Oct): 758 sure, 8 probable, 57 restored, 61 unresolved, by the old split.

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

## Transcription doubts

The 33 places flagged on 11 Nov 2026 (`A-REVOIR-IMAGE`, from the decode, before the image was looked at). Two were
checked on the image on 27 Nov 2026; the other 31 are not checked, and their words keep the marks they have in the
reading. The PARES images are 963 px wide.
- 36 bat ꝓ (L02) - read: bat (= razón); not checked on the image; checked: decode; a sigil other than bat ("hallan") would fit the sense
- 208 37 48 x ho (L07) - read: 48; not checked on the image; checked: decode; 43 for 48 would give "sido uno"
- A̲ (L07, L12, L13) - read: A̲, unresolved; not checked on the image; checked: decode; three uses that one value does not fit; L13 may be H̲
- A̲ 15 47 85 43 (L12) - read: as transcribed; not checked on the image; checked: decode; 15 47 (o li) to look at
- du (L13) - read: du; checked: image, decode; the image shows du (27 Nov 2026); clu (bien) was the expected reading
- 43 λ 255 (L13) - read: as transcribed; not checked on the image; checked: decode; a sign (11 = y) may be missing
- 392 20 ℓ (L14) - read: 392; not checked on the image; checked: decode; a code over 326 is out of the code's zone
- lat, 16̊ 18̊ 10̊ 16̊ (L16-17) - read: as transcribed; not checked on the image; checked: decode; lat may be lac; crossed figures
- 88 33 r 166 (L17) - read: 88; not checked on the image; checked: decode; 85/86 (que) for 88 (de) would give "y que con efecto"
- 8 V̲ ℓ 0 ha 26 33 / 15 6 (L17-18) - read: as transcribed; not checked on the image; checked: decode; builds no sentence; 8 and 6 letters or figures
- go (L21) - read: go; checked: image, decode; the image shows go (27 Nov 2026); yo (la tiene rota conmigo) was the expected reading
- ge (L22) - read: ge; not checked on the image; checked: decode; ye would give p-re-cisamente
- 51 ins 41 65̊ (L29) - read: as transcribed; not checked on the image; checked: decode; a sigil for año, and a crossed 25 for 65, would fit
- 36 30 39 50 45 222 (L36) - read: as transcribed; not checked on the image; checked: decode; "se ca su al la junta" builds no sentence
- 265 m (L39) - read: as transcribed; not checked on the image; checked: decode; "nuevos" or "de nuevo"
- 166 25 mal 41 45 ℓ H m 3 32 0 ℓ (L41) - read: as transcribed; not checked on the image; checked: decode; builds no sentence
- 20 r 263 (L42) - read: as transcribed; not checked on the image; checked: decode; "en mente" ends a sentence badly
- λ 16 ℰ 45 an 3 ℰ 18 (L43) - read: as transcribed; not checked on the image; checked: decode; ℰ for ꝓ/r and 18 for 16/20 would give "En la parte"
- 0 20 ℓ ℰ 16 160 (L43-44) - read: 160; not checked on the image; checked: decode; 160 (embajador) gives no sentence here
- 238 (L45, L64) - read: 238 (= liga); not checked on the image; checked: decode; the same code in two places that read differently
- ilt ya (L47) - read: ilt; not checked on the image; checked: decode; nlt (avisa) would give "se os avisará"
- ℓ H 2 3 (L51) - read: 2; not checked on the image; checked: decode; ʒ for 2 would give es-t-a-r (the reading marks est[a]r)
- ℰ 19 at 3 (L52-53) - read: 19; not checked on the image; checked: decode; 15 for 19 would give "tomar acuerdo"
- 36 vn 33 r (L56) - read: vn; not checked on the image; checked: decode; a verb is expected (reading [van])
- 0 45 3 c x 20 39 m 20 8 46 (L57) - read: as transcribed; not checked on the image; checked: decode; builds no sentence
- 31 3̊ 0 43 (L58) - read: as transcribed; not checked on the image; checked: decode; crossed 3 as rr? (reading ce[rr]ado)
- x r + r ℓ mab (L59) - read: +; not checked on the image; checked: decode; the sign + (in?) for "un instante"
- pel 11 ye λ ℓ (L60) - read: as transcribed; not checked on the image; checked: decode; a 4 or g (i) may stand before ℓ
- un 27 75 (L63) - read: 27; not checked on the image; checked: decode; 20 for 27 would give "puedan escribir"
- at hi pul 238 (L64) - read: as transcribed; not checked on the image; checked: decode; builds no sentence
- 20 9 27 ʒ; t ye ℰ 20 r 32 ʒ (L65) - read: as transcribed; not checked on the image; checked: decode; 9 as ꝓ (e-n-bía, reading e[n]vía); ℰ as n/tt in credencia
- 321 9 48 (L67) - read: 9; not checked on the image; checked: decode; 0 (a) for 9 would give "en cuanto a lo que toca"
- 33 9 m ya 3 (L68) - read: 9; not checked on the image; checked: decode; 9 as 8 (l) would give desculpar (reading desco[m]prar)

## Remaining gaps

- 32 codes with no attestation in a letter with a clear - blocker: open-codes; 282 (×2, "ocasión" from the consulta
  only), bis ("Armada", same), P̲ (×3, "Génova" from the sense), A̲ (×3), cli, du, 392, lat, 6, 76, go, ge, lest, 236,
  lis, 168, 324, cla, loc, bus, 160 (×2, "embajador" from the consulta only), 264, 300, 100, pul (×4), clu (×2), 64,
  258, 197, pel (×2), 113, 149; most are words of the royal voice (vuestra, vos, Génova, embajador, gracias) that the
  ambassadors' letters to the King do not use, and no other royal despatch in this cipher with its clear copy is known
- 180 probable words, 138 of them resting on the values added to the key after the test - blocker: no-key-material;
  making them sure needs a new key, with these values in it, tested on a clear not used yet
- 31 of the 33 transcription doubts of 11 Nov 2026 not checked on the image - blocker: not-attempted; list under
  "## Transcription doubts"; most are questions of sense or of codes, not of sign shape; if
  every shape question went the expected way the count would gain a few sure words (11 Nov count: at most 4) and the
  letter would stay below the read bar, so a blind sheet was not built (27 Nov 2026); the two places checked on
  27 Nov ("du" line 13, "go" line 21) show the transcribed signs

## Escalation

- [x] siblings: every 1638 cipher letter of EST,LEG,3594 with a clear copy (142-169, 164 fetched 27 Nov) and
  3595,308/309 searched for the codes of 312 (27 Nov 2026); Siruela's letters of 1639 in EST,LEG,3595 marked
  "Descifrada" (116, 117, 128, 130 checked) are clear deciphered copies only, with no cipher original next to them
- [x] clear-pages: consulta 3594,311 (all four images): crib for 282, bis, P̲, 160 only
- [x] known-keys: the Rome embassy keys of Philip IV (philippe4-rome-1643, OSUNA CT.2 and CT.7, letters to Siruela in
  1644-45) have another nomenclator (88, 250, 294 differ) and were not used; genes1638 K3f is the same family
- [ ] print: no edition of the despatch searched beyond the PARES record and catalogue 841
- [x] key-rebuild: K3k learnt on declared pairs and frozen before its held-out test (K3h, K3j failed); values added
  after the test are in key_K3k_read.tsv and count as probable
- [ ] retry: the unread groups were not retried with a new key; not yet tried either: the original sent to Genoa and
  Siruela's own papers

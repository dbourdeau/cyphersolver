# chateauneuf1691 — Châteauneuf (Castagnères) at Constantinople/Adrianople, 1691-1694: the five "non déchiffré" pieces of AE/B/I/381 (catalogue 539)

Source: Archives nationales, AE/B/I/381 (Correspondance consulaire, Constantinople, 1691-1694), reproduction ordered by Brice Dudout (51 JPEG, received 20 Nov 2026). Images are not distributed; cite « Archives nationales, AE/B/I/381 ».

## The code
One numeric nomenclator (groups 3-368) for all five pieces, 1691 to 1694, for letters to the King and to Pontchartrain alike: low numbers single letters with homophones (a = 9, 16; s = 22, 45, 47, 49; n = 20, 38; e = 29, 36; t = 27, 50 ...), middle numbers syllables (104 re, 107 ce, 138 de, 333 que, 342 oit), high numbers words and names (275 vizir, 284 seigneur, 285 venitiens, 301 majesté, 325 vaisseau, 328 empire, 332 ottoman, 345 Venise, 362 occasion). 365-368 and 355 behave as nulls (context only). 355 is a null in `key.tsv` and in `decryption.txt` (shown as ‹355›). KEY_v1 and KEY_v2 (`prereg/`, frozen by hash) still carry 355 = "a", which the EM alignment took from its one occurrence in f. 376 (0377 L1, after "Benincasa"); in the five pieces "a" gives "re-a-lution" (0154 R3) and nothing sensible at 0154 R4, 0154 R12, 0232 S1 and 0242 R1, so the reading treats it as a null and counts no word on it. The frozen measure used "a". Part of the letter range runs in alphabetical steps of 5: a 16, b 21, c 26, d 31, e 36, f 41, g 46, i 56; and a 9, b 14, c 19, d 24, e 29 (observation, not used to fix any value). It is not the Louis XIV -> Castagnères code of 1690 (Tomokiyo, Cryptiana louisxiv2; "le" = 195 there, 91 here).

## Key source and measure (pre-registered, prereg/)
- Key source: the period interlinear decipherment of the letter of 17 Jan 1694 (f. 376, 119 cipher lines, ~1,546 groups; key_source/gloss_376.txt). Alignment of number runs with gloss letters by EM over monotone segmentations (tools/em.py), then hand curation -> KEY_v1 (169 codes).
- PREREG (SHA-256 in prereg/SHA256SUMS_prereg.txt) written before any key: held-out portion = all of f. 452 (21 Sep 1694, 457 groups, glossed); one measure; character agreement after normalisation; 200 controls by permuting the key values; pass iff >= 0.85 AND >= best control + 0.30.
- Result (prereg/MEASURE_452.txt): **0.830 vs best control 0.102 — FAIL at the pre-registered bar** (margin over controls met, absolute bar missed by 0.02). The decode is visibly correct French; the shortfall comes from codes left out of KEY_v1, among them three common values attested in the f. 376 gloss that were omitted by oversight during curation (81 la, 50 t, 70 guerre). f. 452 is burnt; no other glossed portion was ordered, so no second measure is possible.
- KEY_v2 (post-measure, not validated): KEY_v1 + 14 values added after the measure: 6 from the f. 376 gloss that KEY_v1 left out (81 la, 50 t, 70 guerre, 233, 217, 353) and 8 read from the f. 452 period decipherment (145 turc, 209 françois, 270 iu, 276 bo, 318 estat, 3 il, 109, 262) (`prereg/KEY_v2_additions_sources.json`). Values fixed from context only (11 il, 43 o, 103 ont, nulls) are listed in key.tsv and counted as holes.

## Transcription of the undeciphered pieces
Two independent blind passes (P1 forward, P2 reverse order, AI agents without key) and a blind arbiter on the 12 disagreements/gutter places (blind/). 597 groups; 13 diff blocks between passes, settled by the arbiter; 4 groups lost in the binding.

## Result
Read in part. 240 of 272 cipher words sure (0.882): f. 152 135/151, f. 155 26/30, f. 232 31/35, f. 239 13/18, f. 433 35/38 (reading.md). No period decipherment of these five pieces exists in the volume (inventory: "la partie chiffrée n'est pas déchiffrée").

## Historical gist
1691: Châteauneuf proposes to Louis XIV that the Venetians (at war with the Porte) lose the French protection under which some 200 of them still traded at Constantinople "by tolerance", and that their Levant trade pass instead on French ships with passports from La Haye (ambassador at Venice) or himself, with penalties for French merchants lending their names; the King answers that no consent may give up rights stipulated by the capitulations. 1692: Fabre is to keep Venetian ships out of Ottoman ports under any (French, English, Dutch) flag without Châteauneuf appearing to have consented; the Venetian siege of La Canée had stirred the Turks against Venice. 1694: Châteauneuf avoided pressing the Vizier while the enemies spread the rumour of an imminent French peace.

## Remaining gaps
- Code groups 305, 280, 177, 69, 57, 146, 152, 61, 64, 33, 59, 196, 108, 232, 166 have no value - blocker: open-codes; each occurs in these five pieces only, and no glossed letter of the volume carries it
- Four groups lost in the binding (0233 L, 0243 L, 0439 L) - blocker: illegible; the gutters are cut in the reproduction, a flat re-shoot is needed
- Validation of KEY_v2 - blocker: needs-physical-access; the 16 other glossed pieces of AE/B/I/381 (f. 131, 222, 261, 289, 317, 325, 330, 339, 398, 400, 409, 422, 425, 448, 470, 472) are not ordered, and f. 452 is spent; they would give a fresh held-out portion
- 355 = null rather than "a" - blocker: open-codes; one occurrence in the glossed letter, no second glossed letter to test it on
- Whether the reproduction may be analysed with an AI assistant - blocker: not-attempted; not raised with the Archives nationales (see Conditions of use of the images)

## Escalation
- [x] siblings: the five pieces compared with each other; one nomenclator found for 1691 to 1694
- [x] clear-pages: clear passages of the pieces and the inventory (FRAN_IR_003977) read; no decipherment of these pieces
- [x] known-keys: the period decipherments of f. 376 and f. 452 of the same volume used as key source; the 1690 code (Tomokiyo) compared and is a different code
- [x] print: catalogue 539 vetting (2 Nov 2026) found no edition or decipherment of these pieces
- [x] key-rebuild: KEY_v1 frozen, one measure, KEY_v2 built afterwards (post-measure, not validated)
- [ ] retry: no fresh glossed portion, so no second measure; waits on the 16 pieces above

## Conditions of use of the images
- Source: Archives nationales, AE/B/I/381. Brice Dudout ordered the reproduction on 2 Nov 2026 through the Archives nationales' online inventory service (reproduction no. 102 974 276), as an ordinary digital file, declaring private use. The invoice (RE-2026-0337, 30.20 EUR for AE/B/I/381 and AE/B/I/414) was paid by Brice Dudout on 17 Nov 2026, and the 51 JPEG files arrived on 20 Nov 2026 by a download link.
- No written conditions of reuse came with the files or with the invoice e-mail, as far as our records show; we have not read the invoice PDF or the delivery message for terms. Whether reuse of the images is allowed has not been confirmed, so the images are not committed or distributed (the files give shelfmark and image numbers only).
- Nobody has agreed to AI analysis: the question was not put to the Archives nationales. AI analysis was not raised with the archive. The pieces were transcribed and read with AI assistants on the strength of the private-use order alone.

## File map for the hashes
`prereg/SHA256SUMS_prereg.txt` was written in the working folder, where the transcriptions sat in `transcr/`. In this
folder they are `key_source/` (gloss_376.txt, gloss_452.txt, CONVENTIONS.md) and `blind/` (blind_P1.txt, blind_P2.txt,
arbiter.txt). Eight of the nine hashes match the files here: PREREG.md, gloss_376, gloss_452, both blind passes,
the arbiter, KEY_v1 and the final KEY_v2. `key_source/CONVENTIONS.md` does not match. It was edited after hashing,
and its text is the transcribers' instructions only. It is not an input to the key or the measure.

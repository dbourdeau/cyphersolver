# duben1764, system B — 13 Nov 2026 (Brice Dudout, Claude Opus 5.5): the clear of 121-124L is on images 127-128

## Finding
Images A0073297_00127-00128 carry a clear French text headed by an archivist's note "Tillhör brev av den 31/12 1764"
(received/answered "28 Jan 765"). It is the plaintext of the Chiffer n:o 2 cipher pages 121, 122L, 123R, 124L, 122R
(1,247 groups; Daniel's tx/c-chiffer2-121-124.txt): "Vous verrez avant l'arrivée de celle-ci que non seulement j'ai prévenu
les ordres du Roi au sujet du Comte Osterman…" to "…pour m'être rendus à mon retour". The profile's "No decipherment" for
this document, and our 12 Nov "read in part" (59.4% sure), are superseded: the letter is fully read from a contemporary clear.
Cipher order differs from the page order: the clear ends with the content of 122R (so the cipher reads 121, 122L, 123R, 124L, 122R).
The cipher sometimes follows the draft before its corrections (e.g. "qui n'a ce[ss]e d'insinuer", "l'a bien profité", "m'en retourner").

## Protocol and the one measure (frozen/)
- 21:44 CET: PREREG.md (a lexical split-half test inside 121-124L) frozen; 21:46: N_draft.json, 15 values read from context in
  121-122R only; 21:49: image 127 seen; 21:51: PREREG-AMENDEMENT-1.md frozen (French): lexical test cancelled unrun; one
  re-test of the 12 Nov key on a NEW text: key_systemB_c03.json (built on 118.00-119L.06 only, SHA b7fd19b0…) against the clear
  127-128, metric and thresholds of the 12 Nov measure (difflib blocks >= 4 letters / clear length; 200 permuted keys +
  200 shuffled orders, seed 1231; pass if M >= 0.35, M > max control and margin >= 0.15).
- Clear transcribed twice (127-128_passe1 from 1200 px views, passe2 from 1800 px bands without looking at pass 1; differences
  were notation of deletions plus "leur/leurs" and a phantom "des", settled on the image); final and normalised text (2,578
  letters) hashed before the run (SHA256SUMS-PREREG).
- Result (measure_result_c04.json): **M = 0.5353 vs controls max 0.0593** (permuted keys mean 0.0375, shuffled mean 0.0409);
  1,032 of 1,247 groups known to the frozen key. VALIDATED. Descriptive: with the 25 values added on 12 Nov from context
  (c03b additions) M = 0.6943 vs max 0.0784 — those context values were mostly right.
- N_draft.json (written before the clear was seen): 14 of 15 values confirmed by the clear (376 or, 202 es, 137 er, 347 ha,
  730 eu, 40 fru, 393 tu, 114 ont, 6 res, 3 ne, 633 g, 505 son, 620 id, 305 dans); wrong: 62 (vu; the clear gives "affaires").

## Key completed after the measure (key_systemB_c04.json, changes in key_systemB_c04_changes.json)
Alignment of the cipher to the clear (scripts/align_clair.py; align_121-124L_to_127-128.json), then value-by-value review:
about 100 values added or corrected (S = 2+ occurrences or whole word, P = single occurrence). Notable corrections of the
12 Nov key: 3 = ne (was null), 12 = con, 320 = fi (was c), 383 = ance, 402 = ci, 437 = ri (was rri), 523 = ar, 118 = vi
(was nn), 137 = er, 142 = oient, 245 = null/stop (was ce), 669 = imperatrice (whole word), 730 = eu (was r). Code words:
53 Fersen, 571 Stachieff, 87 Diète, 679 million, 762 Princesse, 568 intention, 74 chagrin, 81 souverain(eté).
Coverage: 1,236 of 1,247 groups (99.1%); decode vs clear M = 0.946 (circular, descriptive). As an outside check, the 5 Oct
1764 letter (118-119R, not used for the c04 changes) rises from 0.699 (key c03) to 0.825 (key c04) against its clear on 120.
Unresolved: 481 150 761 ("28 Novembre"), 790 + 315 ("31", with a struck word), 236 (three different contexts), 339, 55, 234;
split of a few date and name groups uncertain.

## Reading
decode_121-124L_key_c04.txt follows the clear group by group; the reading is the contemporary clear (frozen/127-128_final.txt),
English translation reading_121-124L_en.md. Status of the document: read (contemporary clear found in the same volume;
nothing new in content, contribution = identification of the clear, a second validation of the system B key, the completed key).
Note: scripts carry absolute local paths of the contributor's working folder.

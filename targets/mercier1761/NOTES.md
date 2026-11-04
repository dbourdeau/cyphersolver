# La Touche and Le Mercier de La Rivière to the minister, Martinique, 12 June 1761 (ANOM C8 A 64 f° 1)

Status: read in part (92.2% of tokens read as sense, measured 27 Oct 2026; key recovered from adjacent plaintext; write-up mercier1761.html, 27 Oct 2026)

Unsolved Catalogue no. 542 (research/central_archives sweep, Oct 2026).

## Document

- Archives nationales d'outre-mer, COL C8 A 64 f° 1 (Correspondance à l'arrivée, Martinique). Digitised:
  ark:/61561/zn401b233uu, five images FRANOM23_C8A_064_0001-0005 (FranceArchives component
  a6723569c4eb8c23ca454a7927a681687ae15cdf). Images are served behind an Anubis proof-of-work page; they open in
  a normal browser. Not downloaded into the repository.
- *Duplicata*, "à la Martinique ce 12 juin 1761", "Mrs de la Touche et de la Rivière" to "Monseigneur": Nicolas René
  Berryer, secretary of state for the Navy (Nov 1758 to Oct 1761; Choiseul took the Navy in October 1761). The
  cipher names "M. le Duc de Choiseul" as the minister who had promised provisions. Signed Levassor de La Touche (governor general of the Windward
  Islands) and De La Rivière (intendant). FranceArchives gives the date range as 1762 (the volume's date); the
  letter itself is dated 12 June 1761.
- Clerk's notes at the top left: "Mr Accaron ... 29 avril ..." (unsure) and **"déchiffrée et remise à M. Accaron par
  M. Villain"**: the bureau deciphered it on arrival and gave the decipherment to Accaron (premier commis of the
  colonies bureau). That decipherment is not filed with the letter, and the inventory says the letter "n'a pas été
  transcrite en clair".
- Content (inventory and clear passages): the British are massing forces at Dominica for an attack on Martinique;
  Belle-Île "pris ou manqué"; a second convoy from New England; provisions bought at prices fixed with the help of the
  négociant Dutasta, who waived his commission; prisoners. P.S. in clear: Sainte-Lucie well supplied; 300 prisoners of
  war held. A second hand adds that many papers relating to this letter left the same day, the duplicates were not
  ready, and this letter goes double.

## System

- Clear French letter with long enciphered runs (images 2-5): **818 code groups, 217 distinct, values 11-696**
  (measured from `groups.txt`). Groups are 2- or 3-digit numbers separated by commas, no other signs. Four groups
  are added above the line with a caret (corrections by the encipherer).
- Clear words sit inside the code: "423, D.. 614. Choiseul" (so 614 is most likely *de*: "M. le Duc de Choiseul"),
  "consommation", "Nous avons ajouté", "il est ... à croire que le public", "établi sur des faits bien calculés".
- Frequency: 674 ×65 (8%), 614 ×28, 280 ×27, 114 ×23, 321 ×21, 541 ×18. Repeats: "114 491 280 674" ×4,
  "128 234 125 328" ×3, "255 541 160" ×2, "357 529 535 (636) 469 200 674" ×2, "16 478" ×3.
- Reading: a numerical nomenclator of ~700 entries, almost certainly two-part (disordered), syllables plus words,
  like the printed Navy form used for Martinique in 1765 (below).

## Key material looked for

- **1765 Martinique key, ANOM C8 A 67 f° 178** ("Chiffre utilisé pour les correspondances avec M. d'Ennery", with its
  clef; ark:/61561/zn401jdcfjgj, images 0280-0283). Printed two-part syllabic nomenclator, values 1-~800, numbers
  filled in by hand. **Does not fit**: there 614 = voisins, 674 = trou, de = 428, and values run past 700 (ab 743,
  cha 742, dre 755), while this letter's 818 groups never exceed 696. Partial transcription of its deciphering table in
  `key1765_ennery.tsv` (vocabulary for a solver).
- Sibling letters from La Touche and La Rivière, Feb-July 1761 (C8 A 63 ff. 1, 2, 6, 9, 17; C8 A 64 ff. 1, 4): none
  is described as ciphered. C8 A 64 f° 4 (17 July 1761) checked: clear. Volumes C8 A 63 and 64 not yet swept
  image by image for other cipher pages.
- **Lead, not online: Archives nationales MAR/G/178**, "Chiffres employés dans les dépêches aux diverses colonies,
  1741-1776": keys used with Froger de l'Éguille (1758), Law de Lauriston (1766), Nozières (Guadeloupe, 1771), and a
  printed Traité du chiffre (1776). The 1761 Windward Islands key may be there or be the 1758 one. Needs a reading
  room visit.
- The decipherment made by Villain for Accaron would have gone into the bureau's files (C8 A, C8 B, or the
  ministry's working papers); not found in the online inventory.

## Key from the sibling letter (27 Oct 2026)

- **ANOM C8 A 63 f° 208** (ark:/61561/zn401g8z62m, images 0374-0375): Le Mercier de La Rivière to the minister
  (Berryer), no. 178, Martinique 21 August 1761, "(chiffrée)" in the inventory. Same code as the target, with a
  **contemporary decipherment written above each code line**. Its 19 clear|code pairs are in `sibling178_pairs.txt`.
- Aligning those pairs gave about 110 values (`key1761.tsv`, each with confidence A/B/C and its evidence).
  Anchors: "Saint Eustache" = 371 201 674 361 313 (three times); 614 = de (so the Choiseul crib holds); 423 = le
  ("423 D.. 614 Choiseul" = le Duc de Choiseul); 674 = s. The code mixes letters (s, r, m, p, n, b, d…), syllables
  (ma, che, ro, te, ment, tion…) and whole words (notre, avec, pour, colonie, farines, vivres, dans…).
- Applied to the target this values 67% of the tokens at once. Context in the target then gave more, each from
  repeated phrases: 491 vo ("nous avons", "nous devons", 7 times), 340 so + 667 tion ("consommation", 4 times; the
  word also stands in clear), 234 i + 306 an ("soixante", "croire"), 357 é + 535 ant ("étant venus", twice),
  31 di + 15 ge ("diligence"), 128 mo + 54 g + 337 mon ("Monseigneur" twice, "moitié" 4 times), 259 cu
  ("spéculation", "calculer"), 482 ar ("arriver", twice), 123 cha ("de change", twice), and others.
- **Final pass (27 Oct): 771 of 818 valued (94.3%), 754 read as sense (92.2%).** The measurement now accepts elided
  l' d' n' s' … only before a vowel, and a declared list of words missing from the corpus sample or spelled as in the
  letter (see `measure_sense.py`).
- Retry round (27 Oct): 761 of 818 valued (93.0%), 709 read as sense (86.7%, earlier measurement). Earlier figures follow.
- **Measured before the retry (27 Oct, after three context rounds): 729 of 818 tokens valued (89.1%, `apply_key.py`); 667 of 818
  read as sense (81.5%, `measure_sense.py`: each decoded run is segmented into dictionary words; a token counts
  only if every character it yields falls inside a word).** Corrections made on the way: 541 is u, not eu; 552 is
  lettre, not vision; 496 is su, not suis (the sibling alignment had these wrong). Working text in
  `reading_draft.txt`, line by line in `reading_lines.txt`, failing groups in `sense_measure.txt`.
- Draft reading, opening of the cipher: "Les vaisseaux espagnols que vous nous aviés annoncé, Monseigneur, n'étant
  venus, les secours en vivres promis par M. le Duc de Choiseul ne nous étant point venus, nous n'avons de vivres ni
  en [408] ni [451] dans la colonie que pour la consommation courante … Dans cette position nous avons [c…] de … de
  Saint Eustache de nous faire passer en toute diligence trois mille barils de farines et douze cent barils de beuf;
  la farine à soixante livres le baril, le beuf à cent livres le baril." Later: "il est à croire que le public payera
  l'un et l'autre plus cher, à moins qu'il ne survienne en [339] une révolution …", "si nous ne sommes [534]s qu'en
  Décembre il faudra fournir à la consommation …", "nous devons croire que nous le serons vigoureusement",
  "nous aurons alors au moins dix [315] … à nourrir", "la longueur d'un siège", "moitié en lettres de change et
  moitié argent ou denrées", "ce n'est pas un petit travail", "nous croyons, Monseigneur, qu'il serait superflu de
  plaider auprès de vous l'[110] et l'exactitude sur les payemens de lettres de change; vous en sentez [403]nement
  toute la [154]."
- Also legible: the provisioning from Saint Eustache ("…nous avons [c-?] de … de Saint Eustache de nous faire
  passer en toute diligence trois [437] … de farines…"), prices ("la farine à soixante livres le baril, le bœuf à
  [424] livres le baril"), consumption ("calculer les consommations"), payment "moitié en provisions … moitié …
  soit en denrées soit en argent", "lettres de change", and an appeal to the minister ("nous croyons, Monseigneur, …
  plaider auprès de vous … l'exactitude sur les payements…").

## Ciphertext-only attack (26-27 Oct 2026)

- `solve.py`: simulated annealing over the map code group -> unit of the 1765 Navy form (all 800 entries
  transcribed in `key1765_ennery.tsv`, 791 distinct units), one unit per group. Score: shared `fr-modern` LM (order 5,
  no spaces) over the whole letter stream with the clear passages in place, plus a unit prior from segmenting
  fr-gutenberg; optionally a word-segmentation score (`wordscore.py`).
- **Control fails.** Held-out French of 1757 (d'Affry despatches, `targets/affry1757/corpus_fr.txt`) was segmented into
  the same units and enciphered in the letter's exact shape: 818 tokens, 218 types (letter 818, 217).
  - Character model plus prior, 1M iterations: 7.7% and 8.9% of tokens correct.
  - Adding the word score ×3: 7.3% and 4.8% correct.
  - In every run the key the solver found scored higher than the true key. The objective cannot tell the true text
    from French-looking word salad at this length with ~790 candidate units. This is not a search problem.
- The same solver on the letter gives word salad, with 614 = "es" against the Choiseul crib. Since the solver
  fails its control, that output means nothing (`run_letter_1.txt`, kept for the record).
- Conclusion: a vocabulary-free or proxy-vocabulary ciphertext-only break of a ~700-entry two-part code is out of reach
  with 818 tokens. A reading needs key material: the 1761 key itself, a deciphered sibling, or the ministry's clear
  minutes.

## Prior art

Web search (26 Oct 2026: shelfmark, correspondents, date, "chiffre" + Martinique 1761) found no published
decipherment. Not on DECODE. Not on cryptiana.

## Remaining gaps

- About 40 single-use word codes (47 of 818 tokens): 408/451 ("ni en [408] ni [451] dans la colonie"), 339 and 75 ("en [339] une révolution … qui nous arrive en [75]"), 100 and 511 ("l'[100]ce[511] est à notre porte"), 183, 403, 154, 110, 138, 413, 459, 638, 82, 173, 199, 245, 223, 600, 267, 670, 161, 462, 317, 404, 195, 516, 180, 685, 232, 336, 44, 449, 264, 327, 439, 523, 345, 480 - blocker: no-key-material; each occurs once, in a context that admits several words, and the 1761 key is not online (sibling and context exhausted)
- C-grade values resting on one context (441, 273, 145, 463, 303, 642, 525, 193, 657, 409, 394, 581, 11, 60, 664, 430, 30, 515, 509, 85, 330, 527, 20, 146, 675, 88, 540, 392, 122) - blocker: no-key-material; no second occurrence in the two letters to confirm them
- Two encipherer slips, checked on the image: "à r-ro-i-s livres" (321 where t is meant) and "nous [16]frons" (offrons) - blocker: no-key-material; the groups are clear but wrong as written; read by sense, marked [?]
- The 1761 key itself, COL B 113/114, MAR/G/178 - blocker: needs-physical-access; not digitised

## Escalation

- [x] siblings: the seven 1761 joint letters listed; C8 A 64 f° 4 opened (clear); inventory search of C8 A 62-65 found C8 A 63 f° 208 with interlinear decipherment, transcribed and aligned. Image-by-image sweep of C8 A 63 (831 images) and 64 (601) not done.
- [x] clear-pages: the clear passages of the letter (images 1-5, P.S.) checked: the letter's own clear text, not a decipherment; the margin note says the decipherment went to Accaron and is not filed here.
- [x] known-keys: 1765 Martinique key (C8 A 67 f° 178) tested and ruled out (614 = voisins, values to 800); no other colonial key of 1755-1765 online; MAR/G/178 (1758/1766/1771 keys) offline.
- [x] print: web search on shelfmark, correspondents, date and "chiffre" + Martinique 1761; FranceArchives; nothing printed.
- [x] key-rebuild: key rebuilt from the sibling's interlinear decipherment (~110 values) and extended from context in three rounds with kwic.py (89.1% valued, 81.5% sense measured); ciphertext-only annealing tried first and failed its control.
- [x] retry: the three odd spots re-checked on the images (two encipherer slips, one confirmed); every open group dumped with kwic.py and retried in context; 22 values added; re-measured 93.0% valued, 86.7% sense; a final pass added attaqué/mille/voi and C-grade values: 94.3% valued, 92.2% sense. Single-occurrence word codes remain, not filled to avoid guesses.

## Brice Dudout: d'Ennery 1765 key corrected (credit added 4 Nov 2026)

Brice Dudout transcribed the d'Ennery key (`key1765_ennery.tsv`) independently from both ANOM C8 A 67 f. 178 tables
(enciphering table 0280, deciphering table 0282) on 29 Oct 2026. 770 of 800 values agree; 7 values were corrected and
confirmed on the enciphering table (413 leur, 535 ba, 89 xu, 235 ol, 349 i, 679 e, 652 préten), with the place name
786 Larcher. The corrections were applied to the TSV here on 29 Oct (see the solution log). He also validated the same
table on d'Ennery's glossed letter of 16 Nov 1770 (C8 A 69 f. 354): 0.924 characters and 0.823 words, against 200
shuffled keys at most 0.322 and 0.210. Note: `research/dudout_2026-10-29/martinique1765-note.txt`. Credited `dudout`,
role "key corrected". The ANOM images were used for study only and are not copied here.

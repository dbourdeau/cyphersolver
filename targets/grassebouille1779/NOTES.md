# Grasse and Bouillé 1779: an enciphered war plan for the defence of the French West Indies

Status: read (Brice Dudout, 28 Oct 2026; running text, 778 of 794 words read in their sense, 757 certain, 9 probable, 12 restored, 16 unresolved; Daniel Bourdeau's 95% rule; the four pages of enciphered tables not read).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Not in the catalogue. Write-up prepared for https://bdudout.github.io/europe-chiffree/en/documents.html#grasse-bouille-1779 (publication pending).

## Document

Archives nationales d'outre-mer, COL C8 A 76 fol. 196, images FRANOM23_C8A_076_0309-0317 (IREL record https://recherche-anom.culture.gouv.fr/ark:/61561/zn401ysttruo; images not included, no reuse licence found). Martinique, 4 August 1779, duplicate. The inventory calls it "Autre chiffre préparé par MM. de Bouillé et de Grasse"; it is in fact a memorandum entirely in cipher, with the enciphered title "Projets remis par M. le comte de Grasse et M. le marquis de Bouillé sur les moyens les plus sûrs de protéger les colonies françoises de l'Amérique et d'attaquer celles des Anglois", signed in autograph "Le comte de Grasse" (image 0313). Images 0314-0317 are enciphered tables (the returns announced in the text), not read here. No gloss and no contemporary decipherment.

## Cipher and key

Bouillé's numerical code ("chiffre du 25 avril 1778", about 850 elements, homophones, nulls 163, 586, 257), the same as in targets/bouille1778 (PR #171). Key K6 of that folder (490 values from glossed letters of 1779-1780) was extended by aligning three contemporary cipher/plain pairs from ANOM C8 A 79-81: the return of stores of 1 Oct 1780 (fols. 3/5), the garrison return of 4 Apr 1782 (fols. 212-213) and letter no. 624 of 4 Mar 1782 (fols. 55-56). New values were taken only where both neighbouring groups aligned with cost <= 1. Result K7, 509 values, frozen (SHA-256 23248c6cd6a5fc3661ba8821546158736ee94396a6b971cc6c21f455398699aa). `key.tsv` is K8 = K7 + the held-out pair, added after validation.

## Validation

Protocol written before any computation; held-out pair fixed in advance: Bouillé's "Mémoire sur la campagne prochaine" (Martinique, 14 Sept 1781, C8 A 80 fols. 113-115), whose cipher original was transcribed and frozen before the contemporary "Déchiffrement" was opened. 485 groups; frozen K7 gives 0.825 of words and 0.889 of characters against the Déchiffrement (passages left in clear in the original removed from both sides); 200 permuted control keys (seed 20261028) reach at most 0.149 and 0.089. Criterion fixed in advance (characters >= 0.85, words >= 0.75, above the controls): passed.

## Reading

First published decipherment, to our knowledge. Daniel Bourdeau's rule (95% of words read in their sense): 794 words, 757 certain (95.3%), 9 probable {x} (1.1%), 12 restored by sense [x] (1.5%), 16 unresolved ‹…› (2.0%, counted one word per number) -> 98.0% read in their sense.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- Content. A month after the capture of Grenada, Grasse and Bouillé propose a small mobile squadron (8 ships of the line, 4 frigates, 2 corvettes, 3 storeships, 2,500-2,600 men, artillery, six months' provisions) to leave France by the end of October, based at Martinique: it would guard the Windward Islands in the winter season and strike the British elsewhere (Leeward Islands, New England, Florida with St Augustine and Pensacola, the Newfoundland banks and fishery), serving the Spanish ally; Bouillé to command on land, Grasse at sea.
- Probable words {x}, with justification (the key gives a near form, the sense requires the word): {opérer} (234, learned on "l'opi·nion", gives "opi·é·rer"); {donc}; {octobre} ("oc·m·bre"); {composition} ("co·m·ser·si·tion"); {contre} (396 = "contraire"); {avantageux} ("retard·a·ge·u·x"); {profitant} (762 "xtant", learned on "hôpi·taux tant"); {connoissance} ("con·267·is·sa·n·ce"; 267 is elsewhere "la Martinique"); {garantir} ("donn·ran·ti·r").
- Words restored [x], with justification: [po]uvant (336, "ne ‹336›u·vant être toutes défendues"); [détail]lés (574, "des états ‹574›·lés"); [Flo]ride (168, next to Saint-Augustin and Pensacola); [ban]c de Terre-Neuve (76); [abon]dance (324, "une ‹324›·da·n·ce inattendue"); [mouvemens] twice (534: "des forces et des ‹534› de l'ennemi", "les ‹534› inattendus"); [im]proviste (667); su[b]sister (481); [prochain]e (603, "la nouvelle de la ‹603›·e arrivée"); Bouil[l]é (785); [armes] (word left out by the encipherer: "rendre à nos l'éclat qu'elles ont perdu").
- Unresolved: 445, 209 ("que les forces soient ‹445›es de ‹209› à pouvoir…"), 401 ("faire partir d'‹401›"), 246.806 and 540.276 ("les ‹…› ‹…›es"), 501, 258 ("si les ‹501› sont ‹258›ables"), 51 ("plus ‹51›es à remuer"), 176 ("un ‹176› dans l'exécution"), 102.449.162 ("dès qu'elle aura …"), 375 ("par ses ‹375›s dans les îles angloises"), 363 ("nos ‹363›es").
- Prior work: IREL gives no summary; no decipherment on the images or neighbouring pieces; nothing in this repository; web search negative (28 Oct 2026). A plain copy might survive among Bouillé's papers or in Marine B4 (Archives nationales); not checked.

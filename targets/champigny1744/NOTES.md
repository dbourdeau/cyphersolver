# Champigny 1744: cipher copy of Commodore Knowles's neutrality notice to the inhabitants of Dominica (ANOM C8 A 56 fols. 57-57v)

Status: read (Brice Dudout, 28 Oct 2026; 154 of 155 words read in their sense, 142 certain, 7 probable, 5 restored, 1 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 28 Oct 2026. Write-up (to be published when the account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#champigny-1744
Not in the catalogue; found through the ANOM inventory (IREL), which says of C8 A 56 fol. 54 "une partie de cette lettre n'a pas été décryptée".

## Document

Archives nationales d’outre-mer (Aix-en-Provence), COL C8 A 56 fols. 57–57v, enclosure of the letter fols. 54–56v; images FRANOM23_C8A_056_0103–0104 (IREL). Inventory: “Arrival of the English admiral Knowles at Dominica […] (in cipher, part of this letter has not been decrypted)”.
17 August 1744 (letter, duplicate); Knowles’s notice dates from July–August 1744. Fort-Royal, Martinique → Versailles (colonial office).
Sender: Jacques-Charles Bochart de Champigny, governor general of the Windward Islands (“Pour copie Champigny”). Recipient: Jean-Frédéric Phélypeaux, comte de Maurepas, secretary of state for the Navy.
Record: https://recherche-anom.culture.gouv.fr/ark:/61561/zn401utsvwe. Images not included (IREL, no reuse licence).

Summer 1744, the start of the Anglo-French war in the West Indies. Commodore Charles Knowles anchors at Dominica, then a “neutral” island, and circulates a notice: protection for inhabitants who stay neutral, four louis d’or for every deserter returned, treatment as enemies for anyone hiding his sailors. Champigny, governor general of the Windward Islands, sends a cipher copy to the minister with his letter of 17 August 1744. The letter was deciphered between the lines in Versailles; the enclosed copy never was (“part of this letter has not been decrypted”).

## System and key

Navy code for the Windward Islands (1740s): a numerical nomenclator of about 500 values (1–500), two-part (non-alphabetical), with syllables, letters and some words (205 Dominique, 474 Royal, 3 trois); several numbers for common syllables; numbers in clear underlined. Distinct from the 1761 code (Daniel Bourdeau, mercier1761), the d’Ennery form of 1765 and the Guiana code of 1744–1762.

`key.tsv` (K5) was built only from the contemporary interlinear glosses of six letters of Champigny of 1744
(C8 A 56 fols. 40, 44, 54-56v, 59, 63, 67; about 4,900 groups aligned automatically to the glosses), with four written
decisions on ambiguous groups (393 = i, 296 = ro, 465 = qu, 300 = fa), and frozen (SHA-256 db2f99ee1d2f3259...) before
the validation letter was opened. Comparison with other keys: key1761 (mercier1761) 0 agreements on 69 common groups;
key1765_ennery 1 on 256; Guiana code 1744-1762 (orvilliers1759/dudout) 0 on 150: a different code.

## Validation

Held-out glossed letter never seen before the freeze: C8 A 56 fol. 79 (17 Nov 1744), 566 groups, 263 gloss words.
Strict normalised measure fixed in advance (global letter-by-letter alignment of the decoded string to the gloss; a word
counts only if all its letters match and nothing is inserted inside it): characters 0.894, words 0.814. 200 control keys
(values shuffled between groups): at most 0.578 and 0.122. Criterion: >= 0.85 and >= 0.75 and above every control: met.
Three earlier validations with poorer keys (K1-K3, other held-out letters) had stayed below it (0.76-0.81 / 0.65-0.74).

## Reading

First published decipherment, to our knowledge. 381 cipher groups, 155 words. Published under Daniel Bourdeau’s rule: 95% of the words read in their sense. Here: 154 of 155 words read in their sense (99.4%): 142 certain (91.6%), 7 probable {x} (4.5%), 5 restored from the sense [x] (3.2%), 1 unresolved ‹…› (0.6%). Each probable or restored word is justified in the notes.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- Context. Champigny’s glossed letter (fols. 54–56v) tells of Knowles’s arrival at the Grande Anse of Dominica with the Superbe (60 guns), two 50-gun ships and frigates, of his sailors deserting to Martinique, and of a feared attack on St Lucia; it announces “a copy of a writing which Mr Knowles circulated in Dominica to offer the inhabitants of that island a neutrality, which they did not accept”. That is our piece.
- Restored from the sense [x] (5). (1) [Knowles]: 381 251 326 110 217 301 = M. ‹251›-no-u-le-s; elsewhere Knowles is 381 25 326 110 217 (25 = K); 251 is probably a malformed 25. (2) [Majesté]: number 222, absent from all glossed letters; “Sa … Britannique” leaves only this word. (3) [arriver]: 13 55 335 300 130 = a-r-ri-fa-r; 300 (fa) for 303 (ve), a slip between neighbouring numbers. (4) [absolument]: 470 (not in the glosses) + so-lu-ment. (5) [d’eux]: 336 306 428 = ce-eu-x; “il demande absolument ce eux la restitution” is ungrammatical, hence d’eux.
- Probable {x} (7). {Britannique}: 391 i t an ni que, 391 standing for -mbr- in “nombre” (280 391): br- probable. {habitans}: 253 = habita (1744 gloss), followed by 436 (ga) instead of 435 (an), a slip between neighbours. {empêcher} ×2: em-pe-296-e-r, 296 = ro in the glosses (35 of 35); the sense requires empêcher. {armés}: 254 (ar, “armements”) + 180, seen once. {traités}: 204 = tr(aités) in a glossed letter of September 1744. {demande}: de-m-433-de; 433 has only one doubtful alignment in the glosses; “comme il demande” echoes “il demande” above.
- Unresolved. “s’ils ‹320›issent comme il demande”: agissent (act) or obéissent (obey); 320 occurs in none of the seven glossed letters examined.
- Identifications and sources. Sender: Jacques-Charles Bochart, marquis de Champigny, governor general of the Windward Islands 1728–1748 (M. Vergé-Franceschi, Les Officiers généraux de la Marine royale 1715–1774, 1990, p. 2097 ff.; Wikipédia, “Jacques-Charles Bochart de Champigny”). Recipient: Jean-Frédéric Phélypeaux, comte de Maurepas, secretary of state for the Navy 1723–1749 (É. Taillemite, Dictionnaire des marins français, 2002, p. 362; J.-P. Zanco, Dictionnaire des ministres de la Marine, 2011). Knowles: Charles Knowles (1704–1777), second in command on the Jamaica station under Chaloner Ogle 1743–1745, active at Antigua, commodore’s broad pennant in the Superb (Naval Chronicle 1, 1799, pp. 100–112; Dictionary of National Biography 31, 1892, pp. 292–294); his presence at Dominica in August 1744 with the Superbe is attested by Champigny’s glossed letter itself (fol. 54).
- Prior work. The ANOM inventory notes the undecrypted part; Daniel Bourdeau’s repository (28 October 2026) holds neither this piece nor this code; no edition known.

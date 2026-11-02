# D'Orvilliers to the Navy minister, Cayenne, 10 June 1761 (ANOM C14 25 fol. 36): read (Brice Dudout, 28 Oct 2026)

Status: read (Brice Dudout, 28 Oct 2026; about 247 of 250 words read in their sense, 2 groups open).

Write-up: https://bdudout.github.io/europe-chiffree/en/documents.html#cayenne-1761

## Access

Brice Dudout opened the C14 24 and C14 25 volumes in an ordinary browser on IREL (recherche-anom.culture.gouv.fr, after the
automatic Anubis page) and saved the views: the C14 volumes are online at volume level (`.../images/MINISTERES/SEM/C14/C14_025/FRANOM34_C14_025_NNN.jpg`),
even though the item notices carry no digital object. No image is included here (no reuse licence).

## The code

A numerical Navy nomenclator of about 500 numbers for letters, syllables and words (215 de, 307 nous, 136 la, 112 garnison,
91 troupes, 355 pour, 375 sans), with homophones (458 and 290 = t; 185 and 170 = d) and words left in clear. It is the same from
1757 to 1762, and it is not the Windward Islands code of mercier1761 (key1761.tsv / key1765_ennery.tsv do not fit: 136 = la,
311 = est here). The Martinique letters of 1744 use another table (C8 A 56 f. 13: "nous avons reçu la" = 165 304 386 491 215 301 302 456 229).

## Key and check held out

Method (protocol written before computing, cryptanalysis/c04/PROTOCOL.md): (1) full transcription of the glossed letters of 1759 (C14 24 fols. 25–29, 32v–33: about 2,500 numbers with their contemporary interlinear decipherment); (2) number ↔ plain alignment by maximum likelihood (EM, respecting word boundaries), key K1 frozen (SHA-256 fca8fcce…) before any validation; (3) validation on a glossed letter held out, d’Orvilliers 10 June 1761, fols. 39–40 (618 numbers, 314 words): 0.955 of the letters recovered (controls with permuted values, 200 draws: p99 = 0.405) and 0.638 of the words exactly (p99 = 0.103) — the code is the same from 1759 to 1761; (4) key K2 retrained on all glossed letters, then K3 = K2 + six values corrected from the context of the target letters, frozen (SHA-256 6469d776…); (5) reading of the letter of 10 June 1761. Files in our research folder.

## Reading

First published decipherment, to our knowledge. 489 cipher numbers, about 250 words. Published under Daniel Bourdeau’s rule: 95% of the words read in their sense. Here: ≈ 247 of 250 words read in their sense (≈ 99%), of which ≈ 236 certain (≈ 94%); 10 words restored from the sense [x] (numbers used only once), 1 probable, 3 unresolved (‹150›, ‹351›, ‹347›).

- The Des Essarts plan. The joint letter of the same day (C14 25 fol. 171, glossed at the time) sets out “M. Desessars’s plan”: to write to his correspondent so as to be understood without risking the secret, and to bring clothing, provisions and even munitions to Cayenne by a foreign route. A year later (20 August 1762, fol. 65) d’Orvilliers reports a purchase of piastres in Holland “through the widow Hamilton of Rotterdam, for Des Essarts”: the channel announced here did work. Surinam, the neighbouring Dutch colony, served as the declared destination of neutral ships supplying Cayenne.
- Restored words. Ten numbers occur only once in the letter and in our training letters; their value follows from the sense and the shape of the sentence: 34 [preuve] and 269 [zèle] (“une … du … de M. Desessars”), 353 [particulier] (against “en commun”; this is the governor’s private “1st” letter), 492 [prompt] (“un … secours”), 192 [dernière] (“dans la … misère”), 95 [Surinam] (twice: “ils enverront à …”, “sucreries de …”), 247 [projet] (twice: “les effets propres au …”, “accomplir ce …”), 493 [moindre] (“le défaut du … sol”). In “{pro}pres”, number 485 is not attested elsewhere with this value.
- The three unresolved numbers. ‹150› (“feront passer par les ‹150›x”: a plural in -x, perhaps “vaisseaux”); ‹351› (“cet ‹351› est dangereux”: “accident”, “état”?); ‹347› (“si je dois être ‹347›”: the first digit is overwritten; “tranquille” or “content” fit the sense).
- Values corrected from context (key K3, see method): 297 = i (“possib·i·lité”), 296 = al (“roy·al”, as in “al·lumée” and “mort·al·ités” in other letters of 1760), 360 = ta (“re·ta·rdement”), 164 = éb (“éb·oulement”), 239 = cl (“obsta·cl·e”), 163 = telle. Two encipherer slips: 290 (t) for u in “par une muraille”.
- Prior work. The office note at the top reads “le triplicata déchiffré”; that decipherment is not filed with the letter, and the ANOM entry says “entirely in cipher and not translated”. Daniel Bourdeau’s repository (folder orvilliers1759) noted on 28 October 2026 that the images were not accessible; no published reading found.

## Two more letters: 27 Sep 1760 (fols. 11-12v) and 20 Dec 1760 (fols. 14-17)

Two more letters of d’Orvilliers, with “passages chiffrés non traduits” (ANOM entries), read with the same key: 27 September 1760 (707 numbers, ≈ 330 words: ≈ 99% of words read in their sense, ≈ 95% certain; 10 isolated numbers restored from the sense, 1 unresolved) and 20 December 1760 (≈ 1,000 numbers, ≈ 520 words: ≈ 98% read in their sense, ≈ 95% certain; 12 restored, 9 words unresolved). Both copies were “handed to M. Accaron” (31 January and 10 March 1761) with no decipherment filed.

- 27 September 1760: restored words. [satisfa]its (number 33), [homme]s (443, also on 20 December: “the number of men we lose”), [l’]état (305), [vaisseau]x [neutre]s ne peuvent s’en [charge]r (308, 416 — 416 recurs on 20 December: “aux bâtiments [neutre]s” —, 340), [bon]nes (324, also “la place est en bon état” on 20 December), [hors] de service (346), [ju]ger (146); {guê}tres (405, “va-gues” elsewhere) and {malades} are probable; 21 = hu (“hu·midité”, as “hu·it” in 1759). Unresolved: ‹32›li état (“meilleur”?). Two encipherer slips: “tout ouvrage de te faute” and “fin·ai·re” for “faire”.
- 20 December 1760: restored and unresolved words. Restored: prodi[gi]euses (497), à tel [poi]nt (132), le [vrai] est (173), a [toujours] manqué (240), [homme]s (443), [fond]s (141), en [état] de défense (30), [bon]s (129, “redoubts and entrenchments are good”), [neutre]s (416), rétri[bu]tion (101). Unresolved: d‹222› and ‹56›vits (“the only relief we had … from some cartel ships …”), ‹56› borné, “l’état des ‹·te·s›, celuy de la ‹411›e”, “d‹193›une [bon]ne te‹…›”, “la plus grande ‹422›” (favour, protection?) and the “parlementaires ‹161›”.
- Context. On 27 September 1760 d’Orvilliers puts into cipher what the ordonnateur Le Moyne told him about the finances (the troops are paid “sou by sou”) and the destitution of the garrison; on 20 December he answers point by point the ministerial dispatch of 6 June 1760: cassava as the only food for three months, 114 men short, “ideas neither feed nor clothe the troops”, a place that is not “in good condition” whatever the minister was told, and a refusal to say more about the terrain lest an intercepted letter “reveal too much about the country”.

Key correction after validation. K1 alone was validated, frozen, on a held-out letter. The reading key K3 = K2 (same method, retrained on all glossed letters including the validation letter) + 9 values corrected from the context of the target letters, after validation: 297 i, 296 al, 360 ta, 164 éb, 8 z, 495 ga, 95 Surinam, 163 telle, 239 cl (evidence in K3_corrections.tsv). Why 0.638 of words but 0.955 of letters? The letter measure counts the letters of the mechanical decryption found, in order, in the contemporary gloss; the word measure requires a gloss word (3 letters or more) to be found whole, letter for letter, in the same place. A single wrong number (often a number used once and absent from training, a spelling variant in the gloss, or a misassigned homophone) loses the whole word; long words made of 3 to 6 numbers are the most exposed. The word measure is therefore a lower bound; it is still six times the controls.

Files: `transcription_1760-*.txt`, `reading_1760-*.md`. In C14 24 (1757-1759) every cipher passage we saw is glossed or a duplicate of a glossed copy.

Files: `transcription.txt`, `decryption.txt`, `key.tsv`, `reading.md`.

## Update (C06): 1746 letter, key K4, 347 = tranquille

An older letter, of [June] 1746 (C14 19 fols. 15v–16, “passage chiffré non traduit”, addressed to “Your Greatness”, Maurepas): the same code is already in use. ≈ 150 numbers, ≈ 105 words: ≈ 99% read in their sense, ≈ 93% certain; 6 restored, 1 probable, 1 unresolved (the ship’s name, read letter by letter but uncertain).

- 1746: restorations. [votre] lettre (89), [malheur]eusement (173), nous [fe]rions (158), le [vaisseau] (308: the same value as “les [vaisseau]x [neutre]s” in 1760) du [Roy] (1; 468 = roy elsewhere), une très [forte] recrue (156; the glossed letter of 18 February 1746 writes “nous envoyer une forte recrue”, with “forte” in clear); Zeylema{k}er (406 = k probable). The ship’s name reads f·ro·ni·ca·le, its division uncertain. M. de l’Isle Adam is named in clear. The glossed letter of 18 February 1746 (C14 19 fol. 18, images 021–022) was transcribed and added to the key (K4), which was revalidated on a second glossed letter held out (14 January 1758, C14 24 fols. 23–24, 252 numbers, 107 words): 0.970 of letters (controls p99 0.423), 0.626 of words (p99 0.103).

- 10 June 1761: 347 is now read "tranquille" ("Jugez, Monseigneur, si je dois être tranquille"), the same formula glossed in the letter of 18 February 1746; open groups there are now 150 and 351.

Files: `transcription_1746.txt`, `reading_1746.md`, `key_K4.tsv` (sha256 66d001de5f710c67e12fc01fc9e2eee1f6f48b9cce514e9c6cc2233a790e02f9; frozen before the second held-out check).

# RESULTS.md  Simon Renard to Charles V, Paris 12 July 1549: the Vienna original

HHStA Wien, StAbt Frankreich, Diplomatische Korrespondenz 17, Konv. Juli 1549, fol. 13-14. Working scan supplied by HHStA to Malcolm McBratney, GZ 2026-0.947.186 (not to be committed or published). Worked 16 Nov 2026 (Brisbane).
First reading of this dispatch: **Ivan Sourvillo** (Cyphersolver renard1549, catalogue 1560), from the Spanish copy at Modena. This file tests his reading against the French original; it does not replace it.
No person has checked the Vienna transcriptions (French or cipher): they were made by AI models (Claude) from the archive's working scan.

Outcome method (Lasry categories): **key recovered from adjacent plaintext**. The cipher looks like Pich-Ponce's PP1 on structure (section 6); if so, a published key also exists. Not compared sign by sign.

## Bottom line

- The French in the margin IS a contemporary decipherment of the cipher. [derived: the cipher decodes to the same French, line after line]
- Key rebuilt: 127 distinct signs over 1,513 sign tokens; 1,201 of 1,513 tokens (79.4%) sit on their sign's majority value. [measured: sum of n_value / sum of n_total in key_renard1549_vienna.tsv]
- Hold-out, first pass (figure of record): **73.8%** letters, 5,000-shuffle controls max 27.9% and 27.0%. Caveat: its seed was written with the whole letter in view. Two leak-free reruns gave **56.7%** and **64.8%**, both under our 65% line. [measured] So the line is met only by the first pass. Reported as is.
- Sourvillo's reading holds on the plot, the people and the numbers, with four differences (the soldier count, the prior, the second plotter's name and office, the courier's day) and one addition (Figueroa) (section 5).

## 1. Layout [measured from the scan unless tagged]

| Page | Content |
|---|---|
| fol. 13r | Later note "12 Juillet 1549" top left. Cipher block, 30 lines, brown ink, right two thirds of the page. Decipherment in black ink: 2 full-width lines above the cipher, 35 short lines down the left margin, 1 full-width line below. Archive stamp, pencil "13". |
| fol. 13v | Cipher block, 28 lines. Decipherment: 2 lines above, 34 margin lines, 1 line below. |
| fol. 14r | Cipher, 9 lines (last line 4 signs and an end flourish). Decipherment: 10 margin lines. Then the sender's clear close in brown ink ("Sire Je supplie le Createur ... De Paris ce douzie[sme] de Juillet 1549"), "De v[ost]re Majeste", and "Tres humble et tres obeissant subiect et serviteur Simon Renard." Pencil "14". |
| fol. 14v | Address "A Lempereur.", seal, fold marks. |

- Hands: S = the sender's secretary, brown ink, writes the cipher and the clear close; the subscription and signature look autograph [unverified]. D = the decipherer at the receiving end, black ink, fast chancery cursive, fitted around the cipher block (above, margin, below). A third, later hand wrote the date note.
- The whole body of the report is in cipher. The only clear text by the sender is the closing prayer, date and signature. There are no clear passages inside the body.

## 2. and 3. Transcriptions (frozen before alignment)

- `FR_CLEAR.txt`: 93 lines = 85 of hand D (4 above the cipher + 79 margin + 2 below) + 7 of the sender (6 on fol. 14r, the address on 14v) + 1 later note. 2,174 letters in the decipherer's zones after expanding abbreviations. [measured]
- `CIPHER.tsv`: 67 lines, 1,513 signs, 69 base shapes with five mark positions, neutral labels S01 to S69; shapes in `SIGNS.tsv`. [measured]
- `FREEZE.txt`: sha256 of all three, 16 Nov 2026 08:44:54Z.
- Doubtful margin readings were flagged [?] at freeze and left untouched. The cipher later settled several: "prevost[?]" is **secretaire** (13r.M07, 13v.T2); "chaulux" is **Chauvey**; "pour[?] cest[?] effect" is "en cest effect"; "porteur[?]" is "pourteur".

## 4. Key and tests

`key_renard1549_vienna.tsv` (per-sign value, n_value, n_total, other aligned values), `ALIGNMENT.tsv`, `DECODE_fullkey.txt`, `pipeline.py`, `HOLDOUT*.txt`.

System [derived from the alignment]:
- Single-letter signs, with homophones for vowels.
- Syllable signs: one base shape per consonant; the mark gives the vowel. No mark = e, dot below = a, dot above = i, underline = o, dot at left = u. Two-letter key values that fit this rule: a 11 of 12, i 8 of 10, o 12 of 13, u 7 of 7. [measured]
- Numerals for doubled letters: 3 cc, 4 dd, 10 ll, 12 mm, 13 nn, 14 pp, 15 rr, 16 ss, 17 tt/ct, 18 uv. [measured, small counts: see key]
- Nulls: 20, 23, 63, 86 align to nothing. [measured] The "63" on fol. 13v is a null, not a number of soldiers.
- Word signs: a three-ring sign for "et"; one sign each for "que" and "qui"; the "Majeste" group after "vostre dicte" is not resolved sign by sign.

Hold-out (last 13 of 67 lines = 19.4%: 13v.25 to 14r.09; 263 signs, 371 letters; key rebuilt from the first 54 lines; one decode; score = 1 - edit distance / longer length; no emendation):

| Run | Seed for the aligner | Letter accuracy | Control max, seed 20261112 | Control max, seed 7 | Shuffles reaching real |
|---|---|---|---|---|---|
| H1 first pass (figure of record) | 71 values, written after seeing the whole-letter alignment (leak) | 0.7377 (1 - 101/385) | 0.2791 | 0.2700 | 0 of 10,000 |
| H2 leak-free | 11 values from fol. 13r repeats (4 wrong) | 0.5666 (1 - 166/383) | 0.2773 | 0.2797 | 0 of 10,000 |
| H3 leak-free, post-hoc bootstrap | H2 seed, then training-only re-seeding | 0.6481 (1 - 133/378) | 0.2897 | 0.2863 | 0 of 10,000 |

Reading of the table: the key is real (every run is far above every shuffle). The score is held down by two things that are not emended: the decipherer shortened and reworded (the cipher says "et qu'il pleut a vostre dicte Majeste luy escripre", "oultre ce ledict navarrois", "soubdainnement le present pourteur", where the margin has other words), and the aligner is a simple one. H1 decode of the held-out lines, verbatim, is in `HOLDOUT.txt`.

## 5. Content against Sourvillo's reading of the Modena copy

Vienna wording below is the cipher decoded with the key, checked against hand D. [derived]

| Point | Sourvillo (Modena, Spanish) | Vienna original (French) | Verdict |
|---|---|---|---|
| Time | about eight in the evening | "environ les huit heures du soir" | agree |
| Informant | says he is from Navarre, of the following of the lord of Tende, governor of Provence; later "este navarro" | "ung qui se dit estre de Navarre de la bande du sieur de Tendes gouverneur de Provence"; later "ledict navarrois" | agree |
| Target | castle of Nice, resolved by the [?King] and [?Council] | "conclute par le Roy et son conseil sur le chasteau de Nice" | agree; his two context guesses confirmed |
| Plotter 1 | Care, "contrareleur" of the Duke | "ung nomme Cara contreroleur du duc de Savoye"; later "Cari" | agree. Spelling supports his Carra identification |
| Plotter 2 | Chaulve[?x], [amo = an office] of the Duke, once in the service of the Marquis del Vasto | "ung nomme Chauvey secretaire dudit duc qui souloit servir le feu marquis del Gasto" | name is **Chauvey**; "amo" = **secretary**. His second-pass identification with Antonio de l'Eschaulx, former bailli, is not supported by the spelling or the office [derived]; who Chauvey was is [unverified] |
| Soldiers won over | sixty-three [?Savoy]ard soldiers | "soixante deux ou trois souldartz savoyens" | **differs**: 62 or 63. Savoyard confirmed |
| Their commander | "prior de [?Saboya]" | "prieur de Lombardie" | **differs**: Lombardy. Matches his own note on the Grand Prior of Lombardy |
| Reward | a sum of [?crowns], four pays for life | "certaine somme de deniers ... quatre payes a son service" | agree in substance |
| Force | Tende with twelve galleys and 300 soldiers | "douze galleres et trois cens souldartz" | agree |
| Cover | the fort the King builds at Antibes, near Nice | "soubz umbre du fort que ledit sieur Roy fait faire a Antiboul qu'est pres dudit Nice" | agree |
| In whose name | Tende's, on a claim to villages in the valley of [?Augusta] | "certains villaiges qui sont en la val d'Oste" | agree: Aosta confirmed |
| Bastard line | Tende descends from a bastard of [?Savoy] | "party d'ung bastard de Savoye" | agree |
| Money courier | the [amo] of the Count of Tende, with whom [...], to leave "next Wednesday" | "le secretaire du conte de Tendes avec lequel il est loge debvoit partir mardi ou mercredi prochain et pourter les deniers" | **differs**: Tuesday or Wednesday. Fills his gap: "with whom he lodges" |
| Constable | gave the galleys to another, put him off with words | "le connestable avoit donne la charge desdites galleres a ung aultre et l'avoit abuse de parolles" | agree |
| Letters | will show letters of Car and Chaulve to the King and Tende | "lettres que lesdits Cara et Chauvey ont escript au Roy et audit conte de Tendes" | agree |
| Genoa | will go to the ambassador in Genoa | "a Gennes devers l'ambassadeur Figueroa" | agree; Vienna names **Figueroa** |
| Close | asks how to deal with him; Paris 12 July 1549 | "me fere escripre come je me debvray conduire devers luy et le contenter"; "De Paris ce douzie[sme] de Juillet 1549" | agree |
| Number 63 | read as the soldier count | on fol. 13v a sign "63" is a null | no conflict in Vienna; relevance to Modena [unverified] |

The Modena images were not seen here, so whether the four differences are the translator's or the reader's is [unverified].

## 6. Which key is it, and what could it open

- **It looks like PP1** (the Saint-Mauris / Granvelle cipher, 1544-1554) on structure: same five vowel-mark rules, same numerals for doubled letters (LL 10, MM 12, NN 13, PP 14, RR 15, SS 16, TT 17, UV 18, CC 3), nulls from 20 up. [derived from Pich-Ponce 2023b as summarised; her sign images were not compared shape by shape: unverified at sign level]
- Renard took over the Paris embassy from Saint-Mauris in 1549, so he inherited the cipher [unverified as a statement of fact; consistent with Tomokiyo's user list].
- renard1554 (AGS E 808 f. 184): Tomokiyo calls it PP1, so the same key; the repo holds no key or transcription to compare sign by sign. [sourced]
- renard1556 (BnF fr. 20991, Lasry): a later letter-and-syllable system written in Latin letters ("que, fo, ma, ta"); **not** this key. [sourced]
- Sourvillo's Modena key (1548 numeric syllabary): a different cipher, as he said. [sourced]

Candidates this key could open (no Renard letter of 1549-1551 is in catalogue.json, leads.json or DECODE [measured by search, 16 Nov 2026]):

| Item | State | Images |
|---|---|---|
| DECODE 9959, Renard to Prince Philip, London 19 Feb 1554, AGS E 808 f. 184 | "Non-decrypted" on DECODE; printed in English in CSP Spain XII | 6 pages on DECODE |
| HHStA Frankreich Dipl. Korr. 17, Renard to the Emperor 14, 18, 28 July 1549 (CSP IX: "in cipher", extracts only, "Vienna, Imp. Arch. F. 28") | full French text unprinted; likely carry marginal decipherments like this one [unverified] | not online; HHStA working scan on request |
| Catalogue 507, HHStA Frankreich Varia 3-99, 3-125: Abbot of Luxeuil to Charles V 1546, French correspondence 1547 | AIS gives no decipherment; Luxeuil is a named PP1 user | not checked |
| Besancon Ms Granvelle 71 fol. 41-48, Charles V to Renard 12 and 15 July 1549 | "chiffree, avec le dechiffrement en regard" | not checked |
| Catalogue 1129 and 1130, Ruy Gomez to Renard, 24 Jun and 17 Sep 1556, Besancon, "non traduit" | after PP1's last known use (May 1554): untested | not checked |
| Lead 1604 / DECODE 1185, Saint-Mauris to Granvelle, Dijon 5 Jul 1548, BNE MSS/7913/127 | already "Decrypted" on DECODE | 1 page |

## Remaining gaps

- 29 signs occur once; their values rest on one alignment each. Blocker: too short.
- The "Majeste" group and three words (13v.11 "obligeroit / oblieroit", 13v.13 "enfon..", 14r.04-05 "me m..e a ge") are not settled. Blocker: needs a second look at the scan with Pich-Ponce's sign table.
- Weiss III and Turba not opened. Blocker: full text not searchable from here.
- Sign-level comparison with Pich-Ponce's PP1 table. Blocker: images in the PDF not read.

## Not done

Nothing committed, pushed, filed, sent or changed on DECODE. No profile.json, no site page: that is the Cyphersolver write-up step and needs Malcolm's go-ahead and Sourvillo's credit on every surface.

# conde1651 — Condé to Armand du Lau du Chambon, Aug–Sep 1651 (AD Dordogne 2 E 1841/18; catalogue 1213)

Source: Archives départementales de la Dordogne, 2 E 1841/18 (du Lau du Chambon papers). Photographs taken in Nov 2026 for the project by the Société historique et archéologique du Périgord (Catherine Schunck, SHAP). Images are not distributed and no crop is included; cite « AD Dordogne, 2 E 1841/18 ». Frame numbers (P1370NNN) are the photographer's.

## Prior art (EXISTING)
- Gen. Arnaud de Brianson, « Sur cinq lettres chiffrées du prince de Condé (1651) », *Bull. Soc. hist. et archéol. du Périgord* CX (1983), 4ᵉ livraison: letter-by-letter summary and description of the system (issue #478).
- The dossier itself also holds Brianson's **complete typescript decipherment** of the five letters (CAPITALS = deciphered, ?/n = unresolved codes; a later all-lower-case version with codes pencilled in), and **his key**: a handwritten syllable grid (tilde / acute / diaeresis series) and a key sheet « Chiffre de Louis II de Bourbon, prince de Condé (août et septembre 1651) » (alphabet with homophones and symbols, caron words, macron names). Unpublished; not reproduced here.
- The letter of 25–27 Aug (18-11) carries brown-ink interlinear glosses of a few phrases (period or early; e.g. « n'y avoir aucun esgard », « mr le presydent dafis », « du retour des deputés »): a partial old decipherment.
- So 1213 is **already solved**. What this target adds: an independent check of Brianson's key on a held-out page, a sign-level transcription, a re-reading with the frozen key, and the list of places where the cipher reads differently from his typescript.

## Bundle (46 photos)
Folder cover; the five cipher letters (P1370687–688, 700–703, 705–706, 710–711; address panels 694, 704, 707, 709, 712; P1370689, presumably p. 4 of the 17 Aug letter, is an unusable grey frame); clear letters of 1651–1652 (incl. the Barbezieux agreement with du Dognon, Sept 1651, and Brouage, 2 June 1652); a **blank period nomenclator** (P1370715–717: « Noms propres de personnes, villes, bourgs et rivières », Roman-numeral codes in A–V order, Saintonge/Aunis names, a « Nombre » list and an A–Z alphabet with no values) — a different system, probably for 1652, used by none of these letters; Brianson's key sheets (718–719) and typescripts (720–727).

## The cipher
Two-digit numbers (some one-digit) with a superscript mark, plus about 20 symbols. Unmarked numbers 15–40 and the symbols: homophonic alphabet. Tilde, acute and diaeresis: syllables in consonant series (ga…gu, ca…cu, da…du, fa…fu, ha…hu; la…lu, ma…mu, na…nu, pa…pu, ba…bu; qua/que/qui, ra…ru, sa…su, ta…tu, va…vu) and short words. Caron: words (affaire, armes, ennemi, ami, avant, afin, aboutissement…). Macron: proper names (16 Paris, 18 Bordeaux, 65 Guyenne, 74 le Président, 81 le chevalier, 82 Monsieur…). Same graphic family as the Condé–Barrière key of 1655, different table.

## Protocol and measure (prereg/)
- K2 = Brianson's key as left in the dossier, transcribed by us without seeing the ciphertext transcription; frozen with SHA-256 together with the protocol, the scorer and the reference (prereg/PREREG.sha256).
- Held-out: all cipher of P1370688 (17 Aug letter, pp. 2–3) between its first clear passage and its last cipher run; 410 signs measured. Reference: Brianson's capitals for the same passages, ?/n removed.
- Transcription: two blind passes + blind arbiter (blind/P688_*).
- Result (validation.json): **K2 0.869 vs best of 200 permuted-key controls 0.293 → pass.** Our 1655 Condé–Barrière key on the same portion: 0.205 (below its controls) → fail. Deviation declared: both keys scored in the same single run; '?' flags stripped mechanically before scoring (hashed). P1370688 is burnt.

## Reading
All five letters transcribed (two blind passes + blind arbiter per group, blind/P1–P3_*), decoded with the frozen K2 (decryption.txt) and read by rule of #728 (reading_*.md, notes in French). Sure words = every sign in K2 and transcribed without '?'. Most holes come from symbols the transcribers and our key transcription name differently (see key_K2b.tsv), not from the cipher.

| Letter | Shelfmark | Cipher signs | Cipher words | Sure | Probable | Restored | Unresolved | Share |
|---|---|---|---|---|---|---|---|---|
| 6 Aug (PS 8 Aug) | 18-14 | 427 | 154 | 75 | 60 | 14 | 5 | 0.487 |
| 13 Aug | 18-12 | 383 | 155 | 92 | 51 | 6 | 6 | 0.594 |
| 17 Aug | 18-3 | 635 | 264 | 170 | 78 | 6 | 10 | 0.644 |
| 25 Aug (PS 27 Aug) | 18-11 | 238 | 113 | 64 | 42 | 2 | 5 | 0.566 |
| 3 Sep (PS 4 Sep) | 18-10 | 235 | 102 | 73 | 25 | 0 | 4 | 0.716 |
| **Total** | | 1,918 | 788 | 474 | 256 | 28 | 30 | **0.602** |

(Brianson dated the first letter 5–6 Aug in 1983; his typescript and the letter say 6 Aug, postscript 8 Aug.)

## Where the cipher reads differently from Brianson's typescript
Word level, each checked against the signs (details in each reading file):
- 17 Aug: « de cette **division** » (46¨ = di, two clear dots) where he typed REVISION; « creu **m'en** devoir ouvrir » (he omits m'en); « n'en parle **plus** », « ne sera **pas** cogneue », « ne doute **plus** » (94′ plus / 84′ pas; his PLUS and PAS are swapped); « en mesme **estat** » for his restoration (TEMPS); « en **ce rencontre** » for « cet encontre »; « ou **chevalier** Todias » (81¯) for his (PAR); « l'**alarme** » for his restoration (ENNUI); he adds AI before « respondu » (no sign); his ?/1 (twice) = **Bordeaux** (18¯ in his own key) and ?/9 = **avec** (48ˇ).
- 13 Aug: « **entretienne** » (67¨ 67~ 69¨ 55′, all sure) for his « entreprenne »; « **ie** n'aye » (he omits ie); « **des** » (51~) for « de »; « n'entre » (sing.) for « n'entrent »; his bare 18̄ = Messieurs de **Bordeaux** (his own key).
- 6 Aug: « l'**aboutissement dans** ces messieurs » (50ˇ, 49¨, both in his key) for his « l'(accord) de ces messieurs »; the cipher opens a passage with « **utiles** » (54ˇ), which he leaves out, and has no « toutes les nouvelles »; word order « rentrent en pas vne » vs his « pas en une ».
- 25–27 Aug: he leaves out the cipher clause « il faut **n'y avoir aucun esgard** » (also in the brown-ink gloss); « l'envoy de vre **homme** » (HOMME is in cipher; he reads the clear « vre » as « vivres »); his 18̄ = **Bordeaux**, his restoration (province) = **Guyenne** (65¯, his key). The brown-ink glosses agree with the cipher where they exist.
- 3–4 Sep: « les armes à **Bordeaux** » (he leaves 18̄); « en estat de **faire** prendre »; « **d'**autant que ». Date: « De Paris le 3e septembre 1651 » as Brianson (not « 23e »: the postscript of the 4th answers « la vostre du dernier du mois passé »).
- Codes he left ?/n and still open here: 96 (×6; he suggests du Dognon in 1983), 97 (×4; Laisné), 99, 59 (bare; 59¯ = Richelieu in his key), 66′, 98′, 12~, 35~, 62′, 8¯, and the marginal insertion of 17 Aug « 85 π 38 68 33 32 / 95 » (« ‹85› et tous ‹95› »; his « lire par un … … » is unread clear text, not this insertion).
- Where he reads more than the frozen key gives (counted as holes here): rien, car comme, nous en, vaisseaux, succès; nos ennemis, leurs, ses vues, jugerez, important, Madame; Conseil (29¨), Madame (83¯), avoir (45ˇ), pas (83′), la dessus / la maniere.

## K2b (key_K2b.tsv) — not validated
Corrections found after decoding: the transcribers' low π = Brianson's « pi-barré » (e), their « w » = his « u » (n), their б-shaped « sigma » = his U/V « 6 » (u/v); 19′ = le, and 18′ = la (his grid's acute row seems shifted by one column); 45ˇ avoir, 98 bien, 48 du, 83′ pas, etc. No fresh held-out portion remains, so K2b is not validated and is never used for a sure word.

## Not done
No reading_review recorded (left to the reviewer). The blank 1652 nomenclator (715–717) was not studied. No image or crop in this folder.

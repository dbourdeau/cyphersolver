# AN 400AP/57, d. 1: Emperor ↔ Empress telegrams and Lasry's key (17 Nov 2026)

Contributed by Jozef Krajčovič (kjfriedo) with an AI model (Claude). Images in `images/400AP57/` (greyscale, 1400 px; Archives nationales, 400AP/57). Groups and proposed values are in `400AP57_emperor_empress_tokens.tsv`. The groups were read from the images by one reader and not checked by a second.

**Source:** AN 400AP/57, dossier 1 ("Dépêches télégraphiques", Apr–Jul 1859), 422 images. Frames `DAFANCH97_MIC014002331`–`2752`; image n = frame 2330+n. From img 177 on, the dossier is "Dépêches télégraphiques 13 mai – 18 juillet 1859": the Emperor's cabinet minutes and the telegraph copies, often partly in clear.
Key: `lasry_key.csv` from the cyphersolver repository (242 values, codes 1–1396).

## 1. Two code systems in the Emperor–Empress correspondence
| system | code range | telegrams (img) |
|---|---|---|
| **A = Lasry's key** (one-part, alphabetical, ≤ 1396) | 1–1396 | 180, 188, 235, 244, 257, 305, 362+363, 366, 410 |
| **B = a second code** (values up to about 2060; also used for Walewski, e.g. img 277 right) | to about 2060 | 178 (13 May), 277 (4 Jul), 326 (8 Jul), 335 (9 Jul), 341 (9 Jul), 343 (10 Jul), 388 (12 Jul), 405 (13 Jul) |
System B does not decode with Lasry's key (0–2 values per telegram match, and those only by chance). The numbers in the headers ("163-358", "163-865", "865", "493", "570", "936", "1115") are probably telegraph or register numbers, not key indicators: 865 appears both on a system A telegram (305) and on a Walewski one (303).
All processed. 327 is the Inspector General's telegram to Dr Conneau, not Emperor–Empress. 421 (Empress → Emperor, 15 July) is in clear.

## 2. System A: transcriptions and readings
Notation: code=value (Lasry's value); **code=NEW** is a new value proposed here; [ ] = unknown. The `near.py` neighbours in the key were checked for each new value: the alphabetical position fits unless stated otherwise.

**img 180, Empress → Emperor, Paris 13 May 11.15 a.m.** (clear: "ici tout va bien … j'ai eu le temps d'écrire hier par la poste")
`708 le · 1264 [?] · 30 a · 1303 [tra-?] · 30 a · 398 du · 1385 vous · 506 fa · 1265 ti · 583 gu(er)=NEW` → "… a dû vous fatiguer"
`677 je · 113 attends=NEW · 323 de · 1379 vos=NEW · 230 chères=NEW? · 859 nouvelles=NEW · 422 [?]`

**img 188, Emperor → Empress, 26 May, 12.50 p.m.** (clear: "Je rentre à l'instant" … "même quand cela n'est pas vrai")
`677 je · 1312 trouv · 708 le · 222 [?] · 783 ment · 772 mauvais=NEW · 888 on · 834 ne · 382 doit=NEW · 672 jamais=NEW · 372 dire=NEW · 1044 qui · 464 est · 114 au · 357 des · 1214 sous=NEW · 400 [de sa?] · 1241 ta · 227 ch(e)`
→ "Je trouve le [ ]ment mauvais; on ne doit jamais dire qu'il est au-dessous de sa tâche, même quand cela n'est pas vrai."

**img 257, Emperor → Empress, Cavriana 29 June, 8.05 a.m.** (clear: "il est difficile de donner dans les premiers moments des renseignements précis")
`1316 tu=NEW · 834 ne · 264 compr=NEW · 432 en · 926 pas · 109 assez · 251 com=NEW · 160 bien`
→ "**Tu ne comprends pas assez combien** il est difficile …" (432 "en" is used as a syllable: compr-en-ds).

**img 244, Emperor → Empress, Cavriana 27 June** (clear: "Rien de nouveau. Je me suis décidé" … "Nous avons eu le 24 toute l'armée autrichienne sur les bras")
`125 avant · 323 de · 766 march=NEW · 453 er · 432 en · 125 avant · 30 à · 509 faire · 708 le · 1188 siège=NEW · 323 de · 932 Pe · 1142 s · 233 chi · 1059 ra=NEW · 1051 [?] · 834 ne · 1174 sera=NEW · 926 pas · 737 longue`
→ "… avant de marcher en avant, à faire le siège de Peschiera, [qui] ne sera pas longue." The second part (779 357 293 …) is not read.

**img 305, Emperor → Empress, Valeggio 7 July, 10.25 a.m.**
`1325 une · 1236 sus=NEW · 938 pens=NEW · 656 ions · 323 de · 1001 [?] · 464 est · 38 ac=NEW · 208 cep=NEW · 1249 te · 445 en-=NEW · 1263 [ ] · 323 de · 1283 [ ] · 465 et · 803 moi · …`
→ "Une suspension de [1001 = 'armes'? the alphabetical position does not fit] est acceptée entre [1263 323 1283] et moi …"
Clear at the end: "Dès que cela sera réglé" + `677 je · 1366 [ ] · 708 le · 1348 [ ] · 1279 [ ]`.

**img 362, Emperor → Empress and Walewski, Valeggio 11 July, 11 p.m.**
`702 la · 909 paix=NEW · 464 est · 1190 signée=NEW · 445 en- · 1263 [ ] · 3283(=1283?) · 465 et · 803 moi · 621 il · 38 ac · 208 cep · 1249 te · 1325 une · 266 con=NEW · 515 fé · 323 dé · 1059 ra · 1274 tions · 664 it · 69 al · 432 i-en · 834 ne · 1214 sous · 702 la · 1002 pré=NEW · 433 si-/-dence?=NEW · 600 hon=NEW · 62 aire=NEW · 398 du · 1873 [Pape?] · 621 il · 773 me`
→ "**La paix est signée entre [l'Empereur d'Autriche] et moi. Il accepte une confédération italienne sous la présidence honoraire du [Pape]** …" This is the content of the Villafranca preliminaries, 11 July.
- 1059 = ra is confirmed twice: con-fé-dé-ra-tions (362) and Pes-chi-ra (244).
- 1263 + 1283 together stand for "the Emperor of Austria" in both 305 and 362. The value is placed by context, and its alphabetical position does not fit; perhaps it is an additional entry, like Rome, Piémont and Sardaigne in Lasry's key.
- 1873 is above the key range (≤ 1396). It is either a misreading or an addition.

**img 410, Emperor → Empress, Desenzano 14 July, 7.25 a.m.** (clear: "Je pars pour Milan")
`465 et · 938 pens(e) · 483 être=NEW · 30 à · 959 [place] · 708 le · 19 [number: dix-sept?] · 114 au · 770 mat · 636 in`
→ "… et pense être à [959] le [19] au matin."


**img 363, continuation of 362** (clear at the end: "partie intégrante de la confédération")
`203 cède=NEW · 1184 ses · 397 droits=NEW · 1252 [ ] · 773 me · 1040 que · 677 je · 1074 re · 789 mets=NEW · 114 au · 1132 roi · 323 de · 980 Piémont · 621 il · 278 conserve=NEW · 702 la · 1339 Vé-=NEW · 834 né · 1266 -tie=NEW · 753 mais · 422 elle=NEW · 510 fait`
→ "**[Il] cède ses droits [sur la Lombardie?] … que je remets au roi de Piémont; il conserve la Vénétie, mais elle fait partie intégrante de la confédération.**" These are the Villafranca terms. 834 "ne" is used as the syllable "-né-" here.

**img 366, Emperor → Empress, Valeggio 11 July, 3.50 p.m.** (clear: "Je reviens de Villafranca" … "la décision prise")
`1284 tout=NEW · 1162 se · 464 est · 760 [ ] · 927 passé · 853 nos=NEW · 834 né · 565 go=NEW · 237 ci · 889 ons · 199 ce · 1201 soir=NEW · 677 je · 1249 te · 84 an=NEW · 825 [non] · 210 cer=NEW · 59 ai`
→ "Je reviens de Villafranca. Tout s'est [ ] passé. Nos négociations … ce soir je t'annoncerai la décision prise."

**img 235, Emperor → Empress, Cavriana 26 June, noon:** 60 groups, only partly readable. It contains 1325 une, 1040 que, 197 cau-, 1162 se, 863 nu (← "cause"), and others. Not processed further.

## 3. New values proposed for Lasry's key (system A)
| code | proposal | evidence |
|---|---|---|
| 1059 | ra | 2× (con-fé-dé-**ra**-tions; Pes-chi-**ra**); between Rome and rapports |
| 909 | paix | context (Villafranca); between où and pain |
| 1190 | signée | between si and sion |
| 38 / 208 | ac- / -cep- | 2× (accepte / acceptée, 305 and 362) |
| 445 | en- (entre) | 2× (305, 362) |
| 938 | pens | 2× (sus-**pens**-ions; et **pens**e) |
| 1316 | tu | between trouv and u; "tu ne comprends" |
| 264 / 251 | compr- / com- | "compr-en-ds", "com-bien" |
| 766 / 1188 / 1174 | march- / siège / sera | 244, alphabetical position fits |
| 382 / 672 / 372 / 1214 | doit / jamais / dire / sous | 188; 1214 also in 362 ("sous la présidence") |
| 772 | mauvais | 188, between materielle and me |
| 266, 1002, 600, 62 | con- / pré- / hon- / -aire | 362 |
| 113 / 1379 / 859 | attends / vos / nouvelles | 180 |
| 483 | être | 410 |
| 1236 | sus- | 305 |
| 583 | -guer | 180 |
| 203, 397, 789, 278, 1339, 1266, 422 | cède / droits / mets / conserve / Vé- / -tie / elle | 363 (Villafranca terms) |
| 1284, 853, 565, 1201, 84, 210 | tout / nos / go / soir / an- / -cer- | 366 |
These are proposals for George Lasry to check. They were made by the same reader without a held-out test. The strongest are those with two independent occurrences: 1059, 38/208, 445, 938 and 1214.

## 4. What remains
- Finish 235 and the second part of 244.
- System B: a separate code. A key-recovery attempt with the clear passages is a separate task.

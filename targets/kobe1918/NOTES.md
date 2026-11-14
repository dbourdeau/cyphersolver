# kobe1918: Department of State cipher telegrams with the consul at Kobe, 30 Jan - 9 Feb 1918 (Red Code of 1876)

Status: read in part (K3: 2 of 5 groups unread; K1, K2, K4, K5 read) (contributed by Brice Dudout, Europe chiffree, with Claude Opus 5.5 agents). Not in the catalogue and not in leads.json; no DECODE record.
Content EXISTING: the clear texts sit on the same file. What is new: the identification of the code and about 70 reusable group values.

## Document
Five numerical telegrams between the Department of State and Robert Frazer Jr., American consul at Kobe, on the "Thyssen" article of the Japan Chronicle of 11 Dec 1917. NARA, RG 59, Central Decimal File 1910-29, 763.72/8789a-8802, microfilm M367 roll 70 (NAID 27099122), images 0474-0477 and 0502 (clear texts); cipher telegrams on M367 rolls 80-81 (rolls 80/0619-0621, 81/0703-0706). Public domain; no image is reproduced here.
Found by an OCR sweep of M367 rolls 80-88 (7 371 images; Auckland 1918 turned up as calibration, already solved).

## System and key
Five-digit groups, one group per word or phrase, ordered alphabetically (one-part code). The notes "Red" on the Department's copies and "RED" on the decoded copies, the two values printed by Weber (from the = 31049, and = 12792) and an order test over 69 pairs identify the **Red Code of 1876** (J. H. Haswell, The Cipher of the Department of State; number = page x 100 + line). The codebook is on NARA microfilm T1171 (catalog id 417267710), the source William Echols used for roosevelt1903 in this repository (issue #353, 9 Nov 2026); it was not consulted for this folder, so key.tsv is the list of 69 values read off the period clear texts. One value agrees with roosevelt1903's key: 47372 = request. The five-letter words BURGY, COLRI, COMFY, COPKY are date-time words (month, tens digit as vowel, units, hour as consonants, final y = p.m.): BURGY = 30 Jan 5 p.m., COLRI = 7 Feb 10 a.m., COMFY = 8 Feb 4 p.m., COPKY = 9 Feb 6 p.m. (22 further cases May-July 1918 seen in the sweep).

## Validation
Order test 0.9996 against 0.597 for 200 permutations (validation.txt). Not a held-out reading: there is no untouched portion, the clear texts are filed with the cipher.

## Prior art
Weber, Masked Dispatches (NSA) describes the ancestor of the date-time scheme (Adee 1900, Blue Code), not the 1918 one. Weber 1979 (United States Diplomatic Codes and Ciphers 1775-1938) not consulted (restricted lending): open. Nothing in this repository (catalogue.json, research/leads.json, targets) on Kobe, Frazer or Thyssen (12 Nov 2026 check, repeated 14 Nov); the same Red Cipher of 1876 is the key of roosevelt1903 (1903, issue #353); FRUS 1918 has nothing on the affair.

## Remaining gaps
- K3 (5 groups): clear text not located (probably in 763.72/8790 or 8802); LILUM, EO unread.
- Digit readings of the five telegrams should be re-checked at full resolution.
- The codebook pages (NARA T1171, catalog id 417267710) should be checked for K3 (LILUM, EO) and for the groups not in key.tsv (K2: 57010, 43000, 36715, 24336, 50552; K4: 52356; K5: 25027, 51685, 41596); 24336 and 41596 may be misreadings of 24338 and 41598.

## Escalation
Siblings: the sweep M367 rolls 80-88 found no other ciphered file; roll 79 (763.72/9001) was not swept. Print: Weber 1979 not checked. Key rebuild: stopped at the values the clear texts give. No blocker is inside the five telegrams.

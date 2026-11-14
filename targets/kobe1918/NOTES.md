# kobe1918: Department of State cipher telegrams with the consul at Kobe, 30 Jan - 9 Feb 1918 (Red Code of 1876)

Status: in progress (integration check, 14 Nov 2026: read in part, 109 of 111 tokens read (98.2%); K1, K2, K4 and K5 read, the groups they left open now found in the codebook, K3 read in part (25131 burgy 15761 = "Department's [telegram of] January 30, 5 p.m.: August", "lilum" begins the spelled name THYS..., the rest open). The K3 gap can still be worked from the codebook images in hand, so no page yet.)

Contributor's status: read in part (K3: 2 of 5 groups unread; K1, K2, K4, K5 read) (contributed by Brice Dudout, Europe chiffree, with Claude Opus 5.5 agents). Not in the catalogue and not in leads.json; no DECODE record.
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

- K3 "lilum" letter 5 and "eo" (2 tokens) - blocker: not-attempted; "lilum" reads THYS with spelling division 1 and the key 25131 (codebook_check.tsv); spelling divisions 2 and 3 (pages 580-581, image 0578), other choices of key digits and a one-letter mutilation not tried. Frazer's letter of 12 Feb says the undated telegram made the meaning clear
- K3's clear text (a Department copy) - blocker: not-attempted; the Department's file 763.72/8790-8802 and Frazer's despatch of 12 Feb (roll 81, 763.72/9242 on the image) are where it would be
- 53 of the 76 values of key.tsv not yet compared with their codebook pages (23 compared, all agree) - blocker: not-attempted; the codebook images are online

## Escalation

- [x] siblings: the sweep of M367 rolls 80-88 found no other ciphered file in this affair; roll 79 (763.72/9001) not swept; roosevelt1903 uses the same codebook
- [x] clear-pages: the clerks' clear texts of K1, K2, K4, K5 (roll 70) and Frazer's despatches of 7 and 12 Feb (roll 80 0619-0620, roll 81 0703) read
- [x] known-keys: the Red codebook of 1876 (NARA T1171 roll 1) found online and used: 23 groups and spelling division 1 (integration check, 14 Nov 2026)
- [ ] print: Weber 1979 (United States Diplomatic Codes and Ciphers) not seen
- [n/a] key-rebuild: the key is a printed codebook
- [ ] retry: K3 with spelling divisions 2-3 not yet tried

## Integration check (14 Nov 2026)

Verified for the maintainer before merging PR #561 (Brice Dudout). The PR carries no scripts; the checks below were made with a decoder and an order test written for the check.

- **Images.** The NARA images are public and fetch with curl from catalog.archives.gov (records API `catalog.archives.gov/proxy/records/search?naId=27099122` for roll 70 lists the files; rolls 80 and 81 sit under the same path, `.../M367/M367_Box_3_70-121/M367_RollNN/M367_RollNN-NNNN.jpg`). Compared group by group: K1 on roll 80 image 0619 (Frazer's despatch of 7 Feb quotes it: 27 groups, all agree); K2 on roll 80 image 0621 (30 groups; 24336 and 50552 doubtful on the image, see below); K3 on roll 81 image 0704 ("25131 burgy 15761 lilum eo Polk Acting", agrees); K4 on roll 81 image 0705 (27 groups, all agree); K5 on roll 81 image 0706 (18 groups: four misread in the PR, 57571 for 57371, 40910 for 40810, 49816 for 48816, 41596 for 41598; two more doubtful, 25027/23027 and 51685/31683). The confirmation copies are typed in a heavy face in which 3 and 5, and 6, 8 and 9, are hard to tell apart. transcription.txt corrected; the old readings are in git history.
- **Codebook.** The codebook the PR left unconsulted is online: NARA T1171 roll 1, "Codebooks of the Department of State, 1867-1876", catalog id 417267710, 587 images, one printed page per image (group = page x 100 + line). 23 groups looked up (codebook_check.tsv): every value of key.tsv that was checked agrees with its entry; the groups the PR had left open are Message words (57010), Period (43000), Japan (36715), Telegram (52356); the doubtful digits are decided by the entries (24338 December, not 24336 Deceives; 50352 Some, not 50552 Speaker; 23027 Copied; 31683 Got, not 51685 To supersede; 48816 Scotland). key.tsv now holds 76 values (7 added, 2 group numbers corrected; labels stay headwords, the full entries are in codebook_check.tsv).
- **Which book (14 Nov 2026, from roosevelt1903).** Roll 1 of T1171 holds two books: images 0005-0089 are the 1867 letter-group code (the roll's NARA target sheet, "Cipher and Key, July 1, 1867", belongs to it), and image 0090 opens "The Cipher of the Department of State" (Government Printing Office, 1876), with a slip at image 0094 headed "To be attached to page 9, Red Cipher of 1876". The numbered pages looked up here are in this second book, so the name Red Code of 1876 is confirmed by the images (roosevelt1903 NOTES, "Which book"). Brice Dudout (PR #565) had flagged the 1867 target sheet; the doubt is settled.
- **Order test.** With the corrected groups the 76 values are in perfect alphabetical order: concordance 1.000 (the PR: 0.9996 over 69 values, its one inversion was the misread 49816); best of 200 shuffles 0.598. Reproduced with an independent script; this tests the structure of a one-part code, not a reading.
- **K3 and the spelling code.** The codebook's spelling code (pages 579-581) is the table roosevelt1903 used (rows chosen by the digits of the first number group; the rule reads that telegram's U A W C as K I E L, checked here on division 1). With 25131, rows 2 5 1 3, "lilum" gives T H Y S. Frazer's despatch of 12 Feb (roll 81 image 0703) says the undated telegram "made the meaning of the Department's original message of January 30 quite clear", and K1's mutilated groups were the name: K3 respells "Thyssen". M, E, O are unread.
- **Count.** 111 tokens; read 109 (K3's "lilum", read only in part, and "eo" are holes): 98.2%, the contributor's figure; the groups the PR had read from the clears alone now have their codebook entries. Above 95%, but the K3 gap is workable (spelling divisions 2-3), so in progress, no page.
- **Outcome method.** The Department's copies are marked "Red", and the Red codebook, applied here, gives every group; four of the five telegrams also have the clerks' clear texts, the existing decipherment the contributor used. Method set to "read with known key"; the PR had "key recovered based on adjacent plaintext" (69 values read off the clears), which describes the contributor's own route. To decide at write-up time.
- **One key, one entry.** roosevelt1903 (Roosevelt to Hay, 1903) is read with the same codebook. The two are separate correspondences fifteen years apart sharing a printed departmental codebook; they are cross-referenced here and kept as separate folders for now. At write-up the owner decides whether the Red Code gets one entry. roosevelt1903's page says the codebook pages were not reachable: they are now (images listed above; 47372 Request checked on its page), so that page is owed a correction when it is next reviewed (not changed in this check).
- **Prior art and duplicates.** Kobe, Frazer, Thyssen: nothing in catalogue.json, research/leads.json or targets (14 Nov 2026). Weber 1979 not seen.
- **Checkers.** `_check_profile.py kobe1918`: valid. `_check_catalogue.py`: valid.

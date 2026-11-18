# abel1797: Christoph Konrad Abel (Wuerttemberg minister in Paris) to Duke Frederick II, 1797-1799: nomenclator rebuilt and validated

Status: in progress (17 Nov 2026 update by the contributor: read in part, 21 of 24 words of the unglossed passages sure = 87.5 % by the strict rule, 23/24 with the probables; six codes found with glosses of the time in Bü 700-701, glossed_codes.tsv; one code, ut, still open. Integration check of 14 Nov 2026: 14/24 = 58.3 %, see below. Catalogue lead 2037 points to this folder.)

Contributor's status: read in part (contributed by Brice Dudout, Europe chiffree, with Claude Opus 5.5 agents; 28 Oct 2026). Not in catalogue.json (only Wolzogen 1792-93 for Wuerttemberg: nos 525, 578, 579), not in leads.json, no target, no DECODE record.
Every enciphered passage seen has a contemporary decipherment in the file, so the content is EXISTING. What is new: the key K3 as a validated table, 24 words read from passages with no clear text, and one correction of a later gloss.

## Documents
Hauptstaatsarchiv Stuttgart, A 16 a (Gesandtschaftsberichte) Buendel 696 (Paris, Oct-Dec 1797, 50 images; Talleyrand, Rastatt, Campo Formio, indemnities, secularisations), 699 (1798, 149 images), 701 (1799, 173), 702 (Jan-Jun 1799, 39), 706 (Normann 1801, 16). Landesarchiv Baden-Wuerttemberg online viewer, images under Public Domain Mark 1.0 (plink http://www.landesarchiv-bw.de/plink/?f=1-515046 and ?f=1-515052); no image is reproduced here.

## System and key
Mixed nomenclator: (a) groups 1-99 = letters with homophones (a 3/9, n 70/67, f 1/7, d 10/11, i 31/30, e 15/sigma); (b) two-letter lower-case codes = words (cc die, cb der, hh ich, gw dem Herzog, cl Directorium, dt Frieden, hs Indemnisationen, hf Kayser, dr Frankreich ...), with flexion exponents; (c) groups >= 100 = nulls; (d) "90" alone = und. Doubled letters are often written once (not always: 54 54 = ll in the held-out piece); the score collapses doubles on both sides. In the held-out transcription the sign σ (e) was written 8, and 8d stands for 0d (82 = 02 = t, 81 = 01 = s): the normalisation 8 -> σ, 8d -> 0d is fixed in frozen/PROTOCOLE-v3.md. Open in K3: 00 is r by a tie broken mechanically (i in 1798-99 is likely), 5 = c and 6 alone = als are not in the frozen table. Same table in 1797 and 1799 with extra homophones in 1799 (4 = b, 21 = u, 23 = m, 26 = h, 33 = y, 72 = o, 01/03 = s). A second system (groups 60-89 only, strongly homophonic) appears in 1798 (Bue 699 Bild 20, 22, 53); Normann's reports of 1801 (Bue 706) use another table. The original keys (A 11 Bue 66, L 6 Bue 1392, A 74 i Bue 24) are not online.

## Validation
K3 validated on a held-out piece (Bue 702 Bild 17): 0.963 characters / 0.792 words against 0.306 / 0.167 for 200 permuted keys. The 1797-only key (0.621 words) and K2 (0.367) were not validated: stated in validation.txt.

## Reading
Passages without clear text (Bue 699 Bild 75, 86, 90): 24 words. First reading (28 Oct): 14 sure, 6 probable, 4 unresolved (58 % strict). Update (17 Nov, reading.md, glossed_codes.tsv): sw von, ka man, ld nach, 33 s, ps Teutschland, vf wollte and oi sicher- found glossed in Bü 700-701; 21 sure, 2 probable ({sicherer}, {hier}), 1 unresolved (‹ut›): 21/24 = 87.5 % strict, 23/24 = 95.8 % with the probables. Read in part by the strict rule. Clear: "Nach dem was ich von {sicherer} ‹ut› weiss, [glaubt man,] dass man von {hier} den Geist der Revolution in Teutschland wollte gehalten [...]"; "Taleyrand"; "nach Baras Antrag". A later pencil gloss "Georgi" on Bue 696 Bild 50 is wrong: the key reads "albert" and the next clear paragraph is about Albert.

## Prior art
Web search (Abel / Konradin Abel, Paris 1797, Chiffre; Cryptiana): no edition or study of the cipher. Obser, Politische Correspondenz Karl Friedrichs von Baden, vol. 3: Abel cited in passing only. Hoelzle, Wuerttemberg im Zeitalter Napoleons (1937): not seen. Nothing in this repository (checked 12 Nov 2026).

## Remaining gaps

- Code ut in Bü 699 Bild 75 (1 word) - blocker: not-attempted; not found glossed in Bü 700 (42 images) or Bü 701 Bild 35-173 (17 Nov 2026); Bü 701 Bild 1-34 only partly examined at reading size
- hb ("hier") probable by sense and its place in the code list; ending of oi ("sicher-") not marked in Bild 75 - blocker: not-attempted
- No unglossed passage of 300 signs or more found in Bü 696-702 (every enciphered passage opened carries its decipherment of the time): K3 cannot be re-tested on new unglossed text - blocker: no-key-material
- Bü 706 (Normann, another table) and the 1798 second system (Bü 699 Bild 20, 22, 53; also Bü 700 Bild 3, 10) - blocker: not-attempted
- Hoelzle 1937 - blocker: not-attempted; not seen

## Escalation

- [x] siblings: Bü 696, 699, 702 sorted piece by piece (contributor); Bü 700 all and Bü 701 Bild 35-173 searched on 17 Nov 2026 (all glossed); Bü 706 not
- [x] clear-pages: every glossed passage seen used to build K1-K3
- [ ] known-keys: the chancery's own keys (A 11 Bü 66, L 6 Bü 1392, A 74 i Bü 24) not online, not seen
- [ ] print: Obser only; Hoelzle 1937 not seen
- [x] key-rebuild: K3 rebuilt from the glosses and tested on a held-out glossed piece
- [x] retry: the four codes and six probable words searched in Bü 700-701 (17 Nov 2026): six confirmed by glosses of the time, oi made probable, hb still probable, ut open

## Integration check (14 Nov 2026)

Verified for the maintainer before merging PR #563 (Brice Dudout). The PR carries no scripts; the checks below were made with a decoder written for the check from key.tsv.

- **Held-out test reproduced.** Decoding the held-out set (Bü 702 Bild 17 and the end of Bild 16, 24 words) with key.tsv, the normalisation 8 = σ = e and 8d = 0d, doubles collapsed: 19 of 24 words exact (0.792) and about 0.963 of characters, as stated. The word figure of the 200 shuffled keys (0.167) is the four "und" (90 alone), which score whatever the key; without them the key gets 15 of 20 (0.75), exactly the bar. The SHA-256 of key_K3.json is the one frozen (ec57a044...); the protocol files hash as listed. The order of events (key frozen at 20:48, Bild 17 transcribed after) rests on self-recorded times: by the contributor's record.
- **Earlier keys failed, as reported.** The 1797 key (words 0.621) and K2 (words 0.367) failed the declared word bar; both are recorded as failed tests in profile.json.
- **Images.** The Landesarchiv viewer serves full images with curl (`https://www2.landesarchiv-bw.de/ofs21/bild_zoom/bild.php?...&originalBilddatei=/data/bildcms/internetbilder/archiv_1/olf/bestand_0000008115/titlaufn_0000NNNNNN/01_0000NNNNNN_BBBB_1-NNNNNN-B.jpg`; Bü 696 = 515046, Bü 699 = 515049, Bü 702 = 515052). Bü 702 Bild 17: about 55 groups of the held-out words compared (helvetische, ihrem, ganzen, oestreich, angegriffen, sollte): agree, except that "angegriffen" has one 20 after 67 on the image (a first sign, 9 or 3, then 67 20 15 20 ...) (the transcription's "9 67 20 20 15 20" has an extra 20; the score is unchanged because doubles collapse). The marginal gloss is the held-out clear text, as stated. Bü 699 Bild 75: both passages (13 and 33 tokens) agree with the transcription at the size viewed. The header of Bild 75 reads "Paris d. 1[2 or 5]. julii 1798": NOTES' 12 Jul not settled.
- **Reading.** Decoding the three unglossed passages with key.tsv gives "[ld] dem was ich [sw] [oi] [ut] weiss" / "dass [ka] [sw] [hb] den geiyt der revolution in [ps] [vf] gehalten" / "taleirand" / "nach baras antrag", as reading.md says. Strict count 14/24 = 58.3% reproduced (the contributor's own strict figure); with the probable words 20/24 = 83.3% (contributor's). Read in part.
- **Prior art and duplicates.** The PR says the correspondence is not in leads.json: it is lead 2037 (Landesarchiv BW sweep, A 16 a Bü 696, 699, 701, 706), closed "read" on 3 Nov 2026 because every passage opened there had its decipherment written over it. The unglossed passages found here go beyond that vetting; the lead's status now points to this folder (the lead stays closed: its verdict is the glossed bulk; the unglossed passages are worked here).
- **Outcome method.** "Key recovered based on adjacent plaintext" kept (K3 rebuilt from the glosses in the same file).
- **Checkers.** `_check_profile.py abel1797`: valid. `_check_catalogue.py`: valid.

# abel1797: Christoph Konrad Abel (Wuerttemberg minister in Paris) to Duke Frederick II, 1797-1799: nomenclator rebuilt and validated

Status: read in part (contributed by Brice Dudout, Europe chiffree, with Claude Opus 5.5 agents; 28 Oct 2026). Not in catalogue.json (only Wolzogen 1792-93 for Wuerttemberg: nos 525, 578, 579), not in leads.json, no target, no DECODE record.
Every enciphered passage seen has a contemporary decipherment in the file, so the content is EXISTING. What is new: the key K3 as a validated table, 24 words read from passages with no clear text, and one correction of a later gloss.

## Documents
Hauptstaatsarchiv Stuttgart, A 16 a (Gesandtschaftsberichte) Buendel 696 (Paris, Oct-Dec 1797, 50 images; Talleyrand, Rastatt, Campo Formio, indemnities, secularisations), 699 (1798, 149 images), 701 (1799, 173), 702 (Jan-Jun 1799, 39), 706 (Normann 1801, 16). Landesarchiv Baden-Wuerttemberg online viewer, images under Public Domain Mark 1.0 (plink http://www.landesarchiv-bw.de/plink/?f=1-515046 and ?f=1-515052); no image is reproduced here.

## System and key
Mixed nomenclator: (a) groups 1-99 = letters with homophones (a 3/9, n 70/67, f 1/7, d 10/11, i 31/30, e 15/sigma); (b) two-letter lower-case codes = words (cc die, cb der, hh ich, gw dem Herzog, cl Directorium, dt Frieden, hs Indemnisationen, hf Kayser, dr Frankreich ...), with flexion exponents; (c) groups >= 100 = nulls; (d) "90" alone = und. Doubled letters are often written once (not always: 54 54 = ll in the held-out piece); the score collapses doubles on both sides. In the held-out transcription the sign σ (e) was written 8, and 8d stands for 0d (82 = 02 = t, 81 = 01 = s): the normalisation 8 -> σ, 8d -> 0d is fixed in frozen/PROTOCOLE-v3.md. Open in K3: 00 is r by a tie broken mechanically (i in 1798-99 is likely), 5 = c and 6 alone = als are not in the frozen table. Same table in 1797 and 1799 with extra homophones in 1799 (4 = b, 21 = u, 23 = m, 26 = h, 33 = y, 72 = o, 01/03 = s). A second system (groups 60-89 only, strongly homophonic) appears in 1798 (Bue 699 Bild 20, 22, 53); Normann's reports of 1801 (Bue 706) use another table. The original keys (A 11 Bue 66, L 6 Bue 1392, A 74 i Bue 24) are not online.

## Validation
K3 validated on a held-out piece (Bue 702 Bild 17): 0.963 characters / 0.792 words against 0.306 / 0.167 for 200 permuted keys. The 1797-only key (0.621 words) and K2 (0.367) were not validated: stated in validation.txt.

## Reading
Passages without clear text (Bue 699 Bild 75, 86, 90): 24 words, 14 sure, 6 probable, 0 restored, 4 unresolved: strict count 14/24 = 58 %, with the probables 20/24 = 83 % (below 95 %: read in part). A later pencil gloss "Georgi" on Bue 696 Bild 50 is wrong: the key reads "albert" and the next clear paragraph is about Albert.

## Prior art
Web search (Abel / Konradin Abel, Paris 1797, Chiffre; Cryptiana): no edition or study of the cipher. Obser, Politische Correspondenz Karl Friedrichs von Baden, vol. 3: Abel cited in passing only. Hoelzle, Wuerttemberg im Zeitalter Napoleons (1937): not seen. Nothing in this repository (checked 12 Nov 2026).

## Remaining gaps
- oi, ut, ps, vf (4 codes) unresolved; Bue 699 Bild 75 could pass 95 % if they are found glossed elsewhere (Bue 701 Bild 35-173, Bue 700).
- Bue 701 (173 images) only partly examined; Bue 706 and the 1798 second system not attempted.
- Hoelzle 1937 not checked.

## Escalation
Siblings: Bue 699 / 701 / 702 / 706 sorted piece by piece (Bild list in the contributor's dossier); every other piece has its clear. Print: Obser only. Key rebuild: done (K3). Retry: needs another unglossed passage or the missing codes; no blocker inside the studied pieces.

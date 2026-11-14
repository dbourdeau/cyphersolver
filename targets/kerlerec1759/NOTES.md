# Kerlérec to the Marine minister, 1759: three cipher despatches without a period decipherment (nos. 206, 207, 215)

Status: in progress (no site page yet; target files and checks only)

Class: read in part (read with known key). The key is the Marine ministry clerks' own decipherments of two other
Kerlérec despatches, cut into code-and-word pairs with the help of Pusch's printed code book, and completed from that
code book where the clerks' pages give no pair. This is not an independent solution.

**Who read what.** The ministry's clerks deciphered nos. 194 (1759) and 228 (1760) on receipt, between the lines; those
glosses are the source of our pairs. They left nos. 206, 207 and 215 bare, and no period plaintext of them is known.
Donald E. Pusch, "Kerlérec's Cipher: The Code Book of Louisiana's Last French Governor", *Louisiana History* 49 (2008)
463-480, rebuilt the code book (Table 2, 547 of 700 entries) and says the three despatches "for which no plaintext
versions are extant" could be decoded with it (p. 468 and n. 13). He summarises the content of no. 206 (pp. 474-475:
devoted to Rochemore and those loyal to him, asks for their recall to France, sent by a Spanish priest bound for
Havana) and of no. 207 (p. 475: the Balize stripped of all cannon but two for signalling, its commander directed to
abandon the post if attacked), and shows the first coded lines of no. 215 as an image (p. 465). He quotes no French
from any of them. What we add is the first full text and translation of the three despatches, two transcriptions of
the code from the images, and a key tied to manuscript pairs with folio and line. Andrew Beling, with AI agents,
13-14 November 2026.

## Documents and limits of coverage

Archives nationales d'outre-mer (ANOM, the French overseas archives at Aix-en-Provence), COL C13A 41, Kerlérec to the
Minister of the Marine (Berryer), New Orleans. Viewer: [C13A 41](https://recherche-anom.culture.gouv.fr/ark:/61561/664449.2269381/daogrp/0)
(image numbers below are those of the viewer's first set, 302 views).

| no. | date | copy | folios (images) | code groups legible | lost in the gutter |
|---|---|---|---|---|---|
| 206 | 3 July 1759 | third | ff. 81r-82r (0162-0164) | 555 | at least 18 |
| 207 | 13 July 1759 | first, coded passage only | ff. 97r-97v (0194-0195) | 191 | 2 |
| 215 | 17 September 1759 | second | ff. 111r-111v (0222-0223) | 322 | at least 7 |

The versos run into the binding: one or more groups at the end of each line of ff. 81v, 97v and 111v are hidden. The
clear opening and closing sentences of each despatch, and the clear body of no. 207, are outside the declared units
except where quoted for context.

Files: `transcriptions/no*_pass1.txt`, `no*_pass2.txt` (second pass from the last line of each page upward, different
crops), `no*_reconciled.txt` (one disagreement in 1,068 groups, settled on the image: `readings/RECONCILE.md`);
`decoded_*.txt`, `reading_fr_*.txt`, `translation_en_*.txt`; `readings/no*_1759-*.md` (decode, normalised French,
English, words resting on Pusch, doubtful points); `readings/DOUBTS.md`; `readings/no*_side_by_side.txt` (each line
decoded with the full key and with the clerks' values only, so a reader sees which words rest on Pusch's values).

## What the despatches say

- **No. 206.** Sent in haste by a Spanish friar sailing for Havana. "The standard of revolt and independence" has been
  raised by an "infamous cabal" headed by Rochemore, with *Estrenan* the treasurer (spelled so in the cipher; the
  identification with Destréhan is ours), the family of the major Belile (Belle-Isle) with his son-in-law d'Orville,
  the Swiss captain Grondel, captains d'Erneville and d'Autrive, Mandeville and others. The horrors just done to him
  cannot be put in cipher. He asks for a strong frigate and 300 [?] Swiss troops, with orders to send the rebels to
  France for long imprisonment; the Swiss colonel Volant is furious with Grondel but kept the peace; the minister's
  despatches should be handed to the governor in person; no goods for the Indian trade are arriving.
- **No. 207.** Answering the officers' demand that a captain replace the chevalier de Villiers at the Balize, Kerlérec
  reports telling them that the post no longer commands the river mouth because the channel has moved; it once had
  thirty-odd cannon and now has two, good and bad, to answer ships' signals; and his orders were to evacuate it
  without difficulty at the sight of a certain number of enemies.
- **No. 215.** "Près de la moitié de la" (in clear) Choctaw nation is resolved to receive English traders; two years
  of efforts to bar them through the Alabama nations have failed for want of trade goods; the commandants of Tombecbé
  and the Alabamas report the traders on the march; a Choctaw war is feared that the colony cannot sustain; the
  garrison is short of nearly 900 men of 2,000; powder is nearly gone.

**Words that rest on Pusch's values alone** (220 of 1,068 groups, 124 codes): in no. 206 *infâme cabale*,
*indépendance*, *forte frégate*, *troupes*, and the *-ville* of d'Orville, d'Erneville and Mandeville and the *che*
of Rochemore; in no. 207 *évacuer*, *ordres*, *canon*, *tant bons que mauvais*; in no. 215 *traiteurs*, *hommes*,
*poudre*, *guerre*, *grand danger*. Without them those sentences are unreadable. Belle-Isle, Grondel, d'Autrive,
*Estrenan*, *suisse*, *révolte*, *deux*, *trente*, the Choctaw, the English, the Alabamas, *neuf cens* and 2000 are read
from the clerks' values alone.

## History and significance

Reading (what the despatches say) is above; this section separates established history, with its sources, from our
inference.

- Established. Kerlérec, governor 1752-1763, quarrelled from late 1758 with the newly arrived commissaire-ordonnateur
  Vincent de Rochemore; the quarrel, with officers and civilians taking sides, became known in France as the "affaire
  de la Louisiane" (Pusch 2008 p. 474, citing H. Gourmelon, *Le Chevalier de Kerlérec*, 2nd ed. 2004). In spring 1759
  the seizure of the Dutch ship *Texel* and in June the Rhode Island flag-of-truce schooner *Trois-Frères* (Captain
  Bull, taken at the Balize on 13 June 1759) set Rochemore's party against the governor; an officers' petition signed
  among others by d'Erneville, Grondel, d'Hauterive and d'Orville called Bull a spy and asked for the Balize command;
  Grondel, a captain in the Swiss troops, was on bad terms with his colonel Volant; the major Simarre de Belle-Isle
  backed Rochemore (Marc de Villiers du Terrage, *Les dernières années de la Louisiane française*, 1904, pp. 94-100).
- Established. A "feuille au Roi" of 9 October 1759 lists the persons Kerlérec complained of (Rochemore, his secretary
  Bellot, Belle-Isle, Destréhan, Fontenette, d'Erneville, d'Orville, Mandeville, Reggio) with the penalties approved;
  Rochemore was recalled, and in 1762 Belle-Isle and d'Erneville were cashiered and Kerlérec ordered Bossu, Grandchamp,
  Grondel, Rocheblave, Broutin, Mandeville and d'Hauterive back to France (Villiers 1904, pp. 140-142).
- Established. The Balize, built to guard the mouth of the Mississippi, had been left behind by the shifting mouth:
  in a letter quoted by Villiers, Kerlérec wrote that the island of the Balize, once a league offshore, was now a league
  and a half inland and the post useless (Villiers 1904, pp. 47-48).
- Established. Louisiana lacked trade goods and powder through the war and its Indian alliances depended on the goods
  (Pusch 2008 p. 475; Villiers 1904 p. 108, quoting no. 228 of 1760 on the Cherokee war and the English passage to the
  Choctaw); in February 1759 Pitt sent Amherst authority to attack Louisiana (Pusch p. 475 n. 32).
- Inference. The "horrors" of no. 206 are the late-June events of the Bull affair and the officers' petition
  (chronology from Villiers); the names in no. 206 largely match Villiers's cast (d'Erneville, d'Autrive/d'Hauterive,
  d'Orville, Grondel, Volant, Belle-Isle, Destréhan, Mandeville), though Villiers also names Reggio and Trent, who are
  not in the decode, and seems to make d'Orville Reggio's son-in-law where the cipher makes him Belle-Isle's. Whether
  the 9 October 1759 list drew on no. 206 cannot be told: no. 206 was the third copy of a letter whose other copies are
  not found, and Kerlérec complained of the same men in clear letters too.
- Inference. No. 207's Balize passage is Kerlérec's answer to the petition's demand for that command.

## System and key

Kerlérec's two-part numerical nomenclator, used unchanged 1755-1762 (Pusch 2008): about 700 numbers for letters,
syllables, words and names; nine letters have two homophones, which the code clerk usually wrote one above the other.

- `key/pairs_build.tsv`: 492 code groups from no. 194 (6 May 1759, C13A 41 ff. 51r-52v) and no. 228 (12 June 1760,
  C13A 42 f. 48r), each with the clerk's plaintext, folio, line and position; `key/pairs_heldout.tsv` the same for the
  held-out pages of no. 228 (ff. 48v-49r), aligned after the test. About 700 pairs in all.
- `key/key_manuscript.tsv`: our table, one row per code (164 codes), the clerks' reading, the number of pairs and the
  first locations. It is the key from the clerks' glosses, segmented with Pusch's table: the running gloss was cut into
  per-code pieces by an aligner that used his Table 2 as its dictionary, so it is not independent of Pusch.
- Comparison with Pusch (`key/compare_pusch.tsv`): 156 codes agree, 5 are spelling variants, 2 differ (198 *pre* where
  he has *considérable*, probably a clerk's slip for 190; 285 *tom* in *Tombekbé* where he has *ton*), 1 is not in his
  table (203, a slip for 230); 384 of his entries have no pair here.
- `key/pusch_values_used.tsv`: the 124 values taken from Pusch 2008 for codes used in nos. 206, 207 and 215 that have
  no clerk's pair, each with its page in his Table 2. His full table is not reproduced here.
- Code 208 is *cu* (Pusch p. 469 prose); an OCR slip in our extraction of his table read *eu*. Corrected after the test.

## Held-out test

Written and hashed before the held-out pages were transcribed (`test/TEST_PLAN.md`, sha256 in `test/TEST_PLAN.sha256`).
Frozen keys: merged key sha256 `b54686fb9b253cd0f1d089539fe0e4ace3ea4f0f0f949e6550ecc2c4b85cba89` (not committed: it
carries Pusch's whole table), key from the clerks' glosses `87f8ad9bc2d2a2e6ab0be7464652e4a90094c7547c018d65f41a52a4bb3ea9ef`
(`key/key_manuscript_frozen.tsv`). Held-out set: no. 228, ff. 48v-49r, 253 code groups scored.

| key | held-out groups decoding to the clerk's word | 200 shuffled keys, mean / max |
|---|---|---|
| merged | 243/253 = 96.0% | 10.8% / 17.8% |
| from the clerks' glosses (segmented with Pusch's table) | 198/253 = 78.3% | 16.4% / 24.1% |

Pass rule (merged key at least 85% and above every shuffle): passed. Caveat: Pusch's table was built partly from no.
228, so the merged key is not independent of the held-out despatch. Villiers 1904 p. 108 quotes the ministry's plaintext
of the same held-out lines, which agrees with our transcription of the gloss. Statistical validation of the reading
(`validation.tsv`, `docs/_validate.py`): pass (recorded in profile.json).

A second AI agent of ours, not shown the readings, confirmed 30 of 30 key pairs and 42 of 42 sampled groups on the page
captures and reran the test with identical numbers; its nine corrections are applied here.

## Prior readings and searches

- Period decipherment: none on any of the three leaves. C13A 41 (all 1,010 views of its three image sets) and C13A 42
  (all 638 views) were paged at thumbnail crops on 14 November 2026: no duplicate or triplicate of nos. 206, 207 or 215
  and no further coded passage beyond those Pusch lists. The bare code at C13A 42 ff. 42-47 (images 0085-0096) is the
  "Première" copy of no. 228, deciphered in its "Seconde" copy that follows it. Thumbnail paging can miss a single
  short coded line in a clear letter.
- Pusch 2008: see the top of these notes.
- Villiers du Terrage 1904 (archive.org full text, searched): narrates the June 1759 events from other papers; no
  summary of the coded parts of these three despatches.
- *Mississippi Provincial Archives: French Dominion*, vol. 5 (1984): its calendar of documents (p. 9, seen in the
  Internet Archive preview) lists for 1759 only Kerlérec's letter of 6 May; none of 3 July, 13 July or 17 September
  1759 is printed.
- Gourmelon 2003/2004: search-only on HathiTrust; not read.

## Remaining gaps

- Groups lost in the binding gutter at the line ends of ff. 81v, 97v and 111v (at least 18, 2 and 7) - blocker:
  needs-physical-access; no second copy in C13A 41-42; the Library of Congress microfilm (Louisiana Colonial Records
  Project, reel 48) or the leaves themselves would restore them.
- Codes 107, 209 and 591 in no. 206 have no value in the clerks' pairs or in Pusch's table - blocker: open-codes;
  context suggests *surpris*, *ô(ter)* and *retour*/*bord* (`readings/DOUBTS.md`); left as holes.
- The group 300 at the end of no. 206 f. 81v l. 8 (small, cramped, fully visible) may be the numeral 300 or a code
  group - blocker: open-codes; numerals and codes cannot be told apart by form in this series.

## Escalation

- [x] clear-pages: the clerks' interlinear decipherments of nos. 194 and 228 transcribed and used as the key source.
- [x] siblings: C13A 41 and 42 paged in full for other copies and coded passages; none of these three found.
- [x] known-keys: Pusch 2008 Table 2 compared code by code with the clerks' pairs and used for the remaining codes.
- [ ] print: Pusch 2008, Villiers 1904 and the MPA vol. 5 calendar checked; Gourmelon 2003/2004 not read.
- [x] key-rebuild: 452 group pairs, 164 codes, from the clerks' glosses; held-out test passed.
- [ ] retry: the three unknown codes and the gutter losses need another source (microfilm or the leaves).

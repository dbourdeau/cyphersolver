# Rubio to the head of the División del Bravo, 15 October 1913

*Update, 22 Nov 2026: Narváez's 2019 book, described below as unavailable or unchecked, has since been checked (chapters VII-XI, pp. 261-410, and the index, pp. 487-495). It prints neither the three telegrams nor Clave núm. 109. See NOTES.md.*

The telegram's two surviving sheets are in Guillermo Rubio Navarrete's archive. The first is dated 15 October 1913, addressed to Laredo, and the second ends “G Rubio.” The catalogue expands the addressee in brackets to Joaquín Téllez and the place of sending to [Lampazos]. Only the numerical passages count here. The first sheet places the clear word *vía* before ESTADESTRUIDA. The two earlier tables and the complete 78-entry table produce different levels of coverage for the seven proposed words. [CEHM, DLXXIII.1.32.6-41, record 137928](https://www.cehm.org.mx/Buscador/FichaBasica/137928?Tipo=A)

The key and both tests were registered at 16:45:13 UTC before the first response from the archive at 16:46:38 UTC. All 71 July and October 8 values were carried forward, together with seven separately marked hypotheses inferred from October 14. The seven additions had not been tested. The entire October 15 document was held out. Optical recognition of this handwritten telegram mixed scripts and merged figures. Following the predeclared handwriting rule, two fresh visual readers transcribed both sheets independently with no key, proposed reading or other transcript. Optical output was excluded throughout. Four digit tokens differ in the diplomatic reading files. Two more were excluded because a reader flagged possible truncation or an additional initial digit, even where the nominal digits agree. The frozen consensus keeps all 104 positions, 98 fully agreed, in 21 cipher runs. No pencil plaintext in the two images was used. The first page is torn at the top right. The conservatively excluded cropped numeral is in the right margin of the message body near the foot. The group sequence on the last line of the first image continues at the top of the second.

| Registered test | Coverage | Score | Control 99.5% | Controls beaten | p | Result |
|---|---|---:|---:|---:|---:|---|
| Complete 78-entry table | 76/104 groups, 40 adjacent pairs, 49 boundary trigrams | −2.1323 | −2.5150 | 1,000/1,000 | .000999 | Pass |
| Incremental contribution of the seven October 14 assignments | 7 occurrences of 3 distinct new codes, 16 affected boundary trigrams | −2.2369 | −2.2279 | 984/1,000 | .01698 | Miss |

The best complete-key shuffle scored −2.4675. The fixed table exceeded all of them and gives the required complete unrepaired words in distinct runs, including *mande*, *relevara*, *relevo*, *elementos* and *temo*. The earlier 71-entry key gave 69/104 groups and 33 boundary trigrams. The difference between its average score and the expanded table's average compares different sets of trigrams. Only the predeclared incremental test addresses the new assignments. Code 20, proposed as *i*, appears three times; 108, proposed as *le*, three; 113, proposed as *me*, once. The four other predictions, 53, 132, 140 and 147, did not occur. In particular, 140 = *pu* came from the October 14 contextual conjecture *puentes*. An X-overtyped passage before the numbers may preserve a contemporary clue. The fitter had seen that page, and October 15 has no occurrence of 140. The failed incremental test validates none of the seven values individually. The first recovered *destruida* echoes the subject and incomplete spelling of the preceding day's message. The whole-key result should be read with the distinct surrounding words.

## Cipher words

These six runs are fully legible under the frozen key. Accents and spaces are editorial. The clear connectors cited for context are excluded from the word count.

| Run | Agreed numerical groups | Letter output | Reading |
|---:|---|---|---|
| 1 | 81 158 72 34 38 33 39 20 71 | ESTADESTRUIDA | está destruida |
| 3 | 112 26 72 | MANDE | mandé |
| 4 | 145 108 165 143 | RELEVARA | relevara |
| 8 | 145 108 171 | RELEVO | relevo |
| 10 | 14 108 113 26 163 34 | ELEMENTOS | elementos |
| 20 | 160 115 | TEMO | temo |

The 78-entry table mechanically completes **7 words on a provisional division of 29**. The previously transferred 71-entry table already completes three, **está, mandé, temo** (unaccented ESTA, MANDE, TEMO). Both *mande* and *temo* occupy entire separate runs of at least two groups and four letters. The other four words require additions whose separate prospective test missed. *Destruida* uses 20 = i, a prediction from the previous day's DESTRU?DA. *Relevara* and *relevo* use 108 = le. *Elementos* uses both 108 = le and 113 = me. The seven-word figure describes the whole-key output. For readers counting only words independent of those seven additions, the tally is **3/29**, with four conditional readings. The earlier table was scored descriptively on this date. Its three-word subtotal has no separate permutation result. The fixed inputs and the full-key pass are untouched. The per-word provenance can be reproduced with `python3 -I word_sources.py`. Run 3 follows the clear *que* and precedes *para que*; the first-person accent on *mandé* is an editorial interpretation. The provisional complete inventory in oct15_words.tsv estimates 29 words over the 21 cipher runs. On that segmentation all 29 estimated words, including unresolved ones, are accounted for. The ciphertext marks clear bridges but has no interword spacings within a run. Several unresolved spans admit other divisions, especially runs 7, 9, 11, 13, 15 and 21, so an exact original word denominator cannot be recovered. All unresolved runs remain in the count. The literal output, code coverage and unknown positions have fixed denominators. The apparent *marcha* inside an unresolved sequence, even though complete as an entry, contributes no sure word.

## Prior work and remaining gaps

The CEHM catalogue groups this telegram with the Téllez papers. The open Mexican archive sweep and the Rubio target already described the numerical system and the interlined July source. The 14 October report records the local calendar, repository, historical cryptography index and available editions checked, the inaccessible Narváez monograph and the limitations on any priority claim. No human has checked the handwriting, the attribution or the editorial segmentation. The July pencil key was initially extracted by one reader. Two additional readers later checked twelve crops (see JULY_GLOSSES.md); the prospective tests measure transfer to the October documents. Expansion from either held sheet would need its own new witness.

The frozen control-count rule was at least 995 out of 1,000 scores strictly below the observation. With the plus-one permutation convention that permits p up to 6/1001. A strict .005 threshold would require 996. All reported pass and miss decisions are unchanged under that stricter interpretation.

A prospectively selected check of the next three contiguous shelfmarks yielded no qualifying telegram. Item 7 concerns Rubio and Ibarra. Items 8 and 9 are from Téllez to Jacinto Guerra. None of their catalogue descriptions identifies cipher. No image was scored on this check.

AI agents did this work; no person has checked it.

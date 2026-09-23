# Potocka and Mniszech to Jakub Dunin

Status: read in part — Potocka alphabet recovered; Mniszech not read.
Work date: 2026-09-23. Catalogue item 280, class C.

## Result and scope

Ten records were examined in all 29 source images. Nine are Barbara Potocka's mostly clear French letters, with Polish phrases and one long encrypted Polish postscript. R7524, Józef Mniszech to Dunin, uses a separate, still unread numerical system. The decipherment is of the encrypted passages, not a new edition of all the clear prose.

`reading.md` is the authoritative segment reading. `potocka-segments.tsv` preserves 96 short cipher passages, their clear anchors and editorial interpretations; `r7526-trial.txt` preserves the 163-token Polish postscript. `standalone-codes.json` inventories 23 additional person-code occurrences separately. `prepare_reading.py` applies `key-potocka.json` without silently emending plaintext and produces `reading-tokens.tsv`, per-record numeric files and `coverage.json`. These count 1,119 cipher tokens: 887 Potocka and 232 Mniszech. The recovered alphabet values 863/887 Potocka tokens (97.3%), or 863/1,119 (77.1%) across the request. This is **key coverage, not 97.3% verified prose**. Four person codes (87, 94, 100, 270; 23 occurrences) and the exceptional figure 73 have no value. Doubtful spellings and names remain graded M; a conservative coherence count excludes whole doubtful segments and the two names in the Polish postscript. It is a lower bound, not a measured error rate.

Every assigned letter is inferred here (I), not read from an original key (H) or an independent known-plaintext copy (C). M marks uncertain readings. No numerical value is assigned to a person code on historical plausibility alone. 100 probably refers to the king, but that remains a contextual suggestion, not a recovered entry.

## Sources and dates

Archiwum Narodowe w Krakowie, Archiwum Sanguszków. Metadata in `R*.json`; source images retrieved through DECODE's record image manager. The full page images and authenticated HTML remain local, excluded from publication. Image suffix P1 etc is an image index, not an asserted archival folio number; some P3/P5/P6 images contain two pages. R7526 has a single spread named `IMG_R7526_I33996_P.jpg`.

| Record | Shelfmark | Date evidence |
|---|---|---|
| R7524 | ASang_teka_290/6 | 1714, metadata and letter heading |
| R7525 | ASang_teka_301/8 | year unknown |
| R7526 | ASang_teka_343/12 | year unknown |
| R7527 | ASang_teka_354/5_1 | Vilna, 7 March 1716, image P1 |
| R7528 | ASang_teka_354/5_2 | 3 August, year absent |
| R7529 | ASang_teka_365/5 | year unknown |
| R7530 | ASang_teka_386/11 | Vilna, 28 March, year absent |
| R7534 | ASang_teka_421/7 | Vilna, 8 January / 30 December 1715, image P2; double date not resolved |
| R7535 | ASang_teka_422/6 | Vilna, 18 January 1716, image P1 |
| R7536 | ASang_teka_422/7 | Vilna, 31 December 1716, image P1; addressed Warsaw on P2 |

The shelfmarks in this table have been checked against the saved metadata. The 1600/1799 dates on some records are catalogue placeholders, not document dates. No blanket replacement with 1714–1716 is justified for the undated items.

Record links: https://de-crypt.org/decrypt-web/RecordsView/7524 through /7530 and /7534 through /7536. Key candidates R7515 (ASang_teka_163/19), R7460 and R7461 (ASang_85/3) were also imaged and inspected.

## Method and work log

1. Retrieved the ten cached metadata records and authenticated source images. R7526 required opening its image manager rather than looking for thumbnails on the record page. Checked blank/address pages and all spreads for additional cipher or decipherment; no contemporary decipherment found.
2. Initial unconstrained French substitution and bijective French annealing over the R7526 postscript failed. The main letter is French, but the postscript is Polish. A Polish monoalphabetic search (`solve_pl.py`, shared `lang/pl-modern`) gave *pan starosta ... iest tu pytalam sie ... do Lublina ... u dominikanow*. This was the break; no outside key or reading preceded it.
3. The resulting alphabet predicted French and Polish names in eight other records. R7535 yielded *fils, saxon, frere, maisson, Oszmiana, Chominski, ensegne, la cour, marszalek, reine, Courlande*. Extra numbers are homophones: 50=e, 52=a, 58=c, 74=r, and similar doubled basic values. Repeated uses of *marchal*, *chancelier*, *Horyhorki*, and *Bychow* verify transfer. R7526 uses 27 for a, where the French passages use 26; 31/32 merge l/ł in the ASCII key. The exact diacritic distinction is not established.
4. Transcribed and revisited the cipher crops. The final all-page audit added 22 passages on the R7527 reverse, corrected *tere* (19, not 29) and the last figure of R7534 *zaia[73]d* (30, not 50), and counted standalone codes. Cancellations are excluded where legible. Source numbers remain unchanged when the literal output is odd. Editorial interpretations are explicitly separated.
5. R7524 has 232 cipher tokens and a different alphabet. Polish quintgram homophonic annealing, tentative *hetmanow* crib, hypothetical null 33/ch=130, and unigram-regularized search yielded no coherent reading. These crib values are NOT recovered key material. A synthetic Polish homophonic control of the same 232-token length and comparable observed alphabet (75 signs) reached only 49/232 correct positions (21.1%); consequently the failed searches are **inconclusive**, not evidence that the historical letter is impossible or even that the assumed design is right. The current solver is inadequate at this length/alphabet ratio. It is left open, with all ciphertext available for a stronger attack.
6. The three key records found in the Sanguszko catalogue were checked: R7515 gives a=5/10/15 and two different alphabet series; R7460/R7461 use graphic signs. None fits. No relevant published decipherment emerged from Polish/French searches for these correspondents, the shelfmarks and cipher terms. Archival catalogue references lead to additional correspondence, but no online scans or same-key plaintext. This is an access limit, not proof of absence.

## What the letters say

- R7525: Horyhorki and court influence: code 94 wants to be alone in the credit of 100; a house causes the writer harm; justice and enemies.
- R7526: the starosta is present; she asked whether he had arranged anything, and he has nothing; a journey to Lublin; a report involving the Dominicans and his staying with a woman. The office/place name reads *serecki* and the reporting name *Tabrowski* in the numerical text; neither is securely identified. Do not silently replace them with Merecki or Dąbrowski.
- R7527: the palatine of Vilna's obligation for *sant mil fran* on Bychow; measures to take and distrust of 94's help. The reverse concerns an accusation against the marshal of Lithuania, Biegański's confession to his father, a letter to 100, a letter through the grand chancellor, and an oath. The allegation is the correspondent's account, not an independently verified event.
- R7528: Rakiszki, the palatine of Mścisław, and property/reformation involving the first husband, Kroszyński. The second surname spelling is irregular (*Krodyznski*).
- R7529: clear French says that since 10 May the *clef* is *rompue* and there is no way to *loubrire*. Another passage says someone has the *clef* in *ceur*. These report trouble using the cipher; they do not establish interception or cryptanalytic compromise. Later cipher words are *rayne* and *maitresse*.
- R7530: the grand treasurer, a confederation, the surrender of an army, and evidence concerning the arrival of a *morcowide* (probably Moscovite). Some number sequences yield corrupt spellings; the letter is not treated as a fluent verified transcript.
- R7534: deputies, *libertation*, a doubtful *zaia[73]d* (possibly Polish *zajazd*), Bychowa, Białystok, Tykocin and Rybiński. Codes 87, 94 and 270 remain open.
- R7535: children and a brother, being Saxon, Dunin's house, Chomiński and an ensign; court correspondence, the marshal and his father, *Menzykw* (possibly Menshikov), the queen and the prince of Courland.
- R7536: a disturbed seal and concern over correspondence; instructions to route letters via a name resembling Königsberg, followed by an unidentified *Kinnik*. The writer expects delay but greater safety. The reverse considers her security, lodging in case of war, keeping Dunin's wife company and a safeguard.

## Prior work and historical context

The target catalogue reported no prior reading on 22 September 2026 and N/A status on all ten records. The session found no independent decipherment; prior-solution existence remains unknown rather than asserted absent. The university project *Women's Court* identifies Barbara née Dunin Potocka (died May 1719) as Jakub Antoni Dunin's aunt, not mother: https://womenscourt.uken.krakow.pl/womencourt/potocka-barbara-z-duninow-zm-v-1719-r-1-v-uniechowska/ . Her *mon fils* is affectionate. This biographical source was found after the key recovery and supplied no cipher values.

The archive catalogue unit 29/637/0/1.3/9477 (former teka 321/8) lists further letters of 1713–1718 but no scans: https://www.szukajwarchiwach.gov.pl/jednostka/-/jednostka/41995540/obiekty/1601530 . It is related correspondence, not a duplicate of a target established here. The Gdańsk manuscript catalogue and Šapoka's article gave further correspondence references, no key or plaintext. No verified portrait of either principal correspondent was found on Commons; namesakes were excluded.

## Remaining gaps
- R7524, all 232 cipher tokens — blocker: no-key-material; separate system, no matching key or plaintext located, current solver also fails its control; not declared impossible.
- Potocka codes 87, 94, 100, 270, 23 occurrences — blocker: open-codes; context suggests roles but does not identify exact entries; no matching nomenclator.
- R7534 exceptional figure 73 in zaia[73]d — blocker: too-short; one occurrence, no independent key, proposed zajazd does not justify assigning a value.
- M-grade names and anomalous sequences in reading.md, especially serecki/Tabrowski, Krodyznski, connedere/morcowide, Keinisberk a Kinnik, tegn and tombap — blocker: illegible; image ambiguities or possible original enciphering/spelling errors, no parallel witness. Literal readings and editorial suggestions remain separate.

## Escalation
- [x] siblings: all ten target records opened; cached Sanguszko records searched for Dunin/Mniszech/Potocka and all three key records inspected; additional archive correspondence has no online scans located.
- [x] clear-pages: all 29 images reviewed including blank/address pages, backs and spreads; clear prose supplies context but no decipherment of the cipher passages.
- [x] known-keys: R7515, R7460, R7461 inspected and ruled out by alphabet/value mismatch.
- [x] print: searches for the correspondents, cipher terms and shelfmarks; university biography, archive catalogue, Gdańsk manuscript catalogue and Šapoka article yielded context but no decipherment.
- [x] key-rebuild: Polish monoalphabetic annealing broke R7526; doubled homophones inferred and checked across eight further letters; separate Mniszech attacks and failed synthetic control documented above.
- [x] retry: every Potocka numeric passage revisited with the extended key, missing reverse passages added, all source pages checked for omitted cipher and standalone codes; unresolved readings retain explicit uncertainty.

## Reproduction and publication

Run `python potocka1714/prepare_reading.py` for readings/counts. Solver files are exploratory and their result files must not be mistaken for accepted plaintext. The shared language-model registry is used without adding a new corpus. Only safe metadata, text, scripts and small source crops are published; authenticated HTML/JWT and full source pages are not. Public DECODE files contain cipher-passage extracts with clear anchors and gaps, not a complete transcription of the letters; updates are queued locally, not sent.

# pandolfini1514: Francesco Pandolfini's letters from the French court, Dec 1514 - Mar 1515, in cipher (ASF Mediceo avanti il Principato LXXII 307, 309, 310, 311, 322, 333)

Status: **one passage read, five letters read in part** (Brice Dudout, 9 Nov 2026; key partial by our held-out tests, P03bis N 0.613 under a lenient threshold, declared; derived keys v4 and v6 declared, not measured). Sure words alone, the rule of #728 (recounted 19 Nov 2026, one basis, see "Recount of 19 Nov 2026" below): 333 28/29 (96.6%; read by the short-text floor, content already given in clear by 332); 307 205/291 (70.4%); 309 59/83 (71.1%); 310 703/1,061 (66.3%; pos. 759 transcribed not blind); 311 424/664 (63.9%; transcription not blind); 322 84/180 (46.7%); all six about 1,503/2,308 (65.1%). Counts approximate where word boundaries are not written. New texts (except 333): no decipherment of the time, no edition.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Lead: catalogue **2389**, found by **Daniel
Bourdeau** (Francesco Pandolfini, Florentine orator in France, six bare cipher letters beside about fifteen cipher/decipherment
pairs of the same system in MAP LXXII). Archive: **Archivio di Stato di Firenze**, Mediceo avanti il Principato, filza LXXII.
No image or derivative is included.

## Document

MAP LXXII **322**, c. 401r (pos. 801): headed in clear "Copia di ij cap.li scripti ad Roma sotto di 20 d'octobre". Three cipher
blocks (6, 2 and 6 lines) between clear passages: the recall of Soliers; "the coming of Rocciafort is awaited by this Majesty";
Alfonso Ariosti's visit for the Duke of Ferrara "per la pace et parentado fatto" (the Anglo-French peace and Louis XII's marriage to
Mary Tudor, 9 Oct 1514), which dates the letter to 1514. Transcription: `transcription_322.txt` (hashed before decoding).

## Documents added on 9 Nov 2026 (second batch)

| Doc | Folio | Date, addressee | Words | Sure alone (#728; with probable words) | Files |
|---|---|---|---|---|---|
| 307 | c. 369r | copy to the Otto di Pratica, 16 Feb 1515 | 291 (205 certain, 57 probable, 29 unresolved) | 70.4% (90%) | `transcription_307.txt`, `reading_307.md`, `translation_307.md` |
| 309 | c. 378r | to Lorenzo de' Medici, 26 Feb 1515 | 83 (59, 16, 8) | 71.1% (90%) | `*_309.*` |
| 310 | cc. 380r-381v | copy to the Otto, 26 Feb - 2 Mar 1515 | 895 units (703, 109, 83 unresolved groups; recounted 19 Nov 2026) | 66.3% (76.5%; 3 words per group) | `*_310.*` |
| 311 | cc. 382r-v | continuation of 310, "Tenuta adi iiij" [4 Mar 1515] | 534 units (424, 44, 1 restored, 65 groups); 664 words at 3 a group | 63.9% (70.5%) | `*_311.*` |
| 333 | c. 417r | to Lorenzo de' Medici, 27 Dec 1514 | 29 (28, 1, 0) | 96.6% (100%): read by the short-text floor | `*_333.*` |

Declared for each piece (and in `reading_<n>.md`):
- **311**: the transcription is NOT blind (doubtful shapes were settled while reading); lines B15-B16 of 382v are nearly illegible.
- **310**: three reservations: pos. 759 was transcribed by the agent that knew the key (NOT blind; pos. 760-762 by three agents that saw neither key nor reading); codes .22. (probably *lanzichenech*, from the clear 316), 20./23. and .uij. not resolved; blocks C-E need re-reading on HD images. "Ghiscia" = Pierre de La Guiche, confirmed by *Letters and Papers, Henry VIII*, vol. 2 (Francis I to Henry VIII, 21 Feb [1515]) and The National Archives E 30/754 and E 30/927. 316 (c. 388r, clear) was re-read: it is the clear of 315 (14 Mar), with shared themes only, not the clear of 310.
- **333**: every word read, but the content is NOT new: 332 (c. 416), the clear copy of the letter to the Otto of the same day, gives the same news with shared words ("dalle bande di qua", "grandissima suspitione"). A new reading of the cipher, not new history.
- **309**: Louise of Savoy's offer of a marriage of Louise Borgia (daughter of the Duke of Valentinois) for Lorenzo: a Borgia match for Lorenzo is mentioned in the literature, but this offer of Feb 1515 is still to be checked in the printed sources; nothing is claimed beyond the text.

The original transcriptions (French notes, hashed before decoding) and the full French working notes are in `frozen/` (N307..N333 with their .sha256, LECTURE_307..333.md).

## The system and the key

Consonant signs carry the vowel as a superscript figure (1-5 = u, o, i, e, a); bare vowel signs, homophones, word signs (F = et,
M = non, T = senza) and a nomenclator between points (.2. papa, .4. Cristianissimo, .5. Cattolico, .6. Inghilterra, .20. Svizzeri,
.24. Milano, .26. Arciduca). `key_v3.json` was learnt from the pairs of the time 345/346 and 340/341 and frozen. `key_v4.json` adds
values derived after the last measurement (2^4 = ce, bare 2 = o, .3. = imperadore, .64. = Santità; alternatives bare 5 = h,
2^5 = ca), each with its attestations: declared, **not measured**.

### Key v6 (`key_v6.json`): declared merge, not measured

Two agents reading 307/309 and 311/333 derived two keys from v4 (`frozen/CLE_v5a.json` 16a6d2de..., `frozen/CLE_v5b.json` 9d5cf3d5...). They disagreed on two signs. `key_v6.json` (SHA256 a2f1c942..., `frozen/CLE_v6.sha256`, built by `frozen/build_cle_v6.py`, which checks the hashes of v4, v5a and v5b and admits only the two conflicts) is their union with a declared arbitration (`frozen/ARBITRAGE-v6.md`, in French):
- **α = per** (not *et*): α is the sign written "P" in the earlier transcriptions; 13 clears of the time (345/346, 340/341, 342/343) read *per*; of its 25 occurrences in the bare letters, 19 allow only *per* (three inside words: per-sonaggio twice, sa-per-e), 2 are neutral, 2 unread, and one (307 L16) would read better as *et* without requiring it, left unresolved. No homophony: *et* has its own sign (F).
- **4# = ll** (333 against the clear 332, "dalle bande di qua"; 21 occurrences, *gg* gives no word) and **G# = gg** (309 "veggia", one occurrence: probable): two distinct signs, of different shapes.
- Sign 2 = c by default, b by sense in the reading only; 0 = c (spelling "ct": tucto, mactina); the v5b rule "0 before 8 = t" was not kept (it changes spellings, not words).
v6 was frozen at 03:42 CET, before the final readings of 307/309/311/333 and before the transcription of 310. No value outside the arbitration. Declared, **not measured**: the key status stays partial.

## Validation (`validation.txt`)

Three held-out measurements, protocols hashed first: P01 346/345 0.788 (control 0.338) and P02 340/341 0.691 (control 0.341),
both under 0.85: not validated; P03bis on 342 c. 433r (Italian n-gram criterion calibrated in advance): N = 0.613 between the
partial (0.004) and validated (0.765) thresholds: **partial**. The partial threshold is lenient and the criterion is more lenient
than character agreement (declared). The ceiling is the resolution of the images.

## Reading (`reading_322.md`, `translation_322.md`)

Block 1 about 74 words (41 certain, 27 probable, 6 unresolved, about 92%); block 2 about 24 (9, 4, 11, about 54%); block 3 about
70 (30, 18, 22, about 69%). Overall about 77% with probable words, 0 restored: read in part. Recounted 19 Nov 2026 from the marks of `reading_322.md` (the block counts above are the first, approximate count): 146 units, 84 certain, 45 probable, 17 unresolved groups; at 3 words a group 180 words, 46.7% sure alone (#728). Content: once Rocciafort arrives the King will send an
ambassador to Rome, believed to be the bishop of "Lancres" (see not identified), empowered to negotiate everything with the Pope;
the informant (code .51.) expects the same quarrel as the Pope's with the bishop of Marseille; after Ariosti's visit the King asked
that the Venetian ambassador be approached so that Venice give back Monselice, Este and Montagnana to the Este.

## Prior work (re-checked 9 Nov 2026)

Second batch: the clear copies 284, 306, 313, 315-317, 332, 337, 344, 347, 350, 365-366, 368 and 419 were checked by date and content; none is the clear of 307, 309, 310 or 311 (365, an extract of 20 Mar "tratto di cifra", corroborates the Suffolk - Mary Tudor rumour of 311); 332 parallels 333.


No decipherment of the time (Daniel's vetting of 6 Nov 2026 of the untitled clear copies; neighbours pos. 797-804 checked: 319
cipher, 320 blank, 321 and 403 clear on other matters). Desjardins and Canestrini, *Négociations diplomatiques de la France avec
la Toscane*, vol. II (1861): gap from 16 Aug 1514 to 25 May 1515. Catalogue 2389 open; no target, PR or issue on it here.

## Remaining gaps

- 307: 29 words unresolved (block 3, end of block 2, α at L16) - blocker: open-codes
- 309: 8 words unresolved (code .48., end of block B) - blocker: open-codes
- 310: 83 unresolved groups (codes .22., 20./23., .uij.; blocks C-E) - blocker: open-codes; HD re-reading wanted
- 311: 65 unresolved groups (codes .16., .17.; signs F^n, E, P, J; lines B15-B16) - blocker: open-codes; transcription not blind
- 322: 17 unresolved groups, about 51 cipher words at 3 a group (code .51., marks T^n, T^x, L^c, and runs of blocks 2 and 3) - blocker: open-codes; the codes are not in the key and HD images would settle the shifted superscripts and δ/d

## Escalation

- [x] siblings: the pairs of the time 345/346, 340/341 and 342/343 in the same filza gave the key and three held-out tests
- [x] clear-pages: neighbours of 322 (pos. 797-804) and the untitled clear copies checked; no decipherment of 322
- [n/a] known-keys: no key sheet of this system is known; the pairs are the key material
- [x] print: Desjardins-Canestrini vol. II checked (gap Aug 1514 - May 1515)
- [x] key-rebuild: key v4 derived from 342/343 and the reading, key v6 merged from v5a/v5b by a declared arbitration; neither measured
- [n/a] retry: a further measurement waits for HD images (the resolution is the ceiling)

All six bare letters of 2389 are now read in part or read. No ASF image or derivative is included.

## 19 Nov 2026: sign checks and corrections (sheets W, X2, x3, x4)

Level: AI decipherment, human-checked on a sample of signs. Brice Dudout chose the shape of boxed signs on blind sheets
(reference shapes cut from the same letters, no value shown, two controls per sheet). The sheets were prepared by AI agents.
Sheets, rules and answers are not in the repository, and no image or derivative is included.

- **310, transcription corrected** (sheet W, controls 2/2). The sign transcribed S is a 5 in B1 (domandono), C1 (ultimamente)
  and C3 (mandato, simil): four tokens changed in `transcription_310.txt`, and the original stays in `frozen/`.
  - Checked and kept: the S^2 of monstrono, and the t before 7^5 in "fra" (A9, C1, H1). Those gaps come from the key or the hand.
- **J# = ss, probable.** "di J# e" (310 A8, D8): the J# is a long s crossed by two bars, and # marks doubling in this cipher.
  Both groups now read {disse}. This value is by analogy and is not added to key v6. On sheet W the checker answered
  "none / other shape" for both signs (the options were r, 6 and J) and wrote "an f with two bars": the two tokens are now
  `J#` in `transcription_310.txt` (A8 J? -> J#, D8 J -> J#), recoded from that remark; the original stays in `frozen/`.
- **310 recounted** from the marks of `reading_310.md`: 895 units, 703 certain, 109 probable, 83 unresolved groups (main: 701,
  109, 85; two words became certain, two groups became probable). Counting 3 words per group, 1,061 words: 66.3% sure alone
  (the read share, README rule) and 76.5% with the probable words. Still read in part.
- **Sign 2: proposal v6b** (`KEY_V6B_PROPOSAL.md`, `key_v6b_proposal.json`, `sign2_forms.tsv`): flat 2 = b, looped ʒ = c,
  bare ʒ = o. On the three sheets that count, c-words were seen ʒ 24 times in 25 (exception: ricercare, 311 A7) and b-words flat
  4 times in 4. key_v6.json is unchanged. Neither v6 nor v6b has been measured.

### Sign-check record (held here until #789)

The sheet record was first filed as `outcome.human_check`; it is withdrawn from `profile.json` because the schema defines
`human_check` as a check without AI help, and these sheets were prepared by AI agents. It will go into `outcome.sign_check`
once #789 (which adds that field) is merged. Until then the record is kept here, and `sign_check_pending.json` holds the
entries in the #789 format; no schema field refers to that file yet.

- Checker: Brice Dudout (project). A model wrote the selection rules, cut the thumbnails, built the sheets, scored the answers
  and interpreted the free-text remarks; the choices are his alone. Answers given 18-19 Nov 2026.
- **W** (310; rule written 18 Nov 2026 before the sheet, SHA-256 3a7d52ac...): 10 signs and 2 controls (2/2). As transcribed
  4 (S^2 of monstrono; t of "fra" in A9, C1, H1); corrected 4 (S -> 5 in B1, C1, C3 x2); "none / other shape" 2 (the J of
  "di J e" in A8 and D8, remark "an f with two bars", recoded J#).
- **x3** (311, 322; rule SHA-256 d1261351...): 7 signs of 1514 and 2 controls (2/2), with 2 signs of pandolfini1515 on the
  same sheet. All 7 are the looped ʒ expected for c.
- **x4** (307, 310, 311, 322, 333; rule SHA-256 f7888348...): 15 signs of 1514 and 2 controls (2/2), with 1 sign of
  pandolfini1515. c-words: 9 looped ʒ, 1 flat 2 (ricercare, 311 A7), 1 "none / other shape" (costì, 333 L2, remark "Z",
  read as ʒ); b-words: 4 flat 2. No token changed.
- Sheets, rules and answers are not in the repository; no image or derivative included.

## Recount of 19 Nov 2026: one basis for all six letters (#728)

`fraction_read` and its source sentence mixed two bases (310 as sure words alone, the five others with probable words). All six
are now counted on one basis, the rule of #728: sure words alone over cipher words; probable, restored, inferred and unresolved
words (and codes with no value) count as holes; 95% per document. Counts from the marks of each `reading_<n>.md`
(plain = certain, {x} probable, [x] restored, ‹…› unresolved). Where a reading counts unresolved groups (310, 311, 322), a group
counts as 3 words, as for 310.

| Doc | Cipher words | Sure | Holes | Sure alone | Class |
|---|---|---|---|---|---|
| 322 | 180 (84 + 45 probable + 17 groups x 3) | 84 | 96 | 46.7% | read in part |
| 307 | 291 (205 + 57 + 29) | 205 | 86 | 70.4% | read in part |
| 309 | 83 (59 + 16 + 8) | 59 | 24 | 71.1% | read in part |
| 310 | 1,061 (703 + 109 + 83 groups x 3) | 703 | 358 | 66.3% | read in part |
| 311 | 664 (424 + 44 + 1 restored + 65 groups x 3) | 424 | 240 | 63.9% | read in part |
| 333 | 29 (28 + 1) | 28 | 1 | 96.6% | read (short-text floor) |
| all | 2,308 | 1,503 | 805 | 65.1% | |

- **333** has fewer than 40 cipher words and 1 hole (the probable word), so it is "read" by the short-text floor (under 40 cipher
  words and at most 2 holes). The floor serves only here; it is never applied at 40 words or more. At 96.6% it would also pass 95%.
- **307 and 309** count each unresolved place as one word, as their status lines do. Counted at 3 words a place, as for 310, they
  would be 205/349 (58.7%) and 59/99 (59.6%), and the total 1,503/2,382 (63.1%). The class does not change.
- **322**: the first count (about 168 words, 80 certain, 49 probable, about 39 unresolved) was approximate; the marks of
  `reading_322.md` give 84, 45 and 17 groups. **311**: the marks give the status line (424, 44, 1, 65 groups); the restored [24]
  is written in clear inside the cipher and counts as a hole.
- `fraction_read` is now 0.651 (was 0.8). Each `read_share` is the sure-alone share; the per-document classes are unchanged.

The checker of every sheet is the author of the PR; the label claims nothing about the key.

Under the floor of #789 (at least 8 target signs per sheet; sheets are not added together): W has 10 signs of 1514 and x4 has 15,
both above it; x3 has 7 signs of 1514, one under it.

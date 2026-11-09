# pandolfini1514: Francesco Pandolfini's letters from the French court, Dec 1514 - Mar 1515, in cipher (ASF Mediceo avanti il Principato LXXII 307, 309, 310, 311, 322, 333)

Status: **one passage read, five letters read in part** (Brice Dudout, 9 Nov 2026; key partial by our held-out tests, P03bis N 0.613 under a lenient threshold, declared; derived keys v4 and v6 declared, not measured). 333: 29 words, 100% (content already given in clear by 332). 307: 90%. 309: 90%. 311: about 80-85% (transcription not blind). 310: about 75% (pos. 759 transcribed not blind). 322: about 77%. Counts approximate where word boundaries are not written. New texts (except 333): no decipherment of the time, no edition.

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

| Doc | Folio | Date, addressee | Words | Read by sense | Files |
|---|---|---|---|---|---|
| 307 | c. 369r | copy to the Otto di Pratica, 16 Feb 1515 | 291 (205 certain, 57 probable, 29 unresolved) | 90% | `transcription_307.txt`, `reading_307.md`, `translation_307.md` |
| 309 | c. 378r | to Lorenzo de' Medici, 26 Feb 1515 | 83 (59, 16, 8) | 90% | `*_309.*` |
| 310 | cc. 380r-381v | copy to the Otto, 26 Feb - 2 Mar 1515 | about 895 units (701, 109, 85 unresolved groups) | about 75% | `*_310.*` |
| 311 | cc. 382r-v | continuation of 310, "Tenuta adi iiij" [4 Mar 1515] | about 534 units (424, 44, 1 restored, 65 groups) | about 80-85% | `*_311.*` |
| 333 | c. 417r | to Lorenzo de' Medici, 27 Dec 1514 | 29 (28, 1, 0) | 100% | `*_333.*` |

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
70 (30, 18, 22, about 69%). Overall about 77%, 0 restored: read in part. Content: once Rocciafort arrives the King will send an
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
- 310: 85 unresolved groups (codes .22., 20./23., .uij.; blocks C-E) - blocker: open-codes; HD re-reading wanted
- 311: 65 unresolved groups (codes .16., .17.; signs F^n, E, P, J; lines B15-B16) - blocker: open-codes; transcription not blind
- 322: about 39 cipher words unresolved (code .51., marks T^n, T^x, L^c, and runs of blocks 2 and 3) - blocker: open-codes; the codes are not in the key and HD images would settle the shifted superscripts and δ/d

## Escalation

- [x] siblings: the pairs of the time 345/346, 340/341 and 342/343 in the same filza gave the key and three held-out tests
- [x] clear-pages: neighbours of 322 (pos. 797-804) and the untitled clear copies checked; no decipherment of 322
- [n/a] known-keys: no key sheet of this system is known; the pairs are the key material
- [x] print: Desjardins-Canestrini vol. II checked (gap Aug 1514 - May 1515)
- [x] key-rebuild: key v4 derived from 342/343 and the reading, key v6 merged from v5a/v5b by a declared arbitration; neither measured
- [n/a] retry: a further measurement waits for HD images (the resolution is the ceiling)

All six bare letters of 2389 are now read in part or read. No ASF image or derivative is included.

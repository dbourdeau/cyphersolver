# pandolfini1514: Florentines at the court of Louis XII, copy of two chapters written to Rome, 20 October [1514], in cipher (ASF Mediceo avanti il Principato LXXII 322)

Status: read in part (Brice Dudout, 9 Nov 2026; about 168 cipher words, about 77% read by sense, block 1 about 92%, 0 restored; counts approximate because word boundaries are not written; key partial by our held-out tests, P03bis N 0.613 under a lenient threshold, declared). New text: no decipherment of the time, no edition.

Contributed by Brice Dudout (L'Europe chiffrée), with Claude Opus 5.5 agents. Lead: catalogue **2389**, found by **Daniel
Bourdeau** (Francesco Pandolfini, Florentine orator in France, six bare cipher letters beside about fifteen cipher/decipherment
pairs of the same system in MAP LXXII). Archive: **Archivio di Stato di Firenze**, Mediceo avanti il Principato, filza LXXII.
No image or derivative is included.

## Document

MAP LXXII **322**, c. 401r (pos. 801): headed in clear "Copia di ij cap.li scripti ad Roma sotto di 20 d'octobre". Three cipher
blocks (6, 2 and 6 lines) between clear passages: the recall of Soliers; "the coming of Rocciafort is awaited by this Majesty";
Alfonso Ariosti's visit for the Duke of Ferrara "per la pace et parentado fatto" (the Anglo-French peace and Louis XII's marriage to
Mary Tudor, 9 Oct 1514), which dates the letter to 1514. Transcription: `transcription_322.txt` (hashed before decoding).

## The system and the key

Consonant signs carry the vowel as a superscript figure (1-5 = u, o, i, e, a); bare vowel signs, homophones, word signs (F = et,
M = non, T = senza) and a nomenclator between points (.2. papa, .4. Cristianissimo, .5. Cattolico, .6. Inghilterra, .20. Svizzeri,
.24. Milano, .26. Arciduca). `key_v3.json` was learnt from the pairs of the time 345/346 and 340/341 and frozen. `key_v4.json` adds
values derived after the last measurement (2^4 = ce, bare 2 = o, .3. = imperadore, .64. = Santità; alternatives bare 5 = h,
2^5 = ca), each with its attestations: declared, **not measured**.

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

No decipherment of the time (Daniel's vetting of 6 Nov 2026 of the untitled clear copies; neighbours pos. 797-804 checked: 319
cipher, 320 blank, 321 and 403 clear on other matters). Desjardins and Canestrini, *Négociations diplomatiques de la France avec
la Toscane*, vol. II (1861): gap from 16 Aug 1514 to 25 May 1515. Catalogue 2389 open; no target, PR or issue on it here.

## Remaining gaps

- 322: about 39 cipher words unresolved (code .51., marks T^n, T^x, L^c, and runs of blocks 2 and 3) - blocker: open-codes; the codes are not in the key and HD images would settle the shifted superscripts and δ/d

## Escalation

- [x] siblings: the pairs of the time 345/346, 340/341 and 342/343 in the same filza gave the key and three held-out tests
- [x] clear-pages: neighbours of 322 (pos. 797-804) and the untitled clear copies checked; no decipherment of 322
- [n/a] known-keys: no key sheet of this system is known; the pairs are the key material
- [x] print: Desjardins-Canestrini vol. II checked (gap Aug 1514 - May 1515)
- [x] key-rebuild: key v4 derived from 342/343 and the reading, declared and not measured
- [n/a] retry: a further measurement waits for HD images (the resolution is the ceiling)

The other bare letters of 2389 (307, 309, 310, 311, 333) are being read and will be added here.

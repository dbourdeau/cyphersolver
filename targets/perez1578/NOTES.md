# Pérez 1578: Antonio Pérez to Don John of Austria, Madrid, 19 August 1578 (RAH 2/Ms Caja 8 no. 4), four cipher passages

Status: read (Brice Dudout, 29 Oct 2026; 69 of 70 words read in their sense, 60 certain, 9 probable, 0 restored, 1 unresolved; Daniel Bourdeau's 95% rule).

Contributed by Brice Dudout (Europe chiffrée), 29 Oct 2026. Write-up (to be published when the account is restored):
https://bdudout.github.io/europe-chiffree/en/documents.html#perez-1578
Not in the catalogue; found in the digital library of the Real Academia de la Historia (Fernández San Román collection).

## Document

Real Academia de la Historia (Madrid), Library, 2/Ms Caja 8 nº 4 (Fernández San Román collection), images 2–3.
19 August 1578 (filing date “Ag.to 19. de 1578”); autograph. Madrid → the Netherlands.
Sender: Antonio Pérez, Secretary of State to Philip II. Recipient: Don John of Austria, governor general of the Netherlands.
Images: https://bibliotecadigital.rah.es/es/catalogo_imagenes/grupo.do?path=1000503 (Public Domain Mark 1.0, credit Real Academia de la Historia, Biblioteca Digital). Not copied here.

August 1578. Don John of Austria, half-brother of Philip II and governor of the Netherlands, is in the field against the States General and asking for money. Antonio Pérez, Secretary of State, answers him from Madrid in his own hand, after the arrival of Don John’s envoy, Don Alonso de Sotomayor. Four passages are in cipher. They say that the Council of Finance has “not a single real”, that providing what is needed is “impossible”, and that the asiento just made will not be followed by another. Don John died six weeks later, on 1 October; Pérez was arrested in July 1579 for the murder of Escobedo, Don John’s secretary.

## System and key

numerical syllabary of the Spanish chancery of 1577, a variant of the table of the Genoa embassy: number = consonant (6 d, 7 c, 15 l, 16 m, 17 n, 20 p, 22 r, 23 s, 24 t…), mark after the number = vowel (+ a, . e, 6 i, hook o, ı u), single numbers 10 a, 4 e, 18 o, 1 u, superscripts ^ n, ¯ s, ˇ r, ′ l. In Pérez’s hand 8 is g (b in the Genoa table) and “8 with a small 2” is ble.

`key.tsv` (K_P2) = our key for the 1577 Genoa embassy cipher (rebuilt on cipher / "descifrada" pairs of AGS Estado 1410,
validated on 1410,78-79: 87.3% words / 95.5% chars), plus four values learnt on Pérez's own exploration lines
(9 = g, 8 = g, X = r, i-stroke = u) and 27 = x (learnt after the 1410,69-70 measurement).

## Validation

1. A lexical-coverage test on held-out lines did not separate the key from its controls (a syllabary yields words even
   when shuffled): declared inconclusive.
2. Pair AGS Estado 1410,69-70 (4 Aug 1577), cipher frozen before the contemporary decipherment was opened: 72.4% words /
   88.5% chars, 200 controls <= 25.3 / 55.7: significant but under the 75% word threshold -> not validated.
3. Decisive: fresh pair AGS Estado 1410,65-66 (Genoa, 19 Jul 1577; PARES 3576652), key K_P2 frozen (SHA-256 4d5eb01d...),
   twelve cipher lines transcribed in two passes and frozen before the "descifrada" was opened; words containing 8
   (b in the Genoa table, g in Pérez's hand) excluded by a rule written in advance. Result: 81.3% words / 87.9% chars;
   200 controls (100 permuted consonant values + 100 shuffled unit orders) at most 16.5% / 47.8%. Criterion
   (>= 0.75 words, >= 0.85 chars, above every control): met.

## Reading

First published decipherment, to our knowledge: no edition found in Mignet (1845), in the CODOIN or in recent work on the San Román collection; Gregorio Marañón’s Antonio Pérez (1947), with its documentary appendices, could not be checked. Rule applied: Daniel Bourdeau’s, 95% of the words read from the sense. Cipher part: 70 words; certain 60 (85.7%), probable {x} 9 (12.9%), restored [x] 0, unresolved ‹…› 1 (1.4%); read from the sense: 69/70 = 98.6%.

Files: `transcription.txt`, `decryption.txt`, `reading.md`, `translation.md`, `key.tsv`.

## Notes

- The cipher. It is neither Pérez’s cipher with Vargas Mexía (1578–1579) nor the “general cipher” of Don John and Escobedo (1576–1577): it is the numerical syllabary found in 1577 in the dispatches of the Spanish embassy at Genoa (Simancas, Estado, leg. 1410), with departures peculiar to Pérez. A draft of 4 February 1577 (Estado 1410,196) announces to the ministers in Italy the change of the “cifra general”; it does not contain the table.
- {ir}. The first sign of the second passage is blotted; the 2 (= i) and the superscript ˇ (= r) can be seen. We keep “ir acomodado”, as the cipher spells it.
- {estrecho}, {dicho}: “7 + hook”. A barred 7 followed by a hook stands for cho both times, as the words require; the sign is not attested elsewhere.
- {imposible}: sign 14. “por 14 16 po si 8²”: 16 = m, 8² = ble, so 14 is i here (in the Genoa table, 14 = gu). A single occurrence: probable reading.
- {cunplira}. The 7ı carries an oblique superscript stroke, which we read as ^ (= n); “no se cunplira” is required by “con protesto de que”.
- ‹ningun›. The signs give u-cin-gan (or nin-gan if 1 and 7 form 17). “ningun otro” is expected, but gan contradicts the u: we leave the word unresolved.
- {estragar}. The letters s-t-ra-ga-r are certain (8 = g in Pérez’s hand); the exact sense of the verb in the sentence remains uncertain.
- Prior work. Checked: Daniel Bourdeau’s cyphersolver repository, Cryptoole/Cryptiana (S. Tomokiyo), F. Mignet (1845), the CODOIN (full text, Internet Archive), P. Ávila Seoane (Vegueta, 2024, on Don John’s autographs in the same collection). Not checked: G. Marañón, Antonio Pérez (1947), whose appendices print many of Pérez’s letters; if the letter is edited there, the present reading becomes an independent check of it.

# delcarretto1576: Alfonso II del Carretto, marquis of Finale, to his agents in Milan, Regensburg, 2 Sep 1576 (catalogue 2164)

Status: read (Brice Dudout, 6 Nov 2026; 174 of 182 cipher words read by sense = 95.6% without restorations, 96.7% with them; the 6 unresolved words are in the torn margin; key validated by our pre-registered test, 0.961 vs 0.263).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **2164** ("Lettera parzialmente
cifrata", no decipherment noted). No decipherment of the time on the leaf; no edition found (see profile.json).

## Document

Modena, Biblioteca Estense Universitaria, Autografoteca Campori, Lettera D, Del Carretto, Alfonso II (sec. XVI), c. 10
(Lodovico Media Library, uuid ca09c927-df47-423e-adbb-dc4fdac1a851). Regensburg, 2 Sep 1576, signed "il principe
marchese del Final"; addressed on c. 10v "Alli Nobili Agenti nri car.mi Lodovico Allaria et Paolo Fenocchio — Milano".
The upper part of c. 10r is 11 cipher lines (L01-L11) with a torn left margin note (M1-M5) and one interlinear insertion;
the rest of the letter is in clear. The neighbouring c. 9 (Vienna, 6 Nov 1574, same agents) is in clear and mentions
letters "in ziffra". The IIIF manifest states no licence: the images were used for study only and none is included here.

## System and key (`key.tsv`)

A substitution of Italian with homophones for the vowels (a = D, m; e = G, O, t, l; o = C, i and the groups oρ / oρo;
i = u, n; u = 7 and ρ with a heavy dot), word division kept, and Latin, Greek-like and digit shapes for the consonants
(h = 4, d = ʒ, f = d, q = barred q, c = q, b = c, p = b, r = e, s = a, t = x, n = k, m = h, g = r, l = ρ, p). An isolated
o is a null. No nomenclator was seen.

The key K_T was broken on lines L01-L08 alone by simulated annealing (4-gram model of 16th-century Italian from other
texts; six seeds identical), with one correction by sense on those lines (d = f), and frozen before L09-L11 were decoded.

## Validation (`validation.txt`)

Held-out lines L09-L11 (54 words), fixed before any calculation. The reference is an independent, fully automatic break
of those three lines alone, frozen before they were decoded with K_T (convergence 0.887 >= 0.60). One measurement:
**character agreement 0.961 against 0.263 for the best of 200 shuffled keys** (thresholds >= 0.85 and >= control + 0.30,
fixed in advance): **validated**. Word agreement 0.852 (not decisive). Reservations: the reference is a machine break,
not a clear text of the time; one held-out word was seen while justifying the tokenisation; the transcription is a
single pass.

## Reading (`reading.md`, `translation.md`)

182 cipher words (block 174, margin 8): 149 certain, 25 probable, 2 restored, 6 unresolved (all in the torn margin).
**174/182 = 95.6% read by sense** (Daniel's rule, restored words not counted): **read**. The probable words depart from
the key by one sign each; several are probably slips of our single-pass transcription (a blind second reading of those
signs has not been done), and "harbbian" (twice, for habbian) looks like a habit of the encipherer.

Content: Beccaria has said that no one could carry out His Majesty's orders better than Count Espinula (Spinola); the
marquis has not failed and will not fail to make the truth known, for the agents' honour and His Majesty's service,
although it is awkward that the man was approved and sent to His Majesty as trustworthy; let the agents do their duty
on their side, for the man is better known to His Majesty and his ministers than is believed, and neither he nor the one
behind him will reach his aim. Beccaria, Signor Pietro and the man in question are not identified.

## Remaining gaps

- 6 margin words lost or cut by the tear (M1, M2, M4, M5) - blocker: needs-physical-access; the left edge of c. 10r is torn and only the line ends survive
- 25 probable words that depart from the key by one sign (D/G, ʒ/ɔ, e/c, ρo/u) - blocker: illegible; a blind second reading of the doubtful signs on the full-resolution tiles would settle whether they are our slips or the encipherer's

Not gaps of this reading (scope): the clear part of the letter is not transcribed here; the persons named in the cipher
(Beccaria, Spinola, Signor Pietro) are not identified.

## Escalation

- [x] siblings: c. 9 (Vienna 1574, same agents) is in clear; cc. 1-8 (letters to the Gonzaga, 1559-65) show no cipher; no other piece in this cipher found online
- [x] clear-pages: no decipherment or clear copy on c. 10r-v or its neighbours
- [x] known-keys: catalogue 'Del Carretto' hits are Ottone del Carretto (Milan, 1520s), another system; alfonso1576 is Alfonso II d'Este, another system
- [x] print: two web searches (4 Nov 2026) found no edition; Cavagna 2012 (La biblioteca di Alfonso II Del Carretto) and the agents' papers in Genoa or Milan were not checked
- [x] key-rebuild: key broken ciphertext-only on L01-L08, frozen, validated once on L09-L11 against an independent machine break
- [n/a] retry: the whole cipher block is read with the frozen key; only the torn margin is left, which no key can restore

## Files

| file | content |
|---|---|
| `transcription.txt` | cipher lines L01-L11 and margin M1-M5, one character per sign shape |
| `key.tsv` | the frozen key K_T, CC BY 4.0 |
| `decryption.txt` | mechanical decryption with K_T, no correction |
| `reading.md` | the reading (Italian, spelling of the letter), marks, count, word-by-word notes |
| `translation.md` | English translation |
| `validation.txt` | protocol order, the single measurement and its reservations |

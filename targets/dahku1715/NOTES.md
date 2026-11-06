# dahku1715: Dahku (signed "Dahka"), Cracow 1715, sign cipher in a Polish letter (AGAD 1/338/0/1/682)

Status: read in part (Brice Dudout, 6 Nov 2026; 53 of 63 cipher words read by sense = 84%, no restorations; key partial by our protocol, M5 0.444 vs 0.083 on held-out lines).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry **1581** (open, "Część listu
pisana szyfrem, nierozwiązanym"). No prior decipherment found (see profile.json, conditions.prior_solution).

## Document

AGAD Warsaw, fonds 338 (Zbiór Anny z Potockich Branickiej), unit 1/338/0/1/682, five scans
(szukajwarchiwach.gov.pl, unit 28224391). A letter signed "Dahka" from Cracow; p. 1, the address and the end are in clear
Polish; only scan 3 (pp. 2-3) carries cipher: 17 lines of graphic signs with clear Polish words among them. No gloss, key
or clear copy is on the scans. The unit card gives "1715, IX, 21", and the cipher speaks of 9 October as still to come, so
the letter is probably of 21 Sep 1715 (our first sorting note said 21 May). No image is included here.

## System and key (`key.tsv`)

A letter-for-letter substitution of Polish with 24 graphic signs and a few homophones (a = + / P, z = W / N, y = z / l,
w = b / C). A framed sign (N, twice) and a tied sign (C, once) decode as single letters but stand where names are
expected: probably nomenclator names, left unresolved. Word breaks follow the manuscript.

The key was broken on the cipher alone (no crib, no clear copy): simulated annealing on the 278 signs of lines d01-e02,
with a Polish 4-gram model learnt from the Deboli clear texts of this repository (targets/deboli1788-1791). All eight
restarts gave the same Polish text. The raw key was frozen before the held-out lines were decoded.

## Validation (`validation.txt`)

Held-out block e03-e06 (72 signs), chosen before any attack. One measurement: **M5 = 0.444** (share of decoded signs in
Polish words of five letters or more) against **0.083** for the best of 200 shuffled keys; margin 0.361. Our thresholds,
fixed in advance: validated if M5 >= 0.60 and >= control + 0.30. **Partial by our protocol.** There is no clear text of
the time to compare with, and the block is short.

After the measurement, a blind shape plate on the barred sign V (Brice Dudout, 3 questions including 1 control) found the
shape of W at d05 and e05; the reading uses z there. The frozen key and the score are unchanged.

## Reading (`reading.md`, `translation.md`)

63 cipher words: 39 certain, 14 probable, 0 restored, 10 unresolved: **84.1% read by sense, under 95%: read in part.**
The passage reports that the Sandomierz deputies asked for the Crown army to support the levée en masse of the Sandomierz
voivodeship, set for 9 October, and not to be moved away from Sandomierz; the answer was that no commitment could be made
before the Primate's resolution was known; it was only declared that the army would not be withdrawn but taken across the
Vistula. Autumn 1715, the run-up to the Confederation of Tarnogród. The addressee and the person behind N are not
identified.

## Remaining gaps

- 7 cipher words unresolved as letters: "zto", "e", "kostalacio" (d02), "kodzarzyc" (e05, a place name expected), "nadra", "zo", "a" (e05-e06; perhaps "na drugą stronę", not given by the letters) - blocker: open-codes; the key is partial and these stretches do not construe
- the framed sign N (twice) and the tied sign C (once), probably names (the subject of "chciał assistere"; a title before "prymas") - blocker: open-codes; no nomenclator for this cipher is known and the letter has only one cipher passage
- e05 last word read on the reduced view at the page edge - blocker: illegible; a full-resolution look at the right margin of p. 3 would settle it
- the key cannot be tested again on this letter (held-out lines used up) - blocker: no-key-material; another letter in the same signs is needed

Not gaps of this reading (scope): the clear parts of the letter (p. 1, address, end) are not transcribed here; the date line
of p. 1 was not re-read; the addressee is not identified.

## Escalation

- [x] siblings: the other scans of unit 1/338/0/1/682 were sorted (only scan 3 is in cipher); catalogue 1583 (Beck 1757) and 1593 (Forbes) of the same sweep are other systems (1583 failed with key 1196; 1593 failed)
- [x] clear-pages: no clear copy or gloss on the five scans; none known elsewhere
- [x] known-keys: AGAD 1/338/0/1/1196 ("Pour déchiffrer", Branicki circle) is a French numeric nomenclator, not this sign cipher; no other key of the fonds is known to us
- [x] print: web searches on Dahku / Cracow 1715 and the Branicki papers found no edition of this passage (3-5 Nov 2026); known.py, DECODE, Tomokiyo and Lasry: nothing
- [x] key-rebuild: key broken ciphertext-only by annealing on the training lines, frozen, measured once (partial); one sign (V) settled afterwards on a blind shape plate, for the reading only
- [n/a] retry: the held-out lines are used up and no second text in this cipher is known, so no second decode with an extended key was made

## Files

| file | content |
|---|---|
| `transcription.txt` | the 17 cipher lines, one ASCII letter per sign shape, clear words as =word |
| `key.tsv` | the frozen key (24 signs -> 20 letters), CC BY 4.0 |
| `decryption.txt` | mechanical decryption with the frozen key, no correction |
| `reading.md` | the reading, line by line and as running text, with marks and the count |
| `translation.md` | English translation |
| `validation.txt` | protocol order, the single measurement, limits |

## Next step

Another letter of Dahku (or of the same Branicki correspondence) in the same signs would allow a second test of the key
and the identification of N and C.

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

## Decrypt audit, 16 Nov 2026

`research/decrypt_audit` flagged this target: 18 of 63 words depart (29%), one text compared (the running text of
`reading.md`). The flag is almost entirely an artefact; one clear word differs between the files.

- Check by hand: `key.tsv` (24 signs) applied to the 350 signs of `transcription.txt` reproduces `decryption.txt`
  exactly. All 39 words given as certain in `reading.md` have the letters of the decryption (diacritics apart).
- Audit artefact and clear words, 13 of the 18: the audit put the clear words of the letter (`=aby`, `=ktore`, `=zeby`,
  `=ze`, `=deklarowac`, `=y`, `=tym`, `=potewaz`, `=iaky`, `=domey`, `=posl`/`=nym`, `=tylko`, `=prosto`) through the key
  as if their letters were sign names (`=aby` gave "sw"), so each clear word of the reading counts as a departure.
- Markers for unread signs, 3 of the 18: ‹N› twice and ‹C›, where the key gives z and w (stated in the reading notes);
  a fourth word, chciał, is counted only because it follows ‹N›.
- Key file and reading differ by a stated override, 1 of the 18: ‹kodzarzyc› (e05). `key.tsv` has V = g; the reading
  uses z for V at d05 and e05 after the shape plate, as the comment of `key.tsv` and the head of `reading.md` say. A
  value that holds at two places only cannot go in the sign table, so the key file is left as it is.
- One unmarked difference in a clear word (not cipher): d11 is `=potewaz` in `transcription.txt` and `decryption.txt`,
  "POTEWAZ" in the decryption column of `reading.md`, and "ponieważ" in its reading column and running text, with no
  mark. Either the transcription of the clear word or the reading is off; the image was not seen for this check.
- Normalisation: the reading adds Polish diacritics (15 cipher words, e.g. poslowie -> posłowie, zas -> zaś) although
  its title says "spelling of the letter"; the key has no value with a diacritic.
- Changed: nothing in the key, the transcription or the reading. Figures after: the same, 18 of 63. Unmarked letter
  changes in cipher words: 0. Open: the d11 clear word.

Marked on 16 Nov 2026: 2 places in `reading.md`, the same clear word at d11 in the line table and in the running text,
now printed po[ni]eważ ([ ] = letters inside a clear word that the transcription does not give, the file's own mark; the
transcription has t there). No letter of the reading was changed and the disagreement is not settled: `transcription.txt`
and `decryption.txt` keep `=potewaz`. Nothing was left unmarked. Header of `reading.md`: two notes added, one saying
that the diacritics and the punctuation are added in the reading, one on d11. The count of cipher words (53 of 63) is
not affected, clear words being outside it. `research/reading_audit/v2_score.py reading.md pl`: hole rate 0.024 before, 0.037 (the script counts the marked clear word as a hole; 82 words) after.

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

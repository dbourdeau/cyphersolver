# Check of the contributor's key and reading (7 Nov 2026, refreshed at commit f465095)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #318). The Estense scans are not reachable from
the project's environment, so **no transcription was compared with a scan by the project**. No human palaeographer has
repeated the check. The first version of this check (published the same day) was made on an earlier snapshot of the
repository, in which the decryption still carried hand fixes; this one uses its commit f465095.

## 1. The table reproduces the decryption exactly

The 40 rows of `key.tsv` (sign label, digit class, value, count of uses) were applied to the cipher signs of
`transcription.txt`: a sign label with a small digit gives the consonant of its class and the vowel of the digit; a sign with
no digit is a single letter; the sign s is the doubling mark (shown "=" in `decryption.txt`); two shapes are nulls. The result
is identical to `decryption.txt` on **all 31 cipher lines**. So `decryption.txt` is the key applied to the transcription,
with no manual edit, as the contributor says. The rows cover the sign shapes of the letter, including the rare ones (a delta,
a sigma, a hooked stem, a looped angle, a short stroke, an arch, a slant with a dot, a triangle, a crossed loop).

## 2. Control against shuffled tables

No Spanish language model could be built here (the Gutenberg corpus returns 403). A lexicon test was used instead: about 85
common Spanish words (articles, prepositions, pronouns, the subject words of this letter) were matched greedily, longest
first, over the 1,114 letters the key gives for the cipher passages. The key covers 0.635 of the letters. The same test on
300 keys with the same signs and shuffled output letters covers at most 0.300 (mean 0.144). The control is weaker than for a
free substitution, because a table of this structure keeps the vowels in place; it still separates the key from random ones.

## 3. What the reading shares with the clear text and with print

The cipher passages join the clear text around them: after "nos days particular cuenta" comes "del patrimonio y estado dél, y de
las necesidades desse reyno" and "de la Goleta, ... por consideración del armada del Turco"; the letter names Perpiñán and
Navarra, the Count of Anguillara and the Viscount Cigala with his galleys. The contributor checked the content against Capasso,
"Il governo di Don Ferrante Gonzaga in Sicilia dal 1535 al 1543" (1906): the Emperor presses Gonzaga to pay the Count (Virginio
Orsini), Cicala threatens to leave imperial service, the treasury is exhausted. The project did not open Capasso. The wider
context (the war of 1542, the siege of Perpignan) is the contributor's, from memory, and was not checked here.

## 4. What was not checked

- The transcription against the scans. The contributor's two passes agree on 94.4% of signs and each difference was settled on the
  scan; a check of every line at full size on 7 Nov 2026 added two signs at line ends, giving 707 signs. The project did not
  repeat it.
- The places where the reading leaves the key (`doubtful_places.md`): "caber" read "haver" rests on the four uses of g with the digit 6
  (all in "haver"); the letter model used there is built from Don Quijote and knows nothing of grammar, so it is a weak test.
- The chancery's clear draft, which may survive in a Spanish archive (not searched).

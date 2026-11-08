# Check of the contributor's key and reading (7 Nov 2026, repository commit f465095)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #320). The AGAD scans are not reachable from the
project's environment, so **no transcription was compared with a scan by the project**. No human palaeographer has repeated
the check.

## 1. The key

`key.tsv` has 30 number-to-letter rows, one letter per number and one number per letter (30 distinct plain letters,
including Polish ł, ą, ę and the digraph-like æ and œ the writer uses for Latin). The transcription writes the letters of a word
joined by dots and the words separated by dashes; code groups are written without dots.

## 2. Control against shuffled keys

No Polish language model could be built here (the corpus fetch returns 403), and the contributor himself notes that his
Polish model is of modern text while the letter has long Latin stretches (so a wrong key can outscore the true one). A
different test was used. The 491 dotted words of the cipher were decrypted with the key and each was looked up in a word list made of
the clear words of the same letter (the clear Polish and Latin parts, normalised without diacritics) and about 90 common Polish
and Latin function words. 31.2% of the decrypted words are in the list, against at most 5.7% (mean 0.9%) for 300 shuffled keys.
The clear words of the letter share its vocabulary, which helps the true key, so this is a check that the key makes words of
this letter, not an independent measure of correctness. The decrypted words begin, for example, "dawszy mu na drogę czerwonych
złotych woli panskiey niepomyslną abardziey nieszczęsliwą sytuacyą naszą protectrix potentia nostra iuz się ztym klarygowała".

## 3. What the reading shares with the clear text and with history

The cipher passages join the clear text around them (the clear "Instantanee tedy" is followed by "dawszy mu na drogę ...
expedyuię go"). The content fits what is known of the winter of 1735-36: the preliminary articles of Vienna (October 1735), the
armistice, and Stanisław Leszczyński's abdication in January 1736; the contributor reads the courier Orlik as an exile's
courier, and "Keyserling, the Russian envoy" as the envoy at Warsaw. The history is from memory (the project did not check it),
and the year 1736 is the contributor's inference from the contents.

## 4. What was not checked

- The transcription against the scans. The contributor's two passes agree on 99.1% of 2,844 tokens and each of the 23 differences
  was settled on the scan; one more group was split later ("5 - 79" is two words).
- The contributor's own limits: no held-out half was run (a short solve on half the text fell into a degenerate key); the
  Polish model was changed once after a first look; the blind reader translated about 85% of the clauses.
- The clear parts of the letter are a working reading of the contributor, not an edition.
- The code-group values other than the 12 uses of 125 (Stanisław) are guesses or unread; 675 "[?Monti]" has no confirming text.

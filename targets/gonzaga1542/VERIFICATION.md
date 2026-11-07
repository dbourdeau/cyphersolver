# Check of the contributor's key and reading (7 Nov 2026)

What an AI model (Claude) checked of the submission by Prabal Gupta (issue #318). The Estense scans are not reachable from
the project's environment, so **no transcription was compared with a scan**. No human palaeographer has repeated the
check.

## 1. The table reproduces the decryption

The table in `key.tsv` was applied to the cipher signs of `transcription.txt` (a sign label with a small digit gives the
consonant of its class and the vowel of the digit; the signs with no digit are single letters; the hooked, looped and crossed
shapes the table does not list were left as ?). The result is identical to `decryption.txt` on 12 of its 31 cipher lines and agrees with
it on 95.1% of the letters over all the lines (a sequence match of 1,117 letters); the differences are the rare signs the
contributor fixed by sense (listed in `decryption.txt` only) and the unlisted shapes. For example `p1.04` gives
"delpatrimonioyestadodelydelasnecesidadesde?erey" by the table and "...necesidadesdeserey" in the decryption, one rare sign
differing; `p1.05` and `p2.05` agree to the letter.

## 2. Control against shuffled tables

No Spanish language model could be built here (the Gutenberg corpus returns 403). A lexicon test was used instead: about 85
common Spanish words (articles, prepositions, pronouns, the subject words of this letter) were matched greedily, longest
first, over the 1,060 letters the table gives for the cipher passages. The table covers 0.605 of the letters. The same test
on 300 tables with the same signs and shuffled output letters covers at most 0.296 (mean 0.175). The control is
weaker than the one for the Branicki letters, because a table of this structure keeps the vowels in place; it still
separates the table from random ones.

## 3. What the reading shares with the clear text

The cipher passages read as continuous Spanish that fits the clear words around them: after "nos days particular cuenta" comes
"del patrimonio y estado dél, y de las necesidades desse reyno" and "de la Goleta, ... por consideración del armada del Turco";
the letter names Perpiñán and Navarra, the Viscount Cigala and his galleys. The history (France declared war on Charles V in July
1542; the autumn siege of Perpignan; Ferrante Gonzaga viceroy of Sicily, governor of Milan from 1546) is from memory and was not
checked here.

## 4. What was not checked

- The transcription against the scans, and the doubtful signs the contributor fixed by sense.
- Whether the reading keeps closer to the sense than to the signs: three "caber" are read "haver", one clause is unread,
  and the reading is an emended text in places.
- The chancery's clear draft, which may survive in a Spanish archive (not searched).
- The identification "Novellara" (a guess).

# Charles V to Ferrante Gonzaga, Monzón, 11 August 1542

Emperor Charles V writes to Ferrante Gonzaga, Prince of Molfetta, his viceroy of Sicily. The letter is signed "Yo el Rey" and countersigned "Idiáquez". The back gives the address, and it marks this copy as the duplicate.

- **Where:** Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera K, Karl V, sfasc. IV, cc. 109-110.
- **Scans:** https://lodovico.medialibrary.it/media/schedadl.aspx?id=c710a32c-42a7-4159-8abc-472aed58f7c9
- **Ledger:** catalogue 1560 at https://github.com/dbourdeau/cyphersolver lists this letter as still unread. The undated letter in the same entry (cc. 131-132) is not covered here.

## What it says

- Sicily cannot pay for its infantry, its galleys and the fort of La Goleta without outside help.
- The Emperor's other kingdoms are as short or worse, so no help can come now.
- La Goleta must be provided for, because of the Turkish fleet.
- Spies report that the main French effort is coming to the frontier of Perpignan, and that the French threaten Navarre.
- The Count of Anguillara must be paid. The Emperor repeats this order.
- The Viscount Cicala must be paid for his galleys, because someone is soliciting him to take another contract.

Read it: [Spanish](reading.md), [English](translation.md).

## Outside check

The source is Carlo Capasso, "Il governo di Don Ferrante Gonzaga in Sicilia dal 1535 al 1543", *Archivio Storico Siciliano*, n.s. 31 (1906).

Capasso works from Gonzaga's registers at Parma: https://archive.org/details/nsarchiviostoric31soci

| The cipher says | Capasso says |
| --- | --- |
| Pay "el sueldo del Conde de la Anguillara", "os lo tornamos a encargar" | Pp. 387, 409: the Emperor presses Gonzaga to pay the Count, Virginio Orsini, whose galleys burden the Sicilian treasury. |
| Pay Cicala, who "es solicitado" for another contract | P. 387: in June, Captain Cicala threatens to leave imperial service unless he gets 8,000 ducats. |
| "El mayor esfuerço de los franceses viene a la frontera de Perpiñán" | P. 408: the main French effort is for now toward Spain. |
| Sicily cannot pay without outside help | P. 409: the treasury is exhausted. |

**What happens next.** Pp. 409-410: "proprio in questo momento" the Count goes over to the French with his galleys. Gonzaga sends Cicala after him on 24 August. Capasso adds that Gonzaga feared blame, because he had not paid the Count as ordered.

So this letter repeats the order to pay the Count days before the news of his defection reaches Sicily. That timing is my reading, and I do not know the exact day he left.

Capasso cites other letters, but I found no citation of this one.

## The cipher

A base sign is a consonant, and a small digit above it adds the vowel. The digits 1 to 5 and the digits 6 to 9 and 0 both run a, e, i, o, u. A sign with no digit is a single letter.

`key.tsv` gives every sign label with its value and its count of uses. A label names a shape in `transcription.txt`, not a value. `decryption.txt` is `key.tsv` applied to the transcription, with no manual edit.

| With a digit | Consonant |
| --- | --- |
| x | d |
| z | r |
| d | p |
| n | m |
| a | t |
| w | tr |
| q | n |
| t | l |
| g | c with 7 to 0; h with 6 |
| b | s |
| S, I, F | b |
| P | f |
| Q | pr |
| c | g with digits 1 to 5, qu with digits 6 to 0 |

| With no digit | Letter |
| --- | --- |
| h | e |
| v | o |
| y | a |
| t | y |
| n | u |
| D | i |
| x, z | n |
| f, T | s |
| o, r, Q | r |
| c | l; d at the end of a syllable |
| C | c |
| E | p |
| M | m |
| G, F | f |
| s | a doubled or palatal consonant: ss, ll, rr or ñ |
| X, g | nulls |

Two values rest on their uses, not on the digit pattern:

- g with 6 gives "ha". Its four uses are all in "haver", and no cipher word of the letter needs "ca". The digit is a clear 6 each time on the scan.
- c with no digit gives d at the end of a syllable: "seguridad", "necesidad", "podrá". Elsewhere it gives l.

The rare shapes:

- D is a delta, and S is a sigma.
- P is a hooked stem, and Q is a looped angle.
- I is a short stroke, and C is an arch.
- E is a slant with a dot, G is a triangle, and X is a crossed loop.

## How it was solved

My count matching algorithm, which opened the other letters in this repo, does not read this sign-and-digit plan. A different bespoke fit does. It takes the plan from the sign statistics of the letter itself, with no key, sibling letter or crib, then solves it on a Spanish letter model. The text was read from that.

- **Transcription:** two passes agree on 94.4% of signs. Each difference is settled on the scan. A check of every line at full size on 7 November 2026 added two signs that both passes missed at line ends, which gives 707 signs.
- **Score, on the first pass:** the key scores -2.21 per letter under the Spanish model. Shuffled signs score -3.33.
- **Repeat runs, on the first pass:** all six starts reach the same key.
- **Held-out half, on the first pass:** a key fitted on the first half agrees with the full key on 89.7% of tokens in the second half. Each half has only about 350 tokens.
- **Blind read:** a reader with no context named this text as Spanish, and it named two shuffled controls as noise.

## What stays open

The cipher passages hold 246 words. 240 of them read, 97.6%.

`doubtful_places.md` lists every place where the reading leaves the key, with what the scan shows and what I tried. The two signs added at line ends settle two of them: "que es solicitado" and "que sucediesse" now read straight from the key.

Six words stay marked. The writer left out a letter or a syllable, or wrote a wrong sign:

- "[g]randes", where the signs give "rrandes";
- "de [?allí]", where the signs give "dela=i";
- "t[a]n", where the digit is a clear 2 and gives "ten";
- "e[x]pedientes", where the signs give "elpedientes";
- "nos [?screbir]", where the last sign is a clear l;
- "amena[ça]van", where a syllable is left out.

"Anguillara" comes from the string "lannuilara". Capasso's account supports it, so it is not marked as doubtful.

I found no printed copy of this letter. But the chancery's clear draft may survive in Spanish archives, and I could not check those.

No historian has checked this reading yet.

## Context, from memory and not checked here

- France declared war on Charles V in July 1542. That autumn a French army under the Dauphin besieged Perpignan and failed to take it.
- La Goleta was the Spanish fort at Tunis.
- Alonso de Idiáquez was a secretary of Charles V.

## Files

- `reading.md`: the letter in Spanish
- `translation.md`: the letter in English
- `transcription.txt`: the cipher and the clear text, line by line, with shape labels
- `key.tsv`: every sign label, its value and its count of uses
- `decryption.txt`: the decryption, line by line, from `key.tsv` with no manual edit
- `doubtful_places.md`: every place where the reading leaves the key, and what I tried

The page images stay with the Biblioteca Estense under their own licence (CC BY-NC-SA). They are not copied here.

© 2026 Prabal Gupta. First published here, 7 November 2026. Released under CC BY 4.0: reuse it, and credit me.

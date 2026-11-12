# vibejuel1651: Peder Vibe to Peder Juel, Danish resident in Stockholm, 1649-1655, cipher passages of 21 letters or pages (catalogue 2527)

Status: read in part (Brice Dudout, 11 Nov 2026; key recovered and validated on a held-out set, margin 0.841; 400 cipher words in letters, 345 certain, 45 probable, 2 restored, 8 unresolved = 97.5% read by sense, but 143 nomenclator codes are not identified, so 390/543 = 71.8% with the codes counted as holes, under the 95% rule). Open: the nomenclator; the Krag letters of 1648 (other system, not solved).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents (transcription, system, protocols, measurements,
reading and write-up). Catalogue entry **2527**, found and vetted by Daniel Bourdeau on 11 Nov 2026 (TKUA paging pass), who
pointed to the interlinear letters on image 78 as the crib.

## Document

Copenhagen, Rigsarkivet, Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del, Sverige: Resident Peder Juels og Mogens Høegs
gesandtskabsarkiver, Ordrer og breve m.m. 1648-55 (leaves stamped "Ny kongl. Saml. Fol. 1299 e"); Arkivalieronline unit 261583,
images 57-95. Letters of Peder Vibe (Copenhagen, later Bierreds and Flensborg) to Peder Juel in Stockholm, numbered in an old hand
(N. 298 ... 337, 143, 167), with passages and whole leaves in a number cipher between clear Danish; plus three letters of
[O.] Krag to Juel of 1648 (images 57, 58, 60) in another cipher. Only N. 319 (image 78) carries a decipherment of the time: faint
letters over about a third of its words.
The images were used for study only; none is included, nor any crop or derivative (Rigsarkivet images are treated here as not
republishable). Credit: Rigsarkivet, Arkivalieronline.

## System and key (`key.tsv`)

A shift cipher with the shift chosen per word. Each cipher word is an **opener** followed by a **body**: the opener (1-3 or 24-39)
gives a shift k, and each body number is the rank of the letter plus k. Vibe used two alphabets, and names both in clear on image
62 (11 Jan 1649): the new one ("dett ny Alphabet") is to be sent, and meanwhile he writes "wed woris forige gamble Ciffres".

- **gamle Ciffres** (old cipher; letters of 1649-1650, the slip f. 318, N. 330 of 20 Sep 1651): 23 letters, **cyclic mod 23**,
  k = -(opener mod 3), so openers 24/27/30 give 0, 25/28/31 give -1, 26/29/32 give -2.
- **ny Alphabet** (new alphabet; N. 316, 319, 331-336, 1651-1654; N. 143/321, 1654; N. 167/337, 1655): 25 letters
  a ... u w x y z ø, not cyclic; one opener table in every letter: 24-29 -> 0, 30-34 -> 1, 35-39 -> 2, 1-3 -> 3.
- In both, 32/33/34 in the body stand for 1/2/3, and a word may be split in pieces with their own openers.
- **Nomenclator**: two- to four-digit numbers between the words (211, 228, 257, 422, 872 ...; in 1655 a new list up to 1771).
  None is identified. Vibe defines two in clear on image 80 (349 and 561, names read as probable only).
- `scripts/decode.py` decodes `transcription.txt` with the fixed tables into `decryption.txt` (no language model).

## Validation (`validation.txt`)

Two pre-registered tests, each with a held-out set transcribed and hashed before any decryption, and one run each.
- **Test 1 failed** (margin 0.21 < 0.30). It froze one opener table for the whole unit. Cause, found after it: N. 330 is in the
  old cipher (cyclic alphabet, k = -(opener mod 3)), not in the table of N. 319. The system was right; the single-table
  assumption was wrong. That set was not measured again.
- **Test 2 passed**: tables learned per letter, controls with the same optimisation; a new held-out set never opened (images 81,
  83, 84, 87, 90: 55 words, 339 numbers): M1 -2.713 against at most -3.555 for 300 controls, **margin 0.841**; readable Danish
  sentences (criterion S). One word of image 87 had been deciphered in the head before the hash; it is declared.

## Reading (`reading.md`, `translation.md`)

- 400 cipher words in letters in Vibe's letters: 345 certain, 45 probable, 2 restored, 8 unresolved: **97.5%**.
- Re-read after the measurements: held-out set 2, 50/51 = **98.0%**; held-out set 1, 55/55 = 100%. The measurements were not
  run again.
- But **143 nomenclator codes** are not identified. Counted as holes (Daniel's rule), the reading falls to **390/543 = 71.8%**,
  so the class is "read in part". If you count codes otherwise, the 97.5% figure stands for the cipher words.
- Content: the Danish court seen from Copenhagen, 1649-1655. In 1649-50, rivalries round #211 (who is "won", "approached",
  "reconciled"); discontent of sailors and people as the Marselis and Friedrich Möller get assignments on the best revenues; the
  High Steward kept away by discontent; the quarrel between #211 and #228 over an arrest and an alleged murder plot; the account
  of the Norwegian fleet. In 1651, #422 to be judged; a seal of #876 to be copied (N. 316); a servant debauched to get letters
  of #872 (N. 319); how to win #370 away from #422 (N. 330). In 1653, Würtz ennobled in Sweden by #222; fireships built by #222
  (N. 333); a border meeting. In 1654-55, an opened letter of #879; who has the confidence of #879; a design that leaves the
  States General perplexed and ships to lie in the Sound (N. 167, 1655).

## Prior art

No decipherment of these letters is known. The only decipherment of the time is the partial interlinear one on N. 319 (image 78).
Daniel Bourdeau's vetting of entry 2527 (11 Nov 2026) found nothing on DECODE, in Tomokiyo or in Lasry. Fryxell (1836) prints a
Swedish abstract of Juel's register of outgoing letters (lead 2553), without the cipher passages. A web search of ours (11 Nov 2026) found no edition of
the cipher passages. We have not searched the Royal Library (NKS 1299 e fol.) or the Danish printed collections at length, so an
edition we do not know of remains possible.

## Remaining gaps

- the 143 nomenclator codes of Vibe's letters (211, 228, 257, 422, 872 ...; 1655 list up to 1771) - blocker: open-codes; the letters read but the codes do not; no list is in the unit and only 349 and 561 are defined in clear; Juel's replies, the rest of NKS 1299 e at the Royal Library, or a code list in the Juel papers could give them
- eight unresolved cipher words (images 62, 64, 69 twice, 71, 72, 78, 93; listed in reading.md) - blocker: illegible; blots, tears and confused ticks at the resolution served online; a re-reading of the original could settle some
- the three letters of [O.] Krag of 1648 (images 57, 58 left, 60 right; 29 groups, 5 codes) - blocker: too-short; another system (dotted numbers 1-36), not the old or new cipher of Vibe; about 160 numbers, too few for a homophonic solve; other Krag letters would be needed

## Escalation

- [x] siblings: all images 57-95 of unit 261583 checked; cipher on 57, 58, 60 (Krag) and 62-93 (Vibe); the related register of Juel (lead 2553, unit 261585) and Juel's glossed originals (unit 261575) were opened, and register p. 115 (1648) turned out to be in Vibe's old cipher; that lead is not part of this target
- [x] clear-pages: the clear pages of the unit were read for their remarks on the cipher (image 62: old and new alphabet; image 80: codes 349 and 561 added, Juel's numbers written in letters; image 93: Krag's last cipher lacks the States General and the Øresund); none is a decipherment
- [x] known-keys: the only key material is in the unit (the gloss of N. 319); DECODE, Tomokiyo and Lasry have nothing (Daniel's vetting); the 1673-74 code of the same embassy archive (christianv1673) is another system
- [x] print: Fryxell 1836 (abstract without the cipher passages); Daniel's vetting; our web search found no edition
- [x] key-rebuild: both alphabets and both opener tables rebuilt and applied to every letter; the w/ø letters of the new alphabet added after the test; codes bracketed only by sense (not counted)
- [x] retry: every unread word retried at native zoom with the final tables and regraded (set 2 from 71% to 98.0%; openers "out of table" shown to be division errors)

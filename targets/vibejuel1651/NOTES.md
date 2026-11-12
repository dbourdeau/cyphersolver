# vibejuel1651: Peder Vibe to Peder Juel, Danish resident in Stockholm, 1651-1655, cipher passages in the new alphabet ("ny Alphabet") of 11 letters or pages (part of catalogue 2527)

Status: read in part (Brice Dudout, PR #410, 11 Nov 2026; integrated and split by key 12 Nov 2026). Key recovered based on adjacent plaintext, key state partial: the letter alphabet and its opener table are recovered, the nomenclator has no values. 146 of 149 cipher words given a value (98.0%; 132 certain, 14 probable, 1 restored, 2 unresolved); with the 73 nomenclator codes counted as holes the read share is 146/222 = 65.8%, under the 95% bar. The first pre-registered test failed; the second, with a rule changed after that result, passed (see Validation).

Contributed by Brice Dudout (Europe chiffrée), with AI agents (transcription, system, protocols, measurements, reading and
write-up; the model is named in the pull request). Catalogue entry **2527**, found and vetted by Daniel Bourdeau on 11 Nov 2026
(TKUA paging pass), who pointed to the interlinear letters on image 78 as the crib.

The letters of 1649-1651 in the same unit use a different cipher, the old one ("gamle Ciffres"), with its own target:
`targets/vibejuel1649/`. This folder holds the new alphabet only (split on 12 Nov 2026, see the end of these notes).

## Document

Copenhagen, Rigsarkivet, Tyske Kancelli, Udenrigske Afdeling (TKUA), Speciel del, Sverige: Resident Peder Juels og Mogens Høegs
gesandtskabsarkiver, Ordrer og breve m.m. 1648-55 (leaves stamped "Ny kongl. Saml. Fol. 1299 e"); Arkivalieronline unit 261583,
images 77-93. Letters of Peder Vibe (Copenhagen, later Bierreds and Flensborg) to Peder Juel in Stockholm, numbered in an old hand
(N. 316, 319, 331-336, 143/321, 167/337), with passages in a number cipher between clear Danish. Dated pieces: 6 Jan 1653
(N. 334, date on image 80), 13 Sep 1654 (N. 336), 1654 (N. 143/321), 6 May 1655 (N. 167/337); N. 316 and N. 319 are undated;
the contributor places them in 1651 (not checked further). Only N. 319 (image 78) carries a
decipherment of the time: faint letters over about a third of its words.

Eleven sections in `transcription.txt`: images 77 (N. 316), 78 and 79 left (N. 319), 79 right (N. 334), 81 (N. 332), 83 left
(end of a letter), 83 right (N. 331), 84 right (N. 333), 87 right (N. 335), 90 left (N. 336), 91 right (N. 143/321), 93 right
(N. 167/337).

The contributor included no image. Credit: Rigsarkivet, Arkivalieronline.

## System and key (`key.tsv`)

A shift cipher with the shift chosen per word. Each cipher word is an **opener** followed by a **body**: the opener (1-3 or 24-39)
gives a shift k, and each body number is the rank of the letter plus k.

- **ny Alphabet**: 25 letters a ... u w x y z ø, not cyclic; one opener table in every letter: 24-29 -> 0, 30-34 -> 1,
  35-39 -> 2, 1-3 -> 3.
- 32/33/34 in the body stand for 1/2/3, and a word may be split in pieces with their own openers.
- **Nomenclator**: two- to four-digit numbers between the words (222, 353, 397, 770, 872, 876, 879 ...; in 1655 a new list up to
  1771): 73 code tokens, 49 different numbers. None is identified. Vibe defines two in clear on image 80 (349 and 561, names read
  as probable only). None of the 49 occurs in the old-cipher letters, whose 22 codes are different numbers.
- `scripts/decode.py` decodes `transcription.txt` with the fixed table into `decryption.txt` (no language model).

## Validation (`validation.txt`, `frozen/`)

Two pre-registered tests, each with a held-out set transcribed and hashed before any decryption, and one run each. The order of
events (protocol hashed before the set was opened) is by the contributor's record: the pull request is one commit and the
timestamps are self-declared.

- **Test 1 failed.** Declared: one opener table for the whole unit, the table of N. 319, with a 23-letter alphabet; held-out
  images 74 (N. 330), 77 (N. 316) and 79 right (N. 334), 54 words, 335 numbers; pass if M1 (mean log-probability per character
  under a 4-gram model of old Danish) is at least the best of 600 controls + 0.30. Result: M1 -3.068, best control -3.281,
  margin 0.21, under the bar of 0.30 (the lexical criterion C2 failed too). The set was not measured again.
- **The rule was then changed** (declared by the contributor): after test 1, N. 330 was found to be in the old cipher, and test
  2 was written with a weaker hypothesis, a shift per word with the opener table **learned on each letter** (k in -4..4 per
  opener value, by likelihood), controls getting the same optimisation.
- **Test 2 passed**: new held-out set (images 81, 83, 84, 87, 90: 55 words, 339 numbers, all in the new alphabet): M1 -2.713
  against at most -3.555 for 300 controls, margin 0.841 over the bar of 0.30; readable Danish sentences (criterion S). One word
  of image 87 had been deciphered in the head before the hash; it is declared.
- **What test 2 does and does not show.** It validates the shift-per-word system on new-alphabet letters. It does not test the
  fixed table of `key.tsv`: the table was fitted per letter in the test, and the 25-letter alphabet with w and ø was established
  after it.
- **Other evidence for the fixed table**: the gloss of the time on N. 319 agrees with the mechanical decode wherever it is
  legible; the tables learned blind in test 2 were the table of N. 319 in four letters of five; and the later controls below.

## Reading (`reading.md`, `translation.md`)

- 149 cipher words in letters: 132 certain, 14 probable, 1 restored, 2 unresolved. Given a value: 146/149 = **98.0%**.
- 73 nomenclator codes (49 different) have no value. Counted as holes, the read share is **132/222 = 59.5%** on certain words only (146/222 = 65.8% with the 14 probable words): read in part.
  (The pull request gave one figure for both ciphers together, 390/543 = 71.8%, with 143 codes; see the recount below.)
- Re-read after the measurements: held-out set 2, 50/51 = 98.0%.
- Content, 1651-1655: a seal of #876 to be copied from wax impressions (N. 316); a servant debauched to get a packet of letters,
  and work to intercept letters of #872 (N. 319); #353 and #397 leaving for #770 with an instruction, and a border meeting (N. 334, 1653); Würtz said to
  be ennobled by #222 in #770 (image 83); fireships built by #222 (N. 333); an opened letter of #879 (N. 336, 1654); whom #879
  trusts most (N. 143/321, 1654); a design that leaves the States General perplexed, and something to lie in the Sound (N. 167, 1655).
  Who does what is mostly behind the codes.

## Prior art

No decipherment of these letters is known. The only decipherment of the time is the partial interlinear one on N. 319 (image 78).
Daniel Bourdeau's vetting of entry 2527 (11 Nov 2026) found nothing on DECODE, in Tomokiyo or in Lasry. Fryxell (1836) prints a
Swedish abstract of Juel's register of outgoing letters (catalogue 2553), without the cipher passages. The contributor's web
search (11 Nov 2026) found no edition of the cipher passages. The Royal Library (NKS 1299 e fol.) and the Danish printed
collections were not searched at length, so an edition remains possible. No prior-art search was repeated at verification or at
integration: this section rests on the contributor's and the catalogue vetting's record.

## Integration check (12 Nov 2026)

PR #410 was verified independently before integration (scripts re-run, hashes checked, a second decoder written, images 62, 74
and 83 fetched from api.rigsarkivet.dk). What that found, and what was changed here:

- **Reproduction.** Test 2 (M1 -2.713, best control -3.555, margin 0.841, the learned tables) and test 1 (M1 -3.068, best control
  -3.281, failed) reproduce exactly from `frozen/` with the 11 archive.org corpus texts (all 11 SHA-256 match
  `PROTOCOLE.sha256`). All frozen hashes match. A second decoder gives the same `decryption.txt`.
- **Why test 1 failed, measured.** Scoring the three held-out images of test 1 separately with the frozen table: image 74
  (N. 330) -3.980 against a best control of -3.125 (worse than chance); image 77 (N. 316) -2.353 against -2.961; image 79
  (N. 334) -2.632 against -3.094. One letter sank the set, the old-cipher one.
- **Later controls made at verification** (after the fact, not pre-registered):
  - the fixed new table, with no fitting, on held-out set 2: M1 -2.611 against a best control of -3.174, margin 0.563. Table and
    set had both been hashed before set 2 was opened, so the hypothesis of test 1 holds on new-alphabet letters;
  - a per-letter refit of k on all 22 sections of both ciphers agrees with the fixed tables for 383 of 403 words; every
    disagreement is an opener seen once or twice;
  - the fixed new table against 200 random opener tables on the final transcription: -1.987 against a best of -2.568.
- **Images.** Image 83 left: about 95 numbers agree with the final transcription at reduced size. The 14 probable words rest on
  numbers corrected by sense after the measurement; none of them was checked against the image at verification.
- **Split by key.** The pull request filed two ciphers and the unsolved Krag letters in one target. They are now three things:
  this folder (new alphabet), `targets/vibejuel1649/` (old cipher), and the Krag letters of 1648, moved out as a lead (see Split).
- **Class and key state.** `outcome.key` was "recovered"; it is "partial" (the nomenclator has no values). `fraction_read` was
  0.718; it is now the share of cipher words given a value (0.980) with `codes_open` 73; `read_share` and `fraction_coherent`
  are 0.658, the figure with the codes as holes, which is the one the site shows.
- **Counts taken again from the files.** Image 77 has 22 cipher words, not 23 (so 149 words, 132 certain). Image 93 has 24 code
  tokens, not 26. The code 545 that opens N. 319 stood inside the clear bracket in `transcription.txt`; it is now a `C` token, as
  in the reading. That gives 73 code tokens in these letters (the pull request's table summed to 75; its total of 143 for both
  ciphers becomes 68 + 73 = 141, where the verification counted 140 `C` tokens before the 545 fix).
- **`scripts/decode.py`** used `eval()` on the `#K` lines; it now uses `ast.literal_eval`. The output was byte-identical before
  and after that change (checked before the 545 fix, which changes one token).
- **Validation wording.** The pull request's "system validated" is restated above: test 1 failed, test 2 passed on a rule changed
  after test 1, and it validates the system, not the fixed table. `validation.txt` carries a preface saying so; the contributor's
  text follows unchanged.
- **Reading review.** The reading was read as sentences against the translation at integration: grade B (coherent Danish where
  the cipher words stand, but most sentences have a code for their subject or object; images 87 and 93 are fragments).
  `_check_reading` calls it "not a reading" on shape, because of the codes.
- **Claims review.** No separate reviewer agent was available in this session: the page was re-read line by line against these
  notes, the profile and the reading files with the checklist of `claims-review.md`. Fixed on that pass: in N. 319 it is #485,
  with the valet of #254, who is to debauch the servant (the page had the valet); "an embassy" for #353 and #397 was more than
  the reading says; the gloss is "of the time", not "a clerk's"; N. 316 and N. 319 are dated 1651 by the contributor only; the
  codes stand for people and places by the sense only. An independent reader is still owed.

### Claims review by a second reader (12 Nov 2026)

- The published read share now counts certain words only: 132 of 149 (59.5% with codes as holes). The 14 probable words (a corrected number, a
  re-divided tick, a supplied letter or an unusual spelling) are not counted, by the rule used for every target of
  this round; the figure with them is given once.
- Wording corrected on the page from this review; see the commit of 12 Nov 2026.

## Remaining gaps

- the 73 nomenclator code tokens (49 numbers: 222, 353, 397, 770, 872, 876, 879 ...; the 1655 list up to 1771) - blocker: no-key-material; no code list is in the unit and the gloss of N. 319 covers letters only; two numbers are defined in clear (349 and 561, image 80) but their names are read as probable only; Juel's replies, the rest of NKS 1299 e at the Royal Library or a code list in the Juel papers could give them
- two unresolved cipher words (image 78: 31.34.26.13.20; image 93: 30.?.9.2.14=5.6.20) - blocker: illegible; a blot after the opener on image 93, and a word read clearly but glossed only "°m t" on image 78; the original could settle them
- the 14 probable words not checked against the images at verification - blocker: illegible; each correction rests on a single number at the limit of the microfilm scans served online (listed with its reason in reading.md)
- prior art outside the repository not searched again (no edition, DECODE or literature search at verification) - blocker: needs-physical-access; the Royal Library's NKS 1299 e fol. and the Danish printed collections are not online in full

## Escalation

- [x] siblings: all images 57-95 of unit 261583 checked by the contributor; the old-cipher letters are read in targets/vibejuel1649; Juel's register (catalogue 2553, unit 261585) and his glossed originals (unit 261575) were opened by the contributor, nothing in the new alphabet reported
- [x] clear-pages: the clear pages of the unit were read for their remarks on the cipher (image 62: old and new alphabet; image 80: codes 349 and 561 added; image 93: Krag's last cipher lacks the States General and the Øresund); none is a decipherment
- [x] known-keys: the only key material is in the unit (the gloss of N. 319); the old cipher of the same correspondents shares no code number with these letters; the 1673-74 code of the same embassy archive is another system
- [x] print: Fryxell 1836 (abstract without the cipher passages); the catalogue vetting (Fridericia 1894, Gigas 1883); the contributor's web search found no edition
- [x] key-rebuild: alphabet and opener table rebuilt and applied to every letter; w and ø added after the test; codes bracketed only by sense (not counted)
- [x] retry: every unread word retried by the contributor at native zoom with the final table and regraded (set 2 from 71% to 98.0%; openers "out of table" shown to be division errors)

## Split (12 Nov 2026)

One key, one entry. `targets/vibejuel1651` arrived holding the letters of both ciphers and three letters of Krag. It now holds
the 11 sections in the new alphabet. The 11 old-cipher sections (images 62-74, 10 letters or pages) are `targets/vibejuel1649/`
with their own key, reading, page and ledger rows. `frozen/` (protocols, hashes, scripts and held-out transcriptions of both
tests) stays here unchanged, because test 2 concerns this cipher and the hashes must keep matching; `vibejuel1649` points to it.
The three Krag letters of 1648 (images 57, 58 left, 60 right; 29 groups and 6 code tokens as transcribed; another system, not solved) are a lead:
`research/leads.json` id 2527 (the catalogue entry narrowed to them) with the transcription in
`research/sweep_2026-11-11_tkua_paging/krag1648_transcription.txt`.

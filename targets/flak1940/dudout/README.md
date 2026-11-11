# flak1940/dudout: the radio message of 4 June 1940 (frames 0863-0867) and the key of that day, recovered independently and tested on a held-out part

Status: read (Brice Dudout, 12 Nov 2026; 129 of 129 words, 124 certain and 5 probable). Key of 4 June 1940 (19 and 22 columns), the same as Harumi-Matsuba's, who published it first (issue #364, 11 Nov 2026); recovered here independently the same day from the teleprinter copy on frame 0862, and passed one pre-registered test on part 4, held out.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus agents (transcription from the images, solver code, measurement, reading). This folder adds the message of 4 June 1940 to `targets/flak1940/`; the files of the 17 May messages are not changed.

## Priority

Harumi-Matsuba added the key of 4 June 1940 and his decryption of frames 0863-0867 to his repository on 11 Nov 2026 (`Harumi-Matsuba/flak1940-public`, commit de8efa9, 08:28 UTC) and reported them in a comment on issue #364 (10:41 UTC). This work reached the same two keys about fourteen hours later (the test on part 4 ran at 23:24 CET the same day). Its working notes record a check of this repository's targets and catalogue only, where the 4 June key was not yet recorded; the issue comment was found on 12 Nov 2026, while this pull request was prepared. What this folder adds to his result:

- an independent transcription of all five parts, made from the NARA images on 28 Oct 2026, before any key was known (`frozen/T863-867.txt`), including part 5, whose letter shapes Harumi-Matsuba fixed after decryption (his issue comment says so);
- the key search on parts 1-2 only, and one pre-registered test of the frozen keys on part 4, held out (`frozen/`);
- a check on the images of the doubtful letters (12 Nov 2026) and a reading with the doubtful words marked.

The K2 search uses the idea of Harumi-Matsuba's `kpb.c` (public in his repository since 9 Nov 2026): after undoing the second key, neighbouring letters are plaintext letters k1 apart, whatever the first key. `solver/kpw.c` is a separate implementation of that idea; its first line still carries the name kpb.

Comparison with his transcription (`data/ciphertext_0863_0867.txt` in his repository), letter by letter over 953 letters: 7 differences. Part 1 group 34 letter 1 (his m, ours n: IMMENDINGEN), part 2 group 4 letter 5 (his u, ours n: FUENFEINS), part 4 group 5 letter 4 (his e, ours c: SCIT), and in part 5 groups 9 and 31 (his n, ours m) and groups 12 and 36 (his q, ours g): four letters where he wrote the letter the decryption needs and the images leave m/n and g/q open. The decryptions are otherwise identical.

## The document

NARA RG 242, T405 roll 9 (NAID 332033680), frames 0863-0867: a hand-written radio form (Funkspruch), "5 Tle", in five parts of 179, 190, 194, 186 and 204 letters (the stated lengths include the indicator group), one part per frame; parts 1-4 in ink (hand 1), part 5 in pencil (hand 2). The form carries no date. It follows frame 0862, a typed teleprinter message (Fernschreiben, "Geheime Kommandosache", file 249/6) of Flugabwehrkommando Schwarzwald Ic to Luftgaukommando VII Ia op 2, copies to Luftgaukommando VII Abt. Qu/1 and to the Flak liaison officer at AOK 7, dated 4 June 1940, 11.45; the decryption is that text. The NARA images are US public domain (https://catalog.archives.gov/id/332033680; frame 0863: https://catalog.archives.gov/medialz/dc-metro/rg-242/7794463/T405/T405-0009/T405-0009-00863.tif, the others by number). No image is included here.

## Transcription (`transcription.txt`)

Transcribed from the NARA images by a Claude Opus agent on 28 Oct 2026 (`frozen/T863-867.txt`, the version the key search and the test used). In hand 1, u carries a hook and n has the same shape without it, the cause of most misreadings. Hand 2 has two letter forms that the first transcription coded N and R; the key shows them to be r and x, and `transcription.txt` writes them so. Six letters were corrected on the images on 12 Nov 2026: part 1, group 2 letter 3 (u to n), group 32 letter 1 (m to n), group 34 letter 1 (m to n); part 5, group 13 letter 5 (z to r), group 23 letter 5 (a to o), group 39 letter 5 (v to r). Every part has the stated number of letters.

## The key (`key_0604.txt`)

Double columnar transposition with irregular grids: the plaintext is written in rows of 19 under K1 and read off by columns in key order, the result written in rows of 22 under K2 and read off the same way, and an indicator group is put in front; each part is enciphered on its own.

- K1 (19): 9 14 17 1 12 6 18 3 16 10 4 8 19 13 7 2 11 15 5
- K2 (22): 19 22 9 17 1 12 7 16 21 13 10 20 4 18 2 15 6 3 8 11 5 14

Indicator groups: rlehs, jktqd, hyvxz, abexb, abhvy. The plaintext follows the conventions of the 17 May messages (`../contributor_reading.md`): X between words, CH written Q, numbers spelled digit by digit (ZWO), ROEM, STRIQ, KLAMMER.

## How the key was found (`solver/`)

1. Crib: the plaintext of parts 1 and 2 taken from frame 0862 with the 17 May conventions and fitted to the letter count of each part, which a transposition keeps (JUNI, since parts 1 and 5 have a j; ZWO; "Sankt"). The fit was approximate (`solver/in12b.txt`).
2. K2 (`solver/kpw.c`, `grid.sh`): simulated annealing on K2 for every pair of lengths k1 = 15-30, k2 = 15-32, on parts 1 and 2, and the same run on the shuffled plaintext as control. (19, 22) stood out alone: 0.267 against 0.093, a margin of 0.174 where the margins have mean 0.004 and standard deviation 0.019 (`solver/ana.py`). Four independent runs gave the same K2.
3. K1 (`solver/k1s.c`): simulated annealing on German quadgrams with K2 fixed, over parts 1, 2, 3 and 5, which then decrypt to the text of frame 0862.
4. Test on part 4, held out (`frozen/`): keys, scorer, controls and pass rule written down and hashed before part 4 was decrypted; one run. German quadgrams -4.993 per letter against -6.643 for the best of 400 controls (200 random key pairs of lengths 19 and 22, and the frozen keys on 200 shuffles of the ciphertext); agreement with the plaintext predicted from frame 0862 0.989 against 0.227. Pass on all three conditions. Declared deviation: before the protocol was frozen, the raw NARA OCR of frame 0866 (about 110 characters of part 4) was printed by an inspection command; it was not analysed, and the key search used parts 1 and 2 only.

Before that, on 28 Oct 2026, a search without a crib (joint annealing of both keys on quadgrams, and scores of the IDP kind) failed on synthetic messages of the same lengths and was not run on the real one. A request to another model (Claude Fable 5.2) on 11 Nov 2026 was refused and gave nothing.

## What it says (`reading.md`, `translation.md`)

On 3 June 1940, to protect army unloadings, seven Flak units of Flugabwehrkommando Schwarzwald moved into position at railway stations and towns of the Black Forest and reported ready to fire: II./2./942 from Immendingen station to Sankt Georgen station (19.45), II. 2./851 from Bodersweier to Triberg (20.30), II./4./251 from Hattingen to Peterzell (20.45), II./10./351 from Ettlingen to Haslach (20.45), I./Light Reserve Flak Battery 453 from Horb to Marbach (21.00), I./3./851 from Ichenheim to Hornberg station (21.00) and 4./321 (Eis) from Hüfingen to Villingen (4 June, 04.35). Signed "Flugabw.Kdo. Ic Nr. F 225/40 g.Kdos.". The radio text differs from the teleprinter copy only in spelling: Sankt for St., zehn for 10, ditto marks written out, and a file number that the teleprinter copy does not have.

Count: 129 words, 124 certain, 5 probable (SEIT in part 4; NAQ, JUNI, NR, STRIQ in part 5), none restored or unresolved. The text was known from frame 0862; what is new is the key of 4 June 1940.

## Count

| Part | Frame | Words | Certain | Probable |
|---|---|---|---|---|
| 1 | 0863 | 27 | 27 | 0 |
| 2 | 0864 | 25 | 25 | 0 |
| 3 | 0865 | 25 | 25 | 0 |
| 4 | 0866 | 24 | 23 | 1 (SEIT) |
| 5 | 0867 | 28 | 24 | 4 (NAQ, JUNI, NR, STRIQ) |
| all | | 129 | 124 | 5 |

Words are counted on the decryption as divided in `decryption.txt` (X not counted; a spelled number such as
NEUNVIERZWO is one word). No word is restored or unresolved: 129 of 129 words read as sense. The first count (11 Nov
2026) had 11 probable words; on 12 Nov 2026 six of the doubtful letters were checked on the images and corrected
in the transcription (see Transcription), which leaves the five above.

## Differences from the teleprinter copy (frame 0862)

The same text is on frame 0862, a teleprinter message (Fernschreiben) of the same command, dated 4 June 1940 11.45,
to Luftgaukommando VII Ia op 2, copies to Luftgaukommando VII Abt. Qu/1 and the Flak liaison officer at AOK 7. The
radio text writes "Sankt" for "St.", "zehn" for 10 in II./10./351, "leichte Reserve Flakbattr." for "Le.Res.Flakbatt.",
writes out "feuerbereit" where the teleprinter copy has ditto marks, and signs "Flugabw.Kdo. Ic Nr. F 225/40 g.Kdos."
(the file number is not on the teleprinter copy, and "Schwarzwald" is left out). In part 2 the sender wrote ROEM ZWO
without an X, and in part 5 NRO for NR.

## Remaining gaps

- Five probable words in parts 4 and 5 rest on doubtful letters of the transcription: part 5 group 12 letter 3 and group 36 letter 2 (g or q), part 5 group 9 letter 5 and group 31 letter 1 (m or n), checked on the images and still ambiguous; part 4 group 5 letter 4 (c for e in SEIT), not yet checked on the image - blocker: illegible; g and q, m and n are not distinct in these hands
- The other Funksprüche of the roll, about 21 messages of other days in May 1940, each with its own key, are not deciphered. A first attempt on six of them (frames 889-894, 978-985, 1039-1040, 1049-1050, 1056-1057, 1113-1114, transcribed from the images on 11-12 Nov 2026) with the same method found no key: the cribs taken from the NARA OCR of the teleprinter copies were too inexact, and the 17 May and 4 June keys do not apply. Correction to a working list: frames 1025-1027 are the 17 May message already in this target - blocker: no-key-material; the next step is an exact crib read from the image of each teleprinter copy
- How the key follows from the indicator group - blocker: no-key-material; no rule for 1940 is known (the 1939 key card on frame 350 lists Kenngruppen only)

## Escalation

- [x] siblings: the 17 May 1940 messages gave the conventions; six other messages of the roll transcribed and attacked, no key found (Remaining gaps)
- [x] clear-pages: the teleprinter copy on frame 0862 is the plaintext beside the ciphertext and was the crib
- [x] known-keys: the 1939 key card (frame 350) and the 17 May 1940 keys tried; daily keys, they do not apply
- [x] print: this repository searched (targets, catalogue, issues and pull requests, 12 Nov 2026): Harumi-Matsuba's comment on issue #364 has the same key (see Priority); nothing else
- [x] key-rebuild: both keys recovered from the crib on parts 1-2 and tested on part 4, held out
- [n/a] retry: all five parts decrypt; what is left is five letters of the transcription

## Files

| File | Content |
|---|---|
| `transcription.txt` | the five parts in five-letter groups, after the checks on the images of 12 Nov 2026 |
| `decryption.txt` | part by part: ciphertext, decryption, word division, notes on the doubtful letters |
| `reading.md`, `translation.md` | the German text as sentences; the English translation |
| `key_0604.txt` | the two keys of 4 June 1940 |
| `solver/` | `decrypt.py`, the K2 and K1 searches, their inputs and the search grids |
| `frozen/` | the pre-registered test on part 4: protocol, hashes, scorer, first transcription, output |

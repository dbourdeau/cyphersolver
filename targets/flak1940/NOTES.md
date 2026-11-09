# flak1940: radio messages of Flugabwehrkommando Schwarzwald, 17 May 1940, and the key of the day (NARA RG 242, T405 roll 9)

Status: read (9 Nov 2026). Contributed by Harumi-Matsuba (issue #364; repository `Harumi-Matsuba/flak1940-public`, commit a181cd7, per the contributor's licence file), who worked with Anthropic Claude (Claude Fable 5.1) and used OpenAI Codex as a blind second reader and Claude Sonnet for image judgements. **No human has checked the transcriptions**, and the project has not seen the images (NARA is not reachable from here); what the project checked is the keys against the contributor's own transcriptions (`VERIFICATION.md`).

## The documents

NARA RG 242, microfilm publication T405 "German Air Force Records: Luftgaukommandos, Flak, Deutsche Luftwaffenmission in Rumänien", roll 9 (NAID 332033680). Two radio messages of 17 May 1940, both in five-letter groups of a double columnar transposition:

- Frame 0993: a teleprinter copy (SMU 0113 17/5 1500, "G-KDOS- 4 TEILE") of a message from Luftgaukommando VII to Flugabwehrkommando Schwarzwald, four parts of 179, 178, 167 and 130 letters. The recipient's hand-written fair copy is on frames 0994-0995.
- Frames 1025-1027: a hand-written radio form of a message sent by Flugabwehrkommando Schwarzwald Ic, two parts of 205 and 194 letters (frame 1026 is the back of the sheet with the last group); its teleprinter original is on frame 1024.

Catalogue 704 listed the reel as a test bed of Luftwaffe radio traffic, daily-keyed double transposition, with the 1939 key card at frame 350 and clear teleprinter messages on neighbouring frames as possible cribs. The first five-letter group of each part is the indicator group and is not text; without them the two messages have 634 and 389 letters, 1,023 in all.

`ciphertext_0993.txt` and `ciphertext_1025_1027.txt` are the contributor's transcriptions, `plaintext.txt` the letter strings his keys give, `key.txt` the two keys, `contributor_reading.md` the division into words and the spelling conventions, `contributor_method.md`, `contributor_open.md`, `contributor_prior_check.md`, `contributor_readme.md` and `contributor_sources.md` his documents.

## The cipher

A double columnar transposition: the plaintext is written in rows in a grid 24 columns wide, read off column by column in the order of the key numbers, and the result written in a grid 28 wide and read off the same way. The keys for 17 May 1940 (`key.txt`) are 15 12 20 8 17 4 22 9 19 2 16 11 5 21 10 3 14 24 7 13 1 6 18 23 and 24 17 10 21 6 18 27 1 22 16 7 25 11 2 20 23 4 8 13 19 28 14 5 9 15 3 26 12. The second key is 28 long, outside the 15-25 range suggested by the catalogue page. In the plaintext, X separates words and names, CH is written Q, numbers are spelled digit by digit, brackets are KLAMMER, the slash STRIQ and roman numerals follow ROEM (`contributor_reading.md`).

## How the keys were found

The contributor fixed the plaintext of parts 3 and 4 of frame 0993 from the recipient's fair copy (frames 0994-0995) by fitting spellings to the letter counts (a transposition does not change them), then ran two known-plaintext searches of his own (`src/kpa.c`, `src/kpb.c`, not in this folder) that gave the key lengths and the keys, from part 4 of frame 0993. The tools were first tested on the 1939 exercise message and its key card (frames 349-350). The final rotation of the columns was confirmed by parts 1, 2 and 4 becoming readable; parts 1 and 2 and the whole of frames 1025-1027 were not used and decrypt as they stand. In part 3, lines 2 and 3 (50 letters each) are interchanged on the page, and letter 113 is read T.

## What they say

Frame 0993: Flakgruppe Friedrichshafen hands over to Flugabwehrkommando Schwarzwald the 1st and 3rd platoons of the 3rd battery of Reserve Light Flak Battalion 932 (Herbertingen), to be transported by the Flugabwehrkommando and employed as arranged by telephone, and employs the 3rd platoon of Anti-aircraft Machine-gun Reserve Company 304 (Sigmaringen) at the protected object Herbertingen; the new positions and readiness to fire are to be reported. Frames 1025-1027: on 16 May 1940 the 1st platoon of 2./932 (2 cm) of Flakgruppe Friedrichshafen was assigned to Flugabwehrkommando Schwarzwald; the platoon has been ready to fire since 22.30 hrs in position 3031 west of Tüllingen and is subordinated to Battalion 942. The plaintexts survive in the same file in their contemporary form (the fair copy of 0993 and the teleprinter message on frame 1024), so no previously unknown text was read; what is new is the key of the day.

## Remaining gaps

- Seven of the 1,023 letters are wrong as plaintext (BATBERIE, TRANSPORTIWRT, FERNNUENDLIQER, the X and Q of part 4 of frame 0993, VIENULL and the final H of frame 1027); the contributor takes five of them for errors of the sender or the relay, since they are in the typed cipher text, and has no way to check - blocker: illegible; the typed text is the only witness here and the hand-written ones (e or R, h or k) cannot be settled from the handwriting
- A human check of both transcriptions against the NARA frame images - blocker: needs-physical-access; NARA is not reachable from the project
- How the key follows from the indicator group (the first five letters of each part) - blocker: no-key-material; the 1939 key card lists four three-letter Kenngruppen but no rule for this day is known

## Escalation

- [x] siblings: the recipient's fair copy (frames 0994-0995), the teleprinter original of the second message (frame 1024) and the 1939 exercise message with its key card (frames 349-350) used; the other days of the reel (9 April, 3, 8, 16 and 20 May, 4 June and others) are other keys and were not read
- [x] clear-pages: the fair copy and the teleprinter original are the plaintexts beside the ciphertext, and were used for the key
- [x] known-keys: the 1939 key card gave the system and tested the tools; its keys (21 and 19 long) do not apply to 1940
- [x] print: the contributor searched this ledger (all issues and pull requests at the time), Cryptiana, Cryptoole, Schmeh's blog, GitHub and the web (`contributor_prior_check.md`): nothing on the key or the messages
- [x] key-rebuild: the keys were recovered by known-plaintext search from part 4 and confirmed on the other five parts
- [n/a] retry: all parts decrypt; what is left is the transcription of a few letters

## Files

| File | Content |
|---|---|
| `ciphertext_0993.txt`, `ciphertext_1025_1027.txt` | the contributor's transcriptions, five-letter groups |
| `plaintext.txt` | the letter strings the keys give, six parts |
| `key.txt` | the two keys of 17 May 1940 |
| `contributor_*.md` | the contributor's reading, method, open points, prior-art search, README and sources |
| `VERIFICATION.md` | what the project re-checked |
| `profile.json` | the target profile |

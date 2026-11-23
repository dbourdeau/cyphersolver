# NARA T405 sweep (2026-11-22)

Run by Jacob Houtrouw (TheLightningCount) with Claude (Anthropic), model `claude-opus-5-5`, in two sessions: the survey and the reading of the frames on 13 Nov 2026, and the duplicate and prior-art checks, this folder and a check of two frames at full size on 22 and 23 Nov 2026. It is the lead asked for on #542 on 14 Nov 2026 (https://github.com/dbourdeau/cyphersolver/issues/542#issuecomment-6879298673).

## Routes
- **NARA's catalogue search** for the file units of T405, "Number 1" to "Number 64": 63 found. Not returned: 19, 28 (1 of 2), 50, 58 (1 of 2) and 60 (1 of 2).
- **NARA's page text,** its own machine reading of the frames, from `catalog.archives.gov/proxy/extractedText/<NAID>`, fetched once for each unit on 13 Nov 2026.
- **The frame images,** from `catalog.archives.gov/medialz/dc-metro/rg-242/7794463/T405/...`, free and without a login.
- Nothing blocked.

## How it was searched
There were no search terms. The page text was filtered for runs of five-letter groups, the form of the 1939-40 traffic on roll 9 (catalogue entry 704). By the survey's note, on roll 9, where 24 frame ranges hold cipher groups, a filter of at least 10 five-letter tokens making up over 35% of a frame's tokens finds all 24.
- **Rolls 1 to 31** (31 units: roll 12 in two parts, of roll 28 only its second part, and no roll 19): the filter ran frame by frame. Besides roll 9, it found two frames of roll 1 (below) and a few frames on rolls 2, 5, 16 and 18. Those hold lists of ranks, names, abbreviations and place names, not cipher.
- **Rolls 32 to 64** (32 units): the survey's output holds one run for each, without frame numbers, so the filter did not run frame by frame on them, and why is not known. **They are not searched.**
- **Roll 1, frames 1048-1100,** were then opened as images: all 53 on a contact sheet, and frames 1056, 1093 and 1094 row by row at 0.8 of full size, with doubtful letters zoomed to 2.0.
- **Frames 1056 and 1094 were opened again at full size on 23 Nov 2026** (3632 px wide, 300 dpi) and looked over for any writing, in the margins and between the rows. There is none between the rows. The margins hold the registry's hand only: the documents' numbers and days, the receipt stamps' entries, pencilled folio numbers, two short marks, and on frame 1094 the journal number. None of it is a word or a group of letters.

## Finds
Three typed exercise messages ("Uebungsspruch") of the Reichswehr in five-letter groups, in the files of the 3. (Preußische) Fahrabteilung, Berlin-Lankwitz, 1933:
1. **Frame 1056** (a lead, row 1): from the 3. Division, Abt. Stonach, Berlin, 18 November 1933. Received on 24.11.33. 86 letters. No decipherment on the frame, read row by row at 0.8 of full size and looked over at full size. The other frames of 1048-1100, apart from 1093 and 1094, were seen on a contact sheet at 0.04 of full size, and those of 1054-1058, 1092, 1095 and 1096 also in NARA's page text; none of them was read.
2. **Frame 1094** (a lead, row 2): from the 3. Division, Stonach, Berlin, 22 July 1933. Received on 25.7.33. 108 letters. No decipherment on the frame, read row by row at 0.8 of full size and looked over at full size. A handwritten note on frame 1093 headed "aufgenommen" may be its decipherment, but as we read it the note does not fit this text's letters (row 2, `status`).
3. **Frame 1093** (left out): the Fahrabteilung's typed draft answer ("Entwurf") of July 1933 to frame 1094's message, 112 letters. Below the signature a handwritten note headed "Befördert" gives its plain text. As we read the note, its visible words account for 94 of the 112 letters, all of them among the message's. The 18 left would be a word that the folio number covers, and no German word we tried fits them. A cipher filed with its decipherment is not a lead (the sweep brief), so it has no row. It is the reason both rows are class A: a sibling deciphered in the same file. On 14 Nov 2026 a sealed plan tested single and double columnar transposition on frame 1093, with its plain text as a crib, and missed on every run. Nothing was run on frames 1056 and 1094.

**Hand ciphers, not the Enigma.** Frames 1058 and 1092 are lists of key documents issued, among them "Heeres-M-Schlüssel" Nr. 253 and 261 (NARA's page text). The messages are not machine ciphers. Their letters keep the frequencies of German, with an index of coincidence of 0.070 and 0.072 for the two leads against about 0.038 for a machine cipher, and frame 1093's letters fit its plain text. The lists name key documents and hold no key, so they are not key leads.

No person has checked the reading of the groups or of the handwritten notes.

## Duplicates and prior art (22 Nov 2026)
- **`known.py`,** at main `4525b440`: "T405" finds only catalogue entry 704 (roll 9). No hits for 332024052, Fahrabteilung, Lankwitz, Uebungsspruch, Übungsspruch, bungsspruch, Stonach, Reichswehr, Reichsheer, Geheimschriftverkehr, or the first group of each message.
- **DECODE** keyword search: Reichswehr, Lankwitz, Fahrabteilung, Übungsspruch: no records.
- **Tomokiyo,** the snapshot `unsolved.htm`: nothing (its one "1933" is a date in a citation).
- **Lasry, HistoCrypt and the web:** four searches on 22 Nov: the unit with "Übungsspruch"; "Übungsspruch" with Doppelwürfel, Würfelverfahren or Geheimschrift; Reichswehr hand ciphers of 1933 with Lasry or HistoCrypt; and T405 roll 1. Searches of 13 Nov covered the 1933 exercise messages, the Fahrabteilung at Lankwitz and the Reichswehr's hand ciphers (Würfel, Doppelwürfel). None found anything on these messages, and none found a public description of the Reichsheer's hand system of 1933. Bundesarchiv RH 57/72 (Geheimschriftwesen, 1934-35) holds "ein Heft zu den Geheimschlüsseln im Reichsheer" by its catalogue entry. It was not opened.
- **No edition** of these files is known to us.

## What is left
- Rolls 32 to 64, and the five units the catalogue search did not return.
- On 30 of the 31 units of rolls 1 to 31, the run without frame numbers that ends each in the survey's output. What it holds is not known.
- Every roll as images, apart from roll 1, frames 1048-1100.
- Traffic in figures or codes: the filter sees only five-letter groups.
- The handwritten notes on frame 1093, which no person has read.
- The answer named on frame 1055, not seen on frames 1048-1100.

## Files
- `candidates.json`: the two leads, each reserved for Jacob Houtrouw.
- The survey's output of 13 Nov is in the contributor's files; its script is not.

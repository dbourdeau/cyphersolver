# NOTE · catalogue 698 · roll 302 around the message, read page by page for the Bureau's typed plaintext · v1-M · 18 Nov 2026

*Provenance:*
- *The model's words throughout (M). J.'s words: none.*
- *Model on record: `claude-opus-5-5` (session `eea13873`), read from the log. Not seen by the desk.*
- *J.'s act: his ruling by box at 01:14:46.926Z, "Look for the typed text" (chain entry 311).*
- *Made after the word rule's output was stamped, so these frames were open by the plan's §5.*

## Result
**No typed plaintext of the message, in Spanish or in English, stands on frames 30 to 70 of M1085 roll 302.** These are the 41 frames around the message: the message itself is frame 39 and its second copy frame 58, and the strip is frame 42 and its second copy frame 59.

The forecast "The Bureau's 1917 text is found on the roll" (0.25) **stays open.** The rest of the roll was not read, nor rolls 301 and 308.

## Weaknesses first
1. **Only frames 30 to 70 were read.** The case runs to about frame 250 of roll 302, and over the end of roll 301 (S1, lines 15 to 17). Its companion case OG 3410 is on roll 308. None of that was read here.
2. **The pages were read by eye at 0.6 of full size.** Several are faint: 34, 35, 37, 38, 55 and 63.
   - A short typed block in Spanish would very likely have been seen.
   - A single quoted word inside an English sentence on a faint page could have been missed.
3. **No OCR could be had.**
   - The frames are JPEGs of 992 by 1,328 pixels or so. NARA serves no larger copy of this roll: the TIFF address gives a 5,454-byte page.
   - Tesseract read nothing from them, as they are or enlarged three times.
   - NARA's catalogue API, asked once without a key, returned its web page. It was not tried another way.

## What the frames hold

| Frames | What |
|---|---|
| 30 | the last page of another case |
| 31, 32, 33 | the film's title card, the reel card (46), "OG-2889 cont'd" |
| 34 to 38 | letters (Barnes; the U.S. Attorney at Houston, Green) of early March 1917, faint |
| 39, 42 | the message and the key strip |
| 40, 41 | the case's cover card (#2889) and its name card |
| 43 to 46, 48, 51 to 54, 56, 64 to 68 | E. E. Swift's daily reports, 9 to 16 March 1917, "In Re Pro German Activities": Bolner's visits, the dictograph, the attack on Olga in her hotel room, her move to the Hotel Travelers |
| 47, 62 | E. T. Needham's reports of 12 and 14 March, the second giving Franz Visser's statement |
| 49 | Barnes to Bielaski, 9 March, enclosing a letter of 23 Feb 1917 from Hugo Horotwischka to E. W. Smith (the letter itself is not on these frames) |
| 50, 57, 63 | telegrams of 12 and 13 March (Barnes; Green) |
| 55, 69, 70 | Department of Justice transmittals and letters, 15 and 16 March |
| 58, 59 | the second photostats of the message and the strip |
| 60, 61 | a card "2889", and T. W. Gregory's note of 16 March asking for "full statement of Visser woman's account" |

None of them quotes the message in Spanish, translates it, or speaks of its reading. Frame 68 holds the one translation on these pages, and it is of something else: Olga's own note of a telephone call with Bolner, "Translated into English her note reads".

## What is next, if anyone wants it
- **The rest of roll 302, from frame 71 on, and frames 1 to 29.**
- **OG 3410 on roll 308, frames 1988 to 2067.** Swift's quotation of the word, which S1 cites, comes from that case.

That is J.'s call. Every fetch is in `visser698/FETCH_visser698_roll302_2026-11-18_0117Z.tsv`.

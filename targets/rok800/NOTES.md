# Rök runestone (Ög 136), Östergötland, c. 800: the cipher runes

Status: closed, cipher keys checked 9 Nov 2026; the readings were already published (Bugge 1878, Wessén 1958, Rundata Ög 136).

## The document

The Rök runestone, 28 rows of runes on a granite block at Rök church, Östergötland, made by Varinn for his dead son
Vámóðr. Most of it is in the 16 short-twig runes of the Younger Futhark. From the Ingold passage on the carver mixes in
Elder Futhark and cipher runes. No image of the stone was read here: the rune string is the published Unicode
transcription (`transcription.txt`, from English Wikipedia, CC BY-SA 4.0, after Rundata Ög 136), the resolved
transliteration is `decryption.txt`, the normalisation `reading_old_east_norse.txt` and the translation
`translation_en.txt`.

## Prior work

Sophus Bugge is credited with the first reading of the cipher runes in 1878 (not consulted here); Elias Wessén's *Runstenen vid Rök* (1958) is the standard edition;
Rundata Ög 136 prints the resolved text. The cipher runes are not an open problem. The meaning is: the 2020s
proposals (Ragnarök and a sixth-century climate crisis) are contested. Found before the attempt (web search, 9 Nov 2026).

## What was done here (`decode_layers.py`, output in `layers_report.txt`)

1. **Coordinate cipher `[a:b]`.** Aett a counted from the right over the rows `fuþąrk / hniast / tbmlʀ`, position b.
   All 11 distinct codes on the stone agree with the stone's own resolution. The coordinate-only lines read
   `ul ni ruþʀ sibi uiauari` and `sakum mukmini þur`.
2. **Shift cipher.** All 16 shifts tried on the 24-rune string, scored by 4-grams shared with the stone's own
   cleartext: shift +1 (each written rune is the previous rune of the 16-rune row) wins and gives
   `sakum mukmini uaim si burin niþ`. The 8-rune string `rhfþrhis` is too short to search; the same shift gives `knuą knat`.
3. **Elder Futhark passage (47 runes).** Not a shift. Crib `sakum mukmini þat`, which stands in the cleartext part of
   the same stone, fixes 11 runes; unchanged runes read as themselves; the remaining 33 read
   `huaʀ i k/gult/d k/ga uaʀi k/gult/d int/d t/d k/guąnaʀ husli` (hwar Inguldinga wari guldin at kwanar husli).
   The Elder row merges k/g, t/d and has three signs for i; that is the orthography, not an ambiguity in the key.
4. Main text glyph values against the published transliteration: 98.84% similarity.

Nothing here is a new reading. What was found here: only the shift key was searched for; the coordinate table and the Elder crib are the published resolution, tested against the transcription, which carries the resolutions it is compared with.

## Remaining gaps
- line beginning `nuk m--- [m]-- alu`, damaged part - blocker: illegible; the runes are lost on the stone, no key can restore them
- Elder passage k/g and t/d spelling - blocker: no-key-material; the Younger-futhark script has one sign for each pair, so the stone itself does not say

## Escalation
- [x] siblings: no sibling inscription uses the same cipher runes
- [x] clear-pages: Rundata Ög 136 prints the resolved text; used for comparison only
- [x] known-keys: Bugge/Wessén keys reproduced for the three layers
- [x] print: Rundata, Wikipedia, Uppsala University news (2022)
- [n/a] key-rebuild: the keys checked above need no extension
- [n/a] retry: no unread cipher group left apart from lost runes

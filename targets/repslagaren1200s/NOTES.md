# Catalogue 3890 · Repslagaren cattle bone

**Method: not solved. Extent: none (text not read).** The ten positions on face B yield no established word. Three shapes have published rune values. No complete decipherment surfaced in the sources below.

## Object and witnesses

Kulturen, Lund, KM 61277:331 (DR EM85;460A, SkL 30, Lund-benstykke 8). The bone is a process from a cattle lumbar vertebra, excavated in 1969 in plot 22. Its archaeological layer was provisionally dated to the thirteenth century. The carver and language are unknown.

The concave face A and convex face B each carry one line. Both Larsen photographs show the tapering end to the right. A starts with a two-armed t, B with crossed strokes and ends with a double tier of arms. These landmarks agree with the drawing reproduced by Nordby. B starts closer to the blunt end than A in the photographs. Position here means ordinal place on each face, not two cuts lying back to back.

- [Jansson, “Nytt runfynd i Lund,” pp. 111–112](https://www.kulturen.com/wp-content/uploads/2019/06/kulturens-arsbok-1970-tema-textil.pdf). The supplied download returned 404. The drawing was examined in Nordby's reproduction.
- [Svärdström, “Runfynd 1969,” fig. 8, p. 312](https://www.arild-hauge.com/fornvannen.se/1970_301-Runfynd%201969.pdf#page=12). Contemporary photograph credited to Kulturen.
- Lennart Larsen, Nationalmuseet photographs, [concave face](https://www.arild-hauge.com/runer.ku.dk/DREM85%3B460A_SkL_30_LUND.jpg) and [convex face](https://www.arild-hauge.com/runer.ku.dk/DREM85%3B460A_SkL_30_LUND-1.jpg). The [image index](https://www.arild-hauge.com/DK_SkL_Lund.htm) credits these to Larsen under CC BY-SA 4.0. Images are linked only.
- [Nordby, *Lønnruner*, pp. 288–289](https://www.arild-hauge.com/PDF/Lonnruner-Kryptografi_i_runeinnskrifter_fra_vikingtid_og_middelalder-K.Jonas_Nordby.pdf#page=289). Nordby reports Moltke's identification as secret runes, discusses shared-staff and branch-count readings, and suggests the possibility of the same text on both faces.
- [Runor, DR EM85;460A](https://runor.raa.se/inscription?id=0feb0e14-f70c-48ba-b555-0cdc4d41ac63). Both translation fields are blank. Searches under the inventory number, signum and findspot, including indexed Cryptiana and DECODE pages, located no clear copy, key sheet or deciphered parallel. Private DECODE attachments were not inspected.

## Transcription and attempted reading

| Face, line | Signs in edition order | Published transliteration | Tokens in established words |
|---|---|---|---|
| A, 1 | t u t a þ o r e r e | tutaþorere | 0/10 |
| B, 1 | B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 | æ????ra??? | 0/10 |

[Sign inventory and shape descriptions](transcription.tsv) · [Position-by-position reading](reading.txt) · [Reproduce checks with Python](check.py). The B identifiers denote the ten visually distinguishable whole forms. Their constituent strokes may recur. No code-group values, nulls, word divisions or English translation have been established. The three ordinary-looking forms on B give 3/10 graphic identifications and 0/10 tokens in sense. The number of missing words is unknown.

## Testing the opposite face as a crib

A repeats t in positions 1 and 3, r in 7 and 9, and e in 8 and 10. B has different drawings at every one of those pairs. Reversing A moves its repeated pairs to 1/3, 2/4 and 8/10, again with different B shapes. This rules out copying A by a fixed one-to-one substitution of whole forms in either order. Reading B01/B06/B07 with their ordinary values gives æ/r/a. At those places A gives t/o/r forward and e/þ/a backward. A shared message would require a different explanation, such as variable spellings or multiple signs per value.

## Testing branch counts

For a conventional two-coordinate rune, the branches give the number of the rune group and the position within it. B07 has a staff and a single left branch. Its left/right counts are (1,0), so neither assignment gives two positive coordinates. Moving a lone branch into a high or low category also leaves one category empty. B10 has two left and two right arms. In the usual three groups with hnias in the middle, (2,2) gives n, which matches neither the final e of A nor the initial t at the opposite end. Swapping the two coordinates leaves (2,2) unchanged.

The script checks all six permutations of the three groups, both side assignments and both within-group directions. Its ten-rune positive control recovers the supplied text among the possible decodes. A single invalid sign suffices to reject a uniform positive-coordinate rule across B. This does not decide a mixed ordinary/branch system or rules with an implicit coordinate. The control tests implementation only. Ten different whole signs give an unrestricted substitution no repeated-symbol constraint to score. The shared language models cannot select a key on that evidence, and the language itself is undetermined.

Allow B01, B06 and B07 to be ordinary runes and retain branch counts only for B10. The same enumeration gives B10 the possible values a, b, l, n, r or u. Neither endpoint of A occurs in this set, even allowing the undotted i-rune for e. This weakens the same-text crib under that mixed convention, independently of the faint strokes on B02 and B08.

## Transcription doubts

- B02, B08 and B09 contain crossing or short cuts. The photographs support the overall forms. Which cuts the carver intended as separate branches is unresolved.
- B03 and B06 have returning curves. A loop might be one element or attach to the staff at two counted points. B04 and B05 share a paired head but differ below it. No decomposition into component runes could be checked against a contemporary key.
- B01, B06 and B07 carry the published graphic values æ, r and a. Their cipher values remain open. B10 clearly has two tiers, but the convention for counting them is unknown.

## Remaining gaps

All ten positions remain semantically open. A dated parallel using one of the compound signs with an ordinary-rune gloss would distinguish possible component readings. Better lighting could settle faint cuts on B02 and B08, although even a perfect tracing would still require evidence for how the signs encode language.

Submitted under [dbourdeau](https://github.com/dbourdeau). Research and checks by OpenAI Codex (GPT-6), using web research, PyMuPDF and Python.

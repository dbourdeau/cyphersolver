# METHOD: 1623 test with the 1634-derived key (frozen before the decode)

Frozen inputs: frozen/T1634_transcription.txt, frozen/K1634_key.tsv (frozen earlier, FREEZE_1634.txt),
frozen/T1623_transcription.txt, frozen/BLIND_1079_0263.txt, scripts/score.py (md5 in FREEZE_1623.txt).

1. Decode once: every group of the 1623 transcription (blocks A, B, C) gets the value from K1634_key.tsv; a number not in
   the key decodes as '?'. Tokens = cipher words between '/' (clear words in [ ] are not tokens). This first pass is the figure of record.
2. Coverage = groups whose number is in the key / all groups (full arithmetic).
3. Scorer (stated now): Dutch 17th-century word list from the GLOBALISE HTR of VOC inv. 1068, 1120, 1132, 1151, 1156
   (none is a source volume of these letters), types with frequency >= 2 after normalisation (lower case; y -> ij; j -> i;
   v and w -> u; letters only). A token "reads as sense" only if it has no '?' and its normalised decode is in that list.
   Score = tokens read / all tokens. Read bar: >= 65%, strict.
4. Shuffle control: 5,000 keys at seed 20261112 and 5,000 at seed 7. Each shuffled key is a random permutation of the
   frozen key's letter values over the same keyed numbers (coverage unchanged). Count shuffles scoring >= the real score.
5. Second transcription: BLIND_1079_0263.txt (block B, signed copy) aligned group by group with block B of the frozen
   transcription; alignment rate = matching groups / groups (difflib alignment).
6. Anything read after the first pass (human reading, proposed values for unkeyed numbers, emendations) is reported
   separately and listed; it does not change the figure of record.

Disclosures made before the decode:
- While reading LEAD.md (before any 1623 transcription), the HTR excerpts of 1080_0486 were mentally decoded with the 1634
  values while checking the 1634 key; the words looked like Dutch (a fleet word and a place name). So the decode of block C
  is not blind. Blocks A and B were not decoded before this freeze.
- The margins of 1079_0129 and 1079_0133 carry clear-text notes beside blocks A and B that may be abstracts of the cipher
  content ("Vier dagen naer het vertreck van d'Engelsche schepen ..."; "Int Wapen en Leyden sijn geladen ... sacken peper ...").
  They were glimpsed on the overview images, not used for transcription or key, and will be used only as an after-the-fact check.

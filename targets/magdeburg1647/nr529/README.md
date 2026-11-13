# Clear drafts in the sister volume LASA A 1 Nr. 529

Lead: Malcolm McBratney's second checker (Perplexity) pointed us to LASA A 1 Nr. 529, the envoys' draft diary (931 frames), and to frames 875 and 881. We verified it ourselves on 13 Nov 2026 (session b189). The images were fetched by plain GET from `https://recherche.landesarchiv.sachsen-anhalt.de/images//A_1/Nr_529/max/A_1__Nr_529__NNNN.jpg`. The md5 of each image is in the contributor's log; the images are not in this folder.

## What we found

| Nr. 530 slip | Nr. 529 frame (archive foliation) | heading in Nr. 529 | verdict |
|---|---|---|---|
| f.5 (training text) | 875 right (fol. 801r) | "1647 ad Diarium No. 31" | clear draft found. The enciphered passages are underlined. **Content NOT FIRST** |
| f.6 (training text) | 881 right (fol. 807r), running on to 882 left (fol. 807v) | "1647 ad Diarium No. 32" | clear draft found. **Content NOT FIRST** |
| f.7 (held out) | 882 left (fol. 807v), the same No. 32 | (continuation of No. 32) | clear draft found: "obstination", "praesertim in pari gradu constituti legati", "humeur". **Content NOT FIRST** |
| f.101 | 532 right (fol. 484r); frame 533 is a second photograph of the same page | "ad Diarium No. 54" (Dec 1646) | clear draft found: "so lang zu Münster", "als der Venetianische hierunter". **Content NOT FIRST** |
| f.104 | none | "Ad Diarium No. 22" | not found in the frames searched (see below) |
| f.102 | none | "ad Appendicem Diarii No. 22" | not found in the frames searched. The 1646 "Appendix Diarii No. 22" itself is at 352 right; we saw no matching underlined passage at overview size and did not read it in full |
| f.204 | none | "Annotata ad No. 40" | not found in the frames searched |

Frames searched (page tops on contact sheets, then the full page where a heading or underlining showed): 772-931 every frame; 516-579 every frame; 341-359 and 362 (360 and 361 failed with a connection reset and were not retried); 436-458 every frame; 300-770 every 10th frame; 5 and 10.
- Diarium No. 22 of 1647 is at 797 right (30 May 1647) and No. 23 at 801 right. We saw no "ad Diarium No. 22" sheet between them.
- Diarium No. 22 of 1646 is at 348 right and No. 23 at 354 right.
- Diarium No. 40 of 1646 is at 443 right and No. 41 at 449 right. No 40 of 1647 would fall after No. 37 (918 right, 4 Sep 1647), past the end of the volume at 931.
- Every other frame of the volume was not checked.

## What the drafts show

- **Key and transcription.** We enciphered our reading of the underlined clear text with the frozen KEY_v2 and compared it letter by letter with our frozen transcriptions (`scripts/compare_nr529.py`, output in `COMPARISON.txt`):
  - f.5 against frame 875: 43 draft words line up with 45 cipher words (two draft words each match two cipher words), and 25 of 43 are exactly equal. Letters agree for 248 of 271 = 91.51%.
  - f.6 against frames 881-882: 65 draft words line up with 67 cipher words (two draft words each match two cipher words), and 28 of 65 are exactly equal. Letters agree for 364 of 419 = 86.87%.
  - Control: with 1,000 random reciprocal keys at each of seeds 20261112 and 7, none reaches the true count. The best is 114/271 (f.5) and 186/419 (f.6).
- **Where the misses come from.** The mismatches are mostly our reading slips, which the earlier controls had already pointed to:
  - g/q in both directions: 6 on f.5 and 5 on f.6.
  - Cipher x (plain m) read as p or y, where a double mm was taken for one letter.
  - Word-final f read as n.
  - Some misses come from the cipher clerk changing the draft wording, for example "wolten" for "wollen" and "intercipiret" for "intercipirt".
- **What does not line up.** 12 cipher words of f.5 (of 57) and 34 of f.6 (of 101) have no counterpart in the draft, because the clerk's wording differs there. They are not counted.
- **Limits.** The clear text was read by one reader (Claude, b189) from the max jpg. It is not blind: the reader knew our decodes. Doubtful readings are marked '?' in the pair files and reported separately.

## Consequences

- The key (KEY_v2) was recovered from ciphertext alone on 12 Nov 2026, before we knew of these drafts. The drafts confirm it against contemporary plaintext, the fifth independent check after the Catalogus, the postscript glosses, the AMPHICTYONES worksheet and the second reader.
- f.5, f.6, f.7 and f.101 are **not first for content**: their text exists in clear in Nr. 529. The readings of these slips are kept as checks of key and transcription, not as new text.
- f.102, f.104 and f.204: no clear draft found in the frames searched. Priority for their content is not established.

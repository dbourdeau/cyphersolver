# chemnitz1631: notes

**Status: partial reading** (the outcome class in profile.json says the same). 89 cipher words in the two bare passages of images 55
and 56: 68 sure, 11 probable, 10 on values restored from the sense. Sure + probable = 79/89 = 88.8 %, under the
95 % bar, so the entry is not marked "read". Image 55: 37/40 (92.5 %); image 56: 42/49 (85.7 %).

## Key and its test
- The key (key.tsv, 79 values) comes only from the **contemporary interlinear decipherment** written at the time over
  the letter of image 57 (same writer, same file): 124 glossed words, 598 letter-group pairs (gloss57_pairs.txt).
  Credit: `contemporary`, role "key or decipherment used".
- Protocol and key frozen by SHA-256 (PREREG-3) before the held-out page was transcribed; one run (validation.txt).
- Held-out portion: image 58 left (another Chemnitz letter, 5 Nov 1631), the only Chemnitz page left in the
  volume. Images 55 and 56 were not used for testing: an earlier 23-value table had been tried on them and failed
  (coverage 59 %).
- **Measure A (frequency): indicative only.** S = 0.969 vs 0.869 for the best of 200 permuted keys, coverage 97 %,
  but on **144 groups, fewer than the 150 asked**. It is reported, not counted as a pass.
- **Measure B (glosses of 58): pass.** Agreement 95.6 % on 91 letters vs 34.1 % for the best control (threshold
  fixed in advance: at least 0.30 above the best control).
- The restored values (46=w, 29=b, 51=r, ligatures Sd=w and Sf=t, 10=c) are not in the 57 glosses; they are marked
  in key.tsv and in reading.md. 51=r also fits the near-cycle of 24 in the numbering (3, 27 = r).

## Prior work checked
- *Arkiv till upplysning om svenska krigens historia* I and II (1854-1861, archive.org OCR): no Chemnitz letter of
  1631. A web search found no edition. Not on DECODE.
- Riksarkivet "Agenten Chemnitz brev till Kungl. Maj:t" (Diplomatica Germanica, SE/RA/2106/F/XI/1392, 1631-1632)
  is not digitised and was not seen: it may hold more letters in the same system, or a key.

## Limits
- Transcription by an AI model from the full-resolution IIIF images; no human palaeographer checked it.
  Doubtful figures: 4/7, 24/27, 14, 58, 21 (listed in reading.md).
- reading_review grade B by the model; `_check_reading` scores 73 % of sentences clean (unspaced text), and
  the weak sentences were the ones read again for the review.
- The date of image 55 is not established.
- Images are not reproduced (Riksarkivet IIIF, Public Domain Mark; cited by image number).

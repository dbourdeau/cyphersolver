# Blind test of KEY_v2 on an unseen VOC letter: Batavia, 9 September 1640 (26 Nov 2026 AEST)

## Bottom line
- KEY_v2 (frozen from the 1634 glosses + 1623 context) decodes the cipher postscript of the 9 Sep 1640 letter into plain Dutch on the first pass.
- Figure of record: 9/11 tokens = 81.82% >= 65%. Shuffles 0/5,000 at seed 20261112 and 0/5,000 at seed 7 (max 3, mean 0.28).
- Coverage 55/57 groups = 96.49%. Unkeyed: 12 (once) and one ink-blotted group.
- Caution: only 11 cipher tokens (57 groups). A real pass, but a small one.
- The deciphered words are not printed in Coolhaas GM II (extract ends before the postscript). A contemporary interlinear decipherment survives in the second copy.
- Reserves: Jan 1643 letter (inv. 1141) not testable under the frozen sign convention (its unglossed copy writes '/' between every number group, so word division is lost) and it mixes a letter code; 7 Mar 1643 letter: only a glossed copy found. Neither scored.

## Selection (by rule, before any cipher value was seen)
- SELECTION_RULE.txt (md5 d4f7fd3a..., 20:35:18 UTC 25 Nov), SELECTION.txt (md5 41110b05...), SELECTION_ADDENDUM.txt (base copy), ADDENDUM2 (reserve).
- Pool: GM I-II grep (806 + 870 = 1,676 pages) and blind HTR detector over inv. 1070-1145 (76 inventories; values never printed; masked triage).
  Known pages caught by the detector: 9 of 9 (1623 and 1634 copies).
- First non-excluded candidate after 25 Dec 1623: 9 Sep 1640 (inv. 1134 scans 583 and 617). Base copy 583 (no gloss at 260 px); 617 glossed, opened after the score.
- Gloss seen before the decode: NO. Printed text seen before the decode: NO. Only the GM II heading date and archive reference (p. 101) were seen;
  the p. 101 summary ("zending van deze brief met het Engelse schip Caesar") was first read in the post-score grep.

## Freeze and decode
- frozen/FREEZE_blind.txt, Wed 25 Nov 2026 20:58:51 UTC: T1640 9b68d68b..., second pass 8819c89b..., METHOD f71a3515..., run_blind.py bcbc9d7a...,
  score.py e04f5aeb... (unchanged), KEY_v2 037b8c7a... (unchanged), image 9d31783b...
- Decoded once (run_1640_output.txt).

## Figures [measured]
- Tokens 11, groups 57 (3 + 6 + 5 + 6 + 7 + 4 + 6 + 6 + 8 + 2 + 4 = 57). Keyed 55; 55/57 = 96.49%.
- First pass: het dubbel deser copien ?rieuen gaet handen uanden schipper o? door
- Score 9/11 = 81.82%. Fails: '?rieuen' (12 unkeyed), 'o?' (blotted group).
- Shuffles: seed 20261112 0/5000 >= 9; seed 7 0/5000. Max 3 in both.
- Second pass of 583 (separate crops): 57/57 = 100%. Not blind (same transcriber, same session).

## After the score (check only, nothing changed)
- 1134_0617 interlinear gloss reads h-e-t d-u-b-b-e-l d-e-s-e-r ... over the same groups: matches the decode; over 12 the gloss has b; over 43.57 the gloss has o m.
  So 12 = b and the blotted group in 583 is 57 (= m in KEY_v2): 'brieuen', 'om'. Human reading 11/11 (post hoc, not the figure of record).
- Copy 617 writes 20 where 583 has 28 in token 2 (5 5 20 35 vs 5 5 28 35); gloss there reads 'bel'. Not collated group by group.

## Reading (normalised; cipher in [ ], letter-cipher words as LC)
Het dubbel deser, neven verscheijde [copien] van [brieven], [gaet] in [handen vanden schipper] des schips den Caesar LC(ctld Gmroodt, gloss: a name, perhaps 'John ... ') [om door] Cornelis Sybertsen pastijbacker op den nieuwen dijck tot Amsterdam LC ... te worden gelieft LC ...
English: "The duplicate of this [letter], together with various copies of letters, goes into the hands of the skipper of the ship Caesar, [name], to be [delivered] through Cornelis Sybertsen, pastry-baker on the Nieuwendijk at Amsterdam ..."
The ten or so letter-cipher words (a second, letter-for-letter system, perhaps names and a place) are not read; the 617 gloss over them is partly legible.

## Verdict
- Blind test PASSED on the figure of record (81.82% >= 65%, 0/5,000 at both seeds), on a small sample of 11 tokens.
- Same number system 1623 -> 1634 -> 1640 [derived].
- Not printed as far as checked; contemporary decipherment in the archive. PR folder prepared, not pushed: PR/targets/voc1640batavia/.

## Independent blind second reader (Fable model, isolated folder blind_reader2/, 26 Nov 2026) [measured]
Reader2 saw only the scan 583 crops. It never saw our transcription, key or results. It froze T1640_reader2.txt (md5 d31ecd94971ef97870e952224d41b179) at 21:30:51 UTC, stamped Sectigo and FreeTSA 21:30:52 GMT, manifest sha256 3ab07449b3b23753eac26bfcbbc1b596447047822d2cdc9f966cec43b0e2b20c.
Alignment (difflib, cipher groups only; the 8 numbers in reader2's file header excluded): reader2 57 groups, frozen 57 groups, 56 matching = 98.2%.
The only difference is the blotted group: frozen 0 (illegible) against reader2 "57?" (5 clear, 7 under the blot). Reader2's 57 agrees with the scan 617 interlinear gloss (m = 57), read independently.
Word division: reader2 has two word-runs over line ends with no slash, which the frozen transcription joins the same way. Separators are dots only. Same convention.
The figure of record is unchanged (9/11 = 81.82%). The second reader supports the transcription.

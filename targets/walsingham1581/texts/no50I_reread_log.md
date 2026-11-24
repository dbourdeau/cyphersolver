# Re-reading log, SP 53/11 no. 50I (23 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b37)

## Starting point

Reading audit (22 Oct): "decoded, not read" (excerpt only). The repository held Tomokiyo's numeric transcription
(`../SP53_11_50b.txt`) and his published opening clause; no reading file: before = 0.00 (excerpt 0.09 by tokens).

## 1. Is there a text already?

- DECODE R3839 re-fetched (`b37_fetch.py`, scratchpad): three images (cover f. 132, a blank/backing view, the
  enclosure f. 138); no attachment, transcription or comment. No decipherment on f. 138 or the cover.
- Neighbours: R3838 (Somer's worksheet and key for SP 53/11 no. 35, another alphabet) and R3840 (clear extracts of
  Mary's letters) were checked in Sept (NOTES); nothing for no. 50I.
- Print/scholars: Tomokiyo, cryptiana mary3.htm (re-fetched 23 Oct): still only the opening "__The beirar is domestik
  servand to the erle of shrevisbvry__ ...", the numeric transcription and the glyph key image; "some symbols remain
  to be identified". Biermann and Lasry's 2023 decipherment is unpublished. CSP Scotland vi 45 calendars only the cover.

## 2. Reading on the image: the concordance

- A crib search on the numeric labels (`b37_wals_crib.py`, `b37_wals_crib2.py`: one-to-one letters, word signs inside
  words, up to 22 nulls) found **no** placement of Tomokiyo's opening: his labels are not one value each.
- Concordance built instead by reading f. 138 glyph by glyph against the label sequence, line by line (crops of the
  DECODE image, 3567 px wide, glyphs about 35 px; scratchpad), and taking each glyph's value from Tomokiyo's key image:
  `no50I_concordance.tsv` (label, glyph, value, where checked). The opening clause comes out exactly
  (*The beirar is domestik servand to the erle of shrevisbvry*: *the* = T + HE sign, *servand* = serv + AND sign),
  which checks the method.
- Lines 1-10 checked on the image; lines 11-14 only partly (the DECODE image is low-resolution and the lines slope, so
  the crops of the last lines cut the glyphs; two attempts).
- Problems found: Tomokiyo's label 10 covers the key's B and K (s-loop and long s: *beirar* / *domestik*, *havkes*,
  *kept*); label 35 covers the g-like null and, in *mai[d]* and *sov[l][d]*, apparently the 9 of D; label 84 is the
  round P in *capitane*, *importance*, *pacqvet* (x2), *kept*; label 13 is *l* in *himself* but a W-like glyph in l. 2.
  These are look-alike merges in the transcription, not key problems.
- 20 labels stay without a value (07, 09, 39, 44, 46, 49, 58, 59, 72, 77, 79, 82, 86, 87, 89, 91, 92, 95, 97, 98),
  seven of them the key's own "unknown" signs. Context suggests 58 THE QUEEN, 87 YOUR, 95 THE, 49 OF; not adopted.

Decode: `no50I_decode.txt` (`b37_wals_dec.py`). It reads in stretches: the bearer is Shrewsbury's servant, is to pass
in a captain's caravel to buy hawks, has offered to carry the packet, "I durst vryte nothing of importance be him",
"you may sovnd and try him, and be him send me ansver", "that there be nothing aganist [58] and [95] stait [49] the
realme, and faylle not to advertis me vhitner [72] the present pacqvet ... cvm to [87] handis vel closit or not".

## 3. Alignment

Every unbracketed word of `no50I_reading.md` is a run of `no50I_decode.txt` with word division supplied; words that need
a merged-label value or an unchecked glyph are bracketed [?word].

## 4. Bar

- `b17_score.py` LANG_=en: 0.077 (1/13); HOLES=1: **0.154** (2/13). Far below 0.60.
- Look-alikes: the merged labels (10 b/k, 35 d/null, 13 l/w) touch about 10 of 562 tokens; not the obstacle.
- Reader's judgement: three sentences hold (the bearer, "I durst vryte nothing of importance be him", "You may sovnd
  and try him"), the rest break on unknown signs.

Verdict: **decoded, not read** (partial reading kept). What would finish it: (a) re-check lines 11-14 glyph by glyph on
a better image (TNA SP 53/11 f. 138 at full resolution; the DECODE copy is small), (b) identify the 20 open signs from
their contexts once every line is checked, or (c) Biermann and Lasry's plaintext (ask George Lasry).

## r2k (23 Oct 2026): lines 11-14 checked glyph by glyph

- Image: DECODE R3839 P3 (`IMG_R3839_I23203_P3.jpg`, 3567 x 2859, the full-size DECODE file; also in the main checkout
  `C:\Users\dbour\cypher\walsingham1581\`). No TNA image is freely available at a higher resolution; the DECODE copy
  read well at 3x once each sloping line was cropped on its own centre (lines 11-14 at y 725, 795, 850, 895; four
  segments per line; crops in the session scratchpad `reread/r2k/wl1*_*.jpg`, `wz11_*.jpg`).
- All 141 tokens of lines 11-14 compared with the concordance glyph (evidence added to `no50I_concordance.tsv`,
  marked r2k). Three places where Tomokiyo's label stands for another glyph (`no50I_position_corrections.tsv`):
  12:1 label 02 is the tall null stroke (as 03 at 14:22), not the crossed f; 14:14 label 53 is the oval with a bar
  (n), crossed by the f's descender, not the infinity h, which gives *vnicorne*; 13:9 label 96 is the key's unknown
  Γ-like sign, not the delta TO of 3:25 (read [?is] by sense only).
- Labels settled: 49 = the OF glyph (same as 19 at 14:11); 59 = the key's # under M (*realme*); 72 = the d-like hook of
  the key's null row (*vhitner the present*); 87 = the key's YOUR sign (*cvm to your handis*); 95 = a lone dot, the
  dot that precedes the s-hook (Tomokiyo leaves it unlabelled at 11:14-15 and elsewhere): not a sign, so *and stait*;
  58 = the key's "THE QUEEN?" sign (three bars on a stem), kept [?the Queen] since the key itself queries it.
- Still without value in these lines: 91 (circle with a dot, key unknown; also 3:4), 89, 77, 82 (key unknowns; 77 82
  close the letter), the Γ-like sign at 13:9.
- Decode `no50I_decode.txt` regenerated with `research/reading_audit/r2k_wals_dec.py` (b37 decoder + position
  corrections). Lines 11-14 now read: "that ther be nothing aganist [?the Queen] and stait of the realme. And fayle not
  to advertis me vhitner the present pacqvet and [?is] cvm to your handis vel closit or not, [91] [?hardvam] and sealed
  of the vnicorne [89] [77] [82]."
- Score (`v2_score.py` en): explicit holes 0.154 (2/13) before and after; hole rate 0.263 -> 0.256. The tail now holds,
  but the holes of lines 2-10 (14 open labels, merged-label words) keep the document far below 0.60: **decoded, not
  read**.
- Look-alike share: the position corrections touch 3 of 562 tokens; the merged labels of b37 (10, 35, 13) about 10.

## 14 Nov 2026: third look (Claude, session of 14 Nov 2026; audit section J), nothing lifted

- Is there a text now? cryptiana `mary3.htm` re-fetched: unchanged since 16 Sept 2026 (still only the opening clause,
  "Some symbols remain to be identified"). DECODE's public API answers for R3839 and marks the ciphertext private: the
  f. 138 image needs a login, and there was none in this session. So no glyph could be checked in this pass.
- The decode (`no50I_decode.txt`) re-read as sentences. Proposals from context, **not adopted** (no image, no text):
  label 91 (the key's unknown circle with a dot) = WITH at both its places (3:4 "pas in [92] with one capitane
  Carrvil", 13:38 "vel closit or not, with hard vam and sealed of the vnicorne", where *vam* would be wax); label 43 =
  WHICH and not w ("the pacqvet [which] I thovght to adres"); 6:35-40 *vhtici* = *vhtil I* with the look-alike l (38)
  for c (37) ("I durst vryte nothing of importance be him vhtil I may have some profe and asevrance of his
  fidelitie"). Each rests on sense alone; the first holds at the sign's two occurrences, the others have one each.
- Even with these three, 13 of the 14 open labels stay without a value, so the explicit-hole share would stay far below
  0.60. The document stays **decoded, not read**, and since it is the target's only document the target is classed
  `not read`; the method is now `read with known key` (the key published for this document, applied through the
  concordance), which is how the decode was obtained. What would finish it is unchanged: the Biermann-Lasry
  plaintext (unpublished), or the values of the key's unknown signs.

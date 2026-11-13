# Third reader (R3, b195) for LASA A 1 Nr. 530: f.102, f.104, f.204 read above our 65% line

Addition to `targets/magdeburg1647`. Nothing in the existing folder is changed. The key is the same frozen KEY_v2 (md5 c8fade56). Figures are per slip. No pooled figure.

## Bottom line

A third reader, using a sign reference built from the glossed frames and the Nr. 529 clear drafts, read the three open slips well above the earlier readers. Each slip was frozen and RFC 3161 stamped before its one decode.

| slip | frame | units | strict, rule read literally | floor (every borderline unit counted E) | shuffles, seeds 20261112 and 7 | earlier readers |
|---|---|---|---|---|---|---|
| f.102 'ad Appendicem Diarii No. 22' | 118 | 84 | 61/84 = 72.62% | 53/84 = 63.10% | 0/5,000 and 0/5,000 | R1 34.57%, R2 39.24% |
| f.104 'Ad Diarium No. 22' | 121 | 102 | 73/102 = 71.57% | 71/102 = 69.61% | 0/5,000 and 0/5,000 | R1 44.55%, R2 45.54% |
| f.204 'Annotata ad No. 40' | 233 | 51 | 45/51 = 88.24% | 42/51 = 82.35% | 0/5,000 and 0/5,000 | R1 47.06%, R2 43.14% |

- f.104 and f.204 are above 65% on both counts.
- **f.102 is marginal.** It is above 65% only if at least two of its eight borderline units count: 55/84 = 65.48%, 54/84 = 64.29%. The eight are listed in `units/f102_R3_judging.tsv`: split-word halves that are words by themselves ('de', 'fangen', 'bruck', 'inter'), 'grun', and the names 'crosen' and 'uehrden' (twice).
- None reaches the 95% 'read' bar. In the maintainer's words these are 'read in part'.

## Disclosures (this reader was not blind)

1. The reader knew KEY_v2 before transcribing.
2. The reader saw reader 2's lists of readable words for f.102, f.104 and f.204 by accident, when opening the scoring-rule file to read its header. It also read the phrases quoted in this folder's NOTES.md. It did not open any transcription or decode file of these slips. The exposure is logged in `transcriptions/FREEZE_LOG_R3.txt`.
3. Knowing the key lets a reader settle a doubtful letter towards a German word. The sign reference (`gloss/REF_SIGNS_R3.md`) states three rules that were applied by form: a flourished final n after d is f; the last letter of 'h f e ?' is l; a tailed g/q before u is q.
4. One judging pass by the same reader. Nothing is emended. The unit with '?' (cipher m is not in the frozen key) is counted E.
5. The clear text on the slips (Kurrent, in braces) is the reader's reading and is less certain than the cipher. It is not counted.

## Reader accuracy check on f.7 (validation only, content not first)

The reader transcribed f.7 before opening its clear draft, froze and stamped it, decoded once, then read the draft (Nr. 529 frame 882 left) and compared (`nr529/f7_R3_vs_frame882_pairs.tsv`, `nr529/f7_R3_VALIDATION.txt`, `scripts/valscore_R3.py`).
- 59 word pairs counted; 19 cipher words not counted, because the draft word is cut off by the gutter in the photograph or the clerk's wording differs.
- Exact words 41/59 = 69.49%.
- Letters 318/341 = 93.26% (longest common subsequence over the longer length; m = x added from the involution).
- Earlier figures by the same method for b189's reading: f.5 91.51%, f.6 86.87%. The draft reading is one reader's and not blind.

## What the slips say

German with Latin phrases. Readings with holes are in `readings/*_R3.md`; English (made by an AI model, marked) in `translations/*_R3.md`.
- **f.204:** the envoys report in confidence and for certain that 'dangerous counsels' are afoot: sooner give up the archbishoprics and bishoprics as recompense, so that a party keeps what it still holds.
- **f.104:** strange thoughts that one of the legates has an eye on four disputed fiefs for his recompense; a proposal reported in confidence; a contrary report in a relation sent to Sweden; 'post repulsam pro ... sua aliisque concilianda invidia'; a Münster burgher.
- **f.102:** the Reformed deputies' deduction; a jest with Wesenbeck; Gross-Glogau, a new investiture and confirmation, Crossen; 'Magdeburg, [Halberstadt], Bremen, Verden, Osnabrück and Minden' to be had; 'spiritu vertiginis'; 'pro forma vel explorandi causa'.

## Prior art for these three slips (details in PRIOR_ART_R3.md)

- No clear draft found. The draft diary (Nr. 529) and the fair copy sent home (Nr. 545) both carry only the insertion marks (alpha, beta, gamma) at these places, and the Appendix says the passage was written 'steganographice'. The slips in Nr. 530 are the inserts.
- Not seen: the fair copy of Diarium No. 40 (the server returned errors for those frames), Nr. 546, most of Nr. 529 and Nr. 543 page by page, and the printed Acta Pacis Westphalicae.
- The file holds the key (frame 168). A contemporary decipherment may exist.

## Key pages in the file (checked 13 Nov 2026)

- Frame 168: the boxed pair 'Amphictyones' over 'zxwurqlkgfdb' equals KEY_v2 in all 12 pairs. So the letter key is present in the file. We recovered it from the ciphertext before reading that page.
- Frames 5 and 6: photographs of the Catalogus booklet (name signs with clear names). No letter table.
- Frame 278: a glossed cipher page with a sign table ('signaturae catalogi sive clavis'). Four glossed words checked against KEY_v2 agree (mylonius, medicus, secretarii, clavis). Not a letter table.

## How to reproduce (standard-library Python)

- `python3 -I scripts/decode_R3.py gloss/KEY_lasa_v2.txt transcriptions/f204_frame233_R3.txt` gives `decryptions/f204_R3.txt`.
- `python3 -I scripts/mkledger_R3.py gloss/KEY_lasa_v2.txt transcriptions/f204_frame233_R3.txt units/f204_R3_judging.tsv out.tsv` gives `units/f204_R3.tsv` and the counts.
- `python3 -I scripts/shuffle_control.py <Simplicissimus> gloss/KEY_lasa_v2.txt transcriptions/f204_frame233_R3.txt 5000 20261112` gives `controls/shuffle/f204_frame233_R3_seed20261112.txt`.
- Same for f102_frame118 and f104_frame121.

## Timestamps

`timestamps/b195/`: Sectigo RFC 3161 tokens for each frozen transcription, taken before its decode: f.7 10:50:57, f.102 10:57:04, f.104 10:58:43, f.204 10:59:38 GMT on 13 Nov 2026. The three open slips were decoded at 11:00:22 GMT; f.7 was decoded at about 10:52 GMT, after its own stamp.

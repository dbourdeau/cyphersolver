# vocbatavia: the VOC Batavia number cipher, 1623-1643 (one key, four letters)

Status: in progress. Bulk drop prepared 26 Nov 2026 AEST (25 Nov UTC) by a Claude session (claude-opus-5-5) in hunts40 G3/M4;
filed as one pull request on 26 Nov 2026 AEST at Malcolm McBratney's direction. Two independent blind second readings (AI) added before filing.
No person has checked the transcriptions, keys or readings yet (AI-checked only).

## Documents (all Nationaal Archief, 1.04.02 VOC; Governor-General and Council, Batavia, to the Heren XVII)
| letter | inv. / scans | role | figure of record | controls |
|---|---|---|---|---|
| 25 Dec 1623 (+ resolution 2 Oct 1623) | 1080_0376/0380/0486; 1079_0129/0133/0263 | training (key test) | 32/54 tokens = 59.26% (below 65%) | key shuffles 0/5,000 at seeds 20261112 and 7 |
| 20 Feb 1634 | 1108_1154-1155; 1111_0564 | key source (glosses) | not scored (glossed) | n/a |
| 9 Sep 1640, postscript | 1134_0583 (base), 0617 (glossed) | blind test 1 | 9/11 tokens = 81.82% | key shuffles 0/5,000 both seeds (max 3) |
| 9 Sep 1640, LC words | 1134_0583 | LC test (key from 1643 glosses) | 5/13 words = 38.46% FAIL | key shuffles 9/5,000 and 12/5,000; letter shuffles 96/5,000 and 118/5,000 |
| 23 Jan 1643 | 1141_0901/0902/0905/0906 (copy 2, base), 0886/0890 (copy 1, glossed) | blind test 2 | 59/86 groups = 68.60% (DP word rule) | key shuffles 0/5,000 both; ciphertext shuffles 0/5,000 both (rank 1 of 5,001) |
| 9 Sep 1640, body | 1134_0570 (base), 0605 (glossed) | found 25 Nov 21:19 UTC; system B | not scored | n/a |

Per-letter arithmetic is in letters/<letter>/RESULT*.md and the *_output.txt files. Figures are never pooled.

## Systems [derived]
- System A (KEY_v2): homophonic number cipher, numbers 1 to about 74, 2-4 numbers per common letter; '/' divides words in the 1623-1640 copies;
  the 1643 copy 2 writes '/' between every number (word division lost; a dynamic-programming word rule was frozen before decoding).
- System B (KEY_B_v1, LC_KEY_v1): letters and numbers mixed, each a plain letter (r = a, d = n, m = t, b = e ...; 2 = t, 12 = o, 16 = n, 24 = e
  in B). Used for names, places, goods, amounts ('mrkmrkcbd' = Tartarien, 'crfrd' = Japan, '2.12.16.16.24.16' = tonnen). Roman numerals are
  code words (XXI = silver, IV = gout). A number in B does not have its A value. Built from contemporary glosses only; no held-out test passed.

## Keys
- key/KEY_v2.tsv: frozen 2026-11-25T20:10:20Z, md5 037b8c7a022be05d332c259d2cc4ca36; unchanged by this drop. Evidence per value in the file.
- key/KEY_B_v1.tsv: frozen 21:20:27Z, md5 c9eade0386af0fa19884d5b391fc204e (glosses of 1640 copy B and 1643 copy 1).
- key/LC_KEY_v1.tsv: frozen 21:16:17Z, md5 a718f1df4643e62531fbf3dde8cf9618 (1643 glosses only; tested on 1640 LC words: failed).

## Readings (normalised; holes as ?)
- 1623 and 1634: letters/1623_1634/RESULT_trackB.md.
- 1640 postscript: "Het dubbel deser ... [copien] van [?rieven] [gaet] in [handen vanden schipper] des schips den Caesar {John ...} [o? door]
  Cornelis Sybertsen pastijbacker ..." (letters/1640/readings/reading.md).
- 1643: letters/1643/RESULT_1643.md. Key passage (905): "Tot ontdeckinge vande Noordt Custe {Tartarien} ende ... de XXI (silver) ende IV (gout)
  rijcke [eylanden, gloss] bij {oosten} {Japan} ... om de [noort] custe van {Tartarien} aen te soecken": the Maerten Gerritsz Vries voyage of 1643.

## Emendations (all post hoc; none changes a figure of record)
- 1623: 13 values from context (SECOND_PASS_values.tsv) and 4 = k; kolden -> konden (EMENDATIONS.md).
- 1640: 12 = b and blotted group = 57, both from the 617 gloss.
- 1643: copy 2 '74' is '70' in copy 1 (copy variant or misreading); '2 28 6 ...' copy 1 may write '12 28 6 ...'.

## Remaining gaps

- **Reading state (26 Nov 2026):** all four texts are now marked "decoded, not read" and the outcome class is "not read". The key and the per-letter figures are unchanged. No person has yet read the decryptions as sentences, which the Reading check needs (a reading_review graded A or B). The class can go back to "read in part" once a reader has read and graded them.
- 1623 letter: first pass below the 65% bar (59.26%); 13 numbers set only from context - blocker: open-codes; Reading exists in the 1079 margins; values set post hoc in SECOND_PASS_values.tsv.
- 1640 postscript: 13 letter-cipher (system B) words - blocker: open-codes; LC_KEY_v1 test failed (5/13); the 617 interlinear gloss is only partly legible at the NA image resolution.
- 1643 letter: 27 of 86 number groups uncovered - blocker: open-codes; 12 are isolated system-B signs the frozen rule cannot score; run 905.3 is system B ('eylanden' in the gloss).
- System B key (KEY_B_v1) - blocker: open-codes; Built from glosses only; no held-out unglossed B passage scored yet.
- 7 Mar 1643 letter (inv. 1141 near scan 876) - blocker: not-attempted; Only a glossed copy found; key evidence only.
- Human check (a person comparing the transcription with the image and applying the key by hand) - blocker: not-attempted; Owed for every letter. Blind second readings by isolated AI readers are done for 1640 and 1643 (below), and for 1623 by non-Anthropic readers (27 Nov 2026, below).

## Blind second readings (added 26 Nov 2026 AEST, before filing)
Isolated Claude subagents (Fable model), images only; never saw our transcription, keys, decode, glosses or results. Frozen and stamped before alignment.
Alignment by script (scripts/align_readers.py, difflib on number groups). Figures of record unchanged.
| letter | reader folder | frozen | reader | matched | differences |
|---|---|---|---|---|---|
| 1640 postscript (1134_0583) | letters/1640/readers/reader2/ | 57 | 57 | 56/57 = 98.25% | blotted group: frozen 0, reader '57?' (= scan 617 gloss m = 57) |
| 1643 letter (1141_0901-0906) | letters/1643/readers/reader3/ | 86 | 89 | 85/86 = 98.84% | 902.4 group 3: frozen 10, reader 16 (listed doubt); 3 reader numbers ('8?', '6?', '6?') are signs frozen inside letter words <m8>, <mtddbi6>, <m6> |
| 1623 letter (1080_0376, block A) | blind_external_2026-11-26/ | 124 | 124 | 121/124 = 97.58% | 3 gutter groups we took from inv. 1079 ({42}, {3}, {28}): readers give '4[illeg]', '[illeg]', '2[illeg]' (consistent, no conflict) |
| 1623 letter (1080_0380, block B) | blind_external_2026-11-26/ | 127 | 127 | 127/127 = 100% | none |
Notes: letters/1640/readers/ALIGNMENT_reader2.md, letters/1643/readers/ALIGNMENT_reader3.md, blind_external_2026-11-26/ALIGNMENT.md.
The 1623 readers are non-Anthropic models (GPT-6.2 Sol, GPT-6.2 Astra, Gemini 4 Carbon; Perplexity run by Malcolm McBratney, 26 Nov 2026),
images of 1080_0376/0380 only, independent of our transcription. No emendation proposed; the 1623 first pass 59.26% (below 65%) is unchanged.

## Prior-art caveats (27 Nov 2026; PRIOR_ART.md, update section)
- 1623: Coolhaas (GM I p. 129) reports that the explanation was written in the margin "in patria"; his witness is old inv. 991 = 1079.
  Cheng 1995 vol. II p. 27 (cited for this letter by Andrade) is unverified: it may print the passage. Open.
- 1643: Leupe 1858 (Reize van M. G. Vries, introduction and note 2) prints the page 905 cipher passage and the meaning of its cipher words
  (Tartarien, gold and silver islands, Japan, noort). Found after our reading; not used. The 1643 page 905 content is therefore not first.

## Escalation
- [x] siblings: the 1623, 1634, 1640 and 1643 letters of the same series worked; leaves next to the cipher opened (inv. 1134 scans 570-617; inv. 1141 scans 886-908); DECODE has only record 1564 (1674, other system).
- [x] clear-pages: the glossed copies (1079 margins, 1108 glosses, 1134 scans 605 and 617, 1141 scans 886 and 890) checked as the decipherment, each after its score.
- [x] known-keys: KEY_v2 tried on 1640 and 1643; LC_KEY_v1 on the 1640 letter words; Ramanacoil 1674 key is graphic signs, not comparable (DECODE login needed for a direct look).
- [x] print: Leupe 1858 (1643 passage printed with explanation, found 27 Nov), Coolhaas Generale Missiven I-II (full text), Dagh-Register 1640-41 and 1643-44 (archive.org OCR), Coen Bescheiden VII, HistoCrypt papers, web searches for Tomokiyo and Lasry; HathiTrust/Google Books phrases left on Malcolm's sheet.
- [ ] key-rebuild: system B not yet extended beyond the gloss values (no annealing or EM run).
- [ ] retry: unread system-B groups not yet retried with KEY_B_v1 and regraded.

## Transcription doubts
- 39 and 5 (1643 copy 2, 905.3 groups 2 and 6) - read: 39, 5; Leupe 1858 OCR prints 89 and 6 for this run; check his page image and the witness he used; not applied.
- 61 (1643 copy 2, 901.4 group 2) - read: 61; checked: image, decode (rycx, copy 1 gloss 'rijcx'); could be 01.
- 10 (1643 copy 2, 902.4 group 3) - read: 10; checked: image, decode (n?aow under KEY_v2; 'ton..' under KEY_B), copy 1 (writes 16), independent transcription (reader 3 reads 16); KEY_B reading 'tonnen' supports 16. Frozen value kept in the figure of record.
- 74 (1643 copy 2, 901.1 group 7) - read: 74; checked: image, copy 1 (writes 70), decode (advisen needs e = 70).
- 39 (1643 copy 2, 905.3 group 2) - read: 39; checked: image, decode ('?' under KEY_v2), copy 1 (39), gloss 'eylanden' (system B y).
- 69 (1643 copy 2, 901.9 group 1) - read: 69; checked: image, decode (ses, gloss 'ses').
- mrkmrkcbd (1643 905.1) - read: mrkmrkcbd; checked: decode (tartarien under LC_KEY_v1), image (could be mrkmrkkcbd), copy 1 gloss 'Tartarien'.
- 0 (1640 583, blotted group) - read: illegible; checked: image, decode ('?'), copy 617 (57), independent transcription (reader 2 reads '57?').
- 12 (1640 583) - read: 12; checked: image, decode ('?', not in KEY_v2), gloss 617 (b).

## Exposure (honest record)
- The transcriber had KEY_v2 in context for 1640 and 1643; disclosed in each METHOD. The blind second readers (no key) agree on 56/57 and 85/86 groups.
- The 1643 frozen transcription header gives 21:10-21:30 UTC; the actual time was about 21:09-21:13 (freeze 21:13:20). Header not edited (frozen file).
- 1640 LC word 1 ('ctld' = John) was worked out before the LC freeze.
- 1134_0605 gloss ('Tonnen', 'Tayel', 'vijftich') seen before any B test was frozen.

## Record note
- RUN_RECORD.tsv was written at the end of the session from the command outputs, freeze files and stamp logs (not row by row as each step ran);
  rows at 21:18:00 and 21:20:57 are approximate to the minute. Effort is not exposed on this surface.

- Images: archive crops are not filed; boxes and IIIF region URLs are in images/crops.tsv (IMAGE_ACCESS.md).

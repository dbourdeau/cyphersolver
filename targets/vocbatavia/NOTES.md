# vocbatavia: the VOC Batavia number cipher, 1623-1643 (one key, four letters)

Status: read in part (written up 27 Nov 2026: docs/vocbatavia.html). Bulk drop prepared 26 Nov 2026 AEST (25 Nov UTC) by a Claude session (claude-opus-5-5) in hunts40 G3/M4;
filed as one pull request on 26 Nov 2026 AEST at Malcolm McBratney's direction. Two independent blind second readings (AI) added before filing.
No person has checked the transcriptions, keys or readings yet (AI-checked only).
The checks were done with AI tools and no person checked each record by hand.

## Documents (all Nationaal Archief, 1.04.02 VOC; Governor-General and Council, Batavia, to the Heren XVII)
| letter | inv. / scans | role | figure of record | controls |
|---|---|---|---|---|
| 25 Dec 1623 (+ resolution 2 Oct 1623) | 1080_0376/0380/0486; 1079_0129/0133/0263 | training (key test) | 32/54 tokens = 59.26% (below 65%) | key shuffles 0/5,000 at seeds 20261112 and 7 |
| 20 Feb 1634 | 1108_1154-1155; 1111_0564 | key source (glosses) | not scored (glossed) | n/a |
| 9 Sep 1640, postscript | 1134_0583 (base), 0617 (glossed) | blind test 1 | 9/11 tokens = 81.82% | key shuffles 0/5,000 both seeds (max 3) |
| 9 Sep 1640, LC words | 1134_0583 | LC test (key from 1643 glosses) | 5/13 words = 38.46% FAIL (v2 transcription, 16 words: 7/16 = 43.75%, not of record) | key shuffles 9/5,000 and 12/5,000; letter shuffles 96/5,000 and 118/5,000 |
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

## Reading state and house count (27 Nov 2026, Dan Bourdeau's review of PR #996)
- [measured] Rule: cipher words only, sure words only (`python -I scripts/house_count.py`, run from this folder; it lists
  every hole and why). A word is read when the key gives every letter and nothing is supplied or emended. Words resting on
  a gloss alone (system B, the code numerals, numbers with no key value) are holes.
| text | cipher words | holes | read share | state | Dan's rough count |
|---|---|---|---|---|---|
| 1623 (A 26, B 23, C 5) | 54 | 1 (kolden, read konden) | 0.981 | read | read in full |
| 1634 (key source) | 35 | 0 | 1.000 | read (from its glosses) | not counted |
| 1640 postscript | 27 | 18 | 0.333 | read in part | about 9 of 27 |
| 1643 | 55 | 44 | 0.200 | read in part | about 12 of some 50 |
- Where we differ from Dan [derived]: 1623 has one hole by the strict rule (the emended konden), still over 95%. 1643: we
  count d'advisen as a hole (74 has no key value; copy 1 writes 70), and we count each letter word and each number run as
  one word, so mixed runs such as <crf> 21 <d> (Japan) count as several words; voor is counted read (the key gives it)
  although copy 1 glosses naer. 1634 is the key source: every word glossed, so its 1.000 is not a test of the key.
- The 65% figures of record (59.26%, 81.82%, 68.60%) stay as test evidence for the key (method_basis); they do not decide
  the state. The earlier fraction_read 0.956 was key coverage (608/636 groups with a value) and is withdrawn; fraction_read
  is now 73/136 = 0.537 (1623 + 1640 + 1643; 1634 left out).
- Class "read in part"; primary method "key recovered based on adjacent plaintext" (the 1634 glosses); provenance
  "contributed", credit mcbratney. Reading reviews are left for the maintainer: a contributor does not sign them.

## Emendations made (27 Nov 2026 UTC): 1640 postscript transcription version 2
- Made as a new frozen version, letters/1640/v2_2026-11-27/ (v1 files untouched): FREEZE_v2.txt 2026-11-27 04:23:58 UTC,
  T1640_transcription_v2.txt md5 77202d0359683d472985ec0412581f79; stamped (Sectigo 04:23:59Z, FreeTSA 04:24:00Z).
- E1: after "Amsterdam" the image shows the letter-cipher words "k bd. p." (reader 2: "te Bd. p."); v1 skipped them, so the
  postscript has 16 letter-cipher words, not 13 (Dan Bourdeau, review of PR #996; reader 2).
- E2: the last letter-cipher word but one is "qbhm" (reader 2 and the image), not "qbbm".
- One re-decode with the frozen LC_KEY_v1 (RESULT_v2.md): 7/16 words = 43.75% (k -> r and bd -> en added; four of the seven are
  single letters); letters keyed 45/60 = 75.00% (v1 43/56 = 76.79%); key shuffles 9/5,000 and 12/5,000, letter shuffles
  235/5,000 and 230/5,000. Under the 65% line; not the figure of record. Number tokens identical (11 = 11), so 9/11 stands.
- Figures of record unchanged: LC 5/13 = 38.46% (v1 first pass). House count unchanged (all 16 already counted as holes).

## Remaining gaps

- 1623 letter: read, 53 of 54 cipher words; the one hole is kolden read konden (26 = l taken as a slip); the first pass (59.26%) is key-test evidence only; 13 numbers set from context after the first pass - blocker: open-codes; Reading exists in the 1079 margins; values set post hoc in SECOND_PASS_values.tsv.
- 1640 postscript: 16 letter-cipher (system B) words (13 in the v1 transcription + 'k bd. p.' in v2, see emendations made) - blocker: open-codes; LC_KEY_v1 test failed (5/13); the 617 interlinear gloss is only partly legible at the NA image resolution.
- 1643 letter: 27 of 86 number groups uncovered - blocker: open-codes; 12 are isolated system-B signs the frozen rule cannot score; run 905.3 is system B ('eylanden' in the gloss).
- System B key (KEY_B_v1) - blocker: open-codes; Built from glosses only; no held-out unglossed B passage scored yet.

## Owed checks (not unread pieces; moved out of Remaining gaps 27 Nov 2026)
- Human check (a person comparing the transcription with the image and applying the key by hand) - Owed for every letter. Blind second readings by isolated AI readers are done for 1640 and 1643 (below), and for 1623 by non-Anthropic readers (27 Nov 2026, below).
- 7 Mar 1643 letter (inv. 1141 near scan 876): a further letter of the series; only a glossed copy was found, so it is key evidence, not an unread piece of these four texts. Not transcribed (see Escalation, siblings).

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

## Statistical test (27 Nov 2026)
- `python docs/_validate.py vocbatavia --write` on validation.tsv (the 1623 letter, 276 numbers, read with the same key as scripts/house_count.py; model nl-modern, the Gutenberg Dutch corpus fetched from the gutenberg.pglaf.org mirror because gutenberg.org answered 503): reading -2.914 per letter; random keys -6.457 (sd 0.299, z 11.8); shuffled refit -3.588 (sd 0.146, max -3.445); annealer power -3.193; verdict **pass**. Recorded in profile.json outcome.validation. The nl-1600 period model needs a DBNL build and was not available.

## Prior-art caveats (27 Nov 2026; PRIOR_ART.md, update section)
- 1623: Coolhaas (GM I p. 129) reports that the explanation was written in the margin "in patria"; his witness is old inv. 991 = 1079.
  Cheng 1995 vol. II p. 27 (cited for this letter by Andrade) is unverified: it may print the passage. Open.
- 1643: Leupe 1858 (Reize van M. G. Vries, introduction and note 2) prints the page 905 cipher passage and the meaning of its cipher words
  (Tartarien, gold and silver islands, Japan, noort). Found after our reading; not used. The 1643 page 905 content is therefore not first.

## Escalation
- [x] siblings: the 1623, 1634, 1640 and 1643 letters of the same series worked; leaves next to the cipher opened (inv. 1134 scans 570-617; inv. 1141 scans 886-908); DECODE has only record 1564 (1674, other system). The 7 Mar 1643 letter (inv. 1141 near scan 876) was found as a glossed copy only and not transcribed (key evidence, not part of these four texts).
- [x] clear-pages: the glossed copies (1079 margins, 1108 glosses, 1134 scans 605 and 617, 1141 scans 886 and 890) checked as the decipherment, each after its score.
- [x] known-keys: KEY_v2 tried on 1640 and 1643; LC_KEY_v1 on the 1640 letter words; Ramanacoil 1674 key is graphic signs, not comparable (DECODE login needed for a direct look).
- [x] print: Leupe 1858 (1643 passage printed with explanation, found 27 Nov), Coolhaas Generale Missiven I-II (full text), Dagh-Register 1640-41 and 1643-44 (archive.org OCR), Coen Bescheiden VII, HistoCrypt papers, web searches for Tomokiyo and Lasry; HathiTrust/Google Books phrases left on Malcolm's sheet.
- [x] key-rebuild: 27 Nov 2026, dictionary/LM-context extension of KEY_B_v1 (scripts/retry_b.py, letters/RETRY_B_2026-11-27.txt): for each B word with unknown signs, Dutch words that fit the known letters (repository nl lexicon plus the words read in this target). No new value is supported by two or more words, so none is adopted; KEY_B_v1 unchanged. Annealing or EM was not run: 47 B words in all, 15 with unknown signs, too few to constrain a key with no held-out text.
- [x] retry: 27 Nov 2026, all 47 system-B words (1640 postscript 16, 1643 letter 31) decoded with the frozen KEY_B_v1 (letters/RETRY_B_2026-11-27.txt): 32 fully valued. The 1643 words give the copy-1 glosses back (tartarien, iapan, oosten, natien, chinees, drie, acht ...), but KEY_B_v1 was built from those glosses, so they are not a test. In the 1640 postscript tpbk = over (its own gloss) and grbk = daer; Gmroodt, lrdgenlm, bpbkdbsbd, Zrpmb, qbbm/qbhm, boode stay unread. Regraded: no hole changes under the house rule (B words rest on glosses; the B key has no held-out test). Figures of record and house count unchanged.

## Transcription doubts
- 39 and 5 (1643 copy 2, 905.3 groups 2 and 6) - read: 39, 5; checked: image, decode (39 = y, 5 = d in system B: 'eylanden', the copy-1 gloss), transcription (blind reader 3 agrees on both; only 902.4 group 3 differs); Leupe 1858 page image checked 27 Nov 2026 [measured]: p. 6 (archive.org reizevanmaarten01siebgoog, image n16), read at full size, prints "24, 39, 17, 30, 16, 5, 50, 20" for this run, and his other two runs ("11, 9, 16, 10, 2"; "2, 25, 20, 72, 22") match ours too: 18 of 18 numbers agree. The OCR's 89 and 6 were OCR reading errors, not a witness difference. Nothing to apply.
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
- Scripts: run_1643.py, run_lc.py, run_blind.py and blind_external_2026-11-26/align_external.py read absolute working paths
  (/home/claude/...) and an unfiled word list module (trackB/scripts, the 37,386-type VOC HTR list); they do not run from a
  checkout as they stand. scripts/house_count.py uses paths relative to this folder.
- RUN_RECORD.tsv was written at the end of the session from the command outputs, freeze files and stamp logs (not row by row as each step ran);
  rows at 21:18:00 and 21:20:57 are approximate to the minute. Effort is not exposed on this surface.

- Images: archive crops are not filed; boxes and IIIF region URLs are in images/crops.tsv (IMAGE_ACCESS.md).

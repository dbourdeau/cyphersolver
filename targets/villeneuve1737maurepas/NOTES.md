# villeneuve1737maurepas — Villeneuve (Constantinople) to Maurepas, 18 Feb and 2 Apr 1737: the two undeciphered cipher letters of Archives nationales AE/B/I/414 (catalogue 538)

Source: Archives nationales, AE/B/I/414 (correspondance consulaire, Constantinople), reproduction ordered by Brice Dudout (26 JPEG, received 20 Nov 2026). Images are not distributed; cite « Archives nationales, AE/B/I/414 ».

## Pieces
- T1 — Villeneuve to Maurepas, Constantinople, 18 Feb 1737 (frames 0060-0062): inventory « Lettre chiffrée — lettre non déchiffrée ». 350 cipher groups, clear passages between them.
- T2 — Villeneuve to Maurepas, 2 Apr 1737 (frames 0092-0096 L): inventory « Lettre partiellement chiffrée, non transcrite ». 1,194 cipher groups. (Frames 0093-0097 also show the header strip of a sheet dated 10 Apr 1737 lying behind; it is not a separate cipher letter.)
- Key witnesses (same volume, period interlinear decipherment): 9 Jul 1737 (frames 0197-0202) and 29 Jul 1737 (frames 0230-0231).

## The code
A numeric nomenclator, groups 1-499: single letters with homophones (n = 78, 409, 182; e = 10; r = 164; t = 220, 400 ...), many syllables (co 26, so 469, pe 374, re 51, se 27, ro 292, la 203, de 441/495, que 117, ...) and some words (dans 189, nostre 461, commerce = 410 + ..., roy 447, bien 462). 318 is very frequent and behaves as a null, often between words. It is not the 1737 Villeneuve -> Otter key read by George Lasry (targets/villeneuve1737; e.g. there 283 = je, 78 = ce).

## Transcription
Two blind passes (A, B; AI agents without key; B in reverse page order) of targets and witnesses, a blind arbiter on the 62 disagreements (blind/), and a separate careful re-reading of the period glosses (key_source/gloss_careful.txt). Agreement before arbitration: 1,498/1,544 target groups, 1,712/1,781 witness groups. Main confusions: this hand's 3 and 5; groups lost in the binding at the end of left-page lines.

## Key and measure (pre-registered, prereg/)
- PREREG-0 (20 Nov, before any key): TRAIN = witness frames 0197-0199 + 0230-0231; HELD-OUT = 0200-0202 (598 groups); one measure; pass iff >= 0.85 and >= best of 200 controls + 0.30.
- K1 (prereg/KEY-K1-frozen.txt, 218 codes): fitted on TRAIN glosses only (coordinate ascent on edit distance + hard-EM majority + manual curation from repeated words; tools/solve.c, tools/align.py). In-sample 0.858.
- Measure (prereg/MEASURE-RESULT.json): **0.661 vs best control 0.263 (mean 0.120) — FAIL at the 0.85 bar**; margin over controls met. Held-out burnt. Causes: 31 held-out groups absent from TRAIN and 56 seen once; the gloss is often written a little ahead of or behind its number line.
- K2 (key.tsv, frozen before decoding the targets, PREREG-2): same fit on all glossed witness frames; each code marked S (supported) or W (weak). Not separately validated.

## Result
Read in part: T1 106 of 255 cipher words sure (0.416); T2 348 of 838 (0.415); rule of #728, sure words only (reading.md, count728_detail.txt). 234 target groups use codes absent from the witnesses.

## Historical gist
The Porte intends to conclude a treaty of commerce with the King of the Two Sicilies (Charles of Bourbon); Villeneuve warns Maurepas that it must not harm French Levant trade, reports in April a conference where he was asked about it, the line he took, and the risk that the maritime powers would use the occasion to obtain advantages. The Ottoman-Neapolitan treaty was signed in 1740.

## Gaps
Codes absent from the witnesses (234 target groups); weak values; gutter losses on left pages (0061 L, 0062 L, 0093-0096 L). More glossed letters of 1737 in AE/B/I/414 (or the register copy at La Courneuve) would give a fresh held-out portion and close many holes.

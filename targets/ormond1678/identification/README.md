# ormond1678: key identification (Tomokiyo's Ormond-Longford Cipher 1, shifted by +7)

Status: key identified: Tomokiyo's reconstruction of Ormond-Longford Cipher 1 shifted by +7; read in part 15/20 figures; holes kept.

This is a key identification, not a new break. The key is S. Tomokiyo's reconstruction (Cryptiana `charlesii2.htm`, image `charlesii2_Ormond_Longford1.png`) from the interlinear glosses printed in HMC Ormonde n.s. V pp.454 ff. What is new is the offset: every 1678 figure is the 1680 number plus 7.

## Reading (holes kept)

Decryption (`decryption.txt`, from `scripts/decode.py` on `key_shifted.tsv`):

    {If what he says of} [445] {and} [342] {, be true} [726] an d King ar e in a [700] [720] {but it seems} to Ormond not c re di b le

English (AI-made): "If what he [Douglas] says of [445] and [342] be true, [726] and the King are in a [700] [720]; but it seems to Ormond not credible."

## Counts (figures, not pooled; first pass)

- Given a value: 15/20 = 75.00%. Holes ('?' rule): 5/20.
- By evidence: 10 from printed glosses or the p.498 plain rendering (84, 26, 86, 377, 725, 566, 519, 636, 207, 48); 4 interpolated from the key's regular order (51 e, 47 a, 25 c, 433 le); 1 from context (418 King); 5 holes (438, 335, 719, 693, 713).
- Gloss-attested only: 10/20 = 50.00%.
- Tomokiyo's key exactly as published gives 14/20 = 70.00% a value (418 is an empty row); it reads "and d" for 84 26 and "Dor/or?" for 566.

## Controls (`scripts/controls.py`, output `controls_out.txt`)

Offsets -150..+150 (301) on two candidate keys (K1 = Tomokiyo's Longford 1, K2 = Longford 2, HMC n.s. VI pp.xix-xxii): 2 x 301 = 602 trials on the real figures. Longford 3 (n.s. VII p.xx) also run as a third key.

- Hits on keyed entries: K1 at -7 = 14/20, the unique maximum (next 12 at -5; offset 0 gives 6). K2 maximum 12 (at -24, +10, +15). K3 maximum 4.
- Longest vocabulary word (5+ letters, seen 5+ times in the OCR of HMC n.s. IV-V, 5,644 words) spelled by 3+ consecutive groups: K1 at -7 gives "credible" (8 letters, 5 groups). Offsets giving any such word: K1 1/301, K2 0/301, K3 0/301.
- 2,000 random figure sets of the same run shape (low positions U[23,99], high U[100,850]; seed 20261113), each at its best of the 602 key-offset pairs (1,204,000 decodes): any 5+ letter word 117/2000; 8+ letters 6/2000. K1 alone: 31/2000 and 3/2000. Same offset with 14+ hits and an 8+ letter word: 0/2000.
- 2,000 random sets, K1 best hit count over 301 offsets: 14 reached by 5/2000.
- 3,000 shuffles of the real 20 figures into the same runs, at -7 on K1 (seed 7): any 5+ letter word 35/3000; 8+ letters 0/3000.

What the controls show: the word statistic picks out -7 and nothing else, and random sets rarely do as well. What they do not show: whether "King" or the interpolated values are right, or whether +7 holds outside the entries touched. No held-out text exists in the 1678 numbering.

## Files

`transcription_b197.txt` (frozen 2026-11-13T10:32:39Z, md5 4a98a80b09b7555ca1875d081a572c03; one reader, not blind; agrees figure for figure with `figures.txt`), `key_shifted.tsv`, `decryption.txt`, `ledger.tsv`, `GLOSS_CHECK.md`, `PRIOR_ART.md`, `keys/` (K1, K1c, K2, K3, vocabulary), `scripts/`, `controls_out.txt`, `crops/`, `timestamps/`.

## Credit

Key reconstruction: S. Tomokiyo (Cryptiana). Glosses: HMC, Calendar of the MSS of the Marquess of Ormonde n.s. V. Offset identification and check: Malcolm McBratney (Brisbane), working with Claude (Anthropic). The offset was first noticed by an agent Malcolm ran on Perplexity, then checked independently here (transcription, glosses on page images, controls rebuilt with our own scripts).

# Santa Cruz 1635: Philip IV → II marqués de Santa Cruz (catalogue 725–727)

Status: in progress

Source: issue #183 (Michael Brackx, 28 Oct 2026). AHNOB SANTA CRUZ C.51, units D.133–215 on PARES.
His gist (key_1635.md, D.179/D.194 transcriptions and readings, dec1635.py, signs_d179.md) is copied in `brackxm/` (5 Nov 2026),
with his permission of 28 Oct 2026 (CC BY 4.0 for text and data, MIT for code), credit Michael Brackx.

## Check done here (28 Oct 2026)
- `decode.py` is our own decoder, built from the prose key in key_1635.md, not from his dec1635.py.
- D.194 (5 lines, image 59): reproduces his reading mechanically (*aunque ... sabiendo vos la necesidad ... el estado de
  Milán ... assistido ... os encargo y mando que lo hagais*).
- D.179 transcription (3,718 tokens): 90.2% of tokens have a key value (p.3 91.6, p.4 91.0, p.5 91.9, p.6 91.4, p.7 84.2).
  Pages 1–2 decode to clean Spanish. Pages 3–7 do not come out as words from the key alone: his transcription there uses
  different sign conventions (nasal l/L, r = a, m = o, 8 = u/v) that key_1635.md only describes in prose.
- Not done: the PARES images (D.176–197, images 7–13 and 59) are unchecked, so the transcriptions are his.

## Check with the D.179 sign list (5 Nov 2026)
- `decode.py` now carries the transcription signs of `brackxm/signs_d179.md` (ff = m, 1u = pu, 1c/Lc = no, ch = os, Le = me,
  7L = de, Lo = ne, Z alone = n, l = n; I, T, S marks), written from that list, not from his `dec1635.py`.
- Share of D.179 groups with a value, before -> after: p.1 93.5 -> 97.3, p.2 86.6 -> 92.4, p.3 91.6 -> 97.6, p.4 91.0 -> 96.7,
  p.5 91.9 -> 97.4, p.6 91.4 -> 96.9, p.7 84.2 -> 91.4. His own figures (dec1635.py): 94, 98, 98, 97, 97, 91. Reproduced within
  about a point, so the reading of pp. 3-7 rests on a fixed sign table, not on hand corrections.
- One difference: his list gives 22 = xe; our key table has 22 = xo (from key_1635.md). Not settled.
- Still not done: the PARES images. The catalogue split of row 727 waits for that check.

## Remaining gaps
- D.179 pp.3–7 and the images; D.143, D.145, D.156–157/159/161/164, D.170, D.201, D.212, D.215, D.99/107/113.

## Escalation
- Check the transcription against PARES images; rebuild the per-page sign conventions; apply the key to D.215 and D.170.

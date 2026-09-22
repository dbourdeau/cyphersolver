# Brief: read BnF fr. 15564 f. 119 (Guise? to Mercœur, 27 May 1587) with Lasry's key

Everything is in `C:\Users\dbour\cypher\guise1587\`.

- `GL_BnFfr15564.png`: George Lasry's 2022 key (enlarged: `key_top.png`, `key_bot.png`). Letters A–Y with their
  homophone signs; nomenclator groups (ff-ligature forms) for DE AU LA ET DES QUE LES MON LE QUI POUR PAR VOUS
  ILS/NOUS NOUS LEUR SON; an "Unknown" row (e.g. 21, 71, 73, 89 = names).
- `img/yNN.png` (NN = 00..43): one manuscript line of f. 119 each, shown as three overlapping thirds stacked
  (left, middle, right). Lines are wholly in cipher; no word division. The full page is `img/f119_cipher.jpg`.
- `f142_reading.txt`: the sibling letter (20 June 1587, same hand, same key), already read. Use it as a model.

## Sign values confirmed on f. 142 (same hand)

n (pi-shape) = E; 6 = E; `:` = T; # = V/U; x = N; ɱ with a long descender (looks like η) = I; single-hump
"an"-shape = N; Δ = O; D = R; ß / % / ɷ-shaped looped signs = S; ɔ = S; ℓ (loop) = A or S (two similar signs:
decide by context); Є plain = L, Є with a dot inside = R (hard to tell apart: context); small open c = F;
ρ (long p) = C; 1 = O or C (context); ƀ (T with a bar, Ƃ) = L; ʑ (2-shaped with tail) = I; long slash ʃ = A
(sometimes C or P: "=ʃ" = P); Ƹ / ε / Σ-shape = U/V or P (context); ɮ / ɜ = M; bold 8 = M or B; q / 9 = D or C;
4 = C; 7 = O; 3 / ǝ = D; ɗ (δ-shape) = D or L; ɤ (bold curvy X) = T; γ = F; Ꮃ (w-shape) = M; Ⱥ (bold A/R-like) =
B; ɯ / ⱱ = X; `::` = H; ʒ with dot = Q; Φ = V; I = B; m̃ (three humps) = G.
Groups: ffuy / fuy = LA (sometimes ET); ff6 / ʃʃb = QUI; fbu / ʃbi = LES; fu / ʃm = ET or DES; ffm = QUE / POUR;
fff = VOUS; ffff = LEUR; ffbm = NOUS; "73" = a person (maybe the queen mother).
Plaintext is 1587 French: v=u, i=j, doubled consonants, "faict", "desseings", "seureté".

## Method

1. Read each line image (Read tool). Transcribe sign by sign, then decode with the table above plus the key,
   choosing between homophone candidates by French context. Work at word level; reread a part of the image when
   the decode is nonsense.
2. Append each finished line to your output file AS YOU GO (one line per manuscript line):
   `NN | glyph transcription | reading` where the reading uses lower case for letters read, UPPER for
   nomenclator groups, `[?]` for anything unread, `[?xyz]` for a tentative letter string.
3. Do not invent text to make it read smoothly. Mark doubt.
4. At the end, report: lines done, a rough percentage of signs read as sense, and any sign values you established
   that differ from the list above.

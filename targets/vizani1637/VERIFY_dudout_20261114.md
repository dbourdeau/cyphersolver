# vizani1637: independent check of the key and of doubtful signs (Brice Dudout, Claude Opus 5.5, 14 Nov 2026)

## Decoder
`verify_dudout_20261114.py targets/vizani1637` segments each word of `cipher_words.tsv` on the signs of `key.json`
(longest first) and decodes it; it does not use `dec.py`.

- 54 words; 182 key-sign tokens and 5 numeric codes (231, 31, 36, 198, 227). (`profile.json` gives 190 tokens; the
  difference is in how digits and the group 6ꝗ are counted, not in the text.)
- 47 words decode exactly to the plain on Satoru's page. The 7 others: ꝗ∸đΩ̇Ωȼ∸⊣ and ꝗ∸đ⊢Ω̇Ω∸⊣ (monsignor, abbreviated,
  as dec.py notes), quattr(o), su(a), dattone? (decodes dattone), ʒ (li?, no key value) and 6ꝗ (see below).
- Key correction: none.

## Image (Gallica, BnF Français 16158 f. 292r, ark btv1b9061541x, view 295; Source gallica.bnf.fr / BnF)
Fetched by IIIF (openapi.bnf.fr) and re-read at the doubtful places. No image is in the repository.
- 231 and 31: digits, as transcribed. The writer's 1 is a short stroke with a dot, the same shape as the e homophone ẻ
  (as in ⊢ẻ, se). The codes stand (the other codes, 36, 198, 227, are plain digits), but the shape is shared.
- The sign read "li?" (line 1, before quattro) is a 3 with a crossed top stroke. It is not the plain 3 of 31 (line 2).
  No value.
- 6ꝗ (before the second "Monsignor Beria"): the two signs have key values elsewhere (6 = a, as before [227]; ꝗ = m, a
  4-like q with a crossed descender). Read as the code 64 the second digit is written exactly like ꝗ. Undecided;
  the "[64?]" mark is right to keep.
- dattone: ɤ ⌒̇ ꝏ ∸ ȼ ẻ as transcribed (the fourth sign has one dot, o, not ÷).
- Line 1 ends at the paper edge after hυ⌒̇ꝏ⊣ (quattr-); the o of quattro is not visible there.

## Read bar (README)
`v10_relabel.measure` on `texts/f292_decryption.md`: 0.926 over 87 words, the recorded value (read in part).

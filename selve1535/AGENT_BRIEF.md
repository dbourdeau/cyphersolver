# Selve 1536 — agent brief

Letter: Georges de Selve, bishop of Lavaur, French ambassador at Venice, to Francis I, 5 July 1536.
BnF fr. 3045 ff. 42–49 (Gallica btv1b9060156p, views 82–95). French, partly in cipher. The clear
text around the cipher is about the siege of Turin / Fossano / Marseille, Imperial troops (Charles V's
invasion of Provence 1536), Fabrizio Maramaldo, Barbarossa, the Pope, Venice, Naples.

Page images (2600 px wide) are in `selve1535/img/th_btv1b9060156p/c0NN_2600.jpg`, NN = view number.
Crop them with PIL into strips of 3–5 lines (full text width, ~400 px tall) and read the strips; do not
read the whole page at once. Save crops in the scratchpad or `selve1535/img/` (git-ignored).

## Key (Tomokiyo, cryptiana francis.htm "Selve's Cipher") — simple substitution, a few homophones

| plain | sign(s) | ASCII alias |
|---|---|---|
| a | `z` (like a z), `3` (like a 3/ʒ open) | a |
| b | `f` crossed (like ƒ with a bar) | b |
| c | `ℓ` small curl like an l/ℓ | c |
| d | `C`/`L`-like hook (like a capital C with a long top) | d |
| e | `‡` (cross with two bars), `o` (small circle), `ω` | e |
| f | `ʃ` short (s-like, stays on the line) | f |
| g | `∽` (o with a tail to the right, like "o-") | g |
| h | `£` (like a script E/£) | h |
| i | `p` (a p shape) | i |
| l | bow-tie `⋈` (like ✕ closed / "x" in a box), `<` with dot, `/` slash | l |
| m | `x` (a plain x) | m |
| n | `▽` (triangle / v shape) | n |
| o | `ɥ` / `4` (like 24 / a 4) | o |
| p | `ʃ` LONG (descends below the line) | p |
| q | `6` | q |
| r | `ꝏ` (two linked o's, "oo") | r |
| s | `o+` (small o followed by a cross; one sign) | s |
| t | `7` | t |
| u | `X` / `Ⴟ` (like an 8/X with a top bar) | u |
| x | `Ƶ`/`8` lying (like a z with a bar / sideways 8) | x |
| y | `ʒ` (3 with a tail below) | y |
| z | circled sign | z |
| null | `S` (a plain capital-like S) | . |

Known confusions: c `ℓ` vs d `C` look close — decide by the French. `o` (= e) vs `o+` (= s): look for the
cross. `f` short vs `p` long: descender. `x`(m) vs `X`(u): the u has a bar/loop. `z`(a) vs `3`(a) are both a.
Tokens may carry an overbar or be struck through with a line; transcribe anyway. The long diagonal strokes
across the page are a later cancellation mark, ignore them.

## Output (write to `selve1535/work/vNN.md`; append as you go, one line at a time)

For every cipher line:

```
vNN lK  clear-before: <any clear words on the line before the cipher, as written>
  signs: <the decryption letter per sign, no spaces; '.' for a null S; '?' for a sign you cannot read; [x|y] for an ambiguous sign>
  read:  <the same, word-divided French, modern spacing, with (?) after doubtful words>
  clear-after: <clear words after the cipher on this line>
```

Then at the end: a continuous reading of the whole ciphered passage in French, a short English gist, a count of
signs read / unclear, and notes on anything that does not fit the key (new signs, possible code words or
numbers, homophones not in the table). Marginal notes or interlinear glosses beside struck cipher lines may be a
contemporary decipherment: transcribe them exactly and compare with your reading.

Work carefully sign by sign; the French must emerge from the signs, do not guess words the signs do not give.
Language: 16th-c. French orthography (cestuy, veu, ledict, faict, sçavoir, aussy, ceulx, etc.).

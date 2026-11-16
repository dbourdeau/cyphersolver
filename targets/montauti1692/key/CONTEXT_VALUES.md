# The two context-only values (not attested under any interline)

File: `key_v3_context.json` (sha256 f5115d3872160fd5f714766a15a1c1538cc14cbe5a171c21ad742a17f33d8e72), kept apart from
the frozen key v3 (`key_v3.json`, sha256 bdc8b174...). `key_v3_plus_context.json` is the two merged, for decoding only.

| group | value | evidence | status |
|---|---|---|---|
| ww | o | 14 places in the bare Codex 534 passages ff. 114r-116r (cotesta, matrimonio, Polonia, Colonia, con, forza, s'opponga, esibizione, circospezione) and 11 in Codex 533; o fits every time; no contradiction. Cosimo writes the second w as an 8-like loop. | context only |
| 62 | q | 3 places, all in Codex 533 ("ritornare qua" 1r, "qualche facilità" 63r, "qu..." 25r). Fits the order of the table (60 p, 62 q, 64 r, 66 s, 6w t). No q in Codex 534. | context only |

Neither value was tested on held-out material. Penn Ms. Coll. 180, Folder 114 ("Documents with code for diplomatic
ciphers, 1689, 1694"), not seen, would confirm or refute them.

## Every reading in Codex 533 that depends on them

A "+" after a letter in `readings/runs_533.tsv` and `readings/L*_decode.txt` marks it. In no case does the word's
identity rest on the context value alone: the other letters fix it (the verifier's finding for 1r-1v; it holds for the others too).

| run | reading | value used | run read |
|---|---|---|---|
| 1r a | l'El[e]ttor[e] Palatino | ww = o (1 letter; the verifier reads the same signs as 48, emended to 40 = o) | whole |
| 1r c | permission[e] | ww = o (1 letter) | whole |
| 1r d | ritornare qua | 62 = q, ww = o (2 letters) | whole |
| 1r f | marito | ww = o (1 letter) | whole |
| 22r a | sono sodisfatt[i] del duca d[i] Savoia | ww = o (3 letters) | whole |
| 25r b | qu[..] | 62 = q (1 letter) | not read |
| 25r c | costà | ww = o (1 letter) | whole |
| 28v a | [..] | ww = o (1 letter) | part |
| 28v c | corte | ww = o (1 letter) | whole |
| 28v d | toscani | ww = o (1 letter) | whole |
| 35v a | [d]ell[a] d[o]n[n]a(?) di camera favorita dell[a] [14] | ww = o (1 letter) | most |
| 63r b | [..] qualche facilità | 62 = q (1 letter) | most |
| 63r c | ult[i]mo(?) | ww = o (1 letter) | part |
| 70v a | agosto | ww = o (1 letter) | whole |

## In the bare passages (Codex 534 and 531)

ww = o in P1 (f. 114r lines 1, 10, 11 ×2, 13 ×2, 15, 16), P2 (f. 115r lines 1, 9, 12) and P3 (f. 116r line 1 ×3); marked
"+" in `bare/P*_decode.txt`. 62 does not occur there.

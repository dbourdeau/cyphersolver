# MTC3 272-274 (and 292): Weakened ElsieFour Parts 1-3 (Rotthaler, 2017-18)

Status: in progress (24 Sept 2026; nothing solved or submitted).

LC4 (Kaminsky 2017): a 6x6 state that changes with each character, over the 36-character alphabet `#_23456789a..z`. The
"weakened" variant drops the nonce, so every message starts from the key itself.

| # | Part | Given | Human solvers | LLM |
|---|---|---|---|---|
| 272 | Weakened 1 | first 12 of 36 key characters; 63-char ciphertext | 7 | 0 |
| 273 | Weakened 2 | 12 consecutive key characters, position unknown; 66-char ciphertext | 2 | 0 |
| 274 | Weakened 3 | 45-char plaintext/ciphertext pair + a 131-char ciphertext under the same key | 4 | 0 |
| 292 | ElsieFour 1 (level III, with nonce) | 51-char known plaintext + nonce; a second ciphertext | 4 | 0 |

The answer each time is the signature (the part of the plaintext starting with `#`).

## What was tried (tools in `src/`)

- `lc4beam.cs`, left-to-right beam over partial states that fills key cells lazily and ranks with a character
  5-gram model: on the documented test pair with 12 cells known, the truth ranks ~53,000th after 3 characters and is
  lost by the 5th, even with 2M hypotheses. Each step adds ~9 bits of placement choice but the model supplies ~2.5.
- `lc4sa.cs`, annealing over whole keys: chaotic landscape (truth -38, best found -112).
- `lc4kpa.cs`, known-plaintext DFS (Kaminsky's branch-and-bound, `State.java`): instant with 12 cells known;
  infeasible with all 36 unknown.
- `lc4gen.py` / `lc4sat_co.py`, SAT encoding (pysat CaDiCaL; load it with
  `os.add_dll_directory(<site-packages>/z3/lib)`): one-hot cell positions per step and transitions that depend on the
  data. It recovers the test key in 109 s with 12 cells known, and shows the key is unique. The Part 3 pair with all 36
  cells unknown ran 2.5 h (CaDiCaL, plus a Glucose run with backward clauses) without an answer; stopped.
- Ciphertext-only SAT, with the plaintext as variables restricted to letters/`_` and corpus 3-/4-grams: finds keys,
  but the first one was a spurious plaintext. The constraints are too weak before the signature is pinned down.

## Remaining gaps

All four challenges are unread.

## Escalation

Next: split Part 3 into cubes (fix the step-0 marker value, 36 cubes) and run them in parallel on a machine with more
free RAM; symmetry-free extra clauses (inverse positions); for Parts 1-2, a hybrid that drags common words as cribs and
checks each placement with the fast DFS (12 cells known makes each check cheap).

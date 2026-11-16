# Key: COME RETRIBUTION, Confederate Vigenere (catalogue 681)

- Tabula recta (Vigenere). Cipher letter = plaintext letter + key letter (mod 26); decipher by subtracting.
- Key **COMERETRIBUTION** (15 letters), one of the three known Confederate keys (MANCHESTER BLUFF, COMPLETE VICTORY,
  COME RETRIBUTION).
- Only the cipher words of a telegram are enciphered; the clear words around them are left as they are. Word
  division is kept, so each cipher word has the length of its plaintext word (a word broken at a line end is
  broken in the cipher too: VW / BFVOZX = co- / -nstant).
- The key runs over the cipher letters only. It starts at C (offset 0) with the first cipher letter of each
  telegram and runs on through all the cipher words of that telegram, across the clear words.
- In all four telegrams read here (12 March, 30 March, 6 April and 8 April 1865) the key is the same, and it
  restarts at offset 0 in each. No change of key was seen. The 12 March telegram has 180 letters, 12 full turns
  of the key.

Worked example (v196-0061, first cipher word): EOHECVR under COMERET gives cavalry
(E-C = c, O-O = a, H-M = v, E-E = a, C-R = l, V-E = r, R-T = y).

`python decrypt.py` applies the key to every cipher word in `alignment.tsv` and checks the result.

## A further key, 11 April 1865: RALLY TO THE FRONT (added 15 Nov 2026)

The second telegram of 11 April on vol. 11 fr. 0046 (Surget to Maury) is enciphered with **RALLYTOTHEFRONT**
(15 letters), the same tabula recta and the same rule (offset 0 at the first cipher letter, over cipher letters only).
It is not one of the published Confederate keys and was found by search, not from a source; the first telegram on
the same page, to the same recipient, is COME RETRIBUTION. See `v11-0046b-maury_decryption.txt` and
`blind_2026-11-15/rally_key/README.md`. Worked example (first cipher word): VXLNREM under RALLYTO gives exactly
(V-R = e, X-A = x, L-L = a, N-L = c, R-Y = t, E-T = l, M-O = y).

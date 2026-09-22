# R7707 — BL Add MS 32287 ff. 37-40 (catalogue: "Unknown sender to unknown recipient")

Status: attempted, open

## What the record is

DECODE R7707, 8 images (ff. 37r-40v). The volume date 1716/1836 on DECODE is the span of Add MS 32287.

- **f. 37r**: the ciphertext, 10 lines, 205 cursive pseudo-letter signs each followed by a dot, no word division.
  Transcribed with my own labels in `ct.txt` (one line per manuscript line; `%` = the "ll" sign).
- **f. 37v**: show-through only.
- **f. 38r**: the codebreaker's frequency tally of the signs (some struck through), a small grid with "x42", and a
  list headed "Duplicates" (ʂ, t, S, p, X, l).
- **f. 38v**: contact tables, the signs before and after ɤ and after l.
- **f. 39r**: an unrelated household bill in English (bread, flour, milk, meat… 18s 11d).
- **f. 39v**: "l – vowel – e; ʂ – consonant; V – conson.; L – consonant": the codebreaker's guesses.
- **f. 40r**: a fair frequency count of 26 signs (max 16, l) and a second "Duplicates" list.
- **f. 40v**: docket "Sⁿ 4 Aout 1728 / Lˢ 31 Aout / Lˢ 5 8bre", so the letter is dated to 1728 and probably French.

No decipherment is on the record. The contemporary worksheets stop at frequency and contact analysis. Nothing
shows the codebreaker reading it.

## Analysis

- My 205-sign transcription matches the f. 40 counts closely (ɤ 14, l 13 against his 16, and so on), so the
  sign inventory (~26-27 signs) is sound.
- The "Duplicates" lists are the signs that occur doubled (ʂʂ, SS, pp, XX, ll are all in the text).
- IoC = 1.07 (normalised ×26). That is flat: any language under a simple substitution would give 1.7-2.0.
  There are no repeated trigrams. **Not a monoalphabetic substitution.**
- Periodic IoC: weak peaks at 5 (1.25), 10 (1.34) and 15 (1.29); 41-sign columns are too short to be sure.
- Tried (scripts in this folder), none gives readable text:
  - `solve.py` / `solve2.py`: mono substitution annealing, capped and injective, in en, fr, de, nl, it, es and la.
    Best about −5.1 per character; real text scores about −2.5.
  - `vig.py`: Vigenère, Beaufort and variant at periods 5 and 10, using the f. 40 tally order as the alphabet.
  - `quag.py` / `quag2.py`: an unknown sign alphabet plus periodic shifts (Quagmire-type), periods 5 and 10, in fr
    and en. The non-injective version collapses into repeated strings; the injective one reaches −4.6, no words.

## Remaining gaps

- The whole text (205 signs) is unread. Gap type: no-key-material. The cipher is polyalphabetic or otherwise
  flattened, the text is too short to break ciphertext-only (~40 signs per alphabet at period 5), and no key or
  clear copy is on DECODE or in the volume's cipher records.

## Escalation

- Siblings: the other DECODE records from Add MS 32287 (R7746-R7751, ff. 163-173) are keys dated 1833-1836 with
  Swedish plaintext, not 1728. None matches this sign set.
- Clear pages: ff. 38-40 are worksheets and a bill, with no decipherment.
- Known keys: none for a 1728 pseudo-letter alphabet in this series.
- Print: nothing found. The sender and recipient are unknown, so no calendar entry can be searched.
- Key rebuild: tried with mono, periodic and Quagmire anneals, listed above.
- Retry needs: the key, or more ciphertext in the same system (the 31 Aout and 5 8bre letters on the docket).

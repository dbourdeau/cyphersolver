# lee1813: the key of William Lee's numerical cipher, Paris, February 1813

## The cipher

A periodic (Vigenère-type) cipher with numerals for ciphertext. Lee enciphers single words or phrases inside an
otherwise clear letter; each coded stretch is written as numerals 1-25, separated by dots, sometimes with a colon
after a word.

- **Alphabet**, 25 letters, I and J one letter: `A B C D E F G H I K L M N O P Q R S T U V W X Y Z`.
- **Keyword**: `WINCHESTER` (10 letters, period 10).
- **Rule.** For the letter at position i of a stretch (i = 0, 1, 2 ...):

      plaintext  = ALPHABET[(numeral - 1 + ALPHABET.index(KEYWORD[(i + offset) mod 10])) mod 25]
      numeral    = (ALPHABET.index(plaintext) - ALPHABET.index(key letter)) mod 25 + 1

  So under the key letter W, 1 = W, 2 = X, ... 5 = A; under I, 1 = I, 2 = K, and so on (the tableau below).
- **Offset.** The key restarts at W (offset 0) at the beginning of every coded stretch. That is the rule; Lee breaks
  it often (below).

Machine-readable tableau: `key.tsv`. Check and decode: `python decode.py`.

| pos | key | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | W | W | X | Y | Z | A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V |
| 1 | I | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H |
| 2 | N | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | K | L | M |
| 3 | C | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B |
| 4 | H | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G |
| 5 | E | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| 6 | S | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R |
| 7 | T | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S |
| 8 | E | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D |
| 9 | R | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q |

Example (6 Feb, F6-04, after "The events in the north are highly"): 8 1 6 17 10 1 1 25 5 22 11 under
W I N C H E S T E R W gives D I S T R E S S I N G.

## Lee's slips

Lee enciphered carelessly. Over the three letters (123 stretches, 2,663 numerals) the key restarted at W reads 98
stretches from end to end, though often with single wrong letters; 25 stretches read only if the key position
changes inside the stretch or does not restart. The kinds of fault, each seen where the numerals are clear on the
page (`errors.py` gives one account per stretch, in `error_accounts.txt`):

1. **A wrong letter.** Usually a numeral one to three off, so a neighbouring letter: V for T, Q for R, N for C, C for
   E. 59 letters in the 6 February letter and 53 in the 2 February letter are supplied in the readings (`[x]`),
   counting wrong and missing letters together, outside the passages given only as proposals. They cluster under
   the key letter W (NOTES.md section 9).
2. **A plaintext letter left out while the key still advances** (offset +1 from that point): F6-39 (the I of HIS),
   F6-47 (the E of EFFECT), F6-51 (the T of IT), F6-52 (TEN of DISCONTENTS, offset +3), and in 2 Feb O, AM and L
   (the R of THEIR).
3. **A key letter used twice** (the key steps back one place, offset 9): F6-42 after DEPRESS, F6-01 (T twice), D
   from numeral 62.
4. **The key run on from the previous stretch instead of restarted:** F6-10 (offset 1, after F6-09), F6-62 (offset
   8, after F6-61), F6-74 (offset 9, after F6-73), 2 Feb J (after I).
5. **Larger jumps**, not explained: 2 Feb Y (offset 7 from numeral 10), AN (4 from numeral 17); G has several short
   runs. In 1 Feb F1-H the key restarts at W after PRESIDENT (offset 8 from numeral 13).
6. **Dots between figures misplaced**: two figures run together, as 11 for 1 1 (F6-02) and 17 for 1 7 (2 Feb J), or
   one figure split, as 1.2 for 12 (F6-01).
7. **A letter enciphered twice or in excess**: OFF for OF (F6-09), FORCEDD (F6-44), a stray C in DISASTRCOUS (F6-11).

The State Department clerk who deciphered the letters in 1813 met the same faults. He repaired single letters
silently where the word was obvious and stopped where the key went out of step (F6-42, F6-39, and in 2 Feb J, L, U,
V, Y).

The offset paths used in the readings are given stretch by stretch in the decryption files. Most come from a
decoder that applies one rule to every stretch: it chooses the offset path that maximises the letter 4-gram score of
the text minus 9.0 nats per offset change (fixed before the first run, not tuned), by exact dynamic programming;
each stretch is also decoded 200 times with its numerals shuffled, and z = (score - mean of controls) / sd is
reported. A few paths were chosen by hand (2 Feb D, J, L and N; 6 Feb F6-01) and are labelled so. Only stretches whose
reading is new and rests on such a path are marked § in the readings; elsewhere the clerk's decipherment of 1813
confirms the words.

## How the key was obtained

- **20 October 2026.** The letters were located on NARA microfilm T164 roll 3 (frames 0095-0115) from the source note
  of the 2 February letter in *The Papers of James Monroe*; the note at the time records that the cipher "remains
  unanalysed" (project file `research/continuation_2026-10-20.md`). Lee's own statement to Warden of 18 February
  1813, "I use my own Cipher and not that of the Government, in corresponding with the Secretary of State" (NARA T1
  roll 4 frames 0347-0348, certified copy), was found the same day and kept the cipher apart from the State Department
  codes.
- **The keyword is written on the film.** On the 6 February letter the 1813 clerk pencilled the key letters
  w i n c h e s t e r above the numerals, restarting at w for each stretch, and his plaintext below them (frames
  0108-0109, pages 1-3). The earliest note of WINCHESTER in our project files is dated **6 November 2026**
  (`research/search_space_comprehensive_audit_2026-11-06.txt`, and a note added that day to
  `research/consular_custody_sources_2026-10-20.md`): with the 25-letter alphabet, the rule above reproduced two of
  the clerk's pencilled words, DISTRESSING and MISFORTUNE, 21 of 21 letters. We found no earlier record of how or when
  the keyword was first noticed.
- **What was recovered here** is therefore not the keyword itself but the system around it: the 25-letter alphabet,
  the numeral rule (numeral - 1 added to the key letter), the restart at each stretch and the kinds of slip, tested
  first on selected passages (6 Nov 2026: 99 letters exact on passages of 1 and 6 February) and then on every
  stretch of the three letters (2 Feb, 6 Nov 2026; 1 and 6 Feb, 10 Nov 2026), with shuffled-numeral controls.
- **Whose cipher.** If the proposed reading of the opening of 6 February is right ("For the purposes of commerce I
  established with C. D. S. S. L and C. W. a cipher, a copy of which I have taken means to put in your hands"), the
  cipher was Lee's private commercial cipher, shared with Monroe. This rests on two doubtful divisions of numerals
  (F6-01, F6-02). C. D., S. S. L and C. W. are not identified, and nothing found ties the word WINCHESTER to Lee
  (NOTES.md section 12).

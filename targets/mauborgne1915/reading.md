# mauborgne1915 - reading of the cipher (English, spelling given by the cipher letters)

Marks: plain = every letter of the word comes out of `key.txt` with the rule, uncorrected; {x} = one letter of the word
was read from the sense because the key and the printed cipher letter disagree (a restored word, a hole under the README
read bar). Word division and punctuation are ours: the cipher has none. The spellings are those the cipher letters give
(pretenses, dispatches), not the British ones of the treaty text.

## Reading

A person can only be considered a spy when acting clandestinely or on false pretenses, he obtains or {endeavors} to
obtain information in the zone of {operations} of a belligerent, with the intention of communicating it to a hostile
party. {Thus}, soldiers not wearing a disguise who having {penetrated} into the zone of operations of the hostile army,
for the purpose of obtaining information, are not considered spies. Similarly, the following are not considered spies:
soldiers and {civilians}, carrying out their mission openly, entrusted with {the} delivery of {dispatches} intended
either for their own army or for ...

The cipher stops here: 499 letters, mid-sentence, where the key text ends. In the text of Article 29 of the Regulations
annexed to Hague Convention IV (1907) the sentence goes on "the enemy's army"; that continuation is not in the cipher.

## Holes: the eight words with a wrong letter (positions 1-based)

| Position | Word (read from the sense) | Raw decryption of the word | Cipher letter | Key letter | Rule gives (plain) | Can any key letter give the printed cipher letter? |
|---|---|---|---|---|---|---|
| 88 | endeavors | endeazors | U | P | Z | yes |
| 122 | operations | rperations | Y | J | R | no (parity) |
| 194 | Thus | bhus | A | N | B | yes |
| 238 | penetrated | penearated | P | F | A | no (parity) |
| 255 | of | mf | V | I | M | yes |
| 397 | civilians | civilkans | Z | S | K | yes |
| 443 | the | she | F | G | S | no (parity) |
| 462 | dispatches | dispatthes | S | A | T | no (parity) |

"Rule gives (plain)" is the letter the rule deciphers the printed cipher letter to. The word at 255 is "of" in "the zone of
operations"; in the list above the word is the one at that position of the plaintext (a two-letter word, so one wrong letter
makes it a hole).

## Count (97 words)

- 97 words in the 499 letters. 89 words come out of the key with no correction (91.8%). 8 words each need one letter read
  from the sense (8 holes, 8.2%). The two spelling differences (positions 69 and 457) are not holes: the cipher letters
  give pretenses and dispatches, and the words read as printed (the word "dispatches" is a hole for position 462 alone).
- By the README read bar (95% of the words read as sense, no restored word counted) this is 89 of 97 = 91.8%: read in part.
- The contributor's count is by letters: 489 of 499 reproduced by the rule against the plaintext with the treaty's British
  spellings, 491 with the two American spellings. Counted by letters with the American spellings as the cipher gives
  them, 491 of 499 = 98.4%. The word count is the one this target uses.

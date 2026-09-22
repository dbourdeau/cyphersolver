# Sir Edward Stafford (Paris) to Sir Francis Walsingham, 19 September 1586 (BL Harley MS 1582 ff. 74-75; DECODE R8503)

DECODE refill catalogue entry "Sr. Edw. Stafford to unknown recipient" (rule-scored class B). Worked 21 Sept 2026.

Outcome: **read.** The letter was deciphered at the time (interlinear glosses). All four cipher runs are re-read here
sign by sign, and the letter values of the key are rebuilt from the glosses.

## What the record is

DECODE R8503 (4 images: f. 74r, f. 74v, f. 75r blank, f. 75v address) is a holograph despatch in clear English from Stafford,
ambassador in Paris, dated "Paris this 19th of September 1586" and signed "E. Stafford". The address on f. 75v reads "To the
right honorable Sir Francis Walsingham knight, her Majesty's principal secretary". The endorsement reads "19 Sept. 1586. From
Sr Edw: Stafford". So the recipient is **Walsingham**, not "unknown", and the place is **Paris**, not London (London is where
the manuscript is now held).

Contents (f. 74r): the ambassador's report that has caused astonishment in England; Mary Queen of Scots and the King of France;
Mendoza and "that vile traitor Charles Paget", who went to the Capuchins to speak with the King; Paget's claim that he will be
received by the King. f. 74v: a copy of a letter "of Villequier" about Épernon; an attempt against the Queen; the King of Navarre
warned of three men sent to kill him and the Prince of Condé, some of them of the Duke of Guise's guard; the Queen Mother's
new powers to treat with Navarre; the point of religion.

The cipher is only four short runs on f. 74v. Each has a contemporary decipherment written above it in darker ink:

| run | line | ciphertext | gloss | reading |
|---|---|---|---|---|
| 1 | 2-3 | `D x ◇ 6 ◇ 6 / Δ Ɗ X 6 · ⊕ 6 ꟻ ʃ ⊗` | villequier | "a letter of **Villequier**('s) to come about Espernon" |
| 2 | 11 | `47` | K. Navar | "**the King of Navarre** be advertised of it that there are three fellows sworn" |
| 3 | 12 | `M x ◇ h 6 47 ω ʒ ϖ 59` | Kyll him and ye P. of Condé | "dispatched to **kill him and the Prince of Condé**, whereof some are" |
| 4 | 13 | `74` | D. Guise | "of the guard of **the Duke of Guise**, who assure themselves to bring it to pass" |

## Key rebuilt from the glosses

Letters, with homophones: v = D, i/y = x and ⊕, l = ◇ and h, e = Δ and ꟻ, q = Ɗ, u = X, r = ʃ, k = M. Run 1 spells
v-i-l-l-e-q-u-i-e-r across the line break (D x ◇ ◇ | Δ Ɗ X ⊕ ꟻ ʃ) once the four `6` signs are dropped; ⊗ is a final s ("Villequier's")
or a stop. Run 3 spells k-y-l-l (M x ◇ h) with the same x and ◇, then `6` again, which confirms `6` as the null. ω ʒ ϖ = "and"
(a word sign or three letters; not split). Codes: 47 = King of Navarre (read as "him" in run 3), 59 = Prince of Condé, 74 = Duke of Guise.
`·` is a separator. Every sign is accounted for; no key sheet for Stafford's Walsingham cipher was found (Tomokiyo's cryptiana
Elizabethan page only notes that Stafford used different ciphers for Walsingham and Burghley and added names to Walsingham's).

Files: `ciphertext.txt` (28 tokens with the separator, 20 distinct, measured), `plaintext.txt`.

## Prior art and print

CSP Foreign Elizabeth XXI part 1 (September 1586, 16-30, British History Online pp. 89-104) calendars Stafford's SP 78
letters of that month but not this one: it is a Harley manuscript, outside the State Papers. No printed decipherment found.
The reading was made at the time by Walsingham's office; the sign-level check and the key values are new here.

## Remaining gaps

None. ω ʒ ϖ is read as "and" from the gloss without splitting it into letters.

## Escalation

- [x] siblings: none needed; all four images of R8503 read (f. 75r blank, f. 75v address)
- [x] clear-pages: the glosses on f. 74v are the decipherment
- [x] known-keys: Tomokiyo's cryptiana Elizabethan page checked; no Stafford-Walsingham key published
- [x] print: CSP Foreign XXI pt 1, September 1586 (BHO pp. 89-104): letter not calendared
- [x] key-rebuild: letter values rebuilt from the glosses; null 6 confirmed across runs 1 and 3
- [x] retry: all four runs re-read with the rebuilt values; all agree with the glosses

Images are BL material behind the DECODE login: kept git-ignored in `img/`.

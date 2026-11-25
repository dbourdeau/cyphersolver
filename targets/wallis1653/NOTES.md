# Wallis's undeciphered "challenge" letters, nos. 50-53 of his 1653 cipher collection (Unsolved Catalogue no. 470)

Status: in progress

One of the four is already deciphered in print: **no. 52, the Duke of Buckingham's letter, was printed with an
interlinear decipherment and a key by John Davys in 1737.** The other three (nos. 50, 51, 53) have not been seen:
the Bodleian manuscripts are not digitised and no printed or online copy of their ciphertext was found. They are
blocked on access (order images of MS. e Mus. 203 pp. 218-226 / MS. Eng. misc. e. 475 pp. 234-247).

Under the one-key rule, the four letters are probably four different ciphers, from different senders (Brasset;
an unknown writer in Scotland; Buckingham; Townesend) and dates (1651-1658). They stay together here only until
images of nos. 50, 51 and 53 are in hand. Then split them.

## The documents

Wallis, *A Collection of Letters and other Papers, which were at severall times intercepted, written in Cipher.
Deciphered by John Wallis*, given to the Bodleian in 1653 (MS. e Mus. 203, SC 3524). There are two more copies in his
hand: MS. Eng. misc. e. 475, given to the Savilian study; and a private copy sold at Dominic Winter, 7 Oct 2020,
lot 375, for £29,000. The private copy has 223 pp. and **53** letters; the auction text says the Bodleian
copies have 52. The last four letters in the private copy carry no decipherment or key.

| no. | letter | EMLO | ciphertext seen | state |
|---|---|---|---|---|
| 50 | Henri Brasset (French resident, The Hague) → Antoine de Bordeaux-Neufville (London), 4 Apr 1653, French | cb69093b | no | not seen; blocked on access |
| 51 | unknown, Scotland, 16 Jan 1651 | 3329a9ec | no | not seen; blocked on access |
| 52 | George Villiers, 2nd Duke of Buckingham, undated (1651), English | 86e81b88 | **yes, Davys 1737 pp. 24-25** | **deciphered by Davys 1737**, 456/480 groups |
| 53 | Peter Townesend, Flanders, 5 May 1658 | eef01c0b | no | not seen; per the auction text only in the private copy (EMLO lists a manifestation for it, unchecked) |

Davys (1737, p. 23) speaks of **three** undeciphered letters in the Bodleian copy: "one is written in French, and
the other two in English". These are nos. 50, 51 and 52. That fits the auction text's claim that no. 53 was added
later to the private copy only.

## No. 52: Davys 1737

John Davys, *An Essay on the Art of Decyphering. In which is inserted a Discourse of Dr. Wallis* (London: Gilliver
and Clarke, 1737). The copy used here is archive.org `bim_eighteenth-century_an-essay-on-the-art-of-d_davys-john_1737`.
The letter is on leaves n31-n32 (pp. 24-25), the key on n33-n34 (pp. 26-27) and Davys's remarks on n34-n36
(pp. 27-29). The page images are git-ignored and can be fetched from
`https://archive.org/download/<id>/page/n<leaf>.jpg`. Davys writes that he found the letter in the Bodleian
manuscript, that it had lain "undisturbed by any but myself" for over eighty years, and that it "is at last very
nearly decyphered". Wallis's manuscript itself told him only that the letter came from the Duke of Buckingham.

- `letter52_davys.txt`: the ciphertext transcribed from the page images, line by line, with Davys's interlinear
  reading aligned group for group. The address, the opening ("Sir, Since I sent to you last") and the closing ("I am
  with great trust Your most affectionate Friend and Servant") are printed in clear.
- `check52.py`: builds Davys's key from the alignment, lists clashes and counts the reading.

**Measured** (`python check52.py`): 480 cipher groups, 156 distinct (`docs/_check_profile.py --measure letter52_ct.txt`), 137 of them given a value. **456 are read (95.0%; one of them, 291, by Davys's emendation) and 24 are
open.** The clashes are all trivial: case, i/I and u/v. Two values are forced: 118 is "county" and is also used
for "counte-" in "counte-na-n-ce"; 144 is "dy" in "ready" and "di" in "credit".

**System.** Numbers 1-65 are single letters with 2-3 homophones each (a 10/28/59, e 23/32/60, o 3/51/62,
v 18/54/63, w 26/40/64, y 19/41/65 ...). Numbers 66-455 are an alphabetical table of syllables and words mixed
together: 82 able, 83 and, 104 ba, 105 be, 107 bo, 108 bu, 112 Cromwell, 114 Colonel, 118 county, 127 ca ... 422 to,
442 we, 449 will, 455 you. The groups 460-506 stand outside the table; Davys took them to stand for numbers. In
short: a two-part, partly alphabetical nomenclator of the 1650s royalist kind. The text is English.

**Content.** Buckingham to a royalist in or near Lancashire, written before Charles II's march into England in
August 1651. The gentlemen of Lancashire "are ready to rise for us" and ask for a party of [50?] horse "from hence
to countenance their rising", confident they can engage Cromwell within [8?] days "without any other assistance".
The Lords in Scotland (71, 254) send word that, on the first drawing together of the army, they will send [50?] of
their best horse and as many good Highland foot, under the command of 277 and Buckingham. Buckingham has leave to
raise a troop of English horse, which within [8?] days will be near [50?] good men. He has chosen to go this way
into England, believing he can do the King more service so than by going in disguise to stay anywhere about London.
The bearer, Colonel Berkenhead, will give a particular account of the whole business. Berkenhead "has been the
main negotiator of the Lancashire business".

### Open groups in no. 52 (24, plus one emended)

| groups | where | Davys (pp. 28-29) | state |
|---|---|---|---|
| 460 482 83 497 382 113 | line above "Sir" | "may contain a Date, or a Direction, or both"; 83 = and | 5 open |
| 492 505; 479 506; 479 505 | "a party of __ horse", "__ of our best horse", "near __ good men" | number codes; strike the first group and the last figure of the second → 50 | Davys's rule, unproven: [50?] |
| 487 (×2) | "within __ days" | strike both outer figures → 8 | Davys's rule, unproven: [8?] |
| 7 42 68; 66 68 | "to countenance __ their rising"; "assistance __ Upon this" | printed as dashes | open; 68 occurs twice, so possibly a null or a punctuation sign |
| 8 | "I shall be able to do the King more service __ so then if I went in disguise" | dash | open |
| 7 20 | after "business" at the end | dash | open |
| 71 | "this 71 and 254 and some other lords of great interest in this Kingdom" | Argyle (guess) | open name; 71 lies in the a-block (66-89), which fits a name in A |
| 254 | ditto | Lauderdale (guess) | open name; between 252 lord and 258 London, so it fits an L name |
| 277 | "under the command of 277 and Buckingham" | Leslie (guess) | open name; between 275 ly and 279 man, so an L or M name. Massey, who commanded the English royalists in 1651, is an alternative [?]. Not decided |
| 291 | "the who[le?] business" | the print shows "291." over a dotted gap, with "(271.)" under it: Davys emends to 271 = le | counted read, uncertain: [le?] |

So no. 52 has been deciphered since 1737, and it is not an open challenge. What Davys left open is the
address line, three or four number codes, three names and a few signs printed as dashes. They are all
short and scattered, and nothing outside the text was found to settle them.

## Nos. 50, 51, 53: where things stand

- **Images.** EMLO lists no images. Digital Bodleian has none under these shelfmarks (search 27 Oct 2026). The 2020
  auction lot has eight photographs online (`dominicwinter.goauction.co.uk/stock/672552-<0..7>-medium.jpg`):
  the binding, the title page, Wallis's preface signature, a key page, the Lauderdale-to-Carlisle letter, the
  provenance inscription, and the King's Newcastle letter in cipher and in clear. None shows letters 50-53.
- **Print.** Davys printed only no. 52. Wallis's *Opera mathematica* iii (1699) prints two other deciphered
  letters. Smith, "John Wallis as a cryptographer" (Bull. AMS 24, 1917), works from BL Add MS 32499 and does not
  print them. Not yet checked: Beeley, "Breaking the Code: John Wallis and the Politics of Concealment" (2016).
- **Crib for no. 50.** The Thurloe State Papers, vol. i (April 1653), has no Brasset letter, only Bordeaux's
  despatches to Brienne. Brasset's correspondence with Bordeaux would be in AE Correspondance politique (Hollande or
  Angleterre), which is not online. `targets/bordeaux/` has Bordeaux's own cipher of 1653-54 (key R7537). Test it
  on no. 50 once the ciphertext is in hand.
- **Prior art.** Davys 1737 for no. 52 (above). For nos. 50, 51 and 53 nothing was found on the web or on
  cryptiana. The "French cipher unsolved by Wallis" on cryptiana is a different item: Louvois 1690, solved by
  Biermann 2020.

## 14 Nov 2026: texts audit (sections I and J)

- No. 52: `letter52_plain.txt` read as sentences. It runs as one coherent English letter; the 24 open groups (address
  line, number codes, three names, dash groups) break no sentence. Reading review recorded in `profile.json`, grade A,
  state read (456 of 480 groups, 0.95). `check52.py` re-run: same counts.
- Nos. 50, 51 and 53 were documents B, C and D of `profile.json` with zero tokens. No ciphertext of them was ever in
  hand (see "Nos. 50, 51, 53: where things stand"), so there is no transcription or decryption to list, and none can
  be made from here: the Bodleian manuscripts are not digitised. They were removed from `documents[]`; the profile now
  describes no. 52 only. They stay the open catalogue entry no. 470 and the first gap below. If images arrive, they
  become their own targets (probably three different ciphers).

## Remaining gaps

- Nos. 50, 51 and 53: needs physical access (Bodleian MS. e Mus. 203 pp. 218-226, Eng. misc. e. 475 pp. 234-247;
  no. 53 may be only in the privately owned 2020 copy).
- No. 52: open codes only (above). Its address line has 5 open groups.

## Escalation

- Siblings: in the same volume, Wallis's 49 deciphered letters and keys are not digitised. They are the next place
  to look for a key to no. 51 (Scotland 1651, the same months as no. 52) and for the names in no. 52.
- Print: Davys 1737 was checked and gave the decipherment of no. 52. Still to check: Beeley 2016 and the EMLO
  manifestation for no. 53 ("MS. 19336" pp. 203-219, an unidentified shelfmark).
- Known keys: the Bordeaux 1653 key (R7537) is waiting for the ciphertext of no. 50.
- Retry: order images from Bodleian Imaging Services for MS. e Mus. 203 pp. 218-226.

## Files

- `letter52_davys.txt`: transcription of no. 52 with Davys's reading; `letter52_ct.txt` the cipher groups alone. `check52.py`: key, clashes, count.
- `src/davys1737_djvu.txt`: archive.org OCR of Davys 1737 (poor on the numbers; use the page images).
- `img/` (git-ignored): Davys leaves n30-n35 and the auction photographs.

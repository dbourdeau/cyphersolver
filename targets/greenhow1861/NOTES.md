# Rose Greenhow, letter in cipher on mourning paper, 1861: side 1 read in part with the 1864 key (catalogue 644)

Status: read in part. Side 1 decodes with the 1864 Greenhow key (NARA M1091 image 0484) into coherent sentences
between paper losses; side 2 and the numeral fragment are not read. No earlier decipherment of this letter was found
(bounded search, below). Contributed by WAINUT (https://github.com/WAINUTAI), 27 Oct 2026; the work was done with AI
language-model agents, and side 1 and the key were each read twice, independently, on the NARA images.

## The document

NARA RG 59, Seized Correspondence of Rose O'Neal Greenhow (entry A1-986), **naId 1634036**, "Letter Written in Cipher
on Mourning Paper by Rose Greenhow": <https://catalog.archives.gov/id/1634036>.

- Image 1: side 1, about 17 lines of signs in ink with a few clear words ("is", "the", "this"), on a black-bordered
  mourning leaf that survives in fragments laid on a backing. Heading "P 31 ?" (not read).
- Image 2: side 2, two ink lines at the top; the rest is show-through.
- Image 3: a separate scrap in figures with a few clear words (`transcription_numerals.txt`).
- Image 4: docket "Written in Characters by Mrs G - on Mourning Paper. Fragments of a Letter".

The Library of Congress / World Digital Library copy (wdl.2706) and the Santa Clara University exhibit (item 3281)
show the same letter and date it 23 Aug 1861, the day of her arrest and the seizure of her papers. The writer is
presumed to be Greenhow and the addressee her Confederate contacts (Thomas Jordan, Beauregard's headquarters), as the
catalogue says; the letter itself names neither.

## The key

The 1864 Greenhow key, NARA RG 45, M1091, file "DC - Codes and cryptography - Miscellaneous", **naId 62017285, image
0484** (image 0485 is a photostat of the same sheet): <https://catalog.archives.gov/id/62017285>. Docket: "found on the
person of Mrs Rose O. Greenhow, who was drowned in trying to land from the Br. S.S. Condor off Fort Fisher, 1864".
Header: **"Lamb Papers CXXIX. Copied A. H. L."** (last initial uncertain), not "Pickett Papers XXIX". Image 0483
("Confederate cipher 1864", white on black) is a different table and does not apply. Table: `key_1864.md`.

Points checked on the signs of side 1:

- G and U are distinct: plain 8 = G (BEING, GAVE, MORNING), struck 8 = U (BUT, HOURLY, BUISY, OUT). I and R are
  distinct: crossed 4 = I, looped 4 = R. Both as on the key.
- N has two forms. The ?-form of the key sheet (BEING, MORNING, FIND) and a looped l with a crossbar (LELAND,
  PANICK, the second N of MORNING). The second form is not on the key sheet; its value comes from context, and every
  word that contains it is otherwise keyed.
- A in her hand is a cross with a hook ("7+"); in GAVE it looks like "47" [?].
- Doubled letters are written twice (ATTACK, WILL, EFFORT, FERRY). The key sheet's rule "2d letter itself inverted"
  is not seen here.

## Transcription and decryption

- `transcription_side1.txt`: side 1 in neutral shape labels, line by line (the second, independent reading; the
  first, by key value, agrees). `ciphertext_side1.txt`: the 183 signs alone, for the count.
- `decryption_side1.txt`: the key applied line by line, with the line read as words.
- `decode.py` applies the key to the labels and runs the controls (`decode_output.txt`; standard library and the
  repository's English word list `lang/lexicons/en.json.gz`).
- `transcription_side2.txt`, `decryption_side2.txt`: side 2, decoded, not read.

## Reading (side 1)

`reading_side1.md`. Clear words in italics there; [x] = supplied at a loss or a missing sign; [?x] = conjecture.

> Al[?l] is acti[vi]ty. McLeland (McClellan) is buisy. Myste[...] a[...] [...]but the panick is gr[?ea]t. A[...]
> [...]y. Attack is hourly expected. They beleive this: the atta[ck] will [b]e simultaneou[s] fr[om] [...]r[?d]s
> Ferr[y], [...] [?Bal]timore. [...]y eff[o]rt is being made to find out who g[?a]ve the alarm. A tro[?op o]f cavalry
> u[...] [...]nt fr[o]m here [?th]is morning. L[...] Harpe[?r's F]erry [...]ont.

Corrections from the second reading, applied:

- **EXPECTED**: the key gives EXPEC-R-TED. There is an extra R-sign between C and T on the leaf; a slip, not
  something the key explains.
- **SIMULTANEOU[S]**: no S-sign is written; the word ends in the struck-8 U and a dot, then the clear "fr...".
- **EFF[O]RT**: no O-sign; line 10 ends E F F at the ruled border and line 11 starts R T.
- **GR[EA]T**: G, R and T are clear; E and A sit on cracks and are uncertain.
- **"[Edwa]rds Ferr[y]"**: only R d S - F E R R is on the paper, and the d is uncertain. "Edwards Ferry" is a
  conjecture. **"[Bal]timore"**: TIMORE is clean; "Bal" is a conjecture.
- **HARPE[R'S F]ERRY**: line 16 ends H A R P E at the edge; line 17 starts after a loss with E R R Y. The restoration
  is plausible, not read.
- **A TRO[OP O]F CAVALRY**: A T R O, a loss, F, then CA|VALRY; "troop of" is a conjecture that fits the loss.

Measured: with every supplied letter and conjecture counted as a hole, 0.492 of the words read as sense: 30 whole
words and 31 holes in the reading body (`research/reading_audit/v10_relabel.py`, `share`; recounted 14 Nov 2026 after
Brice Dudout's check, PR #572). The figure recorded before, 0.595, was `v2_score.py`'s hole rate (0.405 over 42
word tokens), a different count; `v10_relabel`'s share is the one used for `read_share` across the project. That is why the document is "read in part", not "read".

Context: written in Washington in the weeks before 23 Aug 1861 (McClellan took command at Washington in late July 1861).
The panic in the city, an attack hourly expected, a search for whoever "gave the alarm", cavalry movements, and
Harper's Ferry fit the summer after First Bull Run. NARA naId 1634043, "Pasted Fragments of a Letter Mentioning Gen.
George McClellan and Movement of Troops", is a clear pencil draft headed "10 Aug. 1861" in the same file ("The
movements are very active ... McClellan is very active and very discreet ... an attack is apprehended by McClellan").
It is not a copy of this letter, but it is close in theme and wording and supports the dating.

## Controls (`decode.py`, side 1)

| test | whole cipher words in the English word list (of 27) | mean bigram log-likelihood |
|---|---|---|
| the 1864 key | **17** | **-2.49** |
| 2,000 random substitution keys | mean 0.5, max 5 | mean -4.72 (sd 0.40), max -3.64; key z = 5.6 |
| key shifted by one letter | 4 | -4.24 |
| true key, signs shuffled inside each word (500 runs) | mean 2.6, max 6 | mean -3.37, max -3.10 |

The word count understates the fit: her spellings (BUISY, PANICK, BELEIVE, LELAND) and the words cut by losses do
not count as hits. (The second reader's own run, with a different 10,000-word list, gave 16/27 against a random-key
maximum of 5.)

## Earlier work

- Not new as a method: the Rosenbach applied the same family of key to another Greenhow note in 2011, and the North
  Carolina State Archives hold a copy of the key (Greenhow Papers 1863-64).
- No decipherment of this letter was found: the NARA record has no scope note and no decipherment; the LoC/WDL and
  Santa Clara copies give none; phrase searches ("hourly expected", "who gave the alarm", "panic is great",
  "simultaneous" with Greenhow) found nothing.
- Print (review, 27 Oct 2026): the archive.org texts of the Official Records Ser. II vol. 2 (the Greenhow case papers,
  pp. 561-577), Pinkerton's *Spy of the Rebellion* (1883) and Greenhow's *My Imprisonment* (1863) were searched for
  the side-1 phrases ("hourly expected", "gave the alarm", "panic", "simultaneous", "Harper's Ferry", "cavalry") and
  for "mourning": none prints this letter or a decipherment of it. OR II 2 p. 561 says the cipher letters were found
  torn in the stove and some fragments "assorted and placed together so as to be read and copied"; pp. 564-565 print
  Jordan's letter to Benjamin of 29 Oct 1861 (he arranged the cipher "last April", wrote under the alias Thomas John
  Rayford, and thought the War Department "ought to have worked out the key"). Greenhow (1863, pp. 76-77) says the
  agents puzzled over her cipher scraps for seven days. Fishel (1996) and Blackman (2005) are lending-library copies
  on archive.org whose text could not be searched; web searches for the phrases with either book found nothing. A
  period Union decipherment cannot be excluded.
- NARA naId 6925618 ("Copy of a Letter Fragment Partially Written in Cipher", catalogue 646) is a different letter:
  it is Jordan's letter to "Rachel", see `../jordan1861/`.

## Proposed catalogue corrections (entry 644)

- status: the key is M1091 **image 0484** (and its photostat 0485); image 0483 is a different table. Header "Lamb
  Papers CXXIX".
- status: side 1 decodes with that key into sentences (attack hourly expected, simultaneous attack, who gave the
  alarm, a troop of cavalry, Harper's Ferry); side 2 and the numeral scrap are not read.
- date: LoC/WDL and Santa Clara date the letter 23 Aug 1861 (the seizure); the text fits late July to August 1861.
- Suggested status: read in part, key identified; no earlier decipherment found.

## Remaining gaps

- Side 1, paper losses (al[l], acti[vi]ty, atta[ck], [b]e, Ferr[y], eff[o]rt, tro[op o]f, [th]is, Harpe[r's F]erry) - blocker: illegible; lost with the paper, restorations marked.
- Side 1, torn clear words (myste.., a.., u.., l..) and the heading "P 31 ?" - blocker: illegible.
- Side 1, "Edwards Ferry" and "Baltimore" - blocker: illegible; conjectures only.
- Side 2 - blocker: illegible; two ink lines, fragments only (gr..e, tim.., bo.., [or]ganising). Line 2 re-read on
  the image on 14 Nov 2026 (`VERIFY_dudout_20261114.md`): GANISING, not GANI[Z?][?]ING.

## Independent verification by Brice Dudout (PR #572, 14 Nov 2026)

Brice Dudout (PR #572, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) applied the label legend of
`transcription_side1.txt` to the 183 signs of side 1: 17 of 17 lines equal `decryption_side1.txt`. Re-run here: same.
He re-read side 2 line 2 on NARA image 2: `G A N I [Z?] [?] I N G` is `G A N I S I N G`, "[or]ganising"; the "[Z?]"
was the two extra strokes of the I sign and the unread sign is the torn lower half of the S box. Sign count 17,
distinct 11, unchanged. He also notes that the G of MORNING is a closed 8 with a stroke and the U of OUT an open $,
so it is the closed or open form, not the stroke, that tells G from U; no reading changes. The side-2 re-read was not
repeated here on the image (the NARA catalogue returned no image link to a script this session); it is taken on his
record. Side 2 stays decoded, not read: one word and three fragments.
The read share of side 1 was recounted: 0.492 (see "Measured" above). No key correction.
- Numeral fragment (image 3) - blocker: no-key-material; tested against the 1864 key in review (`numerals_test.py`):
  the key writes figures as letter-like signs (1 a, 2 d, 3 phi, 4 ff, 5 m, 6 b, 7 nn, 8 c, 9 c; 10 III), so these
  Arabic figures are not its numbers; read as its digit-like letter signs they give no words (11 of 33 groups hold a 2
  or 6, which has no value). The scrap reads as a money reckoning ("$5 dollers $25", figures 5 to 104); the three
  key-like signs on its last line (S, M, E) are too few to read.

## Escalation

- [x] siblings: Jordan's letter to "Rachel" (`../jordan1861/`) reads with the same key; NARA 1634043 (clear draft,
  10 Aug 1861) read for context.
- [x] clear-pages: no clear copy of this letter on the NARA images; 1634043 is not one.
- [x] known-keys: the 1864 key (M1091 image 0484) fits; image 0483 tested and does not.
- [x] print: OR Ser. II vol. 2 (Greenhow case, pp. 561-577), Pinkerton 1883, Greenhow 1863 searched: not printed;
  Fishel and Blackman by web search only (full text not reachable).
- [n/a] key-rebuild: the key is known; only the second N form was added from context. The key's figure row tested on
  the numeral scrap in review: no fit.
- [x] retry: side 1 re-read independently in shape labels; the corrections above come from that pass.

## Review (Claude, for Daniel Bourdeau, 27 Oct 2026)

- Print step done (Earlier work, above): nothing printed.
- Numeral scrap tested against the key's figure and letter signs (`numerals_test.py`, `numerals_test_output.txt`):
  no fit; blocker stays no-key-material.
- Side 2 counted: 17 signs read (`ciphertext_side2.txt`), no clear words; fills the two "unknown" profile fields.
- Reading re-read against `decryption_side1.txt` and image 1 (lines 4-9 sign by sign): grade **B**, not A. The
  sentences cohere, but 9 of 15 carry losses or conjectures.
- Method unchanged: no decipherment of this letter existed, so "read after matching with key from external sources"
  stands.

## Files

`transcription_side1.txt`, `ciphertext_side1.txt`, `decryption_side1.txt`, `reading_side1.md`,
`transcription_side2.txt`, `decryption_side2.txt`, `transcription_numerals.txt`, `key_1864.md`, `decode.py`,
`decode_output.txt`, `numerals_test.py`, `numerals_test_output.txt`, `ciphertext_side2.txt`. No images are kept here; they are on
the NARA catalogue pages.

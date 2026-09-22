# Andreae, *Chymische Hochzeit Christiani Rosencreutz* (Strassburg 1616): DECODE R4502

Catalogue 210 ("Johann Valentin Andreae to unknown recipient", scored by rule). Worked 22 Sept 2026.

**Outcome: explained; not a letter, and already read.** R4502 is not a ciphered letter. It is a copy of the first
printed edition of the *Chymische Hochzeit* (Strassburg: Lazarus Zetzner's heirs, 1616; colophon Conrad Scher),
held at the Embassy of the Free Mind (Ritman Library), Amsterdam. DECODE's "four pages with ciphertext" are the four
printed openings that carry the novel's secret-script inscriptions (DECODE images P3-P8; P1 is a thumbnail, P2 the
title page, P5 the colophon and P6 pp. 98-99 have no cipher). The owner's note on DECODE says "as far as is known, this
has never been deciphered". In fact the novel deciphers its two long inscriptions itself in the next paragraph, and
English editions have printed them in clear since Foxcroft's translation (1690).

## The four inscriptions

| Page | Where in the story | Kind | Reading |
|---|---|---|---|
| p. 73 (Day IV) | under the Hermes Princeps fountain inscription, after *BIBITE FRATRES, ET VIVITE* | line of alchemical/numeral signs | a date; 1378 in the crcsite.org edition (footnote 12), graded C here |
| p. 95 (Day V) | the copper door to Venus's vault | letter cipher, 70 letters | HIE LIGT BEGRABEN VENUS DIE SCHON[E] FRAW SO MANCHEN HOHEN MANN UMB GLUCK EHR SEGEN UND WOLFART GEBRACHT HATT |
| p. 97 (Day V) | the tablet behind Venus's bed | letter cipher, 86 letters | WAN DIE FRUCHT MEINES BAUMS WIRT VOLLENDS VERSCHMELZEN WERDE ICH AUFWACHEN UND EIN MUTER SEIN EINES KONIGS |
| p. 116 (Day VI) | after *Anno* on the urn inscription | line of signs | a date; 1459 in the crcsite.org edition (footnote 21), graded C here |

On p. 95, *VENUS* and *HOHEN* are printed in Roman capitals above the cipher line and are not enciphered.

The novel glosses both letter inscriptions in the paragraph that follows each one. The page boy says "hie ligt begraben
(sagt er) Venus die schöne Fraw / so manchen hohen Mann umb Glück / Ehr / Segen und Wolfart gebracht hatt" (p. 96).
The boy reports Atlas's words "wann der Baum ... wirdt vollends verschmeltzen / so wirdt Fraw Venus wider erwachen /
vnd sein ein Mutter eines Königs" (p. 98).

## The cipher

A simple substitution in an invented alphabet, cut as type: one sign per letter, words divided, no nulls or code, and
one capital form (the initial H). U and V share a sign. M, N and O are three dotted variants of one base shape, so
they are hard to tell apart at DECODE's resolution. The sign table is in `key.tsv`; it uses 19 distinct signs in 156
letters (`python docs/_check_profile.py --measure andreae1616/ciphertext.txt --letters`). `ciphertext.txt` is the
transcription in stand-in letters, and `decode.py` reproduces `reading.txt` from it. Every sign that occurs has a value.
Only 20 letters of the German alphabet occur (no J, P, Q, X, Y). The alphabet is Andreae's own; no historical key is
known or needed.

**Transcription caveat.** The three dotted M/N/O variants were assigned with the plaintext in view: the dots are
too small at DECODE's resolution (about 1450 px per opening) to separate the signs blind. The other 16 signs are
unambiguous, and they alone fix the text (B-E-G-R-A-B-E-N, F-R-A-W, G-L-U-C-K, F-R-U-C-H-T, B-A-U-M-S and so on).

## The two sign lines (pp. 73, 116)

These are not letter ciphers. They are strings of alchemical, planetary and Roman-numeral signs, read as dates.

- **p. 116**, printed after "A[nn]o.": four ring signs, then signs including XIX and M, then a ligature group
  (P.H.M.D., which crcsite.org reads as "Paracelsus Hohenheimensis Medicinae Doctor"). The rings as CCCC, the IX
  and the M fit M CCCC L IX = 1459, the year on the title page ("Anno 1459"). Graded C: the value 50 (L) is not
  identified with certainty in the signs.
- **p. 73**: a lemniscate with three dots (∞, an old sign for 1000; the dots possibly CCC), two angle signs, XX,
  a reversed C and I, V with dots, and a closing group. That fits the crcsite reading 1378, the birth year Fama/Confessio
  give Christian Rosencreutz (M CCC LXX VIII). Graded C: the signs for L and the III are not identified individually.

## Prior work (contamination)

- The novel itself (1616): both letter inscriptions glossed in the following paragraph.
- Ezechiel Foxcroft, *The Hermetick Romance* (London 1690), and the crcsite.org online edition built on it, footnotes
  12, 14, 15 and 21: English readings of all four
  (https://www.crcsite.org/rosicrucian-library/chymical-wedding4/ , -5/ , -6/).
- Deutsches Textarchiv (valentin_hochzeit_1616) and 12koerbe.de render the inscriptions only as `<figure/>` or leave them out.
- Found before the reading here. The key was rebuilt from the images with the novel's glosses as cribs.

## DECODE corrections

R4502 is a printed book, not a letter; there is no sender or recipient. The catalogue title "Andreae to unknown recipient"
came from the rule scorer. Place of printing: Strassburg (today France). Status should be Decrypted: the novel glosses the two
long inscriptions and the crcsite edition reads the sign lines. Cipher type is simple substitution (plus two symbolic
date lines), not "unknown". Queued in `decode_updates/queue.json`.

## Remaining gaps

- p. 73 and p. 116 sign lines, individual numeral signs - blocker: too-short; each is a one-off symbolic date of about 10 signs and fits the edition's reading (1378, 1459) as a whole, but no second example exists to fix the value of each sign

## Escalation

- [x] siblings: the DECODE owner notes three Ritman copies, only one uploaded; the 1616 edition has fixed type, so the copies carry the same inscriptions
- [x] clear-pages: the novel's next paragraphs gloss both long inscriptions (pp. 96, 98)
- [n/a] known-keys: the alphabet is the author's invention for this book; no archive key exists or is needed
- [x] print: DTA, 12koerbe, crcsite.org (Foxcroft 1690) checked; crcsite reads all four
- [x] key-rebuild: full sign table rebuilt from the images; every sign that occurs has a value
- [x] retry: both date lines re-read against the edition's dates; structure consistent, per-sign values graded C

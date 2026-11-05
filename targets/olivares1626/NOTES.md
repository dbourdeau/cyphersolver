# The Count-Duke of Olivares to the Duke of Alba, Madrid, 22 August 1626 (lead 1273)

Status: read (Brice Dudout, 5 Nov 2026; Daniel's rule: 953 of 1,001 words read from the sense, 95.2%, without restorations; key partial by our protocol: one held-out measurement, M5 0.506 against 0.144 for the best control, under our 0.60 threshold, with a ceiling of about 0.64; about 54 line ends lost in the gutter not counted; DECODE R1190 lists the letter as "Decrypted", but no decipherment or key is attached there).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents, for your lead 1273 (BNE/Hispana sweep).
Not yet published on our site. Text only: the BNE Digital images were used for research and are not reproduced here.

## Document

Madrid, Biblioteca Nacional de España, MSS/10249 ("Papeles varios", Osuna; BDH bdh0000042230), ff. 13r-15r (PDF pp. 16-18).
One letter wholly in cipher except the closing "guarde Dios a V.E. como deseo", the dateline "De Madrid a 22 de Agosto 1626" and the
signature "Don Gaspar de Guzmán"; docket "Madrid 22 de Agosto 1626 / El Conde de Olivares / Respuesta". The addressee is Antonio Álvarez
de Toledo, 5th Duke of Alba, then viceroy of Naples. A covering letter in clear of the same day (f. 11r) says that Olivares gives the Duke
account of his griefs and "del estado de mis cosas ... en otra carta que aquí le remito": this letter. The lead's "undated" can become
22 Aug 1626 (your vetting of 4 Nov 2026 found the same date).

Content. Olivares tells of the griefs of summer 1626: the death of a young Guzmán nephew whom he meant for the Church; the stillbirth
of his daughter María (a granddaughter lost), her recovery, then her death; her virtue. He keeps her widower, Ramiro Núñez de Guzmán,
Marquis of Toral, as son and heir of his house: the dukedom of Medina de las Torres on the commandery of Caravaca, granted by the King
at the marriage; the office of sumiller de corps, which the King gave Ramiro "motu propio" (in Barcelona); he offers his life to the
King's service and hopes that "el Duque mi hijo" will behave wisely. The facts agree with the known chronology (María de Guzmán y Zúñiga died
in 1626, RAH DB~e; Ramiro Núñez de Guzmán became Duke of Medina de las Torres).

## System and key

Philip IV's general cipher "A", the one we rebuilt from the Santa Cruz pairs of 1630-1632 (`targets/santacruz1630`, key K6A): a
homophonic syllabary of letter groups (fer = de, xer = me, fan = que, pon = co ...), numbers for letters and syllables, special signs,
and a nomenclator (fro = Dios, ber = servicio, 199 = hija ...). This letter shows the cipher already in use in August 1626.
`key.tsv` (K_OA1) = K6A + 20 values learnt on the training part A only, by reading and from a fixed list of probable words, listed in its
header; frozen by SHA-256 before the held-out part was transcribed.

## Validation

`validation.txt`. The protocol was hashed before any measurement. Split by manuscript lines: training part A = ff. 13r-14v l.17;
buffer T = f14v.18-20; held-out part H = f14v.21-27 + f15r (542 tokens, 20.7%), transcribed only after the key was frozen and hashed
before decoding. There is no contemporary decipherment, so the measure is M5: the share of decoded letters covered by Spanish words of
at least 5 letters (your `lang/lexicons/es.json.gz`). The control is 200 keys whose values are shuffled within length classes. That
control was set by an amendment written before H was transcribed, because the free shuffle beat the true key on A. Criterion fixed in
advance: M5 >= 0.60 and M5 >= best control + 0.30.

| Held-out part | tokens | M5 | best of 200 controls | margin | result |
|---|---|---|---|---|---|
| H: f14v.21-27 + f15r | 542 | 0.506 | 0.144 | 0.362 | partial |

**The key is partial by our protocol.** The margin is met by far; the absolute threshold is not. M5 has a ceiling: on the
contemporary plaintext D.183 of the Santa Cruz series it is 0.636, so 0.60 asks for about 95% correctness. Nine code tokens of H have no
value in K_OA1 (hol three times, bil, Qar, per, hen, gli, pes), and each cuts a segment. The measured key and transcription were not
changed afterwards.

## Reading

`transcription.txt` (tokens, one manuscript line per line, parts [A] [T] [H]), `decryption.txt` (mechanical, line for line),
`reading.md` (Spanish, marked: {x} probable, [x] restored, ‹?› unresolved, … gutter), `translation.md` (English).
**The reading was made after the measurement.** Counted by script on the marked reading, by your rule (certain + probable; restored
words not counted as read):

| Piece | words | certain | probable | restored | unresolved | read without restorations | state |
|---|---|---|---|---|---|---|---|
| ff. 13r-15r | 1,001 | 906 | 47 | 13 | 35 | 95.2% | read |

Before the reading was counted, Brice Dudout answered a blind proof-reading of 13 sign forms, all outside H. It was pre-registered
and hashed, and the sheet was tested for leaks. It showed forms only, never values, and each answer had a consequence fixed in advance.
It settled hol = Su Majestad (f14r.25, f14v.09, with the reference form f14v.19 in the buffer), gli = buena (twice), pr = for
("premio anticipado"), 209 = "20 9" ("juntas"), a superscript "4" as a null (twice), and the two forms of "t" (p, g). □ was read
"merced" by the sense at f14r.26 (the key says "mi"); it stays probable, and the conflict is left open. **The three "hol" of H
(f14v.21, f15r.02, f15r.07) were then read "Su Majestad" by the value established outside H.** This was Brice Dudout's decision of
5 Nov 2026, and it is a reading decision only: the three words are counted probable, and the key and the measurement are unchanged.
Without them the count is 950/1,001 = 94.9%.

## Remaining gaps

- About 54 line ends lost in the gutter of ff. 13v and 14v (not counted) - blocker: needs-physical-access; an image of the volume opened flat, or the original.
- Codes with no value (22‡, 197, bir, B_, dol, yil, 229, 102, Qar, per, hen, pes; bil, probably "V.E.", only in H) - blocker: open-codes; single occurrences, so a value from the sense would be a guess.
- □ = "mi" in the key, "merced" by the sense (f14r.26 read probable, f14v.21 left unresolved) - blocker: open-codes.
- The two forms of "t" (p, g), not separated at 120 dpi except where the proof-reading settled them - blocker: illegible.

## Prior work

- Your lead 1273 was open on 28 Oct 2026 ("no reading found"). Your vetting of 4 Nov 2026 (`research/leads.json`) closes it as
  "read", because DECODE R1190 is this very letter with status "Decrypted" and an inline-plaintext flag. We found that note only
  after our reading. We then checked R1190 at level 2 (5 Nov 2026): 3 images of BNE MSS/10249 (added 13 Jul 2021), an empty
  documents list, no transcription, no key, no decipherer, and no plaintext written on the pages. Where the "Decrypted" status comes
  from is unknown (perhaps a question for Beáta Megyesi). If an earlier full reading turns up, our credit should be "verification",
  not "solution": your call.
- Edition: Elliott & de la Peña, *Memoriales y cartas del Conde Duque de Olivares* (2013 ed., CEEH/Marcial Pons), from the tables of
  contents: the only piece of 1626 is doc. XI, "Reflexiones políticas y cristianas", to the King; there is no letter to the Duke of Alba
  in 1626. The full text was not seen. The BDH record of MSS/10249 cites no edition. Nothing at Tomokiyo's, nothing found on the web
  (incipit, date, names).

## Method

One agent transcribed the training part, measured the four neighbouring keys once each on it, extended K6A and froze it, then
transcribed the held-out part and measured once. A second agent prepared the blind proof-reading sheet (pre-registered, hashed,
leak-tested with jsdom) and applied Brice Dudout's answers mechanically. A script counted the reading. Images at 120 dpi. Brice
Dudout's check against the images covered the 13 sign forms of the proof-reading only.

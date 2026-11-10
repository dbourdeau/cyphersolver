# rota1624: "Francesco Rota" to "Monsieur Vatron" in London, The Hague, 8 April 1624 (BSB Clm 10398 n. 106)

Status, 9 Nov 2026: **read in part**. Letter key recovered from this leaf alone (key recovered from ciphertext-only);
the code numbers and five single signs are not read. Catalogue item 2176.

## Document

- Munich, Bayerische Staatsbibliothek, Clm 10398 (Collectio Camerariana vol. 48), n. 106, fol. 233r. MDZ bsb00116447
  scan 469 (from microfilm, 1216 x 1849 px, the largest size the IIIF server gives). The verso (scan 470) is blank.
- One page, 20 lines of letter with cipher on lines 4-20, then the close, date, signature and address in clear.
- Italian. Dated "Haia. 8. Aprile. 1624", signed "Franc.o Rota", addressed "A Monsieur Monsieur Vatron. Londre."
- Halm's catalogue (1874, p. 95) says the leaf was written by Ludwig Camerarius, which would make it a copy. The hand
  was not compared here. It is not the hand of n. 107 (scans 471 and 473), which is signed "Francesco Rota".
- The catalogue entry (vetting of 4 Nov 2026) identifies "Francesco Rota" from Goetz and Gardiner as the cover name of
  the Capuchin P. Alexander of Hales, and suggests Rusdorf for "Vatron" (not verified). Neither was checked again here.

## The system (measured on this leaf)

Clear Italian with three kinds of cipher written into it (counts from `decode.py` on `transcription.txt`):

1. **Two-digit groups for single letters**, written together without separators, and mixed with clear letters inside
   one word: "discorre 32 do" = discorrendo, "peti 92 30 40 n" = petition(e), "91 30 gli 40 22 90" = migliore.
   79 groups. One number per letter as far as seen; 20 and 70 may be second values for n and o.
2. **Numbers with a tick above standing alone** (49', 81', 28', 93', 68', 80', 64', 85', 51', 94'; 64 also once without a tick) and **numbers after a
   prefix letter g, c or m** (g 34, g 37, g 24, g 27, g 57', c 94, c 85', c 34, c 84', m 34'), some with a bar above.
   25 in all (20 counted as code numbers and 5 with a bar). They stand where a name or a noun is needed, so they are
   code words. What the tick means is not established: a ticked 81 stands where "la" fits ("et 81' moglie") and 81 is
   the letter l, so a tick may mark a word cut to its first letter; that is a hypothesis, not a reading.
3. **Single signs standing alone**: q, t, p, p', z, x, r, n, pt, &, and a sign like a reversed 2 (written {~}), plus the
   prefix letters of (2). 40 tokens.

## How the key was recovered

No key and no decipherment exist for this leaf (see Prior art). The earlier attack on issue #254 treated the numbers
as a code and did not beat its shuffled control. The break here came from the clear text:

- "discorre 32 do" has clear letters on both sides of one group: 32 = n.
- "peti 92 30 40 n." before "Del resto": petitione, so 92 30 40 = t i o.
- "91 30 gli 40 22 90" after "cosa": migliore, giving 91 = m, 22 = r, 90 = e; "81' 91 40 gli 90" = moglie.
- "può 21 10 22 90" = fare; "ma a 10 81 92 22 40" = altro (twice); "ne è molto 51 90 81 40 94 70" = geloso;
  "che 30 40 71 10 31 30 10 essortato" = io habia; "non venni 41 40 94 92 30" = costì.

Sixteen letter values follow (`key.tsv`), each used in at least one word that the clear text fixes; 70 of the 79
letter groups decode with them (72 with 20 = n and 70 = o, one use each, plausible only) and every run that is complete
forms an Italian word. The signs q = che (4 uses),
t = non (2), p = per (2), p' = però (1), & = et (6) come from their sentences; z = se (3) is plausible only.

Control: none run with a shuffled key. The check is internal: the same sixteen values make far, fare, altro (twice),
geloso, migliore, moglie, petitione, discorrendo, io habia, costì, bene, ho, mi, un, vi è. Not checked by a second
reader or against an independent copy.

## Reading

`reading.txt` (Italian) and `translation.txt` (English); `decode_raw.txt` is the decoder's line-by-line output.
The clear text and the spelled words give the frame: the writer could not leave before today because the Nuncio gave
him business in Amsterdam; he has pressed g34 hard to do something (x 49'), and g34 admitted that for the greatness
of his house there is nothing better, while the wife laughs at it; someone (g37) might say in London that he exhorted
g34, and g24 can say whether that is true, "Non erubesco Evangelium"; g27 writes that once the writer is in Brussels
he will say whether x can do it, and g27 is very jealous of something (51'); the recipient is to maintain that the
writer did not come to London for g57 c34 (in code, not read) but for something else. Greetings to Father Anderson, the Count and "that
gentleman with the Capuchin beard who eats with you".

Who g34 and the others are is **not read**. The frame fits the Capuchin's mission to Frederick V at The Hague as the
catalogue entry describes it (g34 the Palatine, his wife laughing at the proposal), but no code number is confirmed.

Measured (decode.py): 144 cipher tokens = 79 letter groups + 25 code numbers + 40 single signs. Read: 72 letter groups
and 18 signs = 90 of 144 = 62.5%.

## Remaining gaps

- 25 code numbers (ticked numbers standing alone 49', 81', 28', 93', 68', 80', 64', 85', 51', 94', the bare 64, and the numbers after g, c, m: g 34, g 37, g 24, g 27, g 57, c 94, c 85, c 34, c 84, m 34) - blocker: no-key-material; no key or decipherment for this code is known, the neighbouring leaves are in clear, and each code occurs once or twice on a single page (the number 34 four times, after g, c and m)
- 7 unticked numbers inside letter runs (72, 86, 87, 16, 24, 25, 11) - blocker: too-short; each occurs once and no word is fixed around it ("[86][72]ifo", "[16]al[24]", "[25]ara l")
- single signs x (5 uses), r (2), n, m, pt and the reversed-2 sign - blocker: too-short; x is either a person or "si", the page does not decide
- values 20 (n?) and 70 (o?) - blocker: too-short; one use each ("so[20]", "gelos[70]")
- Goetz's "Chiffr. Or./Abschr." reports of Hyacinth and Alexander, Munich St.A. K. schw. 442/19, may be in the same code - blocker: needs-physical-access; not online

## Escalation

- [x] siblings: scans 465-490 opened (n. 105, 107-112), 10 Nov 2026: all in clear, no cipher and no key. n. 107 is Rota to Camerarius, Brussels 29 April (scans 471, 473); n. 108 is Giacinto's letter of 22/23 April (475-479); n. 110 (483) is an extract of a letter of Rota's, written on Hyacinth's order, on German affairs and the Saxon declaration, so later than n. 106 and not a parallel of it; n. 111 (485) is Fra Jacinto's letter in Spanish, Brussels 2 July. Halm's catalogue was searched as text (MDZ search service, bsb11184610): 'Chiffern' marks 13 pages and 'chiffrirt' one, and n. 106 is the only piece of the Rota correspondence marked as cipher; the others are other systems (Anhalt, the Solms letters, Sultan Osman, Ragoczi, Pawel, Fegraeus); 'cifra', 'cifris', 'Zahlen', 'Ziffer' and other spellings gave nothing. So no second leaf in this code is known in the Camerarius volumes, going by Halm's wording only
- [x] clear-pages: the verso (scan 470) is blank; no decipherment on or beside the leaf
- [x] known-keys: camerarius1621 key.tsv does not fit (issue #254: German one-part code with groups to 3200; 3 of 104 groups have a value there)
- [x] print: vetting of 4 Nov 2026 searched Rusdorf's Mémoires (1789), Goetz, Briefe und Akten N.F. II/1, Khevenhüller, Söltl, Gardiner, Krüner: the mission is described, this letter and Vatron are not; Schubert (1955) not online, not seen
- [x] key-rebuild: letter key rebuilt here from the clear context, 16 values; the code numbers have no alphabetical order to bracket (too few, 1-3 uses)
- [x] retry: every group decoded again with the 16 values (decode.py); 7 letter-run numbers and all code numbers stay open

## Context from the clear siblings (10 Nov 2026): proposals, not readings

The clear letters give the persons and the business, but no parallel text for n. 106. These are proposals for the code numbers, each from the context only and not counted in the 62.5%:

- g 27 and g 27' = Father Hyacinth (grade M). The sentence before names him by his motto 'Non erubesco Evangelium', which Halm says Camerarius added to the signature of n. 108, and he is the one who writes from Brussels (n. 108 is dated Brussels).
- g 34 = the Elector Palatine or his house (grade M). n. 107 and n. 108 are about the Palatine, 'la sua Ser.ma moglie' and 'la casa Palatina'; the sentence 'per grandezza della sua casa non vi è cosa migliore ... et la moglie ne ride' fits them. The number 34 also stands after m and c (m 34', c 34), so the prefix letter is not a class mark that fixes the meaning.
- The Nuncio (Monsignor Nuncio, Bagni) and 'Mons. di Tillier' are written in clear in n. 106; n. 107 names a 'sig. Plessen' in clear. None of them is among the code numbers.
- g 24, g 37, g 57, the ticked numbers and all the signs: no proposal; n. 107 and n. 108 name no one who fits.

Nothing here was tested against a second passage, so none of it moves a token to 'read'.

## Prior art (contamination)

No reading existed when the work was done (9 Nov 2026). Catalogue 2176 vetting, 4 Nov 2026: no DECODE record, nothing
in Tomokiyo or Lasry, not printed in Rusdorf, Goetz or the other editions searched. Issue #254 (Brice Dudout): not the
camerarius1621 system; a fresh attack did not beat its shuffled-key control. Lead found by WAINUT (PR #242).

## Files

- `transcription.txt`: line-by-line, one AI transcription from the scan and 4x crops; digits 4 and 7 told apart by
  form (the 4 is crossed, the 7 is an open angle). No second pass by another reader.
- `key.tsv`, `decode.py`, `decode_raw.txt`, `reading.txt`, `translation.txt`.
- `img/`: scans and crops (git-ignored).

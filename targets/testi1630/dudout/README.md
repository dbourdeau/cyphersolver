Prior-art check: the readings of the 1630 letters exist at edition level (all seven are printed in clear, Parenti 1843 and Doglio 1967; checked by Brice Dudout's agents, 17 Nov 2026). The 1636 letter and the Forni and Ottonelli letters are not printed there and stay as in NOTES.md.

# testi1630: the 1630 letters are printed (prior art check, 17 Nov 2026)

Work by Brice Dudout (Europe chiffrée), done with Claude Opus 5.5 agents. Nothing in WAINUT's reading is changed here. This
folder adds the prior-art check that NOTES.md left open ("Doglio ... not opened").

## Finding

Maria Luisa Doglio's edition is online at the Internet Archive, OCR included:
Fulvio Testi, *Lettere*, ed. M. L. Doglio, 3 vols, Bari, Laterza 1967 (Scrittori d'Italia 236-238),
https://archive.org/details/236TestiLettere1Si254 (vol. 1, 1609-1633), `237TestiLettere2Si255`, `238TestiLettere3Si256`.

Vol. 1 prints, among the letters "in nome del Principe" to Ottavio Bolognesi at Vienna, nos. 205-216 (Feb-Mar 1630), in full
and in clear, with no sign that parts were in cipher. Its index gives the source of each as **L 14**, which the Nota filologica
(vol. 3) resolves as: *Lettere inedite di Fulvio Testi*, ed. M. Parenti, in *Memorie di religione, di morale e di letteratura*,
ser. II, XV (Modena 1843), pp. 49-85 (nos. 205-210, 213, 214, 216, 217, 219, 220). So these texts have been in print since 1843.

| Leaf (WAINUT doc) | Date | Doglio vol. 1 | Parenti 1843 | Cipher letters (decryption file) | Found in order in the printed letter | Best other printed letter (control) |
|---|---|---|---|---|---|---|
| c. 7r (c7r) | 7 Feb 1630 | no. 205, p. 216 | L 14, p. 55 | 517 | 513 (99.2%) | 60.7% (no. 209) |
| cc. 9r-9v (c9) | 15 Feb 1630 | no. 206, pp. 216-217 | L 14, p. 56 | 1356 | 1320 (97.3%) | 26.0% (no. 210) |
| c. 11r (c11) | 15 Feb 1630 | no. 207, p. 217 | L 14, p. 58 | 301 | 296 (98.3%) | 58.1% (no. 209) |
| c. 13r, 8 lines (c13) | 22 Feb 1630 | no. 210, pp. 222-223 | L 14, p. 75 | 267 | 266 (99.6%) | 53.2% (no. 209) |
| cc. 16r-16v (c16) | 22 Feb 1630 | no. 211, pp. 223-224 | L 13, p. 156 | 1168 | 1129 (96.7%) | 23.1% (no. 213) |
| cc. 20r-20v (c20) | 1 Mar 1630 | no. 213, pp. 225-226 | L 14, p. 78 | 338 | 315 (93.2%) | 59.5% (no. 210) |
| c. 23r (c23) | 14 Mar 1630 | no. 216, pp. 227-228 | L 14, p. 81 | 382 | 381 (99.7%) | 42.9% (no. 213) |

No. 211 is from L 13 (*Memorie* ser. II, XIII, 1842, pp. 152-193), not L 14. The page numbers after "L 14"/"L 13" are those
of Doglio's index, read from the OCR.

The count is a longest-common-subsequence share after normalising spelling on both sides (the edition modernises:
retentione/retenzione, Sabioneta/Sabbioneta); `compare_doglio.py` makes it and `doglio_comparison.tsv` is its output
(OCR file SHA-256 157a93f4e6a649351d737057fc71b35d394c14bb9930f23b918a855184d72f56). It is a check of identity, not a new
measure of the key: the key was already tested by WAINUT. The decryptions agree with the printed texts to 93-99.7%, against
23-61% for the best wrong letter. c. 20 is lowest; its cipher carries the most writer's slips listed by WAINUT (quclificati, circontanze, qrincipe,
crepcnti dc nostri cicscuno), and the content is the same as no. 213 (courier robbed near Gradisca, duplicates sent, the
agent cannot serve Mirandola and Correggio as well).

**The rest of c. 13r, c. 13v and the cipher of c. 14r**, listed as a remaining gap, are printed too: no. 210 is the whole letter
(Villafranca's offer of "quindicimila fanti e quattrocento cavalli", the minister and Dottor Genuino), the same text as the later
clear copy c. 15.

## Doubtful words settled by the print

| Place | WAINUT | Doglio | Note |
|---|---|---|---|
| c. 7r l. 14 | [?compiamo] | compiangiamo | the signs are certain; the cipher clerk dropped "ng" |
| c. 9v l. 8 | [?roliet] | "Non vi scordate di Roli et invigilate" | a person, Roli; not identified here |
| c. 16v l. 2 | [?coni] | così vuoti et esausti | the cipher has a slip for così |
| c. 16v, clear | [?Inviato predetto] | all'Interprete | "Interprete" is a cover name used in clear in no. 208 ("il principe Interprete ha somma autorità col Ferro"); so the son is the Interprete's son |
| c. 9r, clear | [?Feudo] | "del fune" in the OCR | not checked on the printed page; left open |
| c. 9r, clear | "viene registrata publicamente" | "se ne ragiona publicamente" | clear text, for WAINUT to recheck on the image |

## What is not in Doglio

- cc. 73-74, 2 Feb 1636, to Bolognesi: Testi was at Genoa then; vol. 2 has no letter of that date to Bolognesi (his
  letters of 1-2 Feb 1636 are from Genoa to the duke). Doglio also says in her Nota (vol. 3, section III) that she
  omitted letters in cipher "di cui per giunta non ci è pervenuta la chiave". WAINUT's 1636 reading is not found in print.
- c. 53, c. 54, c. 72 (Forni, 1634-1636) and c. 4, cc. 5-6 (Ottonelli, 1642, 1647): ducal letters not countersigned by Testi,
  none in Doglio. Not attempted here.

## Small catalogue points seen on the images (not changed in catalogue.json)

- cc. 5-6 (Lettera F): the letter is dated on the page "Di Mod.a li 25. Mag.o 1647", 25 May 1647, not 25 Oct 1647 as in the
  record. Countersigned Girolamo Graziani. The cipher is in digits (about three lines). The two small canvases 0005-02 and
  0005-03 are pieces of the address (one ends "Resid.", the other reads "Napoli"), not a decipherment.
- c. 54: headed by Forni "Risposta data alla cifra ad. 22 lug.o 1634" and dated at Florence 25 Jul 1634; about 13 lines of the
  c. 53 signs with clear words between them, which give context for a later attack on the Forni table.

## Not done

No new transcription, key or reading. Parenti 1843 was not opened (the Google Books copy cited in NOTES.md), so how he got the
clear text (minutes, the Reggio Bolognesi papers or a deciphered copy) is not known. No images are included.

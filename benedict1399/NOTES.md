# Benedict XIII's cipher letters to Francesc Climent, 1399–1416 (Arxiu Capitular de Barcelona) — catalogue 334

Status: found already read (Puig y Puig 1920). Written up as `docs/benedict1399.html`.

**Result, 23 Sept 2026:** the "best shot" at an unread cipher from c. 1400 was read a century ago. Meister (1906,
pp. 22–23, second-hand from Ehrle) reported in the Barcelona cathedral archive a letter of Benedict XIII with some
cipher lines and an instruction of about three folio pages, much of it in cipher, and printed nothing. Sebastián Puig
y Puig, canon of Barcelona, found the same material among the papers Francesc Climent (Çapera) left to the chapter,
**broke the cipher himself** and printed the letters in the appendix of *Pedro de Luna, último papa de Aviñón
(1387–1430)* (Barcelona: Editorial Políglota, 1920), with the deciphered passages set in italics. The check the
archive scan left open ("Puig y Puig 1920 may print a transcription; HathiTrust blocked") is closed: it does, and it
is a decipherment, not a transcription.

## 1. How it was found

- HathiTrust (record 100676638) is behind a Cloudflare challenge in curl and in the built-in browser; not solved.
- archive.org has no copy. Google Books has the Wisconsin copy in full view: **id `CuOlkxWnk-EC`**.
  `books.google.com/books?id=…&q=…` and the PDF download were CAPTCHA-walled from this IP, but the in-volume search
  endpoint `books.google.com/books?id=CuOlkxWnk-EC&jscmd=SearchWithinVolume2&q=<term>` answered with JSON, and
  `…&pg=PA466&jscmd=click3` returns signed page-image URLs (fetched at `&w=1600`). Hits for 22 terms are saved in
  `src/puig1920_search_hits.json`. The page images were kept in the session scratchpad, not committed.
- The hit that settled it, p. 466 note 2 (crop on the site page):
  > (2) Las letras cursivas en los apéndices significarán las frases descifradas. La clave o claves que me han
  > servido para soltar la cifra ha sido obtenida a fuerza de paciencia, tomando por base unas líneas dejadas por
  > el ilustre Çapera en este documento 1063 y en los de número 461, 463. En el documento n.º 595 existen dos
  > claves de Climent que no he podido aplicar a ningún otro de los inéditos.
- Preface, p. 2: of the "Documentos inéditos del obispo Çapera" he printed the most important, "especialmente los
  diez u once escritos con desconocida clave, que tras laboriosos tanteos hemos tenido la fortuna de descifrar".

So Puig rebuilt the key(s) from a few lines Climent had deciphered on docs. 1063, 461 and 463 (partial contemporary
decipherments: a crib attack, in effect), and read the rest.

## 2. The archive

- Puig's working label "Documentos inéditos del obispo Çapera" (paper) and "cub. IV, armar. 202, capsa …" (parchment)
  is the fonds Meister called "Documentos referentes a la familia Luna I" (the Ehrle-era capsa). Today it is the ACB
  series **Cisma d'Occident**, split into parchment and paper (1,532 paper pieces). Baucells i Reig, *El fons Cisma
  d'Occident de l'Arxiu Capitular de la Catedral de Barcelona* (IEC 1978; PDF on arxiu.catedralbcn.org) catalogues
  the codices and parchments only; the paper part, where these letters are, had no summaries in 1978.
- Baucells, p. 12, quotes the archivist Josep Mas: "Entre 1920 y 1930 lo M.V. Sr. Dr. D. Sebastià Puig, canonge de
  Barcelona, estudià a sa casa nombrosa documentació, y en part molt important del Cisma de Occident … però molts no
  foren tornats." Some of the cipher originals may therefore be lost; Puig's print may be the only witness.
- Not digitised; the archive has no online images of this series.
- **One page of cipher is in print as an image.** Puig p. 475 carries an uncaptioned photogravure, printed
  sideways, of the last page of letter XXXV (Benedict XIII to Climent, Avignon 22 June 1400, doc. 1068): 26
  manuscript lines, clear Latin alternating with long cipher runs, down to "Dat. Avinion xxii die Junii sub nostro
  signeto". Puig's printed text of the same passage runs beside it (p. 475 right column, p. 476 top), so every
  cipher run on the plate has its plaintext. Site figures `docs/benedict1399_facsimile.jpg` (whole plate, deskewed
  0.7°) and `benedict1399_lead.jpg` (lines 1–5).
- Puig's other photogravure (announced p. 231) is Benedict XIII's autograph minute of April 1410 to Climent
  (text p. 530), a clear letter; that plate is not in the Google scan (the last scanned leaf, PT8, is the back
  cover). Searches for "lámina", "facsímil", "grabado" find no other plate.

## 3. The cipher items in Puig's appendix

Checked page by page (subagent, notes kept in the session scratchpad `puig/items.md`). Italics = deciphered
(Puig p. 466 n. 2). Word counts are estimates from printed lines.

| Puig app. | date | sender → recipient | doc. (Çapera) | pages | italic words | note |
|---|---|---|---|---|---|---|
| XXVI | 22 Sep 1399, Avignon | Benedict XIII → Climent | 1063 | 466–467 | ~195 | one of the three docs with Climent's decipherment lines; Fillet bp of Apt, embassy of Aragon, Castile, Navarre |
| XXVII | Oct 1399 | Benedict XIII → Climent | 409 | 467–469 | ~490 | the "submission" refused for three reasons; much Aragonese/Castilian inside the cipher; mentions a cedula "et chifris et secreta" |
| XXIX | 22 Oct 1399, Avignon | Fr. P. de Santa Cruz → Climent | 922 | 469–470 | ~100 | French ambassadors leave, the besieged household "in periculo mortis" |
| XXXV | 22 Jun 1400, Avignon | Benedict XIII → Climent | 1068 | 473–476 | ~260 | **facsimile of the last page, p. 475** |
| XXXVI | 2 Jul 1400, Avignon (palace) | Benedict XIII → Climent | 921 | 476–477 | ~325 | mostly cipher, Romance-heavy; Cervelló, the see of Lérida, two Carthusians |
| XXXVII | 24 Sep 1400, Avignon | Benedict XIII → Climent | 447 | 477 | ~19 | one ciphered sentence: send 3,000 francs |
| (note) | 15 Sep 1400 | P. Jafet → Climent | 1043 | 477 n. 2 | ~14 | only one deciphered sentence printed: some of Climent's letters "sunt intercepte hodie et recuperate" |
| XXXIX | 6 Oct 1400, Avignon | Benedict XIII → Climent | 1061 | 478 | ~33 | the 3,000 francs again |
| XLI | 18 Dec 1400 | Benedict XIII → Climent | 452 | 478 | ~100 | almost all cipher, date and address included |
| XLII | 29 Dec 1400, Avignon | Benedict XIII → Climent | 50 | 478 | ~255 | nearly all cipher; "absque signeto Pape" |
| XLIII | 11 Jan 1401, Avignon | Benedict XIII → Climent | 463 | 478–479 | ~420 | effectively all cipher; one of the three docs with Climent's lines; one gapped word "mi. i ur" |
| LII | 8 Feb 1403, Avignon | Benedict XIII → bp of Ávila and Climent | 461 | 490–491 | ~85 | bulls for Castile's restitution of obedience; one of the three docs with Climent's lines |
| LXIV | 23 Aug 1408, Perpignan | Alfonso de Exea, abp of Seville → Climent | 133 | 500–503 | ~2,090 | entirely cipher; the defection of Pedro de Frías, "Cardinal of Spain"; the longest text |
| CXVI (printed CXVII) | 21 Dec 1415 | Pedro Comuel → Climent | — | 562–563 | ~300 | a secret mission to the Queen of Castile |
| CXXXV | 27 Jun 1416 | Pedro Comuel → Climent | — | 578–579 | ~85 | his coming to Aragon; note 2 cites another Comuel letter, doc. 661, not printed |

About 4,750 deciphered words in all, Benedict's own letters about 2,200 of them. Eleven items are from 1399–1401
and 1403 (Puig's "diez u once escritos"); Exea 1408 and Comuel 1415–16 may use other keys (Puig says "la clave o
claves"). Puig marks nothing as unread. The doubtful forms inside italics ("n s possumus", "ot.o", "mi. i ur",
"Cardinalis ispanie e l.", "v. stm perfui", "cer ificari") look like decipherment slips or misprints, one letter or
word each.

## 3a. The facsimile: what the cipher looks like, and a first check of Puig

- The cipher runs are strings of small invented signs (δ-, T-, o-, ‡-, Ƭ-, b-, c-shaped strokes, many joined by
  hair-lines), mixed into clear Latin. A dotted **V̇** stands for the King of Aragon (Puig prints "Regis Arag." /
  "Regi Aragon." in roman, i.e. he expanded the sign).
- Known-plaintext check on two runs, read from the plate at 3× (lines 1–2 and the start of line 8):
  - line 1 end + line 2 start, V̇ o cb t ‡ cb o d | Z i b ı cb n ‡ o d = [Regis Arag.] *cum duce Burgundie*:
    c = o (2×), u = cb (3×), m = t, d = ‡ (2×), e = d/δ (2×), b = Z/Ƭ, n = n; one clash (u read as "i").
  - line 8 start, δ ᵭ ı ı δ T δ c δ o t T o ı o Ƭ δ ‡ cb … = *et presertim scribe qu…*: e = δ (4×), s = T (2×),
    m = t, i = o (2×), c = o, b = Ƭ, u = cb, q = ‡(?).
  So it is a letter substitution with invented signs (homophones and a merged o-sign likely) and at least one
  name sign, and Puig's italics fit the plate where tested.
- **Why the key was not rebuilt here:** Google serves the page at 1826 × 2500 px at most, about 40 px per
  manuscript line of a reduced 1920 halftone. δ/ᵭ/o/a and the joined strokes cannot be told apart consistently;
  a first pass at "quo modo se habet" did not align. A trustworthy sign-level transcription (about 700 signs on
  the plate, all with known plaintext) needs a better image: the printed book scanned at 600 dpi, or a
  photograph of ACB doc. 1068.

## 4. What this means for the oldest-cipher hunt

- Catalogue 334 was the project's top pre-1425 lead for a ciphertext-only record. It is not open: the letters of
  1399–1403 were deciphered by Puig in 1920, with the key rebuilt from Climent's partial glosses. They remain,
  as far as found, the oldest *papal* cipher correspondence read from the ciphertext (Meister's Avignon material,
  Lavinde 1379 and Ameilh 1363–64, is keys and a 1363 read text), but the reading is Puig's, not ours.
- What can be added without the ACB is limited to the p. 475 facsimile: it shows the system and confirms
  Puig's reading where tested, but a full key needs a sharper image.

## Remaining gaps

- Fr. Pedro de Vico to Guillem Carbonell, 4 Dec 1398 (Puig app. XIX, p. 461): "Sigue una línea cifrada, de clave
  desconocida" - blocker: needs-physical-access; Puig did not print the line, no image exists.
- Doc. 595 of the Çapera papers: "dos claves de Climent" that Puig could not apply to any document - blocker:
  needs-physical-access; he did not print them.
- P. Jafet to Climent, 15 Sep 1400 (doc. 1043) and Comuel to Climent (doc. 661): cited by Puig, not printed -
  blocker: needs-physical-access.
- Any further cipher pieces among the ~1,532 paper documents that Puig did not print, and those not returned after
  1920–30 - blocker: needs-physical-access.
- The key itself (never printed): rebuildable from the p. 475 facsimile against Puig's text, but not at the
  resolution of the only scan reachable - blocker: illegible; needs a 600-dpi scan of the book or an ACB photograph.

## Escalation

- [x] siblings: Puig's appendix index (pp. 623–627) and a full-text search for "cifra/cifrada/cifrado/clave" read; every cipher item listed above.
- [x] clear-pages: Climent's own decipherment lines on docs. 1063, 461, 463 are what Puig used; not printed separately.
- [x] known-keys: Meister's Avignon keys (Lavinde 1379, Schlüsselsammlung I) could only be tested on ciphertext; none is printed.
- [x] print: Puig 1920 (this reading); Meister 1906; Ehrle ALKG 5–7 (nothing); Baucells 1978 (parchments only);
  IFC 2024 *Benedicto XIII, el Papa Luna* and Cuella's Bulario (nothing on the cipher).
- [x] key-rebuild: the p. 475 facsimile (last page of XXXV) aligned with Puig's text on two runs; a dozen values
  recur consistently, but the halftone at 40 px a line is too coarse for a full sign-level transcription.
- [n/a] retry: the reading is Puig's and he marks nothing unread; nothing of ours to retry until a better image exists.

## Sources

- Puig y Puig, S., *Pedro de Luna, último papa de Aviñón (1387–1430)*, Barcelona 1920 (Google Books CuOlkxWnk-EC,
  Wisconsin copy, full view). Appendix (Apéndices I–CCVII); index from p. 621, cipher items listed pp. 623–627.
- Meister, A., *Die Geheimschrift im Dienste der päpstlichen Kurie*, Paderborn 1906, pp. 22–23 and n. 1 (archive.org
  diegeheimschrift00meis).
- Baucells i Reig, J., *El fons Cisma d'Occident de l'Arxiu Capitular de la Catedral de Barcelona: catàlegs, còdexs i
  pergamins*, Barcelona: IEC 1978 (PDF at arxiu.catedralbcn.org/wp-content/uploads/2026/05/…Mn.-Baucells.pdf).
- Archive-scan notes: `oldest/scan_2026-09-23/iberia.md` (Candidate 1).

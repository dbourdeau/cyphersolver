# Lope de Soria (Genoa) to Charles de Lannoy, viceroy of Naples, 7 March 1527 — Estense, Autografoteca Campori (catalogue 1562)

**Outcome (6 Nov 2026): key recovered from ciphertext-only; read, 95.5% of cipher tokens measured.** Letter key recovered by
joint annealing with no crib; code groups valued by context; 14 single code groups (names, rare words) open.

Catalogue entry 1562. Worked from 6 Nov 2026 (Claude Opus 5.5, in Daniel Bourdeau's session).

## The document

Biblioteca Estense Universitaria, Modena, Autografoteca Campori, Lettera L, "Lope de Soria", cc. 9-12. Record:
https://lodovico.medialibrary.it/media/schedadl.aspx?id=3409a92a-8c78-44bc-a7c4-920fbacb3126 ("Lettera parzialmente
cifrata"). IIIF manifest https://edl-jarvis.cultura.gov.it/meta/iiif/3409a92a-8c78-44bc-a7c4-920fbacb3126/manifest,
licence CC BY-NC-SA. The image server refuses regions over about 1600 px ("Request exceeds server image size limit"):
the full-size leaves (about 3170 x 4480) were stitched from 1500-px tiles (`img/`, git-ignored).

Addressed "Ill.mo y Ex.mo Señor" (Lannoy, prince of Sulmona); signed at Genoa, "De Genoua a vij de março M.D.xxvij".

| side | content |
|---|---|
| 9r | clear: Soria's last letter was of the 23rd of last month "por via de" + a short cipher run; Captain Bracamonte bears this letter; the viceroy's letter of 3 December received; saltpetre (salitre) sent for the galleys, seven mule-loads of gunpowder sent to the Duke of Bourbon near Piacenza, the saltpetre convoy taken by the enemy at the mouth of the [Tesino?]; "Aca se han sentido estos dias diversas nuevas"; "Aqui estamos agora libre de trigo porque es entrada una carraca cargada dello" |
| 9v | "de manera que de la hambre pasamos fuera por agora, pero" + about 28 lines of cipher; then clear "Segun aca hacemos entendido" + about 12 lines of cipher |
| 10r | clear: the Duke [of Genoa] and the Comunidad have spoken to Soria about the remedy for this land, the French fleet at Savona doing harm; the remedy is to have many galleys, to be strong at sea so their ships and merchandise may come safely; "la determinacion es que" + cipher; the prince [Doria?] will arm three galleys, "hasta XX cuerpos de galeras"; + about 18 lines of cipher; "y han me dicho el dicho duque y los de la Comunidad que es menester para que se haga breve que" + 3 lines of cipher |
| 10v | about 22 lines of cipher; clear "el señor duque de Borbon con el exercito arribo junto a Rezo a los xxvij del passado ..., el duque de Ferrara ..., caminar hazia Florencia y si fuere necessario hazia Roma"; cipher; "el s. Antonio de Leyva queda a la guarda y govierno de Milan"; Count Lodron's campaign ... |
| 11r | clear "de Lodron anda con su campillo por el Monferrat haziendo algunos daños; en Ast hay obra de dos mil hombres y cien lanzas francesas ... el Rey es ydo en Picardia para tractar la conclusion de casarse con la hija del Rey de Inglaterra" + 7 lines of cipher; clear "porque el dicho Bracamonte esta cada hora para partir en una carraca que va para Sicilia ... por letras de Francia de los [?] del ponte se entiende que" + 4 lines of cipher; closing, date and signature "A. V. Ill.ma y Ex.ma S.a" |
| 11v, 12r, 12v | bleed-through only; the address leaf |

The catalogue vetting (3 Nov 2026) saw cipher on 10r and 11r only; 9v and 10v are also nearly all cipher.

## Prior work and key search (6 Nov 2026)

- No decipherment on the leaves (no interlinear or marginal plaintext) and no clear copy filed with them.
- DECODE: no record of this letter, of the Autografoteca Campori, or of any Lannoy-Soria letter (list dump and view
  dumps searched for Soria, Lannoy, Sulmona and RAH 9/29-9/41).
- **Soria's keys in the repo do not fit.** Key B (`targets/soria1523/keyB.md`, Soria-Charles V 1523-27; code initials
  z, y, x, t, s, p: zog = de, sub = que) and key A (cap = que, lod = de) have different code groups. This letter's
  groups are lab, leb, den, dan, dri, pre, ral, gis, ges, mor, mur, com, cem, fip, sim, ... (initials b c d f g l m p r s t z).
- **Lannoy's own cipher with Charles V** (Kolosova's Ko.5; O. Kolosova, *El lenguaje secreto de la diplomacia de
  Carlos V (1521-1527)*, thesis, Valencia 2017, http://hdl.handle.net/10550/66216, pp. 63-89): its letter table
  (p. 65) shares several signs with this letter (11 and oo = a, 4 = c, 3 = d, 7 = l, ∠ = g, ff / g# / # = u-v,
  + = n), but its code groups (initials 3/z n m g f p t s: mnr = con, mop = en, nn = de, poo = para, pio = por,
  te = sobre) are not this letter's. The thesis's chapter on Soria's own cipher is Ko.6 = key B (de = zog, p. 98).
  The thesis PDF is in `prior/` (git-ignored).
- **BRAH 9/15 key book** (DECODE R9815-R9832, images in `targets/soria1523/keys/`): looked through again for these
  groups; its tables are Ferdinand-era keys (Cabrero, Castile, Naples c. 1500-1516); none has them.
- Tomokiyo, cryptiana `spanish2.htm` (fetched 6 Nov 2026) and Galende Diaz 1992 (as summarised there): Soria's keys
  with Charles V (Ciphers 1, 2), with King Ferdinand, with the viceroy of Sicily (two-letter codes) and with Leyva
  (syllabic); no Soria-Lannoy key is described. Galende Diaz 1992 itself not seen (no open copy found).
- CSP Spain III.2 (Feb-Apr 1527) calendars Lannoy to Soria, Florence 13 Apr 1527 ("your worship's two letters of the
  5th inst; one of them in cipher") and Siena 25 Apr 1527, both from Soria's archive copies (RAH Salazar A-40), clear.
  It does not calendar this letter. Villa's *Memorias* (1875) prints Soria to the Emperor of 15 March 1527 (p. 71);
  the OCR copy in `lang/corpora` does not carry its text legibly; not used.

## How the key was recovered (6 Nov 2026)

Ciphertext-only: no crib, no key, no clear copy. Claude Opus 5.5.

1. **Transcription.** Sign legend (`transcription/LEGEND.md`); two sub-agents transcribed 9r/9v/11r and 10r/10v from
   full-resolution line crops, one token per sign or code group (`transcription/00*.txt`; 2494 tokens with 53 frame
   marks, `ciphertext.txt`). No human has checked it.
2. **Control.** The joint sign/code-group annealer of cardona1517 (`solve/wsa5.c`, compiled under WSL; driver
   `solve/ann.py`) scored on a 5-gram model of 1520s chancery Spanish (`solve/build_lm.py`: Villa's *Memorias* letters
   of 1526-27, Danvila MHE 37, Soria's own 1523/1527 readings). Matched control, Danvila MHE 38 enciphered with 40
   signs and 70 groups (1408 tokens): 100% of sign tokens; noisy control (43 signs, 110 groups, 5% misread signs,
   1001 tokens): 93-95% of sign tokens in every top run (`solve/control_noisy.log`).
3. **Letters.** On the first 687 tokens the top 3 of 16 runs agreed on 96-99% of sign tokens and the output read as
   Spanish. On the full transcription (22 runs x 6M) the top 4 runs agree on 100% of sign tokens. Two transcription
   splits came out of the decode and were checked in the images: a closed 4 (= o) and an open 4 (`4s`, = s), from
   c-o-s-a / o-d-i-o-s-a; agent A's footed z (= u, n-u-estras) against agent B's crossed z (= d, meata-d).
4. **Code groups.** Valued from the decoded context (`solve/kwic.py`), whole words and syllables as in Soria's key B:
   dri que, leb de (se de-clare), den no (Ge-no-ua), lue es (nu-es-tras, es men-es-ter), ral con (con-tribuyan,
   con-tra), lab las, fip galeras, muc/mur la, moc/mor los, mic/mir lo, lie esto, loe esta/este, gis haze, ges ha,
   cem para, zer muy, sem todo, sim toda, fib porque, dan si (si-n duda, si-endo), pre Su Magestad, lae el, nat
   papa, pof como, goq Francia, cam por, tin aqui, bil fab hasta aqui, dun aunque, zir mas, fob orden, zar mucho,
   pif assi, lee ello. Key: `key.tsv`.
5. **Polyvalent signs and frame marks.** `to` = g (gasto, governarse) and a (armada, buena), checked in the images of
   10r L07, L25, L29; `#` = e (tienen) and q (q-u-itar, q-u-ien, q-u-al); `ff` = i/e; `V` = rr (Fe-rr-ara, Nava-rr-o);
   `o^` = ie (qualquiera). Soria's key A of 1523 has the same kind of variant (P = a/g, targets/soria1523).
   `11`, `g#`, `-o-` open and close each cipher run (9r: "por via de | Ferrara |"); g# is also ha in the text
   (a ha-zia = hazia). Lannoy's cipher has such markers (Kolosova 2017 p. 64).
6. **Reading and measure.** `reading_aligned.txt` (run by run), aligned to the decode token by token by
   `solve/measure.py`: **2332 of 2441 counted cipher tokens read = 95.5%** (frame marks not counted; doubtful
   words [?], unvalued groups and signs unread). Running text with the clear passages `reading.md`, translation
   `reading_en.md`, raw decode `reading_raw.txt`.
7. **Validation** (`docs/_validate.py`, `validation.tsv`, 2325 read tokens): reading -1.917 per letter, random keys
   -4.566 (z 7.0), keys fitted to shuffled text -2.785 (z 79.4): pass.

## What the letter says

Soria reports, in cipher, that some citizens are talking with the Pope of a union of the city's factions, of
governing as a republic and of neutrality, which he has opposed; that the draft agreement negotiated with the Pope
leaves each side what it holds in Italy, so Savona and the riviera would stay French, and Genoa asks that any
settlement restore them; that the Duke [the doge Antoniotto Adorno] and the Commune will arm galleys (three of the
prince's, three more, His Majesty's three = nine) if Charles V pays half, and want the six imperial galleys at Naples
to join them: fifteen together would break the French galleys anywhere; that the commune is poor and tired and its
bad elements talk of changing sides; that the King of France has sent money to fortify Savona, which has invited
him, and orders Pedro Navarro with the galleys towards Naples; and that the King and the Venetians offered someone
([riz]) the kingdom of Naples, who wants Milan too. Bourbon's army, near Reggio, has "muy poco dinero".

## Remaining gaps
- code groups lax pax, zaz, giq, xup, fub, gas, lex, tri, tmi, lir, rez, riz, bel, ten (14 types, 17 tokens; each once or twice: places, owners of galleys, rare words) - blocker: open-codes; each occurs once or twice, no repeat or sibling narrows them
- 9v L25 blotted sign under a superscript 3, and 9v L34 the water-washed last line - blocker: illegible; one image, the ink is gone
- doubtful words 9v L02 (algun go), L08 (ca lo cosa), L12-13 ([mur]s, algd es), L15 (`/` and `.4s.`), 10r L12 (sunydas), L15 (por es), 10v L02 (a [?] y al s. [?] de Borbon), 11r L07-08 (con [?] ... debaxo de l [?] dauana) - blocker: open-codes; the signs are read, the sense needs a code value or a sign not attested elsewhere

## Escalation
- [x] siblings: no other Soria-Lannoy letter in the Estense record or on DECODE; Lannoy's replies of 13 and 25 Apr 1527 (CSP Spain III.2 nos. 49, 54) survive only as clear copies in RAH Salazar A-40
- [x] clear-pages: the clear passages of the letter itself used as context (Bracamonte, galleys, Savona); no decipherment on the leaves
- [x] known-keys: Soria's keys A and B (targets/soria1523), Lannoy's Ko.5 (Kolosova 2017), the BRAH 9/15 key book (R9815-R9832): none fits
- [x] print: CSP Spain III.2 Feb-Apr 1527, Villa's Memorias (1875) index, Tomokiyo spanish2.htm (Galende Diaz 1992): no copy or key
- [x] key-rebuild: letter key recovered ciphertext-only by joint annealing; code groups valued by context
- [x] retry: every unread group run again through solve/kwic.py with the full key; images checked for 10r L07, L17-18, L25, L29 and 9v L08, L11

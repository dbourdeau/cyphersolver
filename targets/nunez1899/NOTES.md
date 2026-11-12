# Roberto Núñez to José Y. Limantour, Mexico 26 Aug 1899: word-code telegram (catalogue 1461, part)

Read in part by the strict count (111 of 119 words = 93.3%, 12 Nov 2026), through a contemporary translation filed under
other numbers; the contributor's own figure was 97% of the 114 telegram units, class read. Written up on the site
(nunez1899.html) at the integration of PR #464.

## Document

- CEHM-Carso, Fondo CDLIV (Colección José Y. Limantour), **CDLIV.1a.1883.38.9926**, 5 images: address leaf
  ("ministro Limantour, 16 avenue Friedland, Paris") and four sheets of a French telegram form No 701, from Mexico,
  No 78, "Mots 98", Via Anglo, Paris stamp 26 Aout 99. Signed Núñez (under-secretary of Finance).
- The CEHM record (FichaBasica 148376) says "Texto codificado. Sin traducción". That is true of the record itself,
  but **the translation exists**: it is filed as the next two numbers, **CDLIV.1a.1883.38.9927** (pencil draft on
  Elysée-Palace-Hotel telegram paper, 2 images) and **CDLIV.1a.1883.38.9928** (fair copy headed "Traducción", signed
  Núñez, 1 image). Their text follows the code telegram word for word (see the alignment in `key.tsv`), so they are
  the translation of 9926 and not of another telegram.

## System

A word code (a "clave") in Spanish dictionary words. Only some words are coded; the rest of the text is clear
Spanish (*cuando*, *conforme en que*, *pero en todo caso usted indicará la manera más conveniente* ...). Code words
keep Spanish endings: *jirpeo* = indicó, *jirpee* = indique; *impulsarlo* = hacerlo, *impulsese* = hágase,
*impulsa* = hacer; *intitular* = imprimir, *intitularse* = se impriman; *besarsele* = abonársele, *besara* = abonará.
One value takes two code words (*garlopas abocados* = E.U.). Numbers are mostly sent clear (23 13/16, 24), but
"4 millones" and "2 y 1/4" are coded. The same code is used by Núñez and Limantour in August 1899 (9922, 9926,
9929, 9930); it is not the Speyer & Co. code of 1905.

## Key source and held-out test

1. `key_frozen.tsv` (90 entries) was built first from three **other** telegrams of the same code, each with its
   plain text on the same sheet (`key_sources.md`): 9922 (Núñez, 10 Aug, code + translation), 9929 (Limantour's
   draft of 28 Aug with plain and code words line by line, his answer to 9926) and 9930 (Núñez, 31 Aug, code +
   "Traducción").
2. Held-out test (`scripts/heldout.py`, `heldout_9926.tsv`): of the 65 code-word tokens of 9926, the frozen key
   covers **28** (23 by the same code word, 5 by the same code root with another ending). All **28/28** give the
   value that the contemporary translation 9927/9928 gives at the same place. The other 37 tokens are code words
   that do not occur in 9922, 9929 or 9930.
3. `key.tsv` then sets those 37 values by aligning 9926 with 9928, token by token (basis `9928`). One code word,
   *ampida*, was left blank by the translator too ("fondos sobrantes se ___ en oro"); it stays a hole.

So the reading rests on the contemporary translation for 36 code words and one hole; the frozen key confirms the
translation wherever it reaches.

## Decryption and reading

- `scripts/decrypt.py`: transcription + `key.tsv` -> `decryption_9926.txt`.
- `reading_9926.md`: marked reading and running Spanish text; `scripts/check_marks.py` rebuilds the decryption
  from the marks and passes (22 lines, 0 mismatches). Marks: `{+de}` x2, `{+aquí}`, `{+empréstito}`, `{+en}`
  (all words the contemporary translator supplied), `{-te se}` (two telegraphed words the translator did not
  render), `{23 13 16/23 13/16}`, `[?depositen]` for *ampida*.
- `translation_9926.md`: English.

Contemporary translation (9928, as written): Presidente acordó préstamo Banco de Londres 4 millones. Pasado año
cuando Gobierno disponga libremente depósitos, Banco abonará 2 y 1/4. Presidente conforme en que cantidad que Ud.
indique de fondos sobrantes se ______ en oro Banco Inglaterra tipo cambio hoy 23 13/16. Creemos que á 24 ó más
podría aquí irse convirtiendo efectivo en oro y remitirlo Camacho para su guarda Banco Inglés, pero en todo caso
Ud. indicará la manera que crea más conveniente hacer esa situación. Camacho pide autorización bonos nuevos
empréstito se impriman en E.U. Presidente llama atención de Ud. si no obstante que Bonos no serían acabados
careciendo de firmas E.U., pudiera ejercitarse proceso semejante á providencia precautoria contra Morgan
ocasionándonos algún estorbo. Sírvase resolver. Núñez

Content: the President (Díaz) has agreed a loan of 4 millions from the Banco de Londres [y México]; surplus funds
are to go in gold to the Bank of England, exchange 23 13/16; Camacho (the financial agent) asks that the bonds of
the new [1899 conversion] loan be printed in the United States; the President fears that unfinished, unsigned bonds
in the U.S. could be the object of an injunction-like proceeding against Morgan. Limantour's answer (9929, 28 Aug)
takes up exactly these points: the Bank of England deposit is not urgent, and he thinks printing the titles in the
U.S. will not cause the difficulties the President fears.

## Word counts (`scripts/count_words.py`)

Telegram text, 114 units (the two-word code *garlopas abocados* counted as one unit each time) plus the signature:

| kind | units |
|---|---|
| clear words, read verbatim from the form | 43 |
| numbers, clear | 4 |
| code words, value from the frozen key (independent) | 28 |
| code words, value from the contemporary translation only | 36 |
| hole (*ampida*, blank in the translation too; guess `[?depositen]`) | 1 |
| telegraphed but not rendered (*te se*) | 2 |

Marked repairs: none to code values; five words added and one number written as a fraction, as listed above.
Sense: 111 of 114 units (97%). Reading checker (`docs/_check_reading.py --file`, run 12 Nov 2026): running Spanish
text 5/10 sentences clean (0.50), whole `reading_9926.md` 0.355, `translation_9926.md` 0.60 (0.571 before "pasado año" was rendered literally). The Spanish is
telegraphic (no articles), and the checker counts bare numbers (4, 2, 1/4, 23 13/16, 24) and abbreviations (Ud.,
E.U.) as holes; the only unread word is *ampida*.

## Independent review (12 Nov 2026)

An AI language-model agent that did not take part in the work read 17 of the 22 lines (L01-L07, L14-L22) from the
scans before opening the transcription, and found no disagreement that affects the reading. It re-ran
`decrypt.py` and `check_marks.py`, and reproduced the held-out result (28/28) with its own decryption from
`key_frozen.tsv` alone. It compared 9928 with the reading word for word. Agreed state: read, grade A
(`reading_review` in `profile.json`). Its two sign doubts and its remark on "pasado año" are listed below.

## Integration check (12 Nov 2026)

Done by the integrating session. Reproduced: check_marks.py (22 lines, 0 mismatches); heldout.py: 28 of 65 code tokens
covered (19 distinct code words), 28/28 agree with 9927/9928. The frozen key was built from 9922, 9929 and 9930, each
with its own plain text on the same sheet, so the test does not use the translation of 9926 itself; that it was frozen
before 9926 was compared with the translation rests on the contributor's record (the file header, one commit). Five of
the 28 matches are by code root with another ending. Image CDLIV.1a.1883.38.9926.0002 was fetched from the CEHM viewer
(no host refused): lines L01-L03 agree with the transcription.
**Class changed from read to read in part.** The README read bar counts supplied words and guesses as not read. Counted
over the 114 telegram units plus the 5 words the translator supplied ({+de} twice, {+aquí}, {+empréstito}, {+en}), the
holes are the guess for ampida, the 2 words not rendered (te se) and the 5 supplied words: 111 of 119 = 93.3%, under 95%.
The contributor's 97% (111 of 114 units) leaves the supplied words out. 36 of the 65 code values rest only on the
contemporary translation of this very telegram, which is why the method is "read from existing decipherment".

## Remaining gaps

- ampida (L06) - blocker: no-key-material; the contemporary translator left it blank; context and Limantour's answer
  ("asunto Depósito Banco Inglaterra") suggest "depositen" or "inviertan", marked as a guess.
- te se (L16) - blocker: too-short; two telegraphed words with no counterpart in the translation, possibly a
  transmission error; one occurrence, nothing to test them against.
- curadela, pareciendo.., torrejones - blocker: illegible; last letters hidden under the pencil docket (L04), the
  watermark (L20) or at the edge (L05); their values are still those of 9928.
- serian (L17), rolliza (L19) - blocker: illegible; the blind review (12 Nov 2026) saw serian possibly beginning with
  v and rolliza possibly ending in o; left as transcribed, neither changes the reading.
- pasado año (L02) rendered literally, "after a year"; "next year" is also possible - blocker: too-short; two words
  with no other occurrence.
- 36 code values rest on the one contemporary translation, with no second source - blocker: no-key-material; no
  codebook of this clave was found in the file.

Not reading gaps: other telegrams of 1899 in file 38 may share the code (9906-9908 Núñez with translations, 9923
Limantour from Karlsbad with a coded second part); images were fetched for 9906-9908 and not used, because they could
only add values to words the translation already values. The five words the translator supplied are counted as not
read in the strict share (above).

## Escalation

- [x] siblings: the other telegrams of the code opened: 9922, 9929 and 9930 (the frozen key), and the translation
  9927/9928; 9906-9908 fetched and not used, 9923 not opened.
- [x] clear-pages: the translation filed as 9927 (pencil draft) and 9928 (fair copy) is the decipherment; it was found
  here although the record says "sin traducción".
- [x] known-keys: the code of this series, frozen from 9922, 9929 and 9930, tested on 9926 (28 of 28); the Speyer code
  of 1905 is a different one (not this key).
- [x] print: one web search (12 Nov 2026) found work on the 1899 conversion loan (Weller, EHS working paper 13023; a
  UNAM thesis on Limantour's Hacienda) and no edition of this telegram or its translation.
- [n/a] key-rebuild: the 36 values not in the frozen key are set from the translation, which is the reading source
  itself; no other text of the code is read here to extend it.
- [x] retry: every code word decrypted again with key.tsv; check_marks.py passes (22 lines, 0 mismatches).

## Prior art (checked 12 Nov 2026)

- Catalogue entry 1461 (prior_art: "open as far as checked", 28 Oct 2026; vetting 2 Nov 2026) and the CEHM record
  say "sin traducción"; neither names 9927/9928.
- Web search (12 Nov 2026: Limantour 1899 Núñez telegrama Banco de Londres préstamo Morgan bonos impresión) found
  general work on the 1899 conversion loan (Weller, "Stretching the financial boundaries", EHS working paper 13023;
  a UNAM thesis on Limantour's Hacienda 1893-1899) but no edition of this telegram or its translation.
- The translation 9927/9928 is a contemporary decipherment: it is a crib, and the reading here is built on it.

## Images (CEHM viewer files, no login; not copied into git)

- 9926: http://visor.cehm.org.mx/assets/docx/fondos/jzd/CDLIV/1a/1883/38/9926/CDLIV.1a.1883.38.9926.0001.jpg ... .0005.jpg
- 9927: .../38/9927/CDLIV.1a.1883.38.9927.0001.jpg, .0002.jpg; 9928: .../38/9928/CDLIV.1a.1883.38.9928.0001.jpg
- 9922: .../38/9922/CDLIV.1a.1883.38.9922.0001.jpg; 9929: .../38/9929/CDLIV.1a.1883.38.9929.0001.jpg;
  9930: .../38/9930/CDLIV.1a.1883.38.9930.0001.jpg ... .0003.jpg
- Catalogue records: https://www.cehm.org.mx/Buscador/FichaBasica/148376?Tipo=A (9926),
  .../148392?Tipo=A (9929), .../148416?Tipo=A (9930), .../148360?Tipo=A (9922)

Work by WAINUT with AI language-model agents; transcriptions from the CEHM images.

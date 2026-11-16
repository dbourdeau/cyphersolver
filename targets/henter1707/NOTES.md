# Mihály Hentér → Ferenc Rákóczi II, Constantinople, 8 July 1707

Status: read in part (16 Nov 2026, recounted over cipher words: paragraphs 1-2 50 of 53, paragraphs 3-4 62 of 66; paragraphs 3-4 re-read 23 Oct 2026, batch b28)

**Result, 20 September 2026:** DECODE R496 is not an undeciphered letter. A
contemporary or near-contemporary plaintext has been written between the cipher
lines on the target folio itself. DECODE records `inline_plaintext = False`, so
the catalogue has overlooked the interlinear decipherment. The manuscript date
is **8 July 1707**, not 1 January: DECODE's 1 January--31 December dates are only
an artificial year range.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **paragraphs 1-2** of the
normalized interlinear **read** (the Belgrade pasha's offer; the audience sought for the deputation). **Paragraphs 3-4
are not read**: words between [...] holes where the interlinear hand overlaps the cipher (split into a second
`outcome.texts` entry, "decoded, not read"). fraction_read 0.8 -> about 0.5 (estimated).

**23 Oct 2026, re-read (REREAD_BRIEF, batch b28)**: paragraphs 3-4 **read** (grade A). The interlinear is legible at
2-3x on the DECODE image, and the cipher under it was decoded sign by sign with the alphabet fixed by paragraphs 1-2
(`texts/mnl-g15-d80-f38_p3-4_reading.md`, `_en.md`, `_cipher.tsv`, `_reread_log.md`). The figures correct the
interlinear (and the normalized text above) at four places: "de a magyar" is **de a jancsarsag közöt turbatio eset**
(a disturbance among the Janissaries), "naltatnak" is **componalodnak**, "zenenkedem" is **remenkedem**; the
audience was solicited twice more and the answer was "habeant patientiam, vocabuntur ad praesentandas literas".
Score 0.000 on the modern Hungarian list (unaccented 1700s spelling), 0.833 explicit holes; 6 letters on look-alike
signs. fraction_read 1.0. No DOC_ attachment or comment on R496/R533/R534. The normalized text above modernises the
spelling; the b28 reading keeps the figures' spelling.

## Identification

- Author: Mihály Hentér
- Addressee: Ferenc Rákóczi II
- Place and date: Constantinople, 8 July 1707
- Shelfmark: MNL OL, G 15, Caps. D, Fasc. 80, fol. 38
- DECODE: [R496](https://de-crypt.org/decrypt-web/RecordsView/496)
- Physical item: one folio, recto (letter) and verso (address)
- Rights: the archive/DECODE notice says that the scan is not in the public
  domain and may be published only with the archive's permission. The scans are
  therefore kept locally under the ignored `img/` directory and are not
  reproduced here.

## What the cipher says

The following is a normalized reading of the interlinear Hungarian. Square
brackets mark words that remain uncertain because the decipherer's cursive
overlaps the cipher characters. Spelling and punctuation have otherwise been
lightly normalized.

> Az nándorfejérvári pasa Felséged ajándékát kedvesen vevé, és
> dicsértette; kiben mondá: ha Felséged hat vagy hét ezer hadat a rácok
> ellen küldene, assecurálja Felségedet, hogy Felséged hadait haddal,
> porral, gabonával is segítené.
>
> [A kuruc követekre vonatkozó rövid, nehezen olvasható mondat.] Ide
> érkezvén Felséged, Uram, levelét vettem. Elmentem és kértem, hogy a
> fővezér előtt a deputát [kihallgatást nyerjen / bővebben
> meghallgattassék], melyre ígérte magát. [Közvetítője] azt izené, hogy
> lett volna audientiája, de a magyar […].
>
> […] Ezen leginkább [a] városban még a dolgok confusióban [vannak]. Idő
> folytában ismét sollicitáltuk az audientiát. […] izené, hogy ha bément
> […], *voce* […], bátor *ad praesentandas literas* […].
>
> Felségednek a szegény rab uram felszabadulása iránt […]. Kérem
> Istent, Felségednek minden áldását […]. Felséged alázatos hű szolgája,
> Hentér Mihály.

This is enough to recover the message's historical substance. The pasha of
Belgrade received Rákóczi's gift favourably and said that, if Rákóczi sent six
or seven thousand troops against the Serbs, he would support those forces with
troops, gunpowder, and grain. Hentér then reports his Constantinople diplomacy:
after receiving Rákóczi's letter he pressed for the deputation to be heard by
the grand vizier. The audience was delayed amid confused conditions in the
capital, so the request and letters were presented again. The letter closes
with a request concerning the liberation of an unnamed captive, called
"szegény rab uram."

The bracketed middle clauses need a Hungarian palaeographer for a publication-
quality diplomatic edition. They do not affect the main intelligence reported
in the letter.

## Verification

Two letters by Hentér in the same fascicle use the same system and carry dense
interlinear plaintext:

- DECODE [R533](https://de-crypt.org/decrypt-web/RecordsView/533), fol. 40
- DECODE [R534](https://de-crypt.org/decrypt-web/RecordsView/534), fol. 46

R533 gives an especially clean control at the closing formula. Cipher
`wi6xi2i4` reads *Felséged*, securely fixing `w=f`, `i=e`, `6=l`, `x=s`,
`2=g`, and `4=d`. Other repeated formulae support `n=a`, `0=o`, `c=h`,
`9=m`, and `5=k` (the remaining handwritten graphic signs are awkward to
represent in plain text). Those mappings agree with the interlinear reading on
R496.

Benedek Láng independently identifies fols. 38, 40, and 46 as Hentér's three
1707 letters (`C.Hen.01–03`) and describes their cipher as monoalphabetic. See
his [doctoral dissertation, pp. 84 and 109](https://real-d.mtak.hu/922/7/dc_758_13_doktori_mu.pdf)
and the related [Aetas article](https://acta.bibl.u-szeged.hu/38710/1/aetas_2014_001.pdf).

## Catalogue corrections

1. Date: replace "1 Jan 1707" with **8 July 1707**.
2. Status: replace "non-decrypted / what the cipher hides is not known" with
   **contemporary interlinear decipherment present; substantive content read**.
3. Inline plaintext: change **False** to **True**.
4. Page description: one folio, with the letter on the recto and address on the
   verso; DECODE exposes two image files despite listing one page.

## Read share over cipher words only (16 Nov 2026)

README Conventions now count the read share over the words written in cipher, holes by words, sure words only. The
letter is wholly in cipher, so every word of both readings counts; nothing had to be separated.

- Paragraphs 1-2 (`texts/mnl-g15-d80-f38_decryption.md`, the normalized interlinear, up to "melyre ígérte magát";
  the next sentence, "[Közvetítője] azt izené ... de a magyar […]", is where the paragraphs 3-4 reading starts, and
  that reading re-reads it from the figures): 0.98 -> **0.943** (50 of 53 words). Holes: the sentence on the kuruc
  envoys, which the file gives only as a bracketed description (counted as one word, extent unknown), and
  "[kihallgatást nyerjen / bővebben meghallgattassék]" (two words, the least the alternatives show). **Read -> read
  in part.** Counted with the overlapping sentence in its old form it would be 0.922 (59 of 64).
- Paragraphs 3-4: unchanged, 0.939 (62 of 66), read in part.
- Both parts are under the bar, so the class goes **already solved -> read in part** (extent partial); fraction_read
  1.0 -> 0.941 (112 of 119 words). The method stays "read from existing decipherment".
- Measure declaration: `cipher_markup: >` on paragraphs 1-2. The tool measures the whole blockquote of the file,
  paragraphs 3-4 in their old normalized form included, and gives 0.912; it has no way to take paragraphs 1-2 alone
  without a heading in the file. The hand count is the figure of record.

## Remaining gaps

- paragraph 2: the short sentence on the kuruc envoys and the phrase [kihallgatást nyerjen / bővebben meghallgattassék] (3 words counted unread) - blocker: illegible; the interlinear hand overlaps the cipher there (a Hungarian palaeographer is needed); paragraphs 1-2 were not decoded sign by sign under the interlinear
- paragraphs 3-4: closed 23 Oct 2026 (read, b28); four words stay [?] on look-alike signs (tiszteket, valtoztatni, uram, pedig) - blocker: illegible

## Escalation

- [x] siblings: R533 and R534 (Hentér's other 1707 letters, same system) used for the alphabet
- [x] clear-pages: the interlinear decipherment is on the leaf itself
- [x] known-keys: not needed; the alphabet is fixed by the interlinear
- [x] print: Láng (dissertation, Aetas 2014) identifies the letter, prints no text
- [x] key-rebuild: alphabet rebuilt from the interlinear of paragraphs 1-2 (b28 cipher tsv)
- [x] retry: paragraphs 3-4 re-read on the image, interlinear and figures, 23 Oct 2026

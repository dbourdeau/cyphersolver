# Mihály Hentér → Ferenc Rákóczi II, Constantinople, 8 July 1707

**Result, 20 September 2026:** DECODE R496 is not an undeciphered letter. A
contemporary or near-contemporary plaintext has been written between the cipher
lines on the target folio itself. DECODE records `inline_plaintext = False`, so
the catalogue has overlooked the interlinear decipherment. The manuscript date
is **8 July 1707**, not 1 January: DECODE's 1 January--31 December dates are only
an artificial year range.

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

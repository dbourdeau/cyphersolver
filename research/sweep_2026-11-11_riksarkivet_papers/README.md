# Riksarkivet private papers and chancery series, volume pass (11 Nov 2026, cloud session)

Source key `riksarkivet_papers`. Goal: sheet the digitised volumes that the earlier Riksarkivet sweeps left out (Reuterholm
E 5135-5141, Stedingk E 6616/6617, De la Gardie, Tessin, Oxenstierna, Kanslikollegium and related fonds) and find cipher
with no decipherment. **Result: 1 row in `candidates.json`, none open** (a fully glossed Oxenstierna despatch of 1634,
class A, no vetting block). No bare cipher was found. Nothing padded.

## Routes (all worked from this network, no bot check)

- NAD API `data.riksarkivet.se/api/records?text=*&only_digitised_materials=true&facet=PartOfArchive:<fonds>`
  (`User-Agent: curl/8.0`): `nad_enum.py` -> `enum.json`, 1,763 digitised units in 25 fonds.
- Image-series id from `data.riksarkivet.se/archive/<id>.jsonld`, else the APE EAD `<dao>`; image count by `info.json`
  bisection (the manifests are slow): `rik.py resolve` -> `units.json` (183 volumes, 63,745 images).
- Images `lbiiif.riksarkivet.se/arkis!<series>_<nnnnn>/full/900,/0/default.jpg` with `Referer: https://sok.riksarkivet.se/`.
  About 1 s an image here for the R and A series, 3 s for the 4000xxxx series. A request wider than the stored image
  returns **400** (no upscaling): `rik.py` then falls back to `full/max`.
- `rik.py sheet` crops the grey copy-stand border (the paper is yellower than the stand, not lighter) before tiling, so a
  520 px tile shows the leaf at roughly the scale of an 800-900 px uncropped image. 12 tiles a sheet, 3 columns.
- Eight `1133.07` units (R0001313-R0001322: Johan Casimir 1622-32, Radziwil-Rosladin, Spens, T, varia) resolved to a
  series id but `info.json` returned nothing: not sheeted.
- The container restarted once; `sheets.log` was cleaned of entries without a sheet and the batch restarted (`run2.sh`).

## What was covered

Sample = k images spaced evenly over the volume from image 2. "Viewed" = the contact sheet was looked at; sheets were
made for 62 volumes (`sheets.log`) but only the ones below were viewed. A sample this thin catches only volumes where
cipher is common: "no cipher seen" is not "no cipher".

| Fonds / volume | Series, images | Sample viewed | Seen |
|---|---|---|---|
| Reuterholm E 5135 (F. Piranesi, Rome 1793) | R0003397, 499 | 12 of 24 (images 2-230) + 100, 120, 140 | clear Italian |
| Reuterholm E 5136 (Piranesi, Jan-Jun 1794) | R0003398, 390 | 12 | clear Italian |
| Stedingk E 6616 (Gustaf III to Stedingk 1778-92) | 90003462, 259 | 12 (images 2-120) | clear French autographs |
| Stedingk E 6617 (royal letters 1788-1828) | 90003463, 216 | 12 (images 2-100) | clear French |
| De la Gardie E 1329 (Adolf Johan 1647-58) | R7000017, 313 | 12 (2-145); image 93 at 1300 px | German/French, clear (93 is Kurrent, not cipher) |
| De la Gardie E 1387 (Moirous de Verrière 1662-68) | R7000022, 488 | 12 (2-225) | clear French newsletters |
| Azzolino K 394 (Christina to Azzolino 1666-68) | R0003359, 301 | 12 (2-139) | French autographs; cipher not visible at this size; the series is edited (Bildt 1899), not pursued |
| Azzolino K 400 (abdication papers 1655-57) | R0003661, 408 | 12 (2-188) | accounts, clear |
| Azzolino K 419 (Texeira letters 1657-80) | R0003795, 495 | 12 (2-228) | clear |
| Scheffer, Ulrik: 002/2, 002/4, 002/14 | 40008914 (272), 40008916 (402), 40008923 (512) | 12 each | receipts 1777, Gustaf III's notes, Swedish drafts; clear |
| Karl XIV Johan K 1032 (C. and G. Löwenhielm 1812-32) | A0076345, 550 | 12 (2-253) | clear French apostilles (microfilm) |
| Karl XIV Johan K 1034 (Tawast, Copenhagen 1811-14) | A0076347, 318 | 12 (2-147) | clear French |
| UD, Berlin despatches 1820-21 (E 2 D/b/29) | R0002561, 307 | 12 (2-142) | clear French |
| UD, Copenhagen despatches Jan-Jun 1849 (E 2 D/j/317) | 40001943, 782 | 12 (2-360) | clear French, enclosures, print |
| Lovisa Ulrika K 260 (to her mother 1750-51) | A0073298, 366 | 12 (2-169) | clear French |
| Lovisa Ulrika K 264 (incoming, princes) | A0073302, 194 | 12 (2-90) | clear |
| Skrivelser till konungen 1133.08/10 (Oxenstierna 1633-34) | R0001375, 295 | 12 + images 243-254 | **cipher, glossed**: images 246-247 |
| Skrivelser till konungen 1133.08/13 (Oxenstierna 1634-35) | R0001378, 402 | 12; image 102 at 2400 px | clear (102 is dense German, not cipher) |
| Skrivelser till konungen 1133.07/18 (Kniphausen 1624-32) | R0000808, 190 | 12 | clear German |

Sheets made but **not viewed** (in scratch only, lost with the session): Reuterholm E 5134, E 5137-5139, E 5141; De la
Gardie E 1330; C. F. Scheffer 001/I-VI; Ulrik Scheffer 002/5, 002/9, 002/16; Azzolino K 413, K 420; Karl XIV Johan
K 1020, K 1033, K 1058 ("Papiers secrets" 1812-13), K 1041-1043; UD Berlin 1821-22, Copenhagen 1836-37 and 1848;
Lovisa Ulrika K 261, K 263; 1133.07/6, /14, /25; 1133.08/2, /7, /16; Christina K 93. The second sheet (images 13-24
of the sample) of most viewed volumes was not viewed either.

## The one find

SE/RA/1133/1133.08/10, images 246-247 (fol. 230-231): Axel Oxenstierna to the regency, March 1634, Swedish, numeric
nomenclator (1-4 digit numbers and doubled letters), every line struck through and deciphered above. Class A pair,
not an open text. AOSB (part I) and DECODE were not opened for it, so the row has no vetting block.
`known.py "1133.08" "Skrivelser till konungen"`: no hits.

## Excluded

- Christina's letters to Azzolino (K 394): cipher passages are known and printed deciphered in Bildt, *Christine de
  Suède et le cardinal Azzolino* (1899); not re-examined (edition named from memory, not opened).
- Oxenstiernska samlingen has only two digitised volumes (E 1039, E 1040, family letters); Kanslikollegium only the
  Antikvitetsarkiv letters and one register; S:t Barthélemysamlingen is the colony's archive; Tessinska samlingen is
  Cronström's art correspondence. None sheeted.

## What remains

- Full paging of 1133.08/7-16 (Oxenstierna to the regency 1632-36, about 3,300 images) for further cipher letters and
  any unglossed one; this is the only place cipher turned up.
- The unviewed volumes listed above, first K 1058 and the Karl XIV Johan incoming letters (K 1020-1036).
- The eight `1133.07` units without images through `info.json` (try the viewer).
- Not resolved at all: Ericsberg autograph volumes (319 units), Hedvig Eleonora's and Ulrika Eleonora's incoming
  letters (about 70), the other Stedingk family volumes, Skokloster manuscripts.

Scripts: `nad_enum.py`, `rik.py` (resolve / sheet / range / pick), `batch.py`, `run1.sh`, `run2.sh`.

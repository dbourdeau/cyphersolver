# sweep_2026-11_pares_diversos_19c (9 Nov 2026)

Result: **3 rows** in candidates.json (all class A, scans seen).

## Routes
PARES answered by curl, no 429 (about 200 requests, 4 s spacing). `series.py`/`crawl.py` list `catalogo/contiene/<id>` children;
`descs.py` reads unit descriptions; `sheet.py` makes contact sheets of images (zoom 10); `run.py` = pares_ags session search
with facet `idFI=19` (start-century facet; the 19th century).
Listed series: Guerras Carlistas tree (3116479, 3534395 with 40 sub-series, 3734617, 4211700), Guerra de la Independencia (2950609, 11 sub-series;
Ejercito de Francia 2983101 27 sub-series, Confidencias, Correspondencia, Operaciones, Asuntos generales: 82 units, all descriptions read),
Sexenio, Trienio, Decada absolutista, Depósito de la Guerra parents (172354, 2964491, 2955471). Units read by description: 82 + 7 + 12 (about 100);
units opened (images): BAENA,C.38,D.267-268; ESTADO,3010,Exp.10; DC 110,N.35; DC 193,N.99; AGI ESTADO,32,N.10; AHN ESTADO,5920; 12 descriptions of the old hit list.
Finding: the French-army units' descriptions flag cipher where present (only 133,N.29, 151,N.8 say anything), so listing children adds little; full text with
`idFI=19` is the better route (cifra 104, cifrada 27, cifrado 93, cifras 15, cifrar 4, descifrado 7, descifrada 61, cifrados 18; 37 not in earlier hit files).

## Excluded
- DC 110,N.35 (Wellington's translations, June 1812; French copies of Jourdan to Soult 28 May, Joseph 26 May, Great Paris Chiffre numbers): same traffic as
  `targets/marmont1812` (134,N.34 is Jourdan 28 May); 26 May letters are Scovell/Oman nos. 26-27. Extra copy for marmont1812, not a row. DC 151,N.8: key and decipherment filed.
- AGI ESTADO,32,N.10 (Apodaca, Mexico 30 Apr 1818): 4-digit cipher with contemporary interlinear letters (image 7). Exclude.
- AHN ESTADO,5920 (Paez de la Cadena, St Petersburg no. 243, 22 Jul 1826, 4-digit cipher, Decembrist executions, images 3-6): partial contemporary interlinear decipherment
  above the groups. Exclude; crib material.
- ESTADO,88-104 (embassies 1816-20) already removed 2 Nov (decipherment filed). CONSEJOS,12204 Exp.1/Exp.18 (Carnerero 1828-30, San Carlos 1827-28, "Acompana cifras"):
  no images online, not a row (description-only; worth an archive scan request). ESTADO,3099 Exp.20, 3004 Exp.47 (Joseph's government, no cipher claim), MENDIGORRIA C.38 1865, FERNAN NUNEZ 1882 telegrams, ULTRAMAR telegram-administration items, AGA/University surname "Cifra"/"Xifra": not leads.
- Not run: AGI Indiferente/Estado 1808-25 beyond the old hit list (hits seen: ESTADO 12,19,32,35,64 all already screened); Archivo de la Casa de Alba/Osuna 19th c; Inquisicion; AGP and AMAE are not on PARES.

## Remaining
Neighbours of ESTADO,3010,Exp.10 (Joseph Bonaparte government papers, ESTADO 3004-3130); further AHN Estado 1810-14 descriptions with "cifra" in other terms
(clave, criptograma, jeroglifico: not searched); Carlist units in DC 168/190 unflagged; CONSEJOS,12204 scans.

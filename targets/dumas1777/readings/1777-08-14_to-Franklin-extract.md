# Extract of Dumas's letter to Franklin, 14 August 1777 (two copies)

Group G1. Reconciled, decoded and print-checked 14 Nov 2026 from R2_A / R2_B (image 90), R5_A / R5_B (M332 image 3) and the images. Nothing posted.

## Source

- PCC item 93 vol. 1 (naId 502964761), image 90 (folio 100): "Copie de l'Extrait de ma Lettre à Mr. le Dr. B. Franklin à Paris du 14e Aout 1777". Glossed (a letter over nearly every number). https://catalog.archives.gov/id/502964761?objectPage=90
- M332 (naId 464815090), image 3: "Extrait de ma Lettre à Mr. le Dr. B. Franklin, à Paris, du 14e Août 1777". No glosses. https://catalog.archives.gov/id/464815090?objectPage=3
- Both read at 2600 px.

## Reconciliation decisions

Image 90:
- L16: A=379 B=179. 379 gives s ("conseiller"), 179 v; the M332 copy has 379. Read 379.
- L04: 485 first figure overwritten; both passes 485 (e); M332 has 485. Kept.

M332 image 3:
- L04: A=B=834 as written. Image (crop at 2x): the first figure is a heavily looped 3 or an 8. 834 is out of range; image 90 has 334 (u, "ambassadeur"). See Emendations.
- L16: A=468 B=408. Image: 408. 408 gives p ("pensionaire"); image 90 has 408. Read 408.

Copies compared number by number: the two runs are identical (100 numbers each) except M332's 834 for 334.

## Numbers

Image 90:

```
# img0090 run 1 before: "J'avois écrit à"  after: "le 2e Aout, une Lettre assez intéressante"
L03: 619 280 74 660 580 500 678 357 366 19
L04: 635 454 334 364 659 457 485 382 69 582 255 461 75 291
L05: 85 613 120 384 465 584
# img0090 run 2 before: "Je lui avois appris, que j'avois si bien profité d'un"  after: "J'étois sûr d'être bien reçu du mari"
L13: 195 236 40 147
L14: 104 467 155 208 480 264 301 183 470 348 253 337 375 482
L15: 20 486 76 393 83 212 158 599 518 489 396 423 424 494 333
L16: 597 439 276 602 379 497 431 361 390 502 398 408 511 627 380
L17: 474 297 661 169 507 411 519 71 281 178 202 385 389 533 412
L18: 84 234 235 207 80 350 535
```

M332 image 3:

```
# m332_0003 run 1 before: "J'avois ecrit a"  after: "le 2e Aout, une Lettre assez interes-"
L03: 619 280 74 660 580 500 678 357 366 19 635
L04: 454 834 364 659 457 485 382 69 582 255 461 75 291 85
L05: 613 120 384 465 584
# m332_0003 run 2 before: "Je lui avois appris, que j'avois si bien profite d'un"  after: "J'etois bien sur d'etre bien recu du mari"
L13: 195 236 40
L14: 147 104 467 155 208 480 264 301 183 470 348 253 337 375 482 20
L15: 486 76 393 83 212 158 599 518 489 396 423 424 494 333 597
L16: 439 276 602 379 497 431 361 390 502 398 408 511 627 380
L17: 474 297 661 169 507 411 519 71 281 178 202 385 389 533
L18: 412 84 234 235 207 80 350 535
```

## Raw decode

Image 90:

```
# img0090 run 1
al'ambassadeurdefrancealahaie,
# img0090 run 2
voyageavecl'spousedemr.vanberchel,conseillerpensionaired'amsterdam,que
```

M332 image 3:

```
# m332_0003 run 1
al'ambassade[834]rdefrancealahaie,
# m332_0003 run 2
voyageavecl'spousedemr.vanberchel,conseillerpensionaired'amsterdam,que
```

## Normalized text

"J'avois écrit à [l'ambassadeur de France à la Haie,] le 2e Aout, une Lettre assez intéressante ..." — "Je lui avois appris, que j'avois si bien profité d'un [voyage avec l'(é)spouse de Mr. Van Berchel, conseiller pensionaire d'Amsterdam, que] J'étois sûr d'être bien reçu du mari ..."

## Translation

"I had written to the ambassador of France at The Hague, on 2 August, a rather interesting letter ..." — "I had told him that I had made such good use of a journey with the wife of Mr. Van Berckel, Pensionary of Amsterdam, that I was sure of being well received by the husband ..."

## Share read

Image 90: 100 numbers, 100 / 100 = 100 % without emendation (one letter, the é/e of "épouse", is not written).
M332 image 3: 100 numbers, 99 / 100 = 99 % without emendation; 100 / 100 after emendation.

## Emendations

- M332 L04 `{emended: 834 [out of range] -> 334 u, from the other copy (image 90 L04)}`; 834/334 is a 3/8 confusion of the looped figure.
- Both copies "l'spouse" (183 470 348 ...): no number for e/é; supplied in the normalized text ("l'espouse" = "l'épouse").

## Print check

Classification: **printed with the cipher read** — the Franklin Papers vol. 24 pp. 428-434 print the clear-text original (APS) of which these are cipher extracts (`print/franklin24_14aug1777_excerpt.txt`). Not in Sparks or Wharton (Wharton's note omits Dumas's letter of 14 Aug 1777).

- Ours: "J'avois écrit à [l'ambassadeur de France à la Haie,] le 2e Aout" — Franklin Papers (original): "J'avois écrit au Facteur le 2e. Août une Lettre assez intéressante"; the editors identify "Facteur" as Dumas's alias for the duc de La Vauguyon.
- Ours: "[voyage avec l'(é)spouse de Mr. Van Berchel, conseiller pensionaire d'Amsterdam, que] j'étois sûr d'être bien reçu du mari" — original: "du voyage que j'ai fait avec l'Epouse de Mr. Van Berkel, Premier Conseiller Pensionnaire de la ville d'Amsterdam, que j'étois sûr d'être bien reçu de son mari".

Differences:
1. The extract names "l'ambassadeur de France à la Haie" where the original has the cover name "le Facteur": the cipher gives the identity the editors had to supply. Agreement with the editors' identification (La Vauguyon was French ambassador at The Hague).
2. "Van Berchel" in cipher vs "Van Berkel" in the original: the key has no k; Dumas writes ch.
3. The extract shortens: "d'un voyage avec" for "du voyage que j'ai fait avec"; "conseiller pensionaire d'Amsterdam" for "Premier Conseiller Pensionnaire de la ville d'Amsterdam"; "du mari" for "de son mari".

Decipherer: image 90 glossed throughout; M332 copy bare. Hand not identified.

## Remarks

Checked on the image: M332 L04 (834/334). Image 90 L16 settled by the M332 copy. No sign of a different system.

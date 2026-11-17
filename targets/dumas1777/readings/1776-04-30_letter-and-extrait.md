# Dumas to the Committee of Secret Correspondence, Utrecht, 30 April 1776 (continued 9 May 1776)

Group G1. Reconciled, decoded and print-checked 14 Nov 2026 from the two independent transcriptions (R1_A forward, R1_B backward) and the page images. Nothing posted.

## Source

PCC item 93 vol. 1 (naId 502964761).

- Signed letter (the "letter"): images 16-19 (folios 20-23; cipher begins on 16 after the key table on 15), 23-24 (folios 27-28: the 9 May addition, cipher inside the copied unsigned letter Dumas received).
  https://catalog.archives.gov/id/502964761?objectPage=16 , ?objectPage=17 , ?objectPage=18 , ?objectPage=19 , ?objectPage=23 , ?objectPage=24
- "Extrait de ma lettre du 30 Avril 1776" (the "copy"): images 27-30 (folios 31-34). Image 30 also holds a second copy of the unsigned letter of 6 May (received 9 May), preceded by a cipher phrase that is not in the letter ("notre homme de la Haie").
  https://catalog.archives.gov/id/502964761?objectPage=27 , ?objectPage=28 , ?objectPage=29 , ?objectPage=30
- Images used: 16-17 at 2290 px (`_max`), the others at 2600 px. Image 29 is cut at the right edge: about 15 line-final numbers of the copy are partly or wholly lost.

## Reconciliation decisions

The automatic merge in `readings/auto/` reported 69, 46 and 76 disagreements on images 16, 17 and 27. Nearly all of them are alignment artefacts: pass B lists the runs of a line in a different order, so line-by-line matching put numbers against the wrong partners. Re-aligning each page as one forward stream (pass B reversed as a whole) leaves 8 real disagreements on 16, 1 on 17, 1 on 18, 0 on 19, 1 on 24, 20 on 27 (mostly the margin insertion), 2 on 28, 11 on 29 (edge losses), 3 on 30. Each copy was then compared with the other, number by number (difflib over the full streams): 1,315 numbers of the copy (before the fixes listed below) stand in stretches identical to the letter.

Letter (images 16-24):
- 0016 L14: A=80?/86 B=80. Image: 80, gloss above reads q. Kept 80 (q, "qui").
- 0016 L15: A=38 B=28. Image (crop at 3x): 38 (curved top on the first figure), gloss e. Kept 38 (e, "s'entendent").
- 0016 L17: A=107?/108 B=107. Image 107; the copy (0027) has 107. Kept 107 (r).
- 0016 L20: A=177?/777 B=177. Image 177; copy 177. Kept 177 (s).
- 0016 L24: A=301?/304 B=301. Image: 30 plus a retouched last figure; copy 301. Kept 301 (l).
- 0016 L25: A=677?/673 B=677. Image: retouched; copy 677. Kept 677 (t).
- 0016 L26: A=698 B=698. Image: 698 (middle figure is a 9 as written). Out of range. The copy (0027 L14) has 658 (e). Emended 698 -> 658 (see Emendations).
- 0016 L27: A=651?/658 B=651. Copy 651. Kept 651 (p).
- 0016 L29: inked-out blot before 585, no number in the copy. Struck, not counted.
- 0016 L31: A=493?/193 B=493. Image 493 (first figure under a blot); copy 493. Kept 493 (d).
- 0016 L33: A=446?/416 B=446?/436. Image 446 (middle figure retouched); copy 446. Kept 446 (c).
- 0016 L36: A=[x#] B=#. Image: an ink blot between 371 and 362; the copy has nothing there. Struck, not counted.
- 0016 L39: A=288?/283 B=288?/283. Copy 288. Kept 288 (e, "eue").
- 0016 L41: A=549 B=549?/249. Copy 549. Kept 549 (r).
- 0017 L01: the last number is blotted out and a faint pencil "83." is written in the margin; the copy has 83 (".") at that point. Not counted in the letter (struck); the full stop is supplied from the copy.
- 0017 L18: "200" written small above 243 (Dumas's ink). The copy (0028 L05) has 200 243 in sequence, giving "leur assurer". Read as an insertion 200 before 243, not a replacement.
- 0017 L35: A=525 B=529. Copy 525. Kept 525 (s, "opprimés").
- 0018 L26: A=180 B=189?/180. Copy 180. Kept 180 (e).
- 0024 L02: A=10 B=20. Image: 10 (crop of L01-L03). Kept 10 (u, "jours").
- 0024 L12: A=108?/18. Copy 108; "reste" needs e. Kept 108 (e).
- 0024 L12: an inked-out number between 113 and 28 ("peu d[.] choses"). Struck, not counted; the copy also has 113 28 with nothing between.

Copy (images 27-30):
- 0027 L08: A=249 B=269?/279. Image: middle figure ambiguous; gloss above is q; the letter has 269. Read 269 (q).
- 0027 L12: A=680 B=681. Image: 68 plus a partly lost figure; gloss e; letter 681. Read 681 (e).
- 0027 L23: A=338?/333; letter 338. Read 338 (i).
- 0027 L33-L36 + left margin: the copyist struck part of L33 and wrote the struck passage again in the margin (vertical, "+"). Image: L36 reads "38.49.[overwritten].42.43.115050.54.34.+62.110". The overwritten number (B: 41?) has gloss e; the letter has 41. "115050" is written without dots; the letter has 115 50. Read 41 and 115 50. The "+" stands before 62 110, so the margin numbers (65 [struck] 55 120 ... 109) go between "cont" and "es": "contre ... aura secourues", the same as the letter.
- 0028 L02: A=92 B=192?/102. Image: first figure overwritten ("ı92"), gloss v. The letter has 102 (v). Read 102; the copy's figure is uncertain.
- 0028 L27: A=B=645 and 91. Image: 645 (letter 654; both are s) and "9ı" with gloss i (letter 98, i). 91 (r) is a copyist's slip; counted as unaccepted in the copy.
- 0028 L37: A=239 B=235. Image: 235, gloss m. Read 235 (m, "commerce").
- 0029: line-final numbers cut by the scan edge on L02, L03, L04, L05, L08, L11, L12, L13, L18, L19, L20, L21, L23, L24, L25, L28, L36, L37 (12 partial readings like "72?", "10?", "2?" and 6 wholly lost). All recorded as lost (#) for the copy; the letter supplies every one of them.
- 0029 L21: copy 205 (e) where the letter has 215 (s, "sous main"). Image: 205. Copyist's slip.
- 0029 L25: copy 322 (o) where the letter has 332 (p, "d'Espagne"). Image: 322. Copyist's slip.
- 0030 L03: A=985?/585 B=585. Image: the first figure is a looped 5. Read 585 (o).
- 0030 L17: A=371?/377 B=377?/379; gloss m. 371 is m; read 371 ("homme"). (Phrase only in the copy.)
- 0030 L20: copy 427 (d) where the letter has 424 (h, "la Haie"). Image: 427, gloss h. Copyist's slip.
- 0030 L21: copy 3 (u) where the letter has 31 (j, "je serai"). Image: "3.29", gloss over 3 unclear. Copyist's slip.
- 0030 L22: copy 90 (s) where the letter has 50 (o, "vos ordres"). Image: 90. Copyist's slip.
- 0030 L23: copy omits 15 (t) of "plutôt": 60 47 45 105 33.
- 0030 L27: A=564 B=504; letter 504 (q). Read 504.

## Numbers

Letter, images 16-19 and 23-24 (struck numbers left out; `{...}` = plain words written inside a run):

```
# img0016 run 1 before: "excepter de ce nombre les Rentiers intéressés dans les fonds publics"  after: "convienent dans cette conjoncture"
L13: 19 14 104 4 2 16 11 24 28 5 18 37 13 12 20 26
L14: 39 115 9 3 17 44 29 10 25 50 60 24 32 27 51 35 58 80 42 21
L15: 87 74 38 54 15 41 56 71 48 63 33 69 1 55 124 37 75 136 67
L16: 45 78 84 183 120 63 104 47 55 57 59 78 91 62 {Loin de vous}
L17: 90 72 181 94 81 107 53 119 207 {elles vous} 93 147 227 134
L18: 103 22 141 82 157 105 150 89 86 57 {à leurs} 159 100 61 108
L19: 173 111 142 133 {ou à leur} 172 114 81 119 83 70 116 175
L20: 85 73 88 162 77 177 269 96 66 8 131 106 101
# img0016 run 2 before: "convienent dans cette conjoncture"  after: "car leur intérêt est que vous"
L21: 207 227 281 122 189 64 220 155 23
L22: 200 158 128 423 135 241 233 506 144 190 186 178 238 139
L23: 153 272
# img0016 run 3 before: "car leur intérêt est que vous"  after: "inquiète. Je me suis donc"
L23: 211 140 40 141 160 36
L24: 301 150 118 204 164 215 241 675 679 659 681 651 673 661
L25: 635 678 627 677 676 633 671 663 281 660 627 625 663 664
L26: 642 658 666 637 698 {dont} 623 183 649 602 610 618 76
L27: 636 651 631 615 609 594 614 599 591 624 202 593
L28: 592 601 616 577 235 621 605 617 589
# img0016 run 4 before: "inquiète. Je me suis donc"  after: "& la copie & traduction de"
L29: 585 586 564 606 592 574 570 563 567
L30: 235 551 520 546 560 555 575 604 539 598 600 571 570
L31: 510 515 595
# img0016 run 5 before: "& la copie & traduction de"  after: "à mon sujet, sont depuis quinze jours au moins"
L31: 564 562 531 493
L32: 588 517 529 582 479 581 530 597 241 481 497 490 495
L33: 496 494 464 489 453 487 491 471 406 446 486
# img0016 run 6 before: "à mon sujet, sont depuis quinze jours au moins"  after: "& par conséquent"
L34: 399 388 389
L35: 398 397 390 391 394 373 387 384 377 385 346 392
L36: 371 362 342 338 386 358 376 393 374
# img0016 run 7 before: "& par conséquent"  after: "Dans la conversation"
L37: 325 350 382 349 353 316 367 395 355 341
L38: 329 439 365 401
# img0016 run 8 before: "Dans la conversation"  after: "j'ai bien pu"
L38: 269 293 292 273
L39: 281 279 271 292 277 290 274 257 288 255 252 282 287 250
L40: 254 203 215 284 285 265 272
# img0016 run 9 before: "j'ai bien pu"  after: "de" (page ends; continues on image 0017)
L40: 246 263 235 258
L41: 237 549 245 261 231 504 239 247 {les} 218 219 240 214 283
# img0017 run 1 before: "sa"  after: "font pour"
L01: 193 178 166 191 196 139
# img0017 run 2 before: "font pour"  after: "seulement"
L01: 195 192 197 198
L02: 162 161 580 183 169
# img0017 run 3 before: "seulement"  after: "contre les"
L02: 199 158 159 142 170 139
L03: 180 152 150 199 600 141 136 132 154 97 167
# img0017 run 4 before: "contre les"  after: "donner aux"
L04: 93 89 49 99 96 91 90 80 74 94 86 60 67 81
L05: 78 65 50 66 97
# img0017 run 5 before: "donner aux"  after: "c'est que, si"
L05: 49 50 73 9 68 53 82 87
# img0017 run 6 before: "c'est que, si"  after: "avec les Anglois,"
L06: 5 4 18 13 11 12 26 17 24 28 2 14 49 16 37
L07: 21 29 15
# img0017 run 7 before: "avec les Anglois,"  after: "la puissance qui les"
L07: 32 47 70 35 39 44 35 25 77
L08: 3 27 53 46 9 51 33 19 1 38 49 41 42 43 115 50 54 34
L09: 65 55
# img0017 run 8 before: "la puissance qui les"  after: "& imiteroient ainsi"
L09: 120 10 107 147 101 59 115
L10: 105 106 107 109 62 110
# img0017 run 9 before: "& imiteroient ainsi"  after: "Je n'avois rien de bon à répliquer, sinon"
L10: 126 72
L11: 112 124 424 103 82 100 101 113 89 146 147 199 155 118
L12: 154 108 194
# img0017 run 10 before: "s'ils voyoient qu'on ne venoit pas"  after: "ils se battoient, mais plutôt"
L14: 172 125 109 119 161 111 132 134
L15: 143 158 102 141 157 182 169 220 150 163 114 165 142
L16: 92 185 127 132 173 182 178 80 170 116 70 73 122
# img0017 run 11 before: "ils se battoient, mais plutôt"  after: "ils ne feroient pas assez méchants pour"
L17: 186 131 170 187 233 234 242
L18: 135 197 200 243 211 215 210 200 144 204
# img0017 run 12 before: "ils ne feroient pas assez méchants pour"  after: "avec ceux qui vouloient leur"
L19: 312 300 301 302 104 320 304 305
L20: 264 319 311 306 324 307 333 310 334 331 335 303 330
L21: 313 314 395 341 338 343 317 337 354 339
# img0017 run 13 before: "avec ceux qui vouloient leur"  after: "Enfin il a voulu savoir de moi positivement"
L22: 378 355 360 387 124 424 326 364 136
L23: 328 358 389 347 361 353 363 356 382 221 249
L24: 634
# img0017 run 14 before: "ce que je demandois"  after: "pour"
L25: 430 400 440 423 403 404 411
# img0017 run 15 before: "pour"  after: "Je lui ai répondu que vous desiriez de savoir Primo:"
L26: 448 407 405 439 409 449 416 406 431 413 418
L27: 30
# img0017 run 16 before: "de savoir Primo: si"  after: "bien,"
L28: 460 419 412 435 474 427 425 429 426 471 510 439
L29: 428 402 473 458 444 432 516 507 490
# img0017 run 17 before: "bien,"  after: "Secundo, au cas qu'une"
L29: 408 471
L30: 437 613 410 420 527 520 546 436 167 241 488 529
L31: 476 567 570 582 546 498 551 490 478 492 573
L32: 582 495 502 503 421 523 509 511 547 512 576
L33: 517 537 539 577 593 521 601 542 599 519 602 600
L34: 614 536 533 505 566 603 535 456 538 513 459 466
L35: 553 522 545 541 651 569 615 528 590 525 548 241
L36: 580 249 627 619 625 559 571 524 661 565 575 217
L37: 446 556 679 453 655 481 675 660 555 16 562 14 549
L38: 532 21 501 565 540 578 514 585 27 530 568 592 544
L39: 678 574 583 610 543 616 579 531 508 581 550 596
L40: 560 526 53 572 588 608 639 201 589 539 640 51 642
L41: 66 534 594 31 652 554 79 609 654 2 98 595 54 670 19
L42: 557 60 69 618 75 552 85 56 677
# img0018 run 1 before: "telle" (catchword "4elles" at foot of 0017)  after: "si les"
L01: 629 598 515 9 63 591 103 558 141 120 15 150
L02: 50 68 86 604 172 563 159 650 653 606 147 564 67
L03: 162 637 587 174 617 586 584
# img0018 run 2 before: "si les"  after: "Il goûta beaucoup la premiere de ces propositions,"
L03: 100 155 33 191
L04: 94 128 654 662 99 607 76 203 669 621 674 158 605
L05: 169 202 178 250 676 105 138 633 624 118 125 611
L06: 666 163 127 139 620 131 631 635 672 137 271 630 193
L07: 34 234 622 28 636 185 52 644 17 623 506 243 643
L08: 657 302 258 229 647 658 659 664 11 648 140 663
L09: 149 251 323 671 12 274 1 681 680 4 5
L10: 656 626 254 628 22 330 49 13 20 74 641 311
L11: 115 184 235 287 26 25 124 29 338 371 373 32
L12: 314 39 35 30
# img0018 run 3 before: "Il goûta beaucoup la premiere de ces propositions,"  after: "L'autre proposition ne lui déplaisoit pas non plus, sans"
L13: 71 183 192 23 199 46 353 65 279 44
L14: 196 329 31 38 646 342 41 78 209 362 37 341 104
L15: 47 213 384 91 48 84 55 107 59 377 113 119 62 18 378
L16: 186 387 431 43 430 665 151 58 668 273 72 57 87
L17: 152 82 90 440 3 61 134 89 93 124 219 420 488
L18: 108 471 10 171 101 474 111 388 110 30
# img0018 run 4 before: "ne lui déplaisoit pas non plus, sans"  after: "Je lui remis donc, avec l'Extrait de votre Lettre,"
L19: 70 281
L20: 424 228 143 157 507 118 73 114 238 42 116 165 173
L21: 122 80 45 546 112 506 135 406 117 81 551 8 187 236
L22: 573 64 144 510 153 96 200 253 295 160 194
# img0018 run 5 before: "un petit Mémoire, où j'insinue combien il importe"  after: "Le tout a été envoyé à"
L25: 527 88 529 395 204 570 520 136 164 244 176 567
L26: 180 298 576 123 95 593 577 129 133 188 216 175 106 163
L27: 667 109 476 132 205 224 126 222 177 181 276 146 297 582
L28: 601 225 189 401
# img0018 run 6 before: "Le tout a été envoyé à"  after: "il y a quinze jours environ;"
L28: 190 614
L29: 227 319 170 231
# img0018 run 7 before: "& qu'elle ne peut que bien disposer"  after: (runs on to next image 0019)
L32: 154 619
L33: 429 237 660 599 252 232 309 322 197 246 102 349
L34: 210 198 268 241 161 74 240 602 561 678 625 247 285
L35: 19 97 352 182 217 294 256 296 597 69 485 75 121 403
L36: 299 615 211 261 305 498 286 517 263 215 409 214 312
L37: 528 85 655 627 220 265 335 339 282 255 416 239 324 340
# img0019 run 1 before: (continues run 7 of image 0018)  after: "Voilà pourquoi j'ai copié exactement, dans l'Extrait, ce"
L01: 269 245 288 130 435 344 148 120 675 357 366 290 147 266
L02: 267 318 292 270 156 300 661 142 166 16 331 304 354 262
L03: 307 600 355 155 679 264 310 207 289 183 313 375 332
L04: 158 104 14 317 241 316 326 379 21 233 328 380 634
# img0019 run 2 before: "ce que vous me marquez avoir"  after: "Tout cela je l'ai exécuté avec le plus profond secret,"
L06: 242 347 336 260 270 385
L07: 259 356 386 473 53 27 268 423 516 528 580 359 66 51
L08: 238 24 54 79 365 277 360 394 272 169 364 76 367 400
L09: 308 202 293 56 98 221 103 523 63 405 638
# img0019 run 3 before: "c'est aussi le meilleur pour votre service & pour"  after: "Mr. Storey, en partant pour l'Angleterre,"
L15: 235 178 418 320 382 374 230 77 345
L16: 504 334 376 31 381 63 391 442 542 141 455 348 545
L17: 150 68 248 446 556 86 100 337 408 562 350 393
L18: 372 284 396 397 439 613 234 398 476 92 325 399
L19: 179 585 462 243 199 22 258 159 411 407 470 682
# img0023 run 1 before: "Vous serez peut-être tenté, Monsieur, de venir voir"  after: "j'aurai l'honneur de vous y renouveller"
L29: 4 19 22 2 16 17 5 20 13 18 69
L30: 424 75 21 26
# img0024 run 1 before: (top of page; previous page ends "les sentimens d'une sincere estime.")  after: "si vous voulez bien m'écrire un mot de votre logement"
L01: 31 29 11 32 25 85 53 120 1 9 12 50 46 71 65 35
L02: 39 34 67 3 44 37 38 87 273 94 10 78 58 147 76 66
L03: 84 79 207 99 42 60 47 45 15 105 33 268
# img0024 run 2 before: "pour me faire savoir l'heure qui vous sera la plus comode. Nous pourrons"  after: "ce sera avec une vérité & une candeur que"
L06: 172 613 98 70 125
L07: 87 127 185 424 41 91 80 81 48 73 269 96 55 90 202
L08: 131 235 59 14 93 101 106 107 262 62 110
L09: 137 118 667 72 57 112 504 109 82 27 140 132
L10: 117 178 8 149 51 123 152 24 273 155 52 119
L11: 158 103 61 77 129 83 133 74 141 88 287 89 134
L12: 108 175 64 111 186 114 170 113 28 424 184
L13: 177 116 189 169 102 192 197 190 244 150 143 122
L14: 272
```

Copy ("Extrait"), images 27-30 (# = lost at the scan edge or blotted; margin = the left-margin insertion on 27):

```
# img0027 run 1 before: "Pour comencer à m'en servir, je vous dirai, Messieurs, que"  after: "convienment dans cette conjoncture,"
L08: 70 116 175 85 73 88 162 77 177 269
L09: 96 66 8 131 106 101
# img0027 run 2 before: "convienment dans cette conjoncture, c'est"  after: "car leur intérêt est que vous"
L10: 220 155 23 200 158 128 423 135 241 233 506 144 190
L11: 186 178 238 139 153 272
# img0027 run 3 before: "car leur intérêt est que vous"  after: "dont"
L11: 211 140
L12: 40 141 160 36 301 150 118 204 164 215 241 675 679 659 681
L13: 651 673 661 635 678 627 677 676 633 671 663 281 660 627
L14: 625 663 664 642 658 666 637 658
# img0027 run 4 before: "dont"  after: "inquiete. Je me suis donc"
L14: 623 183 649
L15: 602 610 618 76 636 651 631 615 609 594 614 599 591
L16: 624 202 593 592 601 616 577 235 621 605 617 589
# img0027 run 5 before: "inquiete. Je me suis donc"  after: "& la copie & traduction de"
L17: 585 586 564 606 592 574 570
L18: 563 567 235 551 520 546 560 555 575 604 539 598 600 571
L19: 570 510 515 595
# img0027 run 6 before: "& la copie & traduction de"  after: "à mon sujet, sont de puis quinze jours au moins"
L19: 564 562 531 493
L20: 588 517 529 582 479 581 530 597 241 481 497 490 495 496 494
L21: 464 489 453 487 491 471 406 446 486
# img0027 run 7 before: "sont de puis quinze jours au moins"  after: "& par conséquent"
L22: 399 388 389 398 397 390 391 394
L23: 373 387 384 377 385 346 392 371 362 342 338 386 358
L24: 376 393 374
# img0027 run 8 before: "& par conséquent"  after: "Dans la conversation"
L24: 325 350 382 349 353 316 367
L25: 395 355 341 329 439 365 401
# img0027 run 9 before: "Dans la conversation"  after: "j'ai bien pu"
L25: 269 293
L26: 292 273 281 279 271 292 277 290 274 257 288 255 252 282
L27: 287 250 254 203 215 284 285 265 272
# img0027 run 10 before: "j'ai bien pu"  after: "les"
L27: 246 263
L28: 235 258 237 549 245 261 231 504 239 247
# img0027 run 11 before: "les"  after: "de sa"
L28: 218 219 240 214
L29: 283
# img0027 run 12 before: "de sa"  after: "sont pour"
L29: 193 178 166 191 196 139
# img0027 run 13 before: "sont pour"  after: "seulement"
L29: 195 192 197 198
L30: 83 162 161 580 183 169
# img0027 run 14 before: "seulement"  after: "contre les"
L30: 199 158 159 142 170 139
L31: 180 152 150 199 600 141 136 132 154 97 167
# img0027 run 15 before: "contre les"  after: "donner aux"
L31: 93 89 49
L32: 99 96 91 90 80 81 74 94 86 60 67 81 78 65 50 66 97
# img0027 run 16 before: "donner aux"  after: "c'est que si [rest of line heavily struck through]"
L33: 49 50 73 9 68 53 82 87
# img0027 run 17 before: "c'est que si [struck]"  after: "avec les Anglois"
L34: 5 4 18 13 11 12 26 17 24 28 2 14 49 16 37 21 29 14 15
# img0027 run 18 before: "avec les Anglois"  after: "& imiteroient ainsi"
L35: 32 47 70 35 39 44 35 25 77 3 27 53 46 9 51 33 19 1
L36: 38 49 41 42 43 115 50 54 34 62 110
# img0027 run 19 before: "& imiteroient ainsi"  after: "Je n'eus rien de bon à repliquer"
L36: 126
L37: 72 112 124 424 103 82 100 101 113 89 146 147 199 155 118 154 108
L38: 194
# img0027 run 20 (left margin, written vertically bottom-to-top, marked "+"; probably the insertion for the struck passage on L33)  before: "+"  after: "la puissance qui les"
M: 65 55
# img0027 run 21 (left margin, continued)  before: "la puissance qui les"  after: (end of margin note)
M: 120 10 107 147 101 59 115 105 106 107 109
# img0028 run 1 before: "raisonnables, s'ils voyoient qu'on ne vanoit pas"  after: "ils se battoient, mais plutôt"
L01: 172 125 109
L02: 119 161 111 132 134 143 158 102 141 157 182 169 220 150 163 114
L03: 165 142 92 185 127 132 173 182 178 80 170 116 70 73 122
# img0028 run 2 before: "ils se battoient, mais plutôt"  after: "ils ne seroient pas assez méchants pour"
L04: 186 131 170 187 233 234 242
L05: 135 197 200 243 211 215 210 200 144 204
# img0028 run 3 before: "ils ne seroient pas assez méchants pour"  after: "avec ceux qui vouloient leur"
L06: 312 300 301 302 104 320 304 305
L07: 264 319 311 306 324 307 333 310 334 331 335 303 330
L08: 313 314 395 341 338 343 317 337 354 339
# img0028 run 4 before: "avec ceux qui vouloient leur"  after: "Enfin il a voulu savoir de moi positivement ce que je demandois"
L09: 378 355 360 387 124 424 326 364 136
L10: 328 358 389 347 361 353 363 356 382 221 249 634
# img0028 run 5 before: "ce que je demandois"  after: "pour"
L12: 430 400 440 423 403 404 411
# img0028 run 6 before: "pour"  after: "Je lui ai répondu qu'on desiroit de savoir Primo: si"
L12: 448 407
L13: 405 439 409 449 416 406 431 413 418 30
# img0028 run 7 before: "de savoir Primo: si"  after: "bien,"
L14: 460 419 412 435 474
L15: 427 425 429 426 471 510 439 428 402 473 458 444 432
L16: 516 507 490
# img0028 run 8 before: "bien,"  after: "Secundo au cas qu'une telle"
L16: 408 471 437 613 410 420 527 520 546
L17: 436 167 241 488 529 476 567 570 582 546 498 551
L18: 490 478 492 573 582 495 502 503 421 523 509 511 547
L19: 512 576 517 537 539 577 593 521 601 542 599 519 602 600
L20: 614 536 533 505 566 603 535 456 538 513 459 466 553
L21: 522 545 541 651 569 615 528 590 525 548 241 580 249
L22: 627 619 625 559 571 524 661 565 575 217 446 556 679
L23: 453 655 481 675 660 555 16 562 14 549 532 21 501 565
L24: 540 578 514 585 27 530 568 592 544 678 574 583 610 543
L25: 616 579 531 508 581 550 596 560 526 53 572 588 608
L26: 639 201 589 539 640 51 642 66 534 594 31 652 554 79
L27: 609 645 2 91 595 54 670 19 557 60 69 618 75 552 85
L28: 56 677
# img0028 run 9 before: "Secundo au cas qu'une telle"  after: "si les"
L28: 629 598 515 9 63
L29: 591 103 558 141 120 15 150 50 68 86 604 172 563 159 650 653 606
L30: 147 564 67 162 637 587 174 617 586 584
# img0028 run 10 before: "si les"  after: (end of page; continues on image 0029)
L30: 100 155 33
L31: 191 94 128 654 662 99 607 76 203 669 621 674 158 605 169
L32: 202 178 250 676 105 138 633 624 118 125 611 666 163 127
L33: 139 620 131 631 635 672 137 271 630 193 34 234 622 28
L34: 636 185 52 644 17 623 506 243 643 657 302 258 229
L35: 647 658 659 664 11 648 140 663 149 251 323 671 12 274
L36: 1 681 680 4 5 656 626 254 628 22 330 49 13 20 74 641
L37: 311 115 184 235 287 26 25 124 29 338 371 373 32 314 39 35
L38: 30
# img0029 run 1 before: "Il goûta beaucoup la premiere de ces propositions,"  after: "L'autre ne lui déplaisoit pas non plus sans"
L01: 71 183
L02: 192 23 199 46 353 65 279 44 196 329 31 38 646 342 41 #
L03: 209 362 37 341 104 47 213 384 91 48 84 55 107 59 377 #
L04: 119 62 18 378 186 387 431 43 430 665 151 58 668 273 #
L05: 57 87 152 82 90 440 3 61 134 89 93 124 219 420 488 #
L06: 471 10 171 101 474 111 388 110
# img0029 run 2 before: "L'autre ne lui déplaisoit pas non plus sans"  after: "Je lui remis donc, avec l'extrait de votre Lettre, un petit mémoire où j'insinue combien il importe"
L07: 70 281 424 228 143 157 507 118 73 114
L08: 238 42 116 165 173 122 80 45 546 112 506 135 406 117 81 #
L09: 8 187 236 573 64 144 510 153 96 200 253 295 160 194
# img0029 run 3 before: "un petit mémoire où j'insinue combien il importe"  after: "Le tout a été envoyé à"
L11: 527 88 529 395 204 #
L12: 520 136 164 244 176 567 180 298 576 123 95 593 577 129 #
L13: 188 216 175 106 163 667 109 476 132 205 224 126 222 #
L14: 181 276 146 297 582 601 225 189 401
# img0029 run 4 before: "Le tout a été envoyé à"  after: "& quand la réponse tarderoit"
L15: 190 614 227 319 170 231
# img0029 run 5 before: "l'ouverture est faite, & qu'elle ne peut que bien disposer"  after: "Voilà pourquoi j'ai copié exactement dans l'Extrait"
L18: 154 619 429 237 660 599 252 232 309 322 197 246 #
L19: 349 210 198 268 241 161 74 240 602 561 678 625 247 #
L20: 19 97 352 182 217 294 256 296 597 69 485 75 121 403 #
L21: 615 211 261 305 498 286 517 263 205 409 214 312 528 #
L22: 655 627 220 265 335 339 282 255 416 239 324 340 269
L23: 245 288 130 435 344 148 120 675 357 366 290 147 266 #
L24: 318 292 270 156 300 661 142 166 16 331 304 354 262 #
L25: 600 355 155 679 264 310 207 289 183 313 375 322 #
L26: 104 14 317 241 316 326 379 21 233 328 380 634
# img0029 run 6 before: "ce dont vous me marquez avoir"  after: "Tout cela je l'ai exécuté avec le plus profond secret"
L28: 242 347 336 260 270 385 259 #
L29: 386 473 53 27 268 423 516 528 580 359 66 51 238 24
L30: 54 79 365 277 360 394 272 169 364 76 367 400 308 202
L31: 293 56 98 221 103 523 63 405 638
# img0029 run 7 before: "Et c'est aussi le meilleur pour votre [blotted word] service &"  after: (foot of page; continues on image 0030)
L36: 235 178 418 #
L37: 382 374 230 77 345 504 334 376 31 381 63 391 442 542 141 #
# img0030 run 1 before: (top of page; continues from previous image)  after: "Je vous disois ensuite, Messieurs, que Mr. Storey"
L01: 348 545 150 68 248 446 556 86 100 337 408 562 350 393
L02: 372 284 396 397 439 613 234 398 476 92 325 399 179
L03: 585 462 243 199 22 258 159 411 407 470 682
# img0030 run 2 before: "la lettre que j'avois reçue le 9e May de"  after: "datée du 6e May. En voici une seconde copie"
L17: 54 196 97 157 135 424 209 371 373 144 262 153 88 178
L18: 613 234 159 160
# img0030 run 3 (quoted letter; SMALL numbers 1-120 dominate here)  before: "Vous serez peut-être tenté, Monsieur, de venir voir"  after: "J'aurai l'honneur de vous y re-"
L19: 4 19 22 2
L20: 16 17 5 20 13 18 69 427 75 21 26
# img0030 run 4 before: "nouvelles les sentimens d'une sincere estime"  after: "si vous voulez bien m'écrire un mot de votre logement"
L21: 3 29 11 32 25 85 53
L22: 120 1 9 12 90 46 71 65 35 39 34 67 3 44 37 38 87 273 94 10 78 58 147
L23: 76 66 84 79 207 99 42 60 47 45 105 33 268
# img0030 run 5 before: "l'heure qui vous sera la plus comode. Nous pourrons"  after: "ce sera avec une vérité & une candeur"
L25: 172 613 98 70 125 87 127 185 424
L26: 41 91 80 81 48 73 269 96 55 90 202 131 235 59 14 93 101 106 107 262
L27: 62 110 137 118 667 72 57 112 504 109 82 27 140 132 117 178 8 149 51
L28: 123 152 24 273 155 52 119 158 103 61 77 129 83 133 74 141 88 287 89
L29: 134 108 175 64 111 186 114 170 113 28 424 184 177 116 189 169 102 192
L30: 197 190 244 150 143 122 272
```

## Raw decode

Letter:

```
# img0016 run 1
angloisecellesdescourseuropeennesquis'entendentaveclacourd'angleterre {Loin de vous} secourir, {elles vous} sacrifieroient {à leurs} interets {ou à leur} peur.lesalliesquivous
# img0016 run 2
,c'estlafrance&l'espagne,
# img0016 run 3
soyiezlibres&independantsdel'angleterr[698] {dont} l'enormepuissancemaritimeles
# img0016 run 4
ouvertaunministredefrance
# img0016 run 5
vosdemandes,&lettredecreance
# img0016 run 6
entrelesmainsduministere
# img0016 run 7
duroidefrance.
# img0016 run 8
quej'aieueavecceministre,
# img0016 run 9
remarquerque {les} voeux
# img0017 run 1
nation
# img0017 run 2
vousilm'a
# img0017 run 3
faitunedifficulte
# img0017 run 4
secoursq'onpourroit
# img0017 run 5
colonies
# img0017 run 6
ellessereconciliet
# img0017 run 7
ellessereunirontaveceuxcontre
# img0017 run 8
aurasecourues
# img0017 run 9
leschiensdelafable.
# img0017 run 10
pourleurravirlalibertepourlaquelle
# img0017 run 11
pourlaleurassurer
# img0017 run 12
seliguercontreleursbienfaiteurs
# img0017 run 13
arrachercetteliberte.
# img0017 run 14
asacour
# img0017 run 15
lescolonies?
# img0017 run 16
leroidefrancevoudroit
# img0017 run 17
parhumanite&magnanimite,interposersamediationenfaveurdepeuplesopprimes,&menagerunereconciliationquileurconservattoutesleurslibertesdontilsjouissoientauparavant
# img0018 run 1
reconciliationnepuisseavoirlieu,
# img0018 run 2
nationssoumisesalamaisondebourbonvoudroientaccepterl'alliancedescoloniesaveclebeneficed'uncommerceimmense?
# img0018 run 3
d'offrirasonjeuneroilagloirederendrelapaixauxsujetsdesautrescommeauxsiens?
# img0018 run 4
l'horribleguerrequis'ensuivroiteneurope.
# img0018 run 5
alafrancedenepaslaissersubjuguerlescolonies.
# img0018 run 6
sacour
# img0018 run 7
lafrancepourvous,&l'engageratolerer,afavorisermemesousmainlessecours
# img0019 run 1
quevosvaisseauxpeuventtirerdefrance,d'espagne&desiles.
# img0019 run 2
leplusbesoin,commeingenieurs,armes,munitions.
# img0019 run 3
masurete,quejenesoispointconnupouretrechargedevosaffaires.
# img0023 run 1
lafoiredelahaie
# img0024 run 1
jeseraiavosordrestouslesjoursamidi,ouplutot,
# img0024 run 2
philosopherquelquesmomenssurdesobjetsquenousavonsdejatraites.s'ilmerestepeudchosesavousdire,
```

Copy:

```
# img0027 run 1
lesalliesquivous
# img0027 run 2
lafrance&l'espagne,
# img0027 run 3
soyiezlibres&independantsdel'angleterre
# img0027 run 4
l'enormepuissancemaritimeles
# img0027 run 5
ouvertaunministredefrance
# img0027 run 6
vosdemandes,&lettredecreance
# img0027 run 7
entrelesmainsduministere
# img0027 run 8
duroidefrance.
# img0027 run 9
quej'aieueavecceministre,
# img0027 run 10
remarquerque
# img0027 run 11
voeux
# img0027 run 12
nation
# img0027 run 13
vous.ilm'a
# img0027 run 14
faitunedifficulte
# img0027 run 15
secoursqu'onpourroit
# img0027 run 16
colonies
# img0027 run 17
ellessereconcilient
# img0027 run 18
ellessereunirontaveceuxcontes
# img0027 run 19
leschiensdelafable.
# img0027 run 20 (left margin, written vertically bottom-to-top, marked "+"; probably the insertion for the struck passage on L33) 
re
# img0027 run 21 (left margin, continued) 
aurasecouru
# img0028 run 1
pourleurravirlalibertepourlaquelle
# img0028 run 2
pourlaleurassurer
# img0028 run 3
seliguercontreleursbienfaiteurs
# img0028 run 4
arrachercetteliberte.
# img0028 run 5
asacour
# img0028 run 6
lescolonies?
# img0028 run 7
leroidefrancevoudroit
# img0028 run 8
parhumanite&magnanimite,interposersamediationenfaveurdepeuplesopprimes,&menagerunereconciliationquileurconservattoutesleurslibertesdontilsjouissorentauparavant
# img0028 run 9
reconciliationnepuisseavoirlieu,
# img0028 run 10
nationssoumisesalamaisondebourbonvoudroientaccepterl'alliancedescoloniesaveclebeneficed'uncommerceimmense?
# img0029 run 1
d'offrirasonjeune#oilagloirederen#relapaixauxsuj#tsdesautrescomm#auxsiens
# img0029 run 2
l'horribleguerrequis'ensu#vroiteneurope.
# img0029 run 3
alafr#ncedenepaslais#ersubjuguerle#colonies.
# img0029 run 4
sacour
# img0029 run 5
lafrancepour#ous,&l'engage#atolerer,afavo#isermemeeousm#inlessecoursquevosvaisseau#peuventtirerd#france,d'eso#gne&desiles.
# img0029 run 6
leplusb#soin,commeingenieurs,armes,munitions.
# img0029 run 7
mas#rete,quejenesoi#
# img0030 run 1
pointconnupouretrechargedevosaffaires.
# img0030 run 2
notrehommedelahaie
# img0030 run 3 (quoted letter; SMALL numbers 1-120 dominate here) 
lafoiredeladaie
# img0030 run 4
ueseraiavossrdrestouslesjoursamidi,oupluot,
# img0030 run 5
philosopherquelquesmomenssurdesobjetsquenousavonsdejatraites.s'ilmerestepeudchosesavousdire,
```

## Normalized text

Cipher passages in [brackets], plain words of the letter outside them (from the transcribers' context notes and the images). Text of the letter; the copy differs only where noted. A plain ... marks plain text of the letter left out of this excerpt; it is not an unread word (it was written with square brackets before 15 Nov 2026, when holes came to be counted by words).

30 April 1776 (image 16 onward): "... & qu'il faut excepter de ce nombre les Rentiers intéressés dans les fonds publics [anglois, e(t) celles des cours européennes qui s'entendent avec la cour d'Angleterre]. Loin de vous [secourir], elles vous [sacrifieroient] à leurs [intérêts] ou à leur [peur. Les alliés qui vous] conviennent dans cette conjoncture[, c'est la France & l'Espagne,] car leur intérêt est que vous [soyiez libres & indépendants de l'Angleterre] dont [l'énorme puissance maritime les] inquiète. Je me suis donc [ouvert à un ministre de France,] & la copie & traduction de [vos demandes & lettre de créance] à mon sujet sont depuis quinze jours au moins [entre les mains du ministère] & par conséquent [du roi de France.] Dans la conversation [que j'ai eue avec ce ministre,] j'ai bien pu [remarquer que] les [voeux] de sa [nation] sont pour [vous. Il m'a] seulement [fait une difficulté] contre les [secours q(u)'on pourroit] donner aux [colonies]; c'est que, si [elles se réconcili(e)nt] avec les Anglois, [elles se réuniront avec eux contre] la puissance qui les [aura secourues] & imiteroient ainsi [les chiens de la fable.] Je n'avois rien de bon à répliquer, sinon que s'agissant d'êtres raisonnables, s'ils voyoient qu'on ne venoit pas [pour leur ravir la liberté pour laquelle] ils se battoient, mais plutôt [pour la leur assurer], ils ne seroient pas assez méchants pour [se liguer contre leurs bienfaiteurs] avec ceux qui vouloient leur [arracher cette liberté.] Enfin il a voulu savoir de moi positivement ce que je demandois [à sa cour] pour [les colonies?] Je lui ai répondu que vous desiriez de savoir, Primo: si [le roi de France voudroit] bien, [par humanité & magnanimité, interposer sa médiation en faveur de peuples opprimés, & ménager une réconciliation qui leur conservât toutes leurs libertés dont ils jouissoient auparavant.] Secundo, au cas qu'une telle [réconciliation ne puisse avoir lieu,] si les [nations soumises à la maison de Bourbon voudroient accepter l'alliance des colonies avec le bénéfice d'un commerce immense?] Il goûta beaucoup la première de ces propositions, [d'offrir à son jeune roi la gloire de rendre la paix aux sujets des autres comme aux siens?] L'autre proposition ne lui déplaisoit pas non plus, sans [l'horrible guerre qui s'ensuivroit en Europe.] Je lui remis donc, avec l'Extrait de votre Lettre, un petit Mémoire, où j'insinue combien il importe [à la France de ne pas laisser subjuguer les colonies.] Le tout a été envoyé à [sa cour] il y a quinze jours environ; ... & qu'elle ne peut que bien disposer [la France pour vous, & l'engager à tolérer, à favoriser même sous main les secours que vos vaisseaux peuvent tirer de France, d'Espagne & des îles.] Voilà pourquoi j'ai copié exactement, dans l'Extrait, ce que vous me marquez avoir [le plus besoin, comme ingénieurs, armes, munitions.] Tout cela je l'ai exécuté avec le plus profond secret, ... c'est aussi le meilleur pour votre service & pour [ma sûreté, que je ne sois point connu pour être chargé de vos affaires.]"

9 May 1776, the unsigned letter Dumas copied (images 23-24; second copy on image 30): "Vous serez peut-être tenté, Monsieur, de venir voir [la foire de la Haie]; j'aurai l'honneur de vous y renouveller les sentimens d'une sincère estime. [Je serai à vos ordres tous les jours à midi, ou plutôt,] si vous voulez bien m'écrire un mot de votre logement pour me faire savoir l'heure qui vous sera la plus comode. Nous pourrons [philosopher quelques momens sur des objets que nous avons déjà traités. S'il me reste peu d(e) choses à vous dire,] ce sera avec une vérité & une candeur que je me flatte que vous approuverez."

Copy only (image 30): "Enfin ma Lettre finissoit par vous communiquer la lettre que j'avois reçue le 9e May de [notre homme de la Haie] datée du 6e May. En voici une seconde copie."

## Translation

"... and that one must except from this number the holders of English public funds, and those European courts that have an understanding with the court of England. Far from helping you, they would sacrifice you to their interests or to their fear. The allies who suit you in this situation are France and Spain, for it is in their interest that you be free and independent of England, whose enormous sea power alarms them. I have therefore opened myself to a minister of France, and the copy and translation of your requests and of the letter of credence concerning me have been for at least a fortnight in the hands of the ministry, and so of the King of France. In my conversation with this minister I was able to see that the wishes of his nation are for you. He raised only one difficulty against the help that might be given to the colonies: that if they were reconciled with the English they would join with them against the power that had helped them, and so imitate the dogs in the fable. I had no good answer except that, rational beings being concerned, if they saw that one came not to rob them of the liberty for which they were fighting but rather to secure it to them, they would not be wicked enough to league against their benefactors with those who wished to tear that liberty from them. At last he wished to know from me exactly what I was asking of his court for the colonies. I answered that you wished to know, first, whether the King of France would be willing, from humanity and magnanimity, to interpose his mediation in favour of oppressed peoples and bring about a reconciliation that would keep for them all the liberties they enjoyed before; second, in case such a reconciliation cannot take place, whether the nations subject to the House of Bourbon would accept the alliance of the colonies with the benefit of an immense commerce. He much liked the first of these proposals, to offer his young king the glory of giving peace to the subjects of others as to his own. The other did not displease him either, were it not for the horrible war that would follow in Europe. So I gave him, with the extract of your letter, a short memorandum suggesting how much it matters to France not to let the colonies be subjugated. The whole was sent to his court about a fortnight ago; ... and it can only dispose France well towards you and lead her to tolerate, even to favour secretly, the supplies your ships can draw from France, Spain and the islands. That is why I copied exactly, in the extract, what you tell me you most need, such as engineers, arms, munitions. All this I have done in the deepest secrecy ... it is also best for your service and for my safety that I not be known as the man in charge of your affairs."

9 May (unsigned letter): "You may be tempted, Sir, to come and see the fair at The Hague; I shall have the honour of renewing there the sentiments of a sincere esteem. I shall be at your orders every day at noon, or earlier, if you will write me a word from your lodging to tell me the hour that suits you best. We can philosophize for a few moments on subjects we have already treated. If I have little left to tell you, it will be with a truth and candour that I flatter myself you will approve." Copy only: "the letter I had received on 9 May from our man at The Hague, dated 6 May."

## Share read

- Letter: 1,464 numbers (struck numbers excluded; 151 of them in the 9 May part). Read without emendation: 1,463 / 1,464 = 99.9 % (only 698 is out of range). After emendation: 1,464 / 1,464 = 100 %. Two letters are missing in the letter (no number written: "réconcili(e)nt", "peu d(e) choses"); both are supplied in the normalized text and, for the first, by the copy.
- Copy: 1,372 number places, of which 18 are lost at the scan edge or blotted; 1,354 legible; 1,348 give an accepted letter (6 copyist's slips: 91, 205, 322, 427, 3, 90) = 98.3 % of all places (99.6 % of legible numbers). After emendation from the letter: 1,354 / 1,372 = 98.7 %; the 18 lost places are all supplied by the letter.

## Emendations

- 0016 L26 `{emended: 698 [out of range] -> 658 e, from the copy (0027 L14 has 658)}` — "Angleterre". alt.py: 698 has no letter; misreads 98=i, 598=e, 648=c; the copy settles 658.
- 0017 L06-L07 `{emended: n supplied after 29, from the copy (0027 L34 has 21 29 14 = "ient")}` — "réconcili(e)nt"; the letter's run is 21 29 15 = "...iet".
- 0016 L13 "angloise celles": no number for t; read "anglois, e(t) celles" (Franklin Papers print "anglois et celles"). Not a wrong number; noted only.
- 0024 L12 "peu d choses" (113 then a struck number, then 28): e not written in either copy; supplied in the normalized text.
- Copy only (not used for the text, which follows the letter): 0028 L27 91 r -> 98 i ("jouissoient"); 0029 L21 205 e -> 215 s; 0029 L25 322 o -> 332 p; 0030 L20 427 d -> 424 h; 0030 L21 3 u -> 31 j; 0030 L22 90 s -> 50 o; 0030 L23 missing 15 t.
- Copy additions that are not slips: 0027 L30 has 83 "." after "vous" (struck in the letter); 0027 L32 has 81 "u" in "qu'on" (letter "q'on"); 0028 L05 has 200 in line ("leur"), where the letter has it as a correction above the line.

## Print check

Classification: **printed with the cipher read** — in French in the Franklin Papers (vol. 22, pp. 403-412, cipher passages in brackets, `print/franklin22_30apr1776_cipher.txt`), and in English translation in Sparks, Diplomatic Correspondence vol. 9 pp. 260-267 (`print/sparks9_11457.txt`), reprinted by Wharton vol. 2 (from line 4927 of `web/revolutionarydip021889unit.txt`, "Dumas to Franklin", from Sparks). Sparks and Wharton do not mark the cipher; their text contains every cipher passage in translation. Sparks does not print the "notre homme de la Haie" phrase (it is only in the copy).

Agreement (selection, ours / Franklin Papers / Sparks):
- [les alliés qui vous] conviennent ... [c'est la France & l'Espagne] / "[peur. Des alliés qui vous]" "[, c'est la france et l'espagne,]" / "The allies, which under such circumstances are suitable for you, are France and Spain".
- [ouvert à un ministre de France] / "[ouvert a un ministre de fiance]" / "I have, therefore, opened myself to the French Minister".
- [les chiens de la fable.] / "[les chiens de la fable.]" / "would imitate the dog in the fable".
- [... d'Espagne & des îles.] / "[... d'espagne et des iles.]" / "from France, Spain, and the Indies".
- [la foire de la Haie] ... [Je serai à vos ordres tous les jours à midi, ou plutôt,] / same / "the fair at the Hague ... I shall be at your orders every day at noon or sooner".

Differences:
1. "ministre de **fiance**" (Franklin Papers) vs **france** (ours). Settled on the images: the run is 600 571 570 510 515 595 in both the letter (0016 L30-L31) and the copy (0027 L18-L19); 571 is r, and the decipherer's gloss over 571 on the copy (image 27, crop at 1.8x) is r. "fiance" is a slip in the printed text. Sparks: "the French Minister".
2. "**Des** alliés" (Franklin Papers) vs **Les** (ours): 70 (l) in both the letter (0016 L19) and the copy (0027 L08); 71 would be d. Sparks "The allies". Added after the independent check: the contemporary gloss over 70 on the copy (image 27) looks like d. So "Les" is right by the key, but the slip "Des" was the period decipherer's, and the editors followed the interlined decoding (they say the decoding "has been interlined on the ms."). It is a decipherer's slip carried into print, not an editors' error.
3. Franklin Papers "anglois **et** celles", "q**u**'on pourroit", "réconcili**e**nt", "jouiss**aient**", "peu de choses": they silently supply letters Dumas left out in the letter (t; u and e are in the copy) and modernize one spelling; no change of sense.
4. Sparks/Wharton: "dog" for "chiens"; "the Indies" for "des îles" (the French West Indies); "required it from me, and promised it in return" and "It is more advantageous to you and safer for me, that I should not be known as your agent" render plain and cipher text freely. No disagreement in names or numbers.

Decipherer: the letter has faint pencil letters over the numbers of 16-19 and 23-24; the copy has a letter in ink over nearly every number (images 27-30). The Franklin Papers editors say the decoding "has been interlined on the ms." Whose hand is not shown by anything on these pages; not attributed.

## Remarks

- Checked on the image: every disagreement listed above that is marked "Image:", plus the "fiance/france" and "Des/Les" points. The other copy-vs-letter differences were settled by agreement of the two passes with the other copy and by sense, not by crop.
- The letter (folios 20-28) is the better text; the copy (folios 31-34) was written after 9 May (its heading "May" is corrected to "Avril") and adds "notre homme de la Haie" to identify the writer of the unsigned letter.
- No sign of a different system: the small numbers 1-130 in the unsigned letter (images 23-24, 30) are positions of the same 682-character key.

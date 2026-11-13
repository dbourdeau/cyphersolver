# mirabel1622: the Marquis of Mirabel to the Count of Gondomar, Paris, early 1622 (BNE MSS/18428, viewer images 13 right - 15 left; catalogue 1271)

Status: **read in part** (Brice Dudout, 14 Nov 2026). 250 cipher words: 183 certain, 36 probable, 11 restored, 20 unresolved;
**sure words only 183/250 = 73.2%**; certain + probable 219/250 = 87.6%. Key CLE_M02 **not validated** by the contributor's
protocol: M01 failed (part B), M02 partial (part A). See `reading.md`, `validation.txt`.

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Pointer: catalogue entry 1271 (Daniel Bourdeau,
BNE/Hispana sweep); inventory of the volume in issue #367 (9 Nov 2026).

## Document

Madrid, Biblioteca Nacional de España, MSS/18428 (Gayangos), BDH 0000141369: letters of Antonio Dávila y Zúñiga, Marquis of Mirabel,
Spanish ambassador in Paris, to Diego Sarmiento de Acuña, Count of Gondomar, 1621-1624, 112 viewer images. Cipher only in the 1622
letters (images 5-44). The letter read here runs from the foot of image 13 right to image 15 left (dated "de Paris a ... 1622" on
image 15 right); clear and cipher are interspersed. Content (Luynes dead, 15 Dec 1621; the French ladies of Queen Isabel sent back
from Madrid; Anne of Austria's confessor; the capitulations of the Grisons treaties) points to the first weeks of 1622.

The scans (BNE Digital) were harvested in a real browser on 5 Nov 2026 for coloma1622 and are kept private; **no image is
reproduced in this repository or on the write-up.**

## System and key (`key.tsv`)

The coloma1622 system (Mirabel / Feria, 1622): syllabary on a grid, two-digit numbers for letters and syllables, three-digit and
underlined code words, faz / fez / fuz = que, marked signs distinct. `key.tsv` is CLE_M02 = coloma1622 key C04 + the values read on
the contemporary clears of this volume (two bound clear copies, one attached clear copy, margin clears), each row with its source.
Added from those clears: **ō = t** (the o with a cross of "trae", "contra", "ministros"; a sign distinct from the Ð = n of coloma1622,
and noted Ð by mistake in the coloma1622 H5 transcription), _0_ = REBELDE (C04: REVES), 308 = NUESTRO (308 34ʳ = nuestro señor).
**g is doubtful**: p by the clear copy v39 d, f by the clear copy v33 g ("ofrecido"); g does not occur in this letter. sa = al as already
integrated in coloma1622 (#417, #543).

## Tests (`validation.txt`)

| test | held-out passage | key | metric | score | best of 200 controls | result |
|---|---|---|---|---|---|---|
| H6 | image 38 right | - | - | - | - | burned before any computation (its clear copy had been seen) |
| M01 | part B, image 15 left, 192 tokens | CLE_M01 | lexical, runs alone | -2.381 (>= -2.35) | -2.880 (gap 0.499, >= 0.60) | failed |
| M02 | part A, images 13 r - 14 r, 349 tokens | CLE_M02 | lexical, whole text | -2.383 (>= -2.25) | -3.413 (gap 1.029, >= 0.30) | partial |

No unseen passage of this system is left in MSS/18428.

## Reading (`reading.md`, `translation.md`, `decryption.txt`)

Mirabel answers Gondomar on court gossip (Madame de ‹Jamuila›, not identified): the King visited a lady the very day he arrived,
very probably Luynes's widow, since her husband "was not yet well dead"; she complained that people spoke ill of her husband, and he
answered that she was to blame, cutting beauty patches and painting her face so soon. A passage on a young woman Mirabel commends to
Gondomar (or will send to the college of Valladolid) is partly unread. On the French ladies: Philip IV's letter orders him to tell Luynes that both crowns resolved to send the French ladies
home (from Madrid) and the Spaniards here (in Paris) to go; the news crossed Luynes's death. He has urged the Spanish servants of the
Queen not to lose their place by their own fault. The Queen wished a companion of her confessor to succeed him; Mirabel objected
(a Spaniard, the grievance if he were removed) and proposed that he be given the title of confessor in the interim. He vouches for
Louis XIII's good intentions and blames the ministers, and expects the capitulations of the Grisons treaties any hour.

Signs read by sense only (c̣ir, xix, f‡, fir, I after 202, 20~; and one-place values g‡, p‡, D‡, x‡, fizt, zan) are probable or
restored, never certain. Unresolved: codes 24, 322, _1_, _13_, _41_, md, 87, 48~, and a few signs.

## The other ciphered letters of the volume (`CONTEMPORARY-CLEARS.md`)

Six of the seven ciphered letters of MSS/18428 carry a contemporary decipherment (margins, interlinear, bound clear copies): they
are read by their contemporaries and only served as cribs for the key. CLE_M02 decodes their 39 aligned segments to 0.921 of the
clears' characters (learning data, not a test).

## Prior art

No modern decipherment found: not on DECODE, nothing at Cryptiana (Tomokiyo) or in Lasry's lists; catalogue 1271 open, no target,
PR or issue in this repository before issue #367 (inventory only). Not read: Herrero García, *Avisos* 100 (2023), on the
Marchioness of Mirabel's letters in this volume (full text behind an anti-bot page, not bypassed); *Correspondencia oficial de
don Diego Sarmiento de Acuña, conde de Gondomar* (Documentos inéditos para la historia de España, 1936-1945); Tobío Campos (cited by
the BNE record). Rodríguez Gómez (*Avisos*, Real Biblioteca) notes that in the Gondomar papers the clear is usually written between
the lines or in the margins, as in this volume.

## Gaps

- The key needs a test on another letter of the system with a contemporary clear (Gondomar papers in the Real Biblioteca, Coloma's
  papers): not done.
- Part B was transcribed in one pass only (5 Nov 2026); part A in two independent passes, arbitrated on the image.
- No palaeographer checked the letter; no human checked the reading.

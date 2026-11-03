# Bouillé to the minister, Martinique, 17 September 1778 (ANOM C8 A 77 f. 88, no. 238) - catalogue 1202, with the 1203 letters surveyed

Status: in progress (read in part: key for Bouillé's code recovered from interlinear decipherments of 1779 letters; f. 88 is a monthly troop return, 96.7% (175/181 tokens) after the f. 144 pairing of 3 Nov 2026 (earlier 91.7% of tokens valued after the 3 Nov 2026 merge of five interlinear letters, 85.6% inside dictionary words by a strict proxy; 14 groups still open; 3 Nov 2026)

Catalogue 1202 (this letter; f. 101 of 5 Dec 1778 surveyed, not transcribed) and 1203 (C8 A 78-81; surveyed, three interlinear letters partly paired).
Written in the checkout cyph-merge, not committed.

## Document

- ANOM COL C8 A 77 f. 88 (image FRANOM23_C8A_077_0141, FranceArchives component 1bd8971212209a5c804b009c94910f186d12a09f,
  ark:/61561/zn401ysswzzd), Bouillé (governor general of the Windward Islands) to the Navy minister, no. 238, "à la
  Martinique le 17 7bre 1778", "Dup.ta". One page: clear "J'ai l'honneur de vous envoier", 12 lines of numeric
  groups, "Je suis avec respect, Monseigneur, Votre très humble et très obéissant serviteur, Bouillé". No interlinear
  decipherment; calendar: "Lettre chiffrée non décryptée".
- **Transcribed digit by digit from the image** (`transcription.txt`, 640x360 crops): **181 groups, 109 distinct,
  values 1-845** (`_check_profile.py --measure`), full-stop separators; a "+" above 451 and an "x" after 37 (line 4) are
  marks, not digits. In the hand a 4 looks like "h", a 5 like "S".
- Same day, no. 237 (f. 87, image 0140): clear, asks the inspection of the Dominica hospitals for a physician at Saint-Pierre.

## What f. 88 is (from the extended key)

A monthly **return of the troops** ("état de la situation des troupes ... au 1er de ce mois"): with the key, line 1 reads
"l'ét[at] de la situation des troupes", line 2 "au 1er de ce mois ...", later "garnison" (268, three times), "la Martinique"
(267), "hommes", "cents", "hôpital" (ho pi ta + [103]), "la Guadeloupe", "troupes", "hommes ef-fe-c-ti-f-s" (effectifs).
The same monthly return exists in the volume: f. 101 (5 Dec 1778, no. 259) opens `208 250 837 361 57 147 1 250 287 361 694
381 303 361 267 636 104 361 270 309 815` = "[J'ai] l'honneur de vous envoyer l'état de la situation des troupes de la Martinique au 1er de ce mois",
and C8 A 78 f. 31 (8 March 1779, no. 281) is the same kind of return with interlinear decipherment.

## System

- Numeric nomenclator, groups 1-845 (the 1761 code C8 A 64 f. 1 stops at 696, the 1765 d'Ennery form at 800). Letters, syllables,
  and whole words, with articles inside place names (428 = la Guadeloupe, 267 = la Martinique). Homophones exist (s = 817/635,
  fe = 658/538?, es/ez = 185, se/sé = 305); numerals are spelled in syllables and letters (si-x, qua-tre, cent-s, vi-n-g-t).
  A semicolon and a comma are written in the cipher line.
- Tests of the sibling keys (`test_keys.py`): the **mercier1761 key does not fit** (28 groups exceed 696; 39 of 181 tokens valued, salad)
  and neither does the **1765 d'Ennery form** (17 groups exceed 800; nonsense). The Bouillé code is a third code.

## Key sources: interlinear decipherments in the same series

Survey of the letters on the catalogue list (first images viewed 28 Oct 2026; image numbers from the manifests):

| letter | images | what is there |
|---|---|---|
| C8 A 78 f. 123 (no. 363, 11 Oct 1779) | 0197 | **interlinear**, fully paired (104 groups, `pairs1779_f123.txt`) |
| C8 A 78 f. 31 (no. 281, 8 Mar 1779) | 0046-0047 | **interlinear** (troop return; heavy ink bleed-through); about 60 groups paired |
| C8 A 78 f. 3 (no. 173, 6 May 1779) | 0004-0006 | **interlinear**, clean hand; lines 1-2 paired |
| C8 A 78 f. 5 (no. 175, 8 Jun 1779) | 0007 | **interlinear** (opens "Nous avons l'honneur de vous envoyer les états de ..."); not transcribed |
| C8 A 78 f. 144 (no. 372, 23 Nov 1779) | 0233-0246 | **interlinear** on image 0233 (opens "de la compagnie de M. d'Est..."); not transcribed |
| C8 A 78 f. 1 (Grasse du Bar) | 0001-0003 | cipher only, no interlinear on 0001-0002; a note says the original was deciphered. (Image 0075, dated 24 mars 1779, is another long cipher letter, no interlinear) |
| C8 A 79 f. 19 (no. 23, 14 Nov 1780) | 0029-0030 | cipher only, opens "Nous avons l'honneur de vous adresser" `250 287 381 744 ...` (état des ...), no interlinear |
| C8 A 79 f. 70 (no. 415, 24 May 1780) | 0107 | cipher only, "J'ai l'honneur de vous envoyer" `250 287 163 586 361 ...` (état des garnisons) |
| C8 A 77 f. 101 (no. 259, 5 Dec 1778) | 0162-0164 | cipher only on 0162 (troop return, parallels f. 88); image 0163 is a **table** of cipher groups in two columns (enclosure) |
| C8 A 79 f. 4, f. 24; C8 A 81 f. 97, f. 104 | first images | clear letters (cipher, if any, later in the letter; not read) |
| C8 A 81 f. 114 (no. 12, 24 Nov 1782) | 0195-0203 | clear opening; cipher lines begin below on 0195; not read |

- `pairs1779_f123.txt` (all of f. 123: "J'ai reçu la lettre ... fortifications de la Guadeloupe ... la moitié des troupes ... à découvert") and
  `pairs1779_f3_f31.txt` (f. 3 lines 1-2: "nous avons l'honneur de vous rendre compte de l'état de la colonie dont la situation est des plus critiques"; f. 31:
  "l'état de la situation des troupes au 1er mars, par lequel vous jugerez que la garnison de la Martinique n'est composée que de quatre ... Des six cents
  quarante cinq hommes de recrue ... trois cent vingt cinq à l'hôpital ... ce qui provient de la marine ..."). Alignment is by label position and by sense (labels sit up-left of their group).
- `apply_key.py` merges them into **`key_bouille.tsv`: 123 groups with provenance per value** and prints conflicts:
  67 qua/vous, 185 es/ez, 305 se/sé/e, 503 è/par (f. 123 vs f. 31; probably a misalignment in one of them), 718 a/à.
  New values include 694 situation, 267 la Martinique, 636 au, 104 1er, 116 ma + 325 rs (mars), 78 ho + 508 pi + 417 ta (hôpital), 453 cents, 91 x, 709 si, 37 hommes,
  558 recrue, 268 garnison, 682 dont, 815 is, 250 l', 287 état, 837 honneur, 810 compte, 488 nous, 448 plus, 353 colonie.
- **Same code, shown statistically** (`shared_ngrams.py`, session 1): 10 shared adjacent pairs and 2 triples against 1.55 and 0.01 expected (p < 0.001). Session 2 adds the identical openings
  of f. 3/f. 31 (250 287 361 587 694 = l'état de la situation) and f. 101/f. 88.
- Access: curl gets 403 from the ANOM image server; the browser pane loads the IIP URL (the manifest gives the path). Drawing a crop of the loaded image into a canvas in an 800x450 viewport gives legible 1:1 or 0.8-scale crops.
  The canvas only has to be displayed, so images can be drawn from any origin. The pane is shared: use your own tab and pass its tabId.

## Reading of f. 88 with the extended key (`apply_key.py`, `measure_sense.py`)

- **Valued: 123 of 181 tokens (68.0%), 61 of 109 distinct groups. Strict sense proxy: 105 of 181 tokens (58.0%)** (`measure_sense.py`: valued stretches are cut at unvalued groups and must
  segment into fr-gutenberg words plus a declared list; it accepts any word-shaped string, so it overstates). Not the 95% read bar.
- Decoded lines (`[n]` = open): 1 "l' ét [5=at] de la situation des troupes"; 2 "au 1er de ce mo-is [191 5 398 339 110 817] aux d' [531] plus d'"; 5 "... dre [403 143 160] isle [494] es"; 6 "... met tre un garnison [481] de [845] r [195]";
  7 "r la Martinique [507] il né re s te en de [412] is [210] le s ho"; 8 "pi ta [103] x ét la garnison de [138] que [516] is [454] [516] is cents"; 9 "hommes ef [538=fe] c ti [614=f] s [88] vous en ver [509] [260] l' état de la";
  10 "situation de la garnison d' é Ce t te [739] [195] er [505] isle [286] est [645]"; 12 "la Guadeloupe [819] en troupes re [26] es ...". The text reads as a garrison return; the numbers of men are mostly open.
- **Tentative values** (`tentative.tsv`, applied only with `--tentative`, not in the key): 5 = at, 538 = fe, 614 = f ("hommes ef-fe-c-ti-f-s" = effectifs; f. 123 has 594 658 345 754 for the same syllables, so 538 may be a misread of 658 in f. 88: check the image). With them 128 of 181 (70.7%) are valued.
- Not claimed: "j'attends" for line 2 (191 = J', 5 = at, 398 = te, 339 = n, 110 = d, 817 = s fits the letters but not the context); "il ne reste en de..." on line 7; 103 = ux.

## Ciphertext-only attack: not run

The mercier1761 control (same shape, ~800 entries, 818 tokens: 5-9% correct, the truth outscored) shows the objective cannot separate the true text at this size; with 181 tokens it is worse. The interlinear
keys make it unnecessary.

## Pairing session 3 Nov 2026 (f.31 rest, f.3, f.5, f.144) and test of the LLM key-editor fills

- New pair files: `pairs1779_f3_f31_more.txt` (f.31 both images, f.3 images 0004-0006; ~365 distinct group=value pairs) and `pairs1779_f5_f144.txt`
  (f.5 image 0007, f.144 image 0233; arks f.5 `zn401yssvxxy`, f.144 `zn401qkkpmkw`). **Not yet merged into `key_bouille.tsv`** (`apply_key.py`
  reads only the earlier files); doubtful alignments carry '?'. Possible conflicts with the key to settle on merging: 25 meme (key: noms), 271 arme(s), 373 commerce, 345 it (key c; homophone?), 307 ba (key ou), 621 ne/dro.
- f.144 image 0233 opens "Vous aurez su tous les evenements malheureux de la campagne de M. d'Estaing", not "de la compagnie de M. d'Est..." as listed above.
- Fills proposed by the research/keyedit editors (`research/keyedit/README.md`, Tests 4-5) checked against these pairs: **103=u, 665=pa, 531=autant, 5=at, 491=an, 321=pas, 402=di confirmed**; 545=it (editors: trois/men), 195=ni, 272=i, 320=mi, 412=du, 443=y, 454=mille, 516=tro, 622=ces, 845=ga, 636=au, 705=re, 719=ver, 807=ne, 815=is refute their fills. 46 reads aux (f.31 twice) and avec? (f.144, f.31) - open. 667=im is consistent with "pa-ti-en-ce" (667 665 754 23 270 = impatience) but 667 occurs in no paired letter; 619, 495, 26, 260, 509, 138, 710 also do not occur anywhere paired.
- **Merged 3 Nov 2026** (`apply_key.py` now reads all four pair files): `key_bouille.tsv` 123 -> 346 groups; f.88 **166 of 181 tokens valued (91.7%), 95 of 109 distinct; strict sense proxy 155/181 = 85.6%** (was 123 = 68.0% / 58.0%). Conflicts listed by `apply_key.py` (46 aux/avec, 12 i/e, 25 meme/noms, 345 c/it, 307 ba/ou, 505 e/y ...) keep the more frequent value first; 46 and 12 still to settle on the images. Reading now: "l'état de la situation des troupes au 1er de ce mois ... j'attends ... d'autant plus d'... (667 pa ti en ce) ... [pou]vant mettre un garnison de ga-r-ni-[son] ... la garnison de [138] que trois mille trois cents hommes effectifs ... je vous en verrai l'état de la situation ... moitié par la Martinique et moitié par la Guadeloupe".
- Still open (14 groups): 26, 138, 146, 260, 481, 495, 509, 568, 619, 645, 667, 710, 809, 819; 619, 667, 495, 26, 260, 509, 138, 710 occur in no paired letter. The three-digit numbers (568 ...) are probably the troop counts.

## Remaining gaps

- 5 of 181 tokens of f. 88 carry no interlinear value (667 im, 495 minist, 568 i, 481 suffisante, 260 incessamment? by context in tentative.tsv); none of them occurs in a glossed letter (the glossed letters f. 3, f. 5, f. 31, f. 123, f. 144 are all paired) - blocker: no-key-material
- Cipher-only letter C8 A 78 f. 1 (Grasse, 'Chiffre de 1777', 560 groups transcribed): a different code, the Bouillé key does not read it - blocker: no-key-material; needs the 1777 code or the first copy's decipherment
- The minister's ciphered minutes (C8 A 77 ff. 31, 43) and MAR/G/178 (colonial Navy keys 1741-1776) - blocker: needs-physical-access (MAR/G/178); minutes not opened

## Escalation

- [x] siblings: f. 87 (clear), f. 112 and the C8 A 78-81 letters surveyed; interlinear decipherments on f. 123, f. 31, f. 3, f. 5, f. 144; f. 101 transcribed 3 Nov and read with the key (same return, header confirms 645 and 138)
- [x] clear-pages: f. 87 clear, unrelated; the clear letters of C8 A 79 f. 4, f. 24 and C8 A 81 are different dispatches
- [x] known-keys: mercier1761 key and 1765 d'Ennery form tested, both ruled out
- [x] print: 3 Nov 2026 two web searches (Bouillé letters to Sartine, état de situation, Dominique 1778): no printed decipherment; Boromé, RHAF 1970, cites Bouillé's 'Détail de la Conquête de la Dominique' (ANOM Dessins et Mémoires, Antilles étrangères, carton II n. 126, 8 Sep 1778) - not opened; CSP/Bain-type calendars do not apply
- [x] key-rebuild: key_bouille.tsv (346 values, provenance per value) from the interlinear letters; no annealing (control fails at this size); LM key editors tested in research/keyedit (about 40% of fills right)
- [x] retry: key re-applied after each pairing (f. 3, f. 31, f. 5, f. 144 paired 3 Nov): 166/181 tokens on interlinear values, 181/181 with context readings; 46 and 12 settled on the images

## Next steps

1. Pair f. 3 (images 0004-0006, clean hand), the rest of f. 31 (0046-0047), f. 5 (0007) and f. 144 (0233-): each adds 100-300 pairs of the same code; many open groups of f. 88 (numbers of men, "présents", "morts", regiment names) will appear.
2. Re-run `apply_key.py` and `measure_sense.py`; fill short gaps by context with `lang/` French models only with a crib, marked tentative.
3. Then read f. 101 and its table enclosure and the cipher-only letters (C8 A 78 f. 1; C8 A 79 f. 19, f. 70). The catalogue 1202/1203 entries should note that C8 A 78 f. 3, f. 5, f. 31, f. 123, f. 144 carry interlinear decipherments.

## Prior art

Catalogue sweep 28 Oct 2026: nothing published, not on DECODE. Not re-searched here.

## Open groups read from context, 3 Nov 2026 (tentative, not in key_bouille.tsv)

13 of the 14 open groups of f.88 got a context reading in `tentative.tsv` (667 im, 495 minist, 710 marine, 568 i, 809 per,
146 entre, 619 va, 481 suffisante, 509 ra, 260 i, 645 fo, 819 tant, 26 gl). None occurs in a paired letter, so none is
checked against an interlinear; each is a word-frame guess (impatience, ministre de la marine, vuide, permet,
entreprendre, pouvant, verrai, fournie, tant en troupes réglées tant en milices). With them f.88 reads 180/181 tokens.
Still open: 138 ("la garnison de [138] que trois mille trois cents hommes effectifs"; not la Martinique, 267).
46 aux/avec and 12 i/e not settled on the images. Test: f.101 or a later letter that repeats these groups.

## f. 101 transcribed, 3 Nov 2026 (`groups1778_f101.txt`, ark zn401dxx151o, image 0162)

Cipher only (no interlinear), 6 lines. Decoded with the key plus tentative.tsv: "[J'ai] l'honneur de vous envoyer l'état de
situation des troupes de la Martinique au 1er de ce mois et celui de la garnison de [138] les [577]-va-u-x pour la sûreté de
cette dernière colonie approchent de leur [678] et elle est dans ce moment en état de défense." Check on the context readings:
619 = va and 103 = u hold in "travaux" (577 = tra). 138 is a place with "cette dernière colonie" (newly taken): la Dominique
(taken 7 Sep 1778; f. 88 is dated 17 Sep). 678 = fin, 208 = j'ai from context. Image 0163 (table enclosure) not transcribed.

Image 0163 of f. 101 (enclosure, folio mark 138 at top left is a page number, not the group) opens with a three-line header in the
same code: "situation de la garnison de [138] au 1er de ce mois ... fo-u-r-ni-e par les garnisons de la Martinique et la
Guadeloupe" (694 361 587 268 361 138 636 104 361 270 135 661 / ... / 645 192 666 195 17 503 607 817 268 817 361 267 266 428).
That is the f. 88 sentence again: it confirms 645 = fo ("fournie") and that 138 is the newly taken colony, la Dominique, whose
garrison came from Martinique and Guadeloupe. Below the header is a two-column table (left: unit or place with dotted leaders; right: figures such
as 453 67 81 = cent quatre-[vingt]); rows partly decoded (331 23 265 815 = vi-en-no-is, Viennois; 267 257 = la Martinique [257];
428 = la Guadeloupe), not transcribed in full.

## 46 and 12 settled, 3 Nov 2026

Re-read on the f. 31 image (image 0046, line 7, 598 525 46 250 278): the blue gloss over 46 is "auec/avec" ("ri-ves avec l'escadre de M. ..."),
and "aux l'" is ungrammatical; f. 88 "avec d'autant plus d'impatience" fits. 46 = avec, the f. 31 pair lines corrected (f. 3/f. 31 and
f. 144 read avec). 12 = i (the single "e?" in f31-L12 was the doubtful one). Conflicts left: 25, 345, 307, 103 (see apply_key.py output).

## f. 101 table transcribed and decoded, 3 Nov 2026 (`table1778_f101.txt`)

Enclosure of 9 Dec 1778 (signed Bouillé): rows "Armement? .. | cent quatre[-vingt]", "au 1er [218]", "Viennois | deux cent quatre-vingt",
"la Martinique [257] | cent [279]-ante sept", "la Guadeloupe | cent quarante-cinq", "Volontaires? de [189]-ille ..", "milices de la
Guadeloupe | dix", brace rows with "la Martinique | vingt six", "la Guadeloupe | quatre-vingt-un", "deux cent vingt-deux", last "cent
soixante-douze". Number words give: 819 73 210 17 = qu-ar-ant-e (quarante) and 819 73 491 398 = qu-ar-an-te, so 819 = qu, 73 = ar.
That replaces the guess 819 = tant on f. 88 by "qu'en troupes réglées qu'en milices". 279 sits in "cent [279]-ant-e sept" (soixante or
quarante sept) and is "pri?" only once in the pairs (f31-L14, doubtful): the f. 88 reading "a an [279] ce" needs re-checking.

## f. 144 paired in full, 3 Nov 2026 (`pairs1779_f144_p2.txt` images 0234-0239, `pairs1779_f144_p3.txt` images 0240-0246)

Two agents read the blue glosses of the 13 further pages (275 lines). key_bouille.tsv went from 346 to 507 groups; f. 88:
175 of 181 tokens valued from interlinear pairs (96.7%, was 91.7%), strict proxy 92.8%. Tests of the context readings: 809 per,
146 entre, 619 va, 138 la Dominique, 645 fo, 577 tra hold. Corrections: 710 = guerre (not marine: 'le ministre de la guerre', so
495 = minist still stands), 509 = rai (not ra), 819 = soit ('soit en troupes réglées soit en milices', not qu/tant), 73 is not ar
(venir/xa), 279 = non ('an-non-ce', 'an-non-cent qu'il', and 'cent non-ante sept' in the f. 101 table; f. 31's 'pri?' dropped).
apply_key.py's label regex now takes labels with several hyphens. Remaining: see Remaining gaps.

## C8 A 79 f. 19 (no. 23, 14 Nov 1780) read with the key, 3 Nov 2026 (`cipher_f19_groups.txt`, ark zn401wqqtxsl, image 0029; `decode_any.py`)

Cipher-only letter, never glossed; 147 of 157 groups valued from the 507-value key (93.6%). It is a provisions return: "l'état des
subsistances existantes dans les magasins du roi et dans [ceux] du commerce au 1er de ce mois. Vous verrez qu'il est on ne peut plus
[a...]er, que nous recevions [...]ement de nouveaux approvisionnements, ce qui serait préjudiciable aux intérêts de sa [majesté], que nous
fussions forcés d'en faire dans la colonie. Les magasins du commerce sont un peu pourvus par le retour de deux bâtiments du convoi
et l'arrivée d'un neutre, mais la consommation est si considérable que notre situation à cet [égard] est toujours infiniment précaire."
Margin: "Martinique ... mois de novembre". Unvalued groups (context guess in brackets): 762 [tant], 58 [ceux], 390 [mo], 571, 603, 306,
485, 662, 20 [majesté], 584 [égard]. Image 0030 is another letter (no. 27), clear.

## C8 A 79 f. 70 (no. 415, 24 May 1780) read with the key, 3 Nov 2026 (`cipher_f70_groups.txt`, ark zn401yssxwtv, image 0107)

Cipher-only letter, 190 groups transcribed by an agent, 182 valued (95.8%): "[J'ai l'honneur de vous envoyer] l'état de la situation des troupes
[de] la Martinique, [de] la garnison de la Dominique et la Grenade au 1er de ce mois, et celui de la garnison d'e St-Vincent au 1er avril
dernier n'ayant pas encore reçu de M. du Montet son état au 1er mai. Je compte envoyer à la Grenade quatre à cinq cents hommes de plus ...
porter sa garnison de dix-sept à dix-huit cents hommes. La garnison de St-Vincent est suffisante à cause des [...] du [...] ... fournissent
... Caraïbes ... que j'ai fait armer. Il manque au régiment de la Martinique trois cent cinquante-neuf hommes pour le mettre au complet,
et il [est] bien intéressant de lui faire passer des recrues." Unvalued: 163, 586 (as 'état des'?), 257, 58, 260, 115, 177, 714. The
blue-pencil gloss above L13-L14 ('int er objet sa nt de lui faire passer des recrues') agrees with the reading. 'suffi-sa-nt-e' here
spells the word that f. 88 has as one unvalued group, 481 (suffisante).

## C8 A 78 f. 1 (Grasse, Martinique 4 Apr 1779) is a different code, 3 Nov 2026 (`cipher_f1_groups.txt`, images 0001-0003)

41 lines, 560 groups transcribed by an agent. Top left "Chiffre de 1777", dated 'à la Martinique le 4 avril 1779', signed
'Le Comte de Grasse'; a margin note says the first copy was deciphered. Applying the Bouillé key gives 60% of groups valued but the
result is not French sense ('emblable', 'pi pi', 'oc er'): a few words appear ('gouverneur', 'st-vincent', 'import', 'subsistance',
'farine', 'quintaux') only because the same numbers happen to be word groups in both codes. So f. 1 is not in the Bouillé code
(a '1777' code of the other writer) and the key cannot read it. Blocker: no-key-material (needs the 1777 code or the first copy's
decipherment).

## C8 A 81 f. 114-116 (no. 12, 24 Nov 1782) read with the key, 3 Nov 2026 (`cipher_f114_groups.txt`, images 0195-0203)

Cipher blocks on images 0195, 0196, 0198, 0199, 0202 (0197, 0200, 0201 are modern translation slips over the page; 0203 clear
closing), 1297 groups transcribed by an agent, 1244 valued (95.9%). The key reads it straight: "je suis préparé à tous les événements,
j'ai eu le temps de mettre toutes les colonies du roi en état de défense, elles sont parfaitement approvisionnées en munitions de
guerre et de bouche, n'ayant pas moins de six mois de vivres ... vous jugerez par l'état des garnisons que je vous envoie qu'à
l'exception de la Martinique où il ne reste plus que deux mille hommes de troupes réglées ... la Grenade seule aurait exigé deux ou
trois cents hommes de plus ... la Guadeloupe attaquée par dix mille hommes doit ... deux vaisseaux, deux frégates et une corvette
doivent être partis aujourd'hui de Saint-Pierre pour aller croiser au vent ... la Dominique ... St-Christophe ne peut être prise que par
famine ... Saint-Christophe et Saint-Eustache exigent une garnison de seize hommes ... si je ne suis point employé dans les opérations ...
ma présence devenant inutile ici." The groups 26 = gl ('troupes régl-ées', f. 88) is confirmed here ('re [26] es'), 481 = suffi-sa-nt-es is
spelled out (so 481 on f. 88 is a word group 'suffisante'), 296 = ? and 208 = ? recur as unvalued groups. Doubtful numbers
marked '?' in the file; page counts approximate.

## Conflicts settled with the new letters, 3 Nov 2026

25 = même ('quand [25] je ne réussirais pas', f. 114: 'quand même'; 'noms' dropped), 345 = c ('saint [345] hi s to p he', f. 114), 103 = u
('tra-va-u-x', 're-u-ni-r'), 307 = ba ('la [307] r ba de' = la Barbade; the 'ou' reading of f. 3 stays unexplained, possibly a second
group misread as 307). 538 is 'sept' in the f. 101 table (cent sept-ante deux, cent non-ante sept) but f. 88 'hommes ef [538] c ti f s' needs
'fe' where f. 123 has 658: the f. 88 image reads 538 clearly (checked 3 Nov), so 538 is either polyphonic or the copyist's slip; f. 88 keeps
538 = fe in tentative.tsv. 260 = 'incessamment' fits both f. 70 and f. 88 (context only).

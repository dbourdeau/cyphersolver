# Holes: what is not read, and why

Every hole is also marked in place in the readings (`[n]` = code with no value in key.tsv; `[?word]` = our guess, outside every count; `(xx)` = one-anchor row value; `!N` = spelling that does not read). This file lists them by kind. Nothing below was applied to any count.

## 1. Tokens with no value in key.tsv, per decryption

From the first two lines that `scripts/decode.py` writes at the head of each decryption (token totals by tier; unknown tokens with their number of occurrences). `~` = marked unsure by the reader. A token with a value in the gloss key of 30 Nov p2-3 (v1) may be unknown there and known in key.tsv (U4, HB, 61, 116, 165 and others: see units/petkum_1665-11-30_R2.units.tsv).

| decryption | tokens (by tier) | unknown tokens (occurrences) |
|---|---|---|
| `paulmyer_1664-04-25.txt` | 76 = tierA 60 + tierB 11 + tierC 0 + unknown 4 ; distinct 43 | [('285', 1), ('313', 1), ('MT?', 1), ('QX?', 1)] |
| `paulmyer_1664-05-02.txt` | 116 = tierA 102 + tierB 4 + tierC 0 + unknown 10 ; distinct 36 | [('133', 3), ('192', 2), ('73', 4), ('CT', 1)] |
| `paulmyer_1664-05-16.txt` | 145 = tierA 114 + tierB 15 + tierC 2 + unknown 13 ; distinct 56 | [('134', 1), ('313', 1), ('328', 1), ('348', 1), ('400', 2), ('70', 1), ('FF', 1), ('M', 1), ('PF', 1), ('Q', 2), ('S8', 1)] |
| `paulmyer_1664-06-19.txt` | 103 = tierA 77 + tierB 12 + tierC 0 + unknown 10 ; distinct 53 | [('130', 1), ('154', 1), ('192', 1), ('285', 1), ('309', 1), ('328', 1), ('329', 1), ('M', 2), ('S8', 1)] |
| `petkum_1665-03-24.txt` | 143 = tierA 115 + tierB 14 + tierC 1 + unknown 13 ; distinct 65 | [('180', 1), ('198', 1), ('278~', 1), ('310', 2), ('313', 2), ('348', 1), ('369', 1), ('394', 1), ('DB', 1), ('PF', 1), ('Q', 1)] |
| `petkum_1665-04-28.txt` | 70 = tierA 52 + tierB 12 + tierC 1 + unknown 3 ; distinct 42 | [('151', 2), ('376', 1)] |
| `petkum_1665-04-28_blind.txt` | 70 = tierA 51 + tierB 12 + tierC 1 + unknown 4 ; distinct 42 | [('151', 2), ('365~', 1), ('376', 1)] |
| `petkum_1665-06-23.txt` | 70 = tierA 54 + tierB 6 + tierC 1 + unknown 6 ; distinct 45 | [('134', 1), ('313', 1), ('348', 1), ('369', 1), ('373', 1), ('390', 1)] |
| `petkum_1665-06-23_blind.txt` | 70 = tierA 54 + tierB 6 + tierC 1 + unknown 6 ; distinct 45 | [('134', 1), ('313', 1), ('348', 1), ('369', 1), ('373', 1), ('390', 1)] |
| `petkum_1665-09-17.txt` | 59 = tierA 43 + tierB 7 + tierC 0 + unknown 3 ; distinct 37 | [('281', 1), ('309', 1), ('348', 1)] |
| `petkum_1665-09-17_blind.txt` | 59 = tierA 43 + tierB 6 + tierC 0 + unknown 4 ; distinct 38 | [('281', 1), ('309', 1), ('348', 1), ('Q~', 1)] |
| `petkum_1665-11-23.txt` | 229 = tierA 185 + tierB 25 + tierC 0 + unknown 11 ; distinct 90 | [('181', 1), ('197', 1), ('248', 1), ('313', 2), ('369', 1), ('374', 1), ('390', 2), ('DB~', 1), ('Q', 1)] |
| `petkum_1665-11-30_R2_blind.txt` | 726 = tierA 591 + tierB 74 + tierC 7 + unknown 31 ; distinct 126 | [('118', 1), ('134', 1), ('151', 3), ('163', 1), ('180', 1), ('197', 2), ('281', 2), ('310', 3), ('313', 4), ('338', 1), ('344', 1), ('351', 1), ('370', 1), ('373', 1), ('390', 1), ('399', 1), ('40', 2), ('DB', 1), ('Q', 3)] |
| `petkum_1665-11-30_p1-p4_R1_heldout.txt` | 168 = tierA 139 + tierB 14 + tierC 3 + unknown 8 ; distinct 68 | [('180', 1), ('281', 1), ('310', 2), ('313', 3), ('390', 1)] |
| `petkum_1665-11-30_p2-3_R1.txt` | 558 = tierA 452 + tierB 61 + tierC 4 + unknown 41 ; distinct 118 | [('116', 2), ('118', 1), ('134', 1), ('151', 3), ('153', 2), ('163', 1), ('165', 4), ('197', 2), ('209', 1), ('281', 1), ('310', 1), ('313', 1), ('338', 1), ('344', 1), ('350', 1), ('351', 1), ('370', 1), ('373', 1), ('399', 1), ('40', 2), ('61', 2), ('74', 1), ('88', 1), ('DB', 1), ('HB', 1), ('Q', 2), ('U4', 4)] |
| `petkum_1665-12-10.txt` | 198 = tierA 159 + tierB 19 + tierC 5 + unknown 9 ; distinct 76 | [('268~', 1), ('276~', 2), ('370', 1), ('373', 1), ('DB', 2), ('PF', 1), ('Q', 1)] |
| `petkum_1666-01-18.txt` | 128 = tierA 103 + tierB 18 + tierC 0 + unknown 6 ; distinct 64 | [('134', 1), ('307', 1), ('313', 1), ('338', 1), ('PF', 2)] |
| `petkum_1666-01-18_blind.txt` | 128 = tierA 99 + tierB 18 + tierC 0 + unknown 10 ; distinct 66 | [('134', 1), ('270~', 1), ('307', 1), ('313', 1), ('338', 1), ('380~', 1), ('G~', 1), ('PF', 2), ('Q', 1)] |
| `petkum_1666-04-06.txt` | 60 = tierA 44 + tierB 7 + tierC 2 + unknown 5 ; distinct 45 | [('235', 1), ('346', 2), ('373', 1), ('FF', 1)] |
| `petkum_1666-04-06_blind.txt` | 60 = tierA 45 + tierB 6 + tierC 2 + unknown 5 ; distinct 44 | [('171~', 1), ('235', 1), ('346', 2), ('373', 1)] |
| `petkum_1666-04-13.txt` | 206 = tierA 148 + tierB 30 + tierC 2 + unknown 18 ; distinct 84 | [('108', 1), ('135', 1), ('180', 1), ('248', 1), ('267~', 1), ('281', 1), ('309', 1), ('310', 2), ('321', 1), ('330', 1), ('346', 1), ('388', 1), ('40', 1), ('82', 1), ('DB', 1), ('DB~', 2)] |

## 2. Code numbers with no value (Petkum letters, KEY_v3)

35 code numbers occur with no value in key.tsv in the Petkum decryptions under KEY_v3 (all of them except the p2-3 R1 decode under key v1), listed by script from the table above: 40, 82, 108, 118, 134, 135, 151, 163, 180, 181, 197, 198, 235, 248, 281, 307, 309, 310, 313, 321, 330, 338, 344, 346, 348, 351, 369, 370, 373, 374, 376, 388, 390, 394, 399 (count: 10 + 10 + 10 + 5 = 35). Blocker: open codes; most are names, titles or frequent words that occur one to four times. Also unknown because marked unsure (~) by a reader, though the number has a value: 171~, 267~, 268~, 270~, 276~, 278~, 365~, 380~; and the signs DB, DB~, FF, G~, PF, Q, Q~.

Values our readers proposed from context and did NOT apply (copied from the readings): Q (plain q) = b; DB (crossed d) = g; PF = f; 310 = nous; 313 = on; 390 = vous; 369 = tant/tent; 370 = temps; 373 = traite; 180 = bon; 281 = maistre; 248 = homme; 181 = bruit; 348 = Roy; 256 = ju; 242 = he; 245 = hu. 348 = Roy is supported by a chancery gloss on a Paulmyer leaf (168R); it is still not in key.tsv and counts N in the Petkum letters. Applying any of these would raise the counts; we have not done it, because each would be a value taken from the letters it is then used to read.

## 3. Signs not in the key

- Petkum: Q (plain q, straight tail), DB (crossed d), PF (crossed p-like), FF (ff-like). One reader wrote FF where the blind reader wrote HSH (6 Apr 1666, 634R l.3); the image was adjudicated FF.
- Paulmyer's hand: plain m without tail (stands where h is needed: Chevalier, Chastelet, Otto, Thurin), a small 8-like sign S8 (stands where m is needed: amy, ambassadeur), plain q, FF, PF, the group 400. Not added to the key.
- A later key built from Paulmyer's glosses alone (our KEY_v4, 195 entries) was tried on six other bare Paulmyer passages: 51/95 = 53.68% strict. It was not adopted and nothing in this folder uses it.

## 4. Transcription doubts left as frozen

- 30 Nov 1665, R1: `220` for 270 twice ('pfos' for plus) and `382` for 381 ('avic' for avec); G for plain Q in 'o[b]liger' (572R l.8). The blind R2 reading was adjudicated on crops for these (270, 270, 381, Q) and the R2 count uses them; the R1 count of record does not.
- 30 Nov 1665, 573R l.9: an overwritten sign (HSH in R1, PSI in R2); not resolved on the image; the unit stays N.
- 30 Nov 1665, catchword 573R l.34 `x.MT` ('to-ls') in both transcriptions; left N.
- 17 Sep 1665: 'Bebgen' for Bergen: the first reader wrote 15 where the blind reader wrote BET; the image was adjudicated BET (r). The first reader's count keeps the frozen 15 (N).
- 17 Sep and 18 Jan: two tokens G (first reader) / Q (blind reader); adjudicated Q, which is not in the key.
- 25 Apr 1664 (Paulmyer): two doubtful signs (MT?, QX?), and 354 written where Savoye needs 352 (Si[v]oye); left N.
- 2 May 1664 (Paulmyer): the a-sign written 'CT' for 'ct' (unit 23) and plain m written MT in 'Chevalier' (unit 2): reader's faults found after decoding, left as frozen (N).

## 5. Text not transcribed

- The clear French around the cipher passages is quoted in the readings only where it gives the context; it was not transcribed in full.
- Further bare pages of the same file are not in this folder: see NOTES.md, What is not claimed.

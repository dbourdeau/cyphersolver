# Binasco to Philip II, Genoa, 25 June 1592 — AGS EST,LEG,1424,43 (PARES 3645975), the cipher of Pedro de Mendoza, conde de Binasco

Status: read in part (89.8% of words read as sense, sure + probable; key not validated at the programme's bar; the measured check of 14 Nov 2026 failed its criterion).

Sibling of catalogue 754 (Spanish embassy in Genoa, 1565-1603). The 1424,79 row removed earlier as "existing" is the
period decipherment of 1424,78 and serves here as key material only.

## Documents
* **1424,78** (PARES 3646215, duplicate of the letter of 24 Dec 1592, f. 158r-v) is in cipher; **1424,79** (PARES 3646230,
  "Descifrada") is its period decipherment. The pair is the main source of the key (`key_basis/`).
* **1424,1 / 1424,2** (PARES 3645100, 14 Jan 1592; a different hand) and **1424,77 / 1424,76** (PARES 3646209 / 3646201) are
  further cipher / period-decipherment pairs, used as held-out tests and then for learning.
* **1424,43** (PARES 3645975, 25 June 1592, "Carta parcialmente cifrada", same hand as 1424,78) is the target. Its PARES
  description has no "Descifrada en" link (checked 28 Oct 2026), and no decipherment or interlinear gloss is filed with it.
  Its three images were transcribed in one pass (18 + 23 + 7 lines, 729 units; `transcription/`).

## The cipher
A numeric syllabary in rows of five per consonant: b 10, c 15, d 20, f 25, g 30, y 35, h 40, l 45, j 50, m 55, n 60, p 65,
qu 70, r 75, t 80, v 85, s 90, x 95, z 100. Each row runs a e i o u forwards or u o i e a backwards (i always in the middle;
the c, d, g, n, qu, v, z rows run backwards). Marks: '.' = +n, ':' = +r, '^' = +s, a superscript hook = r after the onset,
a dot over 4 = al, a bar = numeral. Letter-signs: 4 = a, n/f = e, v = o, a = u, q = y/i, o = final d. The nomenclator is
written in letters: ge aqui, pal duque, pa carta, num hombre, xor para, Tas Rey, dum Florencia, vos Roma, pel Saboya,
T Señoría, and 21 more learnt on 1424,2/1 (`key_v2.json`).

## Prior art
No target, lead, PR or issue on Binasco or EST,LEG,1424 in this repository (checked 14 and 17 Nov 2026). The 1424,79
decipherment is the only period reading found. We know of no printed edition of 1424,43, but have not searched the printed calendars.

## Measurements (each preregistered and frozen by SHA-256 before the held-out text was opened)
| Test | Held-out portion | Key | Characters / words | Best of 200 controls | Bar | Verdict |
|---|---|---|---|---|---|---|
| C02, 28 Oct | 1424,2 vs period decipherment 1424,1 (202 words; other hand) | v1 | 0.661 / 0.540 | 0.493 / 0.248 | 0.85 / 0.75 | significant, **below the bar** |
| C03, 28 Oct | 1424,76 vs period decipherment 1424,77 (38 words) | v2 | 0.723 / 0.474 | 0.559 / 0.237 | 0.85 / 0.75 | significant, **below the bar** |
| C05, 14 Nov | marginal period decipherments of the struck-out lines of 1424,70 / 71 (166 units) | key proposal of 11 Nov | M1 0.479 / 0.333; M2 2 of 3 predicted codes exact (p = 0.003), window 2 of 3 | 0.391 / 0.167 | M1 0.85 / 0.75; M2 window >= 0.80 | **failed its criterion** |

C05 stated in its prereg that it was indicative only (fewer than 300 units, the most that survives intact in this hand). Its
pairing of each marginal note with one cipher block, fixed in advance, proved wrong for part of the blocks (the notes also
cover struck-out lines, and block 71a matches clear text in the body). M2 failed because the alignment gave Jem = "duque"
instead of "Gran Duque". A post hoc check on 105 units of 1424,70 reached 0.861 / 0.731. It was made after we had seen the
decoding, so it is not decisive. The C05 blocks are now used up and were not re-run.

Values attested in the period marginal decipherments of 1424,70, independently of the measurement: **hum = gente** (also
hum#), **mel^ = dineros**, **Jem = Gran Duque**, **49T = Su Santidad**; dum = Florencia confirmed; "sa" (before hum) open.

## Reading of 1424,43 (`reading/t43_reading_es.txt`, translation `reading/t43_reading_en.md`)
A Corsican privateer fitted out in a Genoese port (code Zim) is recruiting and carries a letter of recommendation for
Provence. Binasco raises it with the Doge and the Senate. Through his brother Francesco Grimaldi, the vice-legate of
Avignon reports that Montmorency is at Villeneuve, treating with the consuls of the neighbouring lands for money and men
against Lesdiguières and Savoy. He also reports on the Duke of Lorraine and his sons at Nancy, on the nobility leaning to
Béarn (Henry IV), and on the election and the Parlement of Paris. Finally, the Signoria resolves in council to fortify
Savona, and La Spezia.

Count by Daniel's rule (14 Nov 2026 recount, with hum, mel and Tas/tas from the period glosses): **403 words; sure +
probable 362 (89.8%); supplied 4 (90.8% with them); unread 37.** A mechanical re-count of the shipped file gives 359 of 399
tokens (90.0%), so the verdict is the same. Values proposed on 11 Nov 2026 for the remaining codes (an alphabetical-order
hypothesis for the letter nomenclator) would raise the nominal share to 99.5%. Of the 390 units on which that share rests,
65 depend on unattested values, so those values are **not** counted here.

## Remaining gaps
- codes Zim, Jas, dir, tur, ne, gim, rol, dis, Jee, qua(e) in 1424,43 - blocker: open-codes; no period decipherment attests them; Zim recurs five times (a place, perhaps "puerto").
- validation of the key on a fresh portion of 300+ units in the hand of 1424,78 - blocker: needs-physical-access; the only cipher-decipherment pairs online in legajo 1424 are used up or struck through; the original cipher of 1424,72 (deciphered in 72, the notice says) has not been found online, and the originals (not "Duplicado") of 1424,70/71/72/75 have to be located in AGS Estado 1424-1425 or the Secretaría.

Not part of this target, same hand and system: 1424,54 (17 July 1592; 6 sample lines read), 1425,58, 1426,38-42 and 1422,42
(downloaded, not transcribed). 1424,43 itself has one transcription pass only; a second blind pass is still to do.

## Escalation
- [x] siblings: PARES descriptions or images of 1424,1-2, 5-13, 54, 70-79 opened (28 Oct, 11 and 14 Nov 2026); every intact cipher / "Descifrada" pair found in this hand was used.
- [x] clear-pages: 1424,6, 7, 8, 9, 10, 11, 13, 74 are clear (copies, enclosures or decipherments of letters whose cipher is not in the run).
- [n/a] known-keys: no published key of Binasco's cipher is known; toledo1565 (two-digit homophonic, per catalogue 754) is a different system, so the key was rebuilt from the period decipherments instead.
- [n/a] print: no edition or calendar of Binasco's 1592 letters is known to us; the search went no further than this repository, the PARES notes and the 1424,79 decipherment.
- [x] key-rebuild: key learnt by alignment on three period pairs; nomenclator order hypothesis tested on 351 period code pairs (0 discordances against a minimum of 85 in 20,000 shuffles), values not adopted without attestation.
- [x] retry: 1424,43 recounted with the four period-attested codes (14 Nov 2026); the other codes stay unread.

## Files
* `transcription/t43_p1_cipher.txt`, `t43_p2_cipher.txt`, `t43_p3_cipher.txt`: cipher of 1424,43, one pass.
* `key_v2.json`: key as frozen on 28 Oct 2026, with the values attested in 1424,70 listed apart.
* `key_basis/t78_cipher.txt`, `key_basis/t79_clear.txt`: the training pair.
* `reading/`: reading by Daniel's rule and English translation.

Images: AGS via PARES, not included (study use only).

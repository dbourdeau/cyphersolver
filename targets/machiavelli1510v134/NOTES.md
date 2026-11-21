# Dieci di Balìa → Machiavelli at the French court, cipher letters of August 1510 (catalogue 2911 V/134, 2910 V/125)
Status: V/134 read in part (single pass, decoded in part); V/125 not decoded. Period key identified; its pre-registered
test FAILED the 0.85 threshold (0.660 against a best control of 0.303), so the key is reported as partial.

Contributed by Brice Dudout (Europe chiffrée, https://bdudout.github.io/europe-chiffree/), with Claude Opus 5.5 agents.
Images: Biblioteca Nazionale Centrale di Firenze (BNCF), Teca digitale. **No image or derivative is included here**
(BNCF condition: links only). Teca folders: V/134-136 `idr=BNCF0003856980`, V/124-133 `idr=BNCF0003856930`,
key VI/82 via Internet Culturale (oai ...AutografiPalatini:Machiavelli_VI_82).

## 1. Machiavelli's own decipherments do not cover these two letters
I/80 cc. 1-2 ("Decifrato", opening "El papa dopo assai dibactito con cotesta maestà") is about 3,500 letters of clear text;
V/134 has about 650 cipher signs and V/125 about 1,300. Contents differ (I/80: the pope, the cardinal of Auch, Genoa, Marcantonio;
V/134: Giovanni Girolami's arrival, the Venetian galleys). I/80 c. 3r is a letter "de ij di"; I/81 is the decipherment of the
28 July letter (V/150, per the BNCF record). No clear/cipher pair from I/80-I/81.

## 2. The key: BNCF Carte Machiavelli VI/82 c. 2r
Headed "Roma & Francia da scrivere"; endorsed on c. 2v "Cifera a li Oratori di Francia et Roma ... con Francesco Gualterotti et
Luigi della Stufa". Alphabet with homophones (rows 2-4), nulls, syllables ba ... tu, sul/sal/sel, doubles bb ... tt, dictions
(che, come, quando, sempre, et, non, bene, perché, anchora, nostro, nondimeno ...). Transcribed as `key/KEY.tsv`
(label -> plain; labels whose shapes coincide on the sheet are given as a|b, the first value being the decode), frozen
(`key/KEY.sha256`). Learning only on V/124 copy 2 (c. 236r) lines 3-4 against Opere VI (1877) pp. 76-77
(`protocol/learn_124b.txt`): "a Milano sopra a una richiesta fattaci", "mandare le gente nostre in Lombardia la quale".
The modern slip on VI/82 c. 1r is a partial 19th-century transcription of the same table.

## 3. Pre-registered test (one measure) — partial, threshold not met
`protocol/PREREG.md` (SHA-256 in `PREREG.sha256`, frozen before any decoding of the held-out portion).
Held-out: V/131 (c. 248r, "Copia della di Ruberto Acciaiuoli", Dieci to Roberto Acciaiuoli), lines 1-7, 333 signs, two blind
passes (`transcription/T1_V131.txt`, `T2_V131.txt`; final `T_V131_final.txt`, frozen in `protocol/TRANSCRIPTION.sha256`
before the reference was read; the arbitration comment in that file is in French, kept verbatim for the hash).
Reference: printed text, Passerini-Milanesi, *Le opere di Niccolò Machiavelli* VI (1877) p. 89, archive.org OCR
(`leoperediniccol03milagoog`; the right edge of several lines is lost in the OCR), `protocol/ref_V131_opere6_ocr.txt`.
Result (`protocol/MESURE_V131.txt`, re-run with `protocol/rerun.sh`): **score 0.660; best of 200 permuted-key controls
0.303; margin 0.356 -> PARTIAL; the 0.85 threshold is not met.** The decode carries the printed sense ("in corte al
Machiavello et a Milano al Pandolfino ... et sempre ... in Lombardia ... replicheremo ... dal Machiavello ... facilmente"),
so the system is right; the loss is in the transcription.

Limits: Teca images are about 900 px wide; the two blind passes agree on only 0.64 of the signs; several glyph pairs of the
table (su/ta bb/66, la/ri theta, ga/pa, to/s, so vs a+a) cannot be told apart at that size. Higher-resolution reproductions
of V/134, V/125, V/124 and V/131 have been asked for; with them, a second measure on a fresh portion (V/124 copy 1, V/127 or
V/129, all printed) would settle the key.

## 4. V/134 (catalogue 2911), 17 Aug 1510 — read in part
`reading/V134_reading_in_part.md` (single pass, decoded in part): Giovanni Girolami's arrival (in cipher), the Venetian galleys,
"in porto et da Genova", "l'armata", "da Roma ... intendiamo che", lances, Marcantonio [Colonna], troops. Far below 95 %.

## 5. V/125 (catalogue 2910), "Summario di l(ette)ra de 18 di", 22 Aug 1510 — not decoded
Hypothesis only: V/125 is enclosed with V/124 of 22 Aug, which opens "Scrivemoti a di xviij per via di Milano"; it may be a
ciphered summary of the Dieci letter of 18 Aug 1510 printed in Opere VI pp. 72-74. Not tested.

## Prior work checked (17 Nov 2026)
PRs and issues of this repository (2910, 2911, Machiavelli; issue #590 is lead 1549, Luppi); targets/ and research/
(wave 17 sweep notes); Opere VI (1877) searched for 17 Aug and the summary of the 18th (not printed); Tommasini II.2 p. 1356
only lists them. Not checked: Bertelli, *Legazioni e commissarie* (1964), the Edizione Nazionale *Legazioni*, ASF Dieci di
Balìa missive registers.

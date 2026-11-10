# taulet1866: copybook of colonel Bernardo Taulet, Jalet (Falset), Jan-Mar 1866 (catalogue 2444)

Status: read in part (Brice Dudout, 10 Nov 2026; all 76 cipher words read by sense, 71 certain and 5 probable, 0 restored, 0 unresolved; the key is partial by our own protocol: held-out 0.981 against the best of 200 shuffled keys 0.704, margin 0.277, under our 0.30 rule, criterion not met).

Contributed by Brice Dudout (Europe chiffrée), with Claude Opus 5.5 agents. Catalogue entry 2444 (Daniel Bourdeau's
PARES sweep of AHN Diversos-Colecciones, vetted 9 Nov 2026). A short pointer was sent in issue #367 (9 Nov 2026); this is
the full write-up. No DECODE record, no edition found.

## Document

Archivo Histórico Nacional, Madrid, DIVERSOS-COLECCIONES, 193, N.99 (PARES 5928106), 54 images: orders received from the
military government of Tarragona (views 2-13, 44-50), the copybook of the daily reports nos. 1-67 of lieutenant colonel
Bernardo Taulet, commanding the Jalet (Falset) canton and the Priorato columns during the January 1866 rising (views 14-45,
14 Jan - 2 Mar 1866), and a cipher telegram received from Reus on 7 Mar 1866 (views 51-53). In report 13 (24 Jan, view 21)
Taulet cannot read a dispatch "por carecer de la clave para descifrar" and asks for the key; numbers appear in his reports
from report 18 (27 Jan). No decipherment, interlinear or marginal, on any leaf. **No image, crop or thumbnail is included
here**: text and key only.

## System and key (`key.tsv`)

- Homophonic substitution of **letters** by 2-digit numbers (10-92), no word divider, set inside clear Spanish (small
  words often left in clear). 36 numbers: a 21 62 | b 14 | c 81 82 87 | d 61 | e 11 33 84 | f 25 | g 19 60 | h 70 |
  i 41 92 | j 56 | l 13 18 | ll 16 | m 38 | n 29 | ñ 15 | o 36 64 | p 72 | r 27 77 | s 10 50 80 | t 88 | u 32 55 | v 20.
- 33 cipher runs, about 312 numbers: S01-S30 in reports 18-55 (views 25-42), S31-S33 in the telegram (views 52-53).
- The short run at the end of each report, just before "Dios guarde", is the **day of the week**, matching the 1866
  calendar in all 16 cases: a check word.
- Key status: **partial** (see Validation). Licence CC BY 4.0.

## Validation (`validation.txt`, `frozen/`)

Pre-registered protocol P01 (in French, hashed): held-out set H = S33, the end of the telegram (51 numbers), transcribed
last and mechanically; transcription and key K_T (built on S01-S32 only) frozen by SHA-256 before H was decoded; one
measurement. **Result: car 0.981, best of 200 shuffled-key controls 0.704, margin 0.277. Our rule needs car >= 0.85 and a
margin >= 0.30: criterion not met, key partial.** The controls permute a vowel-rich homophonic key against a lexicon of
short words, so chance coverage is high (0.70), and H is short. H is burned and the unit holds no other unseen cipher, so
no further test is possible here. Declared leak: some values of T were read by eye before the transcription was frozen
(T only). The held-out run reads as clean Spanish ("a Cambrils con su primer batallón dé cuenta de haberse alojado"), and
a clear telegram of the same day (view 51) gives a neighbouring order (march to Vilaseca, "donde quedará alojado"); both
are consistent but not a validation. No new measurement was made for this pull request.

## Reading (`reading.md`, `translation.md`)

76 cipher words: **71 certain, 5 probable, 0 restored, 0 unresolved**. Read share 71/76 = 0.934 with certain words only,
76/76 with the probable ones. The five probable words each need one number corrected by sense: entendi{d}os (81 for 61),
n{o} (15 for o), sába{d}o ("sabaos"), domi{n}go (doubtful 21|29), mar{c}he (21 for c). We keep "read in part" because the
key failed our own rule, not because words are open. `reading_review` B.

Content:
- Report 21 (about 30 Jan 1866): "ahora que son las ocho de la noche se me presenta el cuñado de Saguete con el pliego de
  V.E. fecha de ayer; hemos quedando entendidos y espero su aviso para acudir al sitio que me diga" - Taulet is in contact
  with the brother-in-law of the rebel Saguete (Sagueta) and waits to be told where to go.
- Report 22 (31 Jan 1866): "los más afirman que Sagueta no está en el país, creyendo muchos de ellos (que) marchó a Madrid o
  Barcelona con objeto de obtener el indulto".
- Telegram (Reus, 7 Mar 1866): "Traslade V.S. al coronel Taulet por parejas de Guardia Civil lo siguiente: mañana nueve
  marche V.S. a Cambrils con su primer batallón, dé cuenta de haberse alojado."
- "Saguete/Sagueta", a rebel of the January 1866 rising in the Priorato, is not identified here (local histories not searched).

## Remaining gaps

- The key is not validated (margin 0.277 < 0.30) - blocker: too-short; the held-out run has 51 numbers and no other unseen cipher remains in this unit; other copybooks or telegrams of the same 1866 command (if any survive in AHN Diversos-Colecciones) would allow a fresh test.

## Escalation

- [n/a] siblings: no other cipher unit of Taulet found in the PARES sweep.
- [x] clear-pages: the clear telegram of view 51 (same day) was compared after the measurement; neighbouring order, not a pair.
- [x] known-keys: none in the repository or on DECODE (catalogue vetting, 9 Nov 2026).
- [n/a] print: no edition found.
- [x] key-rebuild: key rebuilt from sense on S01-S32 and tested once on S33.
- [n/a] retry: H is burned; a retest needs new cipher under the same key.

Prior work checked 9 Nov 2026: "Taulet" and "5928106" occur only in catalogue.json and in sweep/vetting files of the
repository; no target, nothing in known.py; two web searches found nothing on Taulet or a published Spanish military
cipher table of 1866.

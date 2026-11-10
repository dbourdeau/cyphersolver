# taulet1866: copybook of colonel Bernardo Taulet, Jalet (Falset), Jan-Mar 1866 (catalogue 2444)

Status: read (classed at integration, 10 Nov 2026, by the read bar: all 144 cipher words read as sense, N.99 76 words, 71 certain and 5 probable; N.94 68 words, 54 certain and 14 probable; 0 restored, 0 unresolved; no gap open in the text). Key: partial, recorded apart: by the contributor's own protocol the key failed twice (held-out S33 0.981 against the best of 200 shuffled keys 0.704, margin 0.277; re-test on new material N.94 0.960 against 0.699, margin 0.261; both under the 0.30 rule). Brice Dudout submitted it as "read in part" because of the key; the project's read bar judges the text, and records the key state separately.

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
  words often left in clear). 35 numbers (36 in the submission; key.tsv holds 35, counted at integration 10 Nov 2026): a 21 62 | b 14 | c 81 82 87 | d 61 | e 11 33 84 | f 25 | g 19 60 | h 70 |
  i 41 92 | j 56 | l 13 18 | ll 16 | m 38 | n 29 | ñ 15 | o 36 64 | p 72 | r 27 77 | s 10 50 80 | t 88 | u 32 55 | v 20.
- 33 cipher runs, 370 numbers (counted at integration, 10 Nov 2026, from transcription.txt; the submission said about 312): S01-S30 in reports 18-55 (views 25-42), S31-S33 in the telegram (views 52-53).
- The short run at the end of each report, just before "Dios guarde", is the **day of the week**, matching the 1866
  calendar in 15 of 16 cases: a check word (S01, report 18 of Saturday 27 Jan, reads domingo, one day ahead; integration check 10 Nov 2026).
- Key status: **partial** (see Validation). Licence CC BY 4.0.
- `key_derived_n94.tsv`: two values seen only in N.94, 12 = y and 78 = u, **derived after the measure, not tested**;
  kept apart, key.tsv is unchanged.

## Validation (`validation.txt`, `frozen/`)

Pre-registered protocol P01 (in French, hashed): held-out set H = S33, the end of the telegram (51 numbers), transcribed
last and mechanically; transcription and key K_T (built on S01-S32 only) frozen by SHA-256 before H was decoded; one
measurement. **Result: car 0.981, best of 200 shuffled-key controls 0.704, margin 0.277. Our rule needs car >= 0.85 and a
margin >= 0.30: criterion not met, key partial.** The controls permute a vowel-rich homophonic key against a lexicon of
short words, so chance coverage is high (0.70), and H is short. H is burned and the unit holds no other unseen cipher, so
no further test is possible here. Declared leak: some values of T were read by eye before the transcription was frozen
(T only). The held-out run reads as clean Spanish ("a Cambrils con su primer batallón dé cuenta de haberse alojado"), and
a clear telegram of the same day (view 51) gives a neighbouring order (march to Vilaseca, "donde quedará alojado"); both
are consistent but not a validation. No new measurement was made on N.99 for this pull request.

**Re-test on new material (`retest/`, 10 Nov 2026).** AHN DIVERSOS-COLECCIONES, 193, N.94 (PARES 5855640), letters
received by Taulet in January 1866, never seen while the key was built. Pre-registered and hashed before transcription:
key and script unchanged, H = all runs of views 43, 87, 78, plus view 26 because the three gave 292 numbers (< 300);
H = 325 numbers in 17 runs; one measurement. **Result: car 0.960, best of 200 controls 0.699, margin 0.261 (< 0.30):
criterion not met again, the key stays partial.** Numbers 12 and 78 are not in the key and were scored as uncovered.
Declared deviations (clear words of views 43 and 87 seen after the key was frozen; two doubtful transcription calls) are
in validation.txt. H is burnt.

A fact about the measure, not an excuse: the shuffled-key controls sit near 0.70 whatever the length (0.704 on 51
numbers, 0.699 on 325). A permuted vowel-rich homophonic key segmented into short Spanish words covers about 70% of the
letters by chance, so the 0.30 margin is structurally near unreachable for this system with this measure, even at
car = 1.0. The rule was set before testing; we report it as written.

## Reading of N.99 (`reading.md`, `translation.md`)

76 cipher words: **71 certain, 5 probable, 0 restored, 0 unresolved**. Read share 71/76 = 0.934 with certain words only,
76/76 with the probable ones. The five probable words each need one number corrected by sense: entendi{d}os (81 for 61),
n{o} (15 for o), sába{d}o ("sabaos"), domi{n}go (doubtful 21|29), mar{c}he (21 for c). The contributor kept "read in part" because the
key failed his own rule, not because words are open; at integration the extent was set to "read" by the read bar, key partial. `reading_review` B.

Content:
- Report 21 (about 30 Jan 1866): "ahora que son las ocho de la noche se me presenta el cuñado de Saguete con el pliego de
  V.E. fecha de ayer; hemos quedando entendidos y espero su aviso para acudir al sitio que me diga" - Taulet is in contact
  with the brother-in-law of the rebel Saguete (Sagueta) and waits to be told where to go.
- Report 22 (31 Jan 1866): "los más afirman que Sagueta no está en el país, creyendo muchos de ellos (que) marchó a Madrid o
  Barcelona con objeto de obtener el indulto".
- Telegram (Reus, 7 Mar 1866): "Traslade V.S. al coronel Taulet por parejas de Guardia Civil lo siguiente: mañana nueve
  marche V.S. a Cambrils con su primer batallón, dé cuenta de haberse alojado."
- "Saguete/Sagueta", a rebel of the January 1866 rising in the Priorato, is not identified here (local histories not searched).

## Reading of N.94 (`transcription_n94.txt`, `decryption_n94.txt`, `reading_n94.md`, `translation_n94.md`)

68 cipher words: **54 certain, 14 probable, 0 restored, 0 unresolved** (54/68 = 0.794 certain only, 68/68 with the
probable ones). Probable = a number corrected by sense, or one of the two numbers absent from the frozen key (12 = y,
5 times; 78 = u, once) read by sense. `reading_review` B.

Content:
- Letter from Albarca, 28 Jan 1866 (view 43): "enterado y se cumplimentará su superior orden, quedando en dar a V.S.
  conocimiento del inmediato resultado. Es cuanto debo decir a V.S. en contestación a su oficio de este día recibido a
  las 9 de la noche."
- Telegram of the Minister of War, forwarded by the Captain General (view 87): "no se haga ninguna concesión a Escoda y
  que se juzgue con arreglo a las leyes si fuera aprendido. Los prisioneros serán igualmente juzgados. Procure V.E. ...
  que a toda costa sean aprendidos no solo Escoda y Sagueta sino los demás dispersos."
- Acknowledgement (view 78): "recibido el veinte y ocho se cumplimentará".
- Troop figures (view 26): "doscientos cuarenta y dos, incluzos los Tambores; solo podrá componerse cada una de estas
  tres columnas de ochenta y uno" (3 x 81 = 243: consistent).
- Combined, both documents: 144 cipher words, 125 certain, 19 probable (125/144 = 0.868 certain only).

## Remaining gaps

- The key is not validated (margins 0.277 on S33 and 0.261 on N.94, both < 0.30) - blocker: too-short; no unseen cipher under the same key is left (both held-out portions are burnt), and length alone does not lift the margin because the shuffled-key controls stay near 0.70; a further test needs fresh cipher of the same command (N.95, other 1866 units of AHN Diversos-Colecciones, if any) and a pre-registered null other than lexicon coverage (for example a letter model).
- The two values 12 = y and 78 = u (key_derived_n94.tsv) are untested - blocker: too-short; they were derived from the measured portion itself, and no fresh cipher under the same key is in hand to test them.

## Escalation

- [x] siblings: N.94 (PARES 5855640, letters received by Taulet, Jan 1866) uses the same key; used for the re-test.
- [x] clear-pages: the clear telegram of view 51 (same day) was compared after the measurement; neighbouring order, not a pair.
- [x] known-keys: none in the repository or on DECODE (catalogue vetting, 9 Nov 2026).
- [n/a] print: no edition found.
- [x] key-rebuild: key rebuilt from sense on S01-S32 and tested once on S33.
- [x] retry: one re-test on new cipher under the same key (N.94, 10 Nov 2026): margin 0.261, still partial; that portion is burnt too.

## Integration check (10 Nov 2026, pull request #376)

- SHA-256 sums of `frozen/` and `retest/` verified (all files except the lexicon path, which is outside the folder).
- Both held-out measurements re-run with `frozen/measure.py` and `lang/lexicons/es.json.gz`: 0.981 / 0.704 / 0.277 and
  0.960 / 0.699 / 0.261, identical to the two MESURE.txt files.
- `decryption.txt` reproduced exactly by `frozen/decode_T.py` with `key.tsv`; `key.tsv` has the same values as `frozen/KEY.tsv`.
- Not done here: the PARES images were not reachable from the integrating session, so the transcription was not
  re-checked against the images, and the other views of N.94 were not surveyed for further cipher.

Prior work checked 9 Nov 2026: "Taulet" and "5928106" occur only in catalogue.json and in sweep/vetting files of the
repository; no target, nothing in known.py; two web searches found nothing on Taulet or a published Spanish military
cipher table of 1866.

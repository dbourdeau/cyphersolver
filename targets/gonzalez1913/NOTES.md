# gonzalez1913: the General en Jefe (identified by the contributor as Pablo González) to Col. Andrés Saucedo, Matamoros, December 1913 (catalogue 1465), simple substitution

WAINUT, 12-13 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the work blind from the scans (below).

Status: read, 12 Nov 2026. The sixteen coded runs of this typed sheet are read with a simple substitution recovered
from the sheet's ciphertext alone. No key or decipherment was found. The split-half test of the key is weak (below);
the evidence for the key is the reading itself, and the repository's statistical validation (`docs/_validate.py`) passes.

## Document

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo LXVIII-1, LXVIII-1.7.890.1,
1 scan page. Typed on the letterhead "Ejército Constitucionalista, División del Noreste, Cuartel General", dated
"H. Matamoros, Diciembre 2[?] de 1913" (the day figure after 2 is faint), addressed "Sr. Coronel Andrés Saucedo,
Sabinas Hidalgo", and signed "El General en Jefe" with no name. The writer is identified by the contributor as Pablo
González: the item is in his papers, it is on the letterhead of the División del Noreste's headquarters, and Murguía's
letter of March 1914 in the same fondo (LXVIII-1.14.1943.1, `targets/murguia1914/`) is addressed to "Pablo González"
as "Gral. en Jefe de la División del Noreste". Clear Spanish with 16 coded runs in two-figure groups.

Images (CEHM public viewer, no account):
https://www.cehm.org.mx/Buscador/VisorArchivoDigital?jzd=/janium/JZD/LXVIII-1/7/890/1/LXVIII-1.7.890.1.jzd
(direct JPG: `http://visor.cehm.org.mx/assets/docx/fondos/jzd/LXVIII-1/7/890/1/LXVIII-1.7.890.1.0001.jpg`).
Fetched on 12 Nov 2026. No licence is stated, so the scan is not in this folder.

## Transcription

`SIGN_CONVENTIONS.md` first (written for the Clave Extra 3 sheets of the same fondo; the same shape conventions are
used here for a typed sheet). Pass 1 from 0.85x crops, pass 2 from fresh crops enlarged 1.1x with contrast stretch,
both without a key. The passes give the same group at 289 of 290 places; the one figure open in pass 1 (M09 g18, 4?)
reads 42 on the pass-2 crop. 290 group occurrences, 23 distinct groups, 16 runs.

## System

Simple substitution, one two-figure number per letter, 23 numbers used, all between 41 and 79: 41 i, 42 h, 43 g,
45 e, 46 d, 47 a, 48 b, 49 c, 52 n, 54 o, 55 l, 56 p, 57 ll, 58 q, 59 m, 71 z, 72 u, 73 y, 74 r, 76 t, 77 v, 78 s,
79 x. The numbers run in partly alphabetical order (a b c = 47 48 49; i h g = 41 42 43). Not Clave Extra 3: the
Clave Extra 3 key gives no Spanish on these runs (tested with `targets/murguia1914/key_frozen.tsv`). `key.tsv` and `key_frozen.tsv` are the same file, 23 entries (one
line each, after a header line).

## Key recovery

`scripts/hillclimb.py <repo> transcription_LXVIII-1.7.890.1.txt` fits a one-to-one substitution by hill-climbing on
Spanish letter trigrams taken from the repository's lexicon (`lang/lexicons/es.json.gz`), with 40 random restarts
(seed 7). Its best fit reads at once (`work/fit_7890_full.txt`). Three cells were then set by reading: 57 ll in Villaldama
(the fit gave j), 77 v (the fit gave f) and 79 x in próximo (the fit gave v). 42 h comes from the fit and stands in
one place, Sánchez. Groups 42, 43, 57, 58 and 79 each occur once in the sheet.

**Split-half test, weak.** Fitted on M01-M08 alone, the same program does not find the key (`work/heldout_7890.txt`).
Fitted on M01-M12 alone, it agrees with the final key in 10 of the 22 cells it fits, and M13-M16 read only in part
("tardeeilabadoodosunzo" for TARDE EL SÁBADO O DOMINGO; `work/heldout_7890_b.txt`). So the key is not validated by a
held-out passage. The evidence for it is the reading: it gives places of Nuevo León and Tamaulipas (Cerralvo,
Lampazos, Villaldama, Laredo, San Ygnacio) and the surnames Castro, Dávila Sánchez and Santoscoy, which the trigram
model does not know. The key has 23 values, fitted on 290 cipher groups.

## Reading

`reading_LXVIII-1.7.890.1.md` (Spanish, coded text in capitals) and `translation_LXVIII-1.7.890.1.md`. The writer
acknowledges Saucedo's message of the day before; someone (the coded run is not read) has left to join his forces at
Cerralvo. Saucedo is to finish operations at Lampazos and Villaldama, or else cut off the enemy at Lampazos and
advance north destroying the lines of communication, and be near Laredo by next Friday. Castro, Dávila Sánchez and
Santoscoy have orders to take up position near Laredo the same day; the place is to be attacked on Saturday or Sunday
at the latest. The writer leaves for San Ygnacio the day after tomorrow and will send instructions for the attack
from there. That these are the preparations for the Constitutionalist attack on Nuevo Laredo is our inference;
the sheet names only "Laredo" and gives no date for the attack.

Coded words (`scripts/count_words.py`): 61 in 16 runs; 59 verbatim from the signs (96.7%), 1 with a marked changed
value (l{o/a}s), 1 open: the first three groups of M01 (45-55-52, "eln") make no word before A REUNIRSE and are
marked `{eln/[?]}`. The clear word after M05 ("avanzar") is typed over on the sheet.

## Checks

- `python scripts/check_marks.py transcription_LXVIII-1.7.890.1.txt reading_LXVIII-1.7.890.1.md`: 16 runs, 2 marks, 0
  failures, PASS.
- `python scripts/decrypt.py transcription_LXVIII-1.7.890.1.txt decryption_LXVIII-1.7.890.1.txt key_frozen.tsv`
  reproduces the decryption file.
- `python docs/_check_reading.py gonzalez1913`: see the pull request text. The checker's period word list does not
  know the place names and some abbreviations; on the coded runs alone the clean share was 0.857.
- `python docs/_validate.py gonzalez1913 --write` on `validation.tsv` (one line per group with the frozen key's value;
  `scripts/validation_pairs.py`; marked repairs not applied, unread groups left out): 290 read tokens, 23
  types, model es-modern: reading -2.216 per letter; 200 random keys mean -7.613, max -5.222 (z 7.4);
  a key annealed onto shuffled ciphertext at best -4.004 (6 shuffles, mean -4.103, z 22.6); the annealer on the
  real text -2.918. Verdict: **pass**.

## Independent review (13 Nov 2026)

An AI language-model agent that did not make this work cut its own crops and compared M01, the end of M08 with the
start of M09, M14 and the end of M16: 36 of 36 groups agree. It re-ran the scripts with the same output. It noted
that the key is a simple substitution of 23 numbers fitted on far more ciphertext than the unicity distance, that
it gives the places and names above in clean Spanish, and that the key has internal order; it accepted the key on
the reading and graded the reading A, with the held-out test marked weak.

## Prior art (checked 12-13 Nov 2026)

Web searches (see `targets/murguia1914/NOTES.md`) found no edition or decipherment of this sheet. LXVIII-1.23.3148.1
in the same fondo is only a cover note sending "Clave alpha-32" and saying that "Clave N/O.3" was cancelled by order of
the First Chief; the key itself is not on the scan (Brice Dudout's note of 29 Oct 2026,
`research/dudout_2026-10-29/CORRECTIONS-FOR-DANIEL-2026-10-29.txt`, says the same). Whether this sheet uses either
named key is not known.
Narváez 2019 and 2025 and M. W. González, *Con Carranza*, were not read (see `targets/murguia1914/NOTES.md`).

## Remaining gaps

- M01, the three groups before A REUNIRSE ("eln") - blocker: too-short. The three typed groups are legible (45-55-52) and
  decrypt to "eln", which is no word; a clerk's slip or a name the key cannot give, with no second occurrence to test
  either on. They count as not read.
- The day of the month (2[?]) - blocker: illegible. The integration check read the typed date as 22 on the scan, the second figure partly worn; not relied on.
- The key rests on one sheet; 42, 43, 57, 58 and 79 occur once - blocker: too-short. The split-half test does not
  recover the key.

Outside this folder: the other cipher items of catalogue 1465 are not read. LXVIII-1.2.56.1 and 2.75.1 do
not read with this key or with Clave Extra 3; 2.75.1 (about 190 groups, numbers 00-99) was not attacked
ciphertext-only in this round. 8.957.1-2 returned 404 on the image route.

## Escalation

- [x] siblings: every cipher item the catalogue entry names was opened: LXVIII-1.2.56.1 and 2.75.1 (1913, other
  systems, not read), 7.890.1 (`targets/gonzalez1913`), 14.1943.1 (`targets/murguia1914`), 17.2435.1
  (`targets/fuentes1914`), 23.3165.1 (`targets/carranza1914`), and the cover note 23.3148.1 ("Clave alpha-32"; no
  key on the scan); 8.957.1-2 returned 404 on the image route.
- [n/a] clear-pages: a single typed sheet; no clear copy or decipherment with it.
- [x] known-keys: Clave Extra 3 from 14.1943.1 tried: no Spanish. "Clave alpha-32" (23.3148.1) is not on the scan.
- [x] print: web searches on 12 and 13 Nov 2026 (no edition or decipherment found); Narváez 2019 and 2025 and
  *Con Carranza* not read (see Prior art).
- [x] key-rebuild: all 23 numbers on the sheet have a value (hill-climbing fit, three cells set by reading).
- [x] retry: the first three groups of M01 retried against the image and the key; no word.

## Files

`SIGN_CONVENTIONS.md`; `transcription_LXVIII-1.7.890.1.txt` (+ `_pass1`, `_pass2`); `decryption_LXVIII-1.7.890.1.txt`;
`reading_LXVIII-1.7.890.1.md`; `translation_LXVIII-1.7.890.1.md`; `key.tsv`, `key_frozen.tsv`; `validation.tsv`; `scripts/`
(`validation_pairs.py`, `hillclimb.py`, `decrypt.py`, `check_marks.py`, `count_words.py`, `coded_only.py`, `reading_debug.py`; standard
library only; run from this folder, `hillclimb.py` needs the repository root for the lexicon); `work/`
(`fit_7890_full.txt`, `heldout_7890.txt`, `heldout_7890_b.txt`: the fits on all runs, on M01-M08 and on M01-M12).

## Integration check (13 Nov 2026)

Done by the integrating session, not by the contributor. Reproduced: `scripts/check_marks.py` passes (16 runs, 2 marks);
`scripts/decrypt.py` gives the same decryption (the file differs only by line endings); `scripts/count_words.py` gives 61
coded words, 59 verbatim, 1 repaired, 1 open; `docs/_validate.py` gives the same figures (z 7.4, pass). `scripts/hillclimb.py`,
run unchanged (python3 -I, 14 s), gives the same fit: 20 of the 23 cells as in the final key, and the same three misfits that
were set by reading (57 j for ll, 77 f for v, 79 v for x). An own decoder written from `key.tsv` (nothing of the contributor's
scripts imported) gives the same sixteen lines. The CEHM image LXVIII-1.7.890.1.0001 was fetched (plain http, no refusal) and
M01 to M12 (about 190 groups, typed and clear) were compared with the transcription: every group agrees. The split-half test is
a failed test and is published as one: fitted on M01-M08 alone the same program does not find the key (20 symbols, no Spanish),
and on M01-M12 alone it gives 10 of 22 cells (the contributor's figures, not re-run); the key is not validated by a held-out passage. What makes it credible instead is
that 23 symbols were fitted on 290 letters of one monoalphabetic text, far above what a fit needs, that the result is clean
Spanish with place names and surnames the trigram model does not know (Cerralvo, Lampazos, Villaldama, Laredo, San Ygnacio;
Castro, Dávila Sánchez, Santoscoy), that the clear words typed before and after each run fit the decrypted runs ("Hoy salió
... con sus fuerzas", "plaza que ... cuando más ... próximos", "Pasado mañana ... donde ... a fin de mandarles ... a que me
refiero"), and that the key has internal order. Three cells (ll, v, x) were set by reading and 42 h, 43 g, 58 q occur in
one place each. Strict share by the README rule: 59 of 61 coded words (96.7%; the repaired word and the open word count as not
read), over 95%, so the class stays read; key recovered from ciphertext-only. The identification of the writer as Pablo
González is the contributor's inference (the papers, the letterhead and a letter of Murguía), not a name on the sheet.

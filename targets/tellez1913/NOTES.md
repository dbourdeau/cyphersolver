# Rubio Navarrete to Joaquín Téllez, 14 and 15 October 1913: two federal telegrams in the División del Bravo syllabary (CEHM DLXXIII)

Status: decoded, not read. 14 Oct 7 of 16 cipher words read, 15 Oct 3 of 29 (strict count, below). Catalogue 1468.

Contributed by Andrew Beling (ajbeling), with AI agents, 18-22 Nov 2026. AI agents transcribed, rebuilt the table,
tested and wrote this; no person has checked it.

## How this folder relates to rubio1913

`targets/rubio1913/` is Brice Dudout's target: three Rubio Navarrete telegrams to the Minister of War in the printed
"Clave núm. 109", read in full, with the key sheet transcribed in `rubio1913/key.tsv`. His NOTES already note that the
Téllez and División del Bravo traffic in the same fonds uses a different table, an alphabetical numerical syllabary of
1 to 255, and that the 19 July 1913 draft carries a pencil decipherment. This folder takes up that traffic. It has its
own key, so under the one-key rule it is a target of its own. The Blanquet telegram of 19 May 1914, which uses Clave
109, is in `targets/blanquet1914/`. Nothing in `rubio1913/` is changed.

## Documents

Centro de Estudios de Historia de México (CEHM-Carso, Fundación Carlos Slim), fondo DLXXIII (Manuscritos del General
Guillermo Rubio Navarrete):

- DLXXIII.1.32.5-41, 14 Oct 1913, Rubio to Téllez, [Lampazos] to Laredo, one typed sheet, 53 cipher groups in 8 runs.
  [Record 137927](https://www.cehm.org.mx/Buscador/FichaBasica/137927?Tipo=A)
- DLXXIII.1.32.6-41, 15 Oct 1913, Rubio to [Téllez], [Lampazos] to Laredo, two handwritten sheets, 104 groups in 21
  runs. [Record 137928](https://www.cehm.org.mx/Buscador/FichaBasica/137928?Tipo=A)
- Key sources: the 19 July 1913 draft DLXXIII.1.30.17-49 with pencil syllables over the groups
  ([record 137860](https://www.cehm.org.mx/Buscador/FichaBasica/137860?Tipo=A)), and Téllez's 8 Oct 1913 telegram
  DLXXIII.1.32.3-41 ([record 137925](https://www.cehm.org.mx/Buscador/FichaBasica/137925?Tipo=A)), used for training.

Images: CEHM public viewer. The site has no terms-of-use page and its pages state no reuse licence; the footer reads "Todos los Derechos Reservados". So the images are linked, not committed. Only text
recognised from them is committed (the transcriptions, and Apple Vision text in `*.jpg.vision.tsv`).

The `*.sha256` files record the paths of the working folder where the runs were made, so `shasum -c` on them fails here; `AUDIT.py` and `rerun_tests.py` check them against the files in this folder. `SHA256SUMS` at the top of this folder lists every committed file by its path here (`shasum -a 256 -c SHA256SUMS`).

## System and key

A numerical syllabary: numbers 1 to 255 for letters, syllables and a few words (133 = par, 170 = vía, 203 = marcha),
set in the clear text of the telegram and joined by spaces. The table was rebuilt here, not found:

- `diez_gloss.tsv`: 26 values first taken from the July pencil glosses (an earlier test on a 10 July letter missed).
- `candidate.tsv`: 71 entries, the July glosses read again on enhanced images (`july_extensions.tsv`) plus 13 values
  inferred from the 8 Oct telegram and its clear text (`oct8_training_values.tsv`). Frozen before the 14 Oct test.
- `candidate15.tsv`: the 71 entries plus seven values guessed from the 14 Oct telegram (20 = i, 53 = al, 108 = le,
  113 = me, 132 = pa, 140 = pu, 147 = ri). Frozen before the 15 Oct test.

Two later blind readers checked twelve July glosses (`JULY_GLOSSES.md`). The period sheet DLXXIII.1.28.8-23
("alfabeto y sílabas") has not been compared with the rebuilt table.

## Tests

Plans were written and hashed before each run (`PLAN_OCTOBER.md`, `PLAN_OCT15.md`, the `*_plan.sha256` and
`*_time.txt` files). The order of plan and result rests on local file times only. Score: mean Spanish trigram
log-probability across group boundaries, against 1,000 tables with the values shuffled.

| Telegram | Table | Groups known | Shuffles beaten | Result |
|---|---|---:|---:|---|
| 14 Oct | original 26 July values | 17/53 | 667/1,000 | miss |
| 14 Oct | candidate.tsv (71) | 43/53 | 999/1,000 | pass |
| 15 Oct | candidate15.tsv (78) | 76/104 | 1,000/1,000 | pass |
| 15 Oct | the seven additions on their own | 7 occurrences | 984/1,000 | miss |

Details: `NOTES_october.md` and `NOTES_oct15.md`. Replays from the repository root:
`python3 -I targets/tellez1913/AUDIT.py` and
`python3 -I targets/tellez1913/rerun_tests.py targets/esp318/lit/quijote.txt`. `score.py`, `score15.py` and `align15.py`
run only through `rerun_tests.py` and `AUDIT.py`, which rebuild the workspace they expect.

## Reading

Strict rule: a word counts as read only when every letter comes from a tested key value; a supplied or fitted letter
is a hole. Accents are editorial. Word totals rest on an editorial division of undivided number runs.

- 14 Oct: 7 of 16 cipher words read (la, Laredo, de, esa, plaza, tren, en), 44%. "Laredo" is also the clear
  destination; the groups for "plaza" occur on the 8 Oct training sheet.
- 15 Oct: 3 of 29 (está, mandé, temo), 10%. With the three untested additions that occur (20, 108, 113), 7 of 29
  (adding destruida, relevara, relevo, elementos); their separate test missed, so they are not counted.

Both have holes in most sentences, so both are decoded, not read. Files: `oct14.runs` and `oct15.runs`
(transcriptions), `decryption_oct14.txt` and `decryption_oct15.txt` (unedited table output, written by
`python3 -I targets/tellez1913/make_texts.py`), `reading_oct14.md` and `reading_oct15.md` (holes marked),
`oct14_words.tsv`, `oct15_words.tsv`, `word_sources.tsv` (where each letter comes from).

## Prior work

Not in the repository before this folder (Brice Dudout's rubio1913 notes list this traffic as unread), not in the
Tomokiyo index, and no reading in Narváez's 2015 or 2025 articles (`NOTES_october.md`).

Roberto Sergio Rodríguez Narváez, *Criptografía diplomática, política y militar en México, 1813-1926* (Mexico City,
SRE, Dirección General del Acervo Histórico Diplomático, 2019), ISBN 978-607-446-152-7, was checked on 21-22 Nov 2026
from Andrew Beling's photographs of a loan copy: chapters VII-XI (pp. 261-410) and the name index (pp. 487-495). The
photographs are not distributed. The book prints neither these telegrams nor their table. Its index has Manuel Téllez
(pp. 391, 393), not Joaquín, and no Rubio Navarrete. It prints the Carranza-Madero train telegrams of 3-4 Feb 1913 in
another alphabet (pp. 294-295, 302-303, figs. 1-3) and the 1921 Argumedo letters (pp. 359-364), where 34 = A against
34 = s here.

## Newer keys tested, 22 Nov 2026

Plan frozen before the run: `keytest_2026-11-22/PLAN.md`, SHA-256
e4ddf8a5dc81ad6d49e18f99a91eb44ee72c96008a40926abe82412505452ecf (time in `PLAN.sha256`). Keys: the limantour1909 key
(`targets/limantour1909/key.tsv`), the Villa key of open pull request #865 (not upstream), and Daniel Jalkut's
two-digit syllabary card of 20 Nov filed in `targets/duron1911/` (`siblings/syl.py`, read row-column and column-row).
1,000 shuffles each, on these two telegrams and on blanquet1914.

- Limantour's key and the Villa key cover too few groups to test (19-31%).
- Jalkut's card missed on all three: on 14 Oct it beat 542 and 370 of 1,000 shuffles, on 15 Oct 196 and 192.
- On both October telegrams the positive control, this folder's table, beat all shuffles but failed the plan's word
  criterion, so by the plan's rule the test is void here. Only the May result (in blanquet1914) is a clean test.

Summary: `keytest_2026-11-22/results_summary.tsv`. Script: `keytest_2026-11-22/keytest.py`, which reads the three keys
by repo path (`targets/limantour1909/key.tsv`; `targets/villa1914/key.tsv` of pull request #865, head b35ba1997, given
with `--villa` while it is not on main; `targets/duron1911/siblings/syl.py`). It is the frozen run's script with only
the input paths changed; rerun on 23 Nov 2026, its output is byte for byte the frozen run's results (SHA-256 e720c99a...
in `run.sha256`). The full results are not committed; the script writes them.

## Transcription doubts

- 14 Oct, line 1, last group - read: ? (143 or 123 under the watermark); checked: image, decode, transcription (blind visual reading `october14.txt` and Apple Vision disagree); kept as one unknown group.
- 15 Oct, six positions (`oct15_boundaries.tsv`, `oct15_visual1_ambiguities.txt`) - read: ?; checked: image, decode, transcription (two blind readers disagree or flag a cut digit); kept as unknown groups.

## Remaining gaps

- 14 Oct, 9 of 16 words - blocker: not-attempted; untried: the period sheet CEHM DLXXIII.1.28.8-23 ("alfabeto y sílabas"), in the same fonds, has not been compared with these groups; groups 20, 53, 108, 113, 132, 140 and 147 have no tested value and one group is illegible; only the July draft and the 8 Oct telegram carry glosses.
- 15 Oct, 26 of 29 words - blocker: not-attempted; untried: the period sheet CEHM DLXXIII.1.28.8-23 ("alfabeto y sílabas"), in the same fonds, has not been compared with these groups; 28 of 104 groups have no value, and the values that would complete four more words failed their separate test.

## Escalation

- [x] siblings: the 8 Oct telegram (1.32.3-41; its second sheet found after the test) used; the catalogue records of the next three shelfmarks after 15 Oct checked, none described as cipher.
- [x] clear-pages: the July pencil draft is the only contemporary decipherment found; its glosses are in the table.
- [x] known-keys: the limantour1909 key and the Villa key of #865 (not upstream) cover too few groups to test (19-31%). Jalkut's card missed on both telegrams (14 Oct: 542 and 370 of 1,000 shuffles beaten; 15 Oct: 196 and 192), but the test is void here because this folder's own table, the positive control, failed the plan's word criterion. Clave 109 (rubio1913) belongs to the War Ministry traffic and was not scored on these two telegrams.
- [x] print: Narváez 2015, 2025 and the 2019 book (chapters VII-XI and index) checked; no reading.
- [x] key-rebuild: table extended from the July glosses and the 8 Oct telegram; the October 14 additions tested and missed.
- [n/a] retry: no new tested value since the 15 Oct test; the period sheet DLXXIII.1.28.8-23 is the next thing to compare.

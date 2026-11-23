# Blanquet to Rubio Navarrete, 19 May 1914: a War Ministry telegram in "Clave núm. 109" (CEHM DLXXIII.2.41.22-41)

Status: decoded, not read. 15 of 25 cipher words read (strict count, below). Catalogue 1468.

Contributed by Andrew Beling (ajbeling), with AI agents, 18-22 Nov 2026. AI agents transcribed, tested and wrote
this; no person has checked it.

## How this folder relates to rubio1913

The key is Brice Dudout's. In `targets/rubio1913/` he identified the printed key sheet "Clave núm. 109. Secretaría de
Guerra y Marina, con el General Guillermo Rubio Navarrete" (CEHM DLXXIII.1.28.14-23), transcribed it as
`rubio1913/key.tsv`, validated it on a contemporary pair and read three telegrams from Rubio to the Minister of War.
This telegram goes the other way, from the Ministry to Rubio. The key is read in place from `../rubio1913/key.tsv`
and not copied; no value was added or changed.

This telegram uses Brice Dudout's Clave 109, so by the one-key rule it belongs in rubio1913. It is kept in its own
folder only so as not to collide with his open pull request #808, which edits the same NOTES.md and profile.json. Once
#808 is merged, Brice or Daniel may move it into rubio1913 (one document, its steps and a NOTES section), or I can. Nothing in `rubio1913/` is changed. The October 1913
telegrams to Téllez use another table and are in `targets/tellez1913/`.

## Document

Centro de Estudios de Historia de México (CEHM-Carso, Fundación Carlos Slim), fondo DLXXIII, DLXXIII.2.41.22-41:
[Aureliano] Blanquet to Guillermo Rubio Navarrete, [Mexico City], 19 May 1914, two handwritten sheets, 98 cipher
groups in 14 runs between clear Spanish. [Record 138008](https://www.cehm.org.mx/Buscador/FichaBasica/138008?Tipo=A)

Comparison: DLXXIII.2.41.17-41, [Rubio] to Huerta, 25 Mar 1914, one recovered sheet, 107 groups
([record 138003](https://www.cehm.org.mx/Buscador/FichaBasica/138003?Tipo=A)).

Images: CEHM public viewer. The site has no terms-of-use page and its pages state no reuse licence; the footer reads "Todos los Derechos Reservados". So the images are linked, not committed. Only text
recognised from them is committed (the two blind transcriptions in `read_one/` and `read_two/`).

The `*.sha256` files record the paths of the working folder where the runs were made, so `shasum -c` on them fails here; `AUDIT.py` and `rerun_tests.py` check them against the files in this folder. `SHA256SUMS` at the top of this folder lists every committed file by its path here (`shasum -a 256 -c SHA256SUMS`).

## Test

Plan, key hash and threshold frozen before the run (`PLAN.md`, `plan.sha256`, `calibration.json`, the `*_time.txt`
files). The order of plan and result rests on local file times only. Two AI readers transcribed both telegrams blind;
they agreed on 90 of 98 positions (19 May) and 100 of 107 (25 Mar). Brice's three read telegrams served only as
positive controls. Score: mean Spanish trigram log-probability across group boundaries, against 1,000 shuffled keys.

| Telegram | Groups known | Score | Best shuffle | Shuffles beaten | Result |
|---|---:|---:|---:|---:|---|
| 19 May 1914 | 90/98 | −2.5395 | −2.6623 | 1,000/1,000 | pass |
| 25 Mar 1914 | 99/107 | −3.5582 | −2.7290 | 418/1,000 | miss |

The 25 Mar miss shows that Clave 109 does not read that telegram, though most of its numbers fall within the key's
range. Details: `NOTES_may19.md`, `ALIGNMENT.md`, `PRIOR_WORK.md`. Replay from the repository root:
`python3 -I targets/blanquet1914/rerun_tests.py`. `test.py` runs only through `rerun_tests.py`, which rebuilds the workspace it
expects.

## Reading

Strict rule: a word counts as read only when every letter comes from the key; a supplied letter is a hole. Accents are
editorial. Word totals rest on an editorial division of undivided number runs (`may19_words.tsv`).

15 of 25 cipher words read (60%): "abstenerse de hacer indicaciones", "individuos" (twice), "por el general",
"proceder con energía", "sorprender", "ellos", "sobre". Five of the fifteen are single key entries (de, por, el,
general, con). *Indicaciones* and *energía* differ from the key output only by a written accent. Holes are in most
runs, so the telegram is decoded, not read. Files: `may19.runs` (transcription), `decryption_may19.txt` (unedited key
output, written by `python3 -I targets/blanquet1914/make_texts.py`), `reading_may19.md` (holes marked).

In English, in outline: Blanquet tells Rubio to refrain from making representations about individuals who, in
the clear text, were "consignados" by a general (provisionally Hernández), and to proceed with energy; the clear text
later asks him to take precautions and keep strict watch. The damaged middle
and the unread groups leave out who they were and what was meant.

## Prior work

Not in the repository before this folder, and no reading in Narváez's 2015 or 2025 articles (`PRIOR_WORK.md`).

Roberto Sergio Rodríguez Narváez, *Criptografía diplomática, política y militar en México, 1813-1926* (Mexico City,
SRE, Dirección General del Acervo Histórico Diplomático, 2019), ISBN 978-607-446-152-7, was checked on 21-22 Nov 2026
from Andrew Beling's photographs of a loan copy: chapters VII-XI (pp. 261-410) and the name index (pp. 487-495). The
photographs are not distributed. The book prints neither this telegram nor Clave núm. 109, and indexes no Blanquet or
Rubio Navarrete. Pp. 267-269, figs. 5-6, print two military tables for Pascual Orozco. Their Clave 23 shares 107 =
*fuerza* with Clave 109 but gives 98 = *perseguir* and 106 = *heridos* (Clave 109: *Gobernador*, *tropa*). Pp. 374-376
print a War Secretariat key 10 of 1923.

## Newer keys tested, 22 Nov 2026

Same frozen plan as tellez1913 (`../tellez1913/keytest_2026-11-22/PLAN.md`, SHA-256
e4ddf8a5dc81ad6d49e18f99a91eb44ee72c96008a40926abe82412505452ecf). On this telegram Clave 109, the positive control,
passed every criterion, so this is a clean test. The limantour1909 key and the Villa key of open pull request #865 (not
upstream) cover too few groups to test. Daniel Jalkut's two-digit card (`targets/duron1911/siblings/syl.py`) missed:
it beat 2 of 1,000 shuffles read row-column and 888 read column-row.

## Transcription doubts

- 19 May, eight positions (`may19.alignment.tsv`, `read_one/ambiguities.txt`, `read_two/ambiguity.txt`) - read: ?; checked: image, decode, transcription (two blind readers disagree, or the group is cut by the page edge or under the watermark); kept as unknown groups.

## Remaining gaps

- 19 May, 10 of 25 words - blocker: illegible; eight groups are cut, faint or under the watermark on the viewer images, and the rest of the damaged words need those groups.
- 25 Mar telegram to Huerta - blocker: no-key-material; Clave 109 missed, and the presidential code it uses is not in the fonds.

## Escalation

- [x] siblings: the 25 Mar telegram (2.41.17-41) tested; its next image returned an error, so a further sheet is not known.
- [x] clear-pages: no contemporary decipherment on either sheet.
- [x] known-keys: Clave 109 applied unchanged; the limantour1909 key, the Villa key of #865 and Jalkut's card tried.
- [x] print: Narváez 2015, 2025 and the 2019 book (chapters VII-XI and index) checked; no reading.
- [n/a] key-rebuild: the key is a printed period sheet; values are not to be fitted to this telegram.
- [n/a] retry: the unread words need the illegible groups; a better image or a person's reading of the sheets is the next step.

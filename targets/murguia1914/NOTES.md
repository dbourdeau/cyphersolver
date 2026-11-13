# murguia1914: Francisco Murguía to Pablo González, Lamadrid, 16 March 1914 (catalogue 1465), Clave Extra 3

WAINUT, 12-13 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the work blind from the scans (below).

Status: read, 12 Nov 2026 (strict share 95.2% at the integration, 13 Nov 2026; written up on the site, murguia1914.html, PR #513). The letter's coded runs carry a contemporary pencil decipherment on the typed copy, so the
reading is an existing decipherment; this folder adds the figure transcription, the key rebuilt from it, a held-out
test of that key, and a marked reading made from the figures. The key is then applied to two bare sheets of the same
fondo: `targets/fuentes1914/` and `targets/carranza1914/`.

## Document

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo LXVIII-1, LXVIII-1.14.1943.1,
4 scan pages:
- pp. 1-2 (0001-0002): the typed report, clear Spanish with 23 coded runs in two-figure groups, signed "El General,
  Fran.co Murguía", dated "Campamento en Lamadrid, Marzo 16 de 1914", addressed "Al C. Gral. en Jefe de la División
  del Noreste, Pablo González, Matamoros, Tamps.";
- pp. 3-4 (0003-0004): a typed copy of the same report headed "CLAVE EXTRA 3." in red. Over its figures a
  contemporary hand has written the plain text in pencil, letter by letter (`gloss_LXVIII-1.14.1943.1.txt`).

The catalogue calls the item "part coded" and does not mention the pencil decipherment.

Images (CEHM public viewer, no account):
https://www.cehm.org.mx/Buscador/VisorArchivoDigital?jzd=/janium/JZD/LXVIII-1/14/1943/1/LXVIII-1.14.1943.1.jzd
(direct JPG: `http://visor.cehm.org.mx/assets/docx/fondos/jzd/LXVIII-1/14/1943/1/LXVIII-1.14.1943.1.000N.jpg`,
N = 1-4). Fetched one at a time, 2 s apart, on 12 Nov 2026. No licence is stated, so the scans are not in this folder.

## Transcription

`SIGN_CONVENTIONS.md` was written first (shapes only). Pass 1 read the figures from the original (pp. 1-2), pass 2
from fresh crops of the copy (pp. 3-4) with the pencil layer covered. The two passes give the same group at 487 of
488 places. The one difference, S11 group 22, is over-struck in both exemplars (58 or 68; both are u in the key).
The other differences between the exemplars are typing over-strikes and dropped hyphens, listed in the notes of
`transcription_LXVIII-1.14.1943.1.txt`. 488 group occurrences, 52 distinct groups, 23 runs.

## System

Clave Extra 3 (so named on the document). Two-figure groups 10-99, a table read by the units figure:
- tens 1 and 2: a0 b9 c8 d7 e6 f5 g4 h3 i2 j1;
- tens 3 and 4: l0 ll9 m8 n7 ñ6 o5 p4 q3 r2 rr1;
- tens 5 and 6: s0 t9 u8 v7 y4 z3; 51 = -mente;
- 7x-9x are word groups: 78 por, 82 enemigo, 87 para, 90 parque, 91 la, 96 de, 99 que; 88 and 97 are not
  identified.

The layout gives each letter two homophones, one for each tens figure of its pair. In this letter the word groups
(51 and 7x-9x) occur 19 times, as 10 distinct groups.

## Key

`key.tsv` has 62 entries (one line each, after a header line):
- 45 from the cipher/pencil pairs (`scripts/build_key.py` aligns the figures with the pencil letters by dynamic
  programming and takes the majority value per group; output `work/key_all.tsv`);
- 5 set by hand from the segment named in the file (46 ñ, 49 ll, 87 para, 91 la, 99 que), because the aligner split
  those word groups wrongly;
- 10 not attested in any pair and filled from the table layout, marked `table` (11, 13, 15, 25, 31, 33, 36, 39, 43,
  53);
- 2 open (88, 97), written `?`.

`key_frozen.tsv` holds the 60 entries with a value (`scripts/make_key.py`), frozen on 12 Nov 2026 before
LXVIII-1.17.2435.1 and LXVIII-1.23.3165.1 were decrypted. Of the 10 `table` cells, 25 f, 39 ll and 53 z later occur
in those two sheets, where they give oficiales, uniformidad, fuerzas, Saltillo, plaza and establezca.

## Held-out test

A key was built from the page-3 segments only (S01-S15, `work/key_train_p3.tsv`), frozen, and applied to the page-4
segments (S16-S23, 217 groups). Letter agreement with the pencil gloss over its 240 letters: **0.842** (1 minus edit
distance over gloss length). 200 keys with the same values shuffled among the groups score at most 0.154 (mean
-0.036). The errors come from 8 groups that page 3 does not contain (21, 34, 46, 49, 51, 78, 87, 90) and from two
word groups the page-3 aligner got wrong (91, 99). Script `scripts/heldout.py`, output `work/heldout_out.txt`.

## Reading

`reading_LXVIII-1.14.1943.1.md` gives the whole letter as sentences: clear text from pp. 1-2, coded text in capitals
decrypted with `key_frozen.tsv`, accents and word division added. `translation_LXVIII-1.14.1943.1.md` is the English
with the same holes.

Murguía reports his campaign of 4-15 March 1914: he cut the Nacional railway between Golondrinas and Huisachito,
took Monclova with Castro on the 10th, lost it on the 11th to a force of more than a thousand from Monterrey, fell
back to San Buenaventura and the Molino del Águila, failed to retake the place on the 15th and fell back to
Lamadrid. His ammunition is spent, and he is sending a commission to Ciudad Juárez by way of Sierra Mojada for
200,000 cartridges.

Coded words (from `scripts/count_words.py`): 103 in 23 runs; 99 verbatim from the signs (96.1%), 2 with a marked
added letter (NACI{+O}NAL, MOLIN{+O}), 2 guessed ([?no:97], [?plaza:88]). By the README read bar the supplied "[por]" counts too, and a word with a restored letter or a guess is not read: 99 of 104 words = **95.2%** (the contributor's 96.1% leaves "[por]" out). "[por]" before SER is a word the sense needs
and the figures do not give; it is supplied in brackets and not counted. All 23 runs read as words.

Where the figures and the pencil gloss differ (the reading follows the figures, with marks): NACINAL (gloss
Nacional), CORTANDO (gloss cruzando), MOLIN (gloss molino), ESAS (gloss estas), EN ELLA (gloss en el). The gloss
leaves 97 and 88 without a value.

## Checks

- `python scripts/check_marks.py transcription_LXVIII-1.14.1943.1.txt reading_LXVIII-1.14.1943.1.md` rebuilds each
  coded run from transcription and frozen key, undoes the marks, and fails on any unmarked departure: 23 runs, 4 marks,
  0 failures, PASS.
- `python scripts/decrypt.py transcription_LXVIII-1.14.1943.1.txt decryption_LXVIII-1.14.1943.1.txt key_frozen.tsv`
  reproduces the decryption file.
- `python docs/_check_reading.py murguia1914`: see the pull request text. The checker's Spanish word list comes from
  period corpora; it does not know 1914 place names, abbreviations and words (Gral., Ud., Monclova, Golondrinas,
  mencionados ...) and counts each as a hole (`scripts/reading_debug.py <repo> <file>` lists them). On the coded runs
  alone (`scripts/coded_only.py`) the clean share was 0.933.

## Independent review (13 Nov 2026)

An AI language-model agent that did not make this work cut its own crops from the scans before opening the
transcription and compared 59 groups of p. 4 (S18, the end of S22, S23): 59 of 59 agree (the "1037" over-strike split
10-37 as the conventions say). It re-ran `check_marks.py`, `decrypt.py` and `heldout.py` and got the same output,
and confirmed that `build_key.py` reads only the training segments in the held-out run. It read the reading against
the translation and graded it A, noting that it is an existing decipherment and should be credited as such.

## Prior art (checked 12-13 Nov 2026)

- Two web searches (Pablo González 1913-1914 clave; cifrados constitucionalistas; Narváez, "Algunos casos
  criptográficos del movimiento constitucionalista, 1914-1915", Historia Mexicana 75/2, 2025) and one more by the
  reviewer on 13 Nov found no edition or decipherment of this letter or of "Clave Extra 3".
- The only decipherment found is the contemporary pencil gloss on pp. 3-4 of the item itself.
- On issue #321 (catalogue 1464), the contributor reports that Narváez 2025 prints other Constitutionalist tables, not
  the 1915 ones; whether it prints Clave Extra 3 is not checked.
- Not read, and not counted as gaps in the text: Narváez, "Algunos casos criptográficos del movimiento
  constitucionalista, 1914-1915" (Historia Mexicana 75/2, 2025; the PDF answered 403 to a script, and the file
  saved was a bot-check page, not the article); Narváez, *Criptografía diplomática, política y militar en México*
  (2019; not available to the project); Manuel W. González, *Con Carranza* (1933-34), a narrative of these
  campaigns (a PDF is online at constitucion1917.gob.mx; not checked for the plain text). Any of them may print
  the table or the text.
- The only earlier work on this fondo in the repository is Brice Dudout's note of 29 Oct 2026
  (`research/dudout_2026-10-29/CORRECTIONS-FOR-DANIEL-2026-10-29.txt`), which found no key and read nothing.

## Remaining gaps

- Groups 88 and 97 - blocker: open-codes. One occurrence each and not glossed; the sense suggests "plaza" (or "plaza
  por") and "no".
- S11 group 22 - blocker: illegible. Over-struck in both exemplars (58 or 68); both are u, so the reading does not
  depend on it.

## Escalation

- [x] siblings: every cipher item the catalogue entry names was opened: LXVIII-1.2.56.1 and 2.75.1 (1913, other
  systems, not read), 7.890.1 (`targets/gonzalez1913`), 14.1943.1 (`targets/murguia1914`), 17.2435.1
  (`targets/fuentes1914`), 23.3165.1 (`targets/carranza1914`), and the cover note 23.3148.1 ("Clave alpha-32"; no
  key on the scan); 8.957.1-2 returned 404 on the image route.
- [x] clear-pages: the typed copy (pp. 3-4) carries the pencil decipherment; it is the key source.
- [x] known-keys: the 1913 substitution of 7.890.1 tried on these runs: no Spanish; Clave Extra 3 is named on the copy.
- [x] print: web searches on 12 and 13 Nov 2026 (no edition or decipherment found); Narváez 2019 and 2025 and
  *Con Carranza* not read (see Prior art).
- [x] key-rebuild: 60 of 62 cells have a value (45 from pairs, 5 set from a named segment, 10 from the table layout).
- [x] retry: 88 and 97 tried against the sense at their one place each; left as guesses, marked.

## Files

- `SIGN_CONVENTIONS.md`; `transcription_LXVIII-1.14.1943.1.txt` (+ `_pass1`, `_pass2`);
  `gloss_LXVIII-1.14.1943.1.txt` (the pencil layer, as written); `decryption_LXVIII-1.14.1943.1.txt`;
  `reading_LXVIII-1.14.1943.1.md`; `translation_LXVIII-1.14.1943.1.md`; `key.tsv`; `key_frozen.tsv`.
- `scripts/`: `build_key.py` (alignment and majority key), `make_key.py` (writes key.tsv and key_frozen.tsv from
  `work/key_all.tsv`), `heldout.py`, `decrypt.py`, `check_marks.py`, `count_words.py`, `coded_only.py`,
  `reading_debug.py`. Standard library only; run from this folder.
- `work/`: `key_all.tsv` (pairs over all segments), `key_train_p3.tsv` (pairs over S01-S15), `heldout_out.txt`.

## Integration check (13 Nov 2026)

Done by the integrating session. Reproduced: `heldout.py` gives 0.842 letter agreement on page 4 (240 gloss letters, 217
groups), shuffled-key control max 0.154; `check_marks.py` passes (23 runs, 4 marks). Own decoder (written from
`key_frozen.tsv`, not their script) gives the same 23 decryptions (8 differ only in capitals that mark word groups).
Image LXVIII-1.14.1943.1.0004 (the typed copy with the pencil layer) fetched from the CEHM viewer (plain http, no host
refused): all 217 groups of S16-S23 compared by eye with the transcription, all agree; the pencil gloss of S16-S23 is
visible and matches `gloss_LXVIII-1.14.1943.1.txt` where legible; page 3 and the original pp. 1-2 were not compared by the
integrating session. The test uses the contemporary pencil gloss as the truth and the key was rebuilt from the same gloss,
so it is a key recovered from external plaintext in effect; the reading is the gloss's text confirmed by the figures. The
order of freezing is by the contributor's record (one commit, no outside timestamp). Own statistical check
(`docs/_validate.py`, es-modern, 486 groups): reading -2.104 per letter against -6.186 for random keys (z 9.3) and -3.566
for keys annealed onto shuffled text (z 17.5): pass. Strict word count by the README rule: 99 of 104 = 95.2%, at the bar,
so the class stays read; key partial (groups 88 and 97 have no value; ten cells are filled from the table layout, none of
them occurs in this letter). The same key is applied to two bare sheets of the same fondo (targets fuentes1914 and
carranza1914, other pull requests); it belongs to this entry.

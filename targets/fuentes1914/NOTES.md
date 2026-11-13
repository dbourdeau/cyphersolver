# fuentes1914: A. Fuentes D. to Pablo González, Monterrey, 13 June [1914] (catalogue 1465), Clave Extra 3

WAINUT, 12-13 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the work blind from the scans (below).

Status: read in part, 13 Nov 2026. The four coded runs of this pencil note are read with the Clave Extra 3 key rebuilt
in `targets/murguia1914/` from the contemporary pencil decipherment of LXVIII-1.14.1943.1. All 13 coded words read as
sense, but 2 of them rest on a marked one-figure repair chosen by the sense, and by the README read bar a repaired word
is not read: 11 of 13 (84.6%) are verbatim from the signs, under the 95% bar. The contributor's own count is the same;
the reviewer proposed "read" and the contributor kept "read in part" at this share. The key was frozen before
this sheet was decrypted and is copied unchanged into this folder (`key_frozen.tsv`).

## Document

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo LXVIII-1, LXVIII-1.17.2435.1,
1 scan page. A pencil note, dated "Monterrey, 13 Jun." with no year, addressed "Gral. don Pablo González" and signed
"El Jefe de E. Mayor, Cnel. A. Fuentes D." The catalogue names the writer as Alberto Fuentes Dávila and dates the
note 13 June 1914; the sheet itself gives neither the full name nor the year. A large pencil loop is drawn across
the text. Clear Spanish with 4 coded runs in two-figure groups.

Images (CEHM public viewer, no account):
https://www.cehm.org.mx/Buscador/VisorArchivoDigital?jzd=/janium/JZD/LXVIII-1/17/2435/1/LXVIII-1.17.2435.1.jzd
(direct JPG: `http://visor.cehm.org.mx/assets/docx/fondos/jzd/LXVIII-1/17/2435/1/LXVIII-1.17.2435.1.0001.jpg`).
Fetched on 12 Nov 2026. No licence is stated, so the scan is not in this folder.

## Transcription

`SIGN_CONVENTIONS.md` first; pass 1 from the 1600 px overview and 1:1 crops, pass 2 from fresh crops enlarged 1.6x,
both without the key. The passes give the same group at 77 of 81 places; the 4 differences (F01 g1 and g2, F03 g3,
F04 g11) were settled on the enlarged crops as noted in `transcription_LXVIII-1.17.2435.1.txt`. In F04 g11 the first
figure is hidden where the pencil loop crosses the line; it is kept as 12, the figure as it shows. 81 group
occurrences, 29 distinct groups, 4 runs. The word groups occur 3 times, as 2 distinct groups (96 de twice, 99 que).

## System and key

Clave Extra 3: see `targets/murguia1914/NOTES.md` for the table, the key build and the held-out test (0.842 letter
agreement on held-out page 4 of LXVIII-1.14.1943.1, shuffled keys at most 0.154). `key_frozen.tsv` here is that file
(60 entries, frozen 12 Nov 2026), with one comment line added to say where it comes from. This sheet was not used to
build or test the key: it is wholly held out from it.

## Reading

`reading_LXVIII-1.17.2435.1.md` (Spanish, coded text in capitals) and `translation_LXVIII-1.17.2435.1.md`. As chief
of staff ("Jefe de E. Mayor"), Fuentes writes that the chiefs of forces draw pay at different rates: in some pay sheets
the first captain is given $5.00, in others $4.00 or $3.00, and the same holds for the other officers. To establish
uniformity he proposes a scale from private (one peso) to colonel (eight pesos) and asks that González's
decision be sent to all chiefs.

Coded words (`scripts/count_words.py`): 13 in 4 runs; 11 verbatim from the signs (84.6%), 2 with a marked changed
value (counted as not read by the strict rule; the script's own "read share 1.000" counts them). Per run:

| Run | Groups | Words | Verbatim | Marked repair |
|---|---|---|---|---|
| F01 haberes que están cobrando | 21 | 4 | 4 | 0 |
| F02 papeletas {g/e}l capitán primero | 25 | 4 | 3 | 1 |
| F03 demás oficiales | 13 | 2 | 2 | 0 |
| F04 de establece{i/r} uniformidad | 22 | 3 | 2 | 1 |

In both repairs the figure as read is one stroke off what the sense needs: F02 g10 reads 24 (g) where 26 (e) gives
"el", and F04 g11 reads 12 (i) where 42 (r) gives "establecer"; in F04 the first figure is the one hidden under the
pencil loop (the second pass had 12 or 42). Every coded word fits the clear text around it. The quoted text of the reading has
117 words (counted by whitespace), with no hole; the clear words "en m[i]s" and the pay list were read from the pencil once,
without a second pass, and are not part of the cipher count. A word in the top right corner ("Earle"?) is not read.

## Checks

- `python scripts/check_marks.py transcription_LXVIII-1.17.2435.1.txt reading_LXVIII-1.17.2435.1.md`: 4 runs, 2
  marks, 0 failures, PASS.
- `python scripts/decrypt.py transcription_LXVIII-1.17.2435.1.txt decryption_LXVIII-1.17.2435.1.txt key_frozen.tsv`
  reproduces the decryption file.
- `python docs/_check_reading.py fuentes1914`: see the pull request text. The checker's period word list does not
  know the abbreviations, pay figures and some 1914 words (Gral., Ud., Respte., Cnel., establezca, uniformidad,
  cuota), and counts each as a hole. On the coded runs alone the clean share was 1.000.
- `python docs/_validate.py fuentes1914 --write` on `validation.tsv` (one line per group with the frozen key's value;
  `scripts/validation_pairs.py`; marked repairs not applied, unread groups left out): 81 read tokens, 29
  types, model es-modern: reading -2.175 per letter; 200 random keys mean -5.569, max -3.946 (z 6.0);
  a key annealed onto shuffled ciphertext at best -2.591 (6 shuffles, mean -2.675, z 6.0); the annealer on the
  real text -2.295. Verdict: **pass**.

## Independent review (13 Nov 2026)

An AI language-model agent that did not make this work cut its own crops and compared F01 line 1, F02 line 1, the
end of F03 with the start of F04, and F04 line 2: 39 of 39 groups agree, including the hidden figure of F04 g11,
which the reviewer also saw as "/2". It re-ran the scripts with the same output, proposed the state "read" and graded the reading A: three clean
sentences, the coded parts fit the clear text exactly, and both one-figure repairs were checked on the image.

## Prior art (checked 12-13 Nov 2026)

Web searches (see `targets/murguia1914/NOTES.md`) found no edition or decipherment of this note or of Clave Extra 3.
No earlier work on it in the repository; Brice Dudout's note of 29 Oct 2026 on this fondo found no key.
Narváez 2019 and 2025 and M. W. González, *Con Carranza*, were not read (see `targets/murguia1914/NOTES.md`).

## Remaining gaps

- F04 g11, the first figure of "establece{i/r}" - blocker: illegible. Hidden where the pencil loop crosses the line; read
  12 as it shows, the sense needs 42.
- F02 g10, "{g/e}l" - blocker: too-short. The sheet shows 24 (g) where the sense needs 26 (e); it is a single occurrence, so
  a slip of the writer or a misread cannot be told apart.
- F01 g2 (second figure of the second group of "haberes") - blocker: illegible. Open at the top, 0 or 9; the transcription
  keeps 20 (a) because "haberes" needs it (the integration check saw 20 and 29 as both possible on the scan). The word stays
  counted as verbatim, as the contributor counted it; the doubt is recorded here.

Not gaps in the cipher: the clear words "en m[i]s" and the pay list were read once, without a second pass,
and the corner word ("Earle"?) is not read; the year 1914 is the catalogue's.

## Escalation

- [x] siblings: every cipher item the catalogue entry names was opened: LXVIII-1.2.56.1 and 2.75.1 (1913, other
  systems, not read), 7.890.1 (`targets/gonzalez1913`), 14.1943.1 (`targets/murguia1914`), 17.2435.1
  (`targets/fuentes1914`), 23.3165.1 (`targets/carranza1914`), and the cover note 23.3148.1 ("Clave alpha-32"; no
  key on the scan); 8.957.1-2 returned 404 on the image route.
- [n/a] clear-pages: a single pencil sheet; no clear copy or decipherment with it.
- [x] known-keys: Clave Extra 3 from 14.1943.1 (same fondo, same year) reads every coded run.
- [x] print: web searches on 12 and 13 Nov 2026 (no edition or decipherment found); Narváez 2019 and 2025 and
  *Con Carranza* not read (see Prior art).
- [x] key-rebuild: every group on the sheet has a value in the frozen key; 25 f, 39 ll and 53 z, filled from the
  table layout, read here.
- [x] retry: the two groups with a repair re-read on enlarged crops and by the reviewer; the figures stay as read.

## Files

`SIGN_CONVENTIONS.md`; `transcription_LXVIII-1.17.2435.1.txt` (+ `_pass1`, `_pass2`);
`decryption_LXVIII-1.17.2435.1.txt`; `reading_LXVIII-1.17.2435.1.md`; `translation_LXVIII-1.17.2435.1.md`;
`key_frozen.tsv` (copy from `targets/murguia1914/`); `validation.tsv`; `scripts/` (`validation_pairs.py`, `decrypt.py`, `check_marks.py`, `count_words.py`,
`coded_only.py`, `reading_debug.py`; standard library only; run from this folder).

## Integration check (13 Nov 2026)

Done by the integrating session, not by the contributor. Reproduced: `scripts/check_marks.py` passes (4 runs, 2 marks);
`scripts/decrypt.py` gives the same decryption (the file differs only by line endings); `docs/_validate.py` gives the same
figures (z 6.0, pass). An own decoder written from `key_frozen.tsv` (nothing of the contributor's scripts imported) gives
the same four lines. `key_frozen.tsv` equals `targets/murguia1914/key_frozen.tsv` of the Murguía pull request (#513) line for
line apart from two comment lines. The CEHM image LXVIII-1.17.2435.1.0001 was fetched (plain http, no refusal) and every run
was compared with the transcription: all groups agree except the places listed under Remaining gaps. The order in which the key
was frozen and this sheet decrypted rests on the contributor's record (one commit, no external timestamp); the test is
nonetheless real because the key was built from another item and nothing on this sheet was used to fit it. Method: key
recovered based on adjacent plaintext (the contemporary decipherment of LXVIII-1.14.1943.1, rebuilt in `targets/murguia1914/`),
applied unchanged here; the key entry is `murguia1914`, this page is one more document read with it. `key: partial` because
the key as a whole has only 60 of its cells valued. Other Mexican targets (mexico1911, hernandez1911, mccarty1911,
nuevaclave1911, duron1911, mundic1912, delabarra1913, nunez1899, reyes1886) use other systems; reyes1886's numeric key agrees
with this one in 1 of 27 common groups.

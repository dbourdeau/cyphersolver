# carranza1914: a message signed V. Carranza, transcribed for Pablo González on Villa and Saltillo, undated [probably May 1914] (catalogue 1465), Clave Extra 3

WAINUT, 12-13 Nov 2026. Work done with AI language-model agents viewing the CEHM images; no human palaeographer has
checked the text. An independent AI language-model agent reviewed the work blind from the scans (below).

Status: read in part, 12 Nov 2026. The eight coded runs of this pencil sheet are decrypted with the Clave Extra 3 key
rebuilt in `targets/murguia1914/` from the contemporary pencil decipherment of LXVIII-1.14.1943.1. The key was frozen
before this sheet was decrypted and is copied unchanged into this folder (`key_frozen.tsv`). 52 of the 61 coded
words are verbatim from the signs (85.2%), under the 95% bar.

## Document

CEHM-Carso (Centro de Estudios de Historia de México, Fundación Carlos Slim), Fondo LXVIII-1, LXVIII-1.23.3165.1,
1 scan page, pencil, undated. "El Capitán Ayudante, A. H. Castañeda" transcribes to "Gral. P. González" a message
signed "V. Carranza" and "fechado ayer en S[...]". The right half is faint, and a large loop and a vertical line are
drawn across the text in pencil. Clear Spanish with 8 coded runs in two-figure groups.

The sheet gives no date. The orders (forces to move on Saltillo, a chief from Monterrey to serve under Villa, Coss to
stand south of Saltillo on the enemy's line of retreat) fit the Constitutionalist operation against Saltillo in May
1914; that date is our inference.

Images (CEHM public viewer, no account):
https://www.cehm.org.mx/Buscador/VisorArchivoDigital?jzd=/janium/JZD/LXVIII-1/23/3165/1/LXVIII-1.23.3165.1.jzd
(direct JPG: `http://visor.cehm.org.mx/assets/docx/fondos/jzd/LXVIII-1/23/3165/1/LXVIII-1.23.3165.1.0001.jpg`).
Fetched on 12 Nov 2026. No licence is stated, so the scan is not in this folder.

## Transcription

`SIGN_CONVENTIONS.md` first; pass 1 from the 1600 px overview, pass 2 from fresh half-width crops enlarged 1.2-1.3x
with contrast stretch, both without the key. The passes give the same group at 209 of 235 places. The 26
differences were settled on the enlarged crops where possible (notes in `transcription_LXVIII-1.23.3165.1.txt`);
8 groups keep one or two unread figures (C01 g9, g13, g36; C06 g14, g31; C07 g10, g25; C08 g15). 235 group
occurrences, 41 distinct fully read groups, 8 runs. The word groups occur 13 times, as 4 distinct groups (82
enemigo once, 87 para once, 96 de seven times, 99 que four times).

## System and key

Clave Extra 3: see `targets/murguia1914/NOTES.md` for the table, the key build and the held-out test (0.842 letter
agreement on held-out page 4 of LXVIII-1.14.1943.1, shuffled keys at most 0.154). `key_frozen.tsv` here is that file
(60 entries, frozen 12 Nov 2026), with one comment line added to say where it comes from. This sheet was not used to
build or test the key: it is wholly held out from it.

## Reading

`reading_LXVIII-1.23.3165.1.md` (Spanish, coded text in capitals) and `translation_LXVIII-1.23.3165.1.md`. The
message orders that forces "pertenecientes a esta División" move on Saltillo; that González choose one of the chiefs
at Monterrey to go and cooperate in the operations against the place under the immediate orders of General Villa;
and that General Coss take up position with his forces south of Saltillo, on the enemy's line of retreat, to attack
him as he leaves the place, acting in concert with General Eulalio Gutiérrez on the line from Saltillo to San Luis.

Coded words (`scripts/count_words.py`): 61 in 8 runs; 52 verbatim from the signs (85.2%), 2 with a marked repair
({+l}as, c{f/o}n), 7 with a guess for a group whose figures are not legible. Five of the guesses are one letter
each (m in moverse, a in al, l in Eulalio, e in se, i in Luis), one is two letters in one word (e and n in
pertenecientes), and one is the whole word "que" for the group ?9 after PARA. Each guess is forced by the word around it. Per run:

| Run | Groups | Words | Verbatim | Marked repair | Guess |
|---|---|---|---|---|---|
| C01 | 60 | 11 | 9 | 0 | 2 |
| C02 | 41 | 9 | 8 | 1 | 0 |
| C03 | 15 | 5 | 5 | 0 | 0 |
| C04 | 20 | 7 | 7 | 0 | 0 |
| C05 | 25 | 6 | 6 | 0 | 0 |
| C06 | 32 | 11 | 8 | 1 | 2 |
| C07 | 25 | 6 | 4 | 0 | 2 |
| C08 | 17 | 6 | 5 | 0 | 1 |

The coded "a esta División a moverse" has no governing verb in what is read of the clear head of the message, whose
words are faint; none is supplied.

## Checks

- `python scripts/check_marks.py transcription_LXVIII-1.23.3165.1.txt reading_LXVIII-1.23.3165.1.md`: 8 runs, 10
  marks, 0 failures, PASS.
- `python scripts/decrypt.py transcription_LXVIII-1.23.3165.1.txt decryption_LXVIII-1.23.3165.1.txt key_frozen.tsv`
  reproduces the decryption file.
- `python docs/_check_reading.py carranza1914`: see the pull request text. The low clean share comes from the guessed
  letters, which sit inside words, and from names and abbreviations the period word list does not know (Saltillo,
  Gral., Ud.). On the coded runs alone the clean share was 0.125.
- `python docs/_validate.py carranza1914 --write` on `validation.tsv` (one line per group with the frozen key's value;
  `scripts/validation_pairs.py`; marked repairs not applied, unread groups left out): 227 read tokens, 41
  types, model es-modern: reading -2.317 per letter; 200 random keys mean -6.136, max -4.722 (z 7.3);
  a key annealed onto shuffled ciphertext at best -2.978 (6 shuffles, mean -3.122, z 8.1); the annealer on the
  real text -2.828. Verdict: **pass**.

## Independent review (13 Nov 2026)

An AI language-model agent that did not make this work cut its own crops and compared C01 line 1, C02 line 1, the
end of C04 and the end of C07 (47 groups): every legible group agrees. C02 g14 it first read 22, and on a 3x zoom 42
as transcribed. A stroke after "32" in C01 that it first took for a group is a descender from the line above, and the
transcription is right to skip it. C01's faint groups are left open by both. It re-ran the scripts with the same
output and graded the reading B: coherent orders, with 7 words guessed for unread pencil figures, each forced by the
word; the clear head is partly faint, and the May 1914 date is an inference and labelled as one.

## Prior art (checked 12-13 Nov 2026)

Web searches (see `targets/murguia1914/NOTES.md`) found no edition or decipherment of this sheet or of Clave Extra 3.
No earlier work on it in the repository; Brice Dudout's note of 29 Oct 2026 on this fondo found no key.
`targets/carranza1915/` (catalogue 1464) is a different fondo (CDLXXX), year and system.
Narváez 2019 and 2025 and M. W. González, *Con Carranza*, were not read (see `targets/murguia1914/NOTES.md`).

## Remaining gaps

- 8 groups with an unread figure (C01 g9, g13, g36; C06 g14, g31; C07 g10, g25; C08 g15) - blocker: illegible. Faint
  pencil or under the drawn loop; the reading guesses a value for each, marked.
- The clear head of the message ("fechado ayer en S[...]") is not fully read - blocker: illegible.

Not a gap in the cipher: the sheet gives no date; probably May 1914 from the content.

## Escalation

- [x] siblings: every cipher item the catalogue entry names was opened: LXVIII-1.2.56.1 and 2.75.1 (1913, other
  systems, not read), 7.890.1 (`targets/gonzalez1913`), 14.1943.1 (`targets/murguia1914`), 17.2435.1
  (`targets/fuentes1914`), 23.3165.1 (`targets/carranza1914`), and the cover note 23.3148.1 ("Clave alpha-32"; no
  key on the scan); 8.957.1-2 returned 404 on the image route.
- [n/a] clear-pages: a single pencil sheet; no clear copy or decipherment with it.
- [x] known-keys: Clave Extra 3 from 14.1943.1 (same fondo, same year) gives a value to every fully read group; the
  unread words come from illegible figures, not from missing key cells.
- [x] print: web searches on 12 and 13 Nov 2026 (no edition or decipherment found); Narváez 2019 and 2025 and
  *Con Carranza* not read (see Prior art).
- [x] key-rebuild: every fully read group on the sheet has a value in the frozen key.
- [x] retry: the 8 groups with an unread figure retried on the pass-2 crops (enlarged, contrast stretched) and by
  the reviewer at up to 3x zoom; still unread, guesses marked.

## Files

`SIGN_CONVENTIONS.md`; `transcription_LXVIII-1.23.3165.1.txt` (+ `_pass1`, `_pass2`);
`decryption_LXVIII-1.23.3165.1.txt`; `reading_LXVIII-1.23.3165.1.md`; `translation_LXVIII-1.23.3165.1.md`;
`key_frozen.tsv` (copy from `targets/murguia1914/`); `validation.tsv`; `scripts/` (`validation_pairs.py`, `decrypt.py`, `check_marks.py`, `count_words.py`,
`coded_only.py`, `reading_debug.py`; standard library only; run from this folder).

## Integration check (13 Nov 2026)

Done by the integrating session, not by the contributor. Reproduced: `scripts/check_marks.py` passes (8 runs, 10 marks);
`scripts/decrypt.py` gives the same decryption (the file differs only by line endings); `scripts/count_words.py` gives 61
coded words, 52 verbatim, 2 repaired, 7 guessed; `docs/_validate.py` gives the same figures (z 7.3, pass). An own decoder
written from `key_frozen.tsv` (nothing of the contributor's scripts imported) gives the same eight lines. `key_frozen.tsv` equals
`targets/murguia1914/key_frozen.tsv` of the Murguía pull request (#513) line for line apart from two comment lines. The CEHM
image LXVIII-1.23.3165.1.0001 was fetched (plain http, no refusal) and runs C01 to C03, C06 and C07 were compared with the
transcription at full resolution (about 100 groups): every legible group agrees; the open places are as transcribed (C06 g14
looks like 99, que, with an open top, which is the contributor's guess). The strict share is the contributor's: 52 of 61
coded words verbatim (85.2%); the 2 repaired and the 7 guessed words are not read. The order in which the key was frozen and this
sheet decrypted rests on the contributor's record (one commit, no external timestamp); the test is nonetheless real because
the key was built from another item and nothing on this sheet was used to fit it, and the decryption names Saltillo, Villa,
Coss, Eulalio Gutiérrez and San Luis. Method: key recovered based on adjacent plaintext (the contemporary decipherment of
LXVIII-1.14.1943.1, rebuilt in `targets/murguia1914/`), applied unchanged here; the key entry is `murguia1914`, this page is
one more document read with it; `key: partial` because the key as a whole has only 60 of its cells valued. The date (probably
May 1914) is the contributor's inference from the orders, not from the sheet.

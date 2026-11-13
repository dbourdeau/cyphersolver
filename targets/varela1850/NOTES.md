# varela1850: Benito Varela to the Consul General of Paraguay in Rio de Janeiro, Asunción, 13 February 1850 (catalogue 1500)

## Document

- Archivo Nacional de Asunción, Colección Rio Branco, ANA-AHRP-PY-558-1-31, item 13 (ex Biblioteca Nacional, Rio de
  Janeiro, I-29,25,23 no. 13), sheets 586-587.
- Benito Varela, who signs for the Ministerio de Relaciones Exteriores of Paraguay, to the Consul General of the
  Republic at the court of Rio de Janeiro. The letter does not name the consul; the ANA file title names the
  correspondent of the whole file as Manuel Moreira de Castro. One letter of two pages, clear Spanish with 12 runs of
  dot-separated numbers (86 group occurrences, 17 distinct values: 16 letter values of the table and the lone 98), five lone numbers (25 twice, 1 twice, 116), a
  lone 98 inside the last run, and one sign: 7 occurrences of 5 distinct items outside the letter table.
- Images: the ANA's PDF of the file, `ANA-AHRP-PY_-_558-1-31.compressed.pdf` (98 images), images 41-42 (0-based),
  https://riobranco.archivonacional.gov.py/uploads/r/archivo-nacional-de-asuncion/8/3/5/8353484cf68d7a80d9ddbfe3c3bee098b13c26efaa58f1bacbc368e0c6755294/ANA-AHRP-PY_-_558-1-31.compressed.pdf
  (downloaded 12 Nov 2026, 6.3 MB). The embedded page images are 685 x 973 and 695 x 961 px, the largest the PDF
  holds; all crops were made from them. Catalogue record:
  https://riobranco.archivonacional.gov.py/index.php/correspondencia-entre-el-ministro-de-relaciones-exteriores-de-la-republica-del-paraguay-y-el-senor-manuel-moreira-de-castro-primeramente-consul-y-despues-plenipotenciario-del-paraguay
  The ANA description of item 13 says the passages could not be identified because they are written in cipher.

## System

A one-value-per-letter table on odd numbers. Vowels on 1-9 (u 1, a 3, e 5, i 7, o 9); consonants on the odd numbers
from 11 in the order of the alphabet with k, ll and ñ and without ch (b 11, c 13, d 15, f 17, g 19, h 21, j 23, k 25,
l 27, ll 29, m 31, n 33, ñ 35, p 37, q 39, r 41, s 43, t 45, v 47, x 49, y 51, z 53). Values found in the letter
runs: 1 3 5 7 9 13 15 19 27 31 33 35 37 41 43 45. Words are enciphered whole inside clear sentences; runs are broken
at line ends. Lone numbers (25, 1, 116, and 98 inside the last run) and one barred-circle sign stand for words or
names from some other list: 25 and 1 would be k and u in the table, which makes no sense alone, and 98 and 116 are
even or above the table. They are not identified.

## Key source

No key is filed and no decipherment is on or with the letter (catalogue vetting, 28 Oct 2026, images 38-45). The key
was rebuilt by cryptanalysis from one crib:

1. Crib (run R05 only): `9.13.1.37.3.13.7.9.33` before the clear `de / Grande` ("[Rio] Grande"), read as
   `ocupacion`. Both repeats in the run (9 o, 13 c) match the word. This gives o 9, c 13, u 1, p 37, a 3, i 7, n 33.
   The crib was suggested at triage from the context ("soñar en la ... de Grande").
2. Rule read off those seven values: vowels on 1-9 (e 5 fills the gap) and consonants on odd numbers from 11 in
   alphabetical order. c 13, n 33 and p 37 fit three orders of the consonants (A: k and ll, no ch; B: ch and ll, no
   k; C: ch and k, no ll). All three were written out and frozen (`scripts/build_keys.py`, `key_candidates.tsv`)
   before any other run was decrypted.

## Held-out test

Held out: all 11 letter runs other than R05 (76 groups; the lone group 98 left out). Script: `scripts/heldout.py`,
against the repo's Spanish lexicon `lang/lexicons/es.json.gz`.

- Whole-run measure (the run decrypts to one, two or three lexicon words): candidate A 49 of 76 groups (64.5%),
  B 46 (60.5%), C 24 (31.6%); 1,000 keys that keep the seven crib values and shuffle the rest: mean 9.1%, max 44.7%,
  none at or above A. The lexicon has no proper names and not `ministerial`, so Olinda, Paulino and ministerial do
  not count, and it lets some nonsense through by cutting it into short words; the number is rough.
- Read by hand, candidate A gives Spanish words or names for 8 of the 11 held-out runs: `contrata`, `pesos`,
  `Olinda` (twice), `Paulino`, `declaracon` (for declaracion, one letter missing), `de`, `ministerial`; and
  `ocupagion` (ocupacion with one group 19 for 13). Not read: `soñ` (R02), `le / ite` (R03), and the tail of R12.
  Candidates B and C give `che` for `de`, `olincha`, `checlaracon`, so A is the key (`key_frozen.tsv`, `key.tsv`).
- Every held-out word uses letters that the crib did not give and the rule predicted (d, e, l, m, r, s, t).
- Limits: the test is short (76 groups); the crib and the rule were chosen by the solver, and the held-out words are
  read against the clear context, which was visible throughout.

## Reading

`reading_varela1850.md` (Spanish, the whole letter), `translation_varela1850.md` (English, same holes),
`marks_varela1850.md` (each cipher item against the signs). `scripts/check_marks.py` rebuilds the decryption and
checks every mark; it passes.

Word counts (cipher only): 14 cipher words. 9 verbatim from the signs (contrata, pesos, ocupacion, Olinda twice,
Paulino, de twice, ministerial), 2 with a marked repair (declarac{+i}on, ocupa{g/c}ion), 0 from a gloss, 3 holes
(R02 `soñ`, R03 `leite`, R12 tail `lg`). Verbatim share 9/14 = 64.3%. Seven further items are lone numbers or a sign,
not identified (25 twice, 1 twice, 116, 98, the barred circle); counted with them as holes the share is 9/21 = 42.9%.

Dan's checker (`docs/_check_reading.py --file`, re-run on origin/main 65cdcd9d5, 13 Nov 2026): reading_varela1850.md
clean share 0.536 (15 of 28 sentences, es); translation_varela1850.md 0.561 (23 of 41 sentences, en; the notes at
its end were reworded on 13 Nov, which split them into more sentences). Many failing sentences fail on ordinary
clear words that the period word list lacks (agradará, concentración, diarios, embarazado, distinguida, explícito) or on dates;
the sentences with cipher fail on the unidentified numbers [25], [1], [98] and the holes.

Proposed state: **read in part**. The letter builds coherent sentences: the minister acknowledges the consul's notes
of 17 October and 21 November 1849 and the newspapers; Hopkins has arrived with the letter of 12 November; the
President does not see why the news of the concentration should please [25], unless [25] dreams of occupying [Rio]
Grande; he has seen in print the business of Olinda with [1]; it is strange that Paulino should feel embarrassed by
Olinda's declaration to [1] that [sign], as to the occupation of [Rio] Grande, would be [116]; he is tainted with the
ministerial perfidy. The cipher gives only the names Olinda and Paulino, and the clear text only the surname Hopkins.
The contributor identifies Olinda and Paulino as, very likely, the Brazilian foreign ministers Pedro de Araújo Lima
(Viscount of Olinda) and Paulino José Soares de Sousa, who followed him in October 1849, and Hopkins as very likely
Edward A. Hopkins, the United States agent in Paraguay. These are identifications from context, not from the signs.
Because most cipher sentences keep one or two unidentified name numbers, a reviewer may judge the state lower; the
holes are marked throughout.

Marked repairs (read, not gaps):
- R10 group 19 for 13 (ocupagion): the blind reviewer saw the 19 on the image and takes it as a writer's slip;
  marked `ocupa{g/c}ion`.
- R08 `declaracon`: the i is missing in the signs (writer's slip); marked `declarac{+i}on`.

## Independent review (13 Nov 2026)

An AI language-model agent that did not take part in the solve reviewed the folder blind (not published here).

- Sign check on the images before it opened the transcription: runs R01, R02, R03, R05, R06, R07, R08 (first line),
  R10 and R12 (second line), 64 group occurrences in all, copied at 3x-7x. All 64 agree with the reconciled
  transcription, including R02 first group 43 and R10 sixth group 19.
- Its own decryption code, from `transcription_varela1850.txt` and `key_frozen.tsv`, gives the same output as
  `scripts/decrypt.py`; `scripts/check_marks.py` passes; `scripts/heldout.py` gives the figures above.
- Reading as sentences, with the rule "about one hole in ten words or fewer": of 15 sentences of the letter, 13 hold,
  1 is borderline (the Paulino sentence: [1], the barred-circle sign, [?Provincia] and [116] in about 35 words, with
  the syntax intact) and 1 fails (the closing "viciado de la perfidia ministerial [98] de [...]").
- State agreed: read in part (9 of 14 cipher words verbatim; 7 occurrences of lone numbers and the sign
  unidentified). Grade B.

## Remaining gaps

- Lone numbers 25 (twice), 1 (twice), 116, 98 and the sign - blocker: open-codes; a separate code list for names
  or words (7 occurrences, 5 distinct items), not identified. Guesses from context (25 = Rosas, 1 = the Argentine
  envoy in Rio) are not tested and are not used in the reading.
- R02 `43.9.35` (soñ) after "Ingles" - blocker: open-codes; decodes letter by letter but gives no sense (an
  abbreviation or a name?). The first group was read 49 in the first pass and settled as 43 on an 8x crop; neither
  gives sense. The blind reviewer also read 43 on the image.
- R03 `27.5 / 7.45.5` (le / ite) after "Montevideo" - blocker: open-codes; decodes, no sense found in place. The
  blind reviewer suggests it may be the surname Leite, a person who received the money ("y de que ese recibió los
  pesos"), to be offered as `[?Leite]` in a later round. Not tested; kept as a hole. The ANA file description of
  558-1-31 (items 4-6) names a merchant Joaquín Leite de Amaral Coutinho; whether he is meant here is not checked.
- R12 tail `98.15.5.27.19` (98 de lg) - blocker: open-codes; 98 is outside the table, `de lg` not read, and the
  last group has a line through it.
- Clear-text doubts - blocker: illegible; the word after "ese" on sheet 587 (read "ayer") and the abbreviated word
  after the second "ocupacion" (read "Provincia", possibly "Frances"), on the low-resolution images.
- Image resolution - blocker: illegible; only the PDF's embedded images (about 690 px wide) are online;
  a better scan from the ANA would help on R02, R10 and R12.
- Held-out test - blocker: too-short; 76 groups, crib and rule chosen by the solver with the clear context visible.
- Sibling letters - blocker: not-attempted; the other Varela letters of 558-1-31 and sibling files were not paged
  through for more cipher in the same table; they could settle the lone numbers.

## Escalation

- [ ] siblings: only PDF images 38-45 of 558-1-31 were opened (catalogue vetting, 28 Oct 2026); the other letters
  of the file and sibling files are not paged through
- [x] clear-pages: images 38-45 checked for a decipherment, interlining or key on or with the letter; none
- [x] known-keys: no key of this series or of the Paraguayan foreign ministry of the period found (DECODE dumps,
  Cryptiana, Lasry's list, web searches, 28 Oct and 12 Nov 2026); nothing to try
- [ ] print: web searches only; printed Paraguayan and Brazilian diplomatic collections not checked page by page
- [ ] key-rebuild: the letter table is complete (27 entries); the lone numbers (4 distinct numbers and one sign) are
  not rebuilt, context guesses only
- [x] retry: R02, R03 and the R12 tail re-read on the images by the blind reviewer (13 Nov 2026) and decoded with
  the frozen key; signs confirmed, still no sense (R03 possibly Leite, open)

## Prior art

- Catalogue vetting, 28 Oct 2026: DECODE dumps, Cryptiana, Lasry's list, web searches for an edition and for
  literature on Paraguayan diplomatic ciphers of the López era: nothing found.
- 12 Nov 2026: one web search (Varela, Moreira de Castro, 1850, carta cifrada, Olinda, Paulino, Rio Grande): no
  edition or decipherment of this letter found. Printed Paraguayan and Brazilian diplomatic collections were not
  checked page by page.

## Method

AI language-model agents (for WAINUT) transcribed the numbers twice from crops of the PDF images without the key
(pass 1 at page view and 2x; pass 2 at 3x-8x), settled three disagreements on the image (R02 43 not 49; R10 19 not
13; R12 27 not 21), built the candidate keys from the crib and the order rule, froze them, ran the held-out test,
decrypted mechanically (`scripts/decrypt.py`) and read with every departure marked. No human palaeographer checked
the text.

## Files

`SIGN_CONVENTIONS.md`, `transcription_varela1850_pass1.txt`, `transcription_varela1850_pass2.txt`,
`transcription_varela1850.txt`, `key_candidates.tsv`, `key_frozen.tsv`, `key.tsv`, `decryption_varela1850.txt`,
`marks_varela1850.md`, `reading_varela1850.md`, `translation_varela1850.md`, `profile.json`, `scripts/`
(`build_keys.py`, `decrypt.py`, `heldout.py`, `reading.py`, `check_marks.py`), `work/heldout_out.txt` (output of
`scripts/heldout.py`). Scans are not in git.

`key_frozen.tsv` and `key.tsv` are the same file: 27 entries (one value per letter, 1 to 53 odd), 29 lines with
the comment line and the header. Of the 27 entries, 7 come from the crib, 1 from the vowel gap (e 5) and 19 from
the order rule. 16 of the 27 values occur in the letter runs. `key_candidates.tsv` holds the three candidate orders
A, B and C side by side: 27 entries, 28 lines with the header.

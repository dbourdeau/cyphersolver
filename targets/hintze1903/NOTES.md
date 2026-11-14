# Hintze Ribeiro to Queen Amélie, two code telegrams of April and May 1903 (ANTT PT/TT/CAM/M15, catalogue 406)

Status: contributed by WAINUT (27 Oct 2026). The May telegram is read from a decode made at the time and written on
the form; the April telegram has no decode, and only one of its 29 groups has a value. Pairing the decode with the
groups gives 24 values of a code whose order is alphabetical within page blocks, with the lower pages reversed. The
site page and the ledger rows are left to the maintainer.

Catalogue 406. Contributed by WAINUT (https://github.com/WAINUTAI). The work was done with AI language-model agents;
the transcriptions were made with a vision-capable language model from the DigitArq images. A reviewing agent checked
all four images (both faces, both backs) against its own crops, re-derived the alignment and the word counts, found
the page model of the code (section 4) and corrected the first pass's account of the April telegram; the corrections
are applied here.

## 1. The unit

- **Source.** Arquivo Nacional Torre do Tombo, *Documentos de D. Carlos, D. Amélia e D. Manuel II*, maço 15,
  PT/TT/CAM/M15, [DigitArq record](https://digitarq.arquivos.pt/documentDetails/70a181c91c944a74bed573252735928b),
  4 images (two telegrams and their backs), downloadable through DigitArq's JSON backend. The images carry the ANTT
  watermark and are not copied here.
- **Dating.** DigitArq dates the file 1913, and the catalogue "before 1907". The telegrams are of 1903: m0001 has the
  stamp NAPOLI 23 APR 03 and "Ricevuto il 23/4 190[3]"; m0003 has the stamp CENTRAL PARIS .. MAI 03 and the header day
  11, on a form printed "Mai 1902". Both belong to Queen Amélie's Mediterranean journey of spring 1903 on the yacht
  *Amélia*, which ended in Paris. Hintze Ribeiro was head of the government.

## 2. The telegrams

| image | route and date | groups | decode of the time | state |
|---|---|---|---|---|
| m0001 (back m0002) | Lisbon -> Naples, "à bord du yacht Amelia", 23 Apr 1903, URGENZA, no. 7325, 75 words | 29 among clear words | none | not read |
| m0003 (back m0004) | Monte Estoril -> Paris (Hotel Bristol), 11 May 1903, Exprès, no. 12, 46 words | 25 among clear words | under the strips, continued on the back | read |

**Word count** (`code.py`, part 1): with five figures to a word, the address counted and punctuation not, m0001 gives
12 + 63 = 75 and m0003 9 + 37 = 46, both the figures of the headers. This confirms both transcriptions, including the
two "S" items of m0003, and shows that m0001's "60134" with a stray stroke is one five-figure group (as a six-figure
group the count would be 76).

## 3. The readings

**m0003, 11 May 1903** (`m0003_*`). The decode is written in four lines under the strips and continues on the back.
Split at the clear words, the groups and the decode's units agree segment by segment (1, 3, 5, 4, 8, 1, 1, 2;
`code.py`, part 2); 43322 stands both times where the decode says "Ministro dos Estrangeiros". Only the split of
"Camara dos Pares / Arroio / divorciado" over three groups is ours.

> Hoje, na Camara dos Pares, Arroio, divorciado de todos, [veio] interpellar o Ministro dos Estrangeiros acerca da
> viagem [de] V. M., fazendo referencia [á] ausencia [das] auctoridades [em] Livorno [?] e [á] falta [de] visita [do]
> Presidente da Republica Franceza. O Ministro dos Estrangeiros [veio] contestar [?], [ser] falso boato, referindo os
> factos em termos convenientes. Hintze Ribeiro.

"Today in the House of Peers Arroio, at odds with everyone, interpellated the Foreign Minister about Your Majesty's
journey, pointing to the absence of the authorities at Livorno [?] and to the President of the French Republic not
having paid a visit. The Foreign Minister answered that it was a false rumour, setting out the facts in suitable
terms." Arroio is presumably João Arroio, a peer who had broken with Hintze's party [our identification, not checked].
"Livorno" is a hard reading of a smudged word; the last word on the face is "contestar" or "contestou". The marks
". S" around 26541 and the ink number "63276" at the right of line 3 are not explained.

**m0001, 23 Apr 1903** (`m0001_transcription.txt`, `m0001_decryption.txt`). The clear words give the frame: "Agradeço
muito a carta de Vossa Magestade. No [..] [..] das [..] em [..] parece-me [..] ... mas Vossa Magestade [..] ... e
muito dedicadamente beijo a sua mão. Hintze Ribeiro." ("I thank Your Majesty very much for your letter ... most
devotedly I kiss your hand.") **One group is read** from the decoded telegram: 41285 = Vossa Magestade. The first
pass counted four; the other three (57136 seu, 53803 regresso, 67394 Lisboa, "no seu regresso a Lisboa") are guesses
from position and the code's order, and are not used in a reading. Its guess "França" for 49638 is dropped: it rested
on 49641 = franceza, which the page model puts in doubt.

## 4. The code (`code_values.tsv`, `python code.py`, output in `code_output.txt`)

- **24 values** from the decode, plus 3 guesses for m0001 marked as such. Groups under 10000 are sent with four
  figures; all 54 groups lie between 1347 and 67398, so the book probably has fewer than about 70,000 entries.
- **Order: alphabetical within page blocks (a hypothesis).** The raw rank correlation of group number with the alphabetical order of
  the value is 0.57. Read each group as page (n // 100) and line (n % 100), and reflect the pages below a split
  (best at 375) while keeping the lines in order: then 21 of the 24 values fall in alphabetical order (rho 0.957).
  Shuffling the 24 words and giving chance the same choice of split reaches a median of 0.275 and a maximum of 0.746
  in 2000 runs, so the model is not a fit to noise (P < 1/2000). The lower, reversed half holds a-h, the upper half
  i-v; Livorno sits in a high block (67398), perhaps for names. The model was found after the fact on these 24 values,
  with a fitted split, so it stays a hypothesis; more decoded traffic in this code would test it.
- **What the model says about the decode.** It supports the doubtful words: divorciado falls among the d-words,
  contestar among the c-words, Arroio among the a-words (so the encoder used the common noun *arroio* for the name).
  3707 ("da Rep.") and 49641 ("franceza") are out of order; the model would rather make 3707 = franceza and 49641 a word
  between ministro and presidente (an unwritten "o" before "Ministro"?). Not adopted; the decode's split is kept.
- **m0001 under the model** (`code.py`, part 4): every open group but one (35512, below acerca) is bracketed between two decoded values. "No 34648
  7684 das 22922 em 67033" would be an a-word, an e/f-word, a c-word and a name (for instance "No actual estado das
  coisas em [place]" [guess]). The brackets are too wide to read the telegram.
- **Not the code of the sibling folders.** No group is shared with King Carlos's code (`targets/carlos1903`),
  Sabugosa's (`targets/sabugosa1910`, which is alphabetical but runs differently), Manuel II's of 1910
  (`targets/manuel1910`) or Venceslau de Lima's two-part code of 1909 (`targets/lima1909`).

## 5. Prior work

- The decode of m0003 is on the form, so its reading is not new. One web search (Arroyo, Câmara dos Pares, May 1903,
  the Queen's journey, Livorno, Loubet) found only general literature on the 1903 journey
  (https://repositorioaberto.uab.pt/entities/publication/5aeeede3-d055-4254-bed2-b88d8c1d459c) and no print of these
  telegrams or of the interpellation. The Diário da Câmara dos Pares of about 11 May 1903 should confirm the day and
  the words Livorno, contestar and divorciado; it was not consulted.
- Context pointer, not checked: `targets/sabugosa1910` has a Lisbon -> Naples telegram of 24 April (m0016) dated 1904
  from its decode ("24-4-04"); this unit puts the Queen at Naples on the yacht on 23 April 1903.

## Corrections to catalogue entry 406

- Date "before 1907 (catalogued 1913)", year 1906: the telegrams are of 23 Apr and 11 May 1903.
- Place "unknown": Lisbon -> Naples (the yacht *Amélia*) and Monte Estoril -> Paris (Hotel Bristol).
- "presumably during a regency": they were sent to the Queen during her Mediterranean journey of spring 1903.
- Status: the May telegram carries a decode of the time.

## Independent verification by Brice Dudout (PR #572, 14 Nov 2026)

Brice Dudout (PR #572, `VERIFY_dudout_20261114.md`, `verify_dudout_20261114.py`) re-read all 54 groups of m0001 and
m0003 and the decode of the time on the four DigitArq images: no difference from the transcriptions; *divorciado* and
*contestar* legible, *Livorno* still doubtful. His script re-derives the telegraph word counts (75 and 46), applies
`code_values.tsv` to m0003 (25 of 25 groups as published) and refits the page model: rho 0.957, 21 of 24 in order, 500
shuffles at most 0.697. Re-run here: same figures. The images were not fetched again here.

His proposal for the two groups out of order, recorded and not adopted: 50554 = *Presidente da Republica* as one
phrase, 3707 = *franceza*, and 49641 = the full stop the decoder wrote after *franceza* (a word such as *ponto*, which
falls between *ministro* and *presidente*). It takes the decode unit for unit, needs no unwritten word, and puts 23 of
24 values in order (rho 0.969; 23 of 23 without Livorno). It replaces the "unwritten o" idea of section 4 as the
better guess; the values of `code_values.tsv` are unchanged, since nothing but the page model speaks for it. He also
notes that the three highest groups (67033, 67394 in m0001 after *em* and *a*, and 67398 Livorno) look like a block of
place names at the end of the book, which supports 67394 = Lisboa as a guess.

Read share of m0003. All 25 groups have a word in the decode of the time, but two of the 46 words of the telegram are
doubtful readings of the ink (Livorno, contestar). Counting sure words only, 44 of 46 = 0.957; `read_share` now carries
that in place of 1.0. It stays read. (`v10_relabel.measure` gives 0.793 on `m0003_reading.md` because it also counts
the ten articles and prepositions supplied in brackets for the English reader as holes; they are not in the telegram,
so they are neither read nor unread.)

## Remaining gaps

- m0001, 28 of 29 groups (Lisbon -> Naples, 23 Apr 1903) - blocker: no-key-material; no decode in M15, only 41285 recurs in m0003, the page model brackets the others but does not fix them, and the codebook was not found
- m0003, the split of 24724 29878 11876 and the doubtful words 67398 Livorno and 18148 contestar - blocker: illegible; smudged ink, and the Diário da Câmara dos Pares would decide

## Escalation

- [x] siblings: all four images of M15 examined; the only decode is on m0003-m0004
- [x] clear-pages: m0001's clear words frame its groups; no decode on its back
- [x] known-keys: the codes of carlos1903, sabugosa1910, manuel1910 and lima1909 compared; no group shared
- [x] print: one web search; no edition of these telegrams found; the Diário da Câmara dos Pares not consulted
- [x] key-rebuild: 24 values; page model of the order found and tested against shuffles; m0001 bracketed
- [x] retry: every m0001 group re-bracketed under the page model (code.py, part 4); none is fixed. More decoded
  telegrams of Hintze Ribeiro in this code, or the codebook, would read m0001

## Files

- `m0001_transcription.txt`, `m0001_decryption.txt` (one value, brackets and guesses)
- `m0003_transcription.txt`, `m0003_contemporary.txt` (the decode of the time), `m0003_decryption.txt`,
  `m0003_reading.md`, `m0003_en.md`
- `code_values.tsv`: 24 values from the decode and 3 guesses; `code.py`, `code_output.txt`

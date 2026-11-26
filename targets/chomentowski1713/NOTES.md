# Stanisław Chomentowski at the Porte to Hetman Sieniawski, 1713-1714, in a three-digit syllabary (DECODE R7476, R7484, R7485)

Status: read in part (written up 9 Oct 2026 in sieniawski1708, own entry 14 Oct 2026)
**22 Oct 2026, reading audit:** the per-document grade C on R7484-R7485 was overturned to A: R7484 reads with scattered holes, and in R7485 the cipher passage reads in full; its holes are in the faint clear body, and pp. 116-117 are clear text, not cipher.


**Split on 14 Oct 2026** from `sieniawski1708` under the one-key rule (George Lasry, 14 Oct 2026). These three letters
share one syllabary; the letters once filed with them are in other keys and have their own entries and pages (a
different cipher in each): [`sieniawski1708`](../sieniawski1708/NOTES.md) (key A), [`turculet1709`](../turculet1709/NOTES.md)
(key B), [`r7475`](../r7475/NOTES.md) and [`schenck1706`](../schenck1706/NOTES.md). The work below was done on 9 Oct 2026
and is carried over from the sieniawski1708 NOTES; `R7476*`, `R7484*`, `R7485*` and `syllabary.tsv` moved here from
`sieniawski1708/sien/` on 14 Oct 2026 (the files still cite their old `sien/` paths).

## The documents

- **R7484, R7485** = Archiwum Narodowe w Krakowie, Zbiór Dzieduszyckich **24/11 no. 116** (not 26/32; DECODE
  "Krakow_UNK_3/4", no description): Chomentowski, voivode of Mazovia, envoy at the Porte, to Sieniawski, Adrianople
  9 May 1713, and an undated second letter (1713); R7485's cipher passage also written out in clear at the head of the
  page.
- **R7476** (Zbiór Dzieduszyckich 26/32 nr 13 pp. 31-34, catalogued with the Brâncoveanu letters): probably
  Chomentowski; code XVIII is glossed "Hospodar Multański", Brâncoveanu, in Yedikule from April 1714, so the letter is
  **May-August 1714, Constantinople** (first dated c. 1712-13).

Not printed by Kaczka 2012.

## The cipher

A three-digit syllabary, dot-separated, clear words between, glossed syllable by syllable. Its codes run in
alphabetical bands (a 6-8, b 14-21 ... z 320-333), names such as Cesarz 42, Moskwa 160, Turcy 271 heading their band
(`syllabary.tsv`, rebuilt from the glosses of the three letters).

## Readings (9 Oct 2026)

- R7484, R7485 checked token by token against gloss and key (`R7484_pass2.txt`, `R7485_pass2.txt`): R7484 492/513
  (three clear date figures taken out of the count), R7485 96/96. Slips settled (191 for 181 in "Hanowi", 160 = Moskwa
  not 169).
- R7484 pass 3: code 76 = ferman (glosses "F[e]rmana", "farman"; f band 70-78; R7476 "dano ferman"), "co im ferman i
  wbijają", "stambulscy" (37 = cy): **495 of 513 = 96.5%**. Open, 18 tokens: "umowi-ia t-r-ze-y s-za psuje" (7) and
  "ta ... s-fi-d-no" (5) whose syllables are certain but form no word found; code 112 (gloss a flourish, illegible at
  3.5x); "c-wo-ko-wa-ni" (5).
- R7476: faint glosses re-read at high contrast (34 crops, `R7476_pass2.txt`), then a language pass with the
  syllabary's bands: 88.5%. Passes 4-6 (`R7476_pass5.txt`, `R7476_unresolved.txt`): the bad stretches re-transcribed at
  2.5-3x digit by digit (the closed 7 read as 4 six times, 51/61, 107/47, 245/243, 249/240, 163/168, 236 = 280), the
  glosses re-read, Polish words scored with lang/ pl-modern, names checked against Perłakowski 2020 on the embassy
  (Jan Spiegel = "Pan Szpigieł", Franciszek Goltz). New: "on z tąd nie ruszy, póki mu Porta nie da takiego konwoju",
  "trzysta lwowych na drogę", "z listu przejętego", "sołtan gałga uciekł do Czerkies", "a wekslowe kupcy nie chcą
  płacić", "donieść Jmci Panu Kanclerzowi Koronnemu"; codes 135 = Kanclerz, 215 = Porta, 280 = u, 310 = x added to
  syllabary.tsv: 1,531 of 1,621. Pass 7 (language only: Ottoman/Tatar terms, Latin, old spellings, one encipherer slip
  per word): "traktatu od Porty" (215, not 245), Latin "którą on renuebat", "rzeczy(?) królewskich" (240 for 230):
  **1,538 of 1,621 = 94.9%**, 2 tokens short of the bar; nothing forced.
- Together: 2,129 of 2,230 tokens (95.5%); per document R7476 read in part, R7484 and R7485 read.

## 23 Oct 2026: verification 3 (explicit-hole score)

The v3 sweep scored `R7476_reading.txt` whole, English header and pass/measure notes included (0.578 explicit-hole).
`## Reading` and `## Notes` headings now frame the body; the body scores 0.651 explicit-hole (41/63 sentences, hole
rate 0.104; 0.694 without page labels and the postscript line), plain 0.143 (small Polish word list). Keeps read.
Note for a later pass: this reading is in modernised spelling (pass 3); the letter-for-letter text is
`sien/R7476_pass5.txt`.

## 23 Oct 2026 (r2b): R7476 restored to the writer's spelling; demoted to decoded, not read

The R7476 reading of 9 Oct (pass 3) was in modernised Polish, which the reading rules forbid. `R7476_reading.txt` now
gives each word as its figures carry it: clear words exactly as transcribed ("y", "poniewasz", "lepiey", "nisz",
"niey", "zwyczayna"), code words as glossed, else as keyed ("ongi", "kihai", "bawio", "chco", "z tod", "puki",
"bespiecznie", "zemby ostrzo", "Ozowa", "odpowiedzielem"). Method: `research/reading_audit/r2b_chom_stream.py` parses
`R7476.txt` into code/gloss/key streams, `r2b_chom_restore.py` aligns the pass-3 reading with them letter by letter and
re-spells each word; then a line-by-line hand check (`R7476_reread_log.md`). Five readings improved from the figures
(p.31 "ongi" for "onegdy"; p.32 "na swoie panstwo", "ktoro on", word code "wozy"; p.33 "odpowiedzielem"). The "(?)"
words became `[?word]` and letters no figure carries are bracketed (przyi[ą]ł, m[u] for the slip 156 mo, ...).
Modern spelling is only in the new English translation `R7476_en.md`.

Score (`research/reading_audit/v2_score.py`): explicit holes **0.651 -> 0.524** (33/63 windows), plain 0.079, hole rate
0.143. Below the 0.60 bar once the doubtful words count as holes, so R7476 is **decoded, not read**, its reading kept as
a partial reading. `fraction_read` 0.955 -> 0.273 (tokens of the documents that read: R7484 + R7485, 609 of 2,230).
R7484_reading.txt and R7485_reading.txt are also in modernised spelling and still need the same restoration.

## 23 Oct 2026 (r2k): R7484 and R7485 restored to the writer's spelling; both keep read

`R7484_reading.txt` and `R7485_reading.txt` (9 Oct, modernised Polish) re-spelt by hand from the C/G lines of
`R7484.txt`/`R7485.txt`, the syllabary and the slips settled in passes 2-3 (`R7484_reread_log.md`). Each code by its
value: where the glosser normalised the writer's o to a nasal the figure is kept ("mowio", "widzoc", "bedoc", "dotod",
"poczoł", "chcoc", like R7476's "bawio", "chco"); 330 = "ze"; clear words as transcribed; slips bracketed ("na na[s]",
"po[te]ntie", "[po]ydo", "Han[o]wi", "wo[ła]ia", "pi[e]r[w]sza"); "(?)" -> [?word]; the 9 Oct guess "zwokowani"
withdrawn ("Stambułsci [...]"); R7485's "[Han]" dropped from the reading (only in the gloss). English only in the new
`R7484_en.md`, `R7485_en.md`. Score (`v2_score.py`, explicit holes): R7484 0.75 -> 0.739 (17/23, hole rate 0.094),
R7485 0.889 -> 0.75 (6/8): both keep read; `fraction_read` unchanged 0.273. The gap blocker "open-codes" (not an allowed
blocker) is now no-key-material for the R7476 and R7484 word residues: values certain, no outside text gives the word.

## Remaining gaps
- R7476: the reading as a whole is decoded, not read (0.524 explicit-hole share, 23 Oct 2026; about 40 [?word]s on p.31 L19-34 and p.32 L9-36) - blocker: illegible; the doubtful words sit under glosses unreadable at 3-3.5x on the DECODE JPEGs or whose letters form no certain word
- R7476: 67 of 1,621 tokens - blocker: no-key-material; letters known from gloss or key but no word, after seven passes (digit re-transcription at 3x, band alternatives, Ottoman/Latin/old-spelling candidates, LM scoring)
- R7476: 8 tokens in names (p. 32 L9-10, code 216) - blocker: no-key-material; glossed syllables, no matching name in the embassy literature
- R7476: 5 one-off codes 2, 224, 266, 299 x2 - blocker: no-key-material; no gloss, no band value
- R7476: 3 tokens - blocker: illegible; margin number p. 31 L32, stroke p. 32 L13, gloss over code 112 at 3x
- R7484: 17 of 513 tokens - blocker: no-key-material; three short passages (p.111 L3-4, p.111 L10, p.113 L6) whose syllables are certain but whose words are not recovered; no sibling, print or other gloss gives them (r2k, 23 Oct 2026: re-spelt, still open)
- R7484: code 112 (1 token) - blocker: illegible; its gloss is a flourish unreadable at 3.5x, and its only other occurrence (R7476) is also illegibly glossed
- R7485: the faint pale-ink clear body, pp. 115-117 (not cipher) - blocker: illegible; very faint with show-through on the DECODE images

## Escalation
- [x] siblings: R7484/R7485 used for R7476's vocabulary; the other Sieniawski records are in other keys
- [x] clear-pages: R7485's clear copy at the head of the page used
- [x] known-keys: keys A, B and the R7475 table compared: different systems
- [x] print: Kaczka 2012 does not print them; Perłakowski 2020 on the Chomentowski embassy used for names
- [x] key-rebuild: syllabary rebuilt from the glosses and its alphabetical bands used to bound values
- [x] retry (23 Oct 2026): R7476 re-spelt from its figures and aligned word by word with the token stream (r2b); doubtful words marked; rescored 0.524, demoted
- [x] retry: R7476 glosses re-read at high contrast, unread stretches re-transcribed digit by digit at 3x (passes 4-6); R7484 pass 3 at 3.5x; Polish candidates scored with lang/ pl-modern
- [x] retry (23 Oct 2026, r2k): R7484 and R7485 re-spelt from their figures, slips bracketed, aligned word by word; rescored 0.739 / 0.75, keep read

## 24 Nov 2026 - R7476 p. 32, the twin digits 4 / 7 checked by a blind reader (Brice Dudout, with Claude), `dudout/`
A blind sheet of 11 questions (8 targets, 3 controls, 3/3) separates an angular 4 from a hooked figure, the hand's 7.
Three digits transcribed 4 are the hooked 7: p.32 L13 141 -> 171 (na: "wyjeżdżał na"), L24 244 -> 247 (sa: "samego"),
L25 240 -> 270 (t, no letter change); "[?od]" at L24 is probable (cut by sense). Tokens read 1,538 -> 1,542 of 1,621
(95.1%; 1,544 with [?od]); no read word breaks. The explicit-hole score (0.524, 23 Oct 2026) was not re-run, so the
state of R7476 is unchanged. The key is unchanged; the 4/7 conflicts in syllabary.tsv need a visual pass first.
Details in `dudout/README.md`; no image is committed.

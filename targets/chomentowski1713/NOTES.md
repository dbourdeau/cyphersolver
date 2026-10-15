# Stanisław Chomentowski at the Porte to Hetman Sieniawski, 1713-1714, in a three-digit syllabary (DECODE R7476, R7484, R7485)

Status: read in part (written up 9 Oct 2026 in sieniawski1708, own entry 14 Oct 2026)

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

## Remaining gaps
- R7476: 67 of 1,621 tokens - blocker: open-codes; letters known from gloss or key but no word, after seven passes (digit re-transcription at 3x, band alternatives, Ottoman/Latin/old-spelling candidates, LM scoring)
- R7476: 8 tokens in names (p. 32 L9-10, code 216) - blocker: no-key-material; glossed syllables, no matching name in the embassy literature
- R7476: 5 one-off codes 2, 224, 266, 299 x2 - blocker: no-key-material; no gloss, no band value
- R7476: 3 tokens - blocker: illegible; margin number p. 31 L32, stroke p. 32 L13, gloss over code 112 at 3x
- R7484: 17 of 513 tokens - blocker: open-codes; three short passages whose syllables are certain but whose words are not recovered
- R7484: code 112 (1 token) - blocker: illegible; its gloss is a flourish unreadable at 3.5x, and its only other occurrence (R7476) is also illegibly glossed

## Escalation
- [x] siblings: R7484/R7485 used for R7476's vocabulary; the other Sieniawski records are in other keys
- [x] clear-pages: R7485's clear copy at the head of the page used
- [x] known-keys: keys A, B and the R7475 table compared: different systems
- [x] print: Kaczka 2012 does not print them; Perłakowski 2020 on the Chomentowski embassy used for names
- [x] key-rebuild: syllabary rebuilt from the glosses and its alphabetical bands used to bound values
- [x] retry: R7476 glosses re-read at high contrast, unread stretches re-transcribed digit by digit at 3x (passes 4-6); R7484 pass 3 at 3.5x; Polish candidates scored with lang/ pl-modern

# Ferenc Rákóczi II to an envoy bound for Holland, Lwów, 27 June 1711 (DECODE R483)

Status: read (23 Oct 2026, re-reading): R483 written out in reading order from the clerk's interlinear decipherment and the clear passages, checked with the rebuilt key (`R483_reading.md`, grade B).

**23 Oct 2026, re-reading** (REREAD_BRIEF batch b33; log `R483_reread_log.md`): the letter is written out as one
running Latin text (`R483_reading.md`, English `R483_en.md`): the clerk's interlinear stretches and the clear passages
interleaved as they stand in each line (`research/reading_audit/b33_rk_merge.py`), every clear word and every doubtful
interlinear word re-read on the six DECODE images (strips and zooms, `b33_rk_crop.py`), and the clerk's doubts settled
group by group with the rebuilt key (`b33_rk_dec.py`); 72 changes in `R483_corrections.tsv` (*ab inimicitiis* for *ab
Armistitiis*, *inimicitias suas* for *amicitiis fidis*, *tranquillos reddat animos* for his letter-by-letter
*Transi- l w s re d da*, *Tabellarius denegato responso*, *copialiter annexus*, *domino Jablonski* for *Fablanski*,
*cellario regio*; *juramento suo*, which the clerk skipped, restored from the figures). Clean-sentence share: before
0.311 plain (`R483_clerk.txt`), after **0.889 (88/99) counting explicit holes**, 0.141 plain (the Latin word list
rejects *ob*, *sincere*, *acceptare* and chancery words). No supplied word; look-alike letters 0. It reads: decoded,
not read -> read (grade B); class not read -> read; method read from existing decipherment; fraction_read 0 -> 1.0.
Print: not in Thaly's *Archivum Rákóczianum* I/3 (letter-books 1710-1712, MEK 18829, searched in full text); its no. 44
to Klement on the fiscal wines Hegyi was to deliver to the King of Prussia's man is the affair of p. 6, so the
addressee is probably Mihály Klement.

**22 Oct 2026, reading audit** (George Lasry's test: can sentences be built and translated?): R483_clerk.txt merges the clerk's interlinear decipherment with the clear passages line by line, out of reading order, with "?" doubts or alternatives on most lines; the themes can be followed but many sentences are only half secure: R483 is *decoded, not read*. Class read -> not read, method read from existing decipherment -> not solved until the text is written out; fraction_read 0.997 -> 0.

Earlier status (before the 22 Oct 2026 reading audit): read. Rákóczi's own Latin letter, in a syllabic cipher with homophones, carries a contemporary interlinear
decipherment over every ciphered stretch (2,524 of 2,531 groups lie under it; measured 14 Oct 2026). Its key, not
preserved, was rebuilt here from that decipherment: 224 codes, which reproduce 70% of the clerk's letters.

Split on 14 Oct 2026 from `rakoczi1704` under the one-key rule (George Lasry, 14 Oct 2026). Until then this letter
was filed with three French reports *to* Rákóczi (R852, R912, R922; catalogue item 44, DECODE author "Rákóczi"),
which use the Bonac–Groffey nomenclator DECODE R639. Those are [`targets/rakoczi1704/`](../rakoczi1704/NOTES.md) (a
different cipher, with its own page). The work below was done in the rakoczi1704 session of 21 Sept 2026 and is
carried over from its NOTES; the R483 files moved here on 14 Oct 2026.

Work date: 2026-09-21. Catalogue item 44 (class B), removed from the catalogue when the four letters were read.

## The document

MNL OL P237 Festetics 10. d. 2. 42–44, 6 pp.; DECODE R483 (images 3666–3671, git-ignored, in the main checkout's
`targets/rakoczi1704/img/` and `.worktrees/rk2/rakoczi1704/img/`; shared source folder, not moved). DECODE's text
transcription `DOC_R483_D2172_2172.txt` stays in `../rakoczi1704/`, where `decode.py` uses it as the control for R639.

2,531 cipher groups in 180 lines, transcribed from the images (`tr/R483_p1.txt`–`p6.txt`), with the clerk's
interlinear on the `P:` lines and clear passages in `{clear: …}`. The letter is signed in autograph "Franciscus
Princeps" and dated in clear "Leopoli die 27. Junii Anno 1711". DECODE's "7 June" is wrong. It is addressed to
"Fidelis nobis sincere dilecte", an envoy on his way to Holland who is in poor health and handles money and the
mathematical instruments ordered from Mangold. A clear postscript deals with those instruments.

Cipher and clear alternate within the lines. The R639 table gives nonsense on it (control, 21 Sept 2026): a different key.

## The interlinear and the key

The clerk wrote the decipherment above every ciphered stretch. Measured 14 Oct 2026 over `tr/`: 2,524 of the 2,531
groups sit on a line with an interlinear; the seven without are a one-group word ending carried to the next line
(430 = -s of *Supprimimus*), a three-group catchword at the foot of p. 4 repeated at the head of p. 5, and three
groups opening a p. 5 line whose words the clerk wrote on the line above. The clerk's doubtful words are marked `?`
in the transcription.

**Key rebuilt.** `align483.py` aligns every cipher line with the interlinear by hard EM, with each code taking
0–4 letters. 168 lines align (23 skipped as ill-fitting). It gives 224 codes (`R483_key_rebuilt.json`), 156 of them
seen at least twice. It is a syllabic cipher with homophones: single letters (190/430 s, 140/380 n, 60/300 e,
20/260 a, 130/370 m), open syllables (257 re, 428 ti, 68 se, 362 de, 96 no, 457 ri, 148 si, 92 ce, 152 co, 59 tu,
378 ta) and a few words and names. Decoding with the rebuilt key (`check483.py`, output `R483_key_read.txt`)
reproduces 3,180 of the clerk's 4,547 letters (69.9%; rerun 14 Oct 2026 after the move, output unchanged). The
mismatches are rare codes, homophones seen once, and the clerk's own abbreviations. Where the clerk's words are
doubtful, the key often settles them: "nos Regem extra dietam promulgatum non deposito [juramento] agnoscere non
posse sine … ruina [libertatum nostrarum]", and "ne fors etiam".

## Content

P. 1: Rákóczi sends a copy of the "Tractatus sic dictae Pacis Carolianae" (Szatmár), which he calls a fraud
engineered in Vienna, and reports that Archduke Charles was proclaimed king in every Hungarian county, contrary to
the 1687 article of the Pozsony diet. P. 2: he will not recognise a king proclaimed outside a free diet. He appeals
to the Tsar and the Polish Republic to mediate. He offers to come to a free diet in person or by plenipotentiaries
and to recognise a lawfully crowned king, provided the confederates are restored to their estates. P. 3: the
Allies' assurances about Hungarian liberties were a "diversio armorum" for Austria, and the war must go on. P. 4:
Pálffy's artillery against "arcem nostram Munkatsiensem", and the restitution of Transylvanian liberty. P. 5: the
general confederation in Poland, letters to go "per Saxoniam", the Muscovite advance, a warning to trust only news
sent directly from Rákóczi, complaints about the Grand Chancellor's "indiscretum procedendi modum" and about Ráday,
and letters from the Chancellor at Dukla. P. 6: receipts left with a Jew, and a member of the Economic Council who
took treasury money for his own use.

## Outcome

Read from the existing (contemporary interlinear) decipherment, which covers 99.7% of the cipher groups; the key was
rebuilt from it and checks it. Since 23 Oct 2026 the letter is written out as a running Latin text with an English
translation (`R483_reading.md`, `R483_en.md`, grade B). Open: five words of the p. 1 clear opening and about a dozen
doubtful words on single-occurrence key groups. The key's single-occurrence codes (68 of 224) are grade C. The
recipient is unnamed in the letter; probably Mihály Klement (see the 23 Oct block).

## Files

- `R483_reading.md`, `R483_en.md` (23 Oct 2026): the reading in reading order and its translation;
  `R483_reread_log.md`, `R483_corrections.tsv` (changes to the clerk's and the clear-text transcription). Helpers in
  `research/reading_audit/b33_rk_merge.py`, `b33_rk_dec.py`, `b33_rk_crop.py`.
- `tr/R483_p1.txt`–`p6.txt`: transcription from the images, interlinear on `P:` lines.
- `align483.py`: hard-EM aligner, writes `R483_key_rebuilt.json`. `check483.py`: decodes with the key and compares
  with the clerk, writes `R483_key_read.txt`.
- `R483_clerk.txt` (14 Oct 2026): the clerk's interlinear merged with the clear passages, line by line, from `tr/`;
  the reading queued for DECODE.
- In `../rakoczi1704/`: `DOC_R483_D2172_2172.txt` (DECODE's transcription), `R483_key08_read.txt` (the R639
  control), `fetch_decode.py` and `fetch_img.py`.

## Remaining gaps

R483 as a running text is closed (23 Oct 2026, `R483_reading.md`, read, grade B); what is left:
- R483 p. 1 clear opening, five words (*Supponimus redditas jam [...] ... abunde [...] [...]nistris*) - blocker: illegible; fast cursive not settled on the DECODE images at 2x, a higher-resolution MNL OL scan is the way on
- R483, about a dozen doubtful words where the clerk's hand and the key decode disagree (*[?concludendam]*, *[?remediationis]*, *[?possidere]*, *[?commisso]*, *domino Jablonski [...]*) - blocker: no-key-material; the groups are seen once or not at all in the rebuilt key

## Escalation

- [n/a] siblings: no other letter in this key
- [x] clear-pages: the clerk's interlinear decipherment over every ciphered stretch; written out in reading order 23 Oct 2026
- [n/a] known-keys: the key is not preserved
- [x] print: searched 23 Oct 2026: web search for the letter's phrases; Thaly, Archivum Rákóczianum I/3 (letter-books 1710-1712, MEK 18829) full text searched for Mangold, Spiegel, Jablonski, Dukla, Pax Caroliana and every June-July 1711 dateline: not printed there (related order to Klement, no. 44)
- [x] key-rebuild: 224 codes rebuilt from the interlinear; used 23 Oct 2026 to settle the clerk's doubtful words
- [x] retry: re-read on the images 23 Oct 2026 (`R483_reread_log.md`)

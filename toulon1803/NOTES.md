# Toulon to Van Hogendorp, 30 July 1803 — DECODE R2034

Status: attempted, open (closed from the evidence 22 Sept 2026: the key survives only as a physical booklet,
NA 2.21.045 inv. 34313, not digitised; fresh full transcriptions of the same-key 1801 letters R1944 and R1946 fix
only 2 of R2034's 67 words with confidence, 222= niet and 394 handen, plus 58 brengen at medium confidence. The nine
"secure" values claimed on 20-21 Sept are withdrawn; see "Session of 22 September 2026" at the end.)

## Source

- Ciphertext: DECODE R2034, Nationaal Archief, The Hague, 1.02.13 (Legatie Rusland), inventory 208.
- The authenticated DECODE image was acquired as `IMG_R2034_I14728_P1.png`; `R2034_upright.png` is the lossless upright rotation.
- Clear text: “Den Haag 30 July 1803”, “Burger Minister!”, and the closing “Heil en Hoogachting! L. van Toulon”.
- The numerical body is transcribed in `ciphertext.txt` (110 groups).

## Key identification

The exact key survives. Nationaal Archief 2.21.227, item 335, describes a *Correspondentiecijffer* annotated:

> eerst voor den minister van Grasveld in anno 1799, nu in anno 1801 voor den Minister van Dedem, met de Ministers der Bataafse Republiek te Parijs en in Spanje … voor den Minister van Hogendorp te Petersburg 1803

The same object is described in the Croiset family archive, Nationaal Archief 2.21.045, inventory 34313 (old number 5187): a ten-page booklet with six written pages, instructions, and six loose sheets of code notes. The physical original was deposited with the Nederlands Postmuseum / Museum voor Communicatie (registration B1 392); the Nationaal Archief holds a photocopy. The catalogue currently marks it **PHYSICAL**, with no online scans.

The six written codebook pages explain the six series in the letter: unmarked numbers and numbers marked by a wave, caret, double stroke, overbar, or plus. Values range from 1 to 992. This is therefore an ordered dictionary code: the mark identifies the codebook page/series and the number identifies an entry.

## Same-key traffic

DECODE R1942 is a two-page dispatch from Dirk van Hogendorp in St Petersburg to Maarten van der Goes, 5 July 1803 (NA 2.01.08, inventory 318). Its numerical groups use the identical six marks and range, so it is almost certainly traffic under item 34313. Its scans and prepared crops are in `../R1942/`. It supplies several hundred additional tokens for joint analysis.

DECODE R1944 (Etienne Bourdeaux, Berlin, 31 January 1801) is another strong candidate: its date and correspondents match the 1801 Dedem/Paris/Spain phase of item 34313, and DECODE notes that its nomenclator was probably devised by S. E. Croiset. Its two authenticated scans use the same six superposed marks as R2034.

More importantly, the immediately following Bourdeaux dispatches R1945 (3 February 1801) and R1946 (7 February 1801) are marked **decrypted** and include contemporary plaintext solution sheets. Their authenticated scans are now downloaded and rotated. They are same-key ciphertext/plaintext pairs for reconstructing item 34313. R1946 is now aligned across all 158 plaintext words, and R1944's misplaced solution is also aligned far enough to recover exact target entries. See `related_plaintext_pairs.md`.

The meaningful part of R2034 ends at group 69, `763~ = Einde des briefs`; groups 70–110 are deliberate random padding.  Directly verified target readings are currently:

`51~ = van` (groups 10, 39, and 62), `279 = en` (24),
`153 = Paul` (30), `222= = niet` (52), `43~ = zyne`
(53), `304~ = wegens` (58), and `380~ = de` (59).

These readings account for the start control which precedes the plaintext in
R1944–R1946.  Omitting that control shifts every apparent mapping by one and
produces false readings such as `51~ = men` and the impossible target sequence
“het Heer”; those provisional values have been withdrawn.

The target transcription was also corrected from `120` to `120~` after
reinspection of the authenticated image.

## Related but different key

DECODE R1891 is Croiset's small (under 500 entries) codebook for R. J.
Schimmelpenninck, Museum voor Communicatie inventory 34312. Its catalogue note
mentions later temporary reuse, but the photographed table cannot be R2034's
1–999, six-mark key. It remains a constructional analogue, not the target
table. R1925 is a decrypted 1799 letter using that related codebook; the
separate contemporary solution survives.

DECODE R1035, Nationaal Archief 1.02.13 inventory 228, is also **not** the target key. It is the much larger, seven-series codebook signed at The Hague on 5 August 1803, six days after R2034. Direct manuscript lookup was tested rather than inferred from metadata. It turns the opening groups into the disconnected sequence `ing | beh | hoe | voor | plus | ...`, and the following groups remain random Dutch/French dictionary entries. Several spot checks are unambiguous in the photographed number columns (for example `430~ = ing`, `336~ = beh`, `501 = hoe`, `1+ = voor`). This is a decisive negative control, not a partial reading. The apparent match `763~ = Einde des briefs` is a retained conventional control group shared by the related system; it does not make the vocabulary tables identical.

The R1035 instructions explain the random material before a `Begin des briefs` control and after an `Einde des briefs` control, but none of its six start controls (`404~`, `27"`, `847"`, `713^`, `325`, `17+`) occurs in R2034. That independently rules out R1035 for this letter.

## Prior-art checks

- Exact-name and exact-date web searches found no published decipherment.
- Searches of Satoshi Tomokiyo's Cryptiana index/domain found no Toulon, Hogendorp, or Batavian match.
- The printed 1943 *Correspondentie van Dirk van Hogendorp met zijn broeder Gijsbert Karel* concerns his brother and does not surface this official letter.
- J. A. Sillem's 1890 biography identifies several numbered ciphered dispatches by Hogendorp, but contains no 30 July letter from Toulon and no decipherment of R2034.
- Florentijn van Kampen's HistoCrypt 2026 reconstruction and repository concern the later inventory-228 codebook and its 1806-1810 traffic. They were checked in full and provide the decisive ruled-out comparison above, not the plaintext of R2034.

## Present result and next attack

R2034 is now securely transcribed and its key is identified archivally, but the plaintext is **not yet read**. A claimed plaintext based on R1035 would be false. The physical key remains offline, but the discovery of R1945 and R1946 provides a new recovery route from same-key known plaintext.

DECODE's authenticated record API adds a useful subject constraint: its
cataloguer notes that a private letter sent by the cipher clerk in his own
name is highly unusual and that the short message "can only pertain to matters
of encryption."  This also fits the replacement St Petersburg nomenclator
dated 5 August 1803, six days after this letter, but it is not itself a
plaintext recovery.

### Ruled-out digitized-key candidates

- DECODE's catalogue contains only three plausibly relevant Dutch key records for this period: R1891 (the much smaller 1798 Schimmelpenninck key), R1035 (the replacement St Petersburg nomenclator signed 5 August 1803), and R1038 (a 1765 St Petersburg nomenclator). There is no separate hidden catalogue entry for Croiset item 34313 / old number 5187. DECODE R5187 is an unrelated 1640--1669 Uppsala key.
- The complete downloadable R1038 transcription was tested against the seven secure R2034 anchors. It is not a reused assignment table: no R1038 variant of numeric base `51` means *van*, whereas the 1801 same-key solution fixes `51~ = van`. Other anchors also disagree (for example R1038's base-380 variants include *van* and *de Keizer*, not the exact target assignment `380~ = de`). R1038 is therefore useful only as a structural analogue, not as a decoding source.
- Web searches for the old inventory number `5187`, current Croiset inventory `34313`, the title *Correspondentie Cijffer*, and museum loan number `B1 392` found only the two official Nationaal Archief descriptions. Neither surviving copy has online scans.
- DECODE R1891 is indeed the immediately preceding museum item 34312, but its four image IDs are followed directly by the two images of unrelated R1892; there is no unattached 34313 scan hidden in that upload sequence. DECODE record R5187 is likewise unrelated (a 1640--1669 Uppsala key).
- DECODE R1943 (Valckenaer, 1799) has a surviving French plaintext and was
  tested as another possible known-plaintext source.  It is a different
  assignment table: repetition in its solution independently fixes its
  `907^` group as *sera*, whereas the exact 1803 R1942 quotation fixes the
  target table's `907^` as *zoo*.  Numerical and mark similarity therefore
  reflects the shared Croiset construction, not reuse of the same key.

### Additional same-key quotation recovery

Sillem's biography explicitly cites R1942, dispatch no. 12 of 5 July 1803, for the passage in which Hogendorp calls Vorontsov's attitude *zoo wonderlijk*. The R1942 ciphertext contains the unique adjacent pair `907^ 934"` at that point. This gives high-confidence (not clerk-solution-level) assignments `907^ = zoo` and `934" = wonderlijk`. They fill R2034 plaintext words 50 and 18 respectively.

1. Transcribe and align the contemporary plaintext/ciphertext pairs R1945 and R1946, then apply every recovered group directly to R2034.
2. Finish and independently verify transcriptions of R1942 and R1944 for additional repeated groups.
3. Test all 720 possible orders of the six marked pages under the assumption that the vocabulary is alphabetically ordered.
4. Solve the resulting monotone word-substitution problem jointly across the messages with an early-19th-century Dutch word/phrase language model.
5. If known plaintext and statistics still leave gaps, request digitization of NA 2.21.045/34313 (or 2.21.227/335 / Museum B1 392); the surviving key would make the reading mechanical.

## Files produced in this pass

- `transcription.txt`: 110 code groups with all six superscript marks and the one grammatical trailing dash.
- `R2034_upright.png` and `cipher_crop_2x.png`: inspection derivatives of the authenticated DECODE image.
- `decode_r2034.py` / `decoded_tokens.json`: partial-codebook comparison harness and output.
- `extract_key_cells.py` / `key_context_line*.jpg`: reproducible manuscript lookups used to reject R1035.
- `prepare_related_images.py` / `R1944_*`, `R1945_*`, and `R1946_*`: upright derivatives of authenticated same-key traffic and plaintext sheets.
- `related_plaintext_pairs.md`: provisional transcription and group alignment from the newly found known-plaintext records.

## Session of 21 September 2026: same-key known plaintext exhausted

- **R1945 read in full** (`R1945_transcription.txt`): 187 groups against a 152-word contemporary solution. The opening
  is `871` (start control) `914+ Caraman`, `803+ verzekert`. The earlier table in `related_plaintext_pairs.md`
  (`814+`, `303+`, `719`) misread these. A one-to-one alignment drifts: `273~`, `733~`, `916=` and `977=` each
  recur on different words. So the solution sheet is not a word-for-word match of the cipher (phrase entries,
  omitted words or re-wording). Only one R2034 group recurs with the same mark, `222=`, and it lands near
  "observatie, dat". That is not proof against `222= = niet` (R1946), but the value should be re-checked if
  the key is ever seen. Bases shared with a *different* mark (670, 37, 394, 202, 145, 44, 410, 99) are
  different entries and give nothing.
- **R1946 cipher page 4** (words 1–40) re-read: homophones are in use (Heer = `453=` and `370~`), and none of these
  groups occurs in R2034's meaningful part.
- **The series are not alphabetical** (~ series: 297 Men, 370 Heer, 500 dat, 580 de, 733 zeer, 884 waar), so
  plan items 3–4 (page-order/monotone alphabet solving) cannot work. With 58 of 67 words appearing nowhere in
  the surviving same-key traffic, a language model has nothing to anchor them to.

**Status: in progress. Blocked (offline key).** R2034 stands at 9/67 words. The only way forward is the
physical key, NA 2.21.045 inv. 34313 (duplicate description NA 2.21.227/335, Museum voor Communicatie B1 392):
request a scan.

## Session of 22 September 2026: transcription corrected, 1801 letters re-read, earlier values withdrawn

**R2034 re-transcribed** (`ciphertext.txt`; the 20 Sept version is kept as `ciphertext_2026-09-20.txt`). Ten
groups were misread before: 336~ (not 336^), 897" (894"), 880^ (080^), 859~ (839~), 528- (320-), 145^ (115^),
616+ (666+), 215- (245-), 625- (625"), 188- (180-). The doubtful ones were checked at full zoom. The faint stroke
under 227 is the wave of 909~ in the next line. There are 110 groups, 103 of them distinct. 430~ opens the letter,
763~ closes it at group 69, and the 67 groups between them carry the text.

**R1946 and R1944 transcribed in full and aligned with their solution sheets** (`R1946_transcription.txt`,
`R1946_solution.txt`, `R1946_alignment.tsv`, and the same three files for R1944).
- R1946 (Bourdeaux, Berlin, 7 Feb 1801, no. 20) has 202 groups against a 158-word solution. The alignment is strictly
  one group per word from the start control 357" to word 150. Group 142, 153=, falls on *Paul* and group 151, 222=, on
  *niet*, which confirms it. The groups after "niet" are the end, the end control and 42 padding groups. The
  solution reads "de Heer van **Krudner**", not Lucchesini. Two dots above a figure (e.g. 974 = *De*) are a separate
  mark from the double stroke. The agent merged them into ", which probably explains some of the 13 groups that
  land on two different words.
- R1944 (31 Jan 1801, no. 16; its solution is misfiled as R1946 image 3) has 115 groups against a 77-word solution.
  The subject is a stolen cipher: Rosencrantz's cipher was copied by a servant, the bureau was broken into, and
  Schuez goes to St Petersburg with a new cipher. The alignment is certain only in stretches: 927+ = *Cyffer* (three
  times), 237" = *zyn*, 480^ = *dat*, 335^ = *van*, 453= = *Heer*. Two runs of 13 and 8 groups have no counterpart
  in the solution.
- A spot check of R1946 page 4 line 1 against the image confirms the agent's readings
  (357" 974 453= 444= 429= 81^ 580~ 370~ 957~ 421=).

**The 20-21 Sept anchors do not survive.** Neither full transcription contains 51~, 380~, 43~, 279 or 304~ where
the earlier alignment put them. In R1946, *van* is 444=, 957~, 61~ and others; *de* has many groups; *wegens* is
564~. *Paul* is 153= with a bar, but R2034 has a bare 153 (checked on the image). The earlier table in
`related_plaintext_pairs.md` rested on partial readings that were never saved as transcriptions, and it cannot be
reproduced. Withdrawn: 51~ van, 279 en, 153 Paul, 43~ zyne, 304~ wegens, 380~ de. Sillem's "zo wonderlijk" pair
(907^ 934" in R1942) is kept only as a conjecture. Sillem paraphrases dispatch no. 12, and nothing in the print ties
the phrase to a particular point in the cipher.

**What R2034 now has** (same number and same mark in a solved 1801 letter):

| Group | R2034 position | Value | Source | Grade |
| --- | --- | --- | --- | --- |
| 222- (overbar) | 52 | niet | R1946 word 150, confirmed by the Paul/niet anchors | high |
| 394 | 6 | handen | R1946 word 111 | high |
| 58 | 29 | brengen | R1944, last word of the text | medium |
| 907^, 934" | 51, 19 | zoo, wonderlijk | Sillem paraphrase of R1942 | conjecture |

Groups in R2034's padding also recur: 205- = *gantschelyk* and 458+ = *ook* in R1946, and 239" = *antwoord*. They
confirm that this is the same code, but they add nothing to the text. Same numbers under a different mark are
different entries and give nothing.

**Other leads closed this session**
- R1035 (the 5 Aug 1803 book, Van Kampen's 1,849-entry `Nomenclator.csv`) was tested under all 2,520 assignments of
  R2034's five marks to R1035's six. Coverage is at or below a random-mark baseline (natural mapping 22%, random
  28%). The best mapping's "met Zijne Keizerlijke Majesteit" is one phrase entry (324+) beside two empty cells: an
  artefact. None of the old 1801 values fits any R1035 series either. R1942 is also at chance against R1035
  (25% vs 26%), so its July 1803 dispatch is not in that book.
- DECODE records not yet looked at: R1926 (Schimmelpenninck, London, 28 Feb 1803, decrypted) marks individual
  digits (°, /, ^, bars), so it uses a different key. It is probably of the R1891 kind, 34312. R1947 and R2053 are
  Van Dedem 1789 four-digit letters, and R1033 is Six van Oterleek 1808 in R1035. None is in 34313.
- R1038 (1765 St Petersburg key) was re-tested because its earlier rejection rested on the withdrawn anchors. It
  still fails. Its parsed key (`deswart1782/R1038_key_parsed.tsv`) has no entry for *niet*, *handen* or *brengen*,
  and it marks individual digits rather than whole groups. R2032, R2051 and R2052 are the 1784-86 Rechteren-family
  known pairs (deswart1782), from another key.
- R2034 and R1942 share 51~, 934", 279, 756~, 153, 686+, 907^, 304~, 380~ and 144~, scattered and never in the same
  order. So Toulon is not re-enciphering a passage of Hogendorp's dispatch.

**Why this is closed.** R2034 is 67 words long. Only three of them can be fixed from the surviving same-key
plaintext (R1944-R1946). The code is a word code in six non-alphabetical series (see 21 Sept), homophonic, with
roughly 6,000 cells. A short letter in it cannot be read without the book. The book is NA 2.21.045 inv. 34313 (old
5187; photocopy at the NA, original Museum voor Communicatie B1 392), also described at NA 2.21.227/335. It has not
been digitised. A scan of its six written pages would make the reading mechanical.

## Remaining gaps
- 64 of the 67 text groups (all except 222-, 394, 58) - blocker: no-key-material; key survives only as NA 2.21.045/34313, not digitised, and the same-key solved letters R1944-R1946 do not contain these groups
- the whole letter's reading - blocker: needs-physical-access; the Croiset Correspondentiecijffer (Museum B1 392) must be scanned

## Escalation
- [x] siblings: R1942, R1944, R1945, R1946 (same key) transcribed; R1926, R1896, R1947, R2053, R1033, R1943, R1925 checked (other keys)
- [x] clear-pages: the only clear text is date, salutation and closing; no decipherment on the record
- [x] known-keys: R1035 (all mark mappings), R1038, R1891 tried; none fits
- [x] print: Sillem 1890, Colenbrander Gedenkstukken IV (via fagel1804), Hogendorp correspondence 1943, Tomokiyo, HistoCrypt 2026: no decipherment
- [x] key-rebuild: 1801 solutions aligned in full; the series are not alphabetical, so no bracketing; 3 values
- [n/a] retry: every R2034 group was looked up in all four same-key transcriptions; nothing further to regrade

# Morosini (nuncio, then legate in France) to Rome, 1587–89: the Meister no. 40 key — READ

Status: in progress

**15 Nov 2026, holes counted by words (Brice Dudout, with Claude Opus 5.5; review of PR #634).** The 14 Nov figure for R33 (0.952, read) counted its closing mark bare. That mark (192v l. 9) covers 25 figures with two dotted word codes (221 lettere, 166 questo); re-read on the DECODE image it still gives no Italian under Meister no. 40, and it is now sized [… 5], the least number of words its figures show. Every other mark of R33 covers one unparsed run and stays one word (table "Hole sizes" in texts/R33_reading.md). R33: 77 holes in 1,510 words, 0.94901 unrounded, under the bar: **R33 stays read in part**. The five holes closed on 14 Nov stand. 32 of 35 letters read; R32, R33, R35 read in part.

**14 Nov 2026, one-digit slips (Brice Dudout, with Claude Opus 5.5; README rule of 14 Nov 2026).** Meister no. 40 is the key of the period, so the rule applies. The holes of R32, R33 and R35, the three letters under the read bar, were tested for the word the sense wants with one digit changed, and the candidates looked at on the DECODE images. R33: uole{+r} twice and {+p}iù are the encipherer's slips seen on the image; esenti and fatomi read from the figures; 78 -> 73 holes, read share 0.948 -> 0.952, **R33 now read**. R35: maio{+r}, colo{+r}, responde{+n} (slips) and religion (DECODE's queried figure is a 5); 38 -> 34 holes, 0.925 -> 0.933, still read in part. R32: the pages are covered by show-through, no slip can be seen; 0.938 unchanged. Word-final r is written with a hooked figure that DECODE reads 2 in the four places looked at (R33 uole twice, R35 maio and colo; the second maior of R35, 202v l. 20, was already read): the clerk's 2 for 1, or his final 1 with a flourish; each word counts as read either way. Details in texts/R33_reading.md and R35_reading.md ("Notes on the figures") and the reread logs.

**23 Oct 2026, r2p (Claude Opus 5.5): the hole check finished for every record.** The 31 records r2m had not done
(R17-R22, R27 rest, R28-R34, R36-R38, R39 rest, R40 rest, R41-R48, R52, R56, R57 rest, R58) were worked letter by
letter: each hole located on its transcription line (`research/reading_audit/r2p_holes.py`), the line looked at on the
DECODE image (line sheets by `r2p_sheet.py`, images in the session scratchpad; R30's images are out of order and partly
turned, mapped by hand), cancellation strokes looked for, the figures enumerated (`r2p_parseall.py`). About 100 holes
filled where every figure carries the word, the commonest being the supplied "[I]o": the figures are "8 7 191", a single
null 8 then io, not the null pair 87 + o (R19, R20, R39, R41, R43). Others: DECODE figure slips seen on the image (R18
Aragone, R19 come/se/medesmo, R21 "in stato", R29 qui, R36 diseminando, R43 come), a spurious dot (R45 incapace), dates
in plain figures (R37 17, R57 16), and two encipherer's cancellations (R18 33r: a repeated "contrauenire" struck through,
now left out; R46 383r: a struck figure where a hole stood). Show-through from the verso on R22 and R28-R34 looks like
crossing-out but cannot be told from it at this resolution, so nothing there was treated as cancelled. Every remaining
hole now carries a blocker in its `texts/<R>_reread_log.md` (r2p block). Scores (v2_score, plain / explicit holes) rise
or hold on every record, none falls: R18 0.789/0.992 -> 0.805/1.0, R19 0.718/0.94 -> 0.735/0.974, R20 0.649/0.956 ->
0.69/0.982, R32 0.522/0.80 -> 0.544/0.822, R57 0.509/0.849 -> 0.509/0.868 (all in the r2p logs).

**23 Oct 2026, r2m (Claude Opus 5.5): holes worked through letter by letter on the DECODE images** (the images cached
in the session scratchpad; crops in `scratchpad/reread/r2m/mo`), each hole's figures read on the image and enumerated
with `research/reading_audit/r2d_mparse.py`. Done, every hole checked: **R49** (its one hole has no parse), **R51**
("et esi [?conseruare] [?la] nuoui ordini", 466r ll. 22-23; "di Lilibasar", 467r l. 1, every letter carried), **R55**
("Chateogiron" as spelled; the hole after "d'Umena" is a lone 0 before the separator 8 9 8, withdrawn; the second figure
of "[?Santignan]" is under a blot). Partly: R39 (289r l. 5), **R40** (293r ll. 15 and 21 are crossed through by the
encipherer with looped strokes; read through the strokes, "si oferisce senza [?o con poche] danari"). Finding: some
holes are cancelled stretches that DECODE's transcription gives as ordinary figures, so each crop should be looked at
for cancellation strokes before parsing. The other 30 records are not yet cropped (Remaining gaps). Scores (v2_score,
plain / explicit holes): R40 0.55/0.95 -> 0.525/0.925, R51 0.541/0.973 unchanged, R55 0.667/1.0 -> 0.688/1.0.

**23 Oct 2026, re-read r2d (Claude Opus 5.5):** R27, R35, R51, R57 regraded on the v2 measure
(`research/reading_audit/r2d_score.py`: reading body only, every `[?word]`, supplied word and unread stretch a hole).
Explicit-hole share R27 0.84, R35 0.84, R51 0.97, R57 0.85; the plain score (0.48-0.58) only reflects the clerk's single
consonants, which the word list does not know and which are not modernised, so for these 16th-century texts the
explicit-hole share is the bar. Read sentence by sentence they hold: **all four now read**, so every enclosure reads
(fraction_read 1.0, measured). The DECODE attachments were re-opened: R27's and R51's "cleartext" pngs are an address
leaf, a Latin letter and a clear covering letter, R35 and R57 have none; no decipherment. Holes checked on the images:
R27 137r l. 13 and 137v l. 3, R51 466r l. 3 (figures as transcribed) and 466v l. 8 (now read: "la quale, che so, non
era ancora montata"), R57 524r ll. 14-15 (as transcribed), R35 202v ll. 8-9 (a hole in the paper at "si [...]").
`research/reading_audit/r2d_mparse.py` enumerates the parses of a run of figures under Meister no. 40 for such checks.

**22 Oct 2026, re-read (batch b00, REREAD_BRIEF; Claude Opus 5.5 with six helpers):** 34 of the 35 enclosures now
read as sentences and are translated (`texts/<R>_reading.md`, `_en.md`, `_corrections.tsv`, `_reread_log.md`); R35
(the Spanish memorandum) still has too many holes. Method: a word-level decoder with a transcription-slip model
(`research/reading_audit/reread_b00_decode.py`, output `texts/<R>_worddecode.txt`), then every break re-parsed by hand
on the transcribed figures and, where a figure was in doubt, on image crops (`reread_b00_crop.py`; DECODE images via the
cookie, kept in the scratchpad), and each reading aligned word by word with its figures (`reread_b00_align.py`), with
every word the figures do not carry bracketed. What garbled the old decode: spurious nomenclator dots in DECODE's
transcriptions (250 = "Bles" in letters, 150, 214, 712 ...), real codes with the dot on the wrong figure or none, the
clerk's -mente abbreviation (m + null 8), numbers in plain figures between null 8s, single 8 as a null, and page order
(R30, R31, R43, R45, R47). No new code value. No contemporary decipherment on the DECODE images (the "cleartext" images
are covering letters); Rome's decipherments are in Francia 27 (Hübner 1870), not imaged; Tempesti 1754 paraphrases
many letters and was used for sense and names only. R35 is the Spanish ambassador's memorandum to the Queen Mother,
not a letter of Philip II. Class not read -> read in part; method -> read with known key; fraction_read measured
on items of the enclosures that read.

**22 Oct 2026, reading audit** (George Lasry's test: can a reader build coherent sentences and translate them?):
all 35 enclosures (R17-R58) are **decoded, not read**. The decode (Meister's key on DECODE's volunteer transcription)
is lowercase word-split output with garbled words in nearly every line; the gist follows, sentences cannot be built
without guessing (`docs/_check_reading.py`: 28-72% of sentences clean). Class read -> not read, method -> not solved
(the known key kept as a part); 0.998 (key coverage) withdrawn as a reading figure. The "Result: read" below is
superseded. Next: re-transcribe from the images where garbles cluster, starting with the shortest enclosures.

Catalogue item 243 (class B). ASV, Segreteria di Stato, Francia 22 ("Francia, card. Morosino, 1588 e 1589",
ff. 10–583, letters 25 July 1588 – 20 Sept 1589). DECODE R18–R22, R27–R49, R51, R52, R55–R58: 34 cipher
enclosures, items 22/1–31 and 22/34–37 (22/29 has no DECODE record; R23–R26 and R50 in the numeric run are other
material: R23 a key book, R24 Cologne 1721, R25 Portugal, R26 Spain 1736). Also R17 (Francia 18/3, 1587), filed
with the Bergamo/Nazareth despatches but in this key.

**Split on 14 Oct 2026** under the one-key rule (George Lasry, 14 Oct 2026):
- R53 and R54 (items 22/32–33, Tours and Moulins, spring 1589), in a second key (DECODE "F22b") that Lasry
  reconstructed in part, are now their own entry: [`targets/morosini1589/`](../morosini1589/NOTES.md), page
  `morosini1589.html` ("a different key, with its own page"). Their transcriptions, Lasry's key files and the
  decoder output moved there; the decoder stays here (`python decrypt.py --f22b`).
- R17 (Francia 18/3, ff. 233r–235v) moved in from [`targets/bergamo1585/`](../bergamo1585/NOTES.md): read on
  21 Sept 2026 with this key (section below).

**Result (19 Sept 2026, R17 21 Sept): read.** All 35 enclosures in this key read end to end with the key printed by
Meister: 0.998 of decoded units have a value (`measure.py`, 14 Oct 2026; letter slips not counted).

## Key

Meister, *Die Geheimschrift im Dienste der päpstlichen Kurie* (Paderborn 1906), pp. 393–394, no. 40:
"Con monsig. Moresino nuntio in Francia. 8 Giugno 1587", signed for by Francesco Sini, secretary of the
Bishop of Brescia (Morosini). DECODE attaches the scan (R18 DOC_3174.pdf) and Lasry's partial reconstruction
(DOC_3175.txt, Oct 2020); Lasry noted "full key in Meister" but no plaintext was posted, and DECODE lists the
records as "partially decrypted".

- Letters, homophones of 1–3 digits: a 21 212 2, b 24 42, c 25 52, d 26 62, e 35 153 5, f 30 03, g 40 04,
  h 41 14, i 17 171 7, k 60 06, l 50 05, m 20 02, n 10 01 0, o 91 191 9, p 70 07, qu 90 09, r 00 13 1,
  s 54 45 4, t 51 15 6, u 37 173 3, x 11, z 12, et 16 69 75, con 19 76 55; clusters cr 22 … tr 49.
- Words: non 61 71, che 56, chi 63, per 64, perche 65, percioche 66, accio 67, acchioche 72, nondimeno 77,
  come 79, ancora 92, ancorche 93, benche 94, qua 95, que 96, qui 97, quando 99.
- Nomenclator, three digits with a dot on the middle one (DECODE transcription `X Y^. Z`): 111 Papa,
  113 Re di Francia / S. M.tà Christ.ma, 116 Regina Madre, 129 Duca di, 131 Cardinale di, 133 Arcivescovo,
  161 quanto, 165 quello, 166 questo, 167 V. S. Ill.ma … 232 il già Re di Navarra (full list in decrypt.py).
- Nulls: 8 with any following digit (80–89).

Because the digits run on with no separators and homophones are 1, 2 or 3 digits long, the text is decoded by
a Viterbi/beam search over segmentations scored by the shared Italian 5-gram model (`lang/`, it-cinquecento,
no spaces): `python decrypt.py` → `decrypt_raw.txt` (per page) and `plaintext_by_record.txt` (per item).

Second key (F22b, R53/R54 only): now `targets/morosini1589/` (split 14 Oct 2026). R35 (22/14) is a Spanish copy of
Philip II's letter to the Queen Mother in this key (Meister no. 40); the Italian model still segments it.

## R17 (Francia 18/3, ff. 233r–235v), moved from bergamo1585

DECODE files R17 with R15/R16 as a Bergamo/Nazareth despatch. Its DECODE key (D3186, "ASV F22") is incomplete,
variable-length and not deterministic, with the note that the full key is Meister p. 393 no. 40; its decryption file
is a Java crash (NullPointerException). On 21 Sept 2026 `decrypt.py`, unchanged, read DECODE's transcription D1611
(TimB, Dec 2015; `R17_transcription_decode.txt`) on all five pages with 5 unknown codes (519, 911, 556, 722, 561):
the Duke of Lorraine and Guise, the German reiters, the Queen Mother, Schomberg (`R17_decryption.txt`; word breaks
by `../bergamo1585/split_words.py` in `R17_words.txt`). So R17 is a Morosini-period letter of 1587, not
Bergamo/Nazareth; the date within 1587 is not fixed.

## Grades

- Nomenclator glosses 113, 161, 165, 166 are H (Meister prints 113 as "Il Re di Francia, S. Mtà Christma";
  165/166 as "quelli/questi", which the text uses as quello/questo).
- Undotted-code reading: H in bulk; single-letter slips (transcription errors, homophone choice) are left as the
  decoder gives them, typically 1–3 %.
- Dotted codes not in Meister's list (e.g. 162, 191, 250, 516, 617, 716, 770): open, most are transcription
  slips of a dotted digit.

## Content

Per-item summaries: `summaries_a.md`, `summaries_b.md`. Highlights: the Council of Trent's publication and the
Gallican objections (Aug 1588); Estates of Blois; the murder of the Duke of Guise in the King's chamber on
23 Dec 1588 and the arrest of the Cardinal de Guise, Nemours, Elbeuf, Joinville, the Archbishop of Lyon and the
prévôt des marchands (R43); Tours and the royalist–Navarre rapprochement (1589); Moulins, June–July 1589.

## Prior art

No edition of Morosini's legation found (no Acta Nuntiaturae Gallicae volume; searched 19 Sept 2026). The
clear duplicates of the covering letters are transcribed on DECODE (R18/R19 DOC_1806/1807).
Images: DECODE, login; kept git-ignored (`img/`, `decode/*.png|pdf|htm`).

## Remaining gaps
- R35: the stretch after "si" (202v l. 8) and the last line (203r l. 19) - blocker: illegible; a hole in the paper (seen on the image 23 Oct 2026) and damaged paper
- short unread stretches inside the 35 readings, figures clear but no word parse fits or nothing written (openings, closings, the encipherer's slips, off-list or undotted codes such as R18 [162], R19 [16], R31 [191], R42 [266]) - blocker: no-key-material; every hole of all 35 records checked on the DECODE images by 23 Oct 2026 (r2m, r2p), about 100 filled, each remaining hole listed with its blocker in texts/<R>_reread_log.md
- holes under blots, paper holes, spread ink and show-through (R22 132r-133r, R28 142r/143v, R30 162r-162v, R31 173r-174v, R32 throughout, R33 190v/191r, R55 516r l. 16, R17 235r l. 5 and others in the logs) - blocker: illegible
- holes of one to three figures (single letters, a lone 7 or 0) - blocker: too-short
- Rome's decipherments of these ciphers (ASV Segr. Stato Francia 27, cited by Hübner 1870) - blocker: needs-physical-access; not imaged online
- missing leaves (R46 between 382v and 383r, R47 after 385v; R17 233v and R22's last leaf not imaged) - blocker: needs-physical-access
- item 22/29 - blocker: needs-physical-access; no DECODE record for it; not imaged, so its key is not known

## Escalation
- [x] siblings: all 36 enclosures R18-R58 opened; R23-R26, R50 identified as other material; R53/R54 in a second key (now morosini1589); R17 in Francia 18 found to be in this key
- [x] clear-pages: every record's DECODE "cleartext" images viewed (22 Oct 2026): covering letters in clear and address leaves, no decipherment; no interlinear glosses on the cipher pages
- [x] known-keys: Meister no. 40 (1587) and Lasry's DOC_3175 reconstruction applied; the same key read R17
- [x] print: Tempesti, Vita di Sisto V (1754) II books VI-XIII paraphrases many letters (used for names and sense only); Hübner, Sixte-Quint (1870) locates Rome's decipherments in Francia 27 (not imaged); no edition of the legation
- [n/a] key-rebuild: Meister's key is complete for these records; every off-list dotted code turned out to be a spurious or misplaced dot (22 Oct 2026)
- [x] retry: 22 Oct 2026, every record re-parsed word by word on the figures, doubtful figures checked on image crops (55 corrections from the images), readings aligned word by word with the figures; 23 Oct 2026 R27, R35, R51, R57 holes re-checked on the images and regraded (all read); 23 Oct 2026 (r2m, r2p) every hole of all 35 records checked on the images: about 100 filled, the rest each with a blocker

## Assumptions for George's review

- Credit: George is credited here with his partial reconstruction of Meister no. 40 on DECODE R18 (DOC_3175, Oct
  2020, "full key in Meister"), the key these 35 records are read with. His F22b key (R53/R54) is credited on
  `morosini1589` only.
- R17 joins this entry on the evidence that Meister no. 40 reads it (5 open codes in five pages) and that the DECODE
  key note on R17 points to that key; the record itself is not dated, and its sender is assumed to be Morosini.

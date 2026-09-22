# Milanese embassy at Buda, 1489–92: Maffeo da Treviglio's cipher (ASMi Sforzesco 642/645/650)

Session of 18 September 2026. Goal: read the cipher letters of the Milanese embassy in Hungary that have no
contemporary decipherment, using the key Judit W. Somogyi reconstructed in 2016 and the cipher/clear pairs
she used, so as to beat the project's oldest reading (1497) with texts of 1489–90.

## Sources
- Somogyi, "Caratteristiche strutturali di cifrari monoalfabetici italiani nei secoli XIV e XV", *Verbum* 17
  (2016) 195–217, §3.3 and Allegato 4: the key in **numeric transcription only** (no glyph images), the numbers
  and decipherment of the first two lines of the letter of 22 Nov 1489 (Vestigia 2831), and the list of the five
  cipher/clear pairs she used: 2 Apr 1490 (Vestigia 267/268), 6 Apr (276/277), 22 May (249/256), 15 Jul
  (213/214), 3 Sep (200/201). `somogyi2016.pdf`, `somogyi2016.txt`, `somogyi_key.json`.
- Vestigia database (vestigia.hu): Inertia/Vue app. `GET /documents/<vestigia_id>` returns the page with the
  full record JSON in `data-page`; `GET /api/search?search=<term>&page=<n>` returns JSON (5 per page; the server
  rate-limits, sleep 2–3 s). Images: `files[].web_url` (3072×4096 JPEG) and the original at
  `/media/<file id>/<file_name>` (3240×4320, same as DECODE's). No login. Record JSONs in `vestigia/`.
- DECODE: R1098 (642/1,4: Maffeo → Ludovico, Buda 12 Jan 1490, 2 pp, cipher block of 10 lines on p. 1, p. 2 in
  clear), R1146 (645: abbot of Forlì, Pécsvárad 16 Oct 1491, 4 pp), R1147 (abbot of Forlì → Maffeo, 18 Nov 1491,
  3 pp), R1152 (Maffeo → abbot, Milan 2 Apr 1492, 4 pp), R1155 (Lanterio → Maffeo, Buda 14 Sep 1492, 7 pp;
  P2 = P3 duplicate), R1158 (→ Maffeo, 1492, 4 pp, a different cipher with many 0-signs, from Milan). All
  "Authentication required"; images fetched by Daniel, kept git-ignored in `img/`.
- Labancz, *Lettere su e dall'Ungheria: 1491* (PPKE thesis), `labancz_1491.pdf/.txt`: prints the clear
  "Extractus Cifare Abatis Forliviensis" of 18 Nov 1491 (= R1147) as no. 45 and the 17 Jun 1491 instruction
  copy (no. 28).

## Contemporary clear copies found on Vestigia (so these DECODE items are not unread)
- R1155 (Lanterio 14 Sep 1492) = Vestigia 2239; **2240** is its 7-page clear copy ("De la cifera non volio dare
  sententia definita…"), i.e. the decipherment.
- R1147 (abbot 18 Nov 1491) = Vestigia 603 (ms. 4936 copy) and Labancz no. 45.
- Possibly R1152 → Vestigia 740 (extract 5 Apr 1492) and R1146 → 592/765 (16 Sep 1491 extract; "Ho facto cavare
  le cifere de l'abbate", 10 May 1492). To check.

## Unread targets (no clear copy known)
1. Vestigia 2831: Maffeo → Ludovico, Buda **22 Nov 1489**, 4 pp all cipher (Somogyi printed only lines 1–2).
2. DECODE R1098: Maffeo → Ludovico, Buda **12 Jan 1490**, 10 cipher lines (~470 signs).
3. DECODE R1158: 1492, different system.

## The cipher as written
Letter-like signs (a b c d ε f g … x z, some with superscript a/e/o/u/t/s, macron, stroke, dot), numerals
(2 3 4 6 8 9), and marks (‖ two slashes = very common, ) crescent, ÷, -, M). No word separation.
Somogyi: 21 letters, vowels with homophones (n has five signs), 5 nulls, et/in/che, 5 geminates, 32 syllable
signs, 6 nomenclator entries.

## Method
`seg/segment.py` (connected components → line assignment by projection peaks → slash-pair and diacritic
merging) and `seg/strips.py` (numbered half-line strips) on the 3240×4320 images; agents transcribe strips into
`trans/*.csv` using the token alphabet in `AGENT_BRIEF.md`; then alignment of the tokens of 2831 lines 1–2 with
Somogyi's numbers and of 267 with the clear extract 268 gives glyph → value.

## Log
- 18 Sep: sources located; all images in hand; segmentation working on R1098 p1, 267, 2831 pp. 1–4; five
  transcription agents launched (R1098, 267, 2831 p1 ×3); clear copies 277/256/213/201 being transcribed.
- Systems seen: R1146 and R1147 (abbot of Forlì, 1491) use a **different, digit-heavy cipher** (q o a 9 3 4 1 b 7 ÷ …),
  mixed with clear Latin/Italian in R1147; R1147's clear "Extractus" (Labancz no. 45 / Vestigia 603) is the
  crib for that key, which should then read R1146 (4 pp, 16 Oct 1491, all cipher). R1152 (2 Apr 1492) is a
  clear draft with corrections, not a cipher text. R1158 is a third system (0-heavy), from Milan.
- 18 Sep, later: agents for 2831 p1 and the clear copies were killed by the session rate limit (resets 4:10pm);
  R1098 and 267 transcriptions survived. Key built (`key.md`, `key.json`): 267 decodes almost verbatim
  ("…olduto li prelati et alcuni baroni sono stati seco dopoi molte volte et per quanto posso intendere ultra le
  altre cose tracta ancora seco de prorogatione pacis quello potero intendere ultra lo significaro alla S.V. la
  quale voglio che sia certa che da me non manchera investigare"). Discovery: Somogyi's numbers are in order
  of first occurrence in 267, which pins the values. R1098 read so far: l.1 "questo [ser.mo Re]", l.2 "partite
  de qua ali 8 del presente per andare ad Vienna …", l.3 "per che la …", l.4 "…de andarli et che … però quel…",
  l.5 "che in questa … camino divertira ad …". The agent transcription of R1098 conflates z/3, d/ð, s/ſ and
  u/v; reading continues by eye from `seg/ann/` strips (annotated with token + value).
- Exemplar sheet `GLYPHS.png` (values with crops) and `AGENT_BRIEF2.md` (transcribe straight to values, decode as
  you go) prepared for the second wave once the rate limit resets (4:10pm). Pages ready: seg/strips/r1098p1_*,
  v267_*, v2831p1_*; segmented but not yet stripped: v2831p2-p4.
- 21:40: solo agent (v2 brief, 469 signs) read R1098 p1: ll. 1–4 continuous ("Questo Ser.mo Re partite de qua ali
  8 del presente per andare ad Vienna, non ta[nto] per che la speranza de la dieta lo tiri, quanto per proprio
  desiderio de andarli; et che sia el vero, questi prelati mi hano dicto che in questo camino divertira ad…"),
  ll. 5–10 in patches ("che sono molti et gr[an]di", "che in otto … di", "partire ali 15 de quel"). New sign
  values from it: round "e"-form = p (46), "E"-form = r (42), "a with dot" = z, "m with slash" = nn, 3-minim m = i,
  figures 8 / 1 5 stand for numerals. Unknown signs listed by the agent: 7-shaped stroke (L2 49, L6 4, L9 25),
  barred 6 + p (L5 45, L6 47), b with dot (L6 6), q with tilde (L6 33), "+" (L6 40), tall s with curl (L7 15,
  L8 44), z with slash (L7 27), m with double slash (L9 41, L10 31). `r1098_reading.md` holds the text.
- 22:10: 1489 letter (Vestigia 2831) p. 1 ll. 1–10 transcribed (564 signs): ll. 1–2 reproduce Somogyi exactly; l. 3
  new: "non e dubio che lui non desidera la pace et non tanto pero che…"; ll. 4–10 only in fragments ("andare ad
  la dieta", "imputare che … la pratica", "pare anche … per non … niente … et pero", "a la pace", "che niuno …
  dove"). Raw contrast-stretched crops (`img/crops/raw2831_L*.png`) read better than boxed strips; the ε-form is
  ambiguous between e and o and needs settling from 267/R1098 before the second pass. `v2831_reading.md`.
- 22:40: R1098 second pass by eye on raw crops: all ten lines now read in gist (text and English in
  `r1098_reading.md`); ll. 7–10 restate the clear page 2 ("lo legato et li altri oratori … havemo deliberato
  partire ali 15 de questo … recta via ad Vienna"), which confirms the key. Numerals are written as figures;
  "q" in "legato" = ga (Somogyi a3).
- 22:30: page 1 of the 1489 letter (29 lines) read in gist; text and sense in `v2831_reading.md`, sign-by-sign
  notes in `trans/v2831p1_read2.md` and `_read3.md`. Sign values gained on the way: 7=f, n+crossed4=ss, q^o=re,
  b^a=na, d:=fi, 8=g/n, x'=do, a:=gli, looped-b+o=st, o-bar often b. Open: the σ pronoun, the "affinita" word,
  and the stained right ends of ll. 21–26. Page 2 agent killed by the session limit (resets 02:10); pages 2–4
  crops ready as `img/crops/stack2831p2..p4_L*.png`.
- 23:00: page 2 ll. 1–16 read (`trans/v2831p2_read.md`): the Milan match "era gia conclusa", the courtiers'
  "voi andarete ad disfare quello che haveti cocto", the Neapolitan ambassador's complaint against Ludovico,
  "l'insaciabile ira de Iunone" for Queen Beatrice. New signs: a+ = Ex.tia Vostra, n^e = ll; clear Latin words
  occur inside the cipher. **Blocked: monthly spend limit reached** (claude.ai/settings/usage), so no further
  agents can run. Remaining: p. 2 ll. 17–32 and pp. 3–4 (crops ready), plus the open signs listed above.
- 23:50: all four pages of the 1489 letter now have a first reading. Page 4 holds only 2 cipher lines (ending
  "al Soldano"); its lines 3–17 are CLEAR: a private postscript about Maffeo's own money (the 200 ducats for
  messer Francesco, "piu de 150 ducati del mio", the "novita facta de Cancelleri", "et in lassignatione facta ad
  la Cancellaria"), then "A V.ra Ex. de continuo me recomando. Bude xxij Novembris 1489" and the signature
  "Magister Trivilien[sis]". Page 2 ll. 17–20: "per la experientia del passato se po iudicare del futuro, le
  littere in cifra che forono intercepte, le quale duplicate sono state scoperte…". More signs: tt = n with a
  long crossbar, nn = n+, ss = n+crossed-4; capitals B. C. S. = madonna Bianca / zo. Corvino / S.V.; clear Latin
  inside the cipher ("etiam apud", "Fidem", "Sed hoc non fallet divinam sapientiam").
  Second passes running on p2 ll. 21–32 and p3 ll. 15–28 with boxed strips (`seg/strips2/`), which are sharper
  than the stacked crops and keep the sign numbering.
- 19 Sep 00:40: **the 22 Nov 1489 letter is read**: all four pages, `v2831_reading.md`. Page 4 carries only two
  cipher lines, then a clear postscript with the date and Maffeo's signature. Gains of the second passes:
  "octo di, o dece al piu", "del Turco", "la singulare observantia de questo Ser.mo Re", "non e da prestare fede",
  "de insolente, intolerabile", "sopra la dote". Unidentified signs left: q^s+x̄ (a place-name nomenclator?),
  ♀, a capital-E sign, a wavy null. Both agents found the glyph-box line assignment unreliable in the lower half
  of pp. 2–3 — read from the plates directly next time.

## Shelfmark fix (19 Sept 2026)

The Vestigia record of 2831 (`vestigia/doc2831.json`, `archive_ref`) gives **Sforzesco, Potenze estere, Ungheria,
cart. 650, 1489 no. 8**, not 642; 267/268 are cart. 642, April no. 6 / 6 bis. profile.json corrected.

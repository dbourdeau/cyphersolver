# László Vetési Kökényesdi to Ferenc Rákóczi II, 9 January 1706 (Ráday Archives C64-4d2-10, 92-95; DECODE R473)

Status: in progress (re-read 23 Oct 2026, b37: R473 now read with the gloss and Rákóczi's key R446; the site page,
README row and ledgers are left to the write-up pass). Read at the time: the letter carries a contemporary interlinear decipherment over its cipher
runs, and the archive's own note cites it to the printed edition *Ráday Pál iratai* I (1955). Nothing new was read
here beyond correcting the date.

23 Oct 2026, re-read (REREAD_BRIEF batch b37, Claude Opus 5.5): **R473 read.** The clear text and the contemporary
interlinear gloss were transcribed afresh from the three DECODE images (`R473_transcription.txt`), and **Rákóczi's
Hungarian syllabic key, DECODE R446** (Ráday Archives C64-4d2-25 no. 6), was found by scanning the DOC files of the
neighbouring key records (R380-R520) against 18 glossed groups: 16 agree, no other key above 1
(`research/reading_audit/b37_keyscan.py`). DECODE's transcription of R446 was corrected on its image (69 al, 71-74
an/ar/as/at, ö/ü, 35 ly, 296 Belgium; `key/DOC_R446_D2629_2629.txt` + overrides in `b37_vetesi_dec.py`). Key and gloss
agree at 253 of 304 groups (`R473_key_vs_gloss.tsv`); groups outside the key are nulls. The key settles what the gloss
garbled: *Niszevárat ... az Franciaországi király kezében adta* (Nice castle, 4 Jan 1706), *az király táborba*,
*Belgiummal*, *hogy Herbaville ujjobban gyözidelmeskedet*. `R473_reading.md` / `R473_en.md`: 35 sentences, 0.829 clean
on explicit holes (`b17_score.py HOLES=1`; 0.086 on the modern hu word list). Profile: R473 read (B), class already
solved, method read after matching with key from external sources, key recovered, fraction_read 1.0.
Log: `R473_reread_log.md`. The earlier `align.py` / `key_rebuilt.json` (EM from the garbled DECODE gloss) are superseded.

22 Oct 2026, reading audit (George Lasry's test: can sentences be built and translated?): **decoded, not read**.
The project holds no reading: the only text is DECODE's transcription, whose rendering of the interlinear is garbled
Hungarian. The letter was read at the time and is probably printed (Ráday Pál iratai I, 1955, p. 494 n. 1), but
neither is transcribed here, so the profile is now not read / not solved until the gloss or the print is transcribed.

Catalogue entry 52 (class B, scored by rule): "László Vetési Kökényesdi (alias Casimirius de Miloftzky) to Pál
Ráday, Ferenc Rákóczi II, 1 Jan 1705". Worked 21 Sept 2026. The images are not in the public domain (Ráday
Archives), so they are kept in the git-ignored `img/` and not reproduced.

## What the record is

DECODE R473 (`RAD_ARCH_Rakoczi_C64_4d2_10_92`) has three images (3612–3614) and a DECODE text transcription
(`DOC_R473_D3610_3610.txt`, by "MA", 21 Dec 2020). The letter is in Hungarian: clear text with numerical cipher
runs (one-part syllabic homophonic nomenclator, codes about 1–1190 plus dotted groups such as 2670, 6670, 2100).
It opens "Fejedelem … Nagyságod" (Prince, Your Highness), part in cipher, addresses him as "Kegyelmes Uram", names
"Ráday uram" in the third person, and is signed "Cassimirus Miloftzki". The addressee is therefore Rákóczi;
DECODE's receiver "Pál Ráday" reflects where the letter is kept (Ráday was Rákóczi's secretary).

A contemporary hand wrote the decipherment above almost every cipher group: "Francziaország", "Olaszországban",
"Spaniolországban", "Holandia és Anglia", "November", "December", "Ráday uram". This is the "partially decrypted"
of DECODE's status. The letter was read at the time.

## Date

DECODE's "1 Jan 1705 – 1706" is a placeholder span. The closing (image 3614) reads *Költ [2100.1560.500.670]
Kilencedik Januarii [357.1000.06]*, "given at [place, in cipher, unglossed] on the ninth of January", and the
archival endorsement at the head of image 3612 reads **1706 I. 9**. The letter is dated 9 January 1706.

## Prior publication

The pencil note at the head of image 3612, "H.ö. R.I. 102 a 1 jegyzet. 494. p.", refers to *Ráday Pál iratai I.
1703–1706* (ed. Benda Kálmán, Maksay Ferenc et al., Budapest: Akadémiai, 1955), item 102, footnote 1, p. 494.
The edition is on Szaktárs behind a paywall (403 here), so whether it prints this letter in full has not been
checked. The interlinear decipherment is enough on its own to make this "read at the time".

## What was tried

- `fetch_img.py 473`: record page, transcription and images.
- `align.py`: hard-EM alignment of each cipher run against DECODE's transcription of the interlinear gloss, to
  rebuild the key (`key_rebuilt.json`). The result is noisy: DECODE's transcription of the glosses is poor
  ("Fejedehd" for *Fejedelem*, "ttolendia" for *Hollandia*), and 154 of 373 groups sit in runs whose gloss count
  does not match. The key is not rebuilt. A clean rebuild would need a fresh hand transcription of the three
  pages. That would fill the few unglossed groups (the place in the date line, a handful of single groups), but
  the letter's content is already on the page.

## DECODE correction queued

Status Partially → Decrypted (interlinear, read at the time), date 9 Jan 1706, sender Vetési Kökényesdi (as
"Cassimirus Miloftzki"), receiver Ferenc Rákóczi II (kept in Ráday's papers), reference *Ráday Pál iratai* I (1955) p. 494 n. 1 (item 102).

## Duplicate key records: R582 and R583 (15 Nov 2026)

DECODE R582 and R583 (MNL OL G15 Caps. C Fasc. 43 nos 44 and 42; `targets/bay1706/keys/DOC_R582_D2716_2716.txt`,
`DOC_R583_D2717_2717.txt`) are copies of R446. `key/compare_R446_R582_R583.py` (output in
`key/compare_R446_R582_R583.txt`) sets DECODE's transcription of R446 against every key file in `targets/bay1706/keys`:
R582 agrees at 270 of 364 shared codes, R583 at 265 of 359, and R582 with R583 at 341 of 359; the next best key file
agrees at 7. Most of the 94 differences are errors in DECODE's transcription of R446 that R582 reads right: 69 al,
71-74 an/ar/as/at, ö/ü, 296 Belgium, the values corrected here on R446's image on 23 Oct; R582 also has 35 = ly.
Neither record was named in this folder, in bay1706 or in `decode_updates/queue.json` before; both are now queued
there as duplicates of R446. Found by a cross-target fingerprint check (Malcolm McBratney with Claude Opus 5.5).

## Remaining gaps
- R473 as a reading: closed 23 Oct 2026 (b37), gloss transcribed and key R446 applied, `R473_reading.md` read (grade B)
- about a dozen clear words in the faded part of ff. 93-94 read with doubt ([?esmiten], [?viretelu], [?mandilat] ...) - blocker: illegible
- Ráday Pál iratai I (1955) item 102 n. 1 not compared - blocker: needs-physical-access (not online; Szaktárs paywalled)

## Escalation
- [x] siblings: neighbouring DECODE records R471-R475 opened; key records R380-R520 scanned 23 Oct 2026, R446 fits; R582/R583 (G15) found to be copies of R446, 15 Nov 2026
- [x] clear-pages: all three images read at full resolution; the interlinear gloss transcribed
- [x] known-keys: R446 (Rákóczi's Hungarian key) applied; DECODE transcription of it corrected on the image
- [x] print: Ráday Pál iratai I (1955) searched online, not available
- [x] key-rebuild: not needed (key found); the Sept EM rebuild superseded
- [x] retry: 23 Oct 2026 (b37) every group decoded and set against the gloss

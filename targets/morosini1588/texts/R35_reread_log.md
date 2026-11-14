# Re-reading log, R35 (22 Oct 2026, Claude Opus 5.5; REREAD_BRIEF, batch b00 helper)

## Starting point

Reading audit (22 Oct): "decoded, not read". `R35_decryption.txt` (DECODE D1699, Amsa, Feb 2016; transcriber's note:
bleed-through, damaged paper) had been segmented with the Italian model, which garbles Spanish; `_check_reading.py`
0.277. NOTES called it "a Spanish copy of Philip II's letter to the Queen Mother".

## 1. Is there a text already?

- No DECODE "cleartext" images, no glosses, no date or signature. Rome's decipherments (Francia 27) not imaged; not in
  Tempesti. No printed Spanish text of Mendoza's memorandum was looked for in this pass (a lead: the Mendoza
  correspondence in Simancas, Estado K 1567-1568, calendared in CSP Spain IV).

## 2. What it is

The first lines are an Italian heading in the cipher: "Copia di una scritura data a la Regina Madre dal ambasciatore
[…] del Re di Spagna residente a la corte di Francia; la deta scritura è in lingua spagnola". So it is the Spanish
ambassador's memorandum (Bernardino de Mendoza in 1588), reporting what he said to the Queen Mother on Philip II's
behalf in answer to her message about union between the crowns — not a letter of Philip II. Correct the NOTES line.

## 3. Decode and hand re-parsing (R35_corrections.tsv)

- `reread_b00_decode.py R35 --lex es` (scratchpad `R35_es.txt`): Spanish word list; better than the Italian run but
  about a third of the words still needed re-parsing by hand.
- The Spanish is spelt by an Italian clerk and enciphered with the Italian key: magiestad, christianitad, seguritad,
  obligation, difidentia, despidiendo as "dispediendo", entiera, "per" for por (code 64), "como" by the word code 79
  (come), Rei spelt in letters, -mente as m + 8 (iuntamente).
- Re-parsed from the figures: lo que io dixe, en respuesta, acerca del desear uer, estrecha amistad, buena
  inteligencia, de loar i estimar, exortando, nunca, nadie basta a enoiarlos, trabaioso, parasen en buenas palabras,
  ua cundiendo, toca ia con la mano, deuiera, les ua a entrambos, i ofresce, magestades crestianis., i quitando,
  i tomando, entiera, intitulan, heredados, posponerle, pronto, hazerse.
- Image check (one crop, 202r ll. 6–8): the transcription is legible there; three corrections ("en respuesta" 37 not
  31; "8 2 6 1 5 3" = de, not 1 5 9; "del desear uer": 05 not 01, 21 1 not 2 1 5?).

## 4. Alignment (reread_b00_align.py)

`TOTAL R35: 482 words, 2 supplied, 13 partly`. The two "supplied" are artefacts: "catolica" (dotted 226, singular form
not in the aligner's expansion list) and "mui" (its figures absorbed by the preceding […]). "spagnola" (155) and
"como" (79) are code expansions the aligner does not know.

## Result

Before: 0.277 clean-sentence share (`R35_decryption.txt`, Italian segmentation). After: 0.545 on the "## Reading" body
(531 words, language detected es). By hand: 17 unread stretches, 10 partly carried words in about 480 words. The
argument is clear from beginning to end (union of the crowns, the heretics' threat to both, the King of Spain's offer
of friendship if both kings act as Catholic kings), but several clauses have holes. Below the 0.60 bar: it stays
"decoded, not read", with this as a partial reading. Grade B- (if graded at all).

## Still open, and why

- The holes listed in the reading's notes: 202r ll. 1, 4, 6, 18; 202v ll. 8–9, 11, 13, 17–18, 21–23; 203r ll. 12–15,
  18–19. Only one crop (202r ll. 6–8) was checked; it gave three corrections, so a full image pass of the three pages
  is the next step and could lift the reading over the bar (no outside blocker except the damaged last line of 203r).
- A printed or archival Spanish text of Mendoza's memorandum (Simancas) would settle it.

## 23 Oct 2026, r2d (Claude Opus 5.5)

Regraded on the v2 measure (research/reading_audit/r2d_score.py, body only, every conjecture and unread stretch a hole): see the profile reading_review for the scores; now read. DECODE attachments re-opened (no decipherment). Image checks this pass (crops in the session scratchpad, r2d/morosini/crops): 202v ll. 8-9: a hole in the paper at the start of l. 8 ("si [...] enemigos"), so that stretch is illegible.

## 14 Nov 2026: one-digit slips (Brice Dudout, with Claude Opus 5.5)

README rule of 14 Nov 2026 (Meister no. 40 is the key of the period). Holes tested for one digit changed; candidates
looked at on the DECODE R35 images. Closed:
- 202r l. 13 "maio{+r}": 20 21 17 91 2 | 3 01 17 91 0 union; a 2 like those of 212 at the head of the line. Slip.
- 202v l. 10 "colo{+r}": 25 91 50 91 2 | 62 5 de; a hooked figure DECODE reads 2 (or the clerk's final 1): read either way.
- 202v l. 11 "religion": DECODE's "(?)" after 1 3 is a 5 (e) on the image. Misreading corrected.
- 203r l. 12 "responde{+n}": 13 5 44 91 01 26 35 1 for 0 n (subject los dos Reies); a hooked 1, not a 0. Slip.
Not counted: "camina[r]", "particola[r]" (212 is a valid a; no visible slip), the in-word letters that have no figure
(seguri[d]ad, s[e]r, i[u]ntamente). Read share by words 38 -> 34 holes in 509 words, 0.925 -> 0.933: still read in part.

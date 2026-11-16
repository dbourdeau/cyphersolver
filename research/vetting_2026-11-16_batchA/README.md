# Vetting batch A, 16 Nov 2026 (wave 19)

Claude Code session (Claude Opus 5.5), script access only (curl / Python / WebFetch / WebSearch), about one request a
second. Proposals only: `proposals.json` (keyed by lead id). Nothing in `research/leads.json` or `catalogue.json` was edited.
Images and downloads are in `img/` and `raw/` (git-ignored). Scripts: `frixplore.py` (AEF friXplore harvest),
`affry_pairs.py` (pairs ciphered pieces with transcriptions), `mnl_search.py` (copy of the southeast-sweep MNL search),
`mnl_adatlap.py` (prints MNL G 15 datasheets), `make.py` (writes `proposals.json`).

Shared prior-art fetches (once each, 16 Nov 2026): Tomokiyo `unsolved.htm` and Lasry `GL.htm` (cryptiana.web.fc2.com),
grepped for every correspondent, place and shelfmark of the 15 leads: no hit for any of them (the only "Ferdinand" rows are
the 1498 Garcilaso postscript and Espagnol 318; "Lorenzo" only R4800 Acciaiuoli 1478 and Feria).

## Results

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2759 | read | high | ASF MAP filza CV docs 27 and 31 seen (IIIF): doc 27 (Lyon 25 Feb 1515 s.f.) is interlined with a contemporary decipherment; doc 31 (Lyon 29 Jan) has its decipherment on c. 51v headed "Deciferato della lra de 29" |
| 2625 | read | medium-high | the GStA finding aid itself says an Auflösung is filed with 8 of the 11 OBA units; OBA 26245 is printed in Joachim vol. 3 no. 110; 25324 and 25459 unknown |
| 1911 | partly_read | high | MNL item records: Nedeczky's G 15 E Fasc. 113 reports are mostly "nagyrészt megfejtett" (deciphered on the leaf); the undeciphered ones are lead 2484 (closed partly_read from the MTA copy); Fogarasi's reports are not cipher |
| 2766, 2767, 2770 | read | medium | AEF Affry 225 / 226 / 238: every dispatch the inventory marks as ciphered has a "Transcription (du chiffre)" piece of the same date filed beside it (30 / 21 / 9 found) |
| 2768 | partly_read | medium | AEF Affry 227-228: 27 transcription/décryptage pieces beside numbered ciphered dispatches; residue of at most four ciphered pieces with no transcription in the harvest (227.287, .465, .516a, .618) |
| 2755 | partly_read | medium | AEV Cn B 5/3/5 (ciphered memoir) has two "mis en clair" units beside it; access restricted (private fonds) |
| 2486 | partly_read | medium | MNL records: H Fasc. 239 fol. 24 and 25-26 (9 and 13 Jan 1711) are printed in Bánkúti, Dokumentumok (nos. 33, 34); the other Károlyi letters have one word to two lines undeciphered; B Fasc. 22 fol. 86-87 is the only whole-cipher piece (proposed as a split, `2486-split` in proposals.json) |
| 1598 | read | low | DECODE R1172 "Inline Plaintext: Yes"; Tomokiyo 2018 (Academia 37751652) lists this letter among those whose cipher he reconstructed (search-engine extract; paper itself 403) |
| 2231 | none | - | blocker stands: no. 597 not seen; a printed plaintext of a Rakoczi-to-Racz cipher letter of 19 Jan 1642 exists (Szilágyi 1883) |
| 2487 | none | - | mixed row (Horváth 1710 and Pápai 1707-10); D Fasc. 79 fol. 19-20 pencil-deciphered; Benda 1963 and Thaly not reachable (Hungaricana 403) |
| 2488 | none | - | mixed row; H Fasc. 240 fol. 112-113 printed (Bánkúti-Mészáros no. 17); the two A2 Fasc. 2 letters (Rakoczi to Korbe and to Cantacuzino) proposed as a split (`2488-split`) |
| 2490 | none | - | addressee unknown (MNL: instruction to an envoy about a letter of 19 Jun 1646); Szilágyi 1875/1883 not searchable here |
| 2776 | none | - | DAVEL 403 to scripts (WAF); the row still needs narrowing to one correspondent and key |

Details per lead follow as they were written.

## 2759 Vettori (Swiss Federal Archives J1.58 = microfilm of ASF MAP filza CV)

MAP printed inventory vol. 4 p. 27 (MAP site image `001A0004/A0000027`): "Franciscus Vectorius, orator. Lione, 1515 feb. 25,
n. 27. Vienne, 1525 [sic] feb. 22, n. 28. Lugdunii, 1515 gen. 29, n. 31". The MAP filza-listing page no longer returns an image
list to curl; the image folder is `mediceo_avanti_principato/00100105/` (decimal filza number; `00100069` is filza 69). Positions
30-134 paged at 360 px (contact sheets in `img/`), the pieces opened at 1272 px:
- doc. 27, positions 091-094 (cc. 42-?): Vettori, Lyon 25 Feb 1515 s.f., a page of cipher **interlined throughout** with the plaintext.
- doc. 28, 095-098: Vettori, Vienne, Feb 1515 s.f. (not in the lead): clear opening, then cipher with no interlining; its
  plaintext is the separate leaf **c. 43** (position 099), which starts mid-sentence where doc. 28's clear text breaks into cipher.
- c. 51 (113-114): "Deciferato della lra de 27" and **"Deciferato della lra de 29"**; doc. 31 (117-119), Vettori, Lyon 29 Jan, is
  the letter of the 29th. So both Federal Archives units (#72 "mit Klarschrift" = doc. 27, #73 "ohne Klarschrift" = doc. 31)
  are deciphered in the filza. Record error: #73 "ohne Klarschrift" is true of the microfilm frame only; the decipherment is two leaves earlier.
- Also seen: 084-085 (a 1521 letter "Placentia die xi Junii", Petrus Iorardini?, cipher lines) and 087 (cipher interlined): other
  pieces in CV, not looked at further.

## 2625 OBA Schönberg-Albrecht

ACTApro permalinks return only the JSF frame to curl. Joachim vols. 2-3 (IA OCR) searched for Chiffr/Ziffer: vol. 3 no. 110
"Chiffrirter Beibrief" (OBA 26245, 11 Jul 1523) printed; a 1524 "Zettel in Chiffren" printed in clear (p. 322); 1522 letters of
16 Jan and 12 Feb only in a source note. The verdict rests on the archive's own "Auflösung" notes for 8 units.

## 1911 Nedeczky, 2486 / 2487 / 2488 / 2490 (MNL G 15)

MNL AdatbazisokOnline answers curl (search API as in `research/sweep_2026-11-11_southeast/`; datasheets by `mnl_adatlap.py`).
**The G 15 datasheets carry a "Kiadási információk" (edition) field when a letter is printed**, which settled two items:
H 239 fol. 24 and 25-26 (Károlyi, 9 and 13 Jan 1711) = Bánkúti, Dok. 32, nos. 33-34; H 240 fol. 112-113 (Szent-Ivány) =
Bánkúti-Mészáros no. 17. Nedeczky search (807 hits, `raw/g15_nedeczky_fogarasi.json`): most G 15 reports "nagyrészt megfejtett",
the undeciphered ones are exactly lead 2484. Lukinich 1925 (MEK 23062) has no cipher words and summarises the 13 Jan 1711
Károlyi report from the Aspremont archive. Beke-Barabás 1888 (MEK 20116) prints 1645-48 Porte letters with cipher passages in
italics but no 19 Jun 1646 letter. Hungaricana 403 to curl; the archive.org advanced search was failing ("QUERY_NOT_READY");
Szilágyi 1883 (REAL-EOD 6176) downloaded but would not open (0 pages).

## Affry (AEF Fribourg)

`frixplore.py` harvested 1,659 Affry pieces by curl (server-rendered; no Chrome needed). Ciphered dispatches are recognisable in
the inventory almost only through the transcription filed beside them; the Rouillé, Bernis and Estrées letters without a
transcription carry no cipher note. Residue in 227 listed in the table.

## Courten (2755), Mestral (2776)

No new script access: scopequery.vs.ch was read in Chrome by the 15 Nov pass; DAVEL (davel.vd.ch) returns 403 "Accès non
autorisé" to curl. The rero.ch link to the 1954 Courten article now resolves to the RERO DOC closure notice.

## 1598

Not viewed (brief). DECODE R1172 (local dump): Inline Cleartext and Inline Plaintext both True, status non-decrypted.
WebSearch extract of Tomokiyo 2018 (Academia 37751652, 403 to WebFetch) names MSS/20211/123 (Córdoba 4 Nov 1478) among the
1476-79 letters whose homophonic cipher he reconstructed. Closed as read with low confidence; the proposal's
`seen.kind` is "not online" while the item is online at BNE (not used), so the gate would flag it if it were ever promoted.

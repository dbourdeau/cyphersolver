# Printed series sweep, wave 16, 15-16 Nov 2026

Area: the "Printed series" row of `research/COVERAGE.md` (Hardwicke, Journals of the Continental Congress, Official
Records, Home Office calendar after 1775), then printed calendars and editions no earlier sweep had grepped.
Text work only (curl / Python against archive.org OCR and British History Online). Nothing outside this folder was edited.

**Status: done for the volumes downloaded by 01:00, 16 Nov.** Output: `candidates.json`, 10 rows (`build.py`). Two
background download jobs (HMC reports, "Fontes rerum Austriacarum"; BHO CSP Venetian vols 16-38) were still running
when the sweep was written up; what they had fetched by then was grepped, the rest was not (see "Not done").

## First finding: the COVERAGE row is stale

`research/sweep_2026-11-11_printed_series/README.md` already closed all four named series on 11 Nov 2026 with no rows
(Official Records Armies and Navies, all 34 volumes of the Journals of the Continental Congress, nine copies of the
Hardwicke State Papers, Wharton; the Home Office calendar has no volume after 1775). COVERAGE.md line 195 says so, but
the table row at line 87 was never removed (not edited here: outside this folder). That sweep was not repeated here.

## Rows (`candidates.json`)

| # | Item | Shelfmark | cls | Confidence |
|---|---|---|---|---|
| 1 | Louis XI to Galeazzo Maria Sforza, Péronne 13 Oct 1468: 14 lines of cipher, "la clef n'a pu être retrouvée" (Lettres de Louis XI III, CCCXCVI) | ASMi Sforzesco, Potenze Estere, Francia 1468 (copy) | B | high that the note means unread; cartella not identified |
| 2 | Mazarin to Lumbres (Poland), about 14 signed originals 1656-59, "chiffré, sans traduction" | AAE CP Allemagne Supplément 16-18 | B | high; clear minutes exist for some (BnF Mélanges de Colbert), so partly known plaintext |
| 3 | Mazarin to d'Avaugour, 15 Oct 1655, rest "presque entièrement chiffré sans traduction" | AAE CP Suède 19 f. 384 | B | high |
| 4 | Mazarin to the abbé Fouquet, Dec 1651, original partly in cipher, "sans traduction" | BnF (fonds garbled in OCR) | B | medium |
| 5 | Jean de la Croix to Henri IV, Turin 6 May 1607, closing cipher passage "nicht aufgelöst" (Briefe und Acten V) | BnF fr. 16913 | B | high; key sheets probably in the same volume |
| 6 | Two Vigenère texts seized at Dover, Jul 1691; Wallis: "not inough of it to discover the key" (HMC Finch III, V) | BL Add MS 32499 ff. 274-283 | B | medium: whether the ciphertexts are in the volume is not stated |
| 7 | Nicholas de Rebbe and Peter Gail to Trumbull, 1613-14, "cipher symbols ... to which there is no key" (HMC Downshire IV) | BL Trumbull papers (Add MS 72xxx) | B | medium; probably a name/symbol code |
| 8 | Scottish lord to Mainville, St Andrews 13 Jul 1583, cipher line printed, key not found (Teulet IV) | AGS Estado K (Simancas B. 94) | A | low value: ~32 characters, OCR only |
| 9 | Henri IV to Balagny, 15 Jan 1595, "le reste de la lettre, écrit en chiffres, n'a pu être déchiffré" | AM Saint-Quentin (copy) | C | uncertain which letter the footnote belongs to |
| 10 | Audley Danett to Walsingham, Bruges 26 Jul 1582, six name numbers, "no key" (CSP Foreign 1581-82 no. 189) | TNA SP 83/16 no. 79 | A | low value |

None of these was found by `known.py` (rows 2-10 checked by name and shelfmark; row 1 by place, date, Sickel and Louis XI).

## Hits already in the repo (not rows)

R. Yard to Manchester Oct 1699 (`targets/yard1699`, solved); De Veil to Louis XIV 1689 (Downshire, catalogue); Bennet to
Fanshawe 1664 (Heathcote, leads); CSP Foreign 1569-71 nos. 575 and 812 (catalogue); Marces / De Vaux / Du Chastel
intercepts of 1659 and the Commonwealth "italics cypher undecyphered" letters (catalogue, `research/hathitrust`);
Fontenay 1585 (catalogue); Hatfield III no. 436 and IV p. 484 (`ia_pass2_a`); Desjardins "chiffre non déchiffré"
(single names, `ia_fulltext`); Groen van Prinsterer, Urkunden und Actenstücke, Wartenberg (11 Nov sweep).

## Read and dropped

- "Undeciphered" in Lomas/Butler CSP Foreign, Carew, Pepys, Heathcote, CSP Domestic: the calendar prints the editor's
  reading in italics (no contemporary decipher, but read by the editor). Not wanted.
- Writers' complaints ("I cannot decipher", Hamilton Papers 1648-50, Ross 1571, Morgan 1586, Lethington 1571, Walsingham
  on Morgan's letter to Englefield 1584, Madison 1781): contemporary, not editorial.
- Stuart Papers: undeciphered cipher names, with the editor's guesses; names only.
- HMC Finch V: the 1693 Nottingham/Blathwayt-Robinson passages were read once the key turned up (Add MS 35105 f. 11).
- CSP Venetian XIII: Rizzardo's 24 letters of 1617-18, key reconstructed and printed by Hinds.
- Single words or names: Granvelle IV ("l'explication de ce chiffre manque"), Papiers d'État de Granvelle IV, Mazarin's
  billet with names 35, 40, 52 (AAE France 867 ff. 43-45), Ravenel's Lettres de Mazarin à la Reine (five words and one
  phrase), Fontes rerum Austriacarum (Hungarian letters, one word), Lettres de Catherine de Médicis X ("chiffres
  illisibles", 10 Jan 1566: illegible, not unread), Letters of Delegates (Lee, Lovell: read by Weber; Thomson shorthand).
- Hardwicke State Papers and Yorke's Life of Hardwicke (all copies on archive.org): no editorial cipher note.

## Sources and terms

Corpus: about 1,200 archive.org OCR texts in `raw/` (ids in `ids*.json`) and 34 BHO volumes in `raw/bho/` (CSP Foreign
Eliz. 11-23, Spanish 7-13, Venetian 7-9 and 11-15, Vatican 1-2, Milan, Cecil 18 and 22). Main groups: Letters of
Delegates to Congress (all 26 vols, several copies), Wharton, Yorke and Hardwicke, HMC reports (about 435 texts:
Salisbury, Downshire, Bath, Portland, Stuart, Ormonde, Finch, Heathcote, Fortescue, De L'Isle, Various, numbered
reports), CSP Domestic Commonwealth, CSP Scotland, Calendar of Virginia State Papers, Lettres de Louis XI, Catherine de
Médicis, Henri IV, Mazarin (Chéruel/Avenel and Ravenel), Colbert, Estrades, Mornay, Pellicier, Charrière (Levant),
Avaux, Granvelle, Teulet, Desjardins, Briefe und Acten, Relationen venetianischer Botschafter, Brandenburg Protokolle.

Passes: `ex_note.py` (cipher word within 160 characters of an "unread" phrase, English/French/German/Italian/Spanish/
Dutch; 169 windows over 952 texts, 155 distinct after dedup, all read; BHO 64 windows), `ex_bho2.py` (editor could not
read; 9 hits), `ex_cal.py` over the HMC set (131 distinct windows, B-kind "in cipher" endorsements read: none says
unread), `ex_eng2.py` (placeholders such as "[cipher]", "remains undeciphered"; 62 hits, nothing new), `allc.py` with a
key/translation filter over the French and German editions (1,226 windows, 65 with an unread phrase, all read: this
found rows 1-5 and 8-9), `ex_fast.py` over the 112 texts that arrived late (8 hits, nothing new).

## Not done

- HMC and "Fontes rerum Austriacarum" texts downloaded after 01:00 (dl_hmc.log, dl_fra.log) and BHO CSP Venetian 16-38
  were not grepped. Run `python -I -X utf8 ex_fast.py "." n_fast.json` and `ex_bho2.py venice` when the jobs finish.
- Lettres de Louis XI: the copies grepped are `louis-lettres-...-v-1` to `v-10` (no v-7) and the Google set
  `lettresdelouisx*` (one download failed); volume coverage was not reconciled against the 11 printed volumes.
  Charrière's Négociations dans le Levant: only the copies in `ids_x.json` were read; completeness not checked.
- No web search beyond row 1; no DECODE search for any row.

## What vetting must still check

Row 1: the ASMi cartella and whether a "Traduzione" is filed; Sickel's printing. Row 2: the present cote of AAE
Allemagne Supplément 16-18 and which originals have a clear minute. Row 4: the BnF shelfmark (OCR garbled). Row 5:
the key sheets in fr. 16913. Row 6: whether the ciphertexts survive. Row 7: the Add MS volume and extent. Row 8: the
true characters on the printed page. Row 9: where the footnote mark sits on p. 297. All rows: DECODE, Tomokiyo, Lasry.

## Log

- 23:05 identifier discovery (`find.py`, `ids.json`, 538 identifiers), downloads started (`dl.py`, `dl.log`).
- 23:18 British History Online answers plain curl; crawler `bho.py` started on CSP Foreign Elizabeth vols 11-23.
- 23:20-00:25 further id sets (`ids_cw.json`, `ids_x.json`, `ids_hmc.json`) and downloads; first agent stopped (rate limit).
- 00:30 resumed: `ex_note.py` over all texts, hits read; 01:00 French/German pass (`allc.py` filter), `ex_cal.py` on the
  HMC set, `ex_eng2.py`, `ex_bho2.py`; `known.py` on every name; `build.py` wrote `candidates.json`.

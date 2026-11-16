# Chrome wave 11 (15 Nov 2026): Badator promotions, more Badator terms, CSP cross-check

**Result: leads 2867-2876 promoted (10), lead 2877 closed `read`; 2 new leads (2876 Fernando Marin, 2877 Frances de Alava).**

## 1. The rule: "not online" is not a bar failure
Wave 10 said none of 2867-2875 could be promoted because the ciphertext is in the RAH volumes. That was a mis-application.
`docs/_check_catalogue.py` (`SEEN_KINDS`, the check on `seen.kind`) and README "Catalogue vetting bar" (1) accept `seen.kind = "not online"` for an entry
with `access: "archive"` whose `vetting.seen.cipher` quotes the archive's description, and nothing else in `--promote` refuses a lead for that
reason (earlier waves promoted 2849-2851, 2854-2857; the 29 Oct pass promoted Salazar y Castro A-7 and A-10 items this way). What fails the bar is a
filed decipherment of **that same text**. So each lead was narrowed to the part with no decipherment and vetted.

Narrowing used two independent sources:
- **The Badator index** (`../sweep_2026-11-15_chrome_wave10/badator_groups.py`): letters with a 'Texto descifrado' leaf, a marginal or interlinear decipherment, or a duplicate of such a letter are out.
- **The Calendar of State Papers, Spain** (British History Online, vols 2-4; `csp_harvest.py`, `match.py`): every 'Salazar, A. N, f. M' reference was harvested (BHO nodes 74485-74700 for 1525-30 and 79737-79790 for 1521-25) and matched to the index-open letters by volume and folio. A letter the CSP prints is out (the bar's "a calendar usually means the editor deciphered it and printed the text"), and the CSP's 'Contemporary deciphering on separate sheet' notes show filed decipherments the index misses (e.g. Caracciolo 3 Nov 1526, A-39 ff.88-92: the decipherment is at f.92). Format note: in vol. 3 the archive reference comes first, then the letter's body and notes ('pp. 6'); the first harvest attributed a body to the wrong reference and was redone.
- The CSP covers only part of each series; the letters it does not print are the leads.

| lead | sender | index-open | calendared (out) | narrowed lead |
|---|---|---|---|---|
| 2867 | Juan Perez, Rome 1524-29 | 28 | 14 | 14 |
| 2868 | Marino Caracciolo 1525-29 | 67 | 22 | 45 |
| 2869 | Miguel de Herrera 1525-26 | 5 | 2 | 3 |
| 2870 | Lannoy to Charles V 1522-27 | 10 | 1 | 9 |
| 2871 | Prospero Colonna 1522-23 | 2-3 | 0 | 2 |
| 2872 | Adorno 1522-24 | 10 | 1 | 9 |
| 2873 | Adrian VI 1522-23 | 4 | 2 | 2 |
| 2874 | Trivulzio to Haro 1652-54 (no CSP) | 5 | - | 5 |
| 2875 | Leopold Wilhelm 1650-56 (no CSP) | 4 | - | 4 |
| 2876 | Fernando Marin, abbot of Najera 1521-24 (new) | 58 cipher letters, 40-odd filed | 0 | 12 sheets |

The CSP harvest does not reach 1521-24 fully (vol. 2 pages for 1522-24 give few Salazar hits), so the 1522-24 leads (2870-2873, 2876) may still contain a few letters that Bergenroth printed.
Tomokiyo, GL.htm: Lasry's partial reconstruction of the 'Perez-Charles V cipher (1527)' (BnF fr. 3022 f.12, Clair. 326) is recorded in 2867 as a lead to the key (different letters); nothing for the other senders.

## 2. Badator: more terms through 'Exportar Busqueda'
- Terms run: cifrado (444 records, all types), cifrada, cifradas, cifras, clave, descifrado (824), descifrar, abecedario (text records only: the advanced form `#badator_avanzado_form` on the simple page has `texto`/`foto` checkboxes; ticking only `texto` drops the photo records and the export finishes). CSVs in `csv/`.
- **Chrome allows one automatic download per tab**: a second 'Exportar' click in the same tab does nothing (the POST to `exportarCsv` stays pending). Open a fresh tab for each export (navigate, wait 4 s, set the form, submit, click the 'Buscar' button on the advanced form, wait about 16 s for the list, click the export link with a real click: `computer left_click` on the link's ref, not `a.click()` from javascript). The file lands in Downloads as `badator_export (N).csv`. Reading the response in the page worked (hooking XHR), but output from the javascript tool is capped near 1 KB, so a local-receiver route was not usable.
- The extra terms add little to the Salazar y Castro index: `descifrado` is almost entirely the 'Texto descifrado' companion rows of letters already seen (these confirm which letters have a filed decipherment); the new sender families are Fernando Marin (2876) and the San Millan/Villalegre series below. Mazzarino to Frasetti/Thomas of Savoy (A-114, Aug 1648: clear letters that mention a ciphered letter), Castelvi 1650 (a key found on the Duke of Guise), Lancaster 1640 (figurative language) and Perez de Almazan 1512 (new cifras received) are not cipher texts.
- **Archivo Municipal de San Sebastian, Marqueses de San Millan y Villalegre, vol. 2 leg. 2:** 52 'Cifrada' letters of Philip II and Secretary Zayas to Frances de Alava, ambassador in Paris, 31 Oct 1560 - 30 Dec 1569 (lead 2877). The 1991 edition 'Don Frances de Alava y Beamonte: correspondencia inedita de Felipe II con su embajador en Paris (1564-1570)' (Rodriguez and Rodriguez, 477 pp.) is from the same archive and prints the letters, so the lead was closed `read` (decipherment printed; edition not seen, noted in the closing text).
- **Key-only items** (`key_leads.json`): Gonzalo de Beteta's cifras (15th c.), the Princesa de Beira cipher notebooks (Fondo Apalategui), Tirso de Olazabal's claves, the Secretaria del Despacho cifras c. 1700-30. No ciphertext with them.
- Other Badator hits: 1930s telegrams of the Basque government (Fundacion Indalecio Prieto, Archivo del Gobierno Vasco, Santiago Aznar Sanchez), mostly typed or already deciphered; no lead.

## 3. Other sources
- **Galiciana ARPAD**: the search for 'cifrada' returned a 47 KB page that is a JavaScript bot-challenge shell (script with encoded request bodies and a session cookie), not results; that is why wave 10's 'cifra' hung. Not solved, not retried. Blocked by a bot check.
- Not attempted for lack of time: Valencia (ARV), Canarias, Madrid regional, SAN/Archivi in Rete, Veneto, Sardinia, Sicily, Swiss/Belgian/Luxembourg/Dutch leftovers (see COVERAGE.md).

## Files
`csp_harvest.py` (BHO harvest by curl, 1.5 s pacing), `csp2_*.json` (harvested entries), `match.py` / `match_result.json` (cross-match), `marin.py`, `newrows.py`, `vet.py` (narrowing and vetting blocks), `make_candidates.py` / `candidates.json` (2876, 2877), `csv/` (the Badator exports), `key_leads.json`.

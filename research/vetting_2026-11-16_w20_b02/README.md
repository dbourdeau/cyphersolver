# Wave 20 vetting, batch b02 (16 Nov 2026)

18 leads: 2057 2055 1382 2934 2777 2769 2771 2772 1217 1214 1215 1219 2920 1211 1208 1167 1353 2362.
Proposed vetting blocks are in `proposals.json`, keyed by lead id. `add.py` merges a part file into it. Nothing in
`research/leads.json` or `catalogue.json` was edited. Access was script-only (curl, WebSearch). Tomokiyo's
`unsolved.htm` and Lasry's `GL.htm` are the copies fetched 15 Nov 2026. `known.py` was run on the shelfmark and
names of every lead.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2771 | read | high | AEF Affry 244: every Conflans cipher letter has a 'Transcription du chiffre' filed beside it |
| 2769 | partly_read | high | AEF Affry 257: every cipher dispatch has a transcription; only 259.12 (17 Mar 1760) has none listed |
| 2772 | partly_read | high | AEF Affry 266: 12 of 15 Ogier letters have a 'Dechiffrement'; 266.13, .22, .68 have none |
| 2920 | open | low | Berger de Xivrey IV p. 297: footnote under Henri IV to Balagny, 15 Jan 1595 (Saint-Quentin copy), says the cipher part 'n'a pu être déchiffré'; survival of the cipher in the copy unknown |
| 2934 | open | low | ANTT title 'Telegramas em cifra do governo geral de Moçambique ...'; undated, extent unknown |
| 2055 | not_cipher | medium | Thomas & Peach, Correspondence of Richard Price I-III: 0 hits for 'cipher', about 25 for Price's shorthand on APS letters |
| 2777 | open | medium | AEV Supersaxo II P 74 is not Tomokiyo's solved 1520 letter (ABS 101-274); Büchi I (1489-1515) prints no c. 1510 cipher letter |
| 1211 | read | medium | ANOM COL B 7 is the clear outgoing register; 'chiffrée' entries are the clear copies, summarised by ANOM |
| 1208 | read | medium | Brymner's calendar summarises the content of the wholly ciphered F3 16 f. 115, so its copy carries the decipherment |
| 1217 | open | low | AD95 68 H 19 'une pièce chiffrée' (Forster papers), a different unit from the read 1644 letter 68 H 8 |
| 1219 | not_cipher | low | 'feuille volante chiffrée' in a merchant's journal and cash book = a sheet of figures |
| 2057 | none | | APS finding aid behind Cloudflare; needs Chrome |
| 1382 | none | | 'veelal cryptisch' says nothing about code groups; ANRI Jakarta, unscanned |
| 1214 | none | | 'systèmes de codage ?': the archivist's own doubt; needs AD24 scans |
| 1215 | none | | Bertier de Sauvigny 1951 may print it; needs AD30 scan and that book |
| 1167 | none | | series-level Archinto record, no volume named |
| 1353 | none | | DRRP has transcriptions only, no leaf images |
| 2362 | none | | ASVe guide record only, no busta |

## Routes found or confirmed

- **e-Helvetica PDFs by script.** `https://search.e-helvetica.nb.admin.ch/search-api/v1/default/search?term=<words>&rows=10`
  returns JSON with `file_pid`. `https://file-token.e-helvetica.nb.admin.ch/download/<file_pid>` returns a
  short-lived signed URL to the full PDF. This route fetched Büchi, *Korrespondenzen ... Schiner* I (nbdig-59316_1.pdf,
  243 MB, text layer). It works for any public-domain Swiss National Library scan.
- **archive.org lending books, full-text search.** `https://<server>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q=<term>`
  (server and dir from `/metadata/<id>`) searches the text of in-copyright lending items. This route searched the
  Thomas & Peach Price edition.
- **Bot checks met:** APS as.amphilsoc.org and search.amphilsoc.org (Cloudflare), HathiTrust (Cloudflare),
  archives.valdoise.fr (Anubis). DigitArq, FranceArchives and archives-online.org are JavaScript apps that give curl an
  empty page. The Google Books API was over quota.

## New lead seen in passing (not in this batch)

Büchi I, pp. 403-404 (no. 481): Heinrich Trübmann, Schiner's chaplain, to the cardinal, Sion, Nov 1515.
Source: B.-A. Sitten, Lade 101, Nr. 35, now AEV ABS 101, the same series as the solved Pechio letter ABS 101-274.
Büchi prints it with six cipher passages left unresolved: '(3 bis 4 Worte in Chiffern)', '(2 chiffrirte Worte)',
'(3 Worte chiffrirt)', '(chiffrirt 12 Worte)', '(6 Worte chiffrirt)' and '(2 Worte chiffrirt)'. Before this goes to
leads it needs checking: whether it is on DECODE, and whether the Pechio 1520 two-digit cipher reads it.

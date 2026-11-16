# Wave 20 vetting, batch b10 (16 Nov 2026)

Leads: 2586 2613 2497 2601 2610 2591 2604 2603 2498 2611 2609 2607 2506 2620 2619 2621 2624 2623 (GStA PK, ACTApro).
Proposed blocks are in `proposals.json` (leads.json and catalogue.json untouched). Scripts: `acta.py` (ACTApro search and record
fetch by plain Python, no browser), `add.py` (merge a part file), `cgrep.py` (grep Tomokiyo's unsolved.htm and Lasry's GL.htm,
fetched 15 Nov 2026). Record texts in `src/`, proposal parts in `parts/`.

## ACTApro by script (new route)

ACTApro answered curl today (not an empty page). `acta.py` GETs `search.xhtml`, copies the `searchForm` fields and POSTs with
`searchForm:searchByType=3` (Verzeichnungseinheiten; required, or the server returns "Wert ist erforderlich"),
`searchForm:searchRootDocument=''`, `resultsForPage=500`, empty date fields. Each hit's `archive.xhtml?id=` link then opens the
full record in the same cookie session (the "Vollansicht" block). One request about every 1.2 s. Broad names (Dohna, Schmettau,
Olfers with a loose filter) are slow because many hits match the filter; use a distinctive word from the title instead.

## Results

| Lead | Verdict | Deciding fact |
|---|---|---|
| 2611 | read | Zegelin item is Frederick II's order of 19 Nov 1775 TO Zegelin, 'Dechiffrierung ist überschrieben' |
| 2613 | read | Rep. 64 Nr. 722 holds an 'entchiffrierte Abschrift' of the letter of 11 July 1710 intercepted at Paris |
| 2610 | read | Esterhazy to Kaunitz, 6 Apr 1756, printed in Volz/Küntzel 1899 Nr. 65 p. 304 'Nach der Urschrift' |
| 2591 | **open** (medium) | Narrowed to Frederick II to Zieten, Lobendau 27 Nov 1757: PC 16 p. 34 n. 3 left it out because key, déchiffré, draft and copy were all missing. Goltz 1760 pieces are printed (PC Nr. 12548) or have the deciphered text filed |
| 2601 | key_lookup | Rep. 96 Nr. 97 E 1 / F list only 'Dechiffrierungscodes, [1745]' |
| 2603 | key_lookup | Rep. 96 Nr. 90 G lists only 'Geheimcodes (Chiffres) mit Schmettau, 1759' |
| 2604 | read | Nr. 85 Oo holds 'Dechiffrierte Nachrichten'; EM 19 c3 Nr. 14 is a sealed deposit of secret papers, no cipher described |
| 2607 | read | Rep. 11 Nr. 10691 = 'Abschriften und Dechiffrierungen' of Lusi 1790; bears on lead 2501 (FA Lusi Nr. 3) |
| 2620 | duplicate | Nr. 3144 is lead 2506; Nr. 3145 is keys only (key_leads) |
| 2506 | not_cipher (medium) | Full title: an attempt to make out a 'Ralliementszeichen' (rallying sign) in a ring |
| 2498 | read (medium) | PC 19-22 print the Rexin letters from drafts and déchiffrés (11 Nov check); ACTApro is title-only |
| 2609 | open (low) | Hohenfels, 15 May 1785, Bl. 46-47, 'Verschlüsseltes Schreiben', no decipherment noted; leaves not seen |
| 2497 | no verdict | Blocker stands: Nr. 959 still says only 'teils chiffriert' in a legation file |
| 2619 | no verdict | Rep. 77 Tit. 437 Nr. 6 is title-only; Adh. is a printed Trithemius book |
| 2621 | read | Rep. 81 Bern Nr. 93 = 'Dechiffrierte Berichte' of Olfers |
| 2624 | key_lookup | Rep. 89 Nr. 666: rules and cipher for Wilhelm II-Abdülhamid telegrams (via Tahsin Bey, state of 26 Nov 1898), no telegram |
| 2623 | open (low) | Westphalen Nr. 461: 'z.T. verschlüsselte Berichte', no decipherment noted; key Nr. 541 in the fonds; fold with 2502 |
| 2586 | duplicate | 14 of 22 volumes are leads 2495-2497; Nr. 945, 951, 966 'mit gleichzeitiger Entschlüsselung'; split out Nr. 753/799 (Strünckede 1725), 760 (Choupard), 718 (memoir 1709) |

## Notes for the lead agent

- Many of these files (Rep. 94 Nr. 5745, Rep. 94 A V Nr. 26, Rep. 400 Nr. 191, Rep. 81 Bern Nr. 93, Westphalen Nr. 461) are marked
  'Unbestellbar bis 31.05.2029 (Magazininstandsetzung)': no scans can be ordered until then.
- 2591's key fact is the Politische Correspondenz vol. 16, p. 34 n. 3: the November 1757 field cipher (letters to Keith 15 and 25 Nov,
  Bevern Nr. 9521/9528, Zieten 27 Nov) had no key, déchiffré or draft for the editors. Worth a look at catalogue 590 (Bevern).
- 2607's decipherments bear on lead 2501 (FA Lusi Nr. 3): re-check 2501 against Rep. 11 Akten Nr. 10691.
- Lead record errors: 2611 is an order TO Zegelin (19 Nov 1775), not his report; 2613's letter is of 11 July 1710; 2620's old
  shelfmark Fasz. 6 belongs to Nr. 3145, Nr. 3144 is Fasz. 5.
- Prior art for 2610 and 2591 comes from archive.org OCR: Volz/Küntzel 1899 (preussischeundst00volz) and PC vols. 16 and 20
  (politischecorres16freduoft, politischecorres20fred).

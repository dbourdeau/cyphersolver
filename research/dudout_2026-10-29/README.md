# Brice Dudout, corrections and findings of 29 Oct 2026

Source: Brice Dudout's email of 29 Oct 2026 and the two attached files in this folder (`CORRECTIONS-FOR-DANIEL-2026-10-29.txt`,
`martinique1765-note.txt`). His GitHub account is suspended, so his work arrives by email and patch file (`dudout/<slug>` branches).
Findings are his, not re-checked here unless a line below says so. Credit him when any of it reaches a page.

## Applied 29 Oct 2026
- `targets/mercier1761/key1765_ennery.tsv`: eight values corrected (413, 535, 89, 235, 349, 679, 652, 786); 565 and 159 stay uncertain.
- Leads closed in `research/leads.json` (`docs/_check_catalogue.py --close`, reason cites this folder): 1126, 1274, 1335, 1152, 1063,
  1064, 1068, 882, 1280, 1279 (read: existing decipherment or print), 1331, 1322 (not a cipher).
- Short notes appended to the NOTES.md of sessa1524, castelcicala1816, breves1610, ceva1632, sega1591, garcilaso1498, jones1802,
  augur1874, lopehurtado1523,.

## Held
- **meiji1874**: Satoshi, Ono Tetsuya (2010) and Nagata Junko (1989) describe the 1874 Army 7 x 7 square already. Do not present the key as
  ours; credit the three; wait for Brice's corrected series after he has read Ono.
- **castaldo1552 (1332)**: the corrections file says the letter of 15 Oct 1552 is read; his email withdraws it (validation 0.731 of words).
  Hold until he confirms. Neither a branch nor a target exists here.
- **bouille1778 (1202)**: he reports it read (455/458 words); his PR #171 is hidden while his GitHub account is suspended, so it is not here. Ask for the files or a patch by email.
- Branches awaited as patch files: harley1582r8505, asang1662 (Krakow 443), rubio1913 (Mexico 1468), biglia1565, sega1590, perez1578,
  desnoyers1659 and the rest of the list in his email. None applied yet; each is re-measured against the read bar when it arrives.

## Not yet recorded in the ledgers (existing or rejected per his file; leads unchecked or catalogue entries)
Catalogue entries (not leads, so no --close): 855, 856, 857 (contemporary glosses), 854 (letters 5 Oct 1517 and 18 Jun 1520 only),
905 = 964 duplicates of 1813, 919-921, 900, 929, 946, 988/989, 1037-1040 (existing by print or interlinear), 1058, 1065, 1534 (paired
cables read at the time), 1535 (no digitised code book), 444 (R7523 interlinear), 1446-1449 and 1460-1468 (CEHM; see the file).
Leads left open for lack of a check on the images: 1269, 1258, 1263 (1260 stays open), 1048, 1320 (only f. 392 undeciphered), 1321.
Rejected keys: R7398 for R7397; R9549 is not the second Castelcicala code; R4887 and R4913 do not fit hyde1659 (catalogue 352);
no key fits Cardona (854); the Santa Cruz keys do not fit the RAH Flanders pairs.

## Second email of 29 Oct 2026 (archive orders, leads, BnF sweep)
Files in this folder: `leads-dudout-2026-10-29.json` (as sent), `already_in_daniel.json` (his 3 matches: ital. 258/314/1636 = leads 1329/1330/1331),
`candidates.json` (his 30 leads), `bnf-bam-sweep-summary.txt`.
- **Archive ledger**: `archive_requests.json` ar-160, 162, 163, 167, 168, 255-257, 261, 265, 266, 269, 277, 281, 291-294 set to `requested`,
  volunteer Brice Dudout (contributor `dudout`, 2026-10), with a history line each. Partial orders are marked "in part" in the note
  (ar-256: OBA 26859; ar-261: Best. 3 Nr. 1450; ar-281: Werther 36 and Rep. 91 A Nr. 86; ar-293: RW 1167 II 44 keys, not II 65). ar-277 is
  a 270 EUR quote on hold. ar-269/291/292 wait for the portal account. GStA order 653#00004#0359#0004 (4-6 weeks).
- **Outside the ledger**: Catinat 15 Sept 1702 (`targets/catinat1702`): Aargau Kantonsbibliothek sent free scans of Acta Helvetica AH 52/93,
  study only until display is asked; Osborn d520 (Shield diary, catalogue 814): Beinecke free digitisation ordered 29 Oct (Aeon 1269090);
  Montcalm 1758: LAC MG18-K8 vol. 3 online on reel C-363 (no target yet).
- **Leads**: 30 rows merged with `merge.py --write` as leads 1548-1577 (sweep `dudout_leads_2026-10-29`). `known.py` found none of the 30
  shelfmarks elsewhere in the repo; `research/venice_archives/README.md` only mentions 143 unreviewed BNCF "in cifra" records. All are
  `seen: catalogue` and leads, not catalogue entries; 4 need an archive scan (NAF 29073, fr. 11270, fr. 3485/3486, fr. 3828/3835).
  Some BNCF and BnF letters may be in print (Avenel, Berger de Xivrey, Bertelli 1964): check before vetting.
- **BnF BAM sweep**: 120 queries, 675 undeciphered-looking articles, 232 volumes (93 digitised and held, 23 digitised and not held, 10
  undigitised and held, 106 undigitised and not held). Three queries returned a default page ("alphabet secret", "en cifra", nomenclateur).
  The 675-article JSON is available from him on request; not asked for yet.
- **Reading split**: he reads each lot as it arrives (key frozen, held-out validation); our re-measure against the read bar is the
  independent check. Tell him if we take any piece ourselves.
- **Blocked sources he added** (do not circumvent; browser route only, per the CLAUDE.md bot-check rule): BNE Digital / BDH (403 to scripts,
  full PDFs in a browser), MiC infrastructure (cultura.gov.it, unreachable from scripts), DigiVatLib (403), RAH Biblioteca Digital (Anubis,
  passes in a browser), ANOM IREL (anti-robot; Anubis passes in a browser), Archivportal-D (Anubis), Colmex. Same as ours: Gallica, MNL /
  Hungaricana, QDL, FranceArchives.
- **Image rule**: when images arrive he sends them with the ar- number and a note on whether they may be shown. Rhineland (ar-293/294):
  not for now, publication needs a separate permission (Virmond deposit especially).

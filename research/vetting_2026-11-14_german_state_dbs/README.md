# Vetting, German state databases sweep leads 2652-2668 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5). `research/sweep_2026-11-14_german_state_dbs` (17 rows) merged as leads 2652-2668;
`make.py` builds `vetting.json`; `python research/vet.py --check` passes. Its `key_leads.json` (5 key-only groups) was not merged.

- **Promoted (7), all `seen.kind` "not online" (record text of the archive's finding aid; no image exists online for them):** 2652 (HStAS E 50/05
  Bue 124 and 129, Degenfeld at Munich 1845-46), 2661 (Kob-Seelig, Nr. 1006), 2662 (Kob-Schneider, Nr. 998), 2663 (Kob-Fischer, Nr. 368),
  2664 (Radefeld debts, Nr. 1307), 2666 (Wallenrodt Denkzettel 1550, Hennebergica Altenburg Nr. 310), 2668 (Fritsch Bundestag reports, A XXVI Nr. 269).
  One key per entry: the three Kob correspondents are three entries.
- **Closed:** 2656 duplicate (BayHStA Kurbayern Aeusseres Archiv 4591 is the volume of catalogue 161/162 and targets kaa4591, kaa4591b);
  2665 partly_read (Reg. E Nr. 136: the key fol. 393 belongs to the Elector's letter to Luther and Bugenhagen of May 1541, printed with its
  resolutions in Mentz, *Johann Friedrich der Grossmuetige* vol. 3 Nr. 43; the lead title's "Saxon councillors" was wrong for that piece).
- **Unvetted (8), reason on each lead:** 2653, 2654, 2655 (key alphabet only), 2657, 2658, 2659, 2660, 2667.
- **Saxon digital copies viewed** (archiv.sachsen.de viewer, Chrome tab): Loc. 00694/10 is 7 microfilm frames of Krauske's 1893 key table (not
  ciphertext; the ciphertext is in 694/08, also digitised but too coarse to find the ciphered passages page by page here, and 694/09); 10736 Nr.
  00457/02 is 6 frames with no cipher sheet. Route: Archivportal-D item page, link "Objekt beim Datenpartner" for the guid, then
  `bestand.jsp?guid=<guid>&_ptabs=%7B%22%23tab-digitalisat%22%3A1%7D#digitalisat`; the DDB iiif image on the portal page is only the archive logo.
- Prior art: Mentz vol. 3 (IA johannfriedrichd03ment) OCR searched; no Wallenrodt 1550 piece in it.

# Vetting, GStA deep-sweep leads 2599-2627 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5). The sweep `research/sweep_2026-11-14_gsta_deep` (29 rows) was merged as leads
2599-2627; its `key_leads.json` (5 key-only groups) was not merged. Records were read in a Chrome tab on archive.spk-berlin.de
(search POST, then each hit's own `archive.xhtml?id=` link: the permalink ids stored on the leads open only the tectonics tree, so
the records have to be reached through a search hit in the same session). No ACTApro record carried an image: every block rests on
the archive description (`seen.kind` "not online", access "archive").

- **Promoted (9), each narrowed to one volume or letter, siblings in `folio_note`:** 2599 (Rep. 81 Dresden Nr. 782; the finding aid
  shows Voss and Maltzahn from Nr. 783, not only Klinggraeffen), 2600 (Dresden Nr. 798, two Austrian ciphered letters with Auflösung),
  2612 (Rep. 64 Nr. 952, 1709 rescripts), 2614 (Nr. 749), 2615 (Nr. 855, Goltz at Paris 1780-81), 2616 (Nr. 846, Goltz 1772-73),
  2617 (Rep. 81 Frankfurt Nr. 173, 1813), 2626 (OBA 23682, Kasimir 1520), 2627 (OBA 27533, Klingenbeck 1525; OBA 27275 is lead 2505).
- **Unvetted (20), reasons on each lead:** records that name only a key or only deciphered copies (2601, 2603, 2604, 2605, 2607, 2618,
  2620, 2621, 2622), records whose full text did not come back (2606, 2609, 2613, 2623), and 2602, 2608, 2610, 2611, 2619, 2624, 2625.
- Prior art: Politische Correspondenz vol. 5 (IA politischecorres05fred) and Joachim's *Politik des letzten Hochmeisters* vols. 1-3
  (IA diepolitikdeslet01-03joac) were downloaded and searched as OCR. Joachim vol. 3 prints OBA 26245 as Nr. 110 (lead 2625, left unvetted);
  the PC vol. 5 prints no order headed to Klinggraeffen at Dresden. friedrich.uni-trier.de did not resolve from this machine.
- Duplicates: none of the promoted volumes is in an existing entry; catalogue 593 is the Saxon-filed copy of Klinggraeffen's ciphered reports.

`make.py` builds `vetting.json`; `python research/vet.py --check` passes.

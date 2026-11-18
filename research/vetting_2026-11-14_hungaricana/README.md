# Vetting, Hungaricana sweep leads 2675-2693 (14 Nov 2026)

Run by a Claude Code session (Claude Sonnet 5.5). `research/sweep_2026-11-14_hungaricana` (19 rows) merged as leads 2675-2693 with no
region/period corrections needed; its `key_leads.json` (9 key-only items) was not merged. `make.py` builds `vetting.json`;
`python research/vet.py --check` passes.

- **Promoted (4), all `seen.kind` "not online":** 1232 (re-opened, see below), 2675 (Wyss, 11 Feb 1564, Kt. 18 Konv. 1, original, no decipherment),
  2676 (Rym, 5 Sep 1572, Kt. 28 Konv. 5, wholly cipher, only the date solved), 2677 (Busbecq, 6 Aug 1559, Kt. 14 Konv. 3, interlinear decipherment on the sheet,
  key sheet of 1559 on DECODE R1220). Each large correspondent run was narrowed to one letter; siblings are listed in `folio_note`.
- **1232 and 2683:** Donellan to Nadasdy. 2683 closed as a duplicate of 1232. Lead 1232 had been closed on 29 Oct because its date, 29 Aug 1670, was not found;
  Hungaricana BecsSeg/146748 is that letter (Fasc. 313 Konv. B fol. 91-92, 'reszben sifrir, nincs feloldasa'), the one letter of the run with no decipherment.
  The earlier block is kept as `vetting_superseded`; key sheets R686/R696/R697/R648 are on DECODE.
- **Closed read (3):** 2678 (Verancsics and Zay 1553-55, printed in MHHS IV with the interlinear decipherment), 2686 (Gerendi 1529, Schuller 1894 and Lang
  C.Jel.02-05), 2693 (Kossuth to Barics 1851, printed with decipherment in Straub 1999). The printed pages were not opened for any of the three (2693: the
  viewer pages 145-150 were searched and the Barics document was not found), and each `closed` text says so.
- **Unvetted (12):** 2679-2682, 2684, 2685, 2687-2692, reasons on each lead. Two findings explain most of the Constantinople ones: the 'nincs feloldva'
  items for Stoeckl, Czernovich and Rym 28 Sep 1572 are copies marked as duplicates, and the Fazekas-Fodor-Gluck edition *Reports of the Habsburg Envoys in
  Constantinople 1568-1574* (2 vols., Budapest-Szeged 2025) covers Wyss from 1568, Provisionali, Stoeckl and Rym; only its front matter is online, so what it
  prints is unchecked (this also applies to 2676).
- **Prior art used:** Lang Benedek's repertory (thesis 2015, `real-d.mtak.hu/922/7/dc_758_13_doktori_mu.pdf`, text layer, 918 rows `C.xxx.nn`) has Wyss
  C.Wys.01-05, Rym C.Rym.01-05 and C.Ryu.01-08, Gerendi C.Jel.02-05 and key tables T.Gev.16-18, but no Busbecq, Stoeckl, Czernovich or Donellan. DECODE
  holds only keys for these writers (R1548 Wyss 1568, R1220 Busbecq 1559, R388-390 Provisionali/Rym 1570, R686/696/697/648 Nadasdy).
- **Leaf pages:** `archives.hungaricana.hu/hu/lear/BecsSeg/<id>/` carries the regest only (shelfmark, date and place, summary, sender named); there is no image
  viewer, so no ciphertext is viewable there. HHStA images would need the archive.

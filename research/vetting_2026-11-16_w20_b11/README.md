# Vetting wave 20, batch b11 (16 Nov 2026)

18 leads: 2502 2602 2596 2608 2501 2503 2622 1620 2595 2505 1157 1134 2655 1725 1708 1713 1726 1220.
Proposed vetting blocks are in `proposals.json`, built by `make.py`. leads.json and catalogue.json were not touched.
Every vetting block passes `vetting_problems` in `docs/_check_catalogue.py`, apart from the expected "only open" message on closed verdicts.

## Results

| Lead | Verdict | Conf. | Deciding fact |
|---|---|---|---|
| 2502 | open | low | Nr. 304 holds legation reports from **Austria** (old shelfmark Rep. 1 B Oestreich), not Berlin. Nr. 393 is a press file holding ciphered reports to Linden. No Aufloesung is noted. Nr. 304, 393 and 541 (the key) are unproducible until 31 May 2029. |
| 2602 | read | high | Politische Correspondenz vol. 18 prints about 28 orders to Wedel "nach der Ausfertigung im Wedell'schen Familienarchiv". It prints no. 11314 from "der dechiffrirten Ausfertigung". The file holds 5 Dechiffrierungen. |
| 2596 | open | low | ACTApro: "Notizheft ... (z. T. verschluesselt)", ca. 1777-81. No edition or decipherment found. Cipher or shorthand is not established. |
| 2608 | not_cipher | medium | The full records show that Nr. 48 a, 52 and 54 are clear letters that only mention ciphers. Nr. 8 has "Der Rest ist nicht dechiffrierbar" (more likely illegible). |
| 2501 | read | medium | The only cipher piece is FW II to Lusi, 1 Oct 1790. Berlin holds the sending side: Rep. 96 Nr. 164 G and Rep. 11 Nr. 10691 "Abschriften und Dechiffrierungen". |
| 2503 | partly_read | low | Nl Boyen 648 holds 7 ciphered letters plus "vier masch. Transkriptionen" in the same unit. The Kunisch volume was not seen. |
| 2622 | key_lookup | high | The record is only "Enthaelt auch: 2 Schluessel zu Chiffern". No ciphered letter is named. |
| 1620 | none | - | Koeppen vol. 3 is not online, and Archivportal-D serves a proof-of-work page (the blocker stands). |
| 2595 | read | medium | Only 22687 is ciphertext, and it is filed "mit Uebertragung". 22442 only lists cipher use as a topic. 23213 is a request for an alphabet. |
| 2505 | partly_read | medium | Joachim III no. 197 prints the letter from its clear Reinkonzept. The King Christiern passage is not in the printed summary. |
| 1157 | partly_read | medium | Wickham Correspondence (1870) prints Drake's cipher letters to Wickham in clear (Venice, 3 Aug 1796). 38M49/1/141/4 is a key. |
| 1134 | not_cipher | medium | The BRAH 98 calendarist uses "indescifrable" for illegible hands and "(en cifra)" for real cipher. |
| 2655 | key_lookup | medium | The finding aid says only "Dabei: Chiffrenalphabet". No ciphered letter is described. |
| 1725 | open | medium | AIS: 28-3, fol 1-146, "teilweise verschluesselt". Same kind as catalogue 1728/1729/1735. Pribram does not cite Spanien Varia. |
| 1708 | none | - | Mur Raurell's bilingual edition of the 1724-27 Ripperda correspondence has not been seen. The Perspectivia review page served a bot check. |
| 1713 | open | low | The unit holds letters *to* Rosenberg. Juretschke prints envoys' reports and was not opened. |
| 1726 | none | - | Reports from Madrid in 1765-68 are what Juretschke III-IV would print. Not online. |
| 1220 | none | - | A cluster of 68 regests (Hungaricana 403). The 2025 edition of the Habsburg envoys' reports prints Rijm's despatches to Nov 1574. |

## Routes

- **GStA ACTApro by plain HTTP (new).** This route works without Chrome.
  - `actadoc.py` fetches `https://archive.spk-berlin.de/actaproweb/document/Vz_<uuid>` and returns the full record ("Vollansicht").
  - It works for random-UUID records. It does not work for name-based (v5, `...-5xxx-...`) UUIDs such as Woellner Nr. 6 and the OBA units: those return the frame only.
  - `actapro.py` POSTs the JSF search form (ViewState plus cookie), 100 hits per page, and gives each hit's header and Kopfregest. Use it for the v5-UUID records.
- HHStA AIS: `detail.aspx?ID=<id>` answers curl. None of the units has a scan.
- TNA Discovery API details: work.
- Internet Archive OCR: Politische Correspondenz vol. 18 (`politischecorres181freduoft`, `...182...`), BRAH 98, Wickham Correspondence, Pribram.
  - The Linnebach Scharnhorst OCR is unusable Fraktur.
- Bot checks: perspectivia.net (JS verification), Archivportal-D (proof-of-work, not tried again), Hungaricana (403, not tried again).

## Record errors

- **2502:** Nr. 304 holds reports from the legation in Austria (Rep. 1 B Oestreich), not from Berlin. Nr. 393 is titled "Presseangelegenheiten". Both units and the key, Nr. 541, are "Unbestellbar bis 31.05.2029".
- **2608:** three of the four letters are not cipher. The title "with ciphered lines or enclosures" is wrong.
- **1157:** 38M49/1/10/1-51 is "Letters from Francis Drake, Genoa, Milan, Padua and Venice", not general foreign correspondence.
- **1134:** "in part undecipherable" is a mistranslation. The calendar means partly illegible.
- **2595:** not every unit is a cipher letter. 22442 is a letter that lists cipher use as a topic, and 23213 is a request for an alphabet.

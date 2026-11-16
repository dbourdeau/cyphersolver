# Vetting, dbourdeau (2026-11-14)

Run for dbourdeau by an AI agent, 14 Nov 2026, following `research/VET.md`. Leads 2930-2936 and 2940. Leads 2937 and 2938 were taken by another session and not touched. Result: 8 leads, all `unvetted`. None has any image online, so no ciphertext was seen. A true `unvetted` was chosen over a weak `open`, since each description only says that a cipher item is somewhere in a mixed folder.

## Per lead

- **2930** AHU OP16696, Berne arbitration 1897. DigitArq API: `hasImages` false; whole description is "Contém relatórios, e documentação cifrada." No count, no sample. Unvetted: needs an AHU scan.
- **2931** AHU OP16752, OP16773, OP16774, OP16775 (Lourenço Marques railway and port folders). All four `hasImages` false. Each lists "telegramas cifrados" among maps, press cuttings, projects and reports (OP16773: also 7 drawings; OP16775: 3 drawings and a photograph). Unvetted: no count, no sample.
- **2932** AHU OP19560, Mozambique telegrams 1891-92. Description "Referentes a negócios estrangeiros. Contém cifrados." `hasImages` false. Unvetted.
- **2933** AHU OP17197, Cape railway conference 1898. "Correspondência, contém telegrama cifrado." One telegram, no image. Unvetted.
- **2934** ANTT JLC/007/00007. Title only ("Telegramas em cifra do governo geral de Moçambique para destinatário não identificado"); description field empty, undated, `hasImages` false. Unvetted. Several sibling JLC items are already catalogue entries (known.py hits).
- **2935** AHU MU-GM Teleg folders 1947-50. Fetched Mozambique 1947 (Teleg00401), Angola 1947 (Teleg00014) and Cabo Verde 1947 (Teleg01082): descriptions are only "Telegramas n.º 1 – 199" (and "1 - 83"), `hasImages` false. Whether the folders keep cipher groups or the decoded copy is unknown, and no key books are held. Unvetted.
- **2936** Dawes, Cadbury CMS/B/OMS/C/W/O31/1-138. The record sits under the id `XCMS/B/1803-1880/W/O/13-100/31` (the id in the lead's link returns "does not exist"; items /29 and /30 have no records of their own). The only text is "/29 Letters to used for cypher 1823; /30 Key to cypher 1823". That could be an enciphered letter plus its key, or an alphabet plus its key, so neither `open` nor `not_cipher` is honest. Adam Matthew's CMS microfilm edition (CMS V Part 1 reels) may show the leaves; it was not opened. Unvetted.
- **2940** Hicks Pasha registers, Durham SAD.866/5/1-46 and SAD.600/2/1-35. Finding aid fetched (reed.dur.ac.uk): both entries read "Language: English, Arabic and cypher"; SAD.600/2/ also lists enclosures (promotions list, food list). No image or digitised link. Daly's *The Road to Shaykan* (1983) is cited for letters to Hicks's wife (SAD.600/1), not for the registers. Unvetted.

## Duplicates and prior art run

- `known.py` for each shelfmark, correspondent and title: hits only the lead's own row and its sweep README/candidates, except 2934 (sibling JLC items already in the catalogue under other shelfmarks) and 2940 (the earlier sweep_2026-11_ireland_uk_univ README that set the Hicks papers aside).
- `decode_search.py` (DECODE): "Lourenço Marques", "Delagoa", "Moçambique", "Mozambique", "Cabo", "Luciano de Castro", "Arquivo Histórico Ultramarino", "Torre do Tombo", "Dawes", "Church Missionary", "Antigua", "Hicks", "Sudan", "Khartoum": 0 records. "Berne" returned only unrelated Vienna Chiffrenschlüssel; "Durham" one BL Egerton 1654 record. Shallow keyword search, so weak evidence.
- Tomokiyo: `cryptiana.web.fc2.com/code/unsolved.htm` and `code/GL.htm` (Shift_JIS) fetched and grepped for Hicks, Dawes, Portugal, Mozambique, Lourenço, Luciano, Ultramar, Durham: no hit. Lasry's key list has no Portuguese colonial, CMS or Hicks entry.
- Web searches (distinct per lead): Delagoa Bay Berne arbitration cipher telegrams (only Hansard and FRUS context, nothing on the cipher); Portuguese telegram ciphers and the 1890 Ultimatum (no source on the code); Hicks register and Daly (nothing says the cypher entries were decoded); Dawes cypher key (nothing; his Antigua correspondence is in the CMS archive and on Adam Matthew microfilm); Lasry/HistoCrypt Portuguese colonial (only Dinnissen and Araújo's 1649 Portuguese ciphertexts, unrelated); José Luciano de Castro cipher telegrams (nothing). No printed edition covering any item was found.

## Routes

- DigitArq: `/api/docs/details/<id>` works from plain curl, no bot check, 2-3 s between calls (as the sweep README says).
- Cadbury CalmView: `calm_record.py` in the sweep folder, with the `XCMS/...` id form. Durham finding aid: plain curl, no block. IIIF at Durham not used: nothing to open.
- No login or CAPTCHA was met. Chrome was not needed or used.

## What is left

Every lead needs an image: AHU/ANTT reproduction orders (2930-2935), a Cadbury scan or the Adam Matthew CMS reel (2936), a Durham scan request (2940). 2933 (one telegram) and 2936 (key or text) are the quickest to settle.

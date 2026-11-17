# Vetting wave 20, batch b14 (16 Nov 2026)

18 leads. `proposals.json` holds the proposals; `build.py` writes it. Three verdicts (one read, two not_cipher), 15 not assessed.
Images in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 1900 | read | high | Vestigia maps the DF set to ASMo Ungheria b. 2. Every cipher piece outside catalogue 348 has its decipherment filed with it: interlinear (seen on DF 295943 and 295948; Vestigia notes for 295991 and 295992), an attached slip (295978), or a "b" clear copy (41b, 42b, 44b, 14b, 31b, 37b). The rest are clear or are catalogue 348's letters |
| 1363 | not_cipher | high | NAI Descriptive List of Secret Dept Records vol. II, 1 Nov 1779 No. 8: a clear 2-page A.L.S. asking J. P. Auriol for the cypher to read Goddard's letter |
| 1356 | not_cipher | medium | Calendar of Persian Correspondence VII no. 1670 (OR 483): a plain news letter. "Secret code" comes from the machine-translated title |
| 2124, 2090 | none | | Morgan 403 (Cloudflare) |
| 2292 | none | | DBBTI IV shows only a clear postscript of a lost ciphered letter in inv. 1698. It prints a selection, so this is not decisive. Needs an MZA scan |
| 1408-1410, 1416-1419, 1421, 1422 | none | | NAA items not digitised; RecordSearch 403 |
| 1357, 1361, 1362 | none | | Abhilekh Patal 202 bot shell. For 1361 and 1362, NAI Descriptive List vol. VII (1787-88) would decide, but it is not on archive.org |

## Routes

- **Vestigia** (`www.vestigia.hu`) answers by script:
  - `api/search?search=<DF number>` returns the full record JSON: language tag `olasz, titkosírás`, notes, publications, incipit.
  - Decipherment copies are sub-records `<DF>-a` / `<DF>-b`.
  - `documents/<vestigia_id>` embeds the image URLs in its Inertia `data-page` JSON, at 2731x4096.
  - Scripts: `vdf.py`, `vsub.py`.
- **NAI Descriptive List of Secret Department Records** on archive.org, OCR text by curl. It footnotes cipher letters ("Part of this letter is written in cypher"):
  - vol. II 1776-80: `descriptivelisto030631mbp`
  - vol. III 1781-82: `unoz-...`
  - vol. VI 1785-86: `wwrm-...`
  - vol. VIII 1789-90: `tdl.36637-...`
- **Calendar of Persian Correspondence** vol. VII: `calendarofpersia07indi`.

## Corrections for the lead agent

- **Catalogue 348** (Costabili 1491-92, DECODE R1162-R1168):
  - It holds the same Vestigia items as the lead: DF 295908, 295909, 295935, 295963 (+44b copy) and 295974 (printed in clear, Berzeviczy 1914 no. CLV).
  - The rectos of DF 295908 and 295935 carry interlinear decipherments.
  - Its open status should be rechecked. DF 295909 and the R1165 piece (b. 2/20 no. 12) were not looked at here.
- **Lead 1900:**
  - "catalogue 361" should read catalogue 348.
  - The "zifara" quote comes from the 44b decipherment copy.
  - DF 295812 is plain Italian, printed in MDE IV.
- **Lead 1363:** the title (Governor-General to Fort St George) is wrong. The piece is the Commander-in-Chief's secretary to J. P. Auriol, Bhagalpur 26 Oct 1779, filed under 1 Nov 1779 No. 8.

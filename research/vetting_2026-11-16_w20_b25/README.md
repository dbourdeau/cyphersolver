# Wave 20 vetting, batch 25 (16 Nov 2026)

Leads: 2145 2115 2201 2511 2508 2509 2510 2512 2516 2765 2879 2881 2880 2065 2107.
Proposals are in `proposals.json` (the lead agent applies them). One file per lead is in `p/`. `add.py` merges a lead into
proposals.json, `lisola.py` builds the five Pribram/Lisola proposals, and `tg.py` greps the local copies of Tomokiyo's and
Lasry's lists (fetched 15 Nov 2026). Images and PDFs are in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2145 | none | medium | UA page: the "telegrams, some in code" are clippings and copies compiled for Vázquez Gómez's *Memorias políticas* (1933); the originals are at SIU Carbondale. No item named. UA ArchivesSpace returns 403 and AAO shows a Cloudflare check |
| 2115 | none | low | TARO now serves an Anubis proof-of-work page; the sentence matching "cipher" is still unread |
| 2201 | none | medium | DigiVatLib manifest still 404. "Copie di lettere inviate in cifra" may be clear register copies |
| 2511 | open | medium | Pribram p. 148 note "Ein Bericht vom 3. März ist nicht dechiffrirt" confirmed in both OCR copies |
| 2508 | open | medium | Pribram pp. 284-285, four "nicht dechiffrirt" notes, confirmed |
| 2509 | open | medium | Pribram p. 316 "2 1/2 Seiten nicht dechiffrirt", confirmed (second OCR copy only) |
| 2510 | open | medium | Pribram p. 317 "Folgt noch eine nicht dechiffrirte Seite", confirmed |
| 2512 | open | medium | Pribram p. 547 "Folgt eine nicht dechiffrirte Stelle", confirmed |
| 2516 | open | medium | UA XIV/2 p. 1186 n. 1, "ein längerer nicht dechiffrirter Passus", confirmed in the OCR |
| 2765 | not_cipher | high | Full VLA regest: only "(Unterschrift auf einem Schreiben an Dr. Christoph Schalck in Geheimschrift)", a disguised signature |
| 2879 | none | medium | Telegram seen: 2-digit groups with red interlinear kana from the 1874 9x9 grid (i14_a0133); the resulting kana do not read as Japanese to me. Needs a Japanese reader |
| 2880 | not_cipher | high | Both volumes of the Enomoto report are clear Japanese prose; the 暗号表 i14_a3051 is a code table |
| 2881 | not_cipher | high | i14_a0133 = 電信秘號九九格 + 増補改正暗号 tables, a key with no ciphertext; it matches the 2879 red kana |
| 2065 | none | low | WVU record readable again: A&M 1841, "Part of the message appears to be in code" (hedged); OR Ser. I vol. 2 not checked |
| 2107 | none | low | Catalogue line only; the sibling diary is "partly in shorthand" |

## Routes found today
- **Waseda Okuma Papers while kotenseki is in maintenance:** `http://hdl.handle.net/2065/<n>` redirects to
  `https://waseda.repo.nii.ac.jp/records/<recid>`. `GET /api/records/<recid>` gives JSON with the PDF URL
  (`/record/<recid>/files/<name>.pdf`, which redirects to object storage; use `curl -L`). Full colour scans.
- **Vorarlberger Landesarchiv findbuch by script:** see `vla.sh`. Search with a POST to `rech_start.php`, then a POST to
  `rechergs.php` with the result keys joined by `~`, then `props.php?kind=ve_e&ve_id=..&be_id=..` returns the full regest.
  No Chrome needed.
- TARO (txarchives.org) now sits behind Anubis proof-of-work. Arizona Archives Online shows a Cloudflare check;
  archives.library.arizona.edu returns 403. The Google Books API answered 429 (daily quota) today.

## Side findings
- VLA VOKA AN 629 "Geheimschrift, Arkana, Chiffrierungsschlüssel" (undated) is already among the Austria/Swiss sweep's key leads.
- Pribram 1887 has two more "nicht dechiffrirte Stelle" notes outside this batch: a longer passage after the precedence
  dispute report (cf. 24 July 1657), and p. 543.
- 暗号電報訳文 (i14_a4670) does not translate the Motono telegram: it is katakana with ン, a sign the 9x9 grid lacks,
  and it does not read as Japanese either. It could be a target in its own right.

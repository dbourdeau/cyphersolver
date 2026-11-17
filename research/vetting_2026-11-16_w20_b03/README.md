# Vetting wave 20, batch b03 (16 Nov 2026)

18 leads: 2208 2398 2919 1941 1942 1301 2866 2863 2852 2853 1442 2373 2047 1997 2048 2000 1998 1999.
Proposals in `proposals.json`. Nothing was applied to `research/leads.json` or `catalogue.json`. The vetting blocks of the two `open` proposals pass `vetting_problems`.

Scripts: `add.py` (merges one proposal into proposals.json), `get_t7519.py` (downloads the 96 ANC1-1-T-7519 images), `sheets.py` (contact sheets). Images are in `img/` (git-ignored).

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2208 | none | high | Aggregate of about 22 ASGe volumes, none digitised. The lead's volume numbers are mis-read, and cipher volumes start in 1730, not 1746. Split it, starting with the keys (vol. 47 c. 166, vol. 89 cc. 126-132). |
| 2398 | open | low | Inventory n. 152 (fetched from saassipa.cultura.gov.it): 'Lettera in codice e in cifrato ... primo ventennio del XIX secolo', no transcription listed, while the neighbour n. 263 lists one. The 1861 date belongs to n. 263. |
| 2919 | open | medium | Teulet IV p. 309 (IA leaf n325) prints a 33-sign cipher subscription with the note 'Je n'ai pas pu retrouver la clef'. No later reading was found. |
| 1941 | none | high | AHNOB unit has no images. The bare 'Cifrada' can hide a marginal decipherment, as on the sister unit (lead 1940). |
| 1942 | none | high | Same as 1941 (AHNOB Montealegre C.1 D.22). |
| 1301 | key_lookup | medium | EHMCM 38 (2009) p. 143 prints the full key of Torrens's 10 x 7 matrix cipher, and notes 2 and 3 of 1826 are wholly in it. |
| 2866 | partly_read | medium | AGN Navarre record files a 'Traducción al castellano' with the partly enciphered letter. |
| 2863 | duplicate | high | OP16696 = lead 2930, OP17197 = lead 2933. |
| 2852 | none | medium | ANC record text is truncated, and the full text is behind reCAPTCHA. Ciphertext versus clear copies (made 1940-45) is undecided. |
| 2853 | read | high | 96 images paged through: the only cipher telegram (img 003/005, Valencia Guerra 19072, 'Clave general T en H') has its typed decipherment on img 002. |
| 1442 | none | high | Harvard 403 to curl and to Chrome. |
| 2373 | none | high | BAV Barb. lat. 9863 not digitised (manifest 404), and the volume is 'cifre e decifrati'. |
| 2047, 1997, 2048, 2000, 1998, 1999 | none | high | BayHStA Kasten blau: analogue only, bare 'Chiffren' (possibly keys). |

## Routes found or confirmed

- Arxius en línia: the backend `unitat/objects?codiReferencia=<ref>`, `unitat/search/basic` and `unitat/detail?codiReferencia=<ref>` all work by curl with an Origin header, and so does the static image host. `unitat/detail/full` (the full description) needs a reCAPTCHA token: needs Chrome.
- Palermo: `saassipa.cultura.gov.it` PDFs now download by curl. `digitalibrary-saassipa.cultura.gov.it` still does not resolve (curl and WebFetch).
- Wayback (`web.archive.org`) returned its "abusive bot traffic" block to curl on 16 Nov 2026. The sweep's extracted inventory text (`research/sweep_2026-11_B_unswept_south/_dl/wb_genova_hits.jsonl`) was used instead.
- Internet Archive page images: `https://archive.org/download/<id>/page/n<leaf>_w1200.jpg`. Take the leaf from `<id>_hocr_pageindex.json.gz` plus `_hocr_searchtext.txt.gz`, not from `_page_numbers.json`, which was off for Teulet IV.
- Harvard (id.lib, api.lib) gives 403. PARES answers curl with a 302 redirect.

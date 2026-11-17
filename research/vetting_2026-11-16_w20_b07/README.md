# Vetting wave 20, batch b07 (16 Nov 2026)

Leads: 2750 868 1257 2811 2211 2129 2598 2660 1885 1886 2672 2454 2936 1610 2812 1539 1542 1543.
Proposals are in `proposals.json` (merged from the per-lead files in `parts/` with `add.py`). Nothing
in `research/leads.json` or `catalogue.json` was edited. The blocks with a `vetting` field pass
`_check_catalogue.vetting_problems` (apart from the expected "only open enters" line for closed verdicts).
Tomokiyo `unsolved.htm` and Lasry `GL.htm` (fetched 15 Nov 2026) were grepped with `cgrep.py`.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2750 | open | medium | BnF notice cc59029 confirms NAF 11238, Abelard epistle in "caracteres cryptographiques" (Villette 1768), no decipherment, not digitised |
| 868 | open | medium | Discovery API: Carte 75 ff. 498-499 "Original; in cypher"; Harris, Life of Sandwich (1912) vol. 2 never cites ff. 493/498 or prints them; DECODE R499 a candidate key |
| 1257 | none | - | C.392 half printed in Sbornik 61 (split off as read); A.286 half unseen; Bodleian ArchivesSpace now Anubis bot check |
| 2811 | none | - | "some in cipher" only; received originals, clear drafts in FO 74; Bodleian bot check; Talbot b. 29 keys in the same collection |
| 2211 | read | medium | Manus item 45 spans cc. 91r-92r: decipherment inside the cipher bifolio, content summarised |
| 2129 | none | - | "some entries in code" may be paroles; ArchiveGrid Cloudflare 403, SNAC bot check |
| 2598 | read | high | Hume, CSP Spanish Eliz. vol. 1 calendars Quadra to the King, 10 Jan 1562 and 27 Jan 1563, in English; BU file is a researcher's working file |
| 2660 | none (key only) | high | BLHA REST record 1097847: Bl. 1100-1259 "Chiffrierkode der engl.-hannoveranischen Armee 1759" - a key; move to key leads |
| 1885 | read | medium | Discovery API: "Copy of cipher letter ... Read in Court 17 August 1779", content summarised - the Court's deciphered copy |
| 1886 | read | medium | Discovery API: "Copy of cipher letter" to Carmarthen copied for the EIC, content summarised - a clear copy |
| 2672 | none | - | "Primarily in Greek"; not digitised |
| 2454 | none | - | Burgerbib records confirmed by curl; Dubler 1940 not found online; split Fischer 1815 from the 1802 card-index items |
| 2936 | none (key only) | medium | CalmView (id with X prefix): only /29 "Letters to used for cypher" and /30 "Key to cypher" - an alphabet and key |
| 1610 | none | - | no scan; Hub Cloudflare, CUDL 403; shorthand not excluded |
| 2812 | none | - | Cambridge ArchiveSearch CloudFront 403; Letters to Grant Richards (1952) not seen |
| 1539 | not_cipher | medium | calendar: item 91 "receipt of ciphered message" vs item 93 "part of message in cypher" (catalogue 1538) |
| 1542 | none | - | notebooks probably route-cipher key books; nothing seen |
| 1543 | none | - | "possibly in code"; needs CPL scan; place is Columbus, Miss. |

## Access routes found
- TNA Discovery: the page is empty to curl/WebFetch, but `https://discovery.nationalarchives.gov.uk/API/records/v1/details/<id>` with `Accept: application/json` returns the record.
- BLHA: `/rest/search` answers 500, but `https://blha-recherche.brandenburg.de/rest/records/<pk>` returns the full record JSON, including the "Enthält" field.
- Burgerbibliothek Bern scopeArchiv detail pages answer curl.
- Cadbury CalmView: the CMS record needs the `XCMS/...` id.

## Bot checks met (16 Nov)
Bodleian ArchivesSpace (Anubis), OCLC ArchiveGrid (Cloudflare 403), SNAC (JS check), Archives Hub (Cloudflare), CUDL (403),
Cambridge ArchiveSearch (CloudFront 403). PARES not tried (429 all day).

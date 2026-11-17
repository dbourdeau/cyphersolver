# Wave 20 vetting, batch b20 (16 Nov 2026)

Leads: 1872 1873 1874 1875 1878 2552 2527 2199 2200 2203 2658 2657 2659 1513 1297 2905 2906 1678.
Proposals in `proposals.json` (built from `parts/<id>.json` by `add.py`; `mk_saxon.py` and `mk_blocked.py` write some parts).
Nothing here edits `research/leads.json` or `catalogue.json`. Tomokiyo's unsolved.htm and Lasry's GL.htm were the copies
fetched 15 Nov 2026 (`cgrep.py` greps them). Images in `img/` (git-ignored); fetched records in `src/`.

| id | verdict | conf. | deciding fact |
|---|---|---|---|
| 2552 | key_lookup | high | Galt's three unglossed passages (images 549 postscript, 587, 609) use the same sign alphabet that the chancery glossed in the margin on image 545 and the upper passage of 549 (all seen at full size today) |
| 2527 | read | high | Fridericia, Danske Magazin 5. r. II (1889-92), prints Otte Krag's letters of 9, 16, 23 Mar 1648 with every cipher part deciphered from the Krag key in the Rigsarkivet |
| 2657 | read | high | archive title 'Dechiffrierte Briefe ... vom Feldwachtmeister de Vela' |
| 2658 | partly_read | medium | Krauske 1893 'Einige Chiffre-Aufloesungen' plus a reconstructed code table for Manteuffel's 1712-13 reports |
| 2659 | read | medium | archive note 'Enthaelt u. a.: Entschluesselung chiffrierter Schreiben' |
| 2905 | open | medium | key volume Loc. 03234/06 holds 'une feuille non dechiffree' with the Albani/Lagnasco keys; no print or DECODE trace; Albani was cardinal of S. Clemente from 1722, so the item is 1722+, not 1692 |
| 1872-1875, 1878 | none | - | RGIA leaves not online; fgurgia.ru JS-only to curl; file titles only |
| 2199, 2200 | none | - | APUG volumes, Manus index titles only; gate.unigre.it bot check |
| 2203 | none | - | BNC Rome Gesuitico 204 not digitised; no duke/envoy/year to search |
| 1513 | none | - | Chilean volume-level aggregate; not digitised |
| 1297 | none | - | HOLLIS 403 to curl |
| 2906 | none | - | 'Zettel mit Chiffren' in an arrest file: ciphertext or key list unknown |
| 1678 | none | - | 'Verwendung von Geheimschrift' is one topic in a list; may be discussion, not ciphertext |

## Notes per lead

- **2552 Galt.** Images 48962266/70/308/330 fetched from api.rigsarkivet.dk. Same triangle-and-hook sign alphabet on all four; image 545 and
  the body passage of 549 have the Danish plaintext in the left margin. Ahnlund's edition (1920) not online (archive.org, Google Books API).
- **2527 Krag.** Fridericia's edition is a free PDF at ronlev.dk (`/bibliotek/3364.pdf`). His introduction: three keys found in a key
  collection in the Rigsarkivet resolved with certainty all cipher parts of the printed letters (one system of Otte Krag, one of Peder Vibe
  to 1652, one of Juel and his correspondents from Dec 1652); only Vibe's letter of 6 May 1655 (Erik Krag's new cipher) stayed unread.
  **This bears on the written-up targets vibejuel1649 and vibejuel1651** (same unit, Vibe's letters): their NOTES say no edition was found,
  but Fridericia prints Vibe's letters deciphered. Record errors in 2527: writer is Otte Krag (signed 'O. Kragh'); image 58 is 'N. 288',
  16 Mar 1648; image 60 is 'N. 5, N. 291', 23 Mar 1648.
- **Saxon leads.** archiv.sachsen.de answers curl; `digitalisatExists` in the page script says whether a digital copy exists. DDB Solr
  (`api.deutsche-digitale-bibliothek.de/2/search/index/search/select?q=id:<id>&wt=json`) returns the full record and `provider_item_id`
  (DE-D271_<guid>) for the archive link.
- **1678 Bruehl.** Dates per the archive: 1739, 1746, 1748-1749, 1750, 1752 (lead says 1739-1745); formerly Geheimes Kabinett Loc. 30539/2.
- **1878.** File dated 1917-1918 by the archive (lead says 1917).

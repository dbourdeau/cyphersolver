# Vetting, ajbeling (14 Nov 2026)

Run by Andrew Beling (GitHub ajbeling) with AI agents: a Claude Code agent, model claude-opus-5-5, working from his
own computer and network, with his Chrome for pages behind bot checks. Seven leads whose blocker a digitization recheck
of 13 Nov 2026 had lifted or narrowed. Before starting, open issues and pull requests were searched for each id and
correspondent (`gh api search/issues`, 13 Nov 2026): none names these leads. `python research/vet.py --check
research/vetting_2026-11-14_ajbeling/vetting.json` prints `result: pass`.

## Leads

- **1208** Vaudreuil to Berryer, 29 Aug 1760 (ANOM COL F3 16 f. 115): `unvetted`. Brymner's calendar (*Report on
  Canadian Archives 1899*, Supplement) confirms it is a cipher despatch ("Cette dépêche est chiffrée", 8½ pages) and
  that it follows the letter of 13 Aug 1760 read in `targets/vaudreuil1760`, so the 1757 Vaudreuil table is the
  likely key. The leaf is not online. The Héritage frames earlier linked to it (reel C-10523, frames 372-373) are a
  different letter: the reel's contents list and frames 360-381 make them F3 16 ff. 12-19, Vaudreuil to the minister,
  Montréal, 15 April 1760, whose two short cipher passages are copied with their decipherment.
- **1151** Whitworth (Moscow), 1707-08 (TNA SP 91/5): `partly_read`. *Sbornik* of the Russian Historical Society vol. 50
  (1886) prints his despatches from 24 March 1708 in English and Russian from deciphered copies, marking groups left
  unread. The earlier months (with ff. 108 and 163) belong in vol. 39, not found online. Overlaps catalogue 863.
- **868** Arlington to Sandwich, 1666-67 (Bodleian MS. Carte 75): `unvetted`. *Original Letters* (1724) vol. 2
  prints the other side (letters from Madrid to Arlington, 55 passages marked "Cypher."), not Arlington's two letters.
  DECODE R499 (TNA SP 106/6, 1667, Spain) is a key that may belong to this channel.
- **1576** Henri IV to Béthune, 1602-05 (BnF Français 3485/3486): `unvetted`. *Lettres missives* tome VI is not online
  by any route tried (HathiTrust has tomes 1-4 and 7-9, the Internet Archive 1-5, 8, 9); the letters are not imaged.
- **2091** Craig to Cornwallis, Wilmington, 23 July 1781: `read`. The copy in the Papers of the Continental Congress
  (item 51 p. 705, National Archives Catalog naId 475670722, image 552) has its 18 cipher passages translated on p. 759
  (image 582); both seen. Upstream's `targets/balfour1781` lists the copy as item D.
- **1036** Jay (Madrid) to Huntington, 28 Jan 1781: `read`. Founders Online (Jay/01-02-02-0151) prints it decoded
  from Jay's own decoded draft; the code is Boyer's *Royal Dictionary*. The letter is short and only partly in code.
- **2110** Spinelli archive (Beinecke GEN MSS 109): `partly_read`. Tommaso Spinelli's Barcelona letter of 7 Sept 1519 is
  now online at Yale (10844890, seen: 9 + 2 lines of symbol cipher, no decipherment on the leaf) and DECODE R2855 marks it
  decrypted with Domnina's 2015 key; upstream closes these letters as read in part (catalogue 306). Piero Spinelli's
  30 letters are not digitised: better split into their own lead.

Count: read 2, partly_read 2, unvetted 3.

## Routes and logins

| Route | Result from this network |
|---|---|
| heritage.canadiana.ca (IIIF manifests and images) | works with curl, no bot check |
| recherche-anom.culture.gouv.fr | Anubis page to curl; notices open in Chrome |
| francearchives.gouv.fr | needs JavaScript; not used |
| catalog.archives.gov proxy records API and medialz images | works with curl |
| founders.archives.gov | full text in Chrome |
| collections.library.yale.edu (IIIF), de-crypt.org | work with curl |
| archive.org full-text search (`services/search/beta/page_production`, `service_backend=fts`) | works with curl |
| catalog.hathitrust.org | 403 to curl; passes in Chrome |
| Gallica | blocked from this network (recheck of 13 Nov) |

## What is left

- 1208: ANOM COL F3 16 f. 115 (microfilm 247 MIOM 13) by reproduction order; Brymner also marks F3 16 f. 26 (3 May
  1760) and f. 50 (June 1760) as partly in cipher.
- 1151: *Sbornik* vol. 39 for January 1707 to March 1708.
- 868: Bodleian MS. Carte 75 ff. 493, 498-499; Harris, *Life of Sandwich* (1912); DECODE R499.
- 1576: *Lettres missives* tome VI (a library copy) or BnF images of Français 3485/3486.
- 2110: split Piero Spinelli's letters (box 126, ff. 2560-65) into a new lead.

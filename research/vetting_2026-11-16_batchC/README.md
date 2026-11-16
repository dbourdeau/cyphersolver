# Vetting batch C, 16 Nov 2026 (wave 19)

Leads: 1857, 1859, 1861, 1864 (RGIA Ф. 560); 2071, 2119 (Morgan); 2116 (Benson, de la Garza); 2146 (Lilly);
2197, 2198 (APUG Concilio di Trento); 2491 (Melas archive). Proposals are in `proposals.json`. **None gets a vetting
block: no lead could be assessed.** All eleven had already been tried at least twice (vetting_2026-11 b/c/n/r/t
batches, vetting_2026-11-04 arch05/07/08, vetting_2026-11-11 out_01-07). This pass repeated none of those checks; it tried new
routes only. Script access only (curl, WebFetch, WebSearch, the Google Books feed in `research/gallica_sweep/gb_feed.py`).

| id | verdict | confidence | deciding fact |
|---|---|---|---|
| 1857 | none | medium | KAISA object JSON: no scans, no annotation; ciphertext or deciphered copies unknown |
| 1859 | none | medium | as 1857; Pokotilov's 1897-98 telegrams exist in clear (prlib.ru digitised items, Krasny Arkhiv 1922), so the case may be deciphered texts |
| 1861 | none | medium | as 1857; 180 leaves of outgoing telegrams, probably clear drafts |
| 1864 | none | medium | as 1857; 571 leaves; lead date wrong (contents May-Aug 1905) |
| 2071 | none (probably read) | medium | Ribier II pp. 768-769 prints King to Angoulême, '14. Aoust' 1558; Morgan leaf (13 Aug) still unseen |
| 2116 | none | low | cipher real; Smoot 2022 says de la Garza's intercepts reached Hitt; Osorio still unopened |
| 2119 | none (probably printed) | medium | Akkerman CES II prints Morgan 161689 (no. 107a, to Rusdorf); this lead is Morgan 161690 |
| 2146 | none | high | Lilly finding aid (Wayback) has 'No content inventory'; no coded item named |
| 2197 | none | medium | blocker stands; gate.unigre.it may hold APUG images (Cloudflare) |
| 2198 | none | medium | CT X prints G. B. Cervini letters of 1546 (e.g. 24 Apr, pp. 891-892) within the register's span |
| 2491 | none | medium | holder is the Benaki Museum Historical Archives, not GAK; Natalia Mela's 1926 book unopened |

## Routes and results, by lead

- **RGIA (1857, 1859, 1861, 1864).** fgurgia.ru answered curl on 16 Nov (on 3 Nov the connection was refused). The object
  page is a JS shell; the case attributes come from `https://fgurgia.ru/ajax/obj/<id>/286525?children=false`
  (`rgia_obj.py`). For all four cases 'Наличие отсканированных листов' is empty, images and files are [], and the
  annotation is empty (1864 only gives the languages). Leaf counts: D. 68 180, D. 48 571, others none. prlib.ru (the
  Presidential Library, which has digitised RGIA telegrams of Pokotilov from Peking, nodes 324325, 324327 and 324328)
  shows a 'Security Check' bot page to curl and WebFetch: it needs Chrome. Web searches on the shelfmarks found no citation.
  A search summary mentions Krasny Arkhiv (1922), the Finance Ministry's correspondence with Pokotilov and Pavlov, Jan-Sep 1898,
  on bribing Chinese dignitaries. It was not opened.
- **2071.** Ribier II djvu text (archive.org bub_gb_qWTswSr32NYC) re-read: pp. 768-769, 'Le Roy à M. l'Evesq.
  d'Angoulesme Ambassadeur à Rome', dated '14. Aoust' with no place, about 1.3 printed pages on the Caraffa nephews. The Morgan record
  is themorgan.org/literary-historical/103825 (from a search result). It returns 403 to curl and WebFetch, and Wayback has no copy.
- **2119.** Google Books feed on Akkerman CES II (CA1T_SaqiicC): the edition cites 'Pierpont Morgan Library, New York,
  Rulers of England James I / 161689 - MA Unassigned, no. 107a. Address: A Monsieur de Rustorf a Hamburg' (signed
  secretarial original, hand of Theobald Maurice). The lead's letter is Morgan 161690. No snippet tied 161690 to a letter number.
- **2116.** Google Books feed: Smoot, *Parker Hitt* (2022, y90uEAAAQBAJ) mentions messages of 'Lazaro de la Garza,
  an agent for Mexican revolutionary leader Pancho Villa at Ciudad Juarez' in Hitt's code-breaking effort. Osorio's
  *Correspondencia de Francisco Villa* (eds 1986/88 and 2006) appears in the feed with no preview.
- **2146.** Wayback snapshot (20250517195535) of archives.iu.edu/catalog/InU-Li-VAD4730 says 'No content inventory'.
  The only cipher sentence is the collection-level one already quoted in the lead.
- **2197/2198.** gate.unigre.it (APUG's GATE wiki, project Monumenta Concilii Tridentini, with transcriptions and some images
  of Trent codices) is behind Cloudflare. Its Wayback works list is a JS table. For 2198, Google Books feed snippets show
  Concilium Tridentinum X prints G. B. Cervini letters from 'C. Cerv.' (24 Apr 1546 at pp. 891-892; index 'Cervini litterae' p. 953).
- **2491.** greekarchivesinventory.gak.gr page fetched: holder 'Μουσείο Μπενάκη, Τμήμα Ιστορικών Αρχείων', Αρ.Εισ. 176,
  287 documents and 71 photographs, 1891-1939, provenance Natalia Mela, source Tselika, *Οδηγός Ιστορικών Αρχείων Μουσείου Μπενάκη*
  (2006). The Makedonika article (ejournals.epublishing.ekt.gr) is behind Cloudflare.

## Prior-art checks run this pass
- cryptiana unsolved.htm and GL.htm fetched once, grepped for Pokotilov, Witte, Davydov, Babou, Angoulême, Elizabeth,
  Rusdorf, Villa, Garza, Maximilian, Contarini, Cervini, Melas, Morgan, Lilly and Gregoriana. Only unrelated hits: a Babou
  father-son cipher in Dupuy 44, Rusdorff to Oxenstierna 1628, Villars and Villeroy.
- known.py on 'Ф. 560'+'Pokotilov', 'Benaki'+'Melas', 'Morgan Library'+'Angoul', 'Morgan'+'Elizabeth',
  'de la Garza'+'Villa', 'Lilly'+'Maximilian', 'Concilio di Trento'+'Contarini'/'Cervini'. No duplicate: only the
  leads themselves and their RGIA/APUG sibling leads.

## Record errors found
- 1864: date is May-Aug 1905 (case 1904-1905), not 1904.
- 2491: the holder is the Benaki Museum Historical Archives (Ar. Eis. 176), not GAK Central Service. The GAK inventory only aggregates it.
- 2071: 'Marchais' is not a place of writing. The Morgan record reads 'Marchaux', and Ribier's 14 Aug letter gives no place;
  the king was camped beyond the Somme.

## Bot checks met (for the next sweep)
prlib.ru (Security Check), themorgan.org (403 Cloudflare), archives.iu.edu (403; Wayback works), gate.unigre.it (Cloudflare),
ejournals.epublishing.ekt.gr (Cloudflare). fgurgia.ru is now open to curl through its /ajax/obj API.

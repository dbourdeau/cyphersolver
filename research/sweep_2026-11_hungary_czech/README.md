# Sweep: Hungary, Czech lands, Slovakia (2 Nov 2026)

22 rows in `candidates.json` (built by `make_candidates.py`). All are leads, none vetted: **the user ruled out web search for
this pass**, so the only prior-art check is `known.py` on names and shelfmarks (no hits for any row). Tomokiyo, Lasry,
DECODE's own site search, editions and literature were not searched. The target of 60 rows was not reached, and nothing is padded.
Every row is scored from a catalogue description; no image was opened.

## Where the rows came from

- **Archives Portal Europe, JSON endpoint.** The search page loads `/get-results/?term=<t>&section=search-in-archives&sort=Relevance&context=listTab&page=<n>&using=default`
  (same-origin `fetch` in Chrome, 2.5 s between pages, 10 records a page). The portal's reCAPTCHA call was never touched. This reaches the
  Hungarian National Archives (MNL OL, repository HU-1) at item level, including the DF photo collection of Italian archives and the
  "MNL Hungarika" abstracts of foreign holdings.
- **Hungaricana** full text (`/hu/search/results/?list=<base64 JSON>&page=<n>`, JSON with `\uXXXX` escapes). 668 hits for "rejtjeles levél":
  almost all newspapers; the usable ones are printed MNL finding aids (rows for the Esterházy, Teleki, Kamara, Rákóczi-War series).
- Terms run on APE (hits): rejtjeles 19, rejtjel 74, titkosírás 141, titkos írás 8, titkosírással 13, rejtjelezett 17, zifara 10, cifera 3,
  chifre 25, šifra 31 (all Baltic/Latvian, none Czech), šifrovaný/šifrovací/šifrované/šifry/šifrové 0, Chiffre 7,864 (global, only 30 read),
  cifre 1,293 and chiffré 579 (global, 40 read each, noise). A search on `cifra`, `Geheimschrift`, `chiffriert`, `tajné písmo` timed out and was not redone.

## Best leads

1. **MNL OL P 396 (Károlyi family), nos. 11214, 699, 9027, 7950-7952, 10924**: Rákóczi-war letters flagged as cipher, with the key
   sheets 379, 11345, 10543 in the same fonds. Best key route in the sweep.
2. **Nedeczky and Fogarasi, Rákóczi's envoys (G 15)**: "largely cipher", keys available per Iványi 1954.
3. **MNL OL R 316 item 27 (1530)**: cipher papers and key filed together.
4. **MNL OL P 1238 I.17.102 + II.1** (Teleki): cipher or unsigned letters with 15 key sheets.
5. **Nicolò Bartolini, 1491-92 (DF 295070/73/143/273)**: new correspondent in the Maffeo da Treviglio / Sforza files (buda1489).

## Key leads (bare keys, not rows)

MNL OL P 396 nos. 379 (cipher key, 4 July 1704), 11345 (keys for the Rákóczi ciphers), 10543 (decipherment keys, 4 fols.);
X 1554 (R 117), Vetter Antal's cipher key and a decipherment fragment, 1848-50; DF 293290 (Giovanni Francesco Oliva and Guidoantonio
Arcimboldi, cipher key, 27 Feb 1488, addressed to Matthias Corvinus); AAV Segr. Stato Germania vols. 221-222 (1695-1700), deciphered
nuncio reports (key route for vol. 219 and the Vienna nunciature).

## Excluded as already tracked or already read

Sadoleto 1482-83 (sadoleto1482), Maffeo da Treviglio 1489-90 (buda1489, catalogue 1235), Lanterio 1490-92 (buda1489), Beatrice d'Aragona
1482-86 (beatrice1482, beatrice1486), Caprile 1519-21 (caprile1519, caprile1520; DF 294931 = R1136, DF 294977 = R1139), Valentini 1486
(DECODE R1119, R1121, `research/oldest`), Bonzagni 1512 (bonzagni1512), Costabili 1491-92 six despatches (catalogue 361; the row here covers the
remaining DF numbers only), Ferdinand → Castaldo 1552 (catalogue), Bakócz-Maffeo DL 46150 (catalogue 1235), the Esterházy box 636 of 1744 (catalogue 344,
esterhazy1744). Left out because a decipherment sits with the item: Bartolomeo di Brescia 1486 (DF 294352-b), Kriegsarchiv 1706 letter and its
solution (Filmtár p. 125), Sadoleto "feloldás" leaves. Left out as not letters or after 1945: Országos Rejtjel Központ 1953-90, XIX-J-1-z, MSZMP papers,
newspaper hits, DL 64920 and DL 91802 ("titkos kancellár" is an office, not cipher).

## What blocked, and what was not reached

- **Czech lands: nothing.** APE returns no Czech record for any cipher term. The Národní archiv and the Moravian archives expose no public
  item-level search that reaches a letter; `badatelna.eu` is now a casino spam site; `manuscriptorium.com` is a codex aggregator whose search page 404'd on
  the URL tried and was not explored further (a cookie banner was declined). Czech terms searched on APE: šifra, šifrovaný, šifrovací, šifrované, šifry, šifrové.
- **Slovakia: nothing new.** The Slovak aristocratic-family ciphers (Esterházy, Pálffy, Üchtritz) are already in the repo through the HistoCrypt 2023 paper; the
  Slovak National Archives have no item-level portal reached here.
- **Hungary:** MNL OL's own portal (`archives.hungaricana.hu`, `mnl.gov.hu`) was not tried directly; APE's mirror was enough for the DF and P/R fonds. Not read: cifra,
  Geheimschrift, chiffriert, Latin "cifris/cyphratae", Hungarian "megfejt", "kulcs", "rejtjeles" beyond APE page 2 for the 1,293-hit cifre set. Not searched: Hungaricana's
  "Levéltári" database (a separate item-level index), MNL OL fonds descriptions for R 316 and P 108 (the fonds numbers P 108 and G 15 are partly from memory of MNL's
  numbering; the P 108 row says so), the DF "Digitális" images (none opened), Slovak Pálffy archives, Czech family fonds (Kinský, Schwarzenberg, Lobkowicz) by
  finding aid.
- The Hungarian sweep tab froze once during a ten-term loop (45 s); loops of three terms ran cleanly.

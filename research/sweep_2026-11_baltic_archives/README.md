# Baltic archives sweep (9 Nov 2026): Estonia, Latvia

Result: 1 weak row (cls B, 1907) in `candidates.json`; `key_leads.json` holds one administrative note. Chrome not used.

| Source | Route | Result |
|---|---|---|
| Europeana API (`api2demo`, `qf=COUNTRY:estonia` / `latvia`, 25 terms in et/lv/de/ru/en) `eu.py`, `eu_hits.json` | works | 8 records, all noise (Tartu GPU block-cipher paper, museum "sifr" inventory numbers, Master Sigfrid Lander, Keila churchyard). Latvia: 0 hits. |
| Estonian AIS `ais.ra.ee/et/description-unit/search?q=` (`ais_ee.py`, `ais_ee_hits.jsonl`) | works (exact-word match unless `*`) | 60+ more terms on top of the 2 Nov sweep (Chiffre/Ziffern/Geheimschr*/cifr*/chiff*/salakirja*/salakiri/sifreeritud/шифров*/цифр*/secret*/Schluessel). All pre-1900 hits are administration (Russian MVD cipher circulars 1863, 1881 key introduction EAA.29.2.5365, 1901/1910 student-unrest "ciphered telegrams" EAA.325.1.1000/1035, 1913-14 EAA.1445.1.64) or noise (Ziffern tables, Schluessel keys, Rossillon letters to V. Chifflard). One real item: AM.272.1.97 (Mihkel Sild, 1905 account "salakirjas", 1907, 19 ll.). 20th-c.: ERA.1868.1.90 (1938 prison letters of Julius Mitt in secret writing, deciphered by the prison), ERA.669.1.20 and EAA.402.11.18 registers of incoming "salakirjad" 1913-19, EAA.2548.1.1038 key-of-secret-writing 1930-31: not leads. |
| digar.ee / dea.digar.ee | 403 (Cloudflare) | not swept, OAI blocked too |
| raduraksti.lv, lvva-raduraksti.lv, arhivi.lv, dspace.ut.ee, tlaarhiiv.ee | no connection (curl 000) | not swept (Latvia's LVVA is unreached) |
| gramatas.lndb.lv, periodika.lv | 200 but no search API probed | not swept |

Tallinn City Archives (TLA fonds) and the Estonian Historical Archives (EAA) are inside AIS, so they were covered by the AIS terms. The Hanseatic Reval letters (TLA.230.1-I) came up only for "sub secreto" (seal).

Left: Latvian State Historical Archive and Riga city archive (host unreachable from this machine; try Chrome later), DIGAR (Cloudflare), Tartu University Library, periodika.lv full text.

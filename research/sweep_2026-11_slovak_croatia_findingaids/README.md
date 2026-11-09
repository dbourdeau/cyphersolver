# Slovak, Croatian, Slovenian, Hungarian finding aids (9 Nov 2026)

**Result: 0 rows in `candidates.json`, 0 in `key_leads.json`.** Nothing was padded.

## Routes
- **minv.sk PDF finding aids**: reachable by curl (browser UA). The site has no crawlable index of aids (`?zoznam-archivnych-fondov...` links one list file only);
  PDF URLs came from web search with `allowed_domains: minv.sk` (path patterns `swift_data/source/verejna_sprava/<archive>/...`). All have a text layer.
- **dlib.si**: home answers 200, but `/results/` is a JavaScript app (no hits in the static HTML); not scripted.
- **hrcak.srce.hr** 200 (not searched by script). **arhiv.hr** 301, **arhiv.gov.si**, **arhinet.arhiv.hr** no connection from this network.
- **Hungaricana (archives/library)**: 403 to curl; needs Chrome (earlier `sweep_2026-11_hungary_czech` already ran Hungaricana and APE in Chrome). Not repeated.

## Grepped (regex šifr/ifrov/Chiffre/rejtjel/kryptogr/Geheimschrift, `grep_pdfs.py`): 0 hits in all 12
Bytča: Rodové archívy 1334-1964 (2186), 584, 116, Illésházy-Trenčín archív prefekta (718) and Trenčín časť 1; SNA Esterházi-česnecká línia repertórium (250+ pp.);
SA Nitra Zbierka listín novoveká 1540-1874; SNA Brunsvik-Chotek; SA Prešov Drugeth (900 pp.); SA Bratislava inv. 63 (350 pp.); SA Košice Rodové archívy I (192 pp.);
SNA Pálffy-Devín. This confirms the earlier remark that Slovak aids rarely flag ciphers; the known Slovak ciphers (Antal et al. HistoCrypt 2023, Esterházy čeklíska
vetva, Amade-Üchtritz) were found by reading the boxes, and are already rows in `sweep_2026-11_mirka_cryptoworld`.

## Web searches (about 10, Slovak/German/Croatian/Slovenian/Hungarian terms)
No finding-aid entry, article or edition naming a ciphered letter in a Slovak, Croatian (HDA, Dubrovnik DADU, Zrinski-Frankopan fonds) or Slovenian family archive
(Turjaški/Auersperg, Attems, Lamberg). Only Vrančić brothers' ciphered letters (hrcak article, Croatian, already treated in the literature) and Láng's Hungarian survey turned up.

## Left
- Remaining minv.sk aids unfetched: other SNA family fonds (Zay, Révay, Erdődy, Zichy, Csáky not located as separate PDFs), SA Banská Bystrica/Levoča family fonds.
  Because the aids do not flag ciphers, the yield is likely nil; box reading (HistoCrypt authors) is the route.
- dlib.si and hrcak need Chrome with the site's own JS search (terms: šifra, tajnopis, šifrirano, kriptogram).
- Hungaricana full text in Chrome (rejtjel*, titkosírás) was done by an earlier sweep.
